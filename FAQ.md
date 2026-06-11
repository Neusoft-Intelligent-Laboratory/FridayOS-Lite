# 🆘 FAQ

> Don't panic — most answers are in here. 中文：[`常见问题.md`](./常见问题.md)

---

## Positioning

**Lite vs. full FridayOS — which one?**
Lite does one thing: a knowledge base managed with Obsidian + Claudian (the six-region idea). Daily/weekly plans you write by hand or dictate in chat.
The full version adds automated entry points: Feishu bot capture from anywhere, a `domains/` project workbench, personality adaptation.
**Start with Lite; when you upgrade, your folder moves over as-is. Zero migration.**

**Why is there no template to download?**
You don't need one. Lite's entire "template" is one file — [`FRIDAY-BLUEPRINT.md`](./FRIDAY-BLUEPRINT.md). Drop it into an empty folder, tell Friday "build from this", and the six regions appear. The document *is* the template.

**Do my notes get uploaded anywhere? What about privacy?**
The note files themselves live **only on your computer** — no cloud account. To be honest though: whatever your conversation touches (your question + the note snippets Friday reads) is sent to the model provider (e.g. DeepSeek) for processing — that's how every AI assistant works. Keep truly sensitive things (passwords, ID numbers) out of Friday's reach.

---

## Install

**I can't code at all — can I really do this?** Yes. Only two steps need you to paste one line into a terminal; everything else is mouse clicks. Just follow [`INSTALL.md`](./INSTALL.md).

**Do I need a VPN?** No. Claude Code installs from a China mirror; DeepSeek connects directly.

**How much does it cost?** Only DeepSeek needs a top-up — ¥10 (≈$1.5) lasts a long while. Everything else is free. Measured: all 11 demo prompts (multi-file analysis over 169 notes) cost **¥0.26 total**.

**Phone / tablet?** No. Claudian is desktop-only (Windows / Mac).

---

## Blueprint / build

**I said "build from the Blueprint" but Friday didn't act / built it wrong?**
1. Confirm the Blueprint file sits in the vault **root** (not a subfolder).
2. Tell it: "**Re-execute Blueprint Section 6 exactly.**"
3. Still stuck? Use the Blueprint's manual fallback — six folders by hand plus one copy-paste, two minutes.

**The build is missing pieces (no templates / skills / interview)?**
Usually means it ran in a **non-empty folder**. Either tell it "re-execute Section 6 steps 1-11 one by one, skip nothing", or — most reliable — start over in a fresh empty folder (30 seconds).

**Downloaded Blueprint invisible in Obsidian / saved as .txt?**
Browsers often save raw pages as `.txt`, and Obsidian only shows `.md` (Windows hides extensions, so you can't even tell). **Skip renaming — use copy-paste**: open the raw page → Ctrl+A, Ctrl+C → in Obsidian Ctrl+N, name it, Ctrl+V.

**Can I edit the Blueprint / contract?**
Of course — it's your brain. After setup the rules live in `system/CLAUDE.md`; edit them in plain language (e.g. "be more brief"). Friday follows the new rules from its next task.

---

## Terminal

**`node -v` or `claude --version` does nothing / "not recognized"?**
1. Close the terminal **completely and reopen** (new installs need a fresh window).
2. Confirm the previous step actually finished (no Node.js → no claude).

**`npm install ...` is slow / spews red errors?**
1. Usually network — **run the exact same line again**.
2. If it still fails, swap the mirror:
   `npm install -g @anthropic-ai/claude-code --registry=https://registry.npmjs.org`
3. Confirm Node.js is LTS (v18+).

**`claude` asks me to log in / subscribe?**
cc-switch hasn't taken over yet. Go back to [`INSTALL.md`](./INSTALL.md) **Step 4**: DeepSeek provider created, key pasted correctly, "Sync" clicked, "Apply to Claude Code Plugin" enabled.

---

## DeepSeek / API key

**Closed the key popup without copying?** Fine — delete that key on the platform and create a new one. Copy it immediately this time.

**Friday won't reply / insufficient balance / 401?** Check in order:
1. **Topped up?** Zero balance = no replies.
2. **Key pasted right** in cc-switch? No extra spaces / missing characters?
3. Base URL exactly `https://api.deepseek.com/anthropic` (**don't drop `/anthropic`**).

**Which model names?** Main: `deepseek-v4-pro[1m]`; budget: `deepseek-v4-flash`. `[1m]` = long context, keep it.

---

## Claudian / Obsidian

**If I installed Claudian, can I skip Claude Code?**
No — **Claude Code is required**. Claudian is just a shell/steering wheel; it drives Claude Code as its engine (official hard requirement; without it you get `spawn claude ENOENT`). Installing the engine needs no subscription, no login, no VPN — cc-switch + DeepSeek handle the rest.

**Can't find Claudian in community plugins?**
1. "Turn on community plugins" clicked? 2. Obsidian ≥ 1.8.9? 3. Spelling: `Claudian`.

**Claudian installed but unresponsive / can't reach the AI?**
Set **Provider to "Claude"** (i.e., Claude Code) in Claudian's settings. Prerequisites: `claude --version` works, cc-switch synced to DeepSeek.

**New computer — do I lose my brain?**
Never. Your brain is the folder — **copy it**. Reinstall the apps on the new machine.

---

## Still stuck?

- Take a **screenshot** and note the **exact error text** of the step you're stuck on.
- Re-check every earlier step in [`INSTALL.md`](./INSTALL.md) ✅.
- **Ask in the community group** (WeCom QR coming soon — see README) or open an Issue in this repo.
- Official docs: DeepSeek × Claude Code 👉 https://api-docs.deepseek.com · cc-switch 👉 https://github.com/farion1231/cc-switch

> Order matters: foundation (Node) → engine (Claude Code) → key (DeepSeek) → wiring (cc-switch) → vault (Obsidian + Blueprint) → AI moves in (Claudian) → one sentence builds the brain.
> Whatever step fails, first confirm everything before it succeeded.
