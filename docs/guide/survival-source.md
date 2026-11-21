# 生存模拟：实现与数据流

本专题根据 `vsslssmod` 1.0.1 当前源码整理。完整玩家操作可以查阅[18 章游戏内手册](/guide/handbook)，该手册来自资源文件；具体机制以源码和当前配置为准。

## 游戏启动与版本

`src/Seraph/SeraphModSystem.cs` 的 `StartPre` 读取运行时游戏版本并检查是否为支持的 1.22.x。公共启动阶段注册井、浴桶、厕所、水处理、烟囱等类及污染地图层；资源完成后执行食物校准和兼容初始化。服务端创建 `ServerCoordinator` 与生理、食物、水、卫生、伤害等桥接，客户端创建界面桥接。

## 身体状态与环境

`src/Seraph.Core` 包含身体状态及模拟逻辑；`src/Seraph.Application` 管理能力、配置与集成契约；`src/Seraph/Server` 将游戏事件连接到服务端模拟，`src/Seraph/World` 实现水、污染和设施。显示的身体状态不是简单的原版饱食度：食物和水经过摄入、消化与吸收，环境和活动又会影响水分、体温、疲劳及伤病。数值和单位必须结合具体配置字段核对。

## 护理与外部模组

`src/Seraph/TreatmentApi.cs` 提供 `RegisterTreatmentV1`、查询、开始、继续、完成和取消护理方法。注册要求有效的完整物品代码和有效定义，重复注册会失败；旧 `RegisterTreatment` 会抛出异常。查询本身不消耗物品或改变生理状态，护理操作由服务端协调。

`src/Seraph.Application/IntegrationContracts.cs` 定义环境、暴露、伤害和倒地适配器契约；`AdapterEvidence` 记录提供方版本与单位是否经过验证。食物份量只有在代码、单位、份量范围和证据均满足条件时才会生成摄入记录。公开方法是否适合外部调用及其依赖类型，应在目标版本的编译环境中确认。

## 配置与诊断

服务端配置类为 `src/Seraph.Application/SeraphServerConfig.cs`。`Mode` 支持 `survival`、`shadow`、`observe`；格式版本不符或数值校验失败时配置不能正常加载。服务端命令注册和权限见 `src/Seraph/Server/ServerCoordinator.cs`，客户端 HUD 和性能命令分别位于 `src/Seraph/Client/SeraphClientBridge.cs` 和 `src/Seraph/Diagnostics/PerformanceClient.cs`。

[生存概览](/guide/survival) · [管理员配置](/admin/survival-config) · [源码覆盖清单](/develop/source-inventory)
