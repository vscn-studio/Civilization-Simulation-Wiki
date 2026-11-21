# 地形采样工具

Algernons Terrain Sampler · 模组代码：algernonsterrainsampler

> 来源：整合包安装包 `Algernons Terrain Sampler-1.3.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `algernonsterrainsampler` |
| 版本 | 1.3.0 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Algernon |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“依赖、兼容与管理工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Provides terrain height and worldgen map-data sampling at any world coordinate without full chunk generation.

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
| 程序集 | 7 | `AlgernonsTerrainSampler.dll`<br>`Microsoft.Extensions.Caching.Abstractions.dll`<br>`Microsoft.Extensions.Caching.Memory.dll`<br>`Microsoft.Extensions.DependencyInjection.Abstractions.dll`<br>`Microsoft.Extensions.Logging.Abstractions.dll`<br>`Microsoft.Extensions.Options.dll`<br>`Microsoft.Extensions.Primitives.dll` |
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

**AlgernonsTerrainSampler.dll**（`6a620e7cfb50c961`）：17 个类型。

```text
Class <Module>
Class AlgernonsTerrainSampler.Mapping
Class AlgernonsTerrainSampler.TerrainSamplerCommand
Class AlgernonsTerrainSampler.TerrainSamplerGenTerra
Class AlgernonsTerrainSampler.TerrainSamplerMod
Class AlgernonsTerrainSampler.WatershedsSamplerCompatability
Class AlgernonsTerrainSampler.Terrain.TerrainGenerationLib
Class AlgernonsTerrainSampler.Terrain.TerrainSamplerNormalizedSimplexFractalNoise
Class AlgernonsTerrainSampler.GenMapsSubstitutions.NoiseLandforms
Class <PrivateImplementationDetails>
Class AlgernonsTerrainSampler.Mapping.ThreadSafeRegionCache
Class AlgernonsTerrainSampler.TerrainSamplerGenTerra.<>c__DisplayClass61_0
Class AlgernonsTerrainSampler.TerrainSamplerMod.<>c
Class AlgernonsTerrainSampler.TerrainSamplerMod.<>c__DisplayClass26_0
Class AlgernonsTerrainSampler.Terrain.TerrainGenerationLib.<>c
Class AlgernonsTerrainSampler.Terrain.TerrainGenerationLib.<>c__DisplayClass19_0
Class AlgernonsTerrainSampler.Mapping.ThreadSafeRegionCache.<>c
```

**Microsoft.Extensions.Caching.Abstractions.dll**（`31caebf834b6da88`）：12 个类型。

```text
Class <Module>
Class System.ThrowHelper
Class Microsoft.Extensions.Internal.SystemClock
Class Microsoft.Extensions.Caching.Distributed.DistributedCacheEntryExtensions
Class Microsoft.Extensions.Caching.Distributed.DistributedCacheEntryOptions
Class Microsoft.Extensions.Caching.Distributed.DistributedCacheExtensions
Class Microsoft.Extensions.Caching.Memory.CacheEntryExtensions
Class Microsoft.Extensions.Caching.Memory.MemoryCacheEntryExtensions
Class Microsoft.Extensions.Caching.Memory.MemoryCacheEntryOptions
Class Microsoft.Extensions.Caching.Memory.CacheExtensions
Class Microsoft.Extensions.Caching.Memory.MemoryCacheStatistics
Class Microsoft.Extensions.Caching.Memory.PostEvictionCallbackRegistration
```

**Microsoft.Extensions.Caching.Memory.dll**（`a6bc869c530a2ed7`）：18 个类型。

```text
Class <Module>
Class FxResources.Microsoft.Extensions.Caching.Memory.SR
Class System.ThrowHelper
Class System.SR
Class Microsoft.Extensions.DependencyInjection.MemoryCacheServiceCollectionExtensions
Class Microsoft.Extensions.Caching.Distributed.MemoryDistributedCache
Class Microsoft.Extensions.Caching.Memory.CacheEntry
Class Microsoft.Extensions.Caching.Memory.MemoryCache
Class Microsoft.Extensions.Caching.Memory.MemoryCacheOptions
Class Microsoft.Extensions.Caching.Memory.MemoryDistributedCacheOptions
Class Microsoft.Extensions.Caching.Memory.CacheEntry.CacheEntryTokens
Class Microsoft.Extensions.Caching.Memory.CacheEntry.<>c
Class Microsoft.Extensions.Caching.Memory.MemoryCache.Stats
Class Microsoft.Extensions.Caching.Memory.MemoryCache.CoherentState
Class Microsoft.Extensions.Caching.Memory.MemoryCache.<>c
Class Microsoft.Extensions.Caching.Memory.CacheEntry.CacheEntryTokens.<>c
Class Microsoft.Extensions.Caching.Memory.MemoryCache.CoherentState.StringKeyComparer
Class Microsoft.Extensions.Caching.Memory.MemoryCache.CoherentState.<GetAllValues>d__7
```

**Microsoft.Extensions.DependencyInjection.Abstractions.dll**（`67fa4325000db017`）：26 个类型。

```text
Class <Module>
Class FxResources.Microsoft.Extensions.DependencyInjection.Abstractions.SR
Class System.ThrowHelper
Class System.SR
Class Microsoft.Extensions.Internal.ParameterDefaultValue
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilitiesConstructorAttribute
Class Microsoft.Extensions.DependencyInjection.FromKeyedServicesAttribute
Class Microsoft.Extensions.DependencyInjection.KeyedService
Class Microsoft.Extensions.DependencyInjection.ServiceCollection
Class Microsoft.Extensions.DependencyInjection.ServiceCollectionServiceExtensions
Class Microsoft.Extensions.DependencyInjection.ServiceDescriptor
Class Microsoft.Extensions.DependencyInjection.ServiceKeyAttribute
Class Microsoft.Extensions.DependencyInjection.ServiceProviderKeyedServiceExtensions
Class Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions
Class Microsoft.Extensions.DependencyInjection.Extensions.ServiceCollectionDescriptorExtensions
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.ConstructorInfoEx
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.ActivatorUtilitiesUpdateHandler
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.<>c
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.<>c__DisplayClass18_0
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.<>c__DisplayClass18_1
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.<>c__DisplayClass18_2
Class Microsoft.Extensions.DependencyInjection.ActivatorUtilities.<>c__DisplayClass8_0
Class Microsoft.Extensions.DependencyInjection.KeyedService.AnyKeyObj
Class Microsoft.Extensions.DependencyInjection.ServiceCollection.ServiceCollectionDebugView
Class Microsoft.Extensions.DependencyInjection.ServiceDescriptor.<>c__DisplayClass5_0
```

**Microsoft.Extensions.Logging.Abstractions.dll**（`45c2252421854171`）：51 个类型。

```text
Class <Module>
Class FxResources.Microsoft.Extensions.Logging.Abstractions.SR
Class System.ThrowHelper
Class System.SR
Class Microsoft.Extensions.Internal.TypeNameHelper
Class Microsoft.Extensions.Logging.LogDefineOptions
Class Microsoft.Extensions.Logging.LoggerExtensions
Class Microsoft.Extensions.Logging.LoggerExternalScopeProvider
Class Microsoft.Extensions.Logging.LoggerFactoryExtensions
Class Microsoft.Extensions.Logging.LoggerMessage
Class Microsoft.Extensions.Logging.LoggerMessageAttribute
Class Microsoft.Extensions.Logging.Logger
Class Microsoft.Extensions.Logging.LogValuesFormatter
Class Microsoft.Extensions.Logging.NullExternalScopeProvider
Class Microsoft.Extensions.Logging.NullScope
Class Microsoft.Extensions.Logging.DebuggerDisplayFormatting
Class Microsoft.Extensions.Logging.Abstractions.NullLogger
Class Microsoft.Extensions.Logging.Abstractions.NullLoggerFactory
Class Microsoft.Extensions.Logging.Abstractions.NullLoggerProvider
Class Microsoft.Extensions.Logging.Abstractions.NullLogger
Class Microsoft.Extensions.Logging.FormattedLogValues.<>c
Class Microsoft.Extensions.Logging.FormattedLogValues.<GetEnumerator>d__14
Class Microsoft.Extensions.Logging.LoggerExternalScopeProvider.Scope
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass0_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass10_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass12_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass14_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass16_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass18_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass1_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass20_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass2_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass3_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass4_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass5_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass6_0
Class Microsoft.Extensions.Logging.LoggerMessage.<>c__DisplayClass8_0
Class Microsoft.Extensions.Logging.LoggerMessage.LogValues.<>c
Class Microsoft.Extensions.Logging.LoggerMessage.LogValues.<GetEnumerator>d__7
Class Microsoft.Extensions.Logging.LoggerMessage.LogValues.<>c
```

其余 11 个类型未在此列出；可按维护说明重新分析程序集。

**Microsoft.Extensions.Options.dll**（`5e01894cbc0661ba`）：69 个类型。

```text
Class <Module>
Class FxResources.Microsoft.Extensions.Options.SR
Class System.ThrowHelper
Class System.SR
Class Microsoft.Extensions.DependencyInjection.OptionsBuilderExtensions
Class Microsoft.Extensions.DependencyInjection.OptionsServiceCollectionExtensions
Class Microsoft.Extensions.Options.ConfigureNamedOptions
Class Microsoft.Extensions.Options.ConfigureNamedOptions
Class Microsoft.Extensions.Options.ConfigureNamedOptions
Class Microsoft.Extensions.Options.ConfigureNamedOptions
Class Microsoft.Extensions.Options.ConfigureNamedOptions
Class Microsoft.Extensions.Options.ConfigureNamedOptions
Class Microsoft.Extensions.Options.ConfigureOptions
Class Microsoft.Extensions.Options.Options
Class Microsoft.Extensions.Options.OptionsBuilder
Class Microsoft.Extensions.Options.OptionsCache
Class Microsoft.Extensions.Options.OptionsFactory
Class Microsoft.Extensions.Options.OptionsManager
Class Microsoft.Extensions.Options.OptionsMonitor
Class Microsoft.Extensions.Options.OptionsMonitorExtensions
Class Microsoft.Extensions.Options.OptionsValidationException
Class Microsoft.Extensions.Options.OptionsValidatorAttribute
Class Microsoft.Extensions.Options.OptionsWrapper
Class Microsoft.Extensions.Options.PostConfigureOptions
Class Microsoft.Extensions.Options.PostConfigureOptions
Class Microsoft.Extensions.Options.PostConfigureOptions
Class Microsoft.Extensions.Options.PostConfigureOptions
Class Microsoft.Extensions.Options.PostConfigureOptions
Class Microsoft.Extensions.Options.PostConfigureOptions
Class Microsoft.Extensions.Options.StartupValidatorOptions
Class Microsoft.Extensions.Options.UnnamedOptionsManager
Class Microsoft.Extensions.Options.ValidateEnumeratedItemsAttribute
Class Microsoft.Extensions.Options.ValidateObjectMembersAttribute
Class Microsoft.Extensions.Options.StartupValidator
Class Microsoft.Extensions.Options.ValidateOptions
Class Microsoft.Extensions.Options.ValidateOptions
Class Microsoft.Extensions.Options.ValidateOptions
Class Microsoft.Extensions.Options.ValidateOptions
Class Microsoft.Extensions.Options.ValidateOptions
Class Microsoft.Extensions.Options.ValidateOptions
```

其余 29 个类型未在此列出；可按维护说明重新分析程序集。

**Microsoft.Extensions.Primitives.dll**（`446ff16e903e7479`）：19 个类型。

```text
Class <Module>
Class FxResources.Microsoft.Extensions.Primitives.SR
Class System.SR
Class System.Numerics.Hashing.HashHelpers
Class Microsoft.Extensions.FileProviders.EmptyDisposable
Class Microsoft.Extensions.Internal.ChangeCallbackRegistrar
Class Microsoft.Extensions.Primitives.CancellationChangeToken
Class Microsoft.Extensions.Primitives.ChangeToken
Class Microsoft.Extensions.Primitives.CompositeChangeToken
Class Microsoft.Extensions.Primitives.Extensions
Class Microsoft.Extensions.Primitives.StringSegmentComparer
Class Microsoft.Extensions.Primitives.ThrowHelper
Class Microsoft.Extensions.Primitives.CancellationChangeToken.<>c
Class Microsoft.Extensions.Primitives.ChangeToken.ChangeTokenRegistration
Class Microsoft.Extensions.Primitives.ChangeToken.<>c
Class Microsoft.Extensions.Primitives.StringValues.StringValuesDebugView
Class Microsoft.Extensions.Primitives.StringValues.<>c
Class Microsoft.Extensions.Primitives.ChangeToken.ChangeTokenRegistration.NoopDisposable
Class Microsoft.Extensions.Primitives.ChangeToken.ChangeTokenRegistration.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
