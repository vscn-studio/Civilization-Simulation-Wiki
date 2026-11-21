# 望远镜

Spyglass Fork · 模组代码：spyglassfork

> 来源：整合包安装包 `Spyglass Fork-0.6.4.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `spyglassfork` |
| 版本 | 0.6.4 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.3 |
| 作者 | Fuami, HansJack |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Spyglass compatibility fork for Vintage Story 1.22.3–1.22.7. Original mod by Fuami; fork maintained by HansJack. MIT License, Copyright (c) 2021 Fuami; see LICENSE and NOTICE.txt.

</details>

作者提供的链接：https://github.com/fuami/Spyglass

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

````text
# Spyglass Fork

Vintage Story **1.22.3–1.22.7**，模组 ID：`spyglassfork`，版本：`0.6.4`。
原作者 **Fuami**，分支维护者 **HansJack**。保留原 MIT 许可证及
`Copyright (c) 2021 Fuami`；安装包包含完整 [LICENSE](LICENSE) 与 [NOTICE.txt](NOTICE.txt)。

修复第三人称禁用缩放时仍遮罩/隐藏人物和 HUD、服务端遮罩同步后信息栏未隐藏、
Scribe 任务 HUD 未隐藏、玩家尚未就绪时的空引用及退出后静态状态残留。
服务端配置到达后会重新构建遮罩；零距离插值不会再产生 NaN。

客户端与服务端都需安装。请用本分支替换原版，避免两个相机补丁同时生效。
本分支使用 `assets/spyglassfork`、`spyglassfork.json` 和独立网络通道。
物品代码变为 `spyglassfork:spyglass-*` / `spyglassfork:spytube-*`，旧版物品和配置不会自动迁移。

默认遮罩是方形镜片（`vignetteStyle: "square"`），也可设为 `"none"` 关闭遮罩；圆形轮廓已移除。
方形视野默认边长为原来的 1/2、面积为原来的 1/4（`lensSize: 0.5`），并保持屏幕居中。边长计算为 `(屏幕短边 - edgeSize × 2) × lensSize`，`edgeSize` 默认为 10 像素。金属主体宽度为 21.6 像素，宽度独立于视野大小；已移除金属框旁的粗黑描边，镜片可视区域每侧扩大约 13 像素，水痕同步覆盖扩大后的区域；镜片外的眼罩和金属均完全不透光，旧 `edgeOpacity` 字段仅保留兼容。遮罩按选定倍率归一化淡入淡出，避免静止时仍透出场景。按 F4 隐藏界面时仍保留望远镜遮罩。
配置文件位于 `VintagestoryData/ModConfig/spyglassfork.json`。镜片外沿直接复用物品模型的 `game:block/metal/ingot/{metal}` 纹理，采用像素采样与较柔和的暗面，随游戏光照调整明暗，并支持材质包替换。镜片直接使用原版玻璃纹理、颜色和透明度，移除人工随机像素斑点；石英及烟色玻璃保留原版的纹理差异。已有配置可添加 `lensSize: 0.5`，省略时也使用此默认值；开启 `overrideClientConfig` 时，服务端会同步视野大小。

镜片配方仍为竖排「同金属镜筒半件 → 玻璃块 → 同金属镜筒半件」。普通玻璃制作原有望远镜；石英、绿、蓝、紫、红、黄、棕、复古、烟色、粉色玻璃分别制作对应镜片版本，手持模型与观察画面共用该原版玻璃贴图。已有 `spyglass-{metal}` 物品保留，默认普通玻璃；新增版本代码为 `spyglass-{metal}-{glass}`。不同镜片只改变外观、色调与透明度，不增加夜视或缩放奖励。

镜片雨水参考 **Anti-Productivity RainyGlass（APRG）**：细小水珠附着在落点，大水滴克服附着力后向下流淌，途中会停顿、轻微偏移、拉长并与接触的水滴合并。大水滴吸收沿路细珠，留下不规则的细水痕和零星残珠；水滴流出镜片后，水痕仍会保留并独立变淡。水痕通常数秒至十余秒消退，附着水珠在持续观察、雨停后约 45 秒渐隐。水下清除全部镜片雨水，雪和冰雹不产生液态水珠。

已移除擦拭/甩水动作、Ctrl+右键拦截和交互提示。连续 30 秒不使用望远镜后，自动清除水珠及水痕；短暂放下保留当前表面状态，重新使用会重置 30 秒计时。未使用时不会新增水珠，即使当地仍在降雨。仅手持而未按住右键观察仍计为未使用。清理在客户端 tick 中执行，不依赖着色器成功或渲染帧。

已移除结霜效果，以及降雪/低温触发、晶体生成、生长消融和光学渲染逻辑。雨雪天气对远景的大气衰减保持不变。

主水珠上限为 80 枚；名额满时将静止细珠转存到持久纹理，让新雨滴持续进入，避免长时间降雨后停止流淌。满强度降雨每秒尝试生成 16 枚主水珠和 45 枚细小水珠，以小尺寸为主。合并后的主水珠半径最多为镜片短边的 4%。CPU 模拟重力、附着和合并，GPU 双通道高度图保存细珠与水痕，结合圆润水滴高度和相邻高度梯度折射游戏场景，并绘制下缘暗边与随游戏光照变化的反光。窗口缩放时保留水痕，雨水纹理长边上限为 1024 像素。APRG 的 MIT 版权与完整许可已收录在 NOTICE.txt。

望远镜现在保留游戏本身的大气雾效，并根据实际降水对镜内远景增加轻微的距离衰减：默认满强度降雨在 256 格处额外损失约 15% 对比度，降雪约 25%，冰雹按降雨处理，额外混合量最多 30%。雨雪类型沿用游戏天气与温度判断，不受粒子质量设置影响。太阳附近会出现局部眩光，随游戏太阳遮挡结果、云量和雾密度减弱，默认混合量最多 10%。完全入夜后，新增天气散射不会增亮目标；水下跳过这些效果。

以下设置仅作用于客户端，不随服务端遮罩配置同步；旧配置省略这些字段时使用默认值：

| 配置项 | 默认值 | 作用 |
| --- | --- | --- |
| `enableAtmosphericOptics` | `true` | 环境光学总开关 |
| `weatherOpticsStrength` | `1.0` | 雨雪额外衰减强度，范围 `0–2`，`0` 关闭 |
| `sunGlareStrength` | `1.0` | 太阳局部眩光强度，范围 `0–2`，`0` 关闭 |
| `enableLensRain` | `true` | 镜片水珠与流淌水痕 |
| `lensRainStrength` | `1.0` | 镜片雨击强度，范围 `0–2`，`0` 关闭 |

效果随缩放动画淡入淡出，使用 `none` 遮罩时覆盖整个观察画面；禁止第三人称缩放时一同停用。实现使用游戏场景颜色和深度，不会恢复雾中已经丢失的细节，也不新增雨雪粒子。天气取玩家所在地并近似为整条视线的天气；透明物体的距离依赖游戏深度缓冲，云层遮挡仅作近似处理。缺少有效离屏缓冲时跳过效果；着色器失败会暂停效果并记录一次日志，可在游戏中重新加载着色器后重试。

使用 1.22.3 游戏目录打包：

```powershell
./package.ps1 -GamePath E:/MVL/Release/1.22.3
```

每次打包均自动部署：脚本将生成的 ZIP 复制到本机 `C:\Users\29596\AppData\Roaming\MVL\Modpack\测试服务器\Mods`，替换旧的本分支 ZIP，并校验部署文件的 SHA256。可用 `-DeployPath` 指定其他部署目录。更新后重新启动游戏以加载新代码。

兼容性及验证边界见 [分支版验证记录](COMPATIBILITY-FORK.md)。

## Original project

Vintage Story Mod, Adds a spyglass so you can spy on your neighbors from the safety of your windmill!

[![Spyglass prominently displayed upon an anvil.](https://img.youtube.com/vi/oCwqJoa6sP0/maxresdefault.jpg)](https://www.youtube.com/watch?v=oCwqJoa6sP0)

[Discuss the mod on Vintage Story Forums](https://www.vintagestory.at/forums/topic/5240-spyglass-v040/)

[Download via Vintage Story Mod DB](https://mods.vintagestory.at/spyglass)
````

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `spyglassfork.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 3 | `assets/spyglassfork/itemtypes/spyglass-glass.json`<br>`assets/spyglassfork/itemtypes/spyglass.json`<br>`assets/spyglassfork/itemtypes/spytube.json` |
| 实体定义 | 0 | — |
| 配方定义 | 3 | `assets/spyglassfork/recipes/grid/spyglass-glass.json`<br>`assets/spyglassfork/recipes/grid/spyglass.json`<br>`assets/spyglassfork/recipes/smithing/spytube.json` |
| 资产补丁 | 2 | `assets/game/patches/game-entities-humanoid-player.json`<br>`assets/game/patches/game-shapes-entity-humanoid-seraph-faceless.json` |
| 语言资源 | 6 | `assets/spyglassfork/lang/en.json`<br>`assets/spyglassfork/lang/fr.json`<br>`assets/spyglassfork/lang/pt-br.json`<br>`assets/spyglassfork/lang/ru.json`<br>`assets/spyglassfork/lang/uk.json`<br>`assets/spyglassfork/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**spyglassfork.dll**（`c59df986659ec4de`）：27 个类型。

```text
Class <Module>
Class spyglass.src.ClientManipulation
Class spyglass.src.ClientPatcher
Class spyglass.src.ItemSpyglass
Class spyglass.src.SpyglassConfig
Class spyglass.src.SpyglassMod
Class spyglass.src.Network.ServerConfigSyncPacket
Class spyglass.src.Client.AtmosphericOpticsModel
Class spyglass.src.Client.AtmosphericOpticsRenderer
Class spyglass.src.Client.LensGlass
Class spyglass.src.Client.LensRainModel
Class spyglass.src.Client.LensRainSurface
Class spyglass.src.Client.OpticsRenderState
Class spyglass.src.Client.SpyglassOverlay
Class spyglass.src.Client.ClientTime
Class spyglass.src.Client.GameWheel
Class spyglass.src.Client.UpdateableTween
Class spyglass.src.Client.ZoomWheel
Class spyglass.src.Client.Patches.BasePatch
Class spyglass.src.Client.Patches.GuiDialogHudPatch
Class spyglass.src.Client.Patches.ImmersiveFpSystemRenderEntities
Class spyglass.src.Client.Patches.OnBeforeRenderFrame3D
Class spyglass.src.Client.Patches.OnMouseMove
Class spyglass.src.Client.Patches.OptionalHudPatches
Class spyglass.src.Client.Patches.Set3DProjection
Class spyglass.src.SpyglassMod.<>c__DisplayClass22_0
Class spyglass.src.Client.LensRainModel.Drop
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 3 个配方文件与 0 个手册章节](/reference/recipes/spyglassfork)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
