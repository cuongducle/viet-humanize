#!/usr/bin/env python3
"""Đánh giá mẫu sinh bởi gpt-5.6-luna trên ngưỡng đã khóa từ eval v2."""
import glob, sys
from pathlib import Path
sys.path.insert(0, 'research')
from eval_v2 import per_file
from lexical_analysis import auc

KEYS = [
    'bien_dong_do_dai_cau_cv', 'ty_le_tu_rieng_ttr_am_tiet', 'mattr_cua_so_50',
    'entropy_dau_cau_bit', 'do_nen_zlib', 'diem_scan', 'lech_do_dai_cau_skew',
    'han_viet_lex/1k', 'tu_chuc_nang', 'pho_tu/1k', 'tro_tu_cuoi_cau_tren_1000',
    'tu_lay', 'tu_noi_khau_ngu', 'lien_tu_hinh_thuc_tren_1000', 'cau_trung_binh_doan'
]
# ngưỡng định trước, tuyệt đối không tối ưu lại trên Luna
THRESH = {
    'formal': [('bien_dong_do_dai_cau_cv', '<=', .290), ('entropy_dau_cau_bit', '<=', .960), ('han_viet_lex/1k', '>=', 17.045)],
    'casual': [('bien_dong_do_dai_cau_cv', '<=', .210), ('entropy_dau_cau_bit', '<=', .980), ('han_viet_lex/1k', '>=', 16.854)],
}

def val(m, k): return m.get(k, 0.0) or 0.0

def med(xs):
    xs = sorted(xs); return xs[len(xs)//2] if xs else 0

def result(h, a, k):
    x, y = [val(m,k) for m in h], [val(m,k) for m in a]
    raw = auc(x, y); direction = 'AI>ng' if raw >= .5 else 'ng>AI'
    return max(raw, 1-raw), direction, med(x), med(y)

def locked(h, a, k, op, t):
    x, y = [val(m,k) for m in h], [val(m,k) for m in a]
    f = (lambda z: z <= t) if op == '<=' else (lambda z: z >= t)
    return sum(f(z) for z in x), sum(f(z) for z in y), len(x), len(y)

def block(label, hp, ap, oldp, out):
    H, _ = per_file(sorted(glob.glob(hp)))
    L, _ = per_file(sorted(glob.glob(ap)))
    O, _ = per_file(sorted(glob.glob(oldp)))
    kind = 'formal' if 'formal' in ap else 'casual'
    out.append(f'\n## {label}\n\n')
    out.append('| chỉ số | AUC Luna | hướng | median người | median Luna | median AI cũ |\n|---|---:|---|---:|---:|---:|\n')
    for k in KEYS:
        a, d, hm, lm = result(H,L,k)
        om = med([val(m,k) for m in O])
        out.append(f'| `{k}` | {a:.3f} | {d} | {hm:.2f} | {lm:.2f} | {om:.2f} |\n')
    out.append('\nNgưỡng khóa từ v2 (không tối ưu lại):\n\n')
    for k, op, t in THRESH[kind]:
        fp, tp, nh, nl = locked(H,L,k,op,t)
        out.append(f'- `{k}` {op} {t}: FP người {fp}/{nh}, TP Luna {tp}/{nl}\n')
    out.append('\n')
    return H,L,O

def main():
    out = ['# Eval GPT-5.6-Luna trên ngưỡng v2\n\n',
           'Mẫu Luna được sinh sau khi chuyển model (`PI_MODEL=gpt-5.6-luna`). '
           'So sánh với corpus người v2 và AI cũ. Ngưỡng được khóa từ v2, không điều chỉnh theo kết quả Luna. '
           'Đây là test model-switch, chưa phải blind test: cùng chủ đề và cùng ngữ cảnh dự án.\n']
    hf, lf, of = block('TRANG TRỌNG (20 mẫu)', 'corpus/v2/human/*.md', 'corpus/v3-luna/ai-formal/*.md', 'corpus/v2/ai/*.md', out)
    hc, lc, oc = block('KHẨU NGỮ (12 mẫu)', 'corpus/v2/human-casual/*.md', 'corpus/v3-luna/ai-casual/*.md', 'corpus/v2/ai-casual/*.md', out)
    out += ['\n## Đọc kết quả\n\n',
            '- AUC Luna vẫn cao chỉ cho thấy chỉ số tách được hai nhóm trong bộ mẫu này; không phải bằng chứng model Luna nói chung luôn như vậy.\n',
            '- Nếu median Luna gần AI cũ ở một chỉ số, đó là tín hiệu có thể xuyên model. Nếu lệch mạnh, nhiều khả năng là tật riêng của model hoặc prompt.\n',
            '- Ngưỡng khóa chỉ có ý nghĩa khi giữ được FP/TP trên Luna; không được chọn lại threshold sau khi xem kết quả.\n']
    text = ''.join(out)
    Path('references/eval-luna.md').write_text(text, encoding='utf-8')
    print(text)
if __name__ == '__main__': main()
