# 生存模拟：功能与操作
> 实际规则可能受服务器配置影响。


炽天使：生存模拟 **1.0.3**，适用于 Vintage Story 1.22.x。客户端与服务端均需安装主包；可选客户端调试包需要 VSImGui 1.2.7。[模组清单](/mods/entries/vsslssmod)的版本号反映整合包实际安装包，使用本页功能前请核对是否已更新。

## 功能

- 营养与消化：热量、六项营养储备、电解质及可搜索的食物营养手册。
- 饮水与水质：水分吸收、污染传播与消退、过滤、煮沸、蒸馏和井水。
- 体能与休息：耐力、劳动疲劳、肌肉训练、睡眠与营养增益。
- 体温与环境：日晒遮阳、衣物、风雨、浸水换热、失温与冻伤。
- 伤病与急救：伤口、出血、绷带、按压止血、免疫与疾病。
- 卫生与污染：排泄、洗浴、整组果蔬清洗、腐败物污染及 Real Smoke 气体联动。
- 生存设施：井、浴桶、导流锅、过滤锅、烟囱、肥皂、堆肥与围石篝火。
- 状态界面：原生角色面板、人体部位图、状态提示和中英文游戏内手册。

各功能的计算常量与公式见[公式与单位](/develop/formulas)，C 键和文明窗口见[窗口与面板清单](/guide/windows)，可查阅各项单位、变化原因与显示规则。

## 食品手册与营养显示

食品手册支持同一物品的不同属性变体；餐食和馅饼按实际配料预览。馅饼按每片显示，一片是整只的四分之一；液体容器显示每升内容物的营养，不把空容器当成食品。物品提示中的馅饼营养也按实际配料和剩余份量计算。

手册提供可用饼皮与单一馅料的烤熟馅饼预览，包括开放式和盖顶式，标明面团类型；点击预览可查看对应配方。搜索“派”也可匹配“馅饼”。预览不穷举任意混合馅料，实际制作的营养仍以实际内容物为准。

乡野烹饪的大块熟肉按剩余块数折算营养，默认完整大块为六块；切走部分后，食用和后续加工均按剩余比例计算。

## 围石篝火

先把原版篝火建造完成并熄灭，手持一叠至少 **12 块散石**，按住 **Shift + 右键**完成升级。一次消耗 12 块散石，创意模式免消耗；领地权限仍需允许操作。已经升级的篝火不能重复升级。

升级保留原有燃料、食物、温度与烹饪结构，燃料燃烧时长为原来的 **1.3 倍**。拆除时返还投入的散石，篝火内物品继续按原版拆除规则处理。

## 操作与指令

按 `C` 查看角色，按 `H` 阅读手册；文明核心菜单的肉图标打开营养手册。对水源按住 `Shift + 右键` 约 3 秒饮水，手持果蔬时清洗整组。按住 `P` 按压止血，`K` 闭眼休息，`Shift + V` 排泄；快捷键可在设置中修改。

| 指令 | 用途 |
| --- | --- |
| `/vsslssmod`、`/vsslssmod check` | 查看自身状态、指标与行动限制 |
| `/vsslssmod cancel` | 取消护理动作 |
| `/vsslssmod drink`、`/vsslssmod pressure`、`/vsslssmod clean` | 查看饮水、止血和清洗操作提示 |
| `/vsslssmod mode survival\|shadow\|observe` | 管理员切换模拟模式 |
| `/vsslssmod compat`、`/vsslssmod probe` | 管理员检查兼容与运行状态 |
| `/vsslssmod speed <倍率>` | 查看速度配置提示；生理速度设置与原版日历速度不是同一项 |
| `.vsslssmodhud` | 开关人体部位图 |
| `.slssdebug`、`.slsspollution` | 开关活动调试、污染范围显示 |
| `.slssperf start\|stop\|status` | 性能采样，默认采样 60 秒 |
| `.vsslssmod debug` | 打开可选调试窗口，也可按 `Ctrl + Shift + V`；修改状态需要管理员权限 |

## 配置

配置由服务器管理员维护；玩家无需修改配置文件。详见[管理员入口](/admin/)。

<details><summary>技术说明</summary>

以下 `ModConfig` 路径相对于游戏数据目录。手动修改后重启服务端；无效配置会拒绝加载并保留原文件，旧测试版存档和配置不自动迁移。

| 文件 | 用途 |
| --- | --- |
| `ModConfig/vsslssmod.Server.json` | 首次运行生成的服务端配置 |
| `ModConfig/vsslssmod.Foods.json` | 可选食物数据覆盖；以主包内 `assets/vsslssmod/config/foods.json` 为模板 |
| `assets/vsslssmod/config/compatibility.json`（包内） | 内置兼容目录，用于诊断 |

常用服务端配置（完整字段以生成文件为准）：

| 字段 | 默认值 | 作用 |
| --- | --- | --- |
| `Mode` | `survival` | `survival` 应用生理效果；`shadow` 仅模拟；`observe` 不推进模拟 |
| `EnableClinicalEffects` / `EnableMovementEffects` | `true` | 生理状态与移动影响 |
| `EnableSymptomVisuals` | `true` | 症状视觉效果 |
| `EnableGroundWaterDrinking` / `EnableMedicalActions` / `EnableDefecation` | `true` | 水源饮水、护理、排泄 |
| `DrinkServingL` / `DrinkCooldownRealSeconds` | `0.25` / `3` | 每次饮水量（升）与冷却（现实秒） |
| `DigestionGPerGameHour` | `1667` | 每游戏小时食物消化量（克） |
| `Digestion.WaterMlPerHour` / `Digestion.WaterHalfLifeHours` | `2000` / `0.3333333333333333` | 每游戏小时吸水上限（毫升）与胃水吸收半衰期（小时） |
| `SolarPowerWAtFullExposure` | `500` | 完全暴露时的日光热量（瓦） |
| `ClothingCloByCode` / `HeadgearShadeByCode` | `{}` | 衣物保暖值与头饰遮阳比例（0–1），按物品代码指定 |
| `SurfaceWater` / `DiseaseExposure` / `Sanitation` | 配置对象 | 天然水、疾病暴露与卫生污染参数 |
| `Exertion` / `ThermalAdaptation` / `Pain` / `Circulation` | 配置对象 | 劳动、热适应、疼痛与循环参数 |
| `TelemetryEnabled` / `CheckpointSeconds` | `false` / `30` | 遥测开关与存档检查点间隔（现实秒） |

</details>

## 作者与授权

作者：HansJack、ch4Ver、buzidao9、Zhiketangjiang2、KitamuraEri。

项目代码采用 MIT；素材和第三方内容分别遵循原作者授权，参见项目随包许可说明。
