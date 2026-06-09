# 🚀 把 FridayOS-Lite 上传到 GitHub（给 Owen）

> 现在 `FridayOS-Lite` 是一个**独立文件夹 / 独立仓库**，单独上传，和完整版 FridayOS 互不影响。
> `FridayOS-Lite` is now a standalone repo — upload it on its own.

## 方式一：命令行新建独立仓库（推荐）

先在 GitHub 网页上 **New repository** 建一个空仓库，命名 `FridayOS-Lite`（不要勾选 README/.gitignore，建空的）。然后在本地这个文件夹里：

```bash
cd FridayOS-Lite

# 打包模板，方便小白下载（已自带 vault-template.zip，重打包才需要）
# zip -r vault-template.zip vault-template

git init
git add .
git commit -m "FridayOS-Lite: beginner edition (Obsidian + Claudian + cc-switch + DeepSeek)"
git branch -M main

# 把下面地址换成你刚建的仓库地址
git remote add origin https://github.com/Neusoft-Intelligent-Laboratory/FridayOS-Lite.git
git push -u origin main
```

推完后访问 `https://github.com/Neusoft-Intelligent-Laboratory/FridayOS-Lite` 就能看到。

## 方式二：网页拖拽（不想用命令行）

1. GitHub 上 **New repository** 建 `FridayOS-Lite`，建好后进入空仓库页。
2. 点 **uploading an existing file** → 把 `FridayOS-Lite` 文件夹里的所有文件**拖进去**。
   - ⚠️ 网页上传**不保留空文件夹**；本项目每个文件夹都有文件（README 等），没问题。
   - 子文件夹（如 `vault-template/`、`docs/images/`）可以直接整个拖进去。
3. 填提交信息 → **Commit changes**。

## 建议做的两件事

1. **在完整版 FridayOS 的 README 里挂个入口**，把新手引过来，例如在 `FridayOS/README.md` 顶部加一行：
   > 🔰 第一次接触、想要最简单的安装？看 👉 [**FridayOS‑Lite（小白版）**](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS-Lite)
2. **补真实截图**（强烈建议）：`安装指南.md` 里标了多处 `📸（截图位置：…）`，把对应步骤截图放进 `docs/images/`，再用 `![](./docs/images/xxx.png)` 引用，小白体验会好很多。
   （`docs/images/` 里已经有 `architecture.png` 总览图和 `hero.png` 封面图可直接用。）

## 给小白发布时

最省心的分发方式——让小白只做两件事：
1. 下载 `vault-template.zip`（他们的"大脑文件夹"）。
2. 打开 `安装指南.md` 照着做。

> 想加 LICENSE？建仓库时选 MIT 即可，和完整版保持一致。
