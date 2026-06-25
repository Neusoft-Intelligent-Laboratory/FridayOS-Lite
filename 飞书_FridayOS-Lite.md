# FridayOS\-Lite

# 🤖 FridayOS\-Lite · 一份文档，一句话，一个 AI 第二大脑

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODhlMDIxNDllMzI1NjYwMjlmYjNkZmFjOTMzYjFkYWRfODNmNWM2NGMwYzdhZDliYjZmYzA1MTViYjU1ZjU0YTRfSUQ6NzY1MDMyNDkxOTQ5ODc4NzgwNl8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

**无需翻墙 ✓ ｜ 便宜到几毛钱（DeepSeek V4）｜ 约 30 分钟装好 ｜ MIT 开源**

**不用懂技术。不用下载模板。** 装好 Obsidian \+ Claudian 五件套，领一份《Friday大脑蓝图》丢进文件夹，对 AI 说一句话——它自己把你的第二大脑 **Friday** 搭建出来。

## Lite 是什么、不是什么

**Lite 只专注一件事：教你用 Obsidian \+ Claudian 管好自己的知识库**——也就是 Friday 的"第二大脑"本体。学会六个脑区的分区理念，让 AI 帮你随手记、定期理、随时找。每日计划、周计划这类记录，你在 Obsidian 里手动写或在对话里让 Friday 代笔。

它**不做**自动化接入：没有飞书机器人、没有随时随地的消息捕获，也没有给大脑定期体检的机械保障（lint 脚本、记忆衰减、入站安全）。那些是正式版 [FridayOS](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS) 的事——**AI 不只帮你记，还按一份契约自主运维整个大脑**。等你用 Lite 把分区理念用顺了，文件夹原样带过去升级即可，零迁移。

**Lite 给这样的你：**

- 没听过 Claude、Obsidian，也不知道去哪下、怎么装

- 一看"命令行""环境变量"就头大

- 不想翻墙、不想付外币订阅

- 只想要一个**能帮我记事、整理、随时问**的 AI 助理

> ✅ 如果你能照着说明点鼠标、复制粘贴一行字，你就能装好。
> 
> 

## 三句话讲清楚

1. **一个文件夹就是你的大脑** —— 所有笔记纯文本存在本地，永不锁定。

2. **一个 AI 住在你的笔记软件里** —— 在 Obsidian 侧边栏和 Friday 聊天，它帮你记、帮你整理、帮你找。

3. **大脑不用你搭** —— 一份《Friday大脑蓝图》丢进空文件夹，对 Friday 说一句"照它搭建"，六个脑区自动建好。

## 📍 阅读地图

> 本文从头滚到尾，正好是上手的完整路径。也可以点右侧大纲（手机端点左下角"大纲"）直达任意一步：
> 
> [**第一章 · 三分钟看懂**](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnNFX4cPMvAWMl8ZWUR4kvSc) —— 五个工具为什么缺一不可（理论）
> [**第二章 · 三十分钟装好**](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcneYDvXWyXT3EiVstclkHdcH) —— 七步走，照着点就行（动手）
> [**第三章 · 玩转示例大脑**](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnRnuGasPu8mlkwNGna1S0mg) —— 11 个提示词见识 Friday 全力（测试）
> [**附录C · 常见问题 FAQ**](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnyixt5EY2FIPlh0lilI84Id) —— 卡住了来这里（排错）
> 
> 👉 **新手按顺序来，别跳。** 先懂再装最省心。
> 
> 

---

# 第一章 · 三分钟看懂：五件套怎么搭起来

> **先看懂，再动手。** 明白了"每个工具为什么存在"，第二章装起来就不迷糊。
> 
> 

## 一张图看懂

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzQ1M2RiYzUxOTYxNWJlYzc5ZGRlNzlmMzlhNWRlZmRfNWZlZWY0Yjg2ZjhlNTU3NTRhMmQyZGVhNTU2ZTkyYTVfSUQ6NzY1MDMyNDkyMTUzODc1OTY0Ml8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

你要给自己造一个 AI 第二大脑 **Friday**。它像一个真人助理，由**四层**搭起来，从外到内：

```
你
   │  说一句话
   ▼
┌─────────────────────────────────────────────┐
│ 1️⃣ Obsidian      ——  大脑的"身体"(你看得见的笔记软件)  │
│     └ 2️⃣ Claudian 插件 —— 让 AI"住进"Obsidian 侧边栏    │
│           └ 3️⃣ Claude Code —— Friday 的"引擎"(干活的 AI) │
│                 └ 4️⃣ cc-switch —— "芯片切换器"            │
│                       └ 5️⃣ DeepSeek V4 —— 便宜又免翻墙的"大脑芯片" │
└─────────────────────────────────────────────┘
```

更清楚的一张图（蓝 = 你看见/操作的，绿 = 幕后帮你思考的）：

下面**按"由表及里"的顺序**讲，每一层都是为了解决上一层的一个问题。

## 1️⃣ Obsidian —— 大脑的"身体"

**是什么**：一个**免费**的笔记软件。它打开的不是云端账号，而是你电脑上的一个**文件夹**，里面全是普通的 `.md` 文本文件。

**为什么需要它**：你的第二大脑得有个能看、能存、能打开的地方。Obsidian 就是这个"容器"。

- 纯文本，不锁定：换软件、换电脑，复制文件夹就全带走。

- 支持 `[[双链]]`：笔记之间能互相跳转，像维基百科。

- **它本身只是个记事本**——能存不能"想"。要让笔记会自己整理、会回答你，得给它接一个 AI。这就引出了下一层。

> 装完 Obsidian，新建一个空文件夹用它打开、放入一份《Friday大脑蓝图》，你就有了大脑的"图纸"——但现在它还是"植物人"，因为还没有 AI。等 AI 接好后，大脑会由它照图纸自己搭出来。
> 
> 

## 2️⃣ Claudian 插件 —— 让 AI"住进"Obsidian

**是什么**：Obsidian 的一个**插件**（社区插件，免费）。它在 Obsidian 侧边栏开一个聊天框，让你**直接在笔记软件里和 AI 对话**。

**为什么需要它**：AI 引擎（下一层的 Claude Code）本来是个**黑乎乎的命令行**工具——小白看到就劝退。Claudian 把它"包"进 Obsidian 里：

- 你永远不用碰命令行，在熟悉的笔记界面里点开侧边栏就能聊。

- AI 能直接读写你这个文件夹里的笔记——帮你建、帮你改、帮你找。

- 打字 `@` 提到某篇笔记、`/` 调用技能，都在侧边栏完成。

> ⚠️ 但 Claudian 只是个"外壳"。它自己不会思考，**底层得有一个真正干活的 AI 引擎**——那就是 Claude Code。
> 
> 

## 3️⃣ Claude Code —— Friday 的"引擎"

**是什么**：一个很强的 AI Agent 引擎（Anthropic 出品）。它能读你的文件、改你的文件、分多步帮你把一件事做完——这正是"第二大脑"需要的能力。

**为什么需要它**：Claudian（外壳）背后必须插一个引擎，Claude Code 就是这台引擎。Friday 的"聪明"来自这里。所以**不能只装 Claudian 而不装 Claude Code**——这是 Claudian 官方写明的硬性要求，缺了它插件根本动不了。

**但这里要分清两件事 👇**：装"Claude Code 这个引擎程序"本身**很简单**（粘贴一行命令，免费）；真正的坎在于它**默认要连 Anthropic 官方模型**，对国内小白来说那才麻烦：

- 要订阅、要付外币 💸

- 要登录账号 \+ 翻墙 🧱

- 还可能限速

> ✅ 所以记住：**引擎要装（一次性、不登录、不花钱），但"连官方模型"这件麻烦事我们不做。**
> 
> 

这正是原版 FridayOS"有技术门槛"的根源。**Lite 版把坎填平**——引擎照装，但改连一个**国产、便宜、免翻墙**的模型。这就引出最后两层。

## 4️⃣ DeepSeek V4 —— 便宜又免翻墙的"大脑芯片"

**是什么**：国产顶级大模型 **DeepSeek V4**（分 Pro / Flash 两档）。它提供一个"Anthropic 兼容接口"，意思是——**Claude Code 可以无缝改用它**，就像给同一台引擎换一颗芯片。

**为什么用它**：

- **免翻墙**：国内直连 `api.deepseek.com`。

- **便宜到离谱**：按用量付费，百万字（token）输入只要几毛钱。一杯奶茶钱够你用很久。

- **够聪明**：V4 Pro 支持超长上下文，写作、整理、编程都能打。

> 你要做的就一件事：去 DeepSeek 平台**注册、充点钱（¥10 起步就够体验很久）、拿一把 API Key（一串密码）**。这把钥匙，下一层要用。
> 
> 

## 5️⃣ cc\-switch —— "芯片切换器"

**是什么**：一个**图形化小工具**（免费桌面软件）。

**为什么需要它**：第 3 层说了，Claude Code 默认连 Anthropic。怎么让它改连 DeepSeek？

- **硬核做法**：手动改一堆"环境变量"——小白噩梦，一个字母打错就报错。

- **cc\-switch 的做法**：打开它 → 在列表里选 "DeepSeek" → 粘贴你的 API Key → 点一下"同步"。**两下点击搞定**，Claude Code 就乖乖去连 DeepSeek 了。

cc\-switch 就是那个"开关 / 切换器"：DeepSeek 是电，cc\-switch 是闸刀。有了它，你不用懂任何代码，就能让 Friday 用上便宜的国产芯片。

