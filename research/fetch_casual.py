#!/usr/bin/env python3
"""Lấy mẫu người register khẩu ý/bạn đọc: VnExpress Góc nhìn (văn quan điểm cá nhân),
Genk (công nghệ, giọng trẻ), Kenh14 (giải trí, giọng trẻ trộn Anh).
Chạy: python3 research/fetch_casual.py [số bài mỗi nguồn]
"""
import html, os, re, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (research)"}

def rss_links(path):
    x = open(path, encoding="utf-8").read()
    items = re.findall(r"<item>(.*?)</item>", x, re.S)
    out = []
    for it in items:
        m = re.search(r"<link>(?:<!\[CDATA\[)?(https?://[^<\]]+)", it)
        if m: out.append(m.group(1))
    return out

def fetch(url):
    for _ in range(2):
        try:
            r = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(r, timeout=15).read().decode("utf-8", "ignore")
        except Exception:
            time.sleep(2)
    return ""

def unesc(t):
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), t)

VI = re.compile(r"[ăâđêôơưàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹ]")

def paragraphs(url):
    t = fetch(url)
    ps = re.findall(r'<p[^>]*class="[^"]*(?:Normal|description|t-j)[^"]*"[^>]*>(.*?)</p>', t, re.S)
    if len(ps) < 3:
        ps = re.findall(r"<p[^>]*>(.*?)</p>", t, re.S)
    out = []
    for p in ps:
        p = html.unescape(unesc(re.sub(r"<[^>]+>", " ", p)))
        p = re.sub(r"\s+", " ", p).strip()
        w = len(p.split())
        cond = (4 <= w <= 60) and VI.search(p) and not re.search(r"function|localStorage|window\.|\{", p)
        if cond: out.append(p)
    return out

def main(n_each=4):
    os.makedirs("corpus/v2/human-casual", exist_ok=True)
    srcs = [("gocnhin", "/tmp/goc-nhin.xml"), ("genk", "/tmp/genk.xml"), ("kenh14", "/tmp/kenh14.xml")]
    for name, path in srcs:
        got = 0
        for url in rss_links(path):
            if got >= n_each: break
            ps = paragraphs(url)
            text = "\n\n".join(ps)
            if len(text.split()) < 90: continue
            slug = re.sub(r"[^a-z0-9]+", "-", url.split("/")[-1].replace(".html", "")).strip("-")[:40]
            open(f"corpus/v2/human-casual/{name}_{slug}.md", "w", encoding="utf-8").write(text[:2200])
            print(f"{name}: {slug} ({len(text.split())} từ)")
            got += 1
            time.sleep(1)
        print(f"--> {name}: {got} bài")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
