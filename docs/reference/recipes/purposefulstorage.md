<!-- generated:start -->
# 专用储存：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>名称未汉化（见物品代码） · belthooks</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>belthooks-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_
PS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>belthooks-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_
PS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P_,PS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "belthooks-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P_,PS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "belthooks-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · blanketrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plankslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>blanketrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S
P
S
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>blanketrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>blanketrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "S,P,S",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:plankslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "blanketrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "blanketrack-normal-east",
        "attributes": {
          "PSAttributes": {
            "wood": "oak"
          }
        }
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "blanketrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · gloverack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>gloverack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PS
PS
PS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>gloverack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PS
PS
PS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PS,PS,PS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "gloverack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PS,PS,PS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "gloverack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · hatrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：2 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>hatrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B_
TS
B_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：2 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>hatrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B_
TS
B_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "B_,TS,B_",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "hatrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "B_,TS,B_",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "hatrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · necklacestand</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>necklacestand-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
P_
PP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>necklacestand-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
P_
PP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PP,P_,PP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "necklacestand-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PP,P_,PP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "necklacestand-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · pantsrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plankslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>pantsrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BPB
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>pantsrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>pantsrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "BPB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:plankslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "pantsrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "pantsrack-normal-east",
        "attributes": {
          "PSAttributes": {
            "wood": "oak"
          }
        }
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "pantsrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shoerack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shoerack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
___
PSP
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shoerack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
___
PSP
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "___,PSP,PPP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "shoerack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "___,PSP,PPP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "shoerack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · wardrobe</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 3 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>wardrobe-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
GNG
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>wardrobe-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
GNG
PPP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 投入 X | 木棍<br><code>game:stick</code> | 5 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 3 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：2 |
| 产物 | 名称未汉化（见物品代码）<br><code>wardrobe-wooden-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
XTX
PPP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 投入 X | 木棍<br><code>game:stick</code> | 5 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：2 |
| 产物 | 名称未汉化（见物品代码）<br><code>wardrobe-wooden-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
XTX
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PSP,GNG,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "wardrobe-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSP,GNG,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "wardrobe-normal-east"
    }
  },
  {
    "ingredientPattern": "PSP,XTX,PPP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      },
      "X": {
        "type": "item",
        "code": "game:stick",
        "quantity": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 3
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "wardrobe-wooden-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSP,XTX,PPP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      },
      "X": {
        "type": "item",
        "code": "game:stick",
        "quantity": 5
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "wardrobe-wooden-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · apothecarycabinet</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>apothecarycabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HNS
PGP
PRP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>apothecarycabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HNS
PGP
PRP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HNS,PGP,PRP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "apothecarycabinet-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "HNS,PGP,PRP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "apothecarycabinet-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · butterflydisplaypanel</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butterflydisplaypanel-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
SGS
SLS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butterflydisplaypanel-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
SGS
SLS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SPS,SGS,SLS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*-down"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "butterflydisplaypanel-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "SPS,SGS,SLS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*-down"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "butterflydisplaypanel-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · gearrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>gearrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
SS
PP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>gearrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
SS
PP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PP,SS,PP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "gearrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PP,SS,PP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "gearrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · glidermount</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>glidermount-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
SPS
_S_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>glidermount-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
SPS
_S_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P_P,SPS,_S_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "glidermount-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P_P,SPS,_S_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "glidermount-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · jonaspartscabinet</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>jonaspartscabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PHP
GNG
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>jonaspartscabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PHP
GNG
PSP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PHP,GNG,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jonaspartscabinet-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PHP,GNG,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jonaspartscabinet-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · medallionrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>medallionrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_SP
_BP
PLP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>medallionrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_SP
_BP
PLP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_SP,_BP,PLP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      },
      "B": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*-down"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "medallionrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_SP,_BP,PLP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "B": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*-down"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "medallionrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · saddlerack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>*:plankslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saddlerack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>*:plankslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saddlerack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_S_,PPP",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "*:plankslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "saddlerack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_S_,PPP",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "*:plankslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "saddlerack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · schematicrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>schematicrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P__
PP_
P_P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>schematicrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P__
PP_
P_P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P__,PP_,P_P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "schematicrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P__,PP_,P_P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "schematicrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · tuningcylinderrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tuningcylinderrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSS
PSS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tuningcylinderrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSS
PSS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tuningcylinderrack-stand-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP_
PPP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tuningcylinderrack-stand-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP_
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PSS,PSS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tuningcylinderrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSS,PSS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tuningcylinderrack-normal-east"
    }
  },
  {
    "ingredientPattern": "PP_,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tuningcylinderrack-stand-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PP_,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tuningcylinderrack-stand-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · clothrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plankslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>clothrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
S
P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>*:plankslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>clothrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
S
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P,S,P",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:plankslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "clothrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P,S,P",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "*:plankslab-*-down-free"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "clothrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · peltrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:debarkedlog-{wood}-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>peltrack-small-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LAL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>*:debarkedlog-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>peltrack-small-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LAL
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:debarkedlog-{wood}-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>peltrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R_R
LAL
L_L
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>*:debarkedlog-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>peltrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R_R
LAL
L_L
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:debarkedlog-{wood}-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>peltrack-huge-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R_R
LAL
LLL
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>*:debarkedlog-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 名称未汉化（见物品代码）<br><code>peltrack-huge-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R_R
LAL
LLL
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "LAL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:debarkedlog-{wood}-ud"
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "peltrack-small-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "LAL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "*:debarkedlog-*-ud"
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "peltrack-small-east"
    }
  },
  {
    "ingredientPattern": "R_R,LAL,L_L",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:debarkedlog-{wood}-ud"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "peltrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "R_R,LAL,L_L",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "*:debarkedlog-*-ud"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "peltrack-normal-east"
    }
  },
  {
    "ingredientPattern": "R_R,LAL,LLL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:debarkedlog-{wood}-ud"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "peltrack-huge-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "R_R,LAL,LLL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "*:debarkedlog-*-ud"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 10
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "peltrack-huge-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · resourcebin</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>resourcebin-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P__
P_P
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>resourcebin-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P__
P_P
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P__,P_P,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "resourcebin-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P__,P_P,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "resourcebin-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · roperack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>roperack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>roperack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
PSP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P_P,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "roperack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P_P,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "roperack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · arrowrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>arrowrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__S
PPS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>arrowrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__S
PPS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "__S,PPS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "arrowrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "__S,PPS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "arrowrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · spearrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>spearrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
PSP
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>spearrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
PSP
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PSP,PSP,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "spearrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSP,PSP,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "spearrack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · swordpedestal</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>swordpedestal-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>swordpedestal-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
PPP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>swordpedestal-stone-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
SBS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SPS,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "swordpedestal-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "SPS,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "swordpedestal-normal-east"
    }
  },
  {
    "ingredientPattern": "_C_,SBS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "game:stone-*"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "swordpedestal-stone-east",
      "attributes": {
        "PSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · swordplaque</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>swordplaque-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
SPS
_S_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>swordplaque-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
SPS
_S_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SPS,SPS,_S_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "swordplaque-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "SPS,SPS,_S_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "swordplaque-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · weaponrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_R_
SPS
SSS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>weaponrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_R_,SPS,SSS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "weaponrack-normal-east",
      "attributes": {
        "PSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "weaponrack-normal-east",
        "attributes": {
          "PSAttributes": {
            "wood": "oak"
          }
        }
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponrack-normal-east"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
