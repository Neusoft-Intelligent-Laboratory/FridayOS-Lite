# 🆘 FAQ

> Don't panic — most issues are here. 中文：[`常见问题.md`](./常见问题.md)

## Install

**I can't code at all — can I really do this?** Yes. Only two steps need you to paste one line into a terminal; everything else is mouse clicks. Just follow [`INSTALL.en.md`](./INSTALL.en.md).

**Do I need a VPN?** No. Claude Code installs from a China mirror; DeepSeek connects directly.

**How much does it cost?** Only DeepSeek needs a top‑up; a few dollars lasts a long time. Everything else is free.

**Phone / tablet?** No — Claudian is desktop‑only (Windows / Mac).

## Terminal

**`node -v` or `claude --version` does nothing / "not recognized"?** Fully close the terminal and reopen it (newly installed tools need a fresh window). Make sure the previous step actually finished.

**`npm install ...` is slow / throws red errors?** Usually a network blip — rerun the exact line. Still failing? Swap the mirror to `--registry=https://registry.npmjs.org`. Confirm Node.js is LTS (v18+).

**`claude` asks me to log in / subscribe?** cc-switch hasn't redirected it to DeepSeek yet. Redo **Step 4**: create the DeepSeek provider, paste the key correctly, click **Sync**, and enable **Apply to Claude Code Plugin**.

## DeepSeek / Key

**I closed the key popup without copying it.** Delete that key on the DeepSeek platform and create a new one — copy it immediately this time.

**Friday won't reply / balance / 401 / auth error?** Check three things in order: (1) Did you top up DeepSeek? (2) Is the API key in cc-switch exactly right (no stray spaces)? (3) Is the Base URL `https://api.deepseek.com/anthropic` (don't drop `/anthropic`)?

**Which model names?** Main `deepseek-v4-pro[1m]`, cheaper `deepseek-v4-flash`. `[1m]` is the long‑context variant — keep it.

## Claudian / Obsidian

**If I install Claudian, can I skip Claude Code?** No — Claude Code is required. Claudian is just a shell that drives the Claude Code CLI under the hood (its official requirement); without it you get `spawn claude ENOENT`. But installing it needs no subscription, no login, no VPN — that's what cc-switch + DeepSeek replace. Claude Code = engine (install once); cc-switch = swaps in the cheap DeepSeek chip.

**Can't find Claudian in community plugins?** Make sure you clicked "Turn on community plugins," Obsidian is ≥ 1.8.9, and you spelled `Claudian`.

**Claudian installed but won't connect to the AI?** In Claudian settings set **Provider = Claude** (Claude Code). This requires `claude --version` to work and cc-switch to already point at DeepSeek.

**New computer — will I lose my brain?** No. Your brain is the folde