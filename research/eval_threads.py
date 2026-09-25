#!/usr/bin/env python3
"""Eval corpus v4-threads: register khẩu ngữ thật từ Threads vs AI cùng chủ đề.
Tái dùng bộ đo của eval_v2. Xuống references/eval-threads.md.
Chạy: python3 research/eval_threads.py
"""
import glob, sys
from collections import Counter
sys.path.insert(0, "scripts"); sys.path.insert(0, "research")
from vi_scan import scan
from lexical_analysis import toks, dens, auc, FUNCTION, SINO_VERBS, INTENSIFIERS

def per_file(paths):
    ms, ts = [], []
    for p in paths:
        text = open(p, encoding="utf-8").read()
        r = scan(text)
        m = dict(r["nhip_hoc"]); m["diem_scan"] = r["score"]
        w = toks(p)
        m["tu_chuc_nang"] = sum(1 for x in w if x in FUNCTION) / max(len(w), 1)
        m["han_viet_lex/1k"] = dens(w, SINO_VERBS)
        m["pho_tu/1k"] = dens(w, INTENSIFIERS)
        ms.append(m); ts.append(w)
    return ms, ts

def table(mh, ma, keys, title, out):
    out.append(f"\n### {title}\n\n| chỉ số | AUC | hướng | md người | md AI |\n|---|---|---|---|---|\n")
    rows = []
    for k in keys:
        x = [m.get(k, 0.0) or 0.0 for m in mh]; y = [m.get(k, 0.0) or 0.0 for m in ma]
        if len(set(x)) < 2 and len(set(y)) < 2 and set(x) == set(y): continue
        a = auc(x, y)
        if a < 0.5: a, d = 1 - a, "ng>AI"
        else: d = "AI>ng"
        rows.append((max(a, 1 - a), k, a, d, sorted(x)[len(x)//2], sorted(y)[len(y)//2]))
    rows.sort(reverse=True)
    for _, k, a, d, m1, m2 in rows:
        out.append(f"| `{k}` | {a:.3f} | {d} | {m1:.2f} | {m2:.2f} |\n")
    return rows

def main():
    H = sorted(glob.glob("corpus/v4-threads/human-threads/*.md"))
    A = sorted(glob.glob("corpus/v4-threads/ai-threads/*.md"))
    R = sorted(glob.glob("corpus/v4-threads/human-replies/*.md"))
    mh, th = per_file(H); ma, ta = per_file(A)
    mr, tr = per_file(R)
    out = ["# Eval corpus v4-threads (2026-09-25)\n\n",
           "Corpus: 24 bài Threads Việt Nam (khẩu ngữ thật, đã ẩn danh) và 12 bài AI cùng chủ đề "
           "viết ở chế độ mặc định, thu bằng Chrome thật qua browser-skill. Chi tiết: corpus/v4-threads/manifest.md.\n"]
    keys = ["diem_scan", "bien_dong_do_dai_cau_cv", "entropy_dau_cau_bit", "lech_do_dai_cau_skew",
            "ty_le_tu_rieng_ttr_am_tiet", "mattr_cua_so_50", "do_nen_zlib", "tu_chuc_nang",
            "han_viet_lex/1k", "pho_tu/1k", "tro_tu_cuoi_cau_tren_1000", "tu_lay",
            "tu_noi_khau_ngu", "lien_tu_hinh_thuc_tren_1000", "han_viet_hanh_chinh_tren_1000",
            "so_dau_bang_than", "dai_cau_tb", "cau_trung_binh_doan"]
    table(mh, ma, keys, f"THREADS: {len(H)} người vs {len(A)} AI", out)

    out.append("\nTrợ từ cuối câu, từng file (trên 1000 âm tiết):\n\n| bên | số file > 0 | trung vị | max |\n|---|---|---|---|\n")
    for name, mm in [("người", mh), ("AI", ma), ("replies", mr)]:
        v = [m.get("tro_tu_cuoi_cau_tren_1000", 0.0) or 0.0 for m in mm]
        sv = sorted(v)
        out.append(f"| {name} | {sum(1 for x in v if x > 0)}/{len(v)} | {sv[len(sv)//2]:.1f} | {max(v):.1f} |\n")

    out.append(f"\nFightin' words ({len(A)} cặp khớp chủ đề):\n")
    ch = Counter(w for t in th for w in t); ca = Counter(w for t in ta for w in t)
    import math
    nh, na = sum(ch.values()), sum(ca.values())
    bg = ch + ca; nb = nh + na; alpha0 = 100.0
    vocab = {w: alpha0 * c / nb for w, c in bg.items()}
    def z(w):
        a_w, b_w = ca.get(w, 0), ch.get(w, 0); al = vocab.get(w, 0.5)
        d = math.log((a_w + al) / (na + alpha0 - a_w - al)) - math.log((b_w + al) / (nh + alpha0 - b_w - al))
        return d / math.sqrt(1/(a_w + al) + 1/(b_w + al) + 1/(na - a_w) + 1/(nh - b_w))
    top_ai = sorted(((z(w), w) for w in bg if ca.get(w, 0) >= 3), reverse=True)[:12]
    top_hu = sorted(((z(w), w) for w in bg if ch.get(w, 0) >= 3))[:12]
    out.append("\nAI lệch dương: " + ", ".join(f"{w} ({zv:+.1f})" for zv, w in top_ai) + "\n")
    out.append("Người lệch âm: " + ", ".join(f"{w} ({zv:+.1f})" for zv, w in top_hu) + "\n")

    open("references/eval-threads.md", "w", encoding="utf-8").write("".join(out))
    print("".join(out))

if __name__ == "__main__":
    main()
