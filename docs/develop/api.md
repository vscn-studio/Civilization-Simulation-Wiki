# 开发者 API 与兼容接入

适用于生存模拟 **1.0.3**。接口版本为 V1；清单中的版本号用于核对实际安装包，使用这些接口前请确认主模组已更新。

入口：`api.ModLoader.GetModSystem<Seraph.SeraphModSystem>()`，版本常量 `SeraphModSystem.DeveloperApiVersion == 1`。参数类型主要位于 `Seraph.Api`、`Seraph.Server`、`Seraph.Core.Framework`。在附属模组 `modinfo.json` 中声明对 `vsslssmod` 的依赖；引用主包的 `vsslssmod.dll`、`vsslssmod.Core.dll` 和 `vsslssmod.Application.dll`，不要把这些 DLL 再打进附属包。

## 调用约定

- 在附属模组的 `Start` 中注册，`ExecuteOrder()` 返回大于主模组默认值 0.1 的数，例如 1。水、衣物、污染源和环境提供者必须早于主模组的 `AssetsFinalize` 注册。食物支持在 `Start` 或 `StartServerSide` 注册，服务端在进入 `RunGame` 时关闭食物注册，客户端在 `AssetsFinalize` 时关闭。水、衣物应在客户端和服务端都注册。游戏本身的物品、方块和配方仍需正常注册。
- 新增 API 的游戏状态查询与写入必须在对应游戏线程调用；服务端写入不能由客户端直接调用。后台任务通过游戏的 `EnqueueMainThreadTask` 调度。外部网络请求的身份、距离、权限、物品和操作完成情况由附属模组验证。
- `V1` 表示接口版本，不是模组版本。普通参数错误抛出 `ArgumentException`；错误调用线程、端或生命周期抛出 `InvalidOperationException`。运行期动作返回 `ApiResultV1`，拒绝原因是机器可读字符串。
- 返回的食物资料、配置、玩家状态、客户端快照都是副本。不要靠修改副本改变游戏状态；不要直接编辑存档、保留槽位或网络消息。频繁 HUD 绘制应缓存快照。
- `ActionReceiptV1(Source, Sequence)`：`Source` 使用 `myaddon:eating` 等精确命名空间代码，`Sequence` 为正且严格递增。同一玩家连接内每个来源只接受比上次更大的序号，最多 128 个来源；重生不清空，重连后重建。所有动作共享这个来源序号空间，建议不同动作使用不同来源。回执不是持久事务日志；尝试进入提交后，即使失败也使用新序号重试。
- 原版进食、已适配餐食、饮水、伤害和劳动已有自动接入。**仅对未自动接入的自定义动作使用记账接口**；回执去重不能识别另一个原版钩子已经计入的同一次操作。

## 食物与制作流程

| 接口 | 用途 |
| --- | --- |
| `RegisterFoodV1(FoodProfile, replaceExisting = false)` | 增量注册精确物品代码，支持一个资料对应多个代码；不同附属注册不能重复。同已有资料冲突默认报错，显式替换只移除冲突代码，保留同资料的其他代码 |
| `GetFoodProfileV1(stack)` | 返回该物品的物理营养资料，优先读取物品保存的实际制作营养；未映射返回 `null` |
| `GetFoodNutritionV1(stack, quantity = 1, litres = false)` | 普通食物营养查询；数量单位为物品份数，`litres = true` 时为升；传液体内容物而非桶/瓶 |
| `GetMealNutritionV1(meal, servings = 1)` | 原版机制餐食和馅饼，按实际内容物及食用份数计算，返回餐食代码，食用量须在剩余份数内 |
| `ComposeFoodV1(output, ingredients, processing = null)` | 只计算自定义配方结果，不修改物品、不消耗材料 |
| `SetFoodIngredientsV1(output, ingredients, processing = null)` | 服务端计算并把每件成品的营养保存到物品，支持自定义合成、烘烤、干燥和切分 |
| `SetFoodCompositionV1(output, profile)` | 服务端保存附属模组已计算的每件成品营养，资料必须只对应该成品代码 |
| `GetFoodCapacityV1(player, food, quantity = 1, litres = false, meal = false)` | 返回当前最多可接受的比例 0–1；`meal = true` 时数量是餐食份数 |
| `RecordFoodIntakeV1(player, receipt, consumed, quantity = 1, litres = false, meal = false)` | 自定义进食的确认记账，进入原有消化、营养、污染及病原流程；不扣物品，不写原版饱食度作为营养 |
| `GetNutrientsV1()` | 当前有效营养 ID、单位及储备定义；不包含不参与玩法的 D/K 保留槽 |

