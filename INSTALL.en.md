# 🛠️ FridayOS‑Lite Install Guide (Beginner Edition)

> Just follow along. **About 20 minutes, no coding, no VPN.**
> Before you start, spend 3 minutes on 👉 [`TOOLS.en.md`](./TOOLS.en.md) so each tool makes sense.
>
> 🌐 中文：[`安装指南.md`](./安装指南.md) · Stuck? 👉 [`FAQ.en.md`](./FAQ.en.md)

---

## 📋 Before you start

| Item | Notes |
|---|---|
| 💻 A computer | Windows or Mac (Claudian is desktop‑only) |
| 🌐 Internet | **No VPN needed** if you use the domestic mirror below |
| ⏱️ ~20 min | First time, take it slow |
| 💰 ~$2 | Top up DeepSeek a little; usage is extremely cheap |

## ⚠️ Install order ≠ explanation order

[`TOOLS.en.md`](./TOOLS.en.md) explains the layers outside‑in (Obsidian → Claudian → Claude Code → cc-switch → DeepSeek) so they're easy to understand. But when you actually install, the order shifts slightly:

- **cc-switch needs a DeepSeek key first**, so we grab the key earlier.
- **Claudian comes last** — the engine (Claude Code) and chip (DeepSeek) must be wired up before there's anything for it to use.

Real hands‑on order:

```
Step 0 Node.js → Step 1 Obsidian + template → Step 2 DeepSeek key
   → Step 3 Claude Code → Step 4 cc-switch → Step 5 Claudian → ✅ done
```

## Step 0 — Install Node.js (the foundation)
Claude Code and cc-switch both run on Node.js. Go to **https://nodejs.org**, click the big **LTS** button, install with all defaults. Verify by opening a terminal (Windows: `Win+R` → `cmd`; Mac: Terminal) and running `node -v`. A version number means success.

## Step 1 — Install Obsidian + open the brain template
Get Obsidian at **https://obsidian.md** and install it. Unzip the `vault-template` folder Lite gave you, rename it (e.g. `MyBrain`), and in Obsidian choose **"Open folder as vault"** → select it. If asked, click **Trust author and enable plugins**. You'll see the `inbox / exec / wiki / skills / raw / system` folders. Read `先看我-START-HERE` first. The body exists now — but it has no AI yet.

## Step 2 — Register DeepSeek, top up, get an API key
Go to **https://platform.deepseek.com**, sign up, and **top up ~$2** under Balance. Click **API keys → Create new API key**, name it (e.g. `friday`). ⚠️ The `sk-xxxx...` string **shows only once** — copy it into a notepad immediately. Lost it? Just delete and make a new one. 🔒 Treat it like a password; never post it online. Remember two values for Step 4:
- Base URL (Anthropic‑compatible): `https://api.deepseek.com/anthropic`
- Models: `deepseek-v4-pro[1m]` (main) and `deepseek-v4-flash` (light/cheap)

## Step 3 — Install Claude Code (domestic mirror, no VPN)
Open a terminal and paste this one line (uses a China mirror, no VPN needed):
```
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```
Wait for it to finish, then verify with `claude --version`. Don't log in yet — it defaults to the paid official models; the next step redirects it to DeepSeek.

## Step 4 — Install cc-switch + connect DeepSeek ⭐ key step
Download cc-switch from **https://ccswitch.io** (or **https://github.com/farion1231/cc-switch/releases**) — `.msi/.exe` for Windows, `.dmg` for Mac. Open it; the default top tab is **Claude**. Click **"+"** to add a provider:
- Pick **DeepSeek** from the preset list.
- **API Key:** paste your `sk-...`.
- **Base URL:** `https://api.deepseek.com/anthropic`.
- **Models:** `deepseek-v4-pro[1m]` and `deepseek-v4-flash`.

In **Settings**, enable **Apply to Claude Code Plugin** and **Skip Claude Code Initial Setup**. Back on the main screen, select DeepSeek and click **Sync to All Apps**. Your engine now runs on DeepSeek. (Test: in a terminal, `cd` to your brain folder, run `claude`, choose **I trust**, ask anything.)

## Step 5 — Install Claudian, bring Friday into Obsidian
In Obsidian → **Settings (gear)** → **Community plugins** → turn them on → **Browse** → search **`Claudian`** → **Install** → **Enable**. In Claudian's settings, set **Provider = Claude** (Claude Code). It will use the local Claude Code engine that cc-switch already pointed at DeepSeek. A Claudian icon appears in the sidebar — that's your chat with Friday. (Requires Obsidian ≥ 1.8.9, desktop only.)

> ℹ️ **Why you can't skip Step 3 (Claude Code):** Claudian is only a shell — it can't think on its own and drives the Claude Code CLI under the hood (its official requirement). No Claude Code = `spawn claude ENOENT` and nothing works. But installing it needs **no subscription, no login, no VPN** — that paid/blocked part is exactly what cc-switch + DeepSeek replace.

## ✅ Done — test it
In the Claudian chat, say:
> **Hi Friday, save this to my inbox: meeting with Mr. Zhang tomorrow at 3pm.**

If a new note appears in `inbox/`, 🎉 your AI second brain is live.

## 🆘 Stuck?

| Symptom | Fix |
|---|---|
| `node -v` / `claude --version` does nothing | Reopen the terminal and retry |
| `npm install` errors / very slow | Network/mirror hiccup — retry; see [`FAQ.en.md`](./FAQ.en.md) |
| Friday won't reply / balance error | DeepSeek not topped up, or wrong key in cc-switch |
| Can't find Claudian | Make sure community plugins are on and Obsidian ≥ 1.8.9 |

More 👉 [`FAQ.en.md`](./FAQ.en.md) · [`下载清单.md`](./下载清单.md)
