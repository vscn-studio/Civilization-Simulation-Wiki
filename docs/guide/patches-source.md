# 兼容补丁：源码核验

本专题依据 `vsscpmod` 1.0.1 源码。补丁按已加载模组和启动环境选择性启用；出现某个文件或类型并不保证对应兼容已启动。

## 石板负重

`src/QuarryCarryCompatibility.cs` 在检测到 `stonequarryrepckfipil` 或 `stonequarry` 时尝试启用。服务端读取 `vsscpmod-quarry-carry.json`、规范化参数并将限制写入世界配置供客户端使用。

石板负重按石板 `slots` 中保存的物品数量计算，再乘该石板堆叠数量；创意预设中仅用于显示的样本不计为储存岩石。统计包括玩家自身的快捷栏、背包、制作栏、角色栏和鼠标物品，并避免重复计算已装备背包的快照；打开的外部箱子或车辆库存不计入自身负重。

默认超过 32 块后逐渐减速，达到实际停止阈值停止；单块石板达到 32 块时要求背包栏位。默认总随身块数上限为 64、石板数上限为 1，达到 16 块时开始限制部分动作。参数规范化及限制判定以该文件和 `src/QuarryContainerRecovery.cs` 为准；详情见[补丁概览](/guide/patches)。

## 初始化与独立地图

`src/SeraphCivilizationPatchesSystem.cs` 中，共用启动阶段注册石板相关实体和方块行为，并尝试初始化若干兼容；服务端负责信息限制、RKN 制作和旧 BodyPhys 数据迁移；客户端负责渲染、快捷键、界面和诊断。独立地图标记界面仅在启用 Immersive Maps 且未启用文明核心时创建，避免与文明核心重复。

## 查看兼容行为

源码按目标功能拆分：`LoggingCarryOnCompatibility.cs` 处理树干搬运，`RknCraftingCompatibility.cs` 处理 RKN 制作，`InformationRestrictions.cs` 处理信息限制，`BodyPhysMigration.cs` 处理迁移。需要具体版本的完整触发条件时应继续检查每个 `TryCreate`、补丁目标与运行日志；[源码覆盖清单](/develop/source-inventory)列出全部文件。
