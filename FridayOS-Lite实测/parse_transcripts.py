# -*- coding: utf-8 -*-
"""Claude Code JSONL 逐字稿 → 可读 Markdown 对话稿
用法: python3 parse_transcripts.py  (在 FridayOS-Lite实测/ 目录下运行)
扫 raw-transcripts/ 全部 .jsonl, 每个会话输出 transcripts-md/<时间>-<会话>.md"""
import json, os, glob
from datetime import datetime

SRC, DST = 'raw-transcripts', 'transcripts-md'
os.makedirs(DST, exist_ok=True)

def text_of(content):
    if isinstance(content, str): return content
    out = []
    for b in content if isinstance(content, list) else []:
        t = b.get('type')
        if t == 'text': out.append(b.get('text',''))
        elif t == 'tool_use': out.append(f"🔧 [{b.get('name','?')}] {json.dumps(b.get('input',{}),ensure_ascii=False)[:200]}")
        elif t == 'tool_result':
            c = b.get('content','')
            s = c if isinstance(c,str) else json.dumps(c,ensure_ascii=False)
            out.append(f"↩️ 工具返回: {s[:300]}{'…' if len(s)>300 else ''}")
    return '\n'.join(x for x in out if x)

for path in sorted(glob.glob(os.path.join(SRC,'**','*.jsonl'), recursive=True)):
    lines, first_ts = [], None
    for raw in open(path, encoding='utf-8', errors='replace'):
        raw = raw.strip()
        if not raw: continue
        try: ev = json.loads(raw)
        except Exception: continue
        typ = ev.get('type'); msg = ev.get('message') or {}
        ts = ev.get('timestamp','')
        if first_ts is None and ts: first_ts = ts
        if typ == 'user':
            txt = text_of(msg.get('content',''))
            if txt.strip(): lines.append(f"\n## 🧑 用户  `{ts[11:19] if len(ts)>18 else ''}`\n\n{txt}")
        elif typ == 'assistant':
            txt = text_of(msg.get('content',''))
            if txt.strip(): lines.append(f"\n### 🤖 Friday\n\n{txt}")
        elif typ == 'result':
            cost = ev.get('costUSD') or ev.get('total_cost_usd')
            if cost: lines.append(f"\n> 💰 本会话成本: ${cost}")
    if not lines: continue
    sid = os.path.splitext(os.path.basename(path))[0][:8]
    proj = os.path.basename(os.path.dirname(path))[-40:]
    day = (first_ts or '')[:10] or 'unknown'
    out = os.path.join(DST, f"{day}-{proj}-{sid}.md")
    with open(out,'w',encoding='utf-8') as f:
        f.write(f"# 逐字稿 · {proj} · {sid}\n来源: {path}\n" + '\n'.join(lines) + '\n')
    print("✅", out, f"({len(lines)} 轮)")
print("完成。逐字稿在 transcripts-md/")
