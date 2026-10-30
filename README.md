# pf-uv-research-log

Pauli–Fierz 模型の紫外の極限についての研究を、Claude Code とともに進めた記録です。A record of my study of the ultraviolet limit of the Pauli–Fierz model, carried out with Claude Code.

## 日本語

論文には成功した道しか書かれません。この研究の大半は、試して閉じた方式、方針の転換、数値計算の失敗、運用の規則の作り直しでした。AI を伴う数学研究の一つの実例として、その経過を残します。

- 著者:田林 伸一郎(論文の著者名は旧姓の S. Futakuchi)
- 期間:2026-09-02 〜 2026-10-28
- 論文 I:[The sharp leading asymptotics of the self-energy of the spinless Pauli–Fierz model](https://arxiv.org/abs/2610.34122)
- 論文 II:[The effective mass of the Pauli–Fierz electron: a cutoff-independent lower bound and the breakdown of mass renormalization](https://arxiv.org/abs/2610.34125)
- 付属コード:https://github.com/tabayashi0117/pauli-fierz-uv-limit-code

どちらも 2026-10-28 に Communications in Mathematical Physics に投稿しました(査読中)。ここに書いた検証は AI の監査と私の確認によるもので、外部の査読はこれからです。

| 場所 | 中身 |
|---|---|
| [book/ja/01_経緯.md](book/ja/01_経緯.md) | 問いから CMP 投稿まで |
| [book/ja/02_証明と失敗.md](book/ja/02_証明と失敗.md) | 証明の検証、初等化、手詰まりの抜け方、失敗 |
| [book/ja/03_数値計算.md](book/ja/03_数値計算.md) | 6 台のマシン、資源の管理、ジョブの設計 |
| [book/ja/04_AIとの協業.md](book/ja/04_AIとの協業.md) | 分担、台帳、成算、集中攻撃、フック |
| `catalog/` | 失敗の全件の索引 |
| `data/ledgers/` | 台帳の写し(2026-10-27 時点、機械で整理したもの) |
| `rules/` | 運用の規則の実物(AI に読ませた文章のまま) |

## English

Papers report only the paths that worked. Most of this study was approaches tried and closed, changes of strategy, failed computations and rewrites of the working rules. This repository keeps that history as one example of mathematical research done with AI.

- Author: Shin-ichiro Tabayashi (papers published under my former name, S. Futakuchi)
- Period: 2026-09-02 to 2026-10-28
- Paper I: [arXiv:2610.34122](https://arxiv.org/abs/2610.34122); Paper II: [arXiv:2610.34125](https://arxiv.org/abs/2610.34125)
- Ancillary code: https://github.com/tabayashi0117/pauli-fierz-uv-limit-code

Both papers were submitted to Communications in Mathematical Physics on 2026-10-28 and are under review. The checks described here were done by AI audits and by me; external peer review is still ahead.

| Where | What |
|---|---|
| [book/en/01_history.md](book/en/01_history.md) | From the question to the CMP submission |
| [book/en/02_proofs_and_failures.md](book/en/02_proofs_and_failures.md) | Proof checking, simplification, getting unstuck, failures |
| [book/en/03_numerics.md](book/en/03_numerics.md) | Six machines, resource management, job design |
| [book/en/04_working_with_ai.md](book/en/04_working_with_ai.md) | Division of labour, ledgers, feasibility estimates, all-out attacks, hooks |
| `catalog/`, `data/ledgers/`, `rules/` | Failure index, ledger copies and rules (Japanese originals) |

## License

Text and data: CC BY 4.0 (`LICENSE`). Code: MIT (`LICENSE-CODE`).
