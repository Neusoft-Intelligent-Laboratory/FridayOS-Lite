# GitHub 上线手册（私有先行 · 停在发布前）

> 目标：把两个仓库以**私有**形式传上 GitHub，做到"成品级、可演示"，但**不公开**。
> 到时候直接用 GitHub 私有仓库给领导**汇报 + 展示实力**；他们点头后，再一键"翻公开"= 正式发布。

---

## 0. 你手上的两个文件夹

| 本地文件夹 | 推成 GitHub 仓库 | 公私 |
| ---- | ---- | ---- |
| `D:\Friday\FridayOS\` | `Neusoft-Intelligent-Laboratory/FridayOS` | 🔒 私有（暂） |
| `D:\Friday\neusoft-org\`（**去掉 3 份内部草稿**，见下） | `Neusoft-Intelligent-Laboratory/.github` | 🔒 私有（暂） |

> ⚠️ 这 3 份是**只给你看的内部草稿**，不要推上去：`ORG-SETUP-GUIDE.md`、`ADVISORS-DRAFT.md`、`DESIGN-PHILOSOPHY.md`。
> `BRAND-视觉规范.md` 可留作贡献者品牌指南；`assets/` 里的 PNG/SVG 都要推。

---

## 1. 推送（两个仓库都设为 Private）

在 GitHub org 里**先建两个空的私有仓库**：`FridayOS` 和 `.github`（名字必须带点）。然后本地推送：

```bash
# ---- FridayOS（旗舰产品）----
cd D:\Friday\FridayOS
git init
git add -A
git commit -m "FridayOS v0.5 — Friday, the complementary AI agent that knows you and completes you"
git branch -M main
git remote add origin https://github.com/Neusoft-Intelligent-Laboratory/FridayOS.git
git push -u origin main