食物资料使用现有 `FoodProfile`：`PortionG` 是每件可食部分克数；`WaterGPer100G`、`AlcoholGPer100G` 和 `Per100G` 的碳水、蛋白质、脂肪、纤维使用克/100 克。钠、钾为毫克/100 克。`MicroPer100G` 支持 `calciumMg`、`ironMg`、`zincMg`、`vitaminAUgRAE`、`vitaminCMg`、`b1Mg`、`b6Mg`、`folateUgDFE`、`b12Ug`，键名指定毫克或微克。缺少某项表示未知，显式 0 表示已知为零。`FoodInfoV1.Nutrients` 的微量营养结果是游戏储备点，单位 `%`，不是物理毫克；能量结果为 kJ，乘除关系为 `kcal = kJ / 4.184`。

查询、容量检查、进食记账和配方原料都要求升数对应具有有效 `watertightContainerProps.itemsPerLitre` 的液体份额物品。固体使用物品数量，餐食使用份数，`meal = true` 与 `litres = true` 同时传入会报错。馅饼整只为 1 份、每片为 0.25 份。缺少 `quantityServings` 时按 `pieSize / 4` 读取，显式保存的剩余份数优先。

`FoodIngredientV1(Stack, Quantity, Litres = false)` 表示**实际消耗**的食材。所有原料必须有资料，未知原料会拒绝整个计算。Rustic Cookery 大块肉按剩余 `pieces / 6` 同步折算进食与加工营养，缺少 `pieces` 时视为完整六块。`output.StackSize` 是本次生成的总件数，须使用本次独立产物堆。

`FoodProcessingV1(FinalMassG, Heat, MicronutrientRetention)`：最终重量是整批重量，只允许通过减水降低重量；加水必须列为原料。`Heat = true` 对尚未烹饪的资料应用默认维生素保留率；已标记熟制的输入不会重复默认扣除。指定 `MicronutrientRetention` 时按本次工序应用给定的 0–1 保留率，未列项保留 100%。复杂多次加工可显式指定每一步保留率。物理营养结果会保存在成品中，下一步可继续把它当原料。

这里保存的是营养组成，不会替其他模组完成其库存扣除、生成成品、原版饱食度设置或变质时间转换。加工后的表面病原、原料残渣和产率由加工设备明确处理，使用病原读写接口；不要假设任意加工会自动灭菌。设置元数据后由调用方对相应物品槽 `MarkDirty()`。

```csharp
using Seraph;
using Seraph.Api;
using Seraph.Server;
using Vintagestory.API.Common;

public sealed class MyAddon : ModSystem
{
    public override double ExecuteOrder() => 1;

    public override void Start(ICoreAPI api)
    {
        var slss = api.ModLoader.GetModSystem<SeraphModSystem>();
        slss.RegisterFoodV1(new FoodProfile {
            Codes = ["myaddon:onionbread"], PortionG = 150,
            Preparation = "cooked", WaterGPer100G = 40,
            Per100G = new() { ["carbohydrate"] = 40, ["protein"] = 8, ["fat"] = 5 },
            MicroPer100G = new() { ["vitaminCMg"] = 3 }
        });
    }
}
```

在服务端自定义设备确认完成制作、拿到本次成品后：

```csharp
// onionBefore / doughBefore 是消费前保留的原料副本，数量是实际扣除量。
slss.SetFoodIngredientsV1(output, [
    new FoodIngredientV1(onionBefore, 2),
    new FoodIngredientV1(doughBefore, 1)
], new FoodProcessingV1(FinalMassG: 300, Heat: true));
outputSlot.MarkDirty();
```

