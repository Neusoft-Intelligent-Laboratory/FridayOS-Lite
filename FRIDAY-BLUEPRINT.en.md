# 🧠 Friday Brain Blueprint

> **This single document is the complete blueprint of your second brain.**
> No template to download, no repo to clone — drop this file into an empty folder,
> then tell Friday in the Claudian chat:
>
> **"Read the Friday Brain Blueprint and build my brain according to it."**
>
> It will set up everything itself — your first demo of what Friday can do. ✨
>
> (Haven't installed Obsidian + Claudian yet? Start with [`INSTALL.en.md`](./INSTALL.en.md).)

---

## 1. The idea: one folder is one brain

Human brains are great at thinking, terrible at storage — we forget, we lose, we mess up. A second brain is externally attached memory that never forgets, and Friday is the butler who lives inside and keeps it tidy.

Three principles:

1. **One folder is one brain.** Every note is plain `.md` text — no database, no lock-in. Copy the folder and you've moved your entire brain.
2. **Notes flow; they don't pile up.** Most note apps become write-only graveyards. Here knowledge has a lifecycle: quick captures (`inbox`) → things in motion (`exec`) → worth keeping (`wiki`) → repeated work becomes routine (`skills`). What doesn't flow gets deleted.
3. **You think, Friday remembers.** Say something in passing — Friday decides where it goes, creates the note, fixes the format. Ask a question — it searches your brain first, then answers.

## 2. The six brain regions

| Region | Folder | In a line | What goes in |
|---|---|---|---|
| 📥 Inbox | `inbox/` | Capture fast, sort later | Sudden ideas, key lines from chats, links to read |
| 🎯 Workbench | `exec/` | The 3–7 things in motion | Current tasks, weekly plan, daily log |
| 📚 Knowledge | `wiki/` | Worth keeping long-term | Polished notes, concepts, people & things |
| ⚙️ Skills | `skills/` | Repeated work as routines | Fixed procedures you often ask Friday to run (advanced) |
| 📦 Archive | `raw/` | Source material, read-only | Originals, PDFs, long documents, references |
| 🫀 Core | `system/` | The brain's manual | `CLAUDE.md` — Friday's behavior contract |

How to use each region:

### 📥 inbox/ — quick capture
Anything you haven't decided where to put goes here, one small file per item. **Never organize inside inbox** — its job is to catch. Every so often, tell Friday **"clean up my inbox"**: active items move to `exec/`, keepers get polished into `wiki/`, useless ones get deleted (with your confirmation).

### 🎯 exec/ — in motion
Keep concurrent work to **3–7 items**; more means it's time to clean up. Two recommended standing files — **write them by hand or let Friday do it**:

- `Weekly Plan.md` — list the week's goals on Monday, review and cross off on Friday;
- `Today.md` — today's todos and scratch notes; Friday archives what expires.

When something finishes: if it has lasting value, have Friday distill it into `wiki/`; otherwise delete.

### 📚 wiki/ — knowledge base
Long-term knowledge lives here. Connect notes with `[[wikilinks]]` (write `[[Another note]]`) — over time it becomes your personal Wikipedia. Every note starts with three lines of frontmatter (Friday adds them automatically):

```yaml
---
created: 2026-06-10
updated: 2026-06-10
tags: []
---
```

### ⚙️ skills/ — routines (advanced; fine to leave empty)
When you notice yourself asking Friday for the same kind of work repeatedly (e.g., "format meeting notes the usual way"), have it write the steps down as a skill file here, then invoke it with one sentence next time.

### 📦 raw/ — source material
Originals, PDFs, long documents. **Friday reads but never modifies** — the brain's only immutable region, so original facts stay traceable.

### 🫀 system/ — core
Rules only. The heart is `CLAUDE.md` — the behavior contract Friday reads before any work (full text in the next section). This blueprint is archived here after setup.

## 3. Friday's behavior contract

During setup, Friday writes the content of the code block below **verbatim into `system/CLAUDE.md`**:

```markdown
# Friday · System Contract

> The first file Friday (the AI agent) reads before any work.

## Who you are

You are **Friday**, the user's AI second-brain butler.
Personality: proactive, reliable, great memory. The user forgets and loses things;
you catch, organize, remind, and execute for them.
Speak the user's language. Be concise and warm, like a dependable assistant. No rambling.

## The brain's regions

| Folder | Role | When to write there |
|---|---|---|
| inbox/ | Quick capture | Anything said in passing, not yet sorted |
| exec/ | Work in motion | Current tasks, weekly plan, daily log |
| wiki/ | Long-term knowledge | Polished notes, concepts, people/things worth keeping |
| skills/ | Routines | Repeated procedures distilled into steps |
| raw/ | Source material | Originals/long documents; **read-only for you** |
| system/ | This file | Global rules |

## How to work

1. **Catch first**: decide which folder each thing belongs to. Unsure → inbox/.
2. **Route**: when asked to "clean up the inbox", triage —
   active → exec/; keepers → wiki/; useless → delete after confirmation;
   repeated procedures → distill into skills/.
3. **Search before answering**: check wiki/ and exec/ for relevant context first.
4. **Filenames**: the user's language, short (≤ 20 characters), self-explanatory.
5. **Frontmatter** on every wiki note (created / updated / tags).
6. **Ask when unsure**: where to file, whether to delete — ask first. **Never delete on your own.**

## The one rule

> **Carry the load so the user doesn't have to.** Whatever you can organize or
> remember, never make the user do it.
```

## 4. Setup instructions

### For Friday: execute exactly 🤖

When the user asks you to build the brain from this blueprint:

1. Confirm the current working directory is the vault root (the folder containing this blueprint).
2. Create six folders: `inbox/`, `exec/`, `wiki/`, `skills/`, `raw/`, `system/`.
3. Write the **entire content of the Section 3 code block** verbatim into `system/CLAUDE.md`.
4. Create `exec/Weekly Plan.md` with a simple template: three goals this week (empty list) + Friday review (empty).
5. Create `wiki/Welcome.md`: a few sentences on how the wiki region works and how to write wikilinks, with frontmatter as a demonstration.
6. Move this blueprint file into `system/` for archival.
7. Report back: list the structure you built, then invite the user to try their first capture — "Save to inbox: …".

Do nothing beyond these steps; never delete or modify the user's other files.

### Manual fallback: if the AI doesn't do it 🛠️

The brain is just 6 folders — two minutes by hand:

1. Right-click in the vault and create 6 folders: `inbox`, `exec`, `wiki`, `skills`, `raw`, `system`;
2. Create `system/CLAUDE.md` and paste in the Section 3 code block;
3. Done. Drag this blueprint into `system/` to archive it.

## 5. Getting started: three sentences to learn

1. **"Save to inbox: meeting with the boss at 3pm tomorrow."** — quick capture, your highest-frequency move.
2. **"Put my three goals for this week into exec."** — start the weekly plan.
3. **"Clean up my inbox."** — regular triage that keeps knowledge flowing.

Once comfortable, try: "Read that document in raw and distill the key points into wiki", or "I'm working on project X — create a wiki page for it."

## 6. Want more?

**Lite focuses on one thing: managing your knowledge base with Obsidian + Claudian.** Write daily/weekly plans by hand, feed the inbox through chat — that's 80% of a second brain's value already.

When you want "feed your brain from anywhere with one sentence" — capture via Feishu chat, bot-assisted daily planning, a `domains/` project workbench, personality adaptation — upgrade to the full 👉 [**FridayOS**](https://github.com/Neusoft-Intelligent-Laboratory/FridayOS). Your folder moves over as-is, no migration.

---

*FridayOS‑Lite · One document, one sentence, one brain.*
