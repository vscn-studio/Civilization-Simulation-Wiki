<!-- generated:start -->
# 天然肥料：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>中效肥料 · manurecompost</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 混合粪浆<br><code>naturalfertilizer:manuremixportion</code> | 50 升 | 未声明附加限制 |
| 产物 | 中效肥料<br><code>naturalfertilizer:maturefertilizer</code> | 16 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：240。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/naturalfertilizer/recipes/barrel/manurecompost.json`

```json
{
  "code": "maturefertilizer",
  "sealHours": 240,
  "ingredients": [
    {
      "type": "item",
      "code": "naturalfertilizer:manuremixportion",
      "litres": 50
    }
  ],
  "output": {
    "type": "item",
    "code": "naturalfertilizer:maturefertilizer",
    "stackSize": 16
  }
}
```

</details>

</details>

<details><summary>混合粪浆 · manuremixgrass</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 粪浆<br><code>naturalfertilizer:manureslurryportion</code> | 50 升 | 未声明附加限制 |
| 投入 2 | 干草<br><code>game:drygrass</code> | 64 | 未声明附加限制 |
| 产物 | 混合粪浆<br><code>naturalfertilizer:manuremixportion</code> | 50 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/naturalfertilizer/recipes/barrel/manuremixgrass.json`

```json
{
  "code": "manuremixportion",
  "ingredients": [
    {
      "type": "item",
      "code": "naturalfertilizer:manureslurryportion",
      "litres": 50
    },
    {
      "type": "item",
      "code": "game:drygrass",
      "quantity": 64
    }
  ],
  "output": {
    "type": "item",
    "code": "naturalfertilizer:manuremixportion",
    "litres": 50
  }
}
```

</details>

</details>

<details><summary>混合粪浆 · manuremixthatch</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 粪浆<br><code>naturalfertilizer:manureslurryportion</code> | 50 升 | 未声明附加限制 |
| 投入 2 | 茅草<br><code>game:thatch</code> | 64 | 未声明附加限制 |
| 产物 | 混合粪浆<br><code>naturalfertilizer:manuremixportion</code> | 50 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/naturalfertilizer/recipes/barrel/manuremixthatch.json`

```json
{
  "code": "manuremixportion",
  "ingredients": [
    {
      "type": "item",
      "code": "naturalfertilizer:manureslurryportion",
      "litres": 50
    },
    {
      "type": "item",
      "code": "game:thatch",
      "quantity": 64
    }
  ],
  "output": {
    "type": "item",
    "code": "naturalfertilizer:manuremixportion",
    "litres": 50
  }
}
```

</details>

</details>

<details><summary>粪浆 · manureslurry</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 新鲜粪肥<br><code>naturalfertilizer:manure</code> | 5 | 未声明附加限制 |
| 产物 | 粪浆<br><code>naturalfertilizer:manureslurryportion</code> | 5 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/naturalfertilizer/recipes/barrel/manureslurry.json`

```json
{
  "code": "manureslurryportion",
  "ingredients": [
    {
      "type": "item",
      "code": "game:waterportion",
      "litres": 1
    },
    {
      "type": "item",
      "code": "naturalfertilizer:manure",
      "quantity": 5
    }
  ],
  "output": {
    "type": "item",
    "code": "naturalfertilizer:manureslurryportion",
    "litres": 5
  }
}
```

</details>

</details>
<!-- generated:end -->
