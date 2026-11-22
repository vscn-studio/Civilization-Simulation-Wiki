# 工业、能源与自动化兼容

工业与自动化需要同时考虑材料加工、储运和服务端结算。自动化模组可以提供食物、液体、环境或伤口数据，但必须通过 Seraph 的服务端接口声明单位和证据。

## 已安装资源能做什么

- **水力取水**：阿基米德螺旋提水模组（Archimedes Screw） 的资源中有铅制槽段、直段与转向段配方；按方块方向拼接后再验证输入/输出水位。页面只列配方事实，实际泵速由方块行为和服务器环境决定。
- **动物动力与加工**：家庭工坊（Cottage Industry） 的 26 个配方文件包含动物动力设备、磨石、发酵和压榨链；先在[配方页](/reference/recipes/cottageindustry)确认输入容器、工具和时长，再接入营养/卫生流程。
- **肥料链**：天然肥料模组（Natural Fertilizer） 的桶配方把水和粪便做成 粪便浆料（`manureslurryportion`），加入草料后成为 粪肥混合料（`manuremixportion`），继续成熟为 成熟肥料（`maturefertilizer`）。SLSS 的排泄物适配器负责来源与存储，不能只放一个物品就假定获得肥料。

<details><summary>技术说明</summary>

开发者接入时遵守：食品提交质量（克）、水提交升、能量提交 kJ；`UnitsVerified=false` 的适配器数据不会进入生理账本。管理员用 `/vsslssmod compat` 查看 provider 与能力所有权。配方与手册的完整 JSON 保存在[资料库](/reference/)，不要从 README 推导加工时间或输出数量。


</details>