> 之后想换别的国产模型（Kimi、智谱 GLM 等），也是在 cc\-switch 里点一下就切，不用重装任何东西。
> 
> 

## 串起来：一句话总结

> **Obsidian** 是身体，**Claudian** 把 AI 请进身体，**Claude Code** 是 AI 引擎，**cc\-switch** 把引擎接到 **DeepSeek V4** 这颗又便宜又免翻墙的芯片上。五件套合起来，就是会自己整理、随叫随到的 **Friday**。
> 
> 🏗️ 这就是整套方案的核心架构：**借 Claudian 的壳（Obsidian 集成界面）\+ DeepSeek 模型（便宜芯片）\+ Claude Code Agents（AI 引擎）**——偷梁换柱，绕过 Claude 原生依赖。这既是 Lite 版能把门槛降到"零翻墙、几毛钱"的技术基础，也是中国 AI 应用生态里的一条完整跑道。
> 
> 

## 搭好后，你的大脑长这样

六个脑区，理念全部写在《Friday大脑蓝图》里（第二章第 5 步领取）：

|脑区|文件夹|一句话|
|---|---|---|
|📥 收件箱|`inbox/`|随手记——先接住，晚点整理|
|🎯 工作台|`exec/`|正在做——手头 3〜7 件事 \+ 周计划/每日记录|
|📚 知识库|`wiki/`|值得长期留的，双链互连|
|⚙️ 技能区|`skills/`|重复的事变套路（进阶）|
|📦 资料库|`raw/`|原始资料——只读不改|
|🫀 中枢|`system/`|大脑说明书（`CLAUDE.md`）|

## 省 token 是架构出来的

六脑区不只是整洁——**它是 Friday 便宜得离谱的根本原因**。聚合查询扫结构化 frontmatter（每档几十 token）而不读全文；每个域有总览地图（MOC），Friday 从一页出发而不是翻十一页；问题只打开它所属的脑区；套路沉淀在 `skills/` 里按名调用，不用每次重新解释。

DeepSeek V4 实测（169 文件知识库）：搭建大脑 **¥0\.10**，一条跨百档案的复杂分析 **约 ¥0\.02**，连跑 11 条共 **¥0\.26**。一个真实 10 人团队用这套架构跑了整周——用得最猛的人花费不到 **¥20**。

理论讲完了。接下来，30 分钟把它装出来。👇

---

# 第二章 · 三十分钟装好：七步走

> 跟着点就行。**全程约 30 分钟，不用会写代码，不用翻墙。** 卡住了随时跳 [附录C · 常见问题 FAQ](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnyixt5EY2FIPlh0lilI84Id)。
> 
> 

> 📱 **正在用手机看？** 安装要在电脑上进行。点飞书的"发送到电脑"或把本文链接发给自己，换电脑打开再开始。
> 
> 

## 📋 开始前：你需要准备

|项目|说明|
|---|---|
|💻 一台电脑|Windows 或 Mac 都行（Claudian 暂不支持手机/平板）|
|🌐 能上网|**不需要翻墙**，普通网络即可|
|⏱️ 约 30 分钟|第一次装，慢慢来，超时也正常|
|💰 约 ¥10|给 DeepSeek 充点钱（用量极省，¥10 能体验很久）|

## 🎬 安装分三幕，一幕一个场景，不来回切换

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MThmZTRhYzQ0OGFiZDM5NTQ3Yjk2YmY0OGQ1YjYzMzlfNzMyNTIwODU4NDVkZDkyNDA1OWQxNGQwYjg0ZDlkN2RfSUQ6NzY1MDMyNDkyMTk5ODc3MzIwOV8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

第一章是按"由表及里"**讲**的；动手装则按"由里及表"——先把幕后装完，最后才见 Friday，每一幕只待在一个软件里：

```
第一幕 幕后准备（命令行，装完永远不用再碰）：第1步 Node.js → 第2步 Claude Code 引擎
第二幕 接上便宜芯片（钥匙拿到立刻就用）：    第3步 DeepSeek 拿 Key → 第4步 cc-switch 接线
第三幕 见到 Friday（全程不离开 Obsidian）：  第5步 Obsidian+蓝图 → 第6步 Claudian → 第7步 一句话搭出大脑
```

## 第 1 步：装 Node\.js（地基，5 分钟）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmQ5N2I1ZThiMjE2YmRlODUwZDY2Y2YwODkyNjJiYzJfZGY5ODIzMWYyODZmOWY4NmE0YmY4MTkyMjg0OWJlMjBfSUQ6NzY1MDMyNDkyMzk5MDgzODI1MF8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

> 🎬 **第一幕 · 幕后准备**：这两步在命令行完成，一次性装完，以后永远不用再碰。
> 
> 

**为什么**：Claude Code 和 cc\-switch 都是建在 Node\.js 上的，它是"地基"。装一次，以后不用管。

