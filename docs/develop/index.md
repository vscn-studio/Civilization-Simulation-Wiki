# 开发与兼容

<PortalCards :items='[{&quot;title&quot;: &quot;API 与接入&quot;, &quot;description&quot;: &quot;治疗接口、适配器契约和单位要求。&quot;, &quot;link&quot;: &quot;/develop/api&quot;}, {&quot;title&quot;: &quot;公式与单位&quot;, &quot;description&quot;: &quot;追溯身体模拟的数值来源。&quot;, &quot;link&quot;: &quot;/develop/formulas&quot;}, {&quot;title&quot;: &quot;源码索引&quot;, &quot;description&quot;: &quot;按模块定位文件和实现。&quot;, &quot;link&quot;: &quot;/develop/source-inventory&quot;}, {&quot;title&quot;: &quot;文档维护&quot;, &quot;description&quot;: &quot;了解来源、生成流程和校验方式。&quot;, &quot;link&quot;: &quot;/develop/maintenance&quot;}]' />

以下以三个源码项目的当前版本为依据：文明模拟 `vsscsmod` 1.0.0、文明补丁 `vsscpmod` 1.0.1、生存模拟 `vsslssmod` 1.0.1。游戏 API、依赖模组和版本变化可能改变内部实现；源码中的类型不都构成稳定的公开 API。

## 项目结构与构建

三个项目均为 C# Vintage Story 模组，客户端与服务端共用发布包。文明模拟和补丁的入口、功能与兼容逻辑位于 `src`，相关检查位于 `tests`；项目根目录有 `build.ps1`。生存模拟使用 `Seraph.slnx`：`Seraph.Core` 实现模拟核心，`Seraph.Application` 承载应用逻辑和契约，`Seraph` 负责游戏桥接，`Seraph.DebugUI` 为可选调试包。其 `scripts` 和 `tests` 包含构建、手册、本地化、食物覆盖及运行检查。

构建前按各项目的工程文件和脚本准备 Vintage Story 游戏程序集及 .NET 环境。运行项目自身测试时，以各项目的 `tests` 工程和 `scripts` 中的检查为准；不要把此 Wiki 的构建成功当作模组运行测试。

## 生存模拟接入

源码 `Seraph/TreatmentApi.cs` 中的 `SeraphModSystem` 暴露护理相关方法：`RegisterTreatmentV1` 在启动时按完整物品代码注册并校验定义，重复注册会抛出异常；旧 `RegisterTreatment` 明确抛出异常，调用方应使用 V1。服务端可通过 `QueryTreatment`、`BeginTreatment`、`ContinueTreatment`、`CompleteTreatment` 和 `CancelTreatment` 管理护理流程；查询不消耗物品或改变状态。`ReadHerbalWater` 用于读取主模组的水质元数据。

`Seraph.Application/IntegrationContracts.cs` 定义房间、暴露、伤害和倒地等适配器契约。`AdapterEvidence` 记录提供方版本和单位验证情况；提供食物数据时必须提供可验证单位和有效份量。使用前应结合实际接线和对应版本源码确认契约是否适用于自己的集成，不要直接修改客户端状态代替服务端验证。

## 兼容开发

文明补丁的兼容代码按目标功能拆分，例如 RKN 制作、Logging 搬运、Stone Quarry 石板、车船货位、地图信息和画布渲染。功能依赖相应模组与版本，优先检查启动条件、补丁目标和日志，再在目标整合包中测试共存；不要假设缺少依赖时仍会执行。

文明模拟将聚落、领地、部落、交易、公告和地图分别组织在不同源码文件。世界状态、服务端配置和客户端地图设置的持久化位置不同；兼容层应保留原有数据所有权和权限检查。公告及教程按世界保存，参考[管理员手册](/admin/)。

生存模拟的食物数据覆盖以发布包内 `assets/vsslssmod/config/foods.json` 为模板；包内 `compatibility.json` 用于兼容诊断。开发新食品或交互时，应核对物品代码、单位、服务端处理与游戏内手册，并使用项目现有的食物覆盖和本地化检查。

## 许可

三个核心项目代码均声明 MIT 许可。生存模拟的模型、图标、音效和数据还受各自素材声明约束；文明模拟亦有第三方声明。第三方模组遵循各自许可，转载资源或代码前请核对原始许可证。
