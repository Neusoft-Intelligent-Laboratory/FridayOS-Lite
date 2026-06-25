# 🚀 FridayOS-Lite 上传手册（给 Owen，不随仓库公开）

> 本文件在仓库**外面**，不会被上传。原仓库内的《上传到GitHub.md》已删除（内部笔记不该公开）。

## 本次重构后的仓库结构

```
FridayOS-Lite/
├── README.md（英文主页）/ README.zh-CN.md（中文）   # ⚠️ 2026-06-11 起英文为主语言（与正式版惯例一致）
├── FRIDAY-BLUEPRINT.md（英）/ Friday大脑蓝图.md（中） # ⭐ 核心交付物
├── TOOLS.md / 工具说明.md · INSTALL.md / 安装指南.md · FAQ.md / 常见问题.md
├── 下载清单.md
├── LICENSE (MIT) · .gitignore · .gitattributes
├── 示例大脑-云栈科技/  + 示例大脑-云栈科技.zip   # 🎮 演示沙盘（169文件：100员工+11项目+6客户+10skills+5模板+3总览MOC）
└── docs/images/  (hero.png · architecture.png · 截图待补)
```

⚠️ **示例大脑改动后必须重新打包 zip**（保持文件夹和 zip 同步）：
```bash
python3 -c "import shutil; shutil.make_archive('示例大脑-云栈科技','zip',root_dir='.',base_dir='示例大脑-云栈科技')"
```
生成脚本永久备份在 `D:\Friday\FridayOS-Lite示例大脑生成器.py`（仓库外，不公开）；数据固定种子 2026。

**演示钩子（11 个提示词的"标准答案"，v3 三幕版）：**
> ⚠️ 公开的演示手册里只给"答案方向"+模型能力免责提示（避免弱模型跑砸被归咎于 Friday）；
> 下面的精确钥匙**只存在本手册**，供你 QA 验收用，勿外传。
- ①借调答案=陆云飞/赵承宇（长风TMS收尾）+郭一鸣（效能平台半搁置）。
- ②⭐延期代价账（基于联网调研的"尾款纠纷+验收条款"真实痛点设计）：违约金¥3.4万/周×2=6.8万 + 尾款¥204万回款顺延 + 二期¥1200万入围悬置 vs 借调零额外成本。数据源=raw/东海港合同关键条款摘录 + 应收台账 + 客户页时间线。
- ③韩磊挽留：34k/连续S/被沈劲松38k倒挂/猎头45k（inbox）/决策日志5月已定调薪倾斜/期权池剩5.8%。
- ④薪酬倒挂=韩磊vs沈劲松。
- ⑤应收答案：长风105万验收已过可提前开票；城投52万逾期47天（政企走流程）；东海港204万联动交付风险。inbox有银行授信线索呼应。
- ⑥续费敞口：**全额口径73万（38+26+9）或按skill公式加权（年费×流失概率，如迅达38×80%=30.4）两种算法都判对**——2026-06-11实测模型按skill公式算，比简单加总更忠实；迅达90天未登录按挽回案处理。
- ⑦会前简报（周总）：雷区=inbox抱怨+验收3条款；目标=用增援方案换7/31信心。
- ⑧经营周报固定格式。⑨接待包：第一条"贺总不吃辣"+主动发现周四16:00林慧会撞资方送机（raw/下周日程）。
- ⑩行政场景（源自2026-06-05 AIx人力行政周会，已匿名化）：对账=陌生IP 10.8.9.88/99 + 无记录 胡海燕/韩晨/郑泽宇 + 未关机 何南絮/蒋安琪；费用=5月差旅×2.6+6月招待×1.9。
- ⑪沉淀skill：应模仿 system/模板/Skill模板.md 格式。

**调研背书（写文案可用）**：高管平均每周近23小时开会（36氪/哈佛商业评论转引）；2024国内软件项目尾款纠纷率同比+67%、平均追款11个月（55kaifa行业稿）；SaaS churn"看不见直到太晚"（sturdy.ai）；20%中小企业现金流撑不到1个月（IFPRI调查）。

已删除：`vault-template/`、`vault-template.zip`（被蓝图取代）、`上传到GitHub.md`。

## 推送

仓库已有 remote（origin → Neusoft-Intelligent-Laboratory/FridayOS-Lite）。在 FridayOS-Lite 文件夹里：

```bash
git add -A
git commit -m "Reposition Lite: blueprint-driven setup, scope = knowledge base only"
git push
```

## 发布前必做清单

0. **建议发一个 GitHub Release（v1.0）**：把 `Friday大脑蓝图.md`、`FRIDAY-BLUEPRINT.en.md`、`示例大脑-云栈科技.zip` 挂为 Release 资产——Release 附件下载**保留正确文件名和 .md 后缀**，可彻底根治"raw 另存为变 .txt"问题（文档里的复制粘贴法是无 Release 时的兜底）。发布后可把安装指南第 5/7 步的下载指引换成 Release 直链。

1. ~~补截图~~ ✅ **已完成（2026-06-11）**：8 个安装步骤 GIF + 1 个 README demo GIF 已压缩入库（`docs/images/gif/`，原片 84M → 入库 21M）。原始高清录屏留在 Downloads/GIF/；测试1、测试3 两段未入库（仓库减重），可作公众号/视频素材。改录屏后用 ffmpeg 重压：`ffmpeg -i 原.gif -vf "fps=8,scale=900:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" 新.gif`
2. **传企业微信群二维码**：存为 `docs/images/group-qr.png`，然后把 README.md / README.en.md 里的注释行取消注释（已留 TODO 标记）。
3. ~~演示提示词实测~~ ✅ Phase C 已过（2026-06-11，11/11，¥0.26/28分钟，报告在 FridayOS-Lite实测/）；**干净机器安装流程实测（A/B）仍待做**：找一台没装过 Node/Obsidian 的 Windows 电脑，从 README 开始照着做一遍。重点验证：① Windows 上 Claude Code 是否还需要 Git/Git Bash；② Claudian 设置里 Provider 选项的确切措辞；③ 蓝图第四节 Friday 是否能一次搭对。
4. **在正式版 FridayOS 的 README 顶部挂入口**：
   > 🔰 第一次接触、想要最简单的安装？看 👉 [**FridayOS‑Lite（小白版）**](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS-Lite)
5. 核对 DeepSeek 模型名/价格是否仍与官网一致（清单整理于 2026-06）。
6. **统一对外口径（2026-06-12 起）**：核心概念词是 **Vibe Knowledge Management（VKM）**——"用自然语言驱动 AI 管理知识库"。已写入 Lite（README 中英/工具说明/FAQ/安装指南/两份蓝图）与正式版两份 README。对外宣传（公众号/视频/repo description）统一用这个词；诚实口径保留一句"可复制性与上手成本待更多用户验证"，把它说成邀请而不是免责。建议 GitHub topics 加 `vibe-knowledge-management`。
7. ~~示例大脑文件夹链接 404~~ ✅ **已按方案二处理（2026-06-12）**：下载唯一入口 = zip（Release 后换 Release 直链，见第 0 条）；在线预览 = `docs/先玩这里-演示手册.md`（带"这是预览，去下 zip"提示）。README 中英的文件夹链接已全部移除。演示手册（docs 预览版 + zip 内版）均已加 VKM 一句，zip 已重打包（162KB）。
