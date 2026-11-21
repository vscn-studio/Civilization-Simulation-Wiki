# 油灯放置

Oil Lamps Anywhere! · 模组代码：oillampsanywhere

> 来源：整合包安装包 `Oil Lamps Anywhere!-1.1.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `oillampsanywhere` |
| 版本 | 1.1.0 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0, survival 1.22.0 |
| 作者 | Zozobra |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Allows oil lamp placement on ceilings, fences, slabs - while preserving the current lamp models and functionality.

</details>

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

```text
Oil Lamps Anywhere! 1.1.0
By Zozobra

Allows oil lamp placement on ceilings, fences, slabs - while preserving the
current lamp models and functionality.

INSTALL / UPGRADE
Fully exit the game and server. Remove previous Oil Lamp Ceiling Fix or Oil
Lamps Anywhere ZIPs and install only oillampsanywhere_1.1.0.zip. The mod ID has
changed: the old mod will not automatically be replaced by this one.
Install on both client and server. Disable the original Hanging Oil Lamps mod.
Existing lamps from the 1.1 release candidates keep their saved block IDs and
remain compatible. No pickup/replacement is needed for those lamps.

FEATURES
- Ceiling lamps face opposite the player's horizontal viewing direction.
- Top-half horizontal slabs raise the lamp to meet their underside.
- Bottom-half slabs and full ceilings use normal hanging height.
- Wall-style placement works on either broad face of vertical slabs.
- Lamps attach underneath and to the sides of fence posts.
- Particles and selection boxes follow the actual facing and mounting surface.
- Lamps drop the ordinary vanilla oil lamp of the same color.

Hold an oil lamp and right-click the desired surface without holding Shift.
Pick up and replace old 1.0.x ceiling lamps to use the new orientation/offsets.

COMPATIBILITY
Minimum game and survival versions: 1.22.0. This allows installation across the
1.22 stable release series. Earlier 1.22 builds have not been individually tested;
compilation, automated checks and user-confirmed in-game testing were on 1.22.7.
The dependencies are minimum versions, not an exclusive 1.22 version range.
Place On Slabs 1.2.0 and Oil Lamp Ignites 1.0.0 were included in integration tests.
Place On Slabs is optional; ceiling and wall offset handling is self-contained.

Before uninstalling or downgrading to 1.0.x, pick up the custom placed lamps.
Versions without their placed block definitions cannot restore those blocks.

VALIDATION
User confirmed the functionality in release candidate 1.1.0-rc.2.
Release 1.1.0 changes branding, mod identity and minimum dependency versions;
placement logic and saved block IDs remain unchanged.
Production build and patch/particle smoke checks passed after the rename.
Prior integration checks covered 80 ceiling and 360 wall variants, client model
loading without server-only assets, support alignment, particles, ray selection,
drops, rotation, neighbor changes and support removal.

SOURCE
The separate source ZIP contains the project and validation fixtures.
Build: dotnet build src/OilLampCeilingFix.csproj -c Release
Uses the game's DLLs from %APPDATA%/Vintagestory by default.
Override the path using -p:GameDir=YOUR_GAME_DIRECTORY.
The integration fixture is test-only: it exits the isolated test server process
and must never be installed in a normal game/server Mods folder.
```

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `OilLampsAnywhere.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 0 | — |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**OilLampsAnywhere.dll**（`b0cdf712a2c1074f`）：14 个类型。

```text
Class <Module>
Class OilLampCeilingFix.CeilingSupport
Class OilLampCeilingFix.BlockCeilingLamp
Class OilLampCeilingFix.WallSupport
Class OilLampCeilingFix.BlockWallLamp
Class OilLampCeilingFix.CeilingAssets
Class OilLampCeilingFix.CeilingFixSystem
Class OilLampCeilingFix.CeilingPlacementPatch
Class OilLampCeilingFix.CeilingRotationPatch
Class OilLampCeilingFix.CeilingParticlePatch
Class OilLampCeilingFix.RaisedLampSelection
Class <PrivateImplementationDetails>
Class OilLampCeilingFix.CeilingSupport.<>c
Class OilLampCeilingFix.CeilingAssets.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
