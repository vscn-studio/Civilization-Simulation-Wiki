# -*- coding: utf-8 -*-
"""Add source-derived feature matrices and generate Seraph config semantics."""
from pathlib import Path
import re, hashlib
from wiki_content import write_generated
from config_semantics import generate_config_semantics

ROOT = Path(__file__).resolve().parent.parent
MODS = {
    "vsscsmod": (Path(r"E:\vintagestory\Seraph Civilization Simulation"), "文明模拟"),
    "vsscpmod": (Path(r"E:\vintagestory\Seraph Civilization Patches"), "文明补丁"),
    "vsslssmod": (Path(r"E:\vintagestory\Seraph Living Survival Simulation"), "生存模拟"),
}

def cs_files(root):
    return [p for p in sorted((root / "src").rglob("*.cs")) if "\\obj\\" not in str(p) and "\\bin\\" not in str(p)]

def declarations(text):
    return list(dict.fromkeys(re.findall(r"\b(?:record\s+struct|record\s+class|class|record|struct|interface|enum)\s+([A-Za-z_]\w*)", text)))

def methods(text):
    # Keep only named methods; this is an index, not a generated API contract.
    names = re.findall(r"\b(?:public|internal|protected|private)\s+(?:static\s+|virtual\s+|override\s+|async\s+|sealed\s+|partial\s+)*(?:[A-Za-z_][\w<>?,\[\].]*\s+)+([A-Za-z_]\w*)\s*\(", text)
    skip = {"if", "for", "while", "switch", "catch", "using", "foreach"}
    return list(dict.fromkeys(n for n in names if n not in skip))[:8]

def matrix(modid, root, label):
    rows=[]
    for p in cs_files(root):
        t=p.read_text(encoding="utf-8-sig", errors="ignore")
        rel=p.relative_to(root / "src").as_posix()
        decl=", ".join(declarations(t)[:8]) or "（顶层注册/补丁逻辑）"
        meth=", ".join(methods(t)) or "（无可索引的显式方法）"
        digest=hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        rows.append((rel,decl,meth,digest))
    groups={}
    for rel,decl,meth,digest in rows:
        top=rel.split("/")[0] if '/' in rel else '根目录'
        groups.setdefault(top,[]).append((rel,decl,meth,digest))
    out=[]
    out += ["## 源码实现矩阵（当前源码树）", "", f"以下 {len(rows)} 个 C# 文件从 `{root}` 的 `src` 目录逐文件扫描生成。每行给出声明类型、前若干可见方法和 SHA-256 前 12 位；完整文件清单与核验状态见[源码盘点](/develop/source-inventory)。源码文件存在不代表该路径在当前配置中启用，运行时仍需看依赖检测、能力所有权和配置校验。", ""]
    out += ["### 如何从矩阵定位功能", "", "| 玩家看到的系统 | 源码目录/文件前缀 | 服务器/开发者关注点 |", "| --- | --- | --- |"]
    if modid=="vsscsmod":
        out += [
          "| 文明核心、身份、复活 | `CivilizationCore.cs`、`CivilizationLifeState.cs`、`VscnRespawnBehavior.cs` | 状态持久化、生命计数、重生保护与名称校验 |",
          "| 部落、授权、领地 | `CivilizationTribes.cs`、`Tribe*.cs`、`*Territory*.cs` | 成员/角色/授权分离，领地检测和加固恢复 |",
          "| 聚落与地图 | `ClusterSpawning.cs`、`GroundMap*.cs`、`MapDrawing*.cs` | 出生点分配、纸图拼接、闭合范围与权限 |",
          "| 公告、教程、HTML | `Announcement*.cs`、`Guidance*.cs`、`CivilizationContent*.cs` | 世界内容文件、资源白名单、分页和管理员编辑 |",
          "| 经济与科技 | `CivilizationEconomy*.cs`、`Economy*.cs`、`Technology*.cs` | 报价快照、库存匹配、铸币/交易历史和科技状态 |",
          "| 兼容、策略与日志 | `*Compatibility.cs`、`ModPolicy*.cs`、`ClientLog*.cs` | 依赖握手、保护策略、客户端日志上传边界 |",
        ]
    elif modid=="vsscpmod":
        out += [
          "| 石板搬运/货舱 | `Quarry*.cs`、`EntityQuarryDrag.cs` | 石板内容统计、负重阈值、拖拽实体与船货舱布局 |",
          "| 制作与容器兼容 | `RknCrafting*.cs`、`ChiselTools*.cs`、`Toolsmith*.cs`、`*Cooking*.cs` | 目标模组检测、配方/容器匹配和恢复命令 |",
          "| 地图、坐标与信息 | `Information*.cs`、`CoordinateDisplay.cs`、`ImmersiveMapWaypointRenderer.cs` | 服务端信息限制、地图航点和客户端渲染 |",
          "| 载具、外观和绘图 | `Cape*.cs`、`VintageCanvas*.cs`、`QuarryShip*.cs` | 网格恢复、纹理/绘制兼容和船体面片 |",
          "| 等级、体能与快捷键 | `Leveling*.cs`、`Jaunt*.cs`、`Komet*.cs` | 技能面板/效果、耐力 HUD、字体与按键 |",
        ]
    else:
        out += [
          "| 核心生理 | `Seraph.Core/Framework/*.cs`、`Simulation/*.cs`、`State/*.cs` | 纯模拟状态、时间步、摄入/能量/体温/血液账本 |",
          "| 服务端桥接 | `Seraph/Server/*.cs` | 原版事件转为已验证适配器输入，所有生理写入在服务端完成 |",
          "| 水、污染与设施 | `Seraph/World/Water*.cs`、`Block*.cs`、`Pollution*.cs`、`Latrine*.cs` | 水批次、处理设备、井/浴缸/厕所、污染路径 |",
          "| 玩家窗口与 HUD | `Seraph/Client/*.cs` | C 键面板、营养手册、趋势、固定窗口、症状与调试显示 |",
          "| API 与能力 | `Seraph.Application/*.cs`、`TreatmentApi.cs` | 治疗注册、能力所有权、适配器证据、设置修订号 |",
          "| 诊断与性能 | `Seraph/Diagnostics/*.cs`、`Seraph.DebugUI/*.cs` | `.slssperf`、调试窗口、性能采样和管理员诊断 |",
        ]
    out += ["", "### 逐文件索引", ""]
    for group,items in groups.items():
        out += [f"#### `{group}/`", "", "| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |", "| --- | --- | --- | --- |"]
        out += [f"| `{rel}` | `{decl}` | `{meth}` | `{digest}` |" for rel,decl,meth,digest in items]
        out.append("")
    return "\n".join(out)

for modid,(root,label) in MODS.items():
    page=ROOT/'docs/develop/sources'/(modid+'.md')
    write_generated(page, f'# {label}源码索引\n\n[返回模组介绍](/mods/entries/{modid})\n\n'+matrix(modid,root,label))
generate_config_semantics(ROOT, MODS['vsslssmod'][0]/'src')
print("updated source matrices and seraph-config-semantics.md")
