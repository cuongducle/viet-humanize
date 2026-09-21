#!/usr/bin/env python3
"""Eval corpus v2: chủ đề khớp từng cặp + thêm register khẩu ý.
Xuất: bảng AUC từng chỉ số theo register, ngưỡng FP/TP, fightin' words v2,
ghi references/eval-v2.md. Chạy: python3 research/eval_v2.py
"""
import glob, math, sys
from collections import Counter
sys.path.insert(0, "scripts"); sys.path.insert(0, "research")
from vi_scan import scan
from lexical_analysis import toks, dens, auc, FUNCTION, SINO_VERBS, INTENSIFIERS

def per_file(paths):
    """trả về (list metric-dict, list token-list) cho từng file"""
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
        if a < 0.5: a, d = 1 - a, "ng>AI"; xr, yr = y, x
        else: d, xr, yr = "AI>ng", x, y
        rows.append((max(a, 1 - a), k, a, d, sorted(xr)[len(xr)//2], sorted(yr)[len(yr)//2]))
    rows.sort(reverse=True)
    for _, k, a, d, m1, m2 in rows:
        out.append(f"| `{k}` | {a:.3f} | {d} | {m1:.2f} | {m2:.2f} |\n")
    return rows

def threshold_eval(mh, ma, key, name, out, direction="AI>ng"):
    x = [m.get(key, 0.0) or 0.0 for m in mh]; y = [m.get(key, 0.0) or 0.0 for m in ma]
    best = None
    cands = sorted(set(x + y))
    for t in cands:
        if direction == "AI>ng": fp = sum(1 for v in x if v >= t); tp = sum(1 for v in y if v >= t)
        else: fp = sum(1 for v in x if v <= t); tp = sum(1 for v in y if v <= t)
        if best is None or (fp, -tp) < (best[0], -best[1]): best = (fp, tp, t)
    out.append(f"- `{key}`: ngưỡng {'≥' if direction=='AI>ng' else '≤'} {best[2]:.3f} -> FP người {best[0]}/{len(x)}, TP AI {best[1]}/{len(y)}\n")
    return best

def fightin(th, ta, out):
    ch = Counter(w for t in th for w in t); ca = Counter(w for t in ta for w in t)
    nh, na = sum(ch.values()), sum(ca.values())
    bg = ch + ca; nb = nh + na; alpha0 = 100.0
    vocab = {w: alpha0 * c / nb for w, c in bg.items()}
    def z(w):
        a_w, b_w = ca.get(w, 0), ch.get(w, 0); al = vocab.get(w, 0.5)
        d = math.log((a_w + al) / (na + alpha0 - a_w - al)) - math.log((b_w + al) / (nh + alpha0 - b_w - al))
        return d / math.sqrt(1/(a_w + al) + 1/(b_w + al) + 1/(na - a_w) + 1/(nh - b_w))
    top_ai = sorted(((z(w), w) for w in bg if ca.get(w, 0) >= 3), reverse=True)[:15]
    top_hu = sorted(((z(w), w) for w in bg if ch.get(w, 0) >= 3))[:15]
    out.append("\nAI lệch dương: " + ", ".join(f"{w} ({zv:+.1f})" for zv, w in top_ai) + "\n")
    out.append("Người lệch âm: " + ", ".join(f"{w} ({zv:+.1f})" for zv, w in top_hu) + "\n")

def main():
    out = ["# Eval corpus v2 (2026-09-21)\n\n",
           "Thiết kế: 20 cặp trang trọng (wiki/news) và 12 cặp khẩu ý (Góc nhìn/Genk/Kenh14), "
           "AI cùng chủ đề từng cặp, viết ở chế độ mặc định, một mô hình (nêu rõ hạn chế). ",
           "So với v1: hết nhiễu chủ đề trong fightin' words, thêm register khẩu ý.\n"]
    keys = ["diem_scan", "bien_dong_do_dai_cau_cv", "entropy_dau_cau_bit", "lech_do_dai_cau_skew",
            "ty_le_tu_rieng_ttr_am_tiet", "mattr_cua_so_50", "do_nen_zlib", "tu_chuc_nang",
            "han_viet_lex/1k", "pho_tu/1k", "tro_tu_cuoi_cau_tren_1000", "tu_lay",
            "tu_noi_khau_ngu", "lien_tu_hinh_thuc_tren_1000", "han_viet_hanh_chinh_tren_1000",
            "so_dau_bang_than", "dai_cau_tb", "cau_trung_binh_doan"]
    for name, hh, aa in [("TRANG TRỌNG (20 cặp, khớp chủ đề)", "corpus/v2/human/*.md", "corpus/v2/ai/*.md"),
                          ("KHẨU Ữ (12 cặp, khớp chủ đề)", "corpus/v2/human-casual/*.md", "corpus/v2/ai-casual/*.md")]:
        H = sorted(glob.glob(hh)); A = sorted(glob.glob(aa))
        mh, th = per_file(H); ma, ta = per_file(A)
        rows = table(mh, ma, keys, name, out)
        out.append("\nNgưỡng (FP người tối thiểu, TP cao nhất):\n")
        for k, d in [("diem_scan", "AI>ng"), ("bien_dong_do_dai_cau_cv", "ng>AI"),
                     ("entropy_dau_cau_bit", "ng>AI"), ("han_viet_lex/1k", "AI>ng"),
                     ("tu_chuc_nang", "ng>AI"), ("tro_tu_cuoi_cau_tren_1000", "ng>AI")]:
            threshold_eval(mh, ma, k, k, out, d)
        out.append("\nFightin' words (chủ đề đã khớp):\n")
        fightin(th, ta, out)
    open("references/eval-v2.md", "w", encoding="utf-8").write("".join(out))
    print("".join(out))

if __name__ == "__main__":
    main()
