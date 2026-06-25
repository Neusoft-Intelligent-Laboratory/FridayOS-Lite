# 🧩 How Friday Is Built (Tool Guide)

> **Read this before installing.** Once you see *why* each tool exists, the install steps make sense.
>
> 🌐 中文版：[`工具说明.md`](./工具说明.md)

---

## The whole picture

You're building yourself an AI second brain named **Friday** — like a real assistant, assembled from **four layers**, outside‑in:

```
  You
   │  say something
   ▼
┌───────────────────────────────────────────────┐
│ 1️⃣ Obsidian       — the brain's "body" (a notes app you can see)   │
│     └ 2️⃣ Claudian plugin — moves the AI *into* Obsidian's sidebar  │
│           └ 3️⃣ Claude Code — Friday's "engine" (the AI that works) │
│                 └ 4️⃣ cc-switch — the "chip switcher"               │
│                       └ 5️⃣ DeepSeek V4 — a cheap, no‑VPN "brain chip" │
└───────────────────────────────────────────────┘
```

Each layer solves a problem the previous one creates. That's why you need all five.

## 1️⃣ Obsidian — the body
A **free** notes app that opens a **folder** on your computer full of plain `.md` text files. It's the container your second brain lives in: plain text, no lock‑in, supports `[[wiki links]]`. But a notepad can store, not *think* — so we bolt an AI onto it.

## 2️⃣ Claudian plugin — moves the AI inside Obsidian
A free Obsidian community plugin that opens a chat sidebar, so you talk to the AI **inside your notes app** and never touch a scary terminal. It can read and write the notes in your folder directly. But Claudian is just a shell — it needs a real engine underneath.

## 3️⃣ Claude Code — the engine
A powerful AI agent engine (by Anthropic) that reads, edits, and completes multi‑step tasks over your files — exactly what a second brain needs. **The catch:** by default it connects to Anthropic's official models, which for users in China means paying in a foreign currency, using a VPN, and putting up with rate limits. That's the barrier the original FridayOS had. Lite removes it by pointing the engine at a domestic, cheap, no‑VPN model instead.

## 4️⃣ DeepSeek V4 — the cheap, no‑VPN chip
A top Chinese model that offers an **Anthropic‑compatible endpoint**, so Claude Code can use it seamlessly — like swapping the chip in the same engine. No VPN (connects directly to `api.deepseek.com`), pay‑as‑you‑go for pennies per million tokens, and smart enough for writing, organizing, and coding. You just register, top up a little, and grab an **API Key**.

## 5️⃣ cc-switch — the switcher
A free desktop GUI. To make Claude Code use DeepSeek instead of Anthropic you'd normally edit environment variables by hand (beginner nightmare). cc-switch does it in two clicks: pick "DeepSeek", paste your API Key, hit Sync. DeepSeek is the electricity; cc-switch is the switch.

## In one sentence
> **Obsidian** is the body, **Claudian** brings the AI inside it, **Claude Code** is the engine, and **cc-switch** wires that engine to **DeepSeek V4** — a chip that's both cheap and VPN‑free. Together they are **Friday**.

What the five tools add up to is **Vibe Knowledge Management**: you speak plain language; Friday manages the knowledge base.

**Lite's boundary**: these five tools plus one [`FRIDAY-BLUEPRINT.md`](./FRIDAY-BLUEPRINT.md) give you a knowledge base managed inside Obsidian — that's all of Lite. Automated entry points (Feishu chat capture, feed-your-brain-from-anywhere) belong to the full [FridayOS](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS); your folder upgrades over as-is.

Next 👉 follow [`INSTALL.md`](./INSTALL.md) step by step.
