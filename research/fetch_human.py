#!/usr/bin/env python3
"""Thu thập corpus văn NGƯỜI tiếng Việt: Wikipedia (bách khoa) + VnExpress (báo chí).
Zero-dependency. Mẫu được cắt thành đoạn 120-350 từ, bỏ bảng/mục lục."""
import json, re, html, pathlib, sys, time, urllib.request, subprocess

UA = {"User-Agent": "viet-humanize-calibration/1.0 (research-open)"}
OUT = pathlib.Path("corpus/human")

def fetch(url):
    r = subprocess.run(["curl", "-s", "--max-time", "25", "-A", UA["User-Agent"], url],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="replace")

def clean(t):
    t = re.sub(r"\[?\d+\]|\[Ghi chú \d+\]", "", t)          # tham khảo
    t = re.sub(r"(?m)^==+.*==+$", "\n", t)                   # đề mục
    t = re.sub(r"(?m)^\s*[*#:|].*$", "", t)                  # danh sách
    t = re.sub(r"\n{2,}", "\n\n", t).strip()
    return t

def chunks(t, lo=120, hi=330):
    paras = [p.strip() for p in t.split("\n\n") if len(p.split()) >= 15]
    out, buf = [], []
    for p in paras:
        buf.append(p)
        n = sum(len(x.split()) for x in buf)
        if hi <= n:
            if lo <= n:
                out.append("\n\n".join(buf))
            buf = []
    return out

# ---- Wikipedia ----
def wiki(n=15):
    got = 0
    while got < n:
        data = json.loads(fetch("https://vi.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=20"))
        titles = [x["title"] for x in data["query"]["random"]][:10]
        api = ("https://vi.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&explaintext=1&exintro=1&redirects=1&titles="
               + urllib.request.quote("|".join(titles), safe=""))
        q = json.loads(fetch(api))["query"]["pages"]
        for pid, page in q.items():
            if got >= n: break
            if "missing" in page: continue
            txt = clean(page.get("extract", ""))
            words = len(re.findall(r"\w+", txt))
            if words < 120: continue
            (OUT / "wiki").mkdir(parents=True, exist_ok=True)
            slug = re.sub(r"\W+", "_", page["title"])[:40]
            (OUT / "wiki" / f"{slug}.txt").write_text(txt[:33000])
            got += 1
        time.sleep(1.2)
    print(f"wiki: {got}")

# ---- VnExpress ----
FEEDS = ["tin-moi-nhat", "doi-song", "du-lich", "gia-dinh", "suc-khoe", "giao-duc"]
def news(n=15):
    links = []
    for f in FEEDS:
        try:
            rss = fetch(f"https://vnexpress.net/rss/{f}.rss")
            links += re.findall(r"<link>(https://vnexpress\.net/[^<]+\.html)</link>", rss)
        except Exception as e:
            print("feed lỗi", f, e)
        time.sleep(0.3)
    got = 0
    for url in links:
        if got >= n: break
        try:
            page = fetch(url)
        except Exception:
            continue
        ps = re.findall(r'<p class="description">(.*?)</p>|<p>(.*?)</p>', page, re.S)
        body = html.unescape(re.sub(r"<[^>]+>", " ", " ".join(a or b for a, b in ps)))
        body = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), body)
        body = body.replace("\\n", " ").replace("\\/", "/").replace("\\\"", '"')
        body = re.sub(r"\s+", " ", body).strip()
        cs = []
        buf, cnt = [], 0
        for p in [body]:
            ws = p.split()
            for i in range(0, len(ws), 250):
                seg = " ".join(ws[i:i+250])
                if len(seg.split()) >= 120:
                    cs.append(seg)
        for i, c in enumerate(cs[:2]):
            if got >= n: break
            (OUT / "news").mkdir(parents=True, exist_ok=True)
            aid = url.rsplit("-", 1)[-1].replace(".html", "")
            (OUT / "news" / f"{aid}_{i}.txt").write_text(c)
            got += 1
        time.sleep(0.4)
    print(f"news: {got}")

if __name__ == "__main__":
    wiki(int(sys.argv[1]) if len(sys.argv) > 1 else 15)
    news(int(sys.argv[2]) if len(sys.argv) > 2 else 15)
