# 食物营养查询

先选择要查询的数据：**Seraph 全部营养校准**显示份量和身体使用的营养组成；**原版与整合包营养分支**显示资源声明的饱食度与类别。两者计量方式不同，不直接互换。

<FoodCatalogue />

## 查表方法

1. 输入中文食物名或游戏内物品代码。没有中文名的记录仍可按代码查询。
2. 校准表可切换“每 100 克”和“每份”。每份按校准质量换算；液体还需核对密度、每升物品数和实际饮用量。
3. 展开“微量营养与电解质”查看全部中文字段；展开“技术说明”核对原始数据、物品代码和置信度。
4. 原版分支中的值只适用于相应条件，烹饪或液体状态可能采用另一组数据。混合餐、派和混合液体应按实际配料核对。

“未声明”不是零。没有命中具体校准时，服务器可能使用分类基线或运行时数据。选择来源模组会只显示已匹配到该模组静态资源的校准；查看全部来源可以保留未匹配的记录。

[下载完整数据](/data/food-catalogue.json) · [营养与消化教程](/guide/nutrition) · [配方与手册](/reference/recipes/)

<details><summary>技术说明：数据来源、运行时边界与未解析资源</summary>

## 数据来源与更新


原版：`E:/vintagestory/Vintagestory/assets`；整合包：用户指定 Mods；Seraph 校准：生存源码 `assets/vsslssmod/config/foods.json`。运行 `npm run asset-catalogue` 可重建。

本次读取 5488 个资源，成功解析 5476 个；营养分支 352 条，涉及 9 个来源。解析错误 12 个。

[下载完整数据（含营养补丁和校准记录）](/data/food-catalogue.json) · [查看全部配方与手册](/reference/)

## 补丁和运行时边界

营养补丁保存在下载文件 patches 中。此表没有假装执行 DLL、JSON 补丁加载顺序和服务器世界规则；多个分支也没有强行合并为最终值。校准命中表示代码匹配，不保证发布 DLL 与当前源码校准完全一致。游戏内 Seraph 食品手册的服务端数据用于核对最终份量。

## 未能解析的资源

以下文件未静默忽略；相关条目需要查看原文件或游戏运行数据。

| 模组 | 文件 | 原因 |
| --- | --- | --- |
| envelopes | assets/envelopes/recipes/grid/remove-wax-parcel.json | JSON5: invalid end of input at 26:1 |
| farmingrevamped | assets/farmingoverhaul/lang/en.json | JSON5: invalid character '\r' at 4:66 |
| longtermfood | assets/pemmican/itemtypes/food/cookedvegetable.json | JSON5: invalid end of input at 458:2 |
| stonebakeoven | assets/stonebakeoven/lang/ja.json | JSON5: invalid character '\r' at 8:122 |
| stonebakeoven | assets/stonebakeoven/lang/pt-br.json | JSON5: invalid character '\r' at 4:112 |
| stonebakeoven | assets/stonebakeoven/lang/uk.json | JSON5: invalid character '\r' at 4:109 |
| tankardsandgoblets | assets/tankardsandgoblets/recipes/grid/alcoholbandage.json | JSON5: invalid end of input at 187:1 |
| vsroofing | assets/vsroofing/lang/en.json | JSON5: invalid character '\n' at 78:0 |
| vsroofing | assets/vsroofing/lang/ru.json | JSON5: invalid character '\n' at 71:0 |
| vsroofing | assets/vsroofing/lang/uk.json | JSON5: invalid character '\n' at 67:0 |
| betterchinese | assets/firestarters/lang/zh-cn.json | JSON5: invalid character '\n' at 6:0 |
| betterchinese | assets/swordz/lang/zh-cn.json | JSON5: invalid character '\n' at 6:0 |

</details>