自定义进食在同一服务端回调中：保留食物副本 → `GetFoodCapacityV1` 检查 → 成功扣除对应食物 → `RecordFoodIntakeV1`。只记录实际吃下的数量，失败由调用方恢复库存。原版机制馅饼直接由原版进食路径计入，不需要额外调用。

## 水质、处理与污染

| 接口 | 用途 |
| --- | --- |
| `RegisterWaterV1(liquidCode, defaults)` | 注册其他模组的水份额物品，必须具备有效 `watertightContainerProps.itemsPerLitre`；默认 `WaterBatch.VolumeL` 不决定物品实际水量 |
| `ReadWaterV1(liquid, ambientC = 15)` | 读取水质与温度，实际水量由物品数量/每升单位数决定；不支持的液体返回 `null` |
| `WriteWaterV1(liquid, water)` | 服务端写入水质，水量必须等于物品实际水量；不支持的旧元数据不会被覆盖 |
| `TryDrinkWaterV1(player, receipt, available, servingL, take, restore)` | 自定义水池/设备饮水事务；先检查容量、温度、盐度和冷却，再调用 `take(实际升数)`，失败时恢复库存与生理状态 |
| `GetWorldWaterV1(position)` | 查询天然水体当前水质，不取水；无可用水源时返回 `null` |
| `GetPollutionV1(position)` | 查询当前位置的粪便、动物、腐尸、烟与无机污染负荷 |
| `RegisterPollutionSourceV1(blockCode, profile)` | 注册放置的实体层方块污染源，参与已有范围传播、水体残留和消退流程；负荷叠加到已有来源，附属声明明确病原 ID |
| `NotifyWorldChangedV1(position)` | 自定义放置、移除、封闭或污染源变化后通知失效缓存；按需重新扫描，不同步扫描整片世界 |
| `ReadPathogensV1(stack)` / `WritePathogensV1(stack, perItem)` | 读取/写入每件物品的表面病原强度；写入替换原有字典，叠加时先读取再合并 |
| `ReadHerbalWater(liquid)` | 保留已有草药模组兼容入口；新代码可用 `ReadWaterV1` |

`WaterBatch` 的体积单位是升、温度为摄氏度、盐度为克/升，病原与普通肠道风险为每升游戏强度，浑浊度为 0–1。`RegisterWaterV1` 接入使用统一水质识别的功能，但不会自动改写第三方容器自行实现的代码比较或传输规则。

原版容器倒入已注册水时保留其物品代码与每升单位数。同种注册水可以反复倒入并混合水质。不同注册水之间，以及注册水与原版水之间会拒绝混入。原版淡水与盐水继续按混合盐度选择原版水物品。

纯计算方法已经公开在 `Seraph.Core.Framework`，无需访问内部存储：

| 接口 | 用途 |
| --- | --- |
| `WaterBatch.Mix(other)` | 按水量加权混合 |
| `WaterHeating.Advance(water, furnaceC, seconds)` | 加热、消毒和蒸发，返回水质与蒸发量 |
| `WaterHeating.Evaporate(water, litres)` | 蒸发与浓缩 |
| `WaterFiltration.Process(input, layeredFilter, cloth)` | 分层过滤/布过滤，保留溶解盐 |
| `WaterDistillation.Separate(input, consumedL)` | 返回剩水、蒸馏水与析盐克数 |
| `PathogenLoads.Add` / `Scale` / `Mix` | 已有病原强度的合并、缩放、加权混合 |

这些方法不扣燃料、不消耗滤材、不生成盐、不改变容器库存；设备必须根据计算结果同步实际水量和产物，再写入水质。

饮水 `take` 回调必须只扣除指定水量，成功返回 `true`；`restore` 必须能幂等地恢复调用前状态。两者不能再次调用饮水 API；异常会向调用方传播，主模组始终回滚本次生理修改。`available` 必须是当前可用水量和水质，不是已经取出的份额。

## 玩家、体能、环境与伤病

