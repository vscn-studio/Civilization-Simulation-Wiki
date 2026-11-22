<!-- generated:start -->
# 草绳工艺：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>空蜜蜂手雷 · beenade</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 干草捆<br><code>grasstoropes:grassbundle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 空蜜蜂手雷<br><code>game:beenade-opened</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_L_
LBL
CLC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_L_,LBL,CLC",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "grasstoropes:grassbundle"
      },
      "C": {
        "type": "item",
        "code": "game:clay-*"
      },
      "B": {
        "type": "block",
        "code": "game:bowl-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "name": "skep",
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:beenade-opened"
    }
  }
]
```

</details>

</details>

<details><summary>粗制护盾 · crudeshield</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 干草捆<br><code>grasstoropes:grassbundle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 粗制护盾<br><code>game:shield-crude</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SSS
BBB
SSS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SSS,BBB,SSS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbundle"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:shield-crude",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>熄灭的火把 · extinguishedtorch</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 干草捆<br><code>grasstoropes:grassbundle</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 熄灭的火把<br><code>game:torch-basic-extinct-up</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
S
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P,S",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "game:torch-basic-extinct-up",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>亚麻纤维 · flaxfibers</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 产物 | 亚麻纤维<br><code>game:flaxfibers</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_B_
BBB
_B_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_B_,BBB,_B_",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>干草捆、干草 · grassbundle</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 干草<br><code>game:drygrass</code> | 1 | 未声明附加限制 |
| 产物 | 干草捆<br><code>grasstoropes:grassbundle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D__
_D_
__D
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：0 |
| 投入 B | 干草捆<br><code>grasstoropes:grassbundle</code> | 1 | 未声明附加限制 |
| 产物 | 干草<br><code>game:drygrass</code> | 3 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：0 |
| 投入 B | 香蒲<br><code>game:cattailtops</code> | 1 | 未声明附加限制 |
| 产物 | 干草<br><code>game:drygrass</code> | 3 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "D__,_D_,__D",
    "ingredients": {
      "D": {
        "type": "item",
        "code": "game:drygrass",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "grasstoropes:grassbundle",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 0
      },
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 1
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:drygrass",
      "quantity": 3
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 0
      },
      "B": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 1
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:drygrass",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、干草捆 · grasschest</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 干草捆<br><code>grasstoropes:grassbundle</code> | 3 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>grasstoropes:grasschest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LLL
L_L
LLL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>grasstoropes:grasschest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 干草捆<br><code>grasstoropes:grassbundle</code> | 12 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "LLL,L_L,LLL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 3
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "grasstoropes:grasschest-east",
      "attributes": {
        "type": "grass"
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "block",
        "code": "grasstoropes:grasschest-east",
        "attributes": {
          "type": "grass"
        }
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "grasstoropes:grassbundle",
      "quantity": 12
    }
  }
]
```

</details>

</details>

<details><summary>干草手提篮、干草捆 · grasshandbasket</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 产物 | 干草手提篮<br><code>grasstoropes:grassbasket</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B_B
BBB
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 B | 干草手提篮<br><code>grasstoropes:grassbasket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 干草捆<br><code>grasstoropes:grassbundle</code> | 5 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "B_B,BBB",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "grasstoropes:grassbasket"
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbasket"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "grasstoropes:grassbundle",
      "quantity": 5
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · haybale</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 干草捆<br><code>grasstoropes:grassbundle</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BB
BB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "BB,BB",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 1
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "game:hay-normal-ud",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>猎人背包 · hunterbackpack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:hide-pelt-*</code> | 1 | 允许变体：['medium', 'large', 'huge'] |
| 投入 C | 干草捆<br><code>grasstoropes:grassbundle</code> | 3 | 未声明附加限制 |
| 产物 | 猎人背包<br><code>game:hunterbackpack</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CPC
CCC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 小型毛皮<br><code>game:hide-pelt-small</code> | 3 | 未声明附加限制 |
| 投入 C | 干草捆<br><code>grasstoropes:grassbundle</code> | 3 | 未声明附加限制 |
| 产物 | 猎人背包<br><code>game:hunterbackpack</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CSC
CCC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "CPC,CCC",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:hide-pelt-*",
        "allowedVariants": [
          "medium",
          "large",
          "huge"
        ],
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 3
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:hunterbackpack"
    }
  },
  {
    "ingredientPattern": "CSC,CCC",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hide-pelt-small",
        "quantity": 3
      },
      "C": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 3
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:hunterbackpack"
    }
  }
]
```

</details>

</details>

<details><summary>马尾草亚麻布膏药、蜂蜜硫磺芦苇膏药 · poultice</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>game:flower-horsetail-free</code> | 4 | 未声明附加限制 |
| 投入 H | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 产物 | 马尾草亚麻布膏药<br><code>game:poultice-reed-horsetail</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 投入 S | 硫磺粉<br><code>game:powder-sulfur</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蜂蜜硫磺芦苇膏药<br><code>game:poultice-reed-honey-sulfur</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SBS
_C_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "B,H",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:flower-horsetail-free",
        "quantity": 4
      },
      "H": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:poultice-reed-horsetail",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SBS,_C_",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:powder-sulfur"
      },
      "B": {
        "type": "block",
        "code": "game:bowl-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:poultice-reed-honey-sulfur",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>绳索捆 · rope</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 产物 | 绳索捆<br><code>game:rope</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BBB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "BBB",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:rope",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>草席 · rushmatting</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 产物 | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__K
LL_
LL_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "__K,LL_,LL_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:rushmat"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · skep</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 干草捆<br><code>grasstoropes:grassbundle</code> | 2 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:skep-reed-empty-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LLL
LLL
LCL
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "LLL,LLL,LCL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "grasstoropes:grassbundle",
        "quantity": 2
      },
      "C": {
        "type": "item",
        "code": "game:clay-*",
        "quantity": 2
      }
    },
    "name": "skep",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:skep-reed-empty-east"
    }
  }
]
```

</details>

</details>

<details><summary>干草 · thatch</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 茅草<br><code>game:thatch</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：0 |
| 产物 | 干草<br><code>game:drygrass</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KT
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "KT",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:thatch",
        "name": "type",
        "quantity": 1
      },
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 0
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:drygrass",
      "quantity": 2
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