1. 打开官网 👉 [**nodejs\.org**](https://nodejs.org)

2. 点页面上那个 **"LTS"**（长期支持版）的大按钮，下载安装包。

3. 双击安装，**一路点"下一步 / Next"** 到底，全部用默认即可。

4. 验证：

    - Windows：按 `Win + R`，输入 `cmd`，回车，打开黑色窗口。

    - Mac：打开"终端 / Terminal"。

    - 输入这行再回车：

        ```
        node -v
        ```

    - 屏幕上**冒出一串版本号**（比如 `v20.11.0`）就成功了 ✅。看不懂没关系，有数字就行。

## 第 2 步：装 Claude Code 引擎（一次性，免登录，免翻墙，5 分钟）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGVmMjk4N2Y0NTU5M2IyZjBhY2ZhOTZiODQ0MThjYjNfZjk3MmY5NjNmMDQzMTljNjdhZDFlN2FkZDg1MmI0MTVfSUQ6NzY1MDMyNDkyNTA5NDIzNTA2OF8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

**为什么必须装**：很多人以为"装了 Claudian 就够了"，其实不是——**Claudian 只是个外壳**，它自己不会思考，背后是把 Claude Code 当引擎在调用（这是它官方写明的硬性要求）。没有这个引擎，Claudian 会报 `spawn claude ENOENT` 之类的错，根本动不了。

> ✅ **放心**：这一步**只是装个引擎程序，不用订阅、不用登录 Anthropic 账号、不用翻墙**。那些要花钱、要翻墙的部分，第二幕用 cc\-switch \+ DeepSeek 全替你免掉了。一句话：**Claude Code = 引擎（装一次就好）；cc\-switch = 给引擎换上 DeepSeek 便宜芯片。**
> 
> 

1. 打开命令行窗口（Windows：`Win+R` → `cmd` → 回车；Mac：打开"终端"）。

2. **复制下面这一整行**粘进去，回车（用的是国内镜像，**不用翻墙**，对所有网络环境都更快更稳）：

    ```
    npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
    ```

    > 💡 代码块右上角有复制按钮，点一下就复制整行。如果你的网络访问国外很流畅，也可以去掉 `--registry=...` 部分直接用官方源，效果相同。
    > 
    > 

3. 等它跑完（可能要一两分钟，刷一堆字是正常的）。

4. 验证：输入

    ```
    claude --version
    ```

> 💡 装的时候先别急着运行 `claude` 去登录——它默认连的是要花钱、要翻墙的官方模型。第 4 步 cc\-switch 会把它改连 DeepSeek，之后就不用登录、不用翻墙了。
> 
> 

## 第 3 步：注册 DeepSeek \+ 充值 \+ 拿 API Key（5 分钟）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWUyODVmMjg4YTY5YzU4NjQ1YmRhMmUzMDRjOGI4M2JfMmRmMzc4NzQ1NTEyN2VjZjMwYzg3ZTE2OWRmYmU4ZjJfSUQ6NzY1MDMyNDkyNjUxMTM2OTE1Ml8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

> 🎬 **第二幕 · 接上便宜芯片**：钥匙拿到手，下一步立刻就用——不用存着等。
> 
> 

1. 打开 👉 [**platform\.deepseek\.com**](https://platform.deepseek.com)

2. 用手机号 / 邮箱**注册并登录**。

3. **充值**：找到"充值 / 余额"，充 **¥10** 就够体验很久（按用量扣费，省得很）。

4. **创建钥匙**：左侧点 **"API keys"** → **"创建 / Create new API key"** → 给它起个名字（随便，比如 `friday`）。

5. ⚠️ **极其重要**：弹出的那串 `sk-xxxxxxxx...`**只显示这一次！** 立刻**复制**，粘贴到记事本里**临时存好**（马上第 4 步就用）。万一没存到——别慌，删掉重新建一把就行。

> 🔒 这把钥匙 = 你账户的密码，**别发到群里、别上传网上**。
> 
> 

**顺便记住这两个值，下一步要填：**

- 接口地址（Anthropic 兼容）：`https://api.deepseek.com/anthropic`

- 模型名：`deepseek-v4-pro[1m]`（主力，聪明）和 `deepseek-v4-flash`（轻快，省钱）

## 第 4 步：装 cc\-switch \+ 接上 DeepSeek（3 分钟）⭐ 关键一步

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWUzNTQxM2I2MmMxOWNiZDIyZTc2N2MxMjc2Zjg1MGFfNjI4NzE0YmI5Y2JjYjhkNTIyOGJkZDM2ZDAwMzEyN2RfSUQ6NzY1MDMyNDkyNTEzMjE4MDQ0Ml8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTA3MDZhYWMwNjk0MzU3YWNlY2FhY2U2YmI3YzVjZDNfZWFiNjdiNTg5MGIyMDZmZmU3YTM4NjllMDE3Y2U0MTVfSUQ6NzY1MDMyNDkyNzAxOTIwNzYzNl8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

**为什么**：cc\-switch 是"切换器"，点两下就让上一步的引擎改用 DeepSeek 芯片，不用碰任何代码。

1. 打开官网 👉 [**ccswitch\.io**](https://ccswitch.io)（或 [GitHub 下载页](https://github.com/farion1231/cc-switch/releases)）。

> ⚠️ 浏览器可能会弹出安全警告（第三方分发工具的通用现象），手动点 `…` → `保留` → `仍然保留` 即可通过。
> 
> 

2. 下载对应你系统的安装包：

    - Windows 选 `.msi` 或 `.exe`；Mac 选 `.dmg`。

    - 

        - 下载后双击安装，一路默认。

    > ⚠️ **不要装到 E 盘**（除非已提前给 E 盘加好"完全控制"权限）。AI 需要在该盘新建和修改文件，若缺少权限会持续弹窗报错。安装在 C 盘最省心——权限最大，不会卡。
    > 
    > 

3. 打开 cc\-switch，顶部默认就是 **Claude** 这一栏（我们就用这个）。

4. 点右上角 **"\+"** 新建一个 Provider（服务商）：

    - 在预置列表里找到并选择 **DeepSeek**。

    - **API Key**：粘贴你第 3 步存的那串 `sk-...`。

    - **接口地址 / Base URL**：确认是 `https://api.deepseek.com/anthropic`。

    - **模型名**：填上 `deepseek-v4-pro[1m]` 和 `deepseek-v4-flash`（`[1m]` 表示开启超长上下文，建议留着）。

    - 保存。

5. 进 cc\-switch 的 **设置 / Settings**，打开这两个开关（让一切自动化、少弹窗）：

    - ✅ **Apply to Claude Code Plugin**（让 cc\-switch 接管模型切换）

    - ✅ **Skip Claude Code Initial Setup**（跳过首次啰嗦的设置）

6. 回到主界面，**选中刚建的 DeepSeek**，点 **"同步 / Sync to All Apps"**。

> 🎉 现在 Claude Code 引擎已经在用 DeepSeek 了！点 cc\-switch 右上角小箭头可查流量/余额，确认充值到位。（以后想换 Kimi、智谱 GLM，也是在 cc\-switch 里点一下就切。）
> 
> 

## 第 5 步：装 Obsidian \+ 建一个空文件夹 \+ 放入蓝图（5 分钟）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDA0MjlkNDU0MDJiZGM2NDI3ODdhNWM0MmYzMjE1NjhfNDc2YWU1MWM0NTc1MDllNzE4NTc2Y2NhY2ExYzY5Y2JfSUQ6NzY1MDMyNDkyOTMzMDEwNTI5M18xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

> 🎬 **第三幕 · 见到 Friday**：幕后全部就绪。从这里开始全程待在 Obsidian 里，一路走到 Friday 上线。
> 
> 

**为什么**：Obsidian 是你第二大脑的"身体"。这一步只需要：一个**空文件夹**，加**一份文档**。

1. 打开官网 👉 [**obsidian\.md**](https://obsidian.md) → 点 **"Download"** → 选你的系统下载 → 双击安装。

1. 在电脑上**新建一个空文件夹**，起名比如 `我的大脑`。

> 💡 建议放在 **E 盘**（空间大，后续 AI 分析文件统一管理），路径如 `E:\我的大脑`。装好后的"仓库"（vault）就用这个文件夹——所有笔记、AI 分析结果都在里面，随文件夹整体备份或迁移。
> 
> 

2. **领取《Friday大脑蓝图》**——这是全套流程里唯一要进你电脑的文档，就在下面，点击下载，移动到 `我的大脑` 文件夹里：

    > 💡 不想下载文件？用**一键复制法**：去 [附录A · 蓝图全文](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnuPqxYXACn3juwS17UzXazd) 点代码块的复制按钮 → Obsidian 里 Ctrl\+N 新建笔记命名"Friday大脑蓝图" → Ctrl\+V，效果完全一样。
    > 
    > 

3. 打开 Obsidian，第一个界面点 **"Open folder as vault"（打开文件夹作为仓库）**，选中 `我的大脑` → 打开。

4. 左侧能看到那份《Friday大脑蓝图》，点开**先读一遍**——它就是你第二大脑的全部图纸。

> 此刻你的大脑只有一份"图纸"，还没盖楼——别急，也**不用自己动手建文件夹**。等第 7 步，Friday 会照着图纸自己把楼盖起来。
> 
> 

## 第 6 步：装 Claudian，把 Friday 请进 Obsidian（3 分钟）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGQ3OWQ1MDE2NGIwYzczZjlmMjQ1MTA4MWE5NjUxNmZfYmJlYzIzNmQwZWQ0ZWU3ZjMxZDk5NDZhZGM2MzI5YzZfSUQ6NzY1MDMyNDkzMDE0NDQwNjQ2OF8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

**为什么放最后装**：引擎和芯片都接好了，现在让 AI"住进"你的笔记软件，从此告别命令行。

> ⚠️ **Claudian 在中国区 Obsidian 社区插件里搜不到**（区域过滤——中国区没有 Claude，这个插件被自动屏蔽了，搜出来只有不相关结果）。必须手动安装。
> 
> 

\[claudion\.zip\]

1. 从 Friday 团队获取 `claudian` 插件文件夹👆。

2. 解压得到 `claudian` 文件夹。

3. 打开 Obsidian → 左下角 **设置（齿轮）** → **第三方插件** → 先**关闭安全模式**。

4. 点 **"打开插件文件夹"**（一个小文件夹图标），把解压出的整个 `claudian` 文件夹**拖进去****（注意：文件位置必须为plugins\\claudion）**。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTQzZThmZjhiMTE1ZWJiNDYxYzlkYTJiZDYwMWQ5OWNfODY5YmEyNTJhMzk2NjJkMzE1MmYxYzM0ZmNkNTk1NjBfSUQ6NzY1MDQwNjIyMTM0MTk2OTM4OV8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

5. 关掉文件夹窗口，回到 Obsidian 设置页 → **刷新** → `Claudian` 出现在插件列表 → 点**开启**。它会自动用你电脑上那台、已经被 cc\-switch 接到 DeepSeek 的 Claude Code 引擎。

6. 关掉设置。Obsidian 左下角出现 🤖 小机器人图标 → 点开就是和AI Agent的聊天框。

> 💡 一个细节：每个 Obsidian 仓库的插件是独立的，换仓库要重新装一次。
> ⚠️ 要求 Obsidian 版本 ≥ 1\.8\.9（新装的肯定满足）。仅支持电脑端。
> 
> 

## 第 7 步：一句话，让 Friday 自己把大脑搭出来 ✨

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzBiNzM3MGRjOGQ1ZWZjZTVkZThhNzI0OWQzNGY2ZTZfNTc1NjYxNGM5Y2NiNWZlYTI4NTFjYTQ4OWEwZmVhNDhfSUQ6NzY1MDMyNDkzMjY0MzgwMjA5MV8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

工具全部就位。现在见证 Friday 的第一次表演。在 Claudian 聊天框里说：

> **请阅读《Friday大脑蓝图》，按照它把我的大脑搭建起来。**
> 
> 

Friday 会照着蓝图自己动手：建好六个脑区、写好行为契约（`system/CLAUDE.md`）、装上三份建档模板和三个起步技能（清理 inbox、每周回顾、导入资料）、建好本周计划和决策日志——然后**反过来采访你三个问题**（怎么称呼你、大脑主要管什么、喜欢什么风格），把你的偏好写进它的说明书。**全程你一个文件夹都不用建，结束时它已经认识你了。**

搭完后再试一句：

> **你好 Friday，帮我记到 inbox：明天下午三点和张总开会。**
> 
> 

如果它在 `inbox/` 里自己建好了笔记——

🎉 **恭喜，你的 AI 第二大脑 Friday 正式上线了！**

接下来怎么用（每日计划、周计划、清理 inbox 的口令），蓝图第七节都写了。再试试：

- "帮我把这周要做的三件事放进 exec。"

- "帮我清一下 inbox。"

- **把你的真资料搬进来**："把这个文件夹搬进来：（粘贴文件夹地址）"——Friday 会复制到 raw/（绝不动原件）、出搬家报告、再给你三个整理选项。**这是大脑第一次装上"你自己的记忆"。**

> 💡 怎么复制文件夹地址：Windows 在文件管理器里**按住 Shift 右键文件夹 → "复制文件地址"**（或点上方地址栏复制）；Mac **右键文件夹按住 Option → "拷贝…的路径名称"**。
> 
> 

> ✅ 搭完它会自动输出一张**自检清单**（蓝图第六节第 11 步）；如果没有，对它说"按蓝图第六节第 11 步自检"。
> 
> 💡 万一 Friday 没动手或搭得不对：让它"删掉刚才建的，重新严格按蓝图第六节执行"；或者按蓝图里的"手动兜底"自己建 6 个文件夹，两分钟的事。
> 
> 

## 🆘 这一章卡住了？

|现象|怎么办|
|---|---|
|`node -v` / `claude --version` 没反应|关掉命令行窗口**重新打开**再试；确认上一步装完了|
|`npm install` 报红、很慢|镜像或网络问题，重试一次；详见 [附录C · 常见问题 FAQ](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnyixt5EY2FIPlh0lilI84Id)|
|Friday 不回话 / 报余额错误|多半是 DeepSeek 没充值，或 cc\-switch 里 Key 贴错了|
|Claudian 搜不到|确认 Obsidian 已"开启社区插件"，版本 ≥ 1\.8\.9|
|Friday 不按蓝图搭建|确认蓝图文件在 vault 根目录；让它"重新严格按蓝图第六节执行"|

装好了，但大脑还是空的，很难体会它强在哪。下一章给你一个**装满数据的现成大脑**直接把玩。👇

---

# 第三章 · 玩转示例大脑：11 个提示词

> 你现在是**云栈科技的创始人**：杭州一家 100 人的仓储软件公司。今年最大的单子交付告急、核心员工被竞对盯上、银行授信要续期、A\+ 轮资方下周来访。这个文件夹是你的第二大脑，**Friday 是你的私人助理**，替你打理它。
> 
> 

## 📦 第 0 步：下载示例大脑

\[示例大脑\-云栈科技\.zip\]

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yjg3YzY5N2U2YjBmZDBhM2RmODA2NDlhMjFjMmY0ZTBfNTY3MDE0NmVkMWNiMTQyNTc5ZGI3OGQ1YzZhMjNhMDhfSUQ6NzY1MDMyNDkzMzM5MDIyNDM3MV8xNzgxMjcxNTQ2OjE3ODEzNTc5NDZfVjM)

下载 → 解压 → 用 Obsidian **"Open folder as vault"** 打开解压出的文件夹。

> ⚠️ **两个必读提醒**
> 
> 1. **示例大脑开箱即用，不需要搭建**——"照蓝图搭建"那句话是给你自己的空文件夹用的，别在这里说。
> 
> 2. **先装插件再玩**：这是个新 vault，Obsidian 插件按 vault 各管各的——先按 [第 6 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnMzTeILLIPzoK5SXFHgnnoc) 在这里把 Claudian 再装一遍（插件已下载过，半分钟点完）。
> 
> 

**玩法**：打开 Claudian 聊天框，把下面的提示词逐条丢给 Friday。每条都带：🎯 它在演示什么能力 → 🥊 为什么免费对话框做不到 → 📖 "答案方向"（**先自己跑，再看**；精准度因模型而异，见排错区第 3 条）。

## 为什么创始人需要 Friday

调研里反复出现的三件事：高管平均每周近 23 小时在开会，会前却没时间准备；软件行业项目尾款纠纷一年激增 67%，根源是合同、开票、回款记录散落在不同部门；SaaS 客户流失"在报表里看不见，直到为时已晚"。

**这些痛的共同根源只有一个：信息散落在十个地方，而你的脑子只有一个。**

第二大脑把人、项目、客户、合同、应收、日程放进同一个文件夹并互相链接；Friday 作为助理，替你在里面跑腿、串线、算账、备会。下面 11 条提示词，就是创始人的一天。

## 这个大脑里有什么

|脑区|内容|
|---|---|
|📥 `inbox/`|7 条随手记：客户抱怨、挖人传闻、银行要材料、产品灵感…（每条都有后续）|
|🎯 `exec/`|本周计划、核心人才保卫战、融资准备、**决策日志**（拍过的板和理由）|
|📚 `wiki/`|**100 名员工档案** \+ 11 个项目 \+ 6 个客户 \+ 部门 \+ 三张总览地图，全部双链互连、frontmatter 结构化|
|⚙️ `skills/`|10 个沉淀好的套路：经营周报、借调分析、人才盘点、回款催收、续费预警、会前简报 \+ 4 个真实行政场景|
|📦 `raw/`|花名册、应收台账、续费台账、**合同关键条款**、日程导出、对账双表、费用明细（只读事实源，**全部可真跑**）|
|🫀 `system/`|Friday 的行为契约 \+ 5 份建档模板（物料标准）|

> 📊 **实测参考**（DeepSeek v4\-pro，2026\-06）：11 条同会话连跑约 28 分钟，单条 30 秒\~1 分半，**总成本约 ¥0\.26**。
> 
> 

## 🧯 通用排错（任何一条跑不出来，先试这三句）

1. **"请先读 system/CLAUDE\.md 和相关的 skill 文件，再回答。"**（提醒它守契约）

2. **"注明每条结论来自哪份笔记。"**（逼它真的去翻库，而不是编）

3. **答案的精准度取决于模型的推理能力，不取决于这个库**。同一份知识库：强推理模型会精确点名、算出具体金额、主动引用文件；轻量模型可能只给出大概方向，甚至漏掉关联——这不是 Friday 的问题，换强模型再跑一次即可。**推荐 ****`deepseek-v4-pro[1m]`**** 或其他高推理能力的模型**；`flash` 类轻量模型只适合单文件的简单任务（如⑩），跑串联类（②③⑦）会力不从心。

## 🔥 第一幕：救火的上午（多知识串联）

### ① 跨项目借人

> **宁波东海港项目后端进度落后两周，帮我从别的项目借两个后端增援。要求绩效 B\+ 以上、不在关键交付期的项目里。给我人选和理由。**
> 
> 

🎯 **演示什么**：AI 沿双链自己跑——项目总览找"收尾/搁置"项目 → 翻成员档案核对绩效和老板备注 → 给人选表。
🥊 **对话框做不到**：它没有你的 100 人数据，更不会"沿着链接自己找"。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：人选应来自"收尾 ✅ / 维保 ✅ / 半搁置 ⏸️"状态项目的后端成员，每个人选附绩效和理由；**不应该**推荐正处于关键交付期、或老板备注里有流失风险标记的人。强推理模型会精确点名并注明出自哪份档案。
> **没跑出来怎么办**：追问"先看 wiki/项目/项目总览，候选只能来自收尾/维保/搁置状态的项目"。
> **功能解读**：员工档案 frontmatter 里有绩效职级、项目页里有状态字段——这就是"物料规范"的回报。
> 
> 

### ② 算清延期的代价 ⭐ 全场最佳

> **如果东海港最终延期两周上线，按合同我们要付出什么代价？把违约金、尾款回款、二期机会都算上，然后和"借调两人增援保住 7/31"的方案比一比，给我结论。**
> 
> 

🎯 **演示什么**：合同 × 财务 × 商务 × 人力**四个域的串联计算**——现实里要 CFO、法务、销售、CTO 四个人开一小时会。
🥊 **对话框做不到**：它连你的合同都没见过。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：三笔账都要出现——按周计算的合同违约金、验收尾款的回款顺延、二期合作机会的悬置风险；再对比增援方案（内部人力重分配，额外成本极低），结论应明确倾向增援。强推理模型会算出具体金额并引用合同条款编号；轻量模型可能只列风险不算账。
> **没跑出来怎么办**："先读 raw/东海港合同关键条款摘录 和 raw/应收账款台账2026\-06\.csv，再算。"
> **功能解读**：知识库\+Agent 的核心价值——**分散在四个部门的事实，在一个文件夹里串成一笔账**。
> 
> 

### ③ 上周那条随手记

> **上周我记了一条韩磊的事，结合他的档案、所在项目、我们的保卫战计划和决策日志，评估风险有多大，给我挽留方案。**
> 
> 

🎯 **演示什么**：**永不过期的记忆**。随手记的一句话，一周后还能连同所有上下文一起翻出来。
🥊 **对话框做不到**：上周的对话它早忘了。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：至少串起四处——inbox 里的挖人线索、员工档案（绩效/薪酬/不可替代性）、所在项目的重要性、决策日志里已拍过的相关板；挽留方案应是"薪酬\+期权\+培养 backup 解除单点"的组合拳，而不是单一加薪。
> **没跑出来怎么办**："先搜 inbox 里关于韩磊的记录，再翻 exec/核心人才保卫战\.md 和决策日志。"
> **功能解读**：随手记的一句话，一周后连同所有上下文一起被翻出来——记忆在文件夹里，永不过期。
> 
> 

## 💰 第二幕：经营的下午（聚合分析）

### ④ 薪酬倒挂体检

> **帮我看看后端序列有没有薪酬倒挂——对比近一年新入职的和司龄三年以上的同职级老员工。有的话给调薪建议，参考 raw 里的薪酬调整方案。**
> 
> 

🎯 **演示什么**：把 100 个 md 文件**当一张表查**——frontmatter 结构化字段的威力。
🥊 **对话框做不到**：没有花名册，只能写《什么是薪酬倒挂》小作文。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：能在同职级、同岗位序列中发现"新人薪资高于高绩效老员工"的倒挂组合，并按 raw/ 里的调薪制度给出可执行路径（调薪窗口、特批通道）。强模型会给出具体对子和差额。
> **没跑出来怎么办**："扫 wiki/团队 全部档案 frontmatter 的 职级/月薪k/入职 字段，按同职级同岗位分组对比。"
> **功能解读**：100 个 md 文件被当成一张表查——frontmatter 结构化的威力。
> 
> 

### ⑤ 应收摸底（银行周二就来）

> **inbox 里记了银行周二来谈授信续期。老规矩，过一遍应收：哪些要催、哪些能提前、哪些有风险，谁去办。**
> 
> 

🎯 **演示什么**："老规矩"\+台账\+项目状态联动——回款不是财务一个部门的事。
🥊 **对话框做不到**：不知道你的台账，更不知道"验收过了没开票=白白压钱"这条你们自己的规矩。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：输出应是分级清单——已逾期的（政企客户要先问卡在哪个审批节点）、验收已过可提前开票的、系于交付节点有风险的；每条派到具体的人。加分项：主动联想到这正是银行要的应收明细材料。
> **没跑出来怎么办**："按 skills/回款催收\.md 的步骤跑 raw/应收账款台账2026\-06\.csv。"
> **功能解读**：回款不是财务一个部门的事——台账×项目状态×合同条款联动才看得全。
> 
> 

### ⑥ 续费风险扫描

> **扫一遍智仓WMS的续费风险，算出风险敞口，每家给动作建议。**
> 
> 

🎯 **演示什么**：流失风险在报表里"看不见直到太晚"——但在台账\+规则里看得见。
🥊 **对话框做不到**：没有你的客户健康数据。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：按 skill 里的规则（续费临近 \+ 健康分低/活跃下降）筛出高风险客户，给出风险敞口的合计金额，并对每家给动作建议——核心是**先做使用回访，不直接催续费**。
> **没跑出来怎么办**："按 skills/续费预警\.md 的规则扫 raw/智仓WMS续费台账2026\.csv。"
> **功能解读**：流失风险在报表里"看不见直到太晚"，但在台账\+规则里看得见。
> 
> 

## 🤝 第三幕：助理的日常（默契与沉淀）

### ⑦ 会前简报

> **周三要和东海港周总开进度会，老规矩，会前简报。**
> 
> 

🎯 **演示什么**：助理的看家本领——开会前 5 分钟，一页纸，不被打措手不及。
🥊 **对话框做不到**：它不知道你周三有会，更不知道周总上周抱怨过什么。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：一页纸结构应齐全——雷区置顶（应来自 inbox 里客户的抱怨 \+ 合同里的验收条款）、上次说到哪（客户页时间线）、本次目标与可让步空间、对方可能问的问题。强模型会把验收标准原文逐条列出。
> **没跑出来怎么办**："按 skills/会前简报\.md 跑：客户页时间线 \+ 项目页风险 \+ 合同摘录 \+ inbox 搜周总。"
> **功能解读**：开会前 5 分钟读一页纸，不被打措手不及——这就是助理的价值。
> 
> 

### ⑧ 一句"老规矩"

> **老规矩，出本周经营周报。**
> 
> 

🎯 **演示什么**：偏好写进契约，套路沉淀成技能——**说一次，管永远**。
🥊 **对话框做不到**：每次都要从头解释格式和口吻。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：格式必须是 skill 里写死的四段（三件大事 → 风险雷达 → 待你拍板 → 下周聚焦）；内容应来自库里真实悬而未决的事，而不是泛泛而谈。如果写成了散文，说明没读 skill——用排错第 1 句。
> **功能解读**：偏好写进契约，套路沉淀成技能——说一次，管永远。
> 
> 

### ⑨ 资方来访全套接待

> **下周四青桐资本来访（inbox 记了，日程原文在 raw），按接待包 skill 出全套。**
> 
> 

🎯 **演示什么**：一封乱邮件进，五件套出；顺带考它会不会**主动发现日程冲突**。
🥊 **对话框做不到**：模板、规矩、日程都在你的库里。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：五件套齐全（内部日程表/欢迎屏文案/司机简表/座位安排/准备清单），且**禁忌信息置顶**（skill 里写明的规矩）；司机简表应只保留司机需要的信息。彩蛋：强模型会主动发现当天日程里埋的一处会议冲突。
> **没跑出来怎么办**："对照 raw/下周日程导出，检查当天有没有安排冲突。"
> **功能解读**：一封格式随意的邮件进，全套标准物料出。
> 
> 

### ⑩ 行政的活也全包（真实场景移植）

> **拿 raw 里的《IT资产白名单》对《在线记录》，按对账 skill 把异常找出来。** 之后再试：**出上半年行政费用分析。**
> 
> 

🎯 **演示什么**：来自一家真实公司人力行政团队的实战（10 人全员上手，人均一周 token 不到 ¥20）。
🥊 **对话框做不到**：1000\+ 条对账它接不住，也不懂"新增一列别覆盖原件"的规矩。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：对账结果应分三类异常（不在白名单的陌生 IP / 整周无记录 / 深夜未关机），并且**另存新文件、不动 raw/ 原件**；费用分析应抓出明显异常的月份并用备注归因，每个图表配一段人话洞察。
> **没跑出来怎么办**：对账时强调"双向核对：A 有 B 无、B 有 A 无、字段冲突三类都要查"。
> **功能解读**：真实团队验证过的场景——上千条人工对账要一两天，AI 几分钟。
> 
> 

### ⑪ 把好答案变成永久技能

> **刚才这套"延期代价测算"很好，沉淀成 skill，以后我说"算一下 XX 项目延期代价"你就照做。**
> 
> 

🎯 **演示什么**：大脑越用越聪明——**这是和对话框的本质区别**。
🥊 **对话框做不到**：用完即焚。

> 📖 **答案方向（先自己跑，再看这块）**
> **方向**：应产出一个新的 skill 文件，结构符合 `system/模板/Skill模板.md`（frontmatter、触发语、步骤、固定输出格式、踩坑栏），且步骤写得换一个项目名也能跑。
> **验收方法**：新开一轮对话换个项目问延期代价，看它会不会自动调用新 skill。
> **功能解读**：大脑越用越聪明——这是和对话框的本质区别。
> 
> 

> 💡 那家真实团队的一句话送给你：**"淘汰你的不是 AI，是用 AI 的人。"**
> 
> 

## 🔬 对照实验（建议真做一次）

把提示词②原样贴到任意免费大模型对话框里：

||免费对话框|你的第二大脑|
|---|---|---|
|数据|"请提供贵司合同条款"|合同、台账、档案就在本地|
|串联|无链可循|合同×应收×客户×人力 四域自动串|
|记忆|上周的事忘了|inbox \+ 决策日志，白纸黑字|
|懂你|每次自我介绍|契约 \+ 10 个 skills，说一次管永远|
|成长|用完即焚|好答案沉淀成新技能|

## 📐 顺便：好的知识库物料长什么样

这个库同时是一份**物料标准样板**——Friday 表现好不好，七分取决于物料质量。三条铁律（细则见 `system/CLAUDE.md` 的"物料规范"）：

1. **frontmatter 是数据库**：每份档案头部的结构化字段让 AI 能把 100 个文件当一张表查。

2. **raw 是事实源，wiki 是视图**：原件只读、派生可改、冲突以原件为准。

3. **模板 \+ 总览**：建档从 `system/模板/` 起步；每个域有总览页（MOC）做地图。试试只看 `[[项目总览]]` 能不能 30 秒看懂全公司。

> 建自己的大脑时，把 `system/模板/` 整个拷走，就是现成的起步标准。
> 
> 

## 玩完之后

- 看知识网络：Obsidian 左侧点 **关系图谱（Graph view）**——100 人和项目客户连成的星系 ✨

- 搭自己的大脑：回 [第 7 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnl3dF655nUJNgaI8vooxz3g)，一句话搭一个空白的

- ⚠️ 本库所有人名、公司、数据均为虚构，仅供演示

---

# 附录A · 《Friday大脑蓝图》全文（一键复制）

> 给不想下载文件的同学：点击下方代码块**右上角的"复制"按钮**（全文一次性复制）→ 回到 Obsidian 按 **Ctrl\+N** 新建笔记，命名为 **Friday大脑蓝图** → **Ctrl\+V 粘贴** → 完成，回 [第 5 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnL1Z3he6E8f9qyd8P89iPtc) 继续。零文件操作，不可能出错。
> 
> 

```markdown
# 🧠 Friday 大脑蓝图 · The Blueprint

> **这一份文档，就是你第二大脑的全部图纸。**
> 不用下载模板、不用建仓库——把这份文件放进一个空文件夹，
> 在 Claudian 聊天框里对 Friday 说一句：
>
> **"请阅读《Friday大脑蓝图》，按照它把我的大脑搭建起来。"**
>
> 它会建好六个脑区、给自己写好行为契约、装上起步模板和技能，
> 最后**反过来采访你三个问题**，把你的偏好写进它的"说明书"。✨
>
> （还没装好 Obsidian + Claudian？先看 [`安装指南.md`](./安装指南.md)。）

---

## 一、理念：一个文件夹就是一个大脑

人脑擅长思考，不擅长存储——会忘、会乱、会丢。第二大脑就是给你外接一块"不会忘的记忆"，而 Friday 是住在里面、替你打理它的管家。

三个底层原则：

1. **一个文件夹就是一个大脑。** 所有笔记是最普通的 `.md` 纯文本，没有数据库、不被任何软件锁定。换电脑、换软件，复制文件夹就把整个大脑带走。
2. **笔记是流动的，不是堆积的。** 大多数笔记软件变成"只进不出"的仓库。这里的知识有生命周期：随手记的（`inbox`）→ 在做的（`exec`）→ 值得长期留的（`wiki`）→ 反复做的变成套路（`skills`）。流不动的，删掉。**分区还直接省钱**：Friday 按区取用、扫 frontmatter 表头而不读全文，实测一条跨上百份档案的分析只要约 ¥0.02。
3. **你负责想，Friday 负责记。** 你随口一句话，Friday 判断放哪、建好笔记、补好格式；你提一个问题，它先翻你的大脑再回答。能它整理的，不让你整理。

## 二、六个脑区

| 脑区 | 文件夹 | 一句话 | 放什么 |
|---|---|---|---|
| 📥 收件箱 | `inbox/` | 先接住，晚点整理 | 突然的想法、聊天关键句、待读链接 |
| 🎯 工作台 | `exec/` | 正在做的 3〜7 件事 | 本周计划、当前任务、决策日志 |
| 📚 知识库 | `wiki/` | 值得长期留的 | 整理好的笔记、概念、人和事 |
| ⚙️ 技能区 | `skills/` | 重复的事变成套路 | 你常让 Friday 做的固定流程 |
| 📦 资料库 | `raw/` | 原始资料，只读不改 | 原文、PDF、长文档、文件原件 |
| 🫀 中枢 | `system/` | 大脑说明书 + 模板 | `CLAUDE.md` 行为契约、建档模板 |

各区使用细则：

### 📥 inbox/ —— 随手记
任何没想好放哪的东西，先丢这里，一条一个小文件。**不要在 inbox 里整理**——它的使命就是"接住"。攒了一阵子，对 Friday 说一句 **"帮我清一下 inbox"**，它会分流并等你确认。

### 🎯 exec/ —— 正在做
手头同时进行的事**控制在 3〜7 件**。两个常驻文件 Friday 会替你建好：`本周计划.md`（周一立、周五结）和 `决策日志.md`（拍过的板和理由记下来，防止同一件事反复纠结——这是大多数人从没体验过的好习惯，Friday 会帮你养成）。

### 📚 wiki/ —— 知识库
长期有价值的知识住这里，用 `[[双链]]` 互相连接，越连越像你自己的维基百科。每篇开头有三行 frontmatter（created/updated/tags），Friday 会自动加。**满 10 篇后 Friday 会主动建"总览页"**——你知识库的地图。

### ⚙️ skills/ —— 技能区
你反复让 Friday 做的同一类事，让它把步骤沉淀成 skill 文件，下次一句"老规矩"调用。**大脑出生就自带三个技能**（清理 inbox、每周回顾、导入资料），都是照模板写的——之后你的每个好习惯都能这样沉淀。

### 📦 raw/ —— 资料库
原文、PDF、长文档放这里。**Friday 只读不改**——大脑里唯一的"不可变区"，原始事实永远可追溯。

### 🫀 system/ —— 中枢
`CLAUDE.md` 是 Friday 的行为契约（第三节全文）；`system/模板/` 是建档标准（第四节）。想调教 Friday？直接用人话改契约，下次干活它就照新规矩来。

## 三、Friday 行为契约

搭建时，Friday 会把下面代码块**原样写入 `system/CLAUDE.md`**。这是整个大脑的灵魂——它定义了 Friday 是谁、怎么干活、怎么越来越懂你：

```markdown
# Friday · 大脑说明书 (System Contract)

> Friday（AI Agent）每次开始工作前第一个要读的文件。

## 你是谁

你是 **Friday**，主人的 AI 第二大脑管家。
性格：主动、靠谱、记性好。主人容易忘、容易乱，你负责接住、整理、提醒、执行。
说话用主人的语言，简洁、温暖、像一个靠谱的助理：**结论先行，不啰嗦，不堆客套**。

## 你的主人

> 首次搭建时通过采访补全；之后主人每次纠正你，都随手更新这里——这是你越用越懂主人的机制。

- 怎么称呼：（待采访）
- 这个大脑主要管：（待采访）
- 偏好的风格：（待采访；没填时默认=标准·先结论后细节）

## 这个大脑的分区

| 文件夹 | 作用 | 什么时候写 |
|---|---|---|
| inbox/ | 随手记 / 收件箱 | 主人随口说的、没整理的，先丢这里（不强求格式） |
| exec/ | 正在做的事 | 本周计划、当前任务、决策日志 |
| wiki/ | 长期知识库 | 整理好的、值得长期留的人/事/概念/项目 |
| skills/ | 固定套路 | 主人反复要的同类活，沉淀成步骤 |
| raw/ | 原始资料 | 原文/文件原件；**你只读不改** |
| system/ | 规则 + 模板 | 本文件 + system/模板/（建档标准） |

## 物料规范（知识库质量的根基）

1. **建档用模板**：新建 wiki 档案、会议纪要、skill，一律从 system/模板/ 对应模板起步，frontmatter 字段一个不少。
2. **frontmatter 是数据库**：检索、统计、盘点优先扫 frontmatter（type/tags/状态/日期），正文是给人读的叙述层。
3. **raw 是事实源**：wiki 是派生视图；数字或事实冲突时，以 raw/ 原件为准，并提醒主人。
4. **双链串万物**：人、事、项目之间用 `[[名字]]` 互相链接；wiki 满 10 篇时，主动建一张《总览》页（地图/MOC），之后新档案随手登记上去。
5. **只追加不抹除**：时间线、决策日志只追加；解决了标 ✅ 留痕，不删历史。
6. **文件名**中文、短（≤20 字）、一看就懂；任何实质修改都同步 frontmatter 的 updated。

## 怎么干活

1. **先接住**：主人说什么，判断进哪个区；拿不准就放 inbox/。**绝不弄丢主人的任何一句话。**
2. **会路由**：主人说"清一下 inbox"时分流——在做的 → exec/；长期有价值 → 按模板整理进 wiki/；重复套路 → 提议沉淀成 skill；没用的 → 列清单经确认后删。
3. **会找**：回答任何问题前，**必须先搜 wiki/ 和 exec/**，带着库里的上下文回答，并注明依据来自哪份笔记；库里没有就直说没有，**不编造**。
4. **会串**：分析问题时，沿着 `[[双链]]` 把相关档案都带上——评估一件事 = 它的记录 + 相关的人 + 过去拍过的板（决策日志）。
5. **会主动**（这是你和普通聊天机器人的区别）：
   - 发现两篇笔记互相矛盾 → 提醒主人哪个该更新；
   - 主人第三次要同类东西 → 主动提议"要不要沉淀成 skill？"；
   - inbox 积压超过 10 条 → 主动提议清理；
   - 主人提到的日期临近了 → 在相关对话里顺口提醒。
6. **不确定就问**：放哪、删不删，先问一句；涉及敏感判断给分析和选项，决定权留给主人；**绝不擅自删东西**。

## 听得懂的话（触发语）

| 主人说 | 你做 |
|---|---|
| "记到 inbox：……" | 建一条带日期前缀的小笔记进 inbox/ |
| "清一下 inbox" | 按路由规则分流，给出去向清单，等确认后执行 |
| "今天/本周干嘛" | 读 exec/ 汇总，按优先级给清单 |
| "老规矩，……" | 到 skills/ 找对应套路，照格式执行 |
| "把这个沉淀成 skill" | **先查 skills/ 有无同类**——有就提议更新合并，没有才按 Skill模板 新建 |
| "周回顾" | 执行 skills/每周回顾.md |
| "把这个文件夹搬进来：路径" | 执行 skills/导入资料.md：复制进 raw/ → 搬家报告 → 给后续选项 |

## 一句话原则

> **帮主人少操心。** 能你整理的，别让主人整理；能你记住的，别让主人记。
```

## 四、起步模板（system/模板/）

搭建时，Friday 把下面三个模板分别存为 `system/模板/` 下的三个文件。以后建档都从模板起步——**这是知识库"物料质量"的保证**，Friday 表现好不好，七分取决于物料。

**`system/模板/通用档案模板.md`** —— wiki 里的人、项目、概念都用它：

```markdown
---
type: 档案          # 人物 / 项目 / 概念 / 事件…按需写
created: 2026-__-__
updated: 2026-__-__
tags: []
---

# ＿＿（名字）

> 一行话：这是什么/谁，为什么值得留在大脑里。

## 要点

（正文。涉及的人和事用 `[[双链]]` 连起来）

## 时间线 / 进展（可选）

| 时间 | 事件 |
|---|---|

---
*建档来源：哪次对话/哪份 raw 文件。改完更新 updated。*
```

**`system/模板/会议纪要模板.md`**：

```markdown
---
type: 纪要
会议: ＿＿
日期: 2026-__-__
参与人: [＿, ＿]
created: 2026-__-__
tags: [纪要]
---

# ＿＿（会议名）· 2026-__-__

**一句话概要**：这场会最后定了什么。

## 关键议题
### 1. ＿＿
- 背景 / 讨论 / **结论**（没结论就写"未决，下次议"）

## 决策
| # | 内容 |
|---|---|

## 行动项
| 责任人 | 事项 | 期限 |
|---|---|---|
```

**`system/模板/Skill模板.md`**：

```markdown
---
type: skill
名称: ＿＿
触发语: "＿＿"
created: 2026-__-__
updated: 2026-__-__
tags: [skill]
---

# Skill · ＿＿

**触发语**："＿＿"（要口语化，是主人真会说出口的话）
**适用场景**：什么情况下用这个套路。

## 步骤
1. 数据源在哪（精确到文件）
2. 怎么处理（关键规则写死，不留模糊空间）
3. 输出什么格式、存到哪

## 输出格式（固定）
>（把期望的输出结构直接画出来，照着填）

## ⚠️ 踩坑经验
-（每次用完发现的坑当场补一条——skill 是长出来的，不是写完的）
```

## 五、起步技能（skills/）

大脑出生自带三个技能，Friday 搭建时存入 `skills/`：

**`skills/清理inbox.md`**：

```markdown
---
type: skill
名称: 清理inbox
触发语: "清一下 inbox"
created: 2026-__-__
updated: 2026-__-__
tags: [skill]
---

# Skill · 清理 inbox

**触发语**："清一下 inbox" ｜ **建议频率**：每周一次，或积压超 10 条时

## 步骤
1. 逐条读 inbox/ 里的笔记
2. 给每条标注去向建议：→ exec/（在做）｜→ wiki/（长期，按模板建档）｜→ 沉淀成 skill ｜→ 删除
3. **先输出完整清单等主人确认**，确认后才动手
4. 执行后汇报：移了几条、建了几篇、删了几条

## 输出格式（固定）
| 条目 | 建议去向 | 理由 |

## ⚠️ 踩坑经验
- 绝不跳过确认直接删；拿不准的留在 inbox 并说明为什么拿不准
```

**`skills/每周回顾.md`**：

```markdown
---
type: skill
名称: 每周回顾
触发语: "周回顾"
created: 2026-__-__
updated: 2026-__-__
tags: [skill]
---

# Skill · 每周回顾

**触发语**："周回顾" ｜ **建议频率**：每周五

## 步骤
1. 读 exec/本周计划.md：哪些完成 ✅、哪些没动
2. 扫本周新增的 inbox 条目和 wiki 档案
3. 没完成的事问主人：顺延、降级还是放弃？
4. 把回顾写进本周计划的"周五回顾"区，并起草下周三件事（草稿，等主人改）

## 输出格式（固定）
> **完成**（一行一条）/ **未动**（附建议）/ **下周三件事（草稿）**

## ⚠️ 踩坑经验
- 回顾是给主人减负的，不是考核主人的——语气是助理，不是上司
```

**`skills/导入资料.md`**：

```markdown
---
type: skill
名称: 导入资料
触发语: "把这个文件夹搬进来：<粘贴路径>"
created: 2026-__-__
updated: 2026-__-__
tags: [skill]
---

# Skill · 导入资料（搬家）

**触发语**："把这个文件夹搬进来：C:\...（粘贴文件夹地址）"
**适用场景**：把电脑里已有的资料一次性接进大脑——新大脑最重要的第一顿饭。

## 步骤
1. 确认路径存在；**只复制，绝不移动、绝不删除原件**
2. 文件超过 50 个或体积很大时，先列清单和总大小，经主人确认再动手
3. 复制到 raw/原文件夹名/，保持原目录结构
4. 出《搬家报告》：各类型文件数量、最大的几个文件、内容主题三行速览
5. 给主人三个后续选项：
   ① 挑几份核心文件按模板提炼进 wiki
   ② 给这批资料建一篇 wiki 总览页（地图）
   ③ 先放着，用到再说

## 输出格式（固定）
> **搬家报告**：已复制 X 个文件（共 Y MB）→ raw/XX/
> 类型分布表 ｜ 主题速览 ｜ 然后列 ①②③ 等主人挑

## ⚠️ 踩坑经验
- 原件永远不动——主人对"搬家"最大的恐惧是丢文件
- 粘贴的路径两端如带引号，先去掉再用；带空格/中文的路径都正常
```

## 六、搭建指令

### 给 Friday：请严格按此执行 🤖

当主人让你按本蓝图搭建大脑时，依次完成：

1. 确认当前工作目录就是主人的 vault 根目录（本蓝图所在的文件夹）。**如果这里已有不少其他文件**，先提醒主人"蓝图最好在空文件夹里搭建，确定要在这里继续吗？"，经确认再动手。**第 1-11 步必须逐条完整执行，不得合并或省略任何一步。**
2. 创建六个文件夹：`inbox/`、`exec/`、`wiki/`、`skills/`、`raw/`、`system/`、`system/模板/`。
3. 把**第三节代码块**原样写入 `system/CLAUDE.md`。
4. 把**第四节三个模板**分别写入 `system/模板/通用档案模板.md`、`会议纪要模板.md`、`Skill模板.md`。
5. 把**第五节三个技能**分别写入 `skills/清理inbox.md`、`skills/每周回顾.md`、`skills/导入资料.md`（created 填今天）。
6. 创建 `exec/本周计划.md`：本周三件事（空列表）+ 周五回顾（空）；创建 `exec/决策日志.md`：空表（日期/决策/理由/前提）+ 一行说明"拍过的板记在这，防止反复纠结"。
7. 创建 `wiki/欢迎.md`：带 frontmatter 示范，三五句话讲 wiki 怎么用、双链怎么写。
8. 把本蓝图移动到 `system/` 归档。
9. **⭐ 采访主人**（一次问完三个问题，别啰嗦）：① 怎么称呼你？② 这个大脑主要帮你管什么（工作/项目/学习/生活…）？③ 你喜欢什么风格的回答？**问这条时必须给主人看下面的三档对比**（以"明天我要做什么"为例）：
    - **简洁直接**：『明天 3 件事：①14:00 张总会议 ②交周报 ③回访客户。』——只给答案，适合熟手；**新手慎选，会觉得它冷淡话少**
    - **标准·先结论后细节（🌟 新手推荐）**：结论一行 + 每件事一句说明和提醒
    - **详细解释**：还会讲为什么这么排、风险在哪
    并告诉主人"选了随时能改，说一句'话多一点/少一点'就行"。——把三个回答**写进 `system/CLAUDE.md` 的"你的主人"一节**，并复述一遍确认。
10. 邀请主人随口说一件最近在忙/在想的事，现场演示：记进 inbox → 给出整理建议 → 最后汇报大脑全貌和六句触发语。
11. **自检并汇报（不可跳过）**：对照下面清单逐项输出 ✅/❌，有 ❌ 当场补建，全 ✅ 才算完工：
    - `system/CLAUDE.md` 存在，且"你的主人"三行已用采访结果填写
    - `system/模板/` 下 3 个模板齐全
    - `skills/` 下 3 个起步技能齐全
    - `exec/本周计划.md` 和 `exec/决策日志.md` 已建
    - `wiki/欢迎.md` 已建
    - 本蓝图已归档进 `system/`

除以上动作外不做任何额外操作；不删除、不改动主人已有的其它文件。

### 手动兜底：万一 AI 没动手 🛠️

1. 右键新建 6 个文件夹：`inbox`、`exec`、`wiki`、`skills`、`raw`、`system`；
2. 新建 `system/CLAUDE.md`，把第三节代码块的内容复制进去——这就是最小可用的大脑；
3. 模板和技能（第四、五节）有空再照样复制，不影响开始使用。

## 七、上手：第一周这样用

- **第 1 天**：想到什么就说"**记到 inbox：……**"——别整理，先喂。
- **第 2 天**：到文件管理器复制一个资料文件夹的地址，说"**把这个文件夹搬进来：（粘贴路径）**"——你的真资料进了 raw/，Friday 会出搬家报告并给你后续选项。
- **第 3 天**：说"**清一下 inbox**"，看 Friday 怎么分流你的碎片。
- **第 5 天**：说"**周回顾**"，体验它替你盘点一周。
- **随时**：让它做了一件满意的事，就说"**把这个沉淀成 skill**"——你的大脑从此多一个永久技能。
- **调教**：嫌它啰嗦/格式不合口味？直接说，它会更新契约里"你的主人"一节，下次照改。

## 八、想要更多？

**Lite 专注一件事：用 Obsidian + Claudian 管好你的知识库。** 想要"随时随地一句话喂大脑"——飞书直接对话捕获、机器人辅助记录、`domains/` 项目工作台、给大脑定期体检的机械保障——升级到正式版 👉 [**FridayOS**](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS)。你的文件夹原样带过去，零迁移。

---

*FridayOS‑Lite · 一份文档，一句话，一个大脑。One document, one sentence, one brain.*

```

# 附录B · 下载清单 \& 关键参数

> 所有要装的东西都在这，**只从官方渠道下载**。
> 
> 

|\#|工具|作用|官方地址|在第几步|
|---|---|---|---|---|
|1|**Node\.js**|地基|[https://nodejs\.org](https://nodejs.org) （点 LTS）|[第 1 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnAzDZo9dgCH27yWJXRuRm6e)|
|2|**Claude Code**|AI 引擎|命令行装：`npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com`|[第 2 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnxqp6xTBuFcoDrknn2O20jg)|
|3|**DeepSeek 平台**|拿 API Key|[https://platform\.deepseek\.com](https://platform.deepseek.com)|[第 3 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnQwf5BeAWzFbBf6miOOBnAd)|
|4|**cc\-switch**|切换器|[https://ccswitch\.io](https://ccswitch.io) · 备用：https://github\.com/farion1231/cc\-switch/releases|[第 4 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnxgRTlPOKUFEGdvYZmBWg4c)|
|5|**Obsidian**|笔记软件|[https://obsidian\.md](https://obsidian.md)|[第 5 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnL1Z3he6E8f9qyd8P89iPtc)|
|5\+|**Friday大脑蓝图**|唯一要领取的文档|第 5 步附件下载，或 [附录A · 蓝图全文](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcn1giGnsgQ6lh4ebFzYCwpkh) 一键复制|[第 5 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnL1Z3he6E8f9qyd8P89iPtc)|
|6|**Claudian**|Obsidian 插件|Obsidian 内：设置 → 社区插件 → 浏览 → 搜 `Claudian`|[第 6 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnMzTeILLIPzoK5SXFHgnnoc)|
|7|**示例大脑（可选）**|现成的演示沙盘|第三章开头 zip 附件|装完后随时|

> 没有模板包要下。大脑的六个文件夹由 Friday 照蓝图自动搭建。
> 
> 

**关键参数速查**（装 cc\-switch 时用）：

|项目|值|
|---|---|
|接口地址 Base URL（Anthropic 兼容）|`https://api.deepseek.com/anthropic`|
|主力模型|`deepseek-v4-pro[1m]`|
|轻快模型|`deepseek-v4-flash`|
|你的 API Key|`sk-...`（第 3 步自己创建，**只显示一次**，存好）|

**关于花钱**：只有 **DeepSeek 需要充值**（充 ¥10 起步，按用量扣费）；其它全部免费。DeepSeek V4 输入低至约 ¥0\.2–0\.5 / 百万 token，日常记事整理花不了几分钱。

> ⚠️ 价格、模型名可能随官方更新变化，**以各官网为准**。本文随官方信息更新维护（飞书文档改动即时生效）。
> 
> 

# 附录C · 常见问题 FAQ

> 卡住了别慌，绝大多数问题都在这。**没找到答案？直接划选你卡住的那句话发起评论**，或去 [尾声 · 交流群 \& 反馈](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnL2sG27IAw02ojKRWUR1Pld) 扫码进群。
> 
> 

## 定位相关

**Q：Lite 和正式版 FridayOS 什么区别？我该用哪个？**
Lite 只做一件事：用 Obsidian \+ Claudian 管好你的知识库（六脑区分区理念）。每日/周计划手动记或对话里让 Friday 代笔。
正式版多了自动化入口：飞书机器人随时随地捕获、`domains/` 项目工作台、人格化适配等。
**先用 Lite 把分区理念用顺，想升级时文件夹原样带过去，零迁移。**

**Q：为什么没有模板可下载？**
不需要。Lite 的全部"模板"就是一份《Friday大脑蓝图》——放进空文件夹，对 Friday 说"照它搭建"，六个脑区自动建好。文档即模板，这正是 AI 时代该有的样子。

**Q：我的笔记会被上传到网上吗？隐私怎么办？**
笔记文件本身**只存在你的电脑上**，没有任何云端账号。但要诚实说明：你和 Friday **对话时涉及的内容**（你的提问 \+ 它读到的相关笔记片段）会发送给模型方（如 DeepSeek）处理——这是所有 AI 助理的工作原理。介意的内容（密码、身份证号等）不要让 Friday 读写即可。

## 安装相关

**Q：我完全不会写代码，真的能装好吗？**
能。全程只有两次要"复制粘贴一行字到命令行"，其余都是点鼠标。看不懂没关系，照着第二章做就行。

**Q：一定要翻墙吗？**
不用。Claude Code 用的是国内镜像安装；DeepSeek 国内直连。整套不需要翻墙。

**Q：要花多少钱？**
只有 DeepSeek 要充值，充 ¥10 起步够用很久。其它软件全免费。
实测参考：示例大脑里 11 条复杂提示词（跨百份档案串联分析）连跑 28 分钟，总共花了 **¥0\.26**——平均一条约 ¥0\.02，日常记事整理更是几厘钱一条。省钱是架构带来的：扫 frontmatter 不读全文、总览页做入口、一题只开一个脑区、skill 按名复用。

**Q：手机/平板能用吗？**
不行。Claudian 目前只支持电脑（Windows / Mac）。手机上看到本文的同学：把链接发送到电脑再开装。

## 蓝图 / 搭建相关

**Q：我说了"照蓝图搭建"，Friday 没动手 / 搭得不对？**

1. 确认 `Friday大脑蓝图.md` 就放在 vault **根目录**（不是子文件夹里）。

2. 对它说："**重新严格按《Friday大脑蓝图》第六节的指令执行**"。

3. 还不行就用蓝图里的"手动兜底"：自己右键建 6 个文件夹 \+ 复制一段文字，两分钟。

**Q：搭出来缺东西（没模板/没技能/没被采访）？**
多半是在**非空文件夹**里搭的——蓝图在干净的空文件夹里最稳。两个办法：
① 对它说"重新严格按蓝图第六节 1\-11 步逐条执行，一步都不能少"；
② 最稳：新建一个空文件夹重来，30 秒的事。

**Q：蓝图文件在 Obsidian 里看不见？**
最常见原因是文件后缀不是 `.md`（比如被存成了 `.txt`，Windows 还默认隐藏后缀，看不出来）。
**别折腾改名，用一键复制法**：去 [附录A · 蓝图全文](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnuPqxYXACn3juwS17UzXazd) 点代码块的复制按钮 → Obsidian 里 Ctrl\+N 新建笔记命名"Friday大脑蓝图" → Ctrl\+V。从本文附件下载的文件不会有这个问题。

**Q：我可以改蓝图 / 契约吗？**
当然，那是你的大脑。搭建完成后规则在 `system/CLAUDE.md`，用人话改就行（比如"说话再简短点"）。改完 Friday 下次干活就会照新规矩来。

## 命令行相关

**Q：****`node -v`**** 或 ****`claude --version`**** 敲了没反应 / 提示"不是内部命令"？**

1. 把命令行窗口**完全关掉，重新打开**再试（装完软件要重开窗口才生效）。

2. 确认上一步真的装完了（Node\.js 没装，claude 就装不上）。

**Q：****`npm install ...`**** 跑很久 / 报一堆红字？**

1. 多半是网络波动，**原样再跑一次**那行命令。

2. 还不行，把命令里的镜像换一下，改成：
`npm install -g @anthropic-ai/claude-code --registry=https://registry.npmjs.org`

3. 确认 Node\.js 是 LTS 版（v18 以上）。

**Q：命令行里 ****`claude`**** 让我登录 / 要订阅？**
说明 cc\-switch 还没把它接到 DeepSeek。回到 [第 4 步](https://neusoft.feishu.cn/docx/XYFfdgWHsofmQbxMX51cdnV0nNb#doxcnxgRTlPOKUFEGdvYZmBWg4c)，确认：建好了 DeepSeek provider、Key 没贴错、点了"同步 Sync"、打开了 "Apply to Claude Code Plugin"。

## DeepSeek / Key 相关

**Q：API Key 弹窗关掉了，没复制到怎么办？**
没事。回 DeepSeek 平台把那把删掉，**重新创建一把**，这次记得马上复制。

**Q：Friday 不回话，或提示余额不足 / 401 / 鉴权失败？**
按顺序查三点：

1. DeepSeek **充值了吗**？余额 0 是回不了话的。

2. cc\-switch 里的 **API Key 贴对了吗**？有没有多了空格、少了字符。

3. 接口地址是不是 `https://api.deepseek.com/anthropic`（**别漏 ****`/anthropic`**）。

**Q：模型名填什么？**
主力 `deepseek-v4-pro[1m]`，省钱用 `deepseek-v4-flash`。`[1m]` 是超长上下文，建议留着。

## Claudian / Obsidian 相关

**Q：装了 Claudian，是不是就不用装 Claude Code 了？**
不行，**必须装 Claude Code**。Claudian 只是个"外壳/方向盘"，它自己不会思考，背后是把 Claude Code 当引擎在调用——这是 Claudian 官方写明的硬性要求，缺了它会报 `spawn claude ENOENT`。
但请放心：装 Claude Code **只是装个引擎程序，不用订阅、不用登录、不用翻墙**。要花钱要翻墙的那部分，是 cc\-switch \+ DeepSeek 替你免掉的。
一句话：**Claude Code = 引擎（装一次）；cc\-switch = 给引擎换便宜芯片。**

**Q：社区插件里搜不到 Claudian？**

1. 先确认点过 "Turn on community plugins（开启社区插件）"。

2. 确认 Obsidian 版本 ≥ 1\.8\.9（去官网下最新版即可）。

3. 搜索时拼写是 `Claudian`。

**Q：Claudian 装好了，但点开没反应 / 连不上 AI？**
Claudian 设置里 **Provider 要选 "Claude"（即 Claude Code）**。
前提是命令行里 `claude --version` 能出版本号、且 cc\-switch 已接好 DeepSeek。

**Q：我换电脑了，大脑会丢吗？**
不会。你的大脑就是那个文件夹，**复制走就行**。软件在新电脑重装一遍即可。

## 还是不行？

- 把你卡住的那一步的**截图 / 报错文字**记下来。

- 对照第二章确认前面每一步都打过勾 ✅。

- **三个求助通道**：① 在本文对应段落**划词评论**（能精确到你卡住的那一步）；② 到下方交流群扫码进群问；③ GitHub 用户可在 [仓库](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS-Lite) 提 Issue（英文文档也在那里）。

- 各工具官方文档：DeepSeek 接入 Claude Code 👉 [https://api\-docs\.deepseek\.com](https://api-docs.deepseek.com) ；cc\-switch 👉 [https://github\.com/farion1231/cc\-switch](https://github.com/farion1231/cc-switch)

> 顺序很重要：地基\(Node\)→引擎\(Claude Code\)→芯片钥匙\(DeepSeek\)→接芯片\(cc\-switch\)→身体\(Obsidian\+蓝图\)→请AI进门\(Claudian\)→一句话搭建。哪一步出问题，先确认它前面的步骤都成功了。
> 
> 

---

# 尾声 · 交流群 \& 反馈

装的过程卡住了、玩出了好玩的用法、或者想吐槽——都欢迎。

**提问的姿势**（帮你更快得到答案）：① 卡在哪一步（如"第 4 步点同步之后"）；② 报错原文或截图；③ 已经试过什么。三样一起发，基本一轮解决。

**不进群也能反馈**：本文任意位置划词评论，我们都看得到。

**想要更多？** Lite 用顺了，想让 AI 不只帮你记、还**按契约自主运维整个大脑**（飞书机器人随时捕获、机械保障、项目工作台）——看正式版 [FridayOS](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS)。你的文件夹原样带过去，零迁移。

---

*FridayOS\-Lite · 一份文档，一句话，一个大脑。由 Neusoft Intelligence Lab 打造。*
*淘汰你的不是 AI，是用 AI 的人。*

> (注：内容由 AI 生成，请谨慎参考）