# ---- .github（org 主页 + 社区文件）----
cd D:\Friday\neusoft-org
del ORG-SETUP-GUIDE.md ADVISORS-DRAFT.md DESIGN-PHILOSOPHY.md   # 内部草稿不入库（Windows）
git init
git add -A
git commit -m "org profile + community health files"
git branch -M main
git remote add origin https://github.com/Neusoft-Intelligent-Laboratory/.github.git
git push -u origin main
```

> 建私有仓库时 Visibility 选 **Private**——这一步决定了"停在发布前"。

---

## 2. 仓库设置（让它看起来像个真产品）

### FridayOS 仓库 → Settings & 右上 About
- **Description**：`Meet Friday — the complementary AI agent that knows you and completes you. Feishu → Claude → Obsidian, one folder.`
- **Topics**（About 齿轮里加）：`ai-agent` `second-brain` `personal-knowledge-management` `obsidian` `claude` `mbti` `knowledge-management` `digital-employee`
- **Social preview**（Settings → 往下找 Social preview → 上传）：`FridayOS/docs/images/social-preview-1280x640.png`

### org 头像 & 资料（Settings → Profile）
- **Avatar**：上传 `neusoft-org/assets/logo-avatar-512.png`（GitHub 头像不收 SVG，PNG 已导好）
- **Name**：Neusoft Intelligence Lab
- **Description**：`数字员工 · 职能智能化 — 为企业职能（人力/财经/采购/法务）构建数字员工。Makers of FridayOS.`

---

## 3. 邀请领导"进来看"（私有阶段的关键）

私有仓库别人默认看不到。两种邀请方式：

1. **加为 org 成员**（People → Invite member）→ 能看到 org 下所有私有仓库。适合简总（你老板）。
2. **单仓库邀请**（FridayOS → Settings → Collaborators → Add）→ 只给某仓库查看权。适合只想给某位看 FridayOS。

> 📌 org **主页**那张落地页，只有 `.github` 仓库**公开**后才自动渲染。私有阶段演示时，**直接打开 `.github` 仓库里的 `profile/README.md` 文件**——GitHub 会把它渲染出来，banner、表格、徽章都在，效果一样。

---

## 4. 三分钟 GitHub 演示脚本（带领导走一遍）

> 顺序：先愿景，再实力，最后要资源。全程在 GitHub 里点，不用 PPT。

1. **开 org `.github/profile/README.md`**（30 秒）——"这是我们实验室主页。**从阿波罗的 HR 数字员工，到现在面向所有职能。**"指 banner + 使命 + 缘起传承线。
2. **滚到"战绩"**（20 秒）——"阿波罗阶段已真上线、省约 10 人月、投产比约 30。"（数字背书）
3. **点进 `FridayOS` 仓库**（60 秒）——hero + README：**"认识 Friday——最懂你、并与你互补的 AI Agent"**，闭环架构图、双脑循环、16 型矩阵。"我和 River 在新公司从零搭的，已跑通飞书→Claude→Obsidian。"
4. **翻 `docs/theory` 和 `template`**（30 秒）——"不是 demo，是完整可复用的开源工程：理论、模板、代码、脱敏都做好了。"
5. **收口要资源**（20 秒）——"现在停在发布前，**想请您把把关**。一个职能 AI 项目在 GitHub 拿高星，对实验室、对集团都是看得见的政绩；想正式发布，需要您的指导和一点资源。"

---

## 5. 汇报话术要点（按对象调）

- **对简国栋（直属老板/子公司 CEO）**：汇报式 + 子公司背书。"东软智行能产出一个对外开源的 AI 项目，是公司技术品牌的加分项。"
- **对王经锡（集团分管 VP）**：借势式。"延续阿波罗的数字员工战略，已做成开源资产，想请您指导、挂个战略顾问。"
- **对宋清君（集团 HR 总监/老战友）**：协作式。"咱们论文的思想我延续做出来了，想请你继续参与。"

> 核心叙事：**"花花轿子众人抬"——高星是大家共同的政绩。** 但先拿成品请教，给每位"轻署名→起势后升级"的台阶，别让人为难。

---

## 6. 正式发布（日后翻公开 = release）

确认领导点头、署名 OK 后，按序：

1. **领导署名同意（硬闸）**：`.github/profile/README.md` 的"缘起"与"致谢/顾问"里已具名 **王经锡、简国栋**。翻公开前，**必须确认两位本人已看过并同意公开署名**（私有演示时当面确认最自然）。任一位不同意，就把对应名字改为泛化表述（如"集团分管 VP""子公司 CEO"）后再公开。
2. **两个仓库翻公开**：各自 Settings → Danger Zone → Change visibility → Public。（先 `.github` 再 `FridayOS`，org 主页立刻有内容）
3. **确认 org 主页渲染**：访问 `github.com/Neusoft-Intelligent-Laboratory`，落地页应自动出现。
4. **Pin FridayOS**：org 主页 → Customize pins → 只 pin `FridayOS`。
5. **发首个 Release**：FridayOS → Releases → Draft → tag `v0.5` + changelog。
6. **开 Discussions**：FridayOS Settings → Features → Discussions 打勾。
7. （增长）发一条朋友圈/公众号/X，同步给领导"已上线 + 当前 star 数"。

---

## 7. 发布前最终 checklist

- [ ] 两仓库都是 **Private**
- [ ] 3 份内部草稿（`ORG-SETUP-GUIDE.md` / `ADVISORS-DRAFT.md` / `DESIGN-PHILOSOPHY.md`）**没有**被推上去
- [ ] **王经锡、简国栋** 已在"缘起/致谢"中具名 —— **翻公开前确认两位本人已同意公开署名**（不同意则改泛化表述）
- [ ] FridayOS README 顶部 hero、徽章、架构图、矩阵都正常显示（全英文物料，无方框）
- [ ] org `profile/README.md` 的 banner / 头像引用路径正常
- [ ] 再跑一遍隐私扫描：无未授权的真实公司/人名/ID/密钥/绝对路径
