"""公開前の検査:私的な情報が残っていないかを grep の型で調べる(書き換えはしない)。

使い方: python tools/sanitize.py [路 ...](既定はリポジトリ全体)
終了コード: 0 = 検出なし、1 = 検出あり(行を表示)。人の目の確認の代わりではない。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 消すもの(絶対パス・計算機名・ユーザー名・メール・セッション ID)
BLOCK = [
    (r"/Users/[A-Za-z]", "絶対パス(macOS)"),
    (r"[A-Za-z]:\\Users\\", "絶対パス(Windows)"),
    (r"/private/tmp/", "一時ディレクトリ"),
    (r"\b(futak)\b", "ローカルのユーザー名"),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "メールアドレス"),
    (r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", "セッション ID・UUID"),
    (r"\ba[0-9a-f]{16}\b", "サブエージェントの ID"),
    (r"(api[_-]?key|token|secret)\s*[:=]", "鍵・トークン"),
]
# 人の目で確かめるもの(敬意・未公開のやり取り)
REVIEW = [
    (r"(Hiroshima|Bach|Hach)", "他者への言及 —— 技術的な事実だけか"),
    (r"(撤回|withdrawn|誤り|error)", "撤回・誤りの言及 —— 敬意のある書き方か"),
]
SKIP = {".git", "LICENSE", "LICENSE-CODE"}


def files(args):
    if args:
        for a in args:
            p = Path(a)
            yield from (p.rglob("*") if p.is_dir() else [p])
    else:
        yield from ROOT.rglob("*")


def main(args):
    hit = 0
    for p in files(args):
        if not p.is_file() or any(s in p.parts for s in SKIP) or p.name in SKIP or p.suffix in {".pdf", ".png", ".json"}:
            continue
        if p.resolve() == Path(__file__).resolve():
            continue
        for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for pat, why in BLOCK:
                if re.search(pat, line, re.I):
                    print(f"BLOCK {p.relative_to(ROOT) if p.is_absolute() else p}:{n}: {why}: {line[:120]}")
                    hit = 1
            for pat, why in REVIEW:
                if re.search(pat, line):
                    print(f"REVIEW {p.relative_to(ROOT) if p.is_absolute() else p}:{n}: {why}")
    return hit


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