| 接口 | 用途 |
| --- | --- |
| `GetPlayerStateV1(player)` | 服务端查询体温、水分、消化、营养储备、耐力、疲劳、肌肉、伤口、疾病、卫生和环境的完整副本；未建立会话返回 `null` |
| `GetClientSnapshotV1()` | 客户端查询本地玩家最近一次同步的显示快照；握手前返回 `null` |
| `GetServerConfigV1()` | 查询服务端配置副本，不修改配置文件 |
| `PlayerStateChangedV1` | 服务端正常状态推送时的通知事件；每个订阅者收到独立副本，订阅者异常不打断其他订阅者 |
| `RegisterClothingV1(itemCode, profile)` | 指定衣物 clo 保暖值和 0–1 遮阳比例；遮阳仅用于头/脸/头盔槽，服务器逐物品配置优先 |
| `RegisterEnvironmentV1(providerCode, provider)` | 修改每次服务端采样后的环境边界：气温、辐射、风、日晒、湿度、浸水、污染等；回调返回 `null` 表示保留当前值 |
| `RecordWorkV1(player, receipt, activity, realSeconds)` | 把确认发生的自定义劳动接入耐力、负荷、疲劳和训练；单次 0–60 现实秒，不接受 0，不重复申报原版已有劳动 |
| `RecordExposureV1(player, receipt, route, hazard)` | 提交一次已有病原的摄入、皮肤或吸入暴露，继续经过屏障和免疫，不直接判定患病 |
| `RecordInjuryV1(player, receipt, injury)` | 自定义伤口：部位、类型、严重度、出血速率与证据；不会额外扣原版 HP，也不要重复提交原版伤害已生成的伤口 |
| `GetDiseasesV1()` | 获取现有疾病 ID 和定义；不允许直接向全局疾病表写入新 ID |
| `RecordPlantContact(player, source, severity)` | 保留已有明确植物接触入口 |
| `OpenNutritionHandbook()` | 客户端打开营养手册 |

环境回调按提供者代码的序数顺序执行，接收前一结果的副本。无效结果或异常会停用该提供者直至重新加载并记录一次日志，其余提供者继续运行；不要在回调中执行世界扫描或等待任务。

`RecordExposureV1` 输入为本次总 hazard（不是百分比、每秒值或屏障单位），单项范围 0–100，使用 `GetDiseasesV1` 返回的 ID。按持续时间采样的附属模组须先乘自己的已验证持续时间。伤口严重度为 0–1，出血为升/秒（0–0.01），部位使用 `Anatomy` 定义的代码。普通攻击仍应使用游戏原生伤害 API；有准确部位的伤害来源可实现已有 `Seraph.Application.IVerifiedInjuryLocation`。

新增生理动作仅在主模组负责的有效存活生存玩家会话中执行，并遵循暂停、相关功能开关和行动限制。查询不改变这些限制。状态事件应作为观察入口；在附属模组 `Dispose` 中取消订阅。

## 治疗接口

| 接口 | 用途 |
| --- | --- |
| `RegisterTreatmentV1(itemCode, TreatmentDefinition)` | 注册固定单件剂量、给药途径、效果及使用要求 |
| `QueryTreatment(player, slot, route)` | 不消耗物品的可用性检查 |
| `BeginTreatment(player, slot, route)` | 开始服务端治疗动作 |
| `ContinueTreatment(player, slot)` | 持续操作时续期并检查移动、死亡、目标变化等中断条件 |
| `CompleteTreatment(player, slot)` | 完成后扣除一件药物并应用效果，重复完成不重复扣药 |
| `CancelTreatment(player)` | 取消未完成动作 |

旧 `RegisterTreatment` 会抛出异常，必须使用 `RegisterTreatmentV1`。治疗定义的生理持续时间按游戏秒，使用动作/心跳时序按现实秒；以 `TreatmentDefinition` 字段说明为准。已有公开 Core 类型中的算法方法可以离线计算，但不会自动连接游戏：`IRoomEnvironmentAdapter`、`IExposureAdapter`、`IInjuryAdapter` 等早期声明不等于已经安装的运行时注册入口，应使用本页的版本化入口。
