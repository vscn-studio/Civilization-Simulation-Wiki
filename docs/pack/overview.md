# 整合包玩法路线

<PortalCards :items='[{&quot;title&quot;: &quot;开局与阶段推进&quot;, &quot;description&quot;: &quot;先获得稳定饮水、食物和休息条件。&quot;, &quot;link&quot;: &quot;/pack/progression&quot;}, {&quot;title&quot;: &quot;农业、烹饪与储存&quot;, &quot;description&quot;: &quot;从食材、加工到营养搭配。&quot;, &quot;link&quot;: &quot;/pack/food-and-nutrition&quot;}, {&quot;title&quot;: &quot;水与卫生设施&quot;, &quot;description&quot;: &quot;取水、处理、洗浴和排泄物处理。&quot;, &quot;link&quot;: &quot;/pack/water-and-sanitation&quot;}, {&quot;title&quot;: &quot;工业与交通&quot;, &quot;description&quot;: &quot;查看加工设备、生产和搬运路线。&quot;, &quot;link&quot;: &quot;/pack/industry&quot;}]' />


> 本页基于本机 `Mods` 目录的 129 个安装包/目录、资源索引、语言/手册 JSON、DLL 类型索引和 Seraph 源码。没有资源或程序集证据的玩法不会在此臆测。

## 从零到稳定生存

1. 先阅读[生存手册章节](/guide/handbook)，再用原版 H 搜索 `vsslssmod` 条目；手册由 `assets/vsslssmod/config/handbook` 逐条解析。
2. 建立饮水流程：记录水源 → 按需要使用过滤、排水和洗浴设施 → 观察 C 键水量与污染 → 结合水质信息确认处理结果，避免再次污染。需要提升取水能力时，先按[阿基米德螺旋提水模组（Archimedes Screw） 配方](/reference/recipes/thetruearchimedesscrew)制作铅制槽段和直/转向螺旋；它是安装包中的真实配方，不能把普通漏斗当作同一泵。
3. 建立卫生流程：处理排泄物、清洁双手、避免把污染水带入食物；疾病暴露按真实交互路径进入。
4. 建立营养流程：用[营养表](/guide/nutrition)和[食物检索器](/guide/food-catalogue)选择有校准或原版回退的食品；查询表中没有记录时，再请管理员检查实际摄入是否无法生成营养组成。
5. 建立休息/劳动节奏：监控耐力、疲劳、睡压、核心温度和出汗负担；坐下或睡眠会触发源码中的恢复路径。
6. 受伤后先看血量、出血、疼痛、白细胞和疾病恢复面板，再进行匹配护理；治疗不要连续盲目重复。

## 手册没有覆盖的补齐规则

- C 键窗口布局与悬停说明 见[角色面板](/guide/character-panel)。
- 疾病阶段、传播路径、免疫修正见[疾病清单](/guide/diseases)。
- 治疗定义的剂量容量、重复剂量和毒性规则见[治疗规则](/guide/treatments)。
- 管理员应先用 `/vsslssmod compat` 确认 功能负责方，再改配置；配置失败时服务器保留上一次有效值。

## 按安装包证据补齐的四条路线

| 目标 | 先做什么 | 关键原始资料 |
| --- | --- | --- |
| 稳定食物 | 原始生存（Primitive Survival） 的生肉熟制/烟熏，再用 长期储存食品（Long-term food） 的腌制、干燥和 肉干油脂食品（pemmican）；每一步都在食物表中核对处理后代码。 | [原始生存（Primitive Survival）](/reference/recipes/primitivesurvival)、[长期储存食品（Long-term food）](/reference/recipes/longtermfood) |
| 肥料和卫生 | 由排泄物或动物粪便进入桶内浆料，再加入草料形成 粪肥混合料（`manuremixportion`），最终得到 成熟肥料（`maturefertilizer`）；连接 SLSS 排泄处理后再施肥。 | [天然肥料模组（Natural Fertilizer）](/reference/recipes/naturalfertilizer)、[水与卫生](/pack/water-and-sanitation) |
| 搬运与旅行 | 先做 Cartwright 的车体/车篷和可穿戴鞍具，再用 造船模组（Shipwright） 的船体路线；旅行前把水、校准食物、绷带和休息点作为同一补给计划。 | [马车与商队（Cartwrights Caravan）](/reference/recipes/cartwrightscaravan)、[造船模组（Shipwright）](/reference/recipes/shipwright) |
| 石材和建筑 | 采石模组（Stone Quarry） 的采石、凿子、楔子与碎石存储配方按工具和支撑条件分阶段使用；不要把普通石锤配方替代凿刻流程。 | [采石模组（Stone Quarry）](/reference/recipes/stonequarryrepckfipil)、[chiseltools](/reference/recipes/chiseltools) |

## 资源覆盖与限制

每个整合包条目的“安装包实现证据”列出实际方块、物品、配方、patch、手册、配置和可反编译 DLL 类型。DLL 类型索引证明类型存在，不能单独证明某个世界条件下必然启用；无源码的第三方行为必须按反编译证据和运行日志复核。
