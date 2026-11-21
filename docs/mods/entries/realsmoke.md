# 真实烟雾

Real Smoke · 模组代码：realsmoke

> 来源：整合包安装包 `Real Smoke-2.0.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `realsmoke` |
| 版本 | 2.0.0 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | XyrVexus |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“世界、气候与环境”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Physics-based smoke

</details>

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `RealSmoke.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 1 | `assets/realsmoke/entities/gas/smoke.json` |
| 配方定义 | 0 | — |
| 资产补丁 | 10 | `assets/realsmoke/patches/asphyxiation.json`<br>`assets/realsmoke/patches/carried.json`<br>`assets/realsmoke/patches/particle-collision-boxes.json`<br>`assets/realsmoke/patches/realgaspump.json`<br>`assets/realsmoke/patches/realsmokeemitter.json`<br>`assets/realsmoke/patches/remove-blockbehaviorchimney.json`<br>`assets/realsmoke/patches/remove-smokeparticles.json`<br>`assets/realsmoke/patches/smokewisps.json`<br>`assets/realsmoke/patches/solid-sides.json`<br>`assets/realsmoke/patches/tag-porous.json` |
| 语言资源 | 11 | `assets/realsmoke/lang/de.json`<br>`assets/realsmoke/lang/en.json`<br>`assets/realsmoke/lang/es-419.json`<br>`assets/realsmoke/lang/es-es.json`<br>`assets/realsmoke/lang/fr.json`<br>`assets/realsmoke/lang/ja.json`<br>`assets/realsmoke/lang/pt-br.json`<br>`assets/realsmoke/lang/pt-pt.json`<br>`assets/realsmoke/lang/ru.json`<br>`assets/realsmoke/lang/uk.json`<br>`assets/realsmoke/lang/zh-cn.json` |
| 手册资源 | 1 | `assets/realsmoke/config/handbook/realsmokeguide.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**RealSmoke.dll**（`68462f03820877cb`）：173 个类型。

```text
Class <Module>
Class RealSmoke.BlockBehaviorSmokeWisps
Class RealSmoke.BlockEntityBehaviorSmokeWisps
Class RealSmoke.EmberParticles
Class RealSmoke.BlockBunchOCandles_Patch
Class RealSmoke.SmokeImmersionFog
Class RealSmoke.SmokeImmersionRenderer
Class RealSmoke.SmokeNoiseTexture
Class RealSmoke.SmokeNoiseVolume
Class RealSmoke.SmokeParcelDebugRenderer
Class RealSmoke.SmokeParcelParticleSpawner
Class RealSmoke.SmokeParcelSpawnerSchedule
Class RealSmoke.SmokeShaderTextures
Class RealSmoke.SmokeWispClearance
Class RealSmoke.SmokeWispSource
Class RealSmoke.SmokeWispRenderer
Class RealSmoke.SmokeWisps
Class RealSmoke.SmokeWispSourceTracker
Class RealSmoke.SphereParticle
Class RealSmoke.SphereParticleSlowSchedule
Class RealSmoke.SphereParticleBudget
Class RealSmoke.SphereParticleCrowding
Class RealSmoke.SphereParticleDepth
Class RealSmoke.SphereParticleEstimate
Class RealSmoke.SphereParcelSnapshot
Class RealSmoke.SphereParticleImmersion
Class RealSmoke.SphereParticleMesh
Class RealSmoke.SphereParticleMotion
Class RealSmoke.SphereParticleOcclusion
Class RealSmoke.SphereParticleSystem
Class RealSmoke.SphereSmokeParticles
Class RealSmoke.SphereSpawnSites
Class RealSmoke.BlockEntityBeeHiveKiln_Patch
Class RealSmoke.BlockEntityStoneCoffin_Patch
Class RealSmoke.ModSystem
Class RealSmoke.SmokeQueryApi
Class RealSmoke.BlockEntityBehaviorRealGasPump
Class RealSmoke.BlockEntityBehaviorRealSmokeEmitter
Class RealSmoke.CarriedSmokeConfig
Class RealSmoke.CarriedSmokePlacement
```

其余 133 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 0 个配方文件与 1 个手册章节](/reference/recipes/realsmoke)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
