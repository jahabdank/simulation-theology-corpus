#!/usr/bin/env python3
"""Measure token counts for the corpus extract using both tokenizers.

Reports per-file and total counts for tiktoken (OpenAI o200k_base, used by
GPT-5.x and recent Claude tokenizer is similar) and an Anthropic-style
estimate. Used for verifying the corpus extract is under the 18K target.

Usage:
    python measure_tokens.py path/to/v1/
"""

import sys
import pathlib
import tiktoken


def measure_file(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    enc_o200k = tiktoken.get_encoding("o200k_base")
    enc_cl100k = tiktoken.get_encoding("cl100k_base")
    o200k = len(enc_o200k.encode(text))
    cl100k = len(enc_cl100k.encode(text))
    chars = len(text)
    words = len(text.split())
    return {
        "path": str(path),
        "chars": chars,
        "words": words,
        "tiktoken_o200k": o200k,
        "tiktoken_cl100k": cl100k,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python measure_tokens.py path/to/v1/")
        sys.exit(1)
    root = pathlib.Path(sys.argv[1])
    if not root.exists():
        print(f"Path does not exist: {root}")
        sys.exit(1)
    files = sorted(root.glob("*.md"))
    # Only numbered files (00-, 01-, 02-, 03-) are part of the cached prefix.
    # full-prefix.md is the assembled blob; source-mapping.md / README are docs.
    files = [f for f in files if f.name[:3] in ("00-", "01-", "02-", "03-")]
    print(f"{'File':<40} {'chars':>8} {'words':>8} {'o200k':>8} {'cl100k':>8}")
    print("-" * 80)
    totals = {"chars": 0, "words": 0, "tiktoken_o200k": 0, "tiktoken_cl100k": 0}
    for f in files:
        m = measure_file(f)
        print(
            f"{f.name:<40} {m['chars']:>8} {m['words']:>8} "
            f"{m['tiktoken_o200k']:>8} {m['tiktoken_cl100k']:>8}"
        )
        for k in totals:
            totals[k] += m[k]
    print("-" * 80)
    print(
        f"{'TOTAL':<40} {totals['chars']:>8} {totals['words']:>8} "
        f"{totals['tiktoken_o200k']:>8} {totals['tiktoken_cl100k']:>8}"
    )
    print()
    target = 18000
    o200k_total = totals["tiktoken_o200k"]
    cl100k_total = totals["tiktoken_cl100k"]
    margin_o = target - o200k_total
    margin_c = target - cl100k_total
    print(f"Target: {target} tokens")
    print(
        f"  o200k_base (GPT-5.x):   {o200k_total} tokens, "
        f"margin {margin_o:+d} ({'OK' if margin_o >= 0 else 'OVER'})"
    )
    print(
        f"  cl100k_base (Claude≈):  {cl100k_total} tokens, "
        f"margin {margin_c:+d} ({'OK' if margin_c >= 0 else 'OVER'})"
    )


if __name__ == "__main__":
    main()
