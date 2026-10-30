> 研究ノートの台帳からの写し(2026-10-27 時点)。元は E05 の `FAILED.md`。整理の規則と除いた件数は [`README.md`](README.md)。台帳の本文は改変していない(整理の置き換えを除く)。

# E05 FAILED(append-only)

## F1 — 「フル PF の1ループでも双極子と同じ線形質量発散が出る」
- 日付: 2026-09-02
- 分類: 仮説の反証(自前導出+文献)
- 正確な障害: 反跳 $k^2/2m$ により $`\int_0^\Lambda\frac{k\,dk}{k+k^2/2m}=2m\ln(1+\Lambda/2m)`$。Hiroshima–Spohn 2005 (1.22) と一致。
- 帰結: 双極子の $\Lambda_c$(命題A)はフル PF に外挿できない。族の終端問題は非摂動的 $h(\lambda)$ の増大度の問題(Q3)に置き換わる。
- 再挑戦条件: なし(確定)。

## F2 — 「コヒーレント(Weyl)ドレッシング試行状態で $h(\lambda)\gtrsim\lambda$(線形以上)を示す」
- 日付: 2026-09-02
- 分類: 手法の失敗(部分的成功を伴う)。詳細は稿 10
- 正確な障害: (i) $1/m_{eff}$ は $P=0$ での2階微分なので、試行族の変分欠損 $\eta\gt0$ がどれほど小さくても $2\eta/P^2\to\infty$ で情報が消える。
  族は厳密な $\psi_0$ に錨を下ろすしかない。(ii) 錨を下ろしても、スクイーズの不確定性下界と $\langle H_f\rangle_0\le E(0)$ から天井
  $h_{coh}-1\le\frac{16\alpha}{3\pi}\frac{\sqrt{2mE(0)}}{m}\ln(1+\frac{\Lambda}{2\sqrt{2mE(0)}})$ が出て、$E(0)\le Cm\lambda^\theta$($\theta\lt2$)なら劣線形。
  無条件に使える上界は $E(0)\le\frac{\alpha m\lambda^2}{2\pi}$($\theta=2$)のみで、それでは殺せない(条件付き)。
- 部分的成果: $E(0)$ は障害でない(アフィン構造 $H(P)=H(0)-\frac1mP\cdot v+\frac{P^2}{2m}$ で相殺、$m_{eff}\ge m$ が無条件)。
  コヒーレント族の Cauchy–Schwarz 最適化は重み $w(k)=\frac{16\pi}{3}k^3(1+\frac{k}{2m})$ を与え、$k/2m$ を落とすと双極子の線形、残すと HS 2005 (1.22) の対数を再現。
  **双極子近似=ファイバー表示で $P_f$ を落とすこと**。Hiroshima–Ito (math-ph/0412026) (2.35) が同じ Feynman–Hellmann 表示、(1.2)–(1.4) の「$\exists\gamma\lt1$」条件は Q3 と同一定式化。
- 再挑戦条件: 変分でなく作用素不等式で反跳項 $R$ の上界(劣線形の直接決着)、または判定基準 $`\mathcal N(k)=\langle\Phi(h_k)^2\rangle_0/\|h_k\|^2`$ の高波数漸近($\asymp1$ なら対数、$\lesssim m/k$ なら線形)。
- 〔2026-10-26 注記(w_E05_728、本文は変えない):本節の標的 $h\gtrsim\lambda$ は別の道で定理になった —— E05-P374(v-b、全ての λ > 0 で $h_{\rm ls}\ge c\lambda$)。障害 (i)(ii) は試行状態の方式の障害として有効のまま。〕

## F3 — 「判定基準 R2($\mathcal N(k)\asymp1$ なら対数、$\lesssim m/k$ なら線形)で Q3 を決着できる」
- 日付: 2026-09-02(11_)
- 分類: 手法の失敗(判定基準の誤り)
- 正確な障害: 反跳項 $R$ は $v_\mu\psi_0$ のスペクトル測度の $-1$ 次モーメントで、その上界には低エネルギー端 $\mu([0,\omega])$ が要る。
  非負次モーメント($\mathcal N$ は2点関数)からは出ない。R2 から出るのは**下界**(定理A)だけで、「$\mathcal N\asymp1\Rightarrow$ 対数」は誤り
  (正しくは「この方法で出る下界が対数止まり」)。また点ごとの $\mathcal N(k)$ は殻幅→0 で 1 に潰れ ill-posed(二次形式比較に置換)。
- 副産物: 定理F(コヒーレント族の天井は無条件に $o(\lambda)$)、pull-through は $k$ 減衰を与えない、TRK 二重交換子は $\Lambda^4$ 発散で無力。
- 再挑戦条件: $\frac{m}{m_{eff}}=1-\frac{4(E(0)-\Theta)}{3\bar\omega^{harm}}$ の調和平均エネルギー $\bar\omega^{harm}$ の下界(低エネルギー端の制御、B8)。
- 〔2026-10-26 注記(w_E05_728、本文は変えない):本節が決着を狙った Q3 は E05-P374(v-b)で漸近で決着(線形以上)。判定基準 R2 の誤りの記録は有効のまま;再挑戦条件は Q3 の決着の手としては失効。〕

## F4 — 「調和平均エネルギー $\bar\omega^{harm}$ の下界(低エネルギー端の制御)で $h$ の劣線形上界を出す」
- 日付: 2026-09-02(12_)。**Q3 は同系統(変分/スペクトル測度)で3ラウンド停滞 → 打ち切り**(math-research 規則)。
- 分類: 手法の失敗(4方向)+定式化の部分成功
- 正確な障害: (a)(b) 交換子・$\partial_P$ 恒等式からの $\mu([0,\omega])\le R\omega$ は Chebyshev と同一で自明。(c) 赤外正則化は無力 —
  予算命題により決定窓は $\omega\asymp E(0)\asymp\alpha\Lambda^2/m$、すなわち深紫外 $k\gtrsim\sqrt\alpha\Lambda$ にあり、$H(0)\ge X$ 型の soft な作用素不等式は全滅(自己エネルギー障壁)。
  (d) BCFS/CFP に必要な向き(分散関係の下界)の評価なし。
- 部分成果: $R=\int F(\omega)\omega^{-1}d\ln\omega=m^2\int_0^\infty C(\theta)d\theta$(虚時間速度自己相関、R3=R4)、$\kappa=\sup F/\omega$、$W=R/\kappa\ge1$、
  マスター評価 $R\le\kappa(2+\ln\frac{AM_0}{\kappa^2})$。**決着の必要十分標的: $\kappa\le\frac{3m}{4\ln\lambda}(1-\varepsilon)$**。数値($\alpha=0.01$, $\Lambda/m\le11$)で $W$ はフル PF で増え続け($1.0\to2.4$)、双極子で飽和($1.44$)。
  (H3) $E(P)\ge E(0)$ の出典: Hasler–Siebert [arXiv:2007.01250](https://arxiv.org/abs/2007.01250) → Gross, JFA 10 (1972)。
- 注意: HS 2005 の2ループ主要項 $\alpha^2\sqrt\lambda$ は「$\kappa$ が $\Lambda$ で平坦」を否定し**線形側**を示唆(11_ の直観と衝突、符号未確認)。
- 再挑戦条件(R5): 切断に関する流れの微分不等式 $\partial_\Lambda\ln(1/m_{eff})\ge-c\alpha/\Lambda$(滑らかな切断で FH 表示)。ただし先に**2ループ $\kappa$ の kill-check**(HS の $\sqrt\lambda$ と整合するか)。
- 〔2026-10-26 注記(w_E05_728、本文は変えない):本節の標的($h$ の劣線形の上界)は E05-P374(v-b、全ての λ > 0 で $h_{\rm ls}\ge c\lambda$)で偽 —— 再挑戦条件 R5 は標的ごと失効(部分成果の恒等式の記録は有効)。〕

## F5 — 「R5: 流れの微分不等式 $\partial_\Lambda\ln m_{eff}\le c\alpha/\Lambda$(絶対定数 $c$)で $h\lesssim\lambda^{c\alpha}$」
- 日付: 2026-09-03(14_)
- 分類: 標的の定式化の誤り(手法は部分成功)
- 正確な障害: HS の $c_0\alpha^2\sqrt\lambda$ が主要項の領域で $\gamma=d\ln h/d\ln\lambda\to\frac12$、$\alpha\to0$ で 0 にならない。ただし $\frac12\lt1$ は劣線形なので Q3 自体は否定されない。
  エネルギー重み付き Cauchy–Schwarz は $\alpha$ の冪を1つ失い Landau スケールが $e^{c/\sqrt\alpha}$ に退化。補題8 $\mathcal E(P)\le\min(P^2/2m,|P|)$ により反跳エネルギーから殻重み $F$ の減衰を取る道は原理的に閉じる。
- 収穫: 流れ恒等式(定理3)、$R=\int\kappa_{flow}d\ln\Lambda$ の恒等表示(命題4、12_ の $W$・$A$・$M_0$・IR 切断を不要化)、Q3 の局所同値形(定理5)、障害の同定(定理9: $f(\Lambda)\lesssim\frac{1}{\alpha\lambda h}$)。
- 再挑戦条件: R5′(予算消費形を殻双一次形式から CS 禁止で直接)、**R6(最優先)**: 殻内2光子背中合わせ相関 $f(\Lambda)$ の非摂動上界(まず (4.3) を殻射影×エネルギー射影の厳密2分割補題に)。
- 〔2026-10-26 注記(w_E05_728、本文は変えない):本節の標的 $h\lesssim\lambda^{c\alpha}$ は $c\alpha\lt1$ の域で E05-P374(v-b)により偽 —— 再挑戦条件 R5′・R6 は劣線形の標的として失効(流れの恒等式など収穫の記録は有効)。〕

## F6 — 「Gross 変換の最小結合版で PF の Fock 空間内 $\Lambda\to\infty$ 極限を構成する」(ROADMAP G3-2 の核心路線)
- 日付: 2026-09-03(16_、Fable)
- 分類: 手法の失敗(障害を命題として同定)
- 正確な障害: (命題1)$x$ 依存位相の Nelson 型 Weyl 作用素は作用素値ゲージ変換で横成分 $A_S$ に触れない。(命題2)Gross 選択 $T_S=-\frac{ie}{m}\mathbf Y_S(x)\cdot\pi_\Lambda$($\mathbf Y_S$=Welton 零点変位、可換族)は
  Q 空間表現で確率的体積保存微分同相として真のユニタリを与え、殻の $O(e^2)$ を局所反項 $\frac{\pi^2}{2m}(1-\delta m_S/m)$ で吸収するが、Doppler 残差 $R_D\propto e\gamma_k(k\cdot v)(\rho\cdot v)$ が $H^{3/2}$-形有界にしかならず、対項は無傷。
  厳密 SW 選択は Cherenkov 集合 $|p|\ge m+|k|/2$ で分母が消える。(命題3)局所 Bogoliubov は背中合わせ対で $`\|\beta\|_{HS}^2\simeq\frac{\alpha^2}\pi\sqrt{\Lambda/m}`$(解析+数値 $0.3126\to1/\pi$。audit27 2026-09-09 が表示式の因子 2 を訂正。数値の側が正しかった)、殻ごと実装可だが $\Lambda'\to\infty$ で非実装、質量繰り込みで悪化 — 13_ の HS $b_2\propto\sqrt\Lambda$ の状態側表現。
  (命題4)$[\pi^2/2m,\mathcal V_n]\subset\mathcal V_{n+1}$: PF は $\mathcal V_1$ から始まり任意の Gross 型ドレッシングが $\mathcal V_2$ 残差を残す(Nelson は $\mathcal V_0$ で1段で閉じる)。共通原因: 横性と反跳の選択性。
- 生き残り: 殻ごとの Welton ドレッシング($\varrho^{PF}\simeq\frac{\alpha^2}{\pi\sqrt{m\Lambda}}$、双極子 H8 と同じ Hölder-1/2)。
- 再挑戦条件/転進: (A) 双極子段の RG(H7–H14)を PF 対セクターへ $\varrho^{PF}$ で移植、(B) 構造群 $\mathrm{SDiff}(\mathbb R^3)\ltimes$Bogoliubov の非 Gauss 束、(C) IR 局所代数 $\mathfrak A_{\Lambda_0}$ 上の状態の weak* 極限(E05-F2 がその1ループ版)。
  kill-check K1–K4(Doppler 残差のスケーリング、局所反項係数、Cherenkov 閾値、背中合わせ対比 $(1+w/m)^2$、コサイクル欠損 $\propto e^2|P|/m$)を 16_ に設計。


## F7 — 「双極子段のハミルトニアン RG(T16/60_ H6–H14)を対セクターに移植して $\Lambda\to\infty$ ドレッシングを得る」(F6 の転進A)
- 日付: 2026-09-03(18_)
- 分類: 手法の失敗(障害を命題として同定)。移植は**半分だけ**成功。
- 移植できたもの: H6(標準ドレッシングの一意存在)、H7(生成子 $\mathcal G=\frac12\dot\Gamma\Gamma^{-1}$、純 $\beta$)、H8(殻密度・非 HS・Hölder-$\frac12$)、H12($\mathsf U$ 不変性)、H14(a)(b)(主 $\mathsf U$ 束・接続)。
  いずれも証明が純状態性と代数だけを使うため。さらに **$x$ 依存は純 $\mathsf U$ ゲージ $u_x$($\Gamma_\Lambda(x)=u_x\Gamma_\Lambda(0)u_x^{\mathsf T}$、厳密)であり、$\varrho$ の $x$ 一様性は漸近評価でなく恒等式**(命題A、数値 $10^{-13}$)。
- 正確な障害: (命題C)底空間が $(\mu,\infty)\times\mathbb R^3_x$ の4次元になるため **H14(c) の曲率零が不成立**。$\mathcal F_{\mu\nu}=[\mathcal G_\mu,\mathcal G_\nu]\in\mathfrak u(n)$、$O(e^4)$、数値で $`\|\mathcal F\|_F/e^4\to0.154`$、面積則・メッシュ収束・縮退プラケット($10^{-14}$)すべて確認。H11(a) のコサイクル性は $\Lambda$ 方向のみ。
  (命題B)$x$ 方向の接続核は $(k+q)_j\beta(k,q)$ で、16_ 命題4 の Doppler 残余と**同一の対象**。幾何の言葉と代数の言葉の違いにすぎず、新しい抜け道ではない。
  (命題D)$\Lambda$ 方向 $\varrho_\Lambda\propto\Lambda^{-1/2}\to0$ に対し $x$ 方向 $\varrho_x\simeq\frac13C\alpha^2\Lambda^2\to\infty$($C\approx0.44$、局所冪 2.018)。固定 $\delta$ では $`\|\beta(\Gamma_\Lambda(x),\Gamma_\Lambda(x+\delta))\|^2\to2\|\beta_{\le\Lambda}\|^2`$(打ち消しなし)。交差は $|\delta|\sim(m\Lambda)^{-1/2}$ で、束縛電子の広がり $\Delta x$ は完全飽和側。**各 $x$ で存在するが $x$ について束ねられない。**
  H9/H10(電子応答)は対セクターに対応物なし。H16($\varrho\simeq\frac{e^2\Lambda}\pi\Gamma_{xx}$)は移植不可: PF では $x$ が純位相で $`\|\beta\|`$ から落ちるため $\Gamma_\Lambda$ 因子分解が起きない(素朴な置換は線形発散を予言して命題3 と矛盾)。
- 副産物(16_ §8 の未決問題への回答): 双極子 H8 の $\Lambda^{-1/2}$ と PF 命題3 の $\Lambda^{-1/2}$ の一致は**偶然**。前者は強結合枝で $\varrho\propto e^1$($D\simeq e^2s^2g$)、後者は小結合の $\varrho\propto e^4$(反跳による背中合わせ位相空間の制限)。双極子の小結合枝は $\varrho\propto e^4\Lambda/m^2$(指数が違う)。$m^{-1/2}\Lambda^{-1/2}$ の形は指数が決まれば次元解析で決まる。
- 生き残り/転進: (1) $\mathsf U$ ゲージによる $x$ の厳密消去(命題A)。(2) **相補的台の分離**: $\sqrt\Lambda$ 発散は $|k+q|\lesssim\sqrt{m\Lambda}$(背中合わせ、$x$ に鈍感、$k+q=0$ では $p$ と厳密可換)、Doppler/曲率障害は $|k+q|\sim\Lambda$(可積分)。$|k+q|\le\sigma(\Lambda)$ で分割し前者を非 Fock 表現へ押し出す案 → 転進 B/C の入口(未検証)。(3) 曲率の明示形 $\mathcal F=[\mathcal G_\mu,\mathcal G_\nu]$。
- 記録: `18_対セクターのBogoliubovRG_転進A.md`(命題A–D、self-audited)、(研究ノート: `18_pair_sector_bogoliubov.py`)。

## F8 — 「殻内2光子相関 $f(\Lambda)$ の $\lambda$ 減衰をモーメント法(光子数・2次モーメント)で示す」(R6)
- 日付: 2026-09-03(17_、Fable)
- 分類: 手法の失敗(障害を命題として同定)
- 正確な障害: (a) 2次モーメント(Chebyshev、定理1)は $f_k(\theta)\le\frac{k^2M_0}{3m^2(\mu_k-\theta)^2}=O(\alpha)$ を $\Lambda$ 一様に与えるが、これは鋭い: $\theta=\mu_k/2$ の質量は摂動2次で $0.035\alpha$ に収束し(連続体数値、$\lambda\le3000$)、$\lambda$ 減衰しない。その質量は $\epsilon\sim\mu_k/3$ にあり流れには無害($O(\alpha^2m)$)だが、Chebyshev は $\theta=\mu_k/2$ と危険な $\theta\sim C\Lambda$(1光子質量は $\asymp\alpha\lambda^{-5/2}$)に同じ上界を与え、閾値情報を原理的に失う。分散は $`\|k\cdot v\psi_0\|^2/m^2`$ で $eA$ の生成部分が支配するため、対配位($P_f\approx-k$ の硬い光子)の重みは分散から分離できない。
  (b) 光子数ルート: $`p_{\ge2}=\|P^S_{\ge2}\psi_0\|^2\le\frac12\langle N_S^2\rangle`$ の非摂動評価は Lemma 7 の分母 $\omega+\mathcal E\le2|k|$(補題8)により $\langle N_S\rangle\lesssim\alpha^2\lambda^2$ と発散(14_ §4.2 と同じ壁)。仮に $p_{\ge2}\lesssim\alpha^2$ が得られても、$O(\Lambda)$ チャネルの重みは「対の総運動量 $\approx-k$」という角度相関で、光子数では表せない。
  (c) 流れ側では (3.1) の 1光子主チャネル $\mathcal T^{\rm main}$ のみ厳密に制御でき(1ループ値 $\le\Lambda\mathcal T^{\rm main}\le\frac{8\alpha m}{\pi}+1.9\alpha^2\Lambda$)、対配位を担う残余 $\mathcal R_\mu$(摂動的 $O(e^4)$)は非摂動的に未制御。
- 再挑戦条件: **尽きた(2026-09-09、22_ / F12 で消尽)**。旧条件のうち「17_ §7 の再帰的 Chebyshev」は 22_ 命題1(pull-through の非斉次項が閾値 $\theta=\Lambda\lambda^s$ を $s\lt1$ の全てで分解できない)と命題3(再帰 1 段の利得は $O(\alpha)$ で $\lambda$ 非依存)で閉鎖。「$(P_f,H_f)$ の同時スペクトル測度の大偏差評価」は 22_ 命題4($\lambda^{-1}$ は射影が供給せねばならず、射影を含まないモーメント上界は原理的に無効)で閉鎖。「対セクター限定の分散下界」は $f$ の減衰ではなく Q3 否定側($\kappa_{\rm flow}$ の下界)の道具なので本条件から除去し別タスクへ移した。有限モード模型($N_f\le2$、$\alpha\lambda^2\lesssim0.5$)は 22_ (2.3) の再帰有効域に完全に収まるため、この失効を原理的に検出できない。転進先は $\mathcal E(P)$ の**下界**、$M_0$ の $\Lambda$ 一様有界性、Q3 否定側の直接攻撃。
  > **【2026-09-09 訂正注記（親 G3、稿 39_ / w122 の指摘）】転進先の 2 番目「$M_0$ の $\Lambda$ 一様有界性」は
  > F13(a) と整合しない。** F13(a) は 14_ 定理9 の要求分母を導く際に $\Lambda\partial_\Lambda M_0\simeq\frac{2\alpha\Lambda^2}{\pi}$
  > を**入力として使っている**ので、$M_0$ が $\Lambda$ 一様有界であることはその入力と両立しない。
  > すなわちこの転進先は、閉鎖済みの F13 の前提を否定しない限り成立しない。**3 標的の最下位に格下げする。**
  > 転進先の 1 番目（$\mathcal E(P)$ の下界）は F13 で既に閉鎖済み（真だが Q3 に無力）。
  > 実質的に生きている転進先は 3 番目（Q3 否定側の直接攻撃 = B16）だけである。

## F9 — 「GHL 2014 型の汎関数積分（Feynman–Kac–Itô）で、対相互作用を Gauss 支配してフル PF の $\Lambda$ 一様評価を得る」(経路①の入口)
- 日付: 2026-09-09(19_、w101/Fable)
- 分類: 手法の失敗(障害を命題として同定)。**経路①そのものは生存**し、§6 の再定式化へ転進する。
- 前提(自前導出、19_ §2): 真空‐真空 FKI は $`\bigl(f\otimes\Omega,e^{-tH_\Lambda}g\otimes\Omega\bigr)=\int dx\,\bar f\,\mathbb E^x_W[g(B_t)e^{-\int V}e^{-\frac{e^2}2\sigma^2_\Lambda(B)}]`$、$`\sigma^2_\Lambda(B)=\int_0^t\!\!\int_0^t W^{\mu\nu}_\Lambda(B_s-B_r,s-r)dB^\mu_sdB^\nu_r`$、$W^{\mu\nu}_\Lambda(x,\tau)=\int_{|k|\le\Lambda}\frac{d^3k}{(2\pi)^32|k|}(\delta_{\mu\nu}-\hat k_\mu\hat k_\nu)e^{ikx}e^{-|k||\tau|}$。Coulomb ゲージで $`\nabla\!\cdot\!A_\Lambda=0`$ が作用素の恒等式ゆえ**伊藤補正は恒等的に 0**（Itô = Stratonovich）。$\frac{e^2}{2m}A_\Lambda^2$ は独立な項ではなく $\sigma^2_\Lambda$ の **Itô 対角**そのもの。
- 正確な障害: (命題A)$P(k)=\delta-\hat k\hat k$ は半正定値で $W_\Lambda$ は正定値核だから $\sigma^2_\Lambda\ge0$。横射影は符号を壊さない（発注時の見立ての訂正）。壊れるのは減算後である。(命題B)Itô 等長より $\mathbb E_B[\sigma^2_\Lambda]=\frac tm\mathop{\mathrm{tr}}W_\Lambda(0,0)=\frac{t\Lambda^2}{4\pi^2m}$ が**厳密**に成り立ち（$=\frac{e^2}{2m}\langle A^2\rangle t=\frac{\alpha t\Lambda^2}{2\pi m}$、決定論的）、これを引いた残差 $\sigma^2_{\Lambda,\rm off}$ は厳密に中心化されて両符号をとる。(命題C)その分散は $`\mathrm{Var}(\sigma^2_{\Lambda,\rm off})\simeq\frac{4t}{m^2}K_2(\Lambda)\simeq5.6\times10^{-3}\,t\Lambda^2/m`$ で**冪発散**する（$K_2=\int_0^t\mathbb E[\mathop{\mathrm{tr}}W_\Lambda(B_s-B_r,\tau)^2]d\tau\simeq1.40\times10^{-3}m\Lambda^2$、$\Lambda=8..4096$ の 10 段で局所冪が $2.066,2.047,2.034\to2$、相対補正 $\sim\Lambda^{-0.4}$）。ゆえに $\sigma^2_{\Lambda,\rm off}$ は $L^2$ 極限を持たず、GHL 2014 の図式「発散 = 対相互作用の**対角部** = 決定論的な対数定数 ⇒ それを引けば残りが収束し $\mathbb E[e^{(\text{残り})}]$ が $\Lambda$ 一様有限」は**第 1 段から偽**。定数（エネルギー）反項をどう選んでも $\Lambda$ 一様な $L^1$ 評価はこの図式から出ない。(命題D)原因は 2 点で、いずれも修復不能: ①結合が $ds$ でなく $dB$（Nelson は $\int\phi(B_s)ds$、PF は $\int A\cdot dB_s$）、②2 次モーメントでは反跳因子が $e^{-|k+k'|^2\tau/2m}$ の形でしか掛からないため**背中合わせ対 $k'\simeq-k$ が反跳抑制を免れる**（F6 命題3 の $`\|\beta\|^2_{HS}\propto\sqrt{\Lambda/m}`$、F7 命題D の $|k+q|\lesssim\sqrt{m\Lambda}$ と同一機構が汎関数積分側に現れたもの）。伊藤補正による冪の相殺は $`\nabla\!\cdot\!A=0`$ より原理的に起こらない。
- 収穫: (1)反跳の汎関数積分側の正体を確定 — Brown 平均 $\mathbb E[e^{ik(B_s-B_r)}]=e^{-k^2|s-r|/2m}$ が有効切断 $k_*(\tau)=\sqrt{2m/\tau}$ を課し、作用素側の分母 $k^2/2m$ に対応する。深紫外は $\tau\lesssim m/\Lambda^2$（$1/\Lambda$ ではない）に押し込められる。(2)1 次モーメントでは反跳が $\tau^{-2}\to m\tau^{-1}$ と 1 冪緩め、$`\int\!\!\int ds\,dr`$ 測度なら $K_1=\frac{m}{\pi^2}\ln\Lambda+O(1)$ と**対数**（反跳なしは線形）。2 次モーメントでは $\Lambda^3\to\Lambda^2$ と 1 冪しか落ちない（反跳なしは $K_2^{\rm dip}/\Lambda^3=1.75008\times10^{-4}$ が 8 桁一定）。(3)発散の台は $|s-r|\lesssim1/\Lambda$（主部 $\lesssim m/\Lambda^2$）で**二次変分チャンネル**にあり、吸収しうる唯一の反項は参照 Wiener 測度の拡散係数の変更 = 経路測度内部の**質量くりこみ**。GHL がまったく必要としない操作である。(4)$K_2/m^2\propto\Lambda^2/m$ ゆえ、物理質量固定で $m_\Lambda\downarrow0$ とすると FKI 密度の揺らぎは**悪化**する（数値: $m=1\to0.25$ で $K_2/m^2$ が $73\to327$）。
- 再挑戦条件/転進: (N1)Spohn 型の橋渡し $1/m_{\rm eff}(\Lambda)=\lim_{t\to\infty}\frac1{3t}\mathbb E_{\mu_{\Lambda,t}}[|B_t-B_0|^2]$（$d\mu_{\Lambda,t}\propto e^{-\frac{e^2}2\sigma^2_\Lambda}d\mathbb W^{(1/m)}$）をフル PF で確立する。**これが無いと以下は無意味**。(N2)$m_{\rm eff}^{\rm full}(\Lambda)\le m^{\rm dip}_{\rm eff}(\Lambda)=m(1+\frac{4\alpha}{3\pi}\lambda)$ を 2 つの Gibbs 経路測度の比較で示す（双極子側は $\sigma^2$ が $B$ の厳密な二次形式で Gauss、完全に解ける）。成立すれば $h$ の初の非摂動的上界で、Q3 の「線形超」を潰す。各経路では $\sigma^2_{\rm full}\le\sigma^2_{\rm dip}$ は偽なので測度の比較でしか示せない点が勝負どころ。(N3)$e^{ik(B_s-B_r)}\to e^{-k^2R(\tau)/6}$、$R(\tau)=\mathbb E_\mu|B_{s+\tau}-B_s|^2$ の Feynman 変分型自己無撞着閉包を数値で解き $\gamma$ を予言する（安い kill-check、1 セッション規模）。
- 記録: `19_汎関数積分での対相互作用のGauss支配_経路1.md`(self-audited、留保 R1: FKI 表示は Trotter+Gauss 積分の形式的導出で Hiroshima の厳密表示と未照合、R2: 分散は直接 Wick 縮約のみで $e^{ik(B_s-B_r)}$ に当たる縮約が未評価 — **独立監査の 2 標的**)、(研究ノート: `50_fki_pair_kernel.py`) と `_output.txt`。

## F10 — 「R5′: 予算消費形 (3.2) を殻双一次形式から Cauchy–Schwarz 抜きで直接示し、$f(\Lambda)$ の問題を迂回する」
- 日付: 2026-09-09(20_、w103、Fable)
- 分類: 手法の**部分的成功 + 標的の一部の閉鎖**(1光子チャネルは設計できた。対チャネルは原理的に閉鎖)
- 正確な障害:
  (命題1)(3.2) は $`h\,\kappa_{\rm flow}\le(1-\delta)\frac{3m}{2}`$ と同値。$h$ は非有界なので、$\kappa_{\rm flow}$ の上界に
  $1/h$ 因子が現れない限り証明不能。かつ右辺 $\frac{3m}{2}-R=\frac{3m^2}{2m_{\rm eff}}$ の**下界**は $m_{\rm eff}$ の上界と同値で
  Q3 そのもの(循環)。$R_\mu$ は Rayleigh 商の**上限**なので試行状態からは上界しか出ない。
  ⟹ 点ごとの双一次形式間の不等式による証明は不可能。Gronwall 型かスケール帰納法でなければならない。
  (命題2)17_ 命題4 の Jensen 下界 $\Lambda\mathcal T^{\rm main}\ge\kappa^{1\rm loop}\to\frac{4\alpha m}{\pi}\gt0$ は**無条件・非摂動**
  (17_ 補題1 の厳密1次モーメント $`\int\epsilon\,\pi_k(d\epsilon)=k^2/2m`$ と凸性のみ)。ゆえに $h\to\infty$ なら
  $\Lambda\mathcal R=-\Lambda\mathcal T^{\rm main}(1-O(\frac1{\alpha h}))$ という**主要項そのものの相殺**が要求される。
  $\mathcal T^{\rm main}$ と $\mathcal R$ を別々に評価する手法(F5 の CS、F5 の補題8、F8 のモーメント法、17_ (3.4))は
  この相殺を原理的に見られない。**3つの独立な失敗の統一的原因**。
  (命題4)$1/h$ 抑制の機構は「殻光子の反跳エネルギーが走る質量 $m_*=hm$ で決まる」ことに依存するが、
  13_ §4.1 より背中合わせ2光子配位は $q=|k_1+k_2|$ が小さく反跳が相殺するため励起エネルギー $\simeq2\Lambda$ が
  **質量に依存しない**。ゆえに対チャネルには $1/h$ が出ない。
  (命題4.1)対チャネルを $1/h^p$ で抑えて救うには $p\ge\frac{1-g}{2g}$($g=\gamma_\infty\ge\frac{8\alpha}{3\pi}$)が必要で、
  $\alpha=1/137$ で $p\ge80.2$、$\alpha\to0$ で発散。$h$ が対数($g\to0$)ならさらに絶望的($\log$ の任意の冪は
  $\sqrt\lambda$ を殺せない)。**有効質量の任意の固定冪による頂点抑制では対チャネルを救えない。**
- 収穫(部分的成功):
  (命題3)RG 不変量は $\kappa_{\rm flow}$ ではなく $\gamma=\frac{d\ln m_{\rm eff}}{d\ln\Lambda}$。1光子チャネルに限れば
  $\gamma_{1\gamma}=\frac{8\alpha}{3\pi}\frac{\lambda_*/2}{1+\lambda_*/2}$($\lambda_*=\Lambda/m_{\rm eff}$)で、(3.2) は
  $\delta=1-\frac{8\alpha}{3\pi}$ で成立する。**$\delta$ は $\lambda$ 非依存、$\alpha\to0$ で $\delta\to1$、Landau スケールは戻らない**
  (発注文の分岐点への回答)。1ループ係数が質量非依存(乗法的)であることが置き換え $m\to m_*$ を許す全内容。
  得られる法則 $h\simeq\lambda^{8\alpha/3\pi}$ は HS の予想 (1.23) と一致し、$\kappa_{\rm flow}$ 一定の Landau 発散
  ($\lambda\le e^{3\pi/8\alpha}$、F5 の帰結1)との分岐点が「共変化するか否か」の一点に絞られた。
- 再挑戦条件: 補題 R5′-3(**最優先**)= 殻の背中合わせ2光子セクターの寄与が $\sqrt{m_*\Lambda}$ / $\sqrt{m\Lambda}$ /
  $f$ が $\lambda_*$ で減衰、のいずれで走るかの決定。これが E05 のオッズを動かす唯一の量(20_ §6)。
  次いで補題 R5′-1(殻1枚の Feshbach 段が質量 $m_*$・電荷 $e$ の PF 模型を再生する形式不変性。残差 $O(\alpha^2d\ell)$)、
  補題 R5′-2(切断がゲージ不変性を破る下での電荷の非繰り込み)。
  なお今後 $\kappa_{\rm flow}\le\Lambda\mathcal T^{\rm main}+|\Lambda\mathcal R|$ の形の評価を書いてはならない(20_ 系2.2)。
- 記録: `20_R5dash予算消費形の直接証明.md`(命題1–5、self-audited)、
  (研究ノート: `60_R5dash_selfconsistent_flow.py`) と `_output.txt`、(研究ノート: `2026-09-09_w103_R5dash.md`)。

## F11 — 「IBC(内部境界条件)法をフル PF に拡張して切断なしのハミルトニアンを直接定義する」(経路③、REGISTRY B6)
- 日付: 2026-09-09(21_、w104。文献確認は w104-lit)
- 分類: 手法の失敗(障害を命題として同定)
- 正確な障害: 1 光子ドレッシング振幅 $g=v/D$ について **IBC 可容条件** (IBC-1) $g\in L^2$(紫外側) かつ
  (IBC-2) $\langle v,g\rangle=\int|v|^2/D$ の発散部が**電子運動量に依らない c 数**、を定式化した(命題1)。
  (命題5、主障害 = D3)フル PF の 1 光子部は (IBC-1) を満たすが (IBC-2) を破る: 形状因子
  $v_\lambda(k)=-\frac em\frac{\epsilon_\lambda(k)\cdot\pi}{(2\pi)^{3/2}\sqrt{2|k|}}$ が電子速度作用素 $\pi/m$ に線形なため、
  引き算すべき発散が $\frac{\pi^2}{2m}\cdot\frac{8\alpha}{3\pi}\ln\lambda$ という**作用素**(質量くりこみ)になる。
  IBC は加法的定数の除去機構である(w104-lit が Lampart arXiv:1909.02430 で確認: Bogoliubov–Fröhlich の
  対数発散はエネルギー定数の引き算のみで吸収され、質量くりこみを要しない。Lampart–Schmidt / LSTT の Nelson 型 IBC は
  「形状因子が粒子運動量を含まない c 数」を必須仮定として使う)。
  (命題3、独立な障害 = D1)$A^2$ 由来の 2 光子成分は背中合わせ対(全運動量が小さく電子への反跳が働かない配位)で
  $`\|g_2\|^2\propto\alpha^2\sqrt\lambda`$ が発散し、(IBC-1) が対セクターで破れる — F6 命題3 と**同一の積分**。
  (命題2、kill-check)双極子 PF は (IBC-1)(IBC-2) をともに破る。ただし (IBC-1) の破れは双極子近似が反跳 $k^2/2m$ を
  分母から落としたアーティファクトでフル PF に遺伝しない。転写できるのは (IBC-2) の破れ($\propto p^2\Lambda$)。
  (命題6、最強形)境界条件の係数を作用素に許す「$\pi$ 依存 IBC」を認めても、有限部分の引き算が裸質量の流れそのものになり、
  構成の存在は **Q3 に帰着する**(循環)。IBC は Q3 に新情報を与えない。
- 障害でなかったもの: **横性(D2)は IBC を壊さない**(命題4。親の見立ての訂正)。$\delta^{ij}-\hat k^i\hat k^j$ は 0 次同次なので
  特異部分の冪は方向に依らず、方向依存は固定されたテンソル値角度プロファイルとして現れるだけで方向極限は存在する。
  Bogoliubov–Fröhlich の IBC が既に複合特異性 $c_{-1}|x-y|^{-1}+c_0\log|x-y|$ を扱っている事実がこれを補強する。
- F6 との関係(命題7): 別の壁ではなく**同一の根**。「PF の紫外発散は c 数ではなく作用素(電子速度 $\pi/m$)に張り付いている」。
  F6 命題4 はこれを「残差の速度次数が上がる」形で、本稿 命題5 は「境界電荷と有限部分が $\pi$ 依存になる」形で見ている。
  対セクターでは共有がさらに直接的で、F6 命題3 = 本稿 命題3 = HS の 2 ループ $b_2\propto\sqrt\Lambda$ が同一の積分。
- 数値: (研究ノート: `70_ibc_admissibility.py`)(新規)。フル PF の $`\|g\|^2`$ 紫外増分は 10 倍ごとに
  $1.5\times10^{-2}\to2.7\times10^{-8}$ で収束、双極子は $\ln10=2.30259$ 一定(対数発散)。
  $\langle v,g\rangle$ はフルで $2m\ln(1+\lambda/2)$ と 6 桁一致(E05-F1 再現)、双極子で $\Lambda$ に厳密比例(G3-1 再現)。
  対セクターの局所勾配 $\gamma=0.680,0.577,0.531,0.498,0.488$($\Lambda\le10^7$)で $\to\frac12$。
  係数は $0.30$ で F6 命題3 の $2/\pi$ と約 2 倍差(対称化因子の規約差。16_ 留保9 が既出)。本稿は指数のみ主張。
- 再挑戦条件/転進: (i) 質量くりこみを伴う IBC 構成の一般論が新たに作られた場合(現時点で前例なし)。
  (ii) 対セクターの $\sqrt\lambda$ を非摂動的に押さえる仕事ができた場合(これは経路を問わず価値がある)。
  **手法選別の基準**(本ラウンドの副産物): 今後 PF の切断除去に用いる手法は「紫外発散が c 数でなく作用素に
  張り付いている」ことを正面から扱えるものに限る。「ドレッシング + 定数の引き算」型は Gross・IBC を含め同じ場所で止まる。
- 格付け: self-audited(敵対的セルフレビュー 10 項目を 21_ §9 に記録)。独立監査未実施。
  留保: 命題1 の必要性は未証明(既知構成からの抽出)。命題3 は $O(\alpha^2)$ 摂動論(E05-L4 により $\lambda\gtrsim\alpha^{-4}$ で無効)。
  命題6 の帰着は片方向のみ。

## F12 — 「再帰的 Chebyshev（17_ §7）で殻内2光子相関 $f(\Lambda)$ の $\lambda$ 減衰を示す」(経路⑥)
- 日付: 2026-09-09(22_、w105/Opus)
- 分類: 手法の失敗(障害を4つの命題として同定)。**F8 の再挑戦条件の消尽**。
- 正確な障害:
  (a) **分解能障害(命題1)**。pull-through は厳密には $`X\,a_j^*(k')=a_j^*(k')(X_{k+k'}+\omega')+\frac em g_j(k')\cdot(k+v)`$(補題A、$P$ 一般で導出)であり、非斉次項 $Z_j$ は横波性で消えない($g_j(k')\perp k'$ であって $\perp k$ ではない)。$`\Xi:=e\,k\cdot a^*(g)\psi_0`$ に対し $(X-\tilde X)\Xi$ は $\psi_0$ 方向の**コヒーレント**な残差で、$`\|(X-\tilde X)\Xi\|/\|\Xi\|=\Delta_{\min}=\frac{|k|}{m}\sqrt{M_0/3}`$。$|k|\asymp\Lambda$、$\theta=\Lambda\lambda^s$ に対し $\Delta_{\min}/\theta=\lambda^{1-s}\sqrt{\alpha/3\pi}$ で、$s\lt1$ の全てで発散する。逃れられる $s=1$($\theta\asymp\mu_k$)では Chebyshev が閾値を見分けない(17_ 命題5(d))。再帰が閾値を分解できるのは $`\lambda\ll3.07\,C/\sqrt\alpha`$ のみで、Landau スケール $\alpha^{-1}$ どころか $\alpha^{-1/2}$ の手前で失効する。
  (b) **横波性は勝つが救わない(命題2、肯定的結果)**。Chebyshev の利得が消える背中合わせ窓の重みは、横波性 $\sin^2\angle$ と窓の測度を厳密に数えて $\nu(S_1)\simeq4.74\bigl(\frac{C-1}{\lambda}\bigr)^{5/2}$(幾何定数 $0.148$ が $C=2,4$ で一致、実験 80)。必要な $\lambda^{-1}$ より 1.5 乗速く、17_ §7 の「背中合わせは横波性で消える」という見立ては**正しい**。しかしこれは窓の中の話であり、(c) に埋もれる。
  (c) **再帰は $\alpha$ 展開であって $\lambda$ 展開でない(命題3)**。窓の外の一般方向では、再帰先ファイバー $q\asymp\Lambda$ の低エネルギー割合を Chebyshev の $\frac{4M_0}{3q^2}\asymp\alpha$ 以上に絞る手段が無い($X_q\ge0$ しか無く、補題8 $\mathcal E(P)\le\min(P^2/2m,|P|)$ が下界を禁じる — 14_ §4.2 の壁の再来)。実験 80 で $I(S_2)/\alpha=0.244(C{=}1),0.320(C{=}2),0.322(C{=}4)$ が 2 つの $\alpha$ で 4 桁一致し、$\lambda$ 当てはめ指数は $-0.004\sim-0.034$(実質 0)。1 段の上界は $f\le\frac{4\alpha}{3\pi}c(C)\alpha\simeq0.14\alpha^2$ で $\lambda$ 一様、$n$ 段で $O(\alpha^{n+1})$。定理9 の $f\lesssim\frac{1}{\alpha\lambda h}$ はどの有限段でも $\lambda\gtrsim\alpha^{-(n+2)}$ で破れる。**この数値は $Z_j$ と $\langle N+1\rangle$ 因子を無視した最も楽観的な版の評価**なので、a fortiori。
  (d) **候補 A は $\lambda$ 盲目(命題4)**。$`\|1_{[0,\theta)}(X)(k\cdot P_f)P^S_{\ge1}\psi_0\|^2`$ に必要な削減比は $\frac{1}{\alpha^2\lambda h}$ で、$\lambda^{-1}$ は**射影が供給しなければならない**。射影を含まない $`\|P_fP^S_{\ge1}\psi_0\|`$ 型のモーメント上界(大偏差評価を含む)は、いくら鋭くてもこれを供給できない。加えて $\langle(n\cdot P_f)^2\rangle\le\langle H_f^2\rangle$ は厳密だが($P_f,H_f$ 可換)、$H_f\psi_0=E\psi_0-\frac{v^2}{2m}\psi_0$ より $\langle H_f^2\rangle$ の制御は $v$ の 4 次モーメントに帰着し、$M_0$ より難しい。
  (e) **第 4 の障害**。(1.4) の対角評価は厳密には $\langle N+1\rangle$ 因子を伴い、$\langle N\rangle\lesssim\alpha^2\lambda^2$(17_ §6)しか無いので再帰 1 段ごとに $\lambda^2$ を失いうる。
- 帰結: **F8 の再挑戦条件は尽きた**。「17_ §7 の再帰的 Chebyshev」は (a)(c) で閉鎖、「$(P_f,H_f)$ の大偏差評価」は (d) で閉鎖。「対セクター限定の分散**下界**」は $f$ の減衰の道具ではなく Q3 **否定側**($\kappa_{\rm flow}$ の下界)の道具なので、F8 の再挑戦条件から除去し別タスクに移す。モーメント法(2次モーメント・光子数・再帰的 Chebyshev)による $f(\Lambda)$ の $\lambda$ 減衰の証明は、機構全体として閉じる。
- 副産物: 有限モード模型($\lambda\le6.5$)は (2.3) の再帰有効域に完全に収まるので、この失効を原理的に検出できない(17_ §5 の「無力」の独立な再導出)。
- 再挑戦条件: なし(この機構としては確定)。転進先 (i) $\mathcal E(P)$ の**下界** は **2026-09-09 に閉鎖(26_ / w109、F13 を見よ)**: 下界は真だが $\mathcal E\le|P|$(補題8)の天井のため定理9 の要求 $\frac2\pi\alpha\lambda\Lambda$ に $\alpha\lambda$ 倍届かず、命題3 も覆らない。残る転進先は (ii) $M_0$ の $\Lambda$ 一様有界性(あれば 22_ §2 の二者択一で Q3 が肯定側に決まる)、(iii) Q3 否定側の直接攻撃(対セクター分散下界の再分類先)の 2 つ。
- 出典: `22_再帰的Chebyshevのkillcheck.md`(self-audited、§7 に敵対的セルフレビュー)、(研究ノート: `80_recursive_chebyshev_window.py`)。

## F13 — 「R7: 一般方向ファイバーでの $\mathcal E(P)$ の下界で pull-through の分母を稼ぎ、$f(\Lambda)$ を制御する」(14_ §7 の R7、F12 の転進先(i))
- 日付: 2026-09-09(26_、w109/Opus)
- 分類: **標的の失格**(下界そのものは真かつ部分的に証明できたが、Q3 に対して原理的に無力であることが確定)。
  F12 の転進先(i) の閉鎖、および 14_ §7 の再挑戦条件 R7 の閉鎖。
- 正確な障害:
  (a) **天井(定理R7-cap、本項の要)**。14_ 定理9 が要求する一様エネルギー分母は $\theta_{\rm req}\simeq\frac{2\alpha\Lambda^2}{\pi m}=\frac2\pi\alpha\lambda\Lambda$($\kappa_{\rm flow}\lesssim m$ と $\Lambda\partial_\Lambda M_0\simeq\frac{2\alpha\Lambda^2}\pi$ から)。一方、補題8 $\mathcal E(k)\le|k|$ は**いかなる下界のもとでも** $\omega(k)+\mathcal E(k)\le2\Lambda$ を課す。比は $\theta_{\rm req}/2\Lambda\ge\frac{\alpha\lambda}\pi\to\infty$。$c\gt1$ は補題8 に反するので改善の余地は無い。**線形下界の最大収量は係数 $(1+c)\le2$、冪はゼロ。** $M_0$ を Lieb–Loss の $\alpha^{2/7}\Lambda^{12/7}$ に替えても比は $\asymp\frac12\alpha^{2/7}\lambda^{5/7}\to\infty$(14_ §4.4 と整合)。
  (b) **構造的な理由**。$\mathcal E(P)$ は**ファイバーのスペクトルの底**、$f(\Lambda)$ は**$\psi_0$ の殻重みが底からどう分布するか**。下界は底しか動かさない。$f=1$(最悪ケース)は任意の $c\le1$ の下界と両立する(背中合わせ対は $q\approx0$、$\mathcal E(q)\approx0$、光子エネルギー $2\Lambda$)ので、**$\mathcal E$ の下界は $f$ の上界を一切与えない**。
  (c) **22_ 命題3 は覆らない(命題R7-1)**。22_ (1.4) の再帰で下界が効くのは $f_q(\theta')=0$ となる消滅域 $`\{\omega'+c|k+k'|\ge C\Lambda\}`$ だけだが、この条件は $(k',k,\Lambda)$ について 1 次同次で、$\nu$ 測度は $(C,c)$ のみに依存し **$\lambda$ に依存しない**。ゆえに再帰 1 段の利得は $c'(C,c)\alpha$ のまま。最良の $c=1$ でも生存域は焦点 $`\{0,-k\}`$・長軸 $C\Lambda$ の回転楕円体で、球に対する体積比は $\frac{C(C^2-1)}8$($C=2$ で $0.75$ — 殺せるのは 25% 程度)。$C\le c\le1$ なら消滅するが、それは $X\ge\mathcal E(k)\ge c\Lambda$ から再帰なしで従う自明な帰結で、要求される $C\asymp\alpha\lambda\to\infty$ に届かない。22_ 命題1(分解能 $\Delta_{\min}$ は $\mathcal E$ を含まない)・命題4・§5(ii)($\langle N\rangle\lesssim\alpha^2\lambda^2$ は $(1+c)^{-2}\ge\frac14$ 倍にしかならない)も R7 のもとで生き残る。
  (d) **証明できる窓が役に立つ窓と同じ**。$H_f\ge|P_f|$・$\epsilon$-Young・$e^2A^2\le\frac{8\alpha\Lambda}\pi H_f+\frac{2\alpha\Lambda^2}\pi$ から $\mathcal E(P)\ge c(\alpha,\lambda)|P|$($|P|\ge\Lambda$)、$c=1-\sqrt{10\alpha/\pi}-\frac{\alpha\lambda}{2\pi}+O(\alpha\lambda^{-1})$(定理R7-a)。窓は $\alpha\lambda\lt2\pi(1-\sqrt{10\alpha/\pi})$(数値: $\alpha=1/137$ で $\lambda_*=737$、$\alpha\lambda_*=5.38$)。一方 R7 が定理9 を満たしうる窓は $\alpha\lambda\lt\frac{3\pi(1+c)}4\simeq3.5\sim4.7$。**両者はほぼ同一で、どちらも摂動論が生きている自明な領域**。一致は偶然ではなく、どちらも $e^2A^2/2m$ と $H_f$ の比 $\asymp\alpha\lambda$ が支配するため($\epsilon$-Young の破綻位置は E05-L5 の双極子の終端 $\alpha\lambda=3\pi/4$ と同スケール)。
  (e) **窓の外は $E(P)$ と同難度(定理R7-b)**。$\mathcal E(P)\ge c|P|$ はドリフト関数 $`W(\epsilon)=\sup\{|\langle v\rangle|/m:\langle H(0)-E(0)\rangle\le\epsilon\}`$ の鋭い上界 $W(\epsilon)\le\sqrt{2\epsilon/m}-c$ と**同値**。真値は $\frac{\langle v\rangle}m=\frac{|P|}{2m}-1+\frac m{2|P|}$ なので相対余裕は $\frac{2(1-c)}\lambda\to0$ で、どんな $c\gt0$ でも $O(1/\lambda)$ の相対精度を要する。Cauchy–Schwarz で代用すると自己エネルギー $E(0)\sim\alpha^{1/2}\Lambda^{3/2}$(E05-L4)が混入して $\mathcal E\ge-E(0)$ となり無情報(14_ 命題6「CS は $\alpha$ の冪をひとつ失う」の $\mathcal E$ 版)。
- 肯定的な副産物(捨てないこと):
  - **線形下界は真である**。有限モード ED(正四面体 4 方向・準対心対なし・2 殻・偏極 2・$N\le4$)で $\mathcal E(P)\simeq|P|-\frac m2$(傾き $0.977\sim1.023$、切片 $-0.33\sim-0.48$、補題8 の上界を $10^{-15}$ で飽和)。**$c\to1$ が最良で、$c\gt1$ は不可能。**
  - **14_ の閉鎖宣言の強化**。14_ §7 は「$\mathcal E(k)\gtrsim k^2/m$ 型の**二次**下界は存在しない」として二次だけを閉じていた。定理R7-cap は「補題8 と両立する**任意の**下界が要求に届かない」ことを示すので、**エネルギー分母の機構というカテゴリ全体が閉じる**。$\kappa_{\rm flow}$ の分母は上下から $[\Lambda,2\Lambda]$ に閉じ込められ、使い切られた。残る資源は**重みの側だけ**である。
  - 摂動窓($\alpha\lambda\lesssim3.5$)では $\kappa_{\rm flow}\le\frac{2\alpha\Lambda}{\pi(1+c)}$ が無条件に成り立ち $R\lt\frac{3m}2$ が従う(既知の摂動的事実の厳密版であり、新情報ではない)。
- 14_ 対 w105 の裁定: **14_ §7 の評価「定数倍の余裕が生まれる(冪は改善しない)。優先度は低い」が正しい**。w105(22_ §6)の「$\mathcal E$ の下界があれば命題3 は覆る／これが真の分水嶺」は誤り(上記 (c))。本項は 14_ の評価を「優先度ゼロ(原理的に無力)」に更新する。
- 再挑戦条件: **なし**。$\mathcal E$ の下界を経由するいかなる形(線形・対数補正つき・方向依存)も (a) の天井に阻まれる。分母の側の資源は尽きた。転進先は (i) $M_0$ の $\Lambda$ 一様有界性、(ii) 殻重みの角度・偏極構造($f$ そのもの。ただし F8・F12 でモーメント法は尽きている)、(iii) Q3 否定側の直接攻撃。
- 出典: `26_励起エネルギーの下界_R7.md`(self-audited、§7 に敵対的セルフレビュー 15 項)、
  (研究ノート: `62_energy_lower_bound_ED.py`)(+`_output.txt`、`_result.json`、conclusion=`PASS_LINEAR`)、
  (研究ノート: `2026-09-09_w109_R7.md`)。

## F14 — 「N3: 反跳の自己無撞着 Gauss 閉包（Feynman 変分型）で $\gamma=\frac{d\ln h}{d\ln\lambda}$ を予言する」(19_ §6.2 N3、B11 の安い kill-check)
- 日付: 2026-09-09(29_、w112/Opus)
- 分類: 手法の失敗（機構を命題として同定）。**B11（経路測度の拡散係数）そのものは生存**し、N1 側（29_ 命題1〜4）へ資源を移す。
- 前提（自前導出、29_ §3.1）: $\mathbb E_\mu[e^{ik\cdot(B_{s+\tau}-B_s)}]\to e^{-k^2R(\tau)/6}$、$R(\tau)=\mathbb E_\mu|B_{s+\tau}-B_s|^2$ と横射影の角度平均 $\frac23\delta^{\mu\nu}$ により、有効核は $`w(\tau)=\frac{1}{6\pi^2}\int_0^\Lambda k\,e^{-k\tau-k^2R(\tau)/6}dk`$、速度スペクトル $S_v(\omega)=[m+e^2\hat w(\omega)]^{-1}$、$R(\tau)=\frac{3\tau}{\pi}\int_0^\infty\frac{2(1-\cos y)}{y^2}\frac{dy}{m+e^2\hat w(y/\tau)}$、$h=1+\frac{e^2\hat w(0)}{m}$ で閉じる。
- **閉包は正しく作れている**（この 2 本は捨てないこと）: (A) $R\equiv0$（反跳なし）で $h=1+\frac{4\alpha}{3\pi}\lambda$（双極子の厳密解）、(B) $R=3\tau/m$（自由 Brown、非自己無撞着）で $h=1+\frac{8\alpha}{3\pi}\ln(1+\frac\lambda2)$（E05-F1）を、**いずれも係数まで解析的に厳密再現**する。数値実装もこの 2 本を相対差 $\le5.6\times10^{-4}$（求積誤差のみ）で通す。自己無撞着解は $\gamma\to\frac{8\alpha}{3\pi}$（$\gamma/g$ が $\alpha=0.03,0.1,0.3,1.0$ で $0.977,0.923,0.793,0.523$、$\lambda\ge10^4$ で 4 桁一定、$\alpha=1$ でも $\gamma=0.44\lt1$ で双極子上界と整合）。解析的にも $w(\tau)\simeq\frac{M(\tau)}{6\pi^2\tau}$ と $d\ln(1/\tau)=2d\ln k_*$ から $\frac{dh}{d\ln k}=gh$、$h\simeq(\lambda/2)^g$、$g=\frac{8\alpha}{3\pi}$。
- 正確な障害: **閉包の $O(\alpha^2)$ 項は $\frac12\bigl(\frac{8}{3\pi}\bigr)^2\alpha^2\ln^2\lambda$ であり、公理 E05-L1 の $c_0\alpha^2\sqrt\lambda$（HS 2005 Thm 4.1、$c_0\simeq1/2\pi^2$、符号確定で相殺不能）を再現しない。** $\sqrt\lambda\gg\ln^2\lambda$ ゆえ、任意の固定 $\alpha$ について $\lambda$ を十分大きくすれば閉包は必ず外れる（数値: $[h_{sc}-h_{1loop}]/\alpha^2$ は $\lambda=10^5,10^6,10^7$ で $43.1,70.0,106.1$ と $\frac12(\frac{8}{3\pi})^2\ln^2\frac\lambda2=42.2,62.0,85.7$ に沿い、$\sqrt\lambda=316,1000,3162$ には乗らない）。原因は実装ではなく構造である: 置き換え $e^{ik(B_s-B_r)}\to e^{-k^2R/6}$ は反跳を光子ごとの**1 体因子**に潰すが、2 次モーメントでは反跳が総運動量 $|k+k'|$ にしか掛からず**背中合わせ対 $k'\simeq-k$ が抑制を免れる**（19_ §3.3、F9 命題D、E05-F7）。この 2 光子相関は $B$ の二次形式（1 体）有効作用には原理的に入らない。$\sqrt\lambda$ はまさにそこから来る。
- 一般化された閉鎖（**このカテゴリ全体が閉じる**）: 反跳を 1 体（Gauss／平均場／変分二次形式）で繰り込む閉包は、どう作っても $\gamma=O(\alpha)$ を出し、双極子の線形上界 $h\le1+\frac{4\alpha}{3\pi}\lambda$ を破らない（$R\ge0$ より $w\le w|_{R=0}$）。F5 が潰そうとした形 $h\lesssim\lambda^{c\alpha}$ は**まさに 1 体閉包の答**であり、F5 が $c_0\alpha^2\sqrt\lambda$ で閉じたのと同じ理由で N3 も閉じる。Q3 の帰趨は 1 体チャンネルには無く、背中合わせ対チャンネルに全部載っている（F5・F6 命題3・F7 命題D・F8・F9 に続く 6 度目の独立な確認）。
- 収穫（捨てないこと）: (1) **走る質量の向きの確定**。$\hat w(\omega)$ は $\tau\lesssim1/\omega$（高 $k$ モード）から作られるので、$m(\omega)=m+e^2\hat w(\omega)$ は低周波（長時間）で最重、$\omega\sim\Lambda^2/m$（$\tau\sim m/\Lambda^2$）で裸に戻る。すなわち**短時間 $\tau\lesssim m/\Lambda^2$ では $R(\tau)\simeq3\tau/m$（裸）、長時間で $3\tau/m_{\rm eff}$**（数値: $M(\tau)/m=1.0016\to9.379$、$h_{sc}=9.364$）。19_ N3 と発注文が想定した「短時間で $m_{\rm eff}$」は**向きが逆**であり、以後この訂正を使う。(2) 閉包は既知の 2 極限（双極子・1 ループ）を係数まで再現するので、**将来の経路側の近似の検算台として再利用できる**（(研究ノート: `52_selfconsistent_R_closure.py`)）。(3) 閉包は正の寄与（$\sqrt\lambda$）を落とすので、その $\gamma$ は真の増大則の**下限側の目安**であり、劣線形（$\gamma=0$）を支持する材料にはならない。
- Q3 のオッズ: **更新しない**（劣線形 18% / 弱い冪 62% / 線形以上 20%）。理由は `EVIDENCE.md` の該当節。
- 再挑戦条件/転進: 1 体閉包の改良は**禁止**（上記の一般化された閉鎖）。背中合わせ対を 2 体自由度として明示的に持つ閉包（例: 対の相対運動量 $q=k+k'$ を独立変数にした 2 体有効作用）なら別機構だが、F6 命題3・F7 命題D が同じ対セクターで既に閉じている点に注意。転進先は 29_ §6.2 の (L2) 尖度の $t$ 一様有界性 $\varkappa_\Lambda\lt\infty$（Q3 肯定側の鍵）、(L1) 無限体積 Gibbs 測度の存在と混合性、(L3) $D^-_\Lambda$ の上界。
- 記録: `29_Gibbs経路測度の拡散係数_B11.md`(self-audited、§3 と §5、留保: (G5) 19_ の FKI 表示が Hiroshima の厳密表示と未照合、S8 閉包の変分的正当化は無い、S10 本項は E05-L1 を公理として受け入れる限りの不一致であって閉包の誤りの証明ではない)、(研究ノート: `52_selfconsistent_R_closure.py`) と `_output.txt`・`_result.json`(conclusion=`INCONCLUSIVE`)、(研究ノート: `2026-09-09_w112_B11.md`)。

## F15 — 「$\langle N_S\rangle$ の $\lambda$ 冪の改良を、エネルギー上界・反跳分母・和則のいずれかから取る」(U2 の 3 系統)
- 日付: 2026-09-09(33_、w116/Opus)
- 分類: **手法の失敗（3 系統の閉鎖）＋ 標的の再定式化**。無条件の改良は得られなかったが、
  1 体量 $\langle N_S\rangle$ に関する (U2) が (U1) の十分条件下で解けることを示したので、
  **未証明項目としての旧 (U2) は独立性を失う**。ただし稿 31_ の再編成により律速は対量
  $\langle N_S(N_S-1)\rangle$（新項目 (U2′)）に移り、**未証明項目の総数は減らない（6 → 7）**（audit3133 §C8）。
- 正確な障害:
  (a) **エネルギー系統**。pull-through で $`\langle N_S\rangle=\frac{e^2}{m^2}\sum_\lambda\int_Sc_k^2\|R_k(\epsilon_\lambda\cdot\pi)\psi_0\|^2`$
  と厳密に書き直すと $E$ は一旦消えるが、$M_\perp$ の**無条件**上界が $`M_\perp\le\|\pi\psi_0\|^2/2\omega_k\le mE/\omega_k`$
  しかないため $E\le\frac{\alpha m\lambda^2}{2\pi}$ が戻る（結果は 17_ §6 / F8(b) の $\alpha^2\lambda^2$ と同一）。
  さらに悪いことに、$\varsigma\langle N_S\rangle$（$\mathcal E_2$ 由来）は**殻幅について不変**なので殻の取り方でも逃げられない。
  E05-L4 の $C_2\alpha^{2/7}\Lambda^{12/7}$ を代入しても $\varsigma\langle N_S\rangle\sim\alpha^{4/7}\lambda^{5/14}$ で発散する。
  **$E$ の上界が $\alpha m\lambda^2$ 型である限り、壁 $\lambda\lesssim\alpha^{-4}$ はどの経路でも動かない。**
  (b) **反跳分母系統**。$`\|R_k\|\le(\mathcal E(k)+\omega_k)^{-1}`$ に対し補題8 $\mathcal E(P)\le\min(P^2/2m,|P|)$ が
  $|k|=\Lambda\gg m$ で $`\|R_k\|\ge\frac1{2\omega_k}`$ を強制する。$`\|R_k\|`$ を $m/\Lambda^2$ 型に改善することは原理的に不可能で、
  E05-F9 の $\mathcal E(P)\ge c|P|$ を入れても $(1+c)\le2$ の**係数だけ**、冪はゼロ。F13（エネルギー分母の機構の
  カテゴリごとの閉鎖）の $\langle N_S\rangle$ 版であり、独立な 7 度目の確認。
  (c) **和則系統**。$H_\sigma=H+\sigma H_f|_S$ の Feynman–Hellmann は $\Theta_S=\partial_\sigma E|_0=\langle H_f|_S\rangle$ を
  与えるだけで、(i) $\langle N_S\rangle\le\Theta_S/\Lambda'$ は初等上界そのもの、(ii) $E(\sigma)$ の凹性から出るのは
  $\Theta_S\le E(0)-E(-1)\le E$（$H_{-1}=\frac{\pi^2}{2m}+H_f|_{S^c}\ge0$）にとどまり $E$ を超えない、
  (iii) 殻上で結合定数をスケールする族は $\langle A_S\cdot\pi\rangle$ 型を与え $\langle N_S\rangle$ にならない。
  $\partial_\Lambda E$ の流れは 14_/F5 で既に閉鎖済み。
- 肯定的な副産物（捨てないこと）:
  - **(U1) $\Rightarrow$ (U2)**。$`\|R_k\phi\|^2\le\|R_k\|\langle\phi,R_k\phi\rangle`$（$`\|R_k\|`$ を 2 乗せず 1 乗しか使わない混合評価）で
    $`\langle N_S\rangle\le\frac{2e^2}{m^2}\int_Sc_k^2\|R_k\|M_\perp\,d^3k`$。(U1)（$M_\perp\le C_M\alpha m$ が $\Lambda$ 一様）の下で
    $\langle N_S\rangle\le\frac{2C_M}{\pi}\alpha^2\lambda\delta$ となり、初等上界より $\alpha$ を 1 つ稼ぎ、**殻幅 $\delta$ に比例**する。
  - **殻幅の scaling（33_ 定理2。audit3133 で独立再現）**: $\varsigma\propto\delta^{-1}$、$\langle N_S\rangle\propto\delta$、
    さらに $\langle N_S(N_S-1)\rangle$ と $A_{\rm res}/D_{\rm free}$ も $\delta\gtrsim\lambda^{-1/2}$ で $\delta$ に比例。ゆえに
    $\varsigma\langle N_S\rangle$（$\mathcal E_2$ 由来）は殻幅不変、律速項は殻幅に比例する。
    **殻を細くする操作は分母評価に対して純益**（稿 30_ が $\delta$ を固定していただけで、逆向きの主張をしていたわけではない）。
  - **(L2) の $\lambda$ 一様化（33_ 定理3）は現状 FAIL**（audit3133、2026-09-09）。旧記載は $\mathcal E_4$ の律速項を
    $\varsigma\langle N_S\rangle^2$ と取っていたが、稿 31_ 命題U4-1〜U4-3 によりその上界は偽で、
    再編成後の律速項は $\varsigma$ の利得を持たない $2\langle N_S(N_S-1)\rangle$ である。救済形は
    (U1) **と** (U2′)（$\langle N_S(N_S-1)\rangle$ の非摂動上界。(U1) からは出ない）を仮定して
    $`\delta\le\min\{1/2,\eta\alpha^{-2}\lambda^{-1/2}\}`$（$\alpha^2$ だけ厳しい）。
  - **細い殻ルートは $h$ の下界に無益（audit3133 §C7、新規の負の結果）**: $D_{\rm free}$ が対角なので
    $\sup_\beta|N[\beta]|^2/D_{\rm free}[\beta]$ は台について加法的であり、達成可能な下界も $\delta$ に比例する。
    ゆえに $\delta\sim\alpha^{-2}\lambda^{-1/2}$ では分子の $\sqrt\lambda$ がちょうど相殺して $\lambda$ 一様定数になる。
    (L2) を全 $\lambda$ で成立させても Q3 には効かない。
  - **$\mathcal E_A$ の改良（33_ 定理4）**: $`\|a(h)\psi_0\|\le\|h\|_{L^2(S)}\langle N_S\rangle^{1/2}`$ に取り替えると
    (U1) の下で $|\mathcal E_A|/D_{\rm free}=O(\alpha^2)$ が $\lambda$・$\delta$ の両方に一様（稿 30_ は $O(\alpha^{3/2})$、太い殻限定）。
  - **1 ループの真値（33_ 命題6、数値）**: $`\langle N_{[\Lambda/2,\Lambda]}\rangle=0.186\,\alpha^2\sqrt\lambda`$（局所冪は
    $\lambda=10^4\to10^7$ で $0.553\to0.493$）。要求 $\lambda^{3/4}$ に対し $\lambda^{1/4}/\alpha^2$ の余裕。
    **反跳を落とすと厳密に $\lambda^2$** になり、差 $\lambda^{3/2}$ は必要な利得と一致する。
    17_ §6 の括弧書き「1 ループ分母を許せば $\alpha^2$ 定数」は $\sqrt\lambda$ だけ楽観的で、真値は
    厳密上界 $\alpha^2\lambda^2$ より $\lambda^{-3/2}$ 低く、楽観見積り $\alpha^2$ より $\lambda^{1/2}$ 高い（訂正ではなく精密化）。
- 再挑戦条件: **$`M^{(2)}_\perp(k):=\frac12\sum_\lambda\|R_k(\epsilon_\lambda\cdot\pi)\psi_0\|^2`$ の非摂動上界**（33_ §2.3 系3）。
  要求は $M^{(2)}_\perp\ll\frac{\pi}{2\alpha}\lambda^{-5/4}\delta^{-1/2}$、1 ループの真値は $`0.78\,\alpha\lambda^{-3/2}`$。
  これは**分母の側ではなく重みの側の量**なので F13 の閉鎖の外にあり、F13 が「残る資源は重みの側だけ」と
  宣言した当のものである。(U1)/30_ 命題6 と合同で攻略・監査するのが自然。
  上記 (a)(b)(c) の 3 系統には戻らない。
- 記録: `33_U2_殻光子数の非摂動上界.md`（self-audited、留保: 細い殻で 27_ §4 の分子 $\sqrt\lambda$ が
  残るかは未検証 — 独立監査の第 1 標的）、(研究ノート: `69_NS_shell_oneloop.py`) と `_output.txt`、
  (研究ノート: `2026-09-09_w116_U2.md`)。

## F16 — 「$\ell=1$ セクター内の余次元 1 の直交化 $\langle\beta,q_\nu\alpha_0\rangle=0$ で U4′（対凝縮との共鳴）を回避し、有用な下界を残す」
- 日付: 2026-09-09（稿 `37_delta2のλ冪.md`、w120/Opus。稿 31_ §4.3 → 36_ (T1) の筋）
- 分類: **機構の閉鎖（摂動的）**。存在言明は真だが到達点が $\lambda$ 一様に $O(\alpha^2)$ 倍まで落ちる。
- 正確な障害:

  直交化を課したときの到達点は $L=|y|^2\le\delta_\perp^2$、
  $`\delta_\perp^2:=\frac2m\min_{c}\|(s+u)^{-1/2}(r_\mu-c\,q_\mu\alpha_0)\|_{HS}^2`$（射影付きが正しい鋭い量。
  稿 36_ §3.4 の $\delta^2$ は射影なしで、その分だけ緩い）。$r_\mu$ の $O(e^4)$ 主要項を求めると:

  (a) **$\psi_0$ の 1 光子成分は恒等的に $0$**（37_ 命題W120-1。$H(0)$ の回転不変性 + 横 1 光子空間に
      回転不変ベクトルが無いこと。非摂動。摂動論でも角度積分が恒等的に消えることで独立確認）。
      よって $r_\mu$ の主要項は $\psi_0$ の 3 光子 $O(e^3)$ 成分だけから来る。

  (b) その主要項は**共鳴ベクトルに平行**である（37_ 命題W120-2）:
      $`r^A_\mu=\Theta(\sigma,v;\Lambda)\,q_\mu\,\alpha_0(1,2)`$。$k_3$ の角度積分が $\delta_{ij}$ と $\hat q_i\hat q_j$ しか
      生まないので、$q_\mu$ への比例は $O(e^4)$ の範囲で厳密である。

  (c) $\Theta\to\frac{2\alpha}{3\pi}\ln\frac{\lambda}{2(\sigma+v)}$（1 ループ質量繰り込み E05-F1 の $\frac{8\alpha}{3\pi}\ln$ の
      ちょうど $1/4$。$\Lambda$ 線型でなく対数なのは反跳 $|q+k_3|^2/2m$ による）。主対数は $(\sigma,v)$ に依らない
      **定数**なので、$q_\mu\alpha_0$ 方向への射影で丸ごと除かれる。残るのは $-\ln(\sigma+v)$ の殻内変動だけで、
      これは $\Lambda$ 非依存である。交換項 B・C は $\Lambda^{-1}$ で減衰し（数値、局所冪 $-1.00$）冪を変えない。

  したがって
  ```math
  \delta^2=1.90\times10^{-4}\alpha^4\sqrt\lambda\,\ln^2\lambda,\qquad
  \delta_\perp^2=6.22\times10^{-6}\alpha^4\sqrt\lambda,\qquad
  \frac{\delta_\perp^2}{L_{\max}}=\frac{4\alpha^2}{9\pi^2}\times0.0327=1.47\times10^{-3}\alpha^2 .
  ```
  **比は $\lambda$ に依存しない。** すなわち直交化枝は全 $\lambda$ で $7.8\times10^{-8}$ 倍（$\alpha=1/137$）だけ劣位で、
  「大 $\lambda$ で優位に転じる」ことは起こらない。冪は $L$ と同じ $1/2$ で、上回らない。
  射影なしの $\delta^2$ で見ても $\delta^2=L_{\max}$ となるのは $\ln\lambda=1.240+\frac{3\pi}{2\alpha}$、
  $\alpha=1/137$ で $\lambda\approx10^{281}$ であり、$L_{\max}=2$ の一貫性閾値 $\lambda\approx8\times10^{13}$ よりはるかに先である。

- **閉鎖の射程（重要）**: これは**摂動的な閉鎖**である。$\psi_0$ を $O(e^3)$ まで展開して得た冪であり、
  公理表 E05-L4 により摂動論は $\Lambda$ 非一様（有効域 $\lambda\lesssim\alpha^{-5/2}$）。
  非摂動的な $r_\mu$ が別の冪を持てば復活しうるが、その場合は比較相手の $L$（1 ループ $\alpha_0$ 由来）も
  同時に壊れるので、**片側だけ生き残る筋ではない**。
- 同じ論法に戻らないための注意: 「消したい汎関数と残したい汎関数がほぼ平行なら、余次元 1 という
  自由度の勘定は無意味」という点は F3（$\mathcal N(k)$ の ill-posedness）と同型の失敗である。
  今回はさらに強く、**残差の主要項までが同じ方向を向いている**ことが分かった。
- 派生（閉じていない）: $\eta$（$\mathcal E_A$ と密度型 4 次ブロック (ii)）の $\lambda$ 一様な上界。
  B16 の律速はここに移った（稿 37_ §7）。稿 36_ 残タスク 3・4、31_ 残タスク 3 と同一。
- 記録: `37_delta2のλ冪.md`（§2–§6）、(研究ノート: `74_delta2_power_termA.py`)、
  (研究ノート: `74_delta2_power_exchange.py`)、(研究ノート: `2026-09-09_w120_delta2.md`)。格付け `self-audited`（独立監査 未）。

## F17 — （w126、2026-09-10）第 5 の datum 候補 (C): スピン $1/2$ の $-\Lambda^2$ による 5 つの読みの判別

**閉じた主張**: Hiroshima–Ito の 2 ループ datum $a_2\approx-(\Lambda/m)^2$（負・$\lambda^2$）を
Q3 の 5 つの読み (i)–(v)（稿 40_ §2.1）に適用し、非摂動的な下界 $h\ge1$ と突き合わせて
「$h\ge1$ を保つ読みはどれか」を判別する。

**正確な障害（判別は成功しないのではなく、原理的に不可能）**:

1. **縛り 1 は使える。** E05-F3（$m_{\rm eff}\ge m$）はスピン $1/2$ でも成り立つ（稿 43_ 命題 W126-1）。
   $\sigma\cdot B$ は全運動量 $P$ に依存しないので、ファイバーのアフィン構造
   $H(P)=H(0)-\frac1mP\cdot v+\frac{P^2}{2m}$（$v=P_f+eA(0)$、スピン項を含まない）が逐語で保存され、
   パリティ $\Pi$ について $\Pi B(0)\Pi^*=+B(0)$、$\Pi v\Pi^*=-v$ なので $\langle v\rangle_0=0$。
   HI Corollary 2.15 が摂動版（$|e|$ 小）を独立に与える。**Kramers 縮退があっても一意性は不要。**
2. **その縛りが 5 つ全部を殺す。** $\alpha=1/137$、$C_2=1$ で $h\lt1$ になる $\lambda_\dagger$ は
   $0.3400523 / 0.3400523 / 0.3397734 / 0.3396633 / 0.3397184$（読み (i)–(v)）で、
   **相対ばらつき $1.1\times10^{-3}$**。5 つは区別されない。
3. **失敗の構造（命題 W126-3）**: 5 つの読みは 2 ループ率 $|P|$ について**相対差 $O(|P|)$ しか持たず**、
   $O(1)$ で分岐するのは $|P|\gtrsim1$ でのみである。$q\lt0$（$h$ を減らす向き）の datum では
   $h\lt1$ が $|P|\sim\frac{8\alpha}{3\pi}\rho\ln\lambda_\dagger\ll1$ で起きるので、
   **分岐域は丸ごと縛り 1 の禁止域の中に入る**。判別を殺したのは $-\Lambda^2$ の**大きさ**ではなく**符号**である。
   （発注時の見立て「符号も冪も違うから結果が劇的に離れる」は、**離れる場所**を外していた。）
4. **縛り 2 は使えない（弱いのではなく自己矛盾）。** HI 自身の「$\gamma\ge2$ を示唆」は**読み (i) の出力**
   （数値で $\gamma\to2.000000$ を確認）であり、読み (i) は $h\to-\infty$ を与えるので
   **同じ論文の Cor 2.15 が反証する**。$\gamma\ge2$ は $|h|$ の局所冪であって $h$ の局所冪ではない。
   HI 自身の Remark 2.10（「$a_2\lt0$ は $m_{\rm eff}\gt m$ と矛盾しない。漸近展開だから」）は**正しい**。
5. **転移も二重に閉じている。** 仮に判別が成功していても Q3 には触れられなかった。
   (a) D4 の工学次元 $+\frac12$ はスピンなし対セクター核（背中合わせ 2 光子、25_ 命題1）から来るが、
   HI の $-\Lambda^2$ は**別チャネル**（$\sigma\cdot B$ の自己エネルギーが $\mathcal E_4$ で相殺相手を持たない、
   $|k_1|/|k_2|\ll1$ の軟+硬。13_ §6）から来る。ルーティングされる対象が同じでない。
   (b) 13_ §6 の警告「2 ループの漸近則はスピンの有無で連続的につながらない」。

**同じ論法に戻らないための条件（(D5-条件)。次の datum 探索に効く）**:

> 判別に使える第 5 の datum は、**5 つの読みが $O(1)$ で分岐する領域（$|P|\gtrsim1$）が
> 既知の外的な縛りで禁止されていない**ものに限る。特に **2 ループ量が $h$ を増やす向き（$q\gt0$）**
> でなければならない。負符号の datum は冪 $\rho$ がどれほど大きくても判別に使えない。

さらに、$\lambda_*$ 共変か否かで $O(1)$ の差を生む領域が E05-L4 の摂動有効域（$\lambda\lesssim\alpha^{-5/2}$）の
**内側**にある必要がある（スピンなしの読み (iii) の固定点 $\lambda_*^{\rm fix}\sim\alpha^{-4}$ は外側で、
これが audit40 の判別も効かなかった理由）。**摂動論の外挿では原理的に届かない公算が大きく、
非摂動的な入力（$M^{(2)}_\perp$ の上界、対振幅の抑制）に戻る**——稿 40_ §4 の KC4-7 と同じ標的。

**閉鎖の射程**: 閉じたのは「**スピン $1/2$ の 2 ループ datum を読みの選別に使う**」という経路だけである。
HI の結果そのもの、W126-1（$h\ge1$ のスピン版）、および (D5-条件) は生きている。
Q3（スピンなし）の 3 バケットに対しては本ラウンドは**中立**（オッズ据え置き）。

**記録**: `43_D5_スピン1半による判別.md`（§3–§7）、(研究ノート: `79_spin_readings_flow.py`) と
`_output.txt`・`_result.json`、(研究ノート: `2026-09-10_w126_spin.md`)。
格付け `self-audited`（独立監査 未）。数値は C0（実行 < 10 秒）、格子 3 段で最後の 2 段の不変を確認済み。
同じコードにスピンなし datum を入れると稿 40_ の $\gamma_\infty=\frac12/\infty/1/1^-/\frac13$ を再現する（互換性確認）。


## F18 — 第 5 の datum を「2 ループ主要 UV 率（$\sqrt\lambda$）チャネル」の摂動的測定から取る道（2026-09-10、w127、稿 44_）

**閉じた主張**: KC-4 の 5 つの読み (i)–(v)（稿 40_ §2.1）のうち指数化群
$`E=\{(ii),(iii),(iv),(v)\}`$ の内部を、$h$ の $\alpha^n\sqrt\lambda$ 系列の摂動的 datum（絶対値）で判別する。

**正確な障害（3 点。どれか 1 つでも致命的）**:

1. **読み間の差が構造的に $P$ の 1 次で、係数が読みごとに違わない。**
   $\dfrac{\gamma_{(iv)}-\gamma_{(iii)}}{\gamma_{(iii)}}=-\dfrac{P}{1+P}$（**厳密**、$P=\frac{c_0\alpha^2}2\sqrt{\lambda_*}$）。
   発注 w127 が期待した「$O(|P|)$ の係数が読みごとに違うので高精度で見れば分けられる」は、
   この対については成立しない（係数はちょうど 1）。$(v)$–$(iii)$、$(ii)$–$(iii)$ は $O(P\ln\lambda_*)$ で、
   数値でも窓の端で $\le12P$。稿 40_ §2.1 の「相対差 $1.35\times10^{-6}$（$\lambda=1$）」は $|P|$ そのものであった。

2. **窓の内側では $P$ が小さすぎる。** 摂動窓の内側での最大分離は
   $P(\lambda_{\rm win})=\frac{c_0}2\alpha^{3/4}=6.3\times10^{-4}$（E05-L4 の窓）、
   $P(\lambda_\times)=\frac{8\alpha}{3\pi}=6.2\times10^{-3}$（内的な窓）。いずれも $\alpha\to0$ で 0。
   分岐域 $|P|\gtrsim1$ は窓の外にあり、隔たりは
   $\lambda_{\rm br}/\lambda_\times=1/A^2=(3\pi/8\alpha)^2$（$c_0$ にも E05-L4 にも依らない、稿 44_ 命題 W127-C）。

3. **$c_0$ の未決着が信号の 853 倍ある（決定的）。** 読み間の差は $h$ に対し $A\times$(2 ループ項)、
   $`c_0\in\{\frac1{2\pi^2},\frac1\pi\}`$ の未決着（audit41）は $(2\pi-1)\times$(2 ループ項)。
   比 $\frac{(2\pi-1)3\pi}{8\alpha}=853$（$\alpha=1/137$）で、$\alpha\to0$ で発散する。
   判別には $c_0$ を相対精度 $`\frac{8\alpha}{3\pi}=0.62\%`$ で確定する必要があり、現状は因子 $2\pi$（$528\%$）。

**閉じない部分（同じ論法に戻ってよい条件。ここを消さないこと）**:

- **log チャネルは閉じていない。** $h$ の $\alpha^2(\ln\lambda)^2$ 係数 $C_{LL}$ は
  固定次数の読み $(i)$ と指数化群 $E$ を分け、**$c_0$ を含まず**、摂動窓の内側にある（稿 44_ 命題 W127-B）。
  これが**予想 W127 の反例**であり、w124 が計算中。
- **「比」の datum は閉じていない。** $\alpha^3\sqrt\lambda$ 係数を $\alpha^2\sqrt\lambda$ 係数との**比**で見れば
  $c_0$ が約分され、障害 3 を迂回できる（読み $(iv)$ の予言は $-A$、$(iii)$ は $0$）。
  ただし 3 ループの UV 漸近計算が要り、E05 は現在それを持たない。
- **$c_0$ が決着すれば障害 3 は消える**（障害 1・2 は残る）。したがって本項目は
  「$c_0$ 未決着の下で」閉じた項目であり、audit41 の処方が通れば再開の余地がある。

**教訓（次の発注への含意）**: 第 5 の datum の必要条件は 2 つになった。
**(N1)**（43_ の (D5-条件)）$h$ を増やす向き（$q\gt0$）であること。
**(N2)**（本項目）$\lambda_*\gtrsim\lambda_{\rm br}=16\pi^4/\alpha^4$ の流れに感度を持つか、
さもなくば窓の内側の**$c_0$ フリーな部分主要係数**であること。

## F19 — 「D6（$h$ の $\alpha^3\sqrt\lambda\ln\lambda$ 係数）を『$b_2$ 型の 2 光子対 × 1 光子対数ループの積項』1 積分で決める」（2026-09-10、w130、稿 47_）

**閉じた主張**: audit43 §E-3 の 5. が提案した kill-check —「先に $b_2$ 型 × 1 光子ループの積項だけを計算し、
その係数が $\frac{8c_0}{3\pi}$ 相当のスケールを持つかを見る」— によって、$a_3$（$e^6$）の全計算に入らずに
D6 を（あるいは既約図の要否を）**その場で決める**道。

**正確な障害**（稿 47_ 命題 47-2・47-4、`self-audited`）:

1. **$\sqrt\Lambda$ の源が $b_2$ 型に限られることは正しい**（命題 47-1）。3 光子クラスターは
   Coulomb ゲージ $\epsilon(k_3)\cdot k_3=0$ が頂点を $\Lambda\to Q$ に落とすため
   $Q^7/\Lambda^4\big|_{Q=\sqrt\Lambda}=\Lambda^{-1/2}$ で $\Lambda^{-1}$ 抑制される。
   **ここまでは発注文・audit43 の見立てどおりである。**
2. **しかし「積項」は 1 本ではない。** $b_2$ 型の対に付く 1 光子対数ループには
   **(A) 対と重ならない挿入**（可約。$a_1\times b_2$ に分解）と **(B) 対と共存する挿入**（既約）があり、
   **両方が同オーダー $\sqrt\Lambda\ln\Lambda$ に効く**。対数重みは
   $`\Delta(S,\Lambda)=\int_0^\Lambda\frac{r\,dr}{S+r+r^2/2}`$ で計られ、
   $\Delta(0,\Lambda)=2\ln\frac{\Lambda+2}{2}$（= $a_1$ の $L$）に対し $\Delta(2\Lambda,\Lambda)=\ln\Lambda-\ln4+O(\Lambda^{-1/2})$、
   **比はちょうど $\frac12$**（解析＋数値: 切断 7 段・格子 3 段で最後の 2 段 $0.500084\to0.500008$。
   対の重み $s^{-1/2}$ 込みでも $0.500696\to0.500089$。(研究ノート: `84_D6_killcheck_logweight.py`)）。
   (B) の明示的な一員は $`\langle eA\psi_0^{(2\gamma)},G_0\,eA\psi_0^{(2\gamma)}\rangle_{3\gamma}`$
   （速度作用素の $-eA$ 部分が対状態から光子を放つ $e^6$ 項）で、$a_1\times b_2$ に分解しない。
3. **可約部分だけで決まる分岐は存在しない。** 逆転が自動的に与える level-1 可約部分は
   $[2a_1a_2+a_1^3]_{\sqrt\lambda\ln\lambda}=\frac{16c_0}{3\pi}$、D6 単位で $+\frac{16}{3\pi}=+1.6977$ であり、
   5 読みの予言 $[-0.4244,+0.8488]$ の**どれとも一致しない**。ゆえに $[a_3]_{\sqrt\lambda\ln\lambda}$ は
   必ず大きな負で、判別は既約部分に 100% 載っている。
4. **判別能力そのものにも欠落がある**（命題 47-6）。**D6 は読み (i) を落とせない。**
   (i) の D6$=0$ は「$\alpha^3$ 項を書かない」という定義上の値であり、稿 41_ §3 は D5 のとき (i) を
   「補完」して延命させた前例を作っている。同じ扱いを許すなら (i) は任意の摂動 datum で反証不能、
   literal に取るなら (i) は既に D5（$C_{LL}\ne0$）で死んでいる。
   **D6 が分けるのは (ii) / (iii)(iv) / (v) の 3 群であって、(i) と (v) ではない。**

**閉じない部分（同じ論法に戻ってよい条件。ここを消さないこと）**:

- **D6 そのものは閉じていない。「現実的でない」とは判定しない。** 障害は積分ではなく
  $e^6$ 展開の項生成であり、HS Lemma 3.8 の証明を 1 段延長する紙の作業である。
  稿 47_ §6 のフィルタ（「端の背中合わせ対を含む項だけ」+「$\ln$ を作る第 3 光子は 1 本だけ」）で
  残る項は十数本の規模と見込まれ、audit43 の「1 ワーカー 1 セッションで届く」は維持される。
- **標的は 1 パラメータに縮んだ**（稿 47_ 命題 47-3）: $\mathrm{D6}=\frac8{3\pi}(1-\theta)$、
  $\theta$ = 対セクターの $\sqrt{\Lambda/M}$ の $`M=m\,h^\theta`$ の冪。$\theta=0,\frac12,1,\frac32$ が
  (ii),(iii)(iv),(i),(v)。**次発注は数ではなく $\theta$ 1 個を狙えばよい。**
- **D6 は $c_0$ に依らない**（命題 47-5）。F18 が閉じた最大の理由（$c_0$ の因子 $2\pi$ が信号の 853 倍）は
  D6 では比で完全に相殺する。**F18 の「閉じない部分」に書かれた『比の datum』の具体化が D6 である。**

**教訓（次の発注への含意）**: 「可約と既約を分ける kill-check」を設計するときは、
**同じ対数が異なる重み（ここでは $2\ln\Lambda$ と $1\ln\Lambda$）で複数回現れる**可能性を先に潰すこと。
本件では「項数が多い」ではなく「1 つの対数が半分の重みで二重に現れる」ことが kill の理由だった。

## F20 — E05-L5（双極子の終端 $\Lambda_c=\frac{3\pi m}{4\alpha}$）をフル PF に移送して $s_{\rm exp}\ge1$（線形以上）を主張する筋

**閉じた主張**: 双極子で物理質量固定の裸質量の解が有限 $\Lambda_c$ で消える（E05-L5）ことを根拠に、
フル PF の対セクターでも指数 $s_{\rm exp}\ge1$（$\gamma_\infty\ge1$、Q3 の「線形以上」バケット）が支持される。

**正確な障害**（稿 45_ 命題 S-5、§4.3）。双極子の終端は自己無撞着関係の内部で厳密に再現される
（$h-1=a\lambda=a\lambda_*h$、$a=\frac{4\alpha}{3\pi}$、$h=\frac1{1-a\lambda_*}$ が $\lambda_*=\frac1a=\frac{3\pi}{4\alpha}$ で発散）。
しかし一様な質量の着せ替えの下では

$h-1=q_0\lambda^\theta=q_0(\lambda_*h)^\theta$ より $h^{1-\theta}\simeq q_0\lambda_*^\theta$ であり、
**物理質量を固定して $h\to\infty$ が有限の $\lambda_*$ で起きるのは $\theta\ge1$ のときに限る**
（$\theta=\frac12$ では $\lambda_*\to\infty$ が要る）。すなわち終端の原因は datum のチャネル指数 $\theta$ であって
着せ替えの度合いではない。双極子は $\theta_{\rm dip}=\nu=1$ でちょうど境界、フル PF の対チャネルは
$\theta=\frac12$ なので、**L5 から $s_{\rm exp}\ge1$ は導けない**。
これは 42_ §4.4・audit42 (E)（「KC4-5 の一致は $\nu=1$ の偶然」）を独立に補強する。

**残る余地**: $s_{\rm exp}\ge1$ 自体は閉じていない。非一様な着せ替え（反跳質量だけを着せ、頂点の質量を
着せない＝最小結合の破れ）なら $s_{\rm exp}\ge1$ に到達する。**ただしその根拠は L5 ではない。**

---

## F21 — 「対セクターの $M$ が $m$ か $m_*$ かを決めれば $s_{\rm exp}$ が決まる」という 2 択の枠付け

**閉じた主張**: 2 ループ対セクターの $h-1\simeq c_0\alpha^2\sqrt{\Lambda/M}$ の $M$ が裸質量 $m$ か走る質量 $m_*$ かを
決めれば、$`s_{\rm exp}\in\{\frac12,0\}`$ が定まり $`\gamma_\infty\in\{\frac12,\frac13\}`$ が決まる。

**正確な障害**（稿 45_ 命題 S-1・S-6、§2.2–§2.5）。質量は 1 箇所ではなく **4 箇所**に入る:

$$h-1\ \propto\ \alpha^2\,m_0\,M_k^{5/2}\,m_g^{-2}\,m_v^{-2}\,\Lambda^{1/2}$$

（規格化 $m_0$、シーガル頂点 $m_g$、速度作用素 $m_v$、反跳 $M_k$。全部裸で E05-L1 の $\sqrt\lambda$ に一致）。
$m_i=mh^{\tau_i}$ とすると $s_{\rm exp}=\frac12+\tau_0+\frac52\tau_k-2\tau_g-2\tau_v$ で、
$\tau_i\in[0,1]$ を独立に振ると $s_{\rm exp}\in[-\frac72,4]$。**「$M$」という単一の対象が無く、2 択は ill-posed。**
さらに支配的配位の反跳運動量は $|q|\sim\sqrt{2M\Lambda}\gg m_*$ で、14_ 補題8（$\mathcal E\le|q|$）と
E05-F9（$\mathcal E\ge c|q|$）よりその領域のドレスト分散は**線形**であり、$\frac{q^2}{2m}$ でも $\frac{q^2}{2m_*}$ でもない。

**転進先**: well-posed な問いは「4 つの質量スロットの着せ替えが**一様**か（＝有効理論が最小結合形
$\frac1{2M}(p-eA)^2$ を保つか）」である（稿 45_ 補題 W129-L1）。
【2026-09-10、出所 audit47 (C-2)】以下に続いていた「一様であれば $\gamma_\infty=\frac1{2+\tau}\in[\frac13,\frac12]$」の
帰結は退化した $\gamma_\infty=\theta/(1+\tau\theta)$ に依存しており無効。well-posed な問いは
**一様性の検証**であるという上記の一文までで止める。


## F22

**閉じた経路**: **摂動 datum（$C_{LL}$ と $\mathrm{D6}$）から、再和した自己無撞着関係の Q3 バケットを決める。**
経路 B17（KC-4 の読み族）と B18（較正器を通る $\tau$ 族・正規形）の**共通の終着点**である。

**日付・出所**: 2026-09-10。稿 51_（w134）→ (研究ノート: `51_骨格原理_audit55_2026-09-10.md`)（audit55、S2 full fresh audit）。
数値は (研究ノート: `97a_audit55_normalform_series.py`)・`97c_audit55_buckets_alpha_scaling.py`。

**正確な障害（構造的。これが本項の内容）**:

> **摂動係数は、着せ替え関数の $h=1$ における 1 階微分しか測らない。バケットは $h\to\infty$ の大域挙動である。**

自己無撞着関係を $`h-1=G\,A(h)\ln(1+\frac\lambda{2h^\mu})+c_0\alpha^2\lambda^\theta B(h)`$（$A(1)=B(1)=1$）と書くと
```math
C_{LL}=G_1^2A'(1),\qquad \mathrm{D6}=G_1\bigl(A'(1)+B'(1)\bigr)
```
であり、**2 本の datum が拘束するのは $(A'(1),B'(1))=(\frac12,\frac54)$ という 2 つの数だけ**である。
$A,B$ の大域形は自由に残るので、audit55 は $(A'(1),B'(1))$ を厳密に保ったまま次を構成した。

| 族 | 着せ替え | $\gamma_\infty$ | バケット |
|---|---|---|---|
| X1 | $B(h)=1+\frac54\ln h$（対数） | $\frac12$ | 弱い冪 |
| X2 | $B(h)=1+\frac{\frac54(h-1)}{1+a(h-1)}$（Padé） | $\frac12$ | 弱い冪 |
| X3 | $`\alpha^3\sqrt\lambda\,h^{9/4}`$ の第 3 チャネル（係数負） | $0$ | 劣線形 |
| (N) | 2 チャネル・純冪 $h^{r_p}$ | — | 有限 $\lambda$ 終端 |

**3 つとも (R-a)（対チャネルは双極子極限で恒等的に 0）と (R-b) を厳密に満たし、$C_{LL}$・$\mathrm{D6}$ を 10 桁で再現する。**
すなわち **3 バケットすべてが同じデータと整合する**。「不定になる」のではなく「**どれにでも確定させられる**」。

**なぜ稿 50_ 命題 50-2 で塞げないか（量化子が 2 段違う）**: 命題 50-2 は
「$O(e^6)$ の $\sqrt\Lambda\ln\Lambda$ を出す図」という**固定次数・固定対数構造**の列挙の閉包であって、
**全次数の再和における $h$ 依存性の関数形**の閉包ではない。X3 は対数なしの $\alpha^3\sqrt\lambda$ なので
列挙対象にすら入らず、X1・X2 は図を一切変えない。

**副次的な障害**: 仮に (N) を認めても、終端位置は $\lambda_c\propto\alpha^{-4}$（97c [C1] で傾き 4.02）で、
**E05-L4 の摂動有効域 $\lambda\lesssim\alpha^{-5/2}$ の遥か外**にある（$\alpha=\frac1{137}$ で $x_c=20.6$ 対 $x_{L4}=12.3$）。
$\alpha\to0$ で終端は $\Lambda\to\infty$ に逃げるので、「終端」は摂動論の破れの言い換えでありうる。

**何が新しければ再挑戦可か**:

1. **正規形 (N) の完全性の証明**（全次数の再和で $h$ 依存性が 2 チャネル・純冪に閉じること）。
   これは図の列挙ではなく**関数形の閉包**なので、稿 50_ の手法の延長では届かない。
2. **$h=1$ の高階微分を測る datum**。$A''(1)$・$B''(1)$ を測るには $\alpha^4$ 以上の係数が要るが、
   有限個の微分を測っても大域形は決まらない（X1 と X2 は全次数で異なるのに同じバケット、
   逆に $B$ を微調整すれば任意のバケットを作れる）。**datum を増やす方向は原理的に閉じている。**
3. **非摂動側の情報**（変分下界 B16、汎関数積分・拡散係数 B11）。**残る生きた経路はこちらだけである。**

**関連**: F19（D6 の 1 積分 kill-check）、E05-F14（軸 A）、E05-L4。B17・B18 は本項により実質閉鎖。



## F23 「較正器を強める」ことで自己無撞着関係の骨格（パラメータ化）を選ぶ経路

**閉じた主張**: 稿 48_ の族が (R-a)(R-b) を通っても骨格が絞られない（audit51 (B-1)(D-3)）ので、
**較正器を「$\gamma_\infty$ の一致」から「T-e の関数形 $h=1+W$ の再現」へ強めれば骨格が 1 つに決まる**、
という道（audit50 §2.5、audit51 (C-2)、発注 (研究ノート: `w134_骨格を選ぶ独立な原理.md`) §2 の中心的作業仮説）。

**正確な障害**（2026-09-10、稿 51_ 命題 W134-5、w134）: **強い較正器は 3 骨格を 3 つとも通す。選別力はゼロ。**
双極子極限が骨格ごとに
#1（Φ 形・1 光子前因子 $h^{\tau_0-2\tau_v}$、拘束 $\tau_0=2\tau_v$）で $h-1=Wh^{\tau_0-2\tau_v}$、
#2（Φ 形・拘束 $\tau_0=\tau_v=\tau_g=\tau$）で $h-1=Wh^{-\tau}$、
#3（Woodbury）で $h=h^\tau+W$ となり、$h=1+W$ との一致条件はそれぞれ
「$\tau_0=2\tau_v$（＝#1 自身の拘束。無条件に通る）」「$\tau=0$」「$\tau=0$」で、
**いずれの骨格にも通る点が存在する**。強い較正器が持つのは**骨格内で $\tau$ を 1 点に潰す力**だけである。

さらに、その 1 点での帰結は骨格ごとに**食い違う**: Φ 形（#1/#2）は $\mathrm{D6}=\frac{14}{3\pi}$ を
パラメータ無しで予言して**的中する**が、Woodbury（#3）は $\mathrm{D6}=\frac{10}\pi=3.1831$ を予言して
**実測 $\frac{14}{3\pi}=1.4854$ を 2.1429 倍外す**（(研究ノート: `96_w134_normalform_D6_selection.py`) [D]）。
すなわち**「強い較正器 ＋ Woodbury 骨格」は D6 に反証される**が、それを反証したのは較正器ではなく datum である。

**同型の誤りへの注意**: この経路が魅力的に見えたのは「強い較正器が $\rho_{\rm pair}=\frac54$ を予言し、
後から独立計算された D6 がちょうどその値だった」という一致による。しかし
**同じ $\mathrm{D6}=\frac{14}{3\pi}$ は骨格 #1 では $\tau_g=0$、#3 では $\tau=\frac8{13}$ で実現する**
（稿 51_ §3）。同じ数値が 3 つの互いに異なる構造的事実に対応するので、
**数値の一致は「$\tau=0$」を構造として同定していない**（T9・T19・T31 と同型。稿 51_ 非主張 4）。

**転進先（2026-09-10、親が audit55 を踏まえて書き換え）**: 骨格を選ぶ必要そのものは確かに無くなった
（$C_{LL}$ と D6 は骨格に依らない正規形指数 $(r_1,\ r_1+r_p)$ を測る。稿 51_ 命題 W134-1・W134-2、`verifier-backed`）。
**しかしそれで Q3 のバケットが決まるわけではない。** 残ると思われた「仮定 (N) の検査」は
**audit55 が反例で決着させた**（(N) を外すと 3 バケットすべてが同じデータと整合する）。
**転進先は F22**（摂動 datum からバケットを決める経路そのものの閉鎖）であり、
**生きた経路は非摂動側の B11・B16 だけである。**

**注記**: w134 自身が上で「数値の一致は構造を同定しない」（T9・T19・T31 と同型）と正しく警告しながら、
最後の段落で「バケットは一意に定まる」と書いていた。**親はその段落を採用せず、本項を F22 に接続した。**


## F24

**閉じた経路**: **Föllmer ドリフトのマルティンゲール部 $G=M_T$ を試行関数に取る変分下界で、Q3 の劣線形側を示す。**
稿 52_ 命題 52-4 の $\beta$ 判定条件
$`\sqrt\lambda(1-\sqrt m\,\beta_\Lambda)\to\infty\Rightarrow`$ Q3 劣線形。

**日付・出所**: 2026-09-10。稿 52_（w135）→ (研究ノート: `52_L5a_audit56_2026-09-10.md`)（audit56、S2、命題 A56-1・A56-2）。
数値は (研究ノート: `99_audit56_slack_asymptotics.py`)。

**正確な障害（循環。これが本項の内容）**:

> **逆向き三角不等式から $`1-\sqrt m\,\beta_\Lambda\le\sqrt{mD_\Lambda}=h^{-1/2}`$ が恒等的に成り立つ**（命題 A56-1）。

したがって $t:=h(1-\sqrt m\beta_\Lambda)^2\le1$ とおくと
```math
\sqrt\lambda\bigl(1-\sqrt m\beta_\Lambda\bigr)=\sqrt{t\,\lambda/h}\ \le\ \sqrt{\lambda/h}
```
で、**判定条件の左辺は $\lambda/h$ を超えない。** すなわち **$\beta$ 判定条件は Q3 より弱い条件には決してならず、
$\beta_\Lambda$ の $\Lambda$ 一様上界を作る仕事は $h$ の上界を作る仕事と同難度**である。
これは 38_ (7.2)（Q3 $\iff\Lambda\sigma^2_\Lambda\to\infty$）と**同じ身分の書き換え**であって、証拠ではない。

**緩みの漸近（稿の申告は誤りだった。ただし訂正の向きも救いにならない）**: 稿 52_ は較正から
「緩みは $h$ とともに増え、判定条件は $h=o(\sqrt\lambda)$ までしか届かない可能性」と書いたが、
audit56 命題 A56-2 は可解模型で $\sqrt m\beta_\Lambda=1-h^{-1/2}$ が**厳密**（$t\equiv1$）であることを示した。
数値でも $1-t=\Theta(1/T)$ で前係数は $h$ について有界。**稿の表は有限 $T$ の端効果の産物である。**
$t\to1$ なので**弁別できないバケットは無い代わりに、判定条件は $\lambda/h\to\infty$ そのものになる。**
**「緩みが悪化して届かない」のではなく「緩みが無くて同値」だから使えない。**

**未申告だった前提（audit56 (P1)）**: 稿は判定条件を「無条件」と書いたが、実際には
(i) $\lim_TR_\Lambda(T)/3T=D_\Lambda$ と $\lim_T\beta_\Lambda(T)$ の存在（＝29_ (G1)(G2)、未証明）、
(ii) **N1 の等号 $D_\Lambda=1/m_{\rm eff}$**（E05-F11）を使う。
29_ 命題3 が無料で与えるのは**逆向き** $1/m_{\rm eff}\le D^-$ だけで、$D$ の下界からは $h$ の上界は出ない。
**稿 §5.4 の「向きは 29_ 命題3 で確定済み」は帰属誤りである。**

**無条件で残るもの（閉鎖しない部分）**: 変分下界そのもの
$R_\Lambda(T)\ge|\mathbb E_\mu[X_T\cdot G]|^2/\mathbb E_\mu|G|^2$（任意の $G\in L^2(\mu)$）は
**真に無条件で成立する**（Cauchy–Schwarz と有限 $T$ の三角不等式のみ。`verifier-backed`）。
閉じたのは**試行関数の選択 $G=M_T$** であって、変分原理そのものではない。

**何が新しければ再挑戦可か**:

1. **$M_T$ と異なる試行関数 $G$**。ただし採用前に**縮退検査**を通すこと（下記）。
2. **$D_\Lambda$ の下界を経由しない経路**。N1 の等号を使わずに $h$ の上界へ行く道。
3. 非摂動側で $\Lambda$ 一様な情報を新たに供給するもの（B16 の $\eta$ など）。

**新設する必須手続き（縮退検査）**: **Q3 に効くと称する不等式・判定条件は、採用前に
「それが Q3 の言い換えに退化していないか」を検査する。** 具体的には
**(a) 逆向きの不等式が同じ量を同じオーダーで抑えないか、(b) 厳密可解模型（双極子）で等号にならないか**を確認する。
本項と 38_ (7.2) と B16 の天井は**すべて同じ失敗形**（道具が問題を制約せず言い換える）であり、
この検査を先にすれば 3 ラウンド節約できた。

**関連**: F22（摂動 datum は大域挙動を決めない）、38_ (7.2)、REGISTRY B16 の天井、E05-F11。


## F25

**閉じた経路**: **変分下界 $R_\Lambda(T)\ge|\mathbb E_\mu[X_T\cdot G]|^2/\mathbb E_\mu|G|^2$ の試行関数 $G$ を
うまく選んで、Q3 の劣線形側（$D_\Lambda$ の $\Lambda$ 一様下界）を得る。** B11 の L5b／L5b′ ルート全体。

**日付・出所**: 2026-09-10。稿 53_（w136、定理 53-7）→ (研究ノート: `53_試行関数_audit57_2026-09-10.md`)（audit57、S2）。
数値は (研究ノート: `100_w136_trial_function_degeneracy.py`)・`101_audit57_trial_degeneracy_recheck.py`。

**正確な障害**: **試行関数の選び方の問題ではない。$h$ を知らずに両辺を評価できる経路が足りない。**

- **第 1 カオス族（決定論的核 $f$）は 1 つの数しか測らない**（系 53-4）:
  $\mathcal B=3TD_\Lambda\cdot\langle f\rangle^2/\langle f^2\rangle$ で、$f$ の選択は $[0,1]$ の係数を掛けるだけ。
  **$G=M_T$ の失敗（F24）はこの族全体の性質の特殊例だった。**
- **唯一 $h$ 盲目な分子を持つ $G=\Xi_T$ は $h\le h$ に潰れる**（命題 53-6）。
  audit57 命題 A57-2 はこれを**模型に依らず無条件**に強化した: $\mathbb E_\mu|\Xi_T|^2/3T\ge(h-1)^2/h$ が
  Cauchy–Schwarz と命題 52-1 から従い、**双極子は等号＝最良ケース**。フル PF では不等式がさらに緩むので**さらに無益**。
- **$h$ 盲目の評価経路は 4 本**（稿は 3 本と数えたが audit57 が 1 本追加）:
  (C-I) Wiener 比較（$e^{TE_\Lambda(0)}$ で $T$ 非一様）、(C-II) $e^2$ 摂動（$\alpha^2T\Lambda^2/m$ で非一様。E05-L4 の確率側版）、
  (C-III) $\mu$ の厳密恒等式（射程は第 1 カオスと $\Xi_T$ に尽きる）、
  **(C-IV) 相対エントロピー／Girsanov**（audit57 が発見。コストが $`H(\mu\|\mathbb W)`$ で $T$ に線型＝**$T$ 一様**なので
  (C-I) の kill を通り抜けるが、**$\Lambda$ で死ぬ**: $H/T$ が要求精度 $3/(m\lambda)$ の $1.9\to172$ 倍に発散）。
- **列挙依存を解消する非増幅命題**（audit57 命題 A57-1）: $G$ から得られる上界は最良でも $h/\eta[G]$。
  したがって**経路の列挙が完全でなくても閉鎖は成り立つ**。定理 53-7 の主柱はここに移した。
- **他の 9 候補は向きが逆**（対数 Sobolev、FKG、結合、スペクトルギャップ、単調収束、$\partial_\Lambda$、OS/KL 等）。
  いずれも $D$ の**上界**＝$h$ の**下界**＝Q3 **否定**側を与え、劣線形側には効かない。
- **殻に局在した $G$** は audit3133 の閉鎖が及ぶ（「線型分子 + 対角分母 ⟹ 台について加法的」という同じ補題の 2 実例）。

**何が新しければ再挑戦可か**:

1. **$h$ 盲目でない入力**を許す。ただし自明界 $h\le X$ を入れても増幅しない（audit57 (Q1-b) の不動点計算。
   第 1 カオスで $h\le X\langle f^2\rangle/\langle f\rangle^2\ge X$、$\Xi$ でも $\ge h$）。**非自明な $\Lambda$ 一様入力が要る。**
2. **(C-IV) の $\Lambda$ 依存を改善する**（相対エントロピーのコストを $\lambda$ の要求精度以下に落とす）。
3. **向きが逆の 9 候補は Q3 否定側には使える**。線形以上／終端を示す方向なら生きている。

**生き残るもの**: 変分下界そのもの（稿 52_ 命題 52-4 前半、`verifier-backed`）は真である。閉じたのは**その使い道**。

**関連**: F22（摂動 datum）、F24（$G=M_T$）、E05-F17、REGISTRY B11。
**次の一手の種**: audit57 §8.1 の**双極子による下からの支配**（$\lambda mb_\Lambda\to3\pi/4\alpha$ で**閾値に 1 冪足りない**）。
成功すれば「線形以上」から**超線形を除去する非摂動 datum** になる。**向きが正しい唯一の残り筋である。**


## F26

**通らなかった経路（※「閉鎖」ではない。B19 として未解決で継続）**:〔2026-10-26 注記(audit_S0_731):**B19 は偽で閉じた** —— 系 731-B(E05-P388、稿 `731_B19の否定とA4primeの強い版_P375の系_2026-10-26.md` §1 (b)):本項の標的 $h\le C(\alpha)\lambda$ は、どの $C(\alpha)\lt\infty$ でも大きい λ で偽(E05-P375 の $h_{\rm ls}\ge c_\kappa\lambda^{1+(1-\kappa)/7}(\ln\lambda)^{-k}$)。本項の「閉じた 2 つ」(命題 54-1・54-3)は方法の否定としてそのまま残る。〕
**双極子による下からの支配 $D_\Lambda\ge b_\Lambda$ を示して $h\le C(\alpha)\lambda$ を得る**
（Q3 の「線形以上」から**超線形を除去する非摂動 datum** を作る筋）。稿 `54_双極子による下からの支配.md`。

**日付・出所**: 2026-09-11。稿 54_（w137）→ (研究ノート: `54_双極子支配_audit58_2026-09-11.md`)（audit58、S2）。
数値は (研究ノート: `102_*`)・`103_*`・`104_*`。**支配は未証明。得られた上界は 1 本もない。**

**閉じた（＝原理的に不可）のは 2 つだけである**:

1. **核の点ごと比較**（命題 54-1、`verifier-backed`）: $\sigma^2_{\rm full}(B)\le\sigma^2_{\rm dip}(B)$ は**厳密に偽**。
   非対角部は Wiener 測度の下で厳密に中心化されるので $\mathbb E_{\mathbb W}[\Delta]=0$ であり、
   $\Delta\ge0$ a.s. なら $\Delta\equiv0$ になるが $\Delta\not\equiv0$（$\Phi_{\rm full}\lt\Phi_{\rm dip}$ から全 $\Lambda\gt0$ で厳密）。
   **射程**: 「**点ごと比較だけを入力とする証明**は存在しない」まで（audit58 (R3) が射程を限定。
   **Hargé 型は入力が違うので抵触しない**）。
2. **FKG／Harris 型の相関不等式**（命題 54-3、`verifier-backed`）: 増分場は $e\ne0$ の全 $\Lambda$ で
   **association を持たない**。反射正値性から $C^{\rm reg}_v(\tau)\lt0$（双極子では閉形式で厳密）。
   **audit58 (R1) の判定で射程は稿より広い**: 実際に使うのは association の**自明な必要性**だけなので
   **Gauss 性も Pitt の非自明な向きも不要**で、**フル PF に直接移る**。
   **Hargé・Royen・GCI 型（凸性）は殺されていない。**

**通らなかったが死んでいない 2 つ**:

3. **エントロピー・ドリフト**: 通らないが**稿の死因の説明は誤り**（相対エントロピーからは対角部が恒等的に落ちる）。
   正しい死因は「**双極子だけで $H/T$ が超線形**」。**窓は $\alpha$ に強く依存する**:
   $H_{\rm dip}/T=\frac32$ を割る $\Lambda$ は $\alpha=0.30$ で $14.9$、**$\alpha=1/137$ で $141$**
   （親が 2026-09-11 に確定。(研究ノート: `104_親_P13_entropy_alignment.py`)、`verdict: PASS`）。
   **参照測度を $\mu_{\rm dip}$ に替えた $`H(\mu_{\rm full}\|\mu_{\rm dip})`$ は未検討。**
4. **ハミルトニアン側 Legendre 双対（ラウンド 3）**: **死んでいない。**
   旧命題 54-4「厳密に循環」は **audit58 (R4) が撤回**した。示すべきは
   $F_{\rm full}(u)\ge\frac{m^{\rm dip}_*}2|u|^2$、$m^{\rm dip}_*=m\frac{h_{\rm dip}}{h_{\rm dip}-1}$ で、
   **この定数は既知**であって $h_{\rm full}$ ではない。**しかも N1（E05-F11）を要さない唯一の経路である。**

**構造的な成果（本項の本体。E05-F19 として事実表へ）**: **系 54-3a** —
**反射正値性が「安い道具が軒並み逆向きになる」ことの単一の原因である。**
$C^{\rm reg}_v\le0$ から (a) $3D=\inf_\tau R(\tau)/\tau$（$D$ が**下限**として現れるので安い評価はすべて**上界**＝
$h$ の下界＝Q3 **否定**側）と (b) Gauss 参照測度が**負相関**（FKG 不可）が**同時に**従う。
audit57 §8.1 の 4.（反射正値性）と 5.（FKG）は**同じ構造の 2 つの顔**だった。

**再挑戦の入口（audit58 §6.3 の優先順位）**:

| 順位 | 入口 | 1 行に還元した問い |
|---|---|---|
| **1** | **Hargé 型の凸性不等式** | **$\sigma^2_{\rm full}$ は $B$ について凹か**（同値: $e^{c\Delta}$ は $B$ について凸か）。偶関数性で右辺が 0 になり目標がそのまま出る。**安い kill-check 可** |
| 2 | ラウンド 3（制約付き励起エネルギーの 2 次下界） | $F_{\rm full}(u)\ge\frac{m^{\rm dip}_*}2|u|^2$。**N1 不要** |
| 3 | 参照測度を $\mu_{\rm dip}$ に替えたエントロピー | $`H(\mu_{\rm full}\|\mu_{\rm dip})/T`$ は $\Lambda$ 一様か |
| **却下** | $\rho_{\rm full}-\rho_{\rm dip}$ の赤外相殺 | **目標の restatement**で方法を与えず、相殺すべき赤外発散も最初から無い（$\int d\rho/E$ は収束） |
| 却下 | Brascamp–Lieb | 向きが逆 |

**関連**: F22・F24・F25（いずれも「閉鎖」。本項だけが「未解決」）、E05-F7（役割の訂正）、REGISTRY **B19**。


## F27

**閉じた入口（B19 の第 1 位と第 5 位。B19 本体は未解決のまま継続）**:
**Gauss 測度の相関不等式（凸×凸型・GCI 型）で $\mathrm{Cov}_{\mu_{\rm dip}}(|X_T|^2,e^{c\Delta})\ge0$ を出す。**
稿 `55_凸性判定とHarge経路.md`（w138）。

**日付・出所**: 2026-09-11。数値は (研究ノート: `105_*`)（較正 PASS）・`105b_*`・`105c_*`（ともに `COUNTEREXAMPLE`）。

**正確な障害（2 行で閉じる。これが本項の要点）**:

> **$\Delta$ は偶関数で $\Delta(0)=0$ である。ゆえに $e^{c\Delta}$ が $B$ について凸なら
> $\Delta\ge0$ がいたるところ従い、それは点ごとの核支配であって命題 54-1（`verifier-backed`）により厳密に偽。**
> $c\gt0$ の取り方に依存しない。同じ論法で $\sigma^2_{\rm full}$ の凹性も 2 行で否定される
> （$\Sigma\ge0$ かつ $\Sigma(0)=0$ で凹なら $\Sigma\equiv0$）。

**最も重要な構造的発見**: **$\mu_{\rm dip}$ のパリティは、Hargé の右辺を 0 にして入口を開けると同時に、
凸性の仮定を点ごと核支配に格上げして出口を塞ぐ。** すなわち audit58 §1.4 が「唯一の隘路」と名指した 1 点は、
**同じ稿 54_ の §3（命題 54-1）で既に閉じていた**。入口と出口が同じ性質から来ている。

**書誌の訂正（w138 が照合。本テーマの禁止事項に直結する）**:

- **凸×凸の相関不等式の一次出典は Hu (1997)** であって **Hargé (2004) ではない**
  （Hargé 2004 は別証明を与えたにすぎない）。**audit58 §1.4 の帰属は誤りだった。** [2026-10-04 lit_GXN3 注記: 原典では Hargé 2004 Thm 1.2 も凸×凸の不等式(Hu 1997 Thm 6 の改良)。「誤り」は「一次出典は Hu 1997 Thm 6」に弱める。閉鎖の結論は不変]
- **Hargé (2004) の看板定理は「$f$ 対数凹・$g$ 凸 $\Rightarrow\mathrm{Cov}\le0$」で向きが逆**である。
  すなわちこの経路は**符号中立**で、仮定の向き次第で Q3 の両側に振れる。
  **閉じたことをどちらのバケットの証拠にもできない。**
- **Royen (2014) の GCI も系として閉鎖**（稿 55_ 系 55-3）。関数形は「両者が準凹かつ偶 $\Rightarrow\mathrm{Cov}\ge0$」。
- 照合は二次文献 arXiv:2302.05208 Thm 1.1 経由で、**原論文 PDF は未取得**（`CITATIONS_PENDING.md`）。

**凹性の破れの量化（T1）**: 必要条件は「$W(0,\cdot)$ が負定値核」だが共分散なので不可能。
反跳位相は 2 次に効かず 4 次から効く。直線経路に制限すると $\Delta\ge0$ が厳密に成り立つ（＝反例は経路の揺らぎに宿る）。
破れは $\rho=-\lambda_{\min}/\lambda_{\max}=O(0.1\text{–}2.5)$ で**大域的**であり、$\Lambda$ を大きくしても解消しない。

**B19 に残る入口は 2 つだけになった**:

| 入口 | 状態 |
|---|---|
| ラウンド 3（$F_{\rm full}(u)\ge\frac{m^{\rm dip}_*}2|u|^2$、**N1 不要**） | 生存。壁は**系 54-3a / E05-F19 (a) そのもの**（$\inf$ を下から評価できない） |
| 参照測度を $\mu_{\rm dip}$ に替えたエントロピー | 生存・**未検討**。$`H(\mu_{\rm full}\|\mu_{\rm dip})=c\,\mathbb E_{\mu_{\rm full}}[\Delta]-\log\mathbb E_{\mu_{\rm dip}}[e^{c\Delta}]`$ と**$\Delta$ だけで閉じる**。発注 (研究ノート: `w139_mudip参照エントロピー.md`) |

**何が新しければ再挑戦可か**: **偶関数性を壊さずに凸性より弱い仮定で足りる相関不等式**。
現行の 3 つ（Hu・Hargé・Royen）はいずれも $\Delta\ge0$ 相当を要求するか向きが逆である。

**関連**: F26（B19 の 4 ラウンド）、命題 54-1（**本項の唯一の入力**）、E05-F19、REGISTRY **B19**。


## F28

**閉じた入口（B19 の残り 2 つのうち 1 つ。B19 本体はまだ未解決）**:
**参照測度を $\mu_{\rm dip}$ に替えた相対エントロピー $`H(\mu_{\rm full}\|\mu_{\rm dip})`$ から $D_\Lambda\ge b_\Lambda$ を出す。**
稿 `56_mudip参照エントロピー.md`（w139）。数値は (研究ノート: `106a_*`)（較正 4 本 PASS）・`106b_*`・`106c_*`・`106d_*`。

**障害は 2 段ある。2 段目の方が強い。**

**(1) 量的**: $`H(\mu_{\rm full}\|\mu_{\rm dip})/T`$ は $\Lambda$ 一様に有界でなく **$\Theta(\Lambda^3)$**
（$\alpha=1/137$ で局所冪 $3.80\to3.03$、5 段）。**参照測度を替えて落ちるのは共通の 1 ループ的寄与ではなく、
小さい方（フル側の $\Lambda^2$）だけである。** 双極子自身の $V_{\rm dip}=\Theta(T\Lambda^3/m^2)$ が
Cauchy–Schwarz $\mathrm{Var}(\Delta)\ge(\sqrt{V_{\rm dip}}-\sqrt{V_{\rm full}})^2$ でほぼ丸ごと残る（骨格は E05-F6）。
律速は $-\log\mathbb E_{\mu_{\rm dip}}[e^{c\Delta}]$ で、その 98% が双極子自身の寄与。
窓は参照 $\mathbb W$ の $141$ から $\mu_{\rm dip}$ の $154$ へ **9% しか広がらない**。

**(2) 構造的（こちらが本体。命題 56-2）**: **相対エントロピーからは $\beta_\Lambda$ の有用な上界が原理的に出ない。**
$H$ は**示量的**（$H\propto T$）なので Cauchy–Schwarz は $\sqrt m\beta_\Lambda\le\sqrt{2H/3}$ しか与えず、
$\sqrt{2H/(3T)}$ ではない。$D_\Lambda=\lim_{T\to\infty}R(T)/3T$ が定義そのものなので、
**この不等式は $H/T$ の大小に依らず空虚である。$\Lambda$ にも依らない。**

**内部訂正（重要。親の作業にも波及した）**: 稿 54_ §6.2 の要求「$H/T\lt3/2$」は **「$H\lt3/2$」（全時間・示量量）の誤り**。
$`\|\int_0^Tb\|\le\sqrt{2H/m}`$ は一般に偽（定数ドリフトで $T|b_0|\gt\sqrt T|b_0|$）。
**命題 52-4 自身は $\beta_\Lambda$ だけで述べられ $H$ を含まないので無傷**で、壊れていたのは §6.2 の接続だけである。
**したがって「$\Lambda\lesssim141$ ならエントロピー経路が使える」という読みは成立しない**
（数値 141・14.9 自体は正しく (研究ノート: `106d_*`) が再現した。誤っていたのは「使える窓」という解釈で、
これは親が (研究ノート: `104_*`) の verdict に書いてしまっていた。**T39**）。

**E05-F19 との関係**: 厳密には**別の壁**（示量性 vs $\sqrt T$）だが、**結果として F19 の一般則が回復する**。
三角不等式は「$D$ を下から押さえる唯一の例外」に見えていたが、例外に見せていたのは §6.2 の $\sqrt T$ の取り落としで、
「有限窓に切る」という修理も 系 54-3a (a) が直接塞ぐ。

**何が新しければ再挑戦可か**: **示量的でない情報源**。相対エントロピー・自由エネルギー差など $T$ に比例する量からは
$\beta$ の $T$ 一様な上界が出ない。$T$ について $O(\sqrt T)$ 以下で増える量が要る。

**B19 に残る入口は 1 つだけになった**: **ラウンド 3**（$F_{\rm full}(u)\ge\frac{m^{\rm dip}_*}2|u|^2$。定数は既知で
**循環せず、N1 も不要**）。壁は **E05-F19 (a)** そのもの（$\inf$ を下から評価できない）。
w139 の回避案は Legendre 双対を使うもの 1 件だが、**向きは未確認**である。

**関連**: F26・F27（B19 の他の入口）、命題 54-1（稿 55_ と本稿で 2 つの半分がそれぞれ使われ、
audit58 §6.3 の優先順位表の 1 位・3 位・5 位を単独で閉じた）、E05-F6・F19、REGISTRY **B19**。


## F29

**閉じた入口（B19 の 5 番目＝最後）**: **ハミルトニアン側の 2 次下界（ラウンド 3）**
$F_{\rm full}(u)\ge\frac{m^{\rm dip}_*}2|u|^2$（$m^{\rm dip}_*=m\frac{h_{\rm dip}}{h_{\rm dip}-1}$ は既知定数）。
稿 `57_ラウンド3_ハミルトニアン側.md`（w140）。数値は (研究ノート: `107_*`)（較正 PASS、最大相対誤差 $5.8\times10^{-14}$）。

**この経路は「循環しない」「N1 を要さない」という 2 つの利点を持ち、B19 で唯一残っていた入口だった。**

**障害**: **制約付き $\inf$ を下から評価する既知手段が 18 件中 0 件**（稿 57_ §4.3 の T1〜T18）。
内訳は **α 向きが逆 5 件／β 同語反復 4 件／γ 既閉鎖（F4・F6）3 件／δ 厳密に偽・原理的に不能 5 件**。
とくに**最も自然な作用素不等式 $`H(0)-E(0)\ge\frac{m^{\rm dip}_*}2\|v\|^2`$ は大域形を含意して厳密に偽**であり、
模型の構造そのものに塞がれている。

**本ラウンドで確定した新事実（B19 の外にも効く。3 件）**:

1. **標的の大域形は厳密に偽**（命題 57-1）。フル PF の励起エネルギーには**光子放出の天井
   $\mathcal E_{\rm full}\le\min(\frac{P^2}{2m},|P|)$** があるが、双極子の $\mathcal E_{\rm dip}=\frac{p^2}{2mh_{\rm dip}}$ は
   上に有界でないので、$|P|\gt2mh_{\rm dip}$ で比較が**逆転**する。破れは切断より下で始まる
   （$|P|_{\rm cross}/\Lambda\to\frac{8\alpha}{3\pi}$）。**正しい標的は局所形（$P\to0$ の曲率）だけである。**
   → **今後「双極子で下から支配する」型の提案は、まず天井に当てて量化子を確認すること。**
   **親の発注文 w140 は大域形で標的を書いていた（T40）。**
2. **Legendre 双対で E05-F19 (a) は回避できない**（命題 57-4）。**順序反転の対合は「$\inf$ の下界」を
   「$\sup$ の上界」に写すだけ**で、どちらも変分的に安い側ではない。**この 1 行で同型の提案を 1 手で殺せる。**
   w139 が残した回避案は符号が逆だった（稿 56_ が $P^2/2m$ を落としていた）。
3. **E05-F9（B13）の再演ではなかった**（命題 57-2）。F9 は $|P|\ge\Lambda$ の線形下界で要求/天井 $\to\infty$、
   本項は $P\to0$ の 2 次下界で要求/天井 $=1/h_{\rm dip}\to0$。**比の向きが逆**で、F9 の datum は流用もできない。
   → **「天井に当たる」型の kill-check は $|P|$ の領域を明示してから当てること。**

**縮退検査**: 落ちるのは **(ii) 計算可能性のみ**。(i) 盲目型でも不動点でもない（入力は既知定数）。
**主張 $h_{\rm full}\le h_{\rm dip}$ 自体は縮退していないし、偽と判定されたわけでもない。**
示量性の検査（T39 の再発防止）も通した（両辺とも 1 電子エネルギーで示量量ではない）。

**⟹ B19 は閉鎖**（REGISTRY 参照）。**閉じたのは実装の在庫であって命題の真偽ではない。**
再挑戦条件 5 項は REGISTRY の B19 に量化子つきで記載した。

**関連**: F26・F27・F28（B19 の他の入口）、**E05-F19**（単一の原因）、E05-F9、REGISTRY **B19**。

---

## F30 【格下げ 2026-09-11 / audit59。**閉鎖ではない**】

> ⚠ **【封印 2026-09-11 / audit59】本項の「閉鎖」判定は撤回された。** 変分下界は
> $\sup_\varphi M_\varphi=M$（Cauchy–Schwarz の等号、最適化子 $\varphi_*=(H(0)-E_0)^{-1}Qv_1\psi_0$）で
> **飽和する**ので、この経路には**原理的障害が存在しない**。
> **残る唯一の障害は計算可能性**（$\varphi_*$ が未知の $\psi_0$ を含む）。
> **以下の本文は「$\inf_\Lambda\varepsilon\gt0$ の試行族では不能」に格下げされた記述として読むこと。**
> **「原理的に不能」と引用してはならない。** 出典: (研究ノート: `58_Q3否定側_audit59_2026-09-11.md`) (R2) K-1。

**（格下げ後の正しい言明）** 変分下界 $h\ge[1-\frac2{3m}M_\varphi]^{-1}$ で欠損率を
$\varepsilon:=1-M_\varphi/M$ と置くと得られる下界は $[\varepsilon+(1-\varepsilon)/h]^{-1}\le1/\varepsilon$ であり、
**$h\gtrsim\lambda$ には $\varepsilon(\Lambda)=O(1/\lambda)$ が必要十分**。$\inf_\Lambda\varepsilon\gt0$ の族では頭打ち。
**しかしこれは原理的障害ではない**: (i) 各 $\Lambda$ で $\varepsilon=0$ の最適化子が存在する。
(ii) **B16 は $\varepsilon$ が $\Lambda$ 定数でない実例**で、$L\propto\alpha^2\sqrt\lambda$ の増大とともに
$\varepsilon\to0$ する（稿 36_ 命題W119-4、audit59 (R3) の 3 択判定 **(b)**）。
(iii) $N$ 本の明示基底で $\varepsilon_N$ は $\Lambda$ に依らず減少する（(研究ノート: `110_audit59_epsilon_family.py`)）。

**以下は 2026-09-11 に w141 が「閉鎖」として書いた原文（歴史的記録）である。**

**~~変分（試行状態）による $h\gtrsim\lambda$ の証明 — 欠損率が $\Lambda$ について定数である限り閉鎖。
$\lambda$ の冪ではなく「天井への相対精度 $1/\lambda$」が壁である~~**

出所: 稿 `58_Q3否定側の設計.md` §4.3 命題 58-2（w141、2026-09-11、`self-audited`）。
発注: (研究ノート: `w141_Q3否定側の設計.md`)。実験: (研究ノート: `108_negative_side_variational_bound.py`)
（較正 **PASS**: 双極子 $\frac{4\alpha}{3\pi}\lambda$ 相対誤差 $0$、1 ループ $\frac{8\alpha}{3\pi}\ln(1+\lambda/2)$ 相対誤差 $\le2.4\times10^{-15}$）。

**⚠ 閉鎖するのは「$h\gtrsim\lambda$ を変分で示す」という到達目標であって、変分経路そのものではない。**
**同じ経路で $h\ge1+c\alpha^2\sqrt\lambda$ を狙うことは閉鎖しない**（そちらは kill-check を通過した。REGISTRY の新経路 B20）。

### 正確な障害

$M$ を $P=0$ での静的感受率（$\frac2{3m}M=1-\frac1h$、**厳密**）とする。試行族から得られる下界 $M_\varphi$ の
欠損率を $\varepsilon:=1-M_\varphi/M$ と置くと、得られる $h$ の下界は
```math
h\ \ge\ \Bigl[1-\tfrac2{3m}M_\varphi\Bigr]^{-1}=\frac{1}{\varepsilon+(1-\varepsilon)/h}\ \le\ \frac1\varepsilon .
```
**$\varepsilon$ が $\Lambda$ について定数である限り、$h$ の下界は $1/\varepsilon$ という定数で頭打ちになる。**
$h\ge c\lambda$ を出すには $M$ を天井 $\frac{3m}2$ に相対精度 $O(1/(c\lambda))$ で迫らせる必要があり、
すなわち**試行族の欠損率 $\varepsilon(\Lambda)$ 自身が $O(1/\lambda)$ で消えねばならない。**

~~**これは E05-F19 の否定側での対応物である。** 肯定側の壁は「向きが原理的に取れない」であり、
否定側の壁は「向きは無料だが、Q3 を決める閾値だけが天井への相対精度 $1/\lambda$ を要求する」である。~~
**【撤回 2026-09-11 audit59】E05-F19 との対応は成り立たない。** F19 は**原理的**な向きの障害だが、
こちらは**計算可能性**の障害にすぎない。**この 2 つを対にして語ってはならない。**

### 実測（(研究ノート: `108_*`)。$\alpha$ と $\Lambda$ を列に持つ）

1 光子セクター（厳密なレゾルベント）と 2 光子背中合わせ対セクターの両方を足しても

| $\alpha$ | $\Lambda$ | $\frac2{3m}(M^{(1)}+M^{(2)})$ | 必要水準 $1-1/\lambda$ | 不足 |
|---:|---:|---:|---:|---:|
| $1/137$ | $3\times10^5$ | $4.9\times10^{-2}$ | $0.999997$ | $0.95$ |
| $0.1$ | $3\times10^5$ | $0.81$ | $0.999997$ | $0.19$ |

**桁で足りない。** しかも $\alpha=1$ の行は $\frac2{3m}M\gt1$ となるが、これは**摂動評価の破綻**（E05-L4）であって
終端の証拠ではない。**引用禁止。**

### 再挑戦の条件（量化子つき）

**$\Lambda$ に依存する試行族 $`\{\varphi_j(\Lambda)\}`$ で、欠損率 $\varepsilon(\Lambda)=1-M_\varphi/M$ が
$`\limsup_{\Lambda\to\infty}\lambda\,\varepsilon(\Lambda)\lt\infty`$ を満たすものを構成できたとき**に限り再挑戦してよい。
「殻を増やす」「光子数を増やす」だけでは足りない（各 $\Lambda$ で有限の欠損が残る限り $\varepsilon$ は定数のまま）。
**$\varepsilon(\Lambda)\to0$ の速さを $\lambda$ の言葉で見積もった 1 行を発注文に必ず書くこと。**

### 踏んでいない落とし穴（記録）

- **F2 とは別物である。** F2 が閉じたのはコヒーレント（Weyl）試行族、すなわち $\varphi$ を $\psi_0$ から作らない族で、
  $P=0$ での変分欠損 $\delta\gt0$ が $\mathcal E(P)\le\delta+cP^2$ を作って $P^2$ の係数が読めなくなるものである
  （公理表の罠「変分欠損のある試行族は無情報」）。本項の族は $\psi=\psi_0+t\varphi$ で $t=0$ の欠損がゼロなので**この罠は踏まない**。
  それでも命題 58-2 で落ちる、というのが本項の内容である。
- **E05-F18（非増幅）とも別物である。** F18 は変分**下界**から $h$ の**上界**を作る経路の制約で、本項は逆向き。
- **「双極子で等号」は棄却理由にしていない**（E05-F18・T37）。棄却根拠は縮退検査の **(ii) 計算可能性**のみ。

---

## F31 「B20 の残る障害は真空重なり $Z=|\langle\Omega,\psi_0\rangle|$ の $\Lambda$ 一様下界である」という定式化

閉じた日: 2026-09-11（w142、稿 `59_Zの一様下界.md` 命題 59-1、`self-audited`）。出所: 稿 `58_` §5。

**閉じた主張**: 対セクターの試行 $\varphi=b\psi_0$（$b=a^*(f)a^*(g)$）について
$M_\varphi=3|N|^2/D$ の分子が $\psi_0$ の 2 光子振幅を要求し、それが $Z$ の $\Lambda$ 一様下界に帰着する。

**正確な障害（＝なぜ誤りか）**: $\psi_0=Z\Psi$（$\Psi$ は真空成分の係数 1）と置くと恒等的に
$N=Z^2\widetilde N$・$D=Z^2\widetilde D$ で $M_\varphi=Z^2\cdot3\widetilde N^2/\widetilde D$ だが、$`\|\Psi\|^2=Z^{-2}`$ なので
$\widetilde N,\widetilde D$ が同じ桁で発散し **$Z^2$ は相殺する**。$M_\varphi$ に実際に現れるのは Fock 2 光子成分 $\psi_0^{(2)}$ ではなく
**規格化された基底状態の異常 2 点関数 $\langle\psi_0,a(g)a(f)\psi_0\rangle$** であり、これは $Z\to0$ でも消えない。
可解模型（(研究ノート: `109_Z_power_counting_killcheck.py`)、較正 3 本 PASS）で、$Z^2$ が 1 桁動く間に $M/Z^2$ が 12 桁動き、
Fock 成分が減少する一方で異常 2 点関数が単調増大することを実測した。

**含意**: $Z$ の下界を追う発注をしてはならない。稿 58_ §5 の「残る唯一の技術的障害」は無効
（同稿の命題 58-1・58-2 と §4.1 の枠組みには影響しない）。なお発注文 (T0) の判定基準
（双極子閉形式で $Z^2\delta=\frac u2e^{-u}\to0$、$u=\frac{\alpha^2}\pi\sqrt\lambda$）は前提が偽なので適用しない。

---

## F32 rank-1 総和則（Bijl–Feynman）下界で $\delta=\frac{c_0}2\alpha^2\sqrt\lambda$ を $\Lambda$ 一様に出す
【**条件付き閉鎖**へ格下げ 2026-09-11 / audit60 (R3)】

> ⚠ **【格下げ 2026-09-11 / audit60】閉鎖そのものは維持するが、根拠を差し替える。**
> **稿 59_ の「交点は意味のある窓の内側にある」は $C_2=1$ という無根拠の代入に依存する。**
> $\lambda_\times\propto C_2^{28/15}$ で、$\alpha=0.1$ では **$C_2\gt5.9$ だけで窓の外に出る**（(研究ノート: `111_*`) T2）。
> **閉鎖を述べるときは窓を経由せず、下の $\lambda^{-4/7}$ の形で述べること。**
> 依存しているのは **$S$ の主要項の下界**であって上界ではない。以下が差し替え後の正しい本文である。

rank-1 総和則（Bijl–Feynman）下界で $\delta=\frac{c_0}2\alpha^2\sqrt\lambda$ を $\Lambda$ 一様に出す

**⚠ 既存 F32 の格下げ。新規採番ではなく F32 の本文を差し替える場合はこの節を使うこと。**

- **閉じた主張**: 命題 59-2 の rank-1 下界 $1-\frac1h\ge\frac{2\langle v_1^2\rangle^2}{mS}$（$\varphi=v_1\psi_0$）で
  $\delta$ を $\Lambda$ 一様に出す。
- **正確な障害**: フル PF では $S\simeq\frac{2\alpha\Lambda^3}{9\pi}+\frac{\alpha\Lambda^4}{6\pi m}$ で**反跳項が支配**し
  （$S/S_{\rm dip}=1+\frac{3\lambda}4$）、E05-L4 の天井 $E_0\lt C_2\alpha^{2/7}\Lambda^{12/7}$ を入れると
  **この下界が到達しうる最大値そのものが**
  $\frac{16\pi C_2^2}3m^{10/7}\alpha^{-3/7}\lambda^{-4/7}\to0$ **で消える**
  （数値の傾き $-0.571428$ vs $-\frac47$。(研究ノート: `111_audit60_rank1_ceiling.py`) T4）。
  $\delta$ どころか**任意の定数**すら $\Lambda$ 一様には出せない。
- **格付け: 条件付き閉鎖（`self-audited` + 独立監査の条件つき確認）。** 依存しているのは
  **$S$ の主要項の下界**であって上界ではない。残る留保 2 件:
  (i) 符号不定項（worklog A8）は交点で主要項の **63%** に達し「劣位」ではない。最悪の符号でも交点は
  約 2 倍動くだけで窓の内側に留まる（`111_*` T3）。
  (ii) スクイズ（A9）は向きが有利（$`\|Y_{j1}\psi_0\|^2=\langle\Pi_g^2\rangle`$ は $A^2$ 項で anti-squeeze される）。
  逆向きの最悪ケースを潰すには $\langle N\rangle\gtrsim\lambda^{15/7}$ が要り非現実的。
- **⚠ 稿 59_ の「交点は意味のある窓の内側にある」は $C_2=1$ という無根拠の代入に依存する。**
  $\lambda_\times\propto C_2^{28/15}$ で、$\alpha=0.1$ では **$C_2\gt5.9$ で窓の外に出る**（`111_*` T2）。
  **閉鎖を述べるときは窓を経由せず、上の $\lambda^{-4/7}$ の形で述べること。**
- **閉じていないもの**: 真の $M=3\sum_nw_n/\omega_n$ は rank-1 下界よりいくらでも大きくなりうる。
  B20 全体は閉じていない（**F33** の 1 本目を参照）。
  **【2026-09-11 追記】B20 本体はその後 F34（w143 + audit61）で条件付き閉鎖になった。**
- 出所: 稿 `59_Zの一様下界.md` 命題 59-3（w142）+ (研究ノート: `59_Zの一様下界_audit60_2026-09-11.md`) (R3)。

---

**以下は 2026-09-11 に w142 が書いた原文（歴史的記録。窓の議論は上のとおり無根拠）。**

閉じた日: 2026-09-11（w142、稿 `59_Zの一様下界.md` 命題 59-3、`self-audited`。**leading-order 評価に依存**）。

**閉じた主張**: 無条件下界 $1-\frac1h\ge\frac{2\langle v_1^2\rangle^2}{mS}$（$\langle v_1^2\rangle=\frac{2m}3(E_0-\Theta)$、
$S=\frac12\langle[v_1,[H,v_1]]\rangle$。$Z$ も試行関数も使わない。命題 59-2、無条件）で $h\ge1+c\alpha^2\sqrt\lambda$ を示す。

**正確な障害**: フル PF の $S$ は**反跳支配**で $S\simeq\frac{2\alpha\Lambda^3}{9\pi}+\frac{\alpha\Lambda^4}{6\pi m}$
（$S/S_{\rm dip}\simeq1+\frac{3\lambda}4$。$v_1\psi_0$ は運動量 $k$ の光子 1 個を足した状態でその励起エネルギーが $\omega_k+\frac{k^2}{2m}$）。
このため必要量 $(E_0-\Theta)_{\rm req}=\frac32\sqrt{\delta S/2}\propto\alpha^{3/2}\lambda^{9/4}$ が、
E05-L4 の上界 $E_0-\Theta\le E_0\lt C_2\alpha^{2/7}\Lambda^{12/7}$（$\Theta\ge0$）に対して比
$\propto\alpha^{17/14}\lambda^{15/28}\to\infty$ となり、**交点が意味のある窓（$\delta\lt1$、$\lambda\lt4\pi^2/\alpha^4$）の内側**に来る
（$\alpha=1/137$: $\lambda_\times=5.4\times10^6$ vs 窓 $1.4\times10^{10}$。$\alpha=0.1$: $1.4\times10^4$ vs $3.9\times10^5$）。
(研究ノート: `109c_fsum_recoil_and_requirement.py`)（角度・動径積分の較正 4 本 PASS）。

**閉じていないもの（射程の明示）**: B20 本体（対セクター変分）は閉じていない。真の
$M=3\sum_nw_n/\omega_n$ は rank-1 下界よりいくらでも大きくなりうる。
また本判定は $S$ の主要項評価に依存し、符号不定の劣位項とスクイズ（$`\|Y_{j1}\psi_0\|^2`$ の下界）は
桁の見積りで処理している（稿 59_ 「仮定」、worklog §6 A8・A9）。**S2 監査を要する。**

**副産物（記録のみ、Q3 には無力）**: 命題 59-2 と $h\lt\infty$（E05-F3）から無条件の a priori 不等式
$\langle v^2\rangle=2m(E_0-\Theta)\lt3\sqrt{mS/2}$。向きが逆なので否定側には使えない。

---

## F33 B20-d — 「硬い光子 ⟹ 分母に反跳 / 軟光子 ⟹ $\sqrt\lambda$ の材料なし」の二律背反で B20 を閉じる

- **閉じた主張**: 稿 `59_Zの一様下界.md` §4 の提案。「$\sqrt\lambda$ の材料は硬い 2 光子にしか無く、
  硬い光子を試行に使えば分母に反跳 $\frac{k^2}{2m}\sim\frac{\Lambda\lambda}2$ が**必ず**付く。軟光子に移せば
  $\sqrt\lambda$ の材料が無い。ゆえに B20（否定側の変分下界枝）全体が閉じる」。
  REGISTRY に「成立すれば B20 全体が閉じる」経路候補として登録されていた。
- **正確な障害（3 点。いずれも既存の台帳だけで殺せる）**:
  1. **前提が E05-F7（`verifier-backed`）と矛盾する。** 2 光子状態 $a^*(k)a^*(k')\psi_0$ の分母に入る電子の反跳は
     **総運動量で決まる $\frac{(k+k')^2}{2m}$** であって $\frac{k^2}{2m}$ ではない。E05-F7 は
     「反跳の抑制は総運動量 $k+k'$ のみで決まり、**背中合わせ対は免れる**」と述べており、
     $k'\simeq-k$ の対では反跳はほぼ 0、分母は $\omega_k+\omega_{k'}\simeq2\Lambda$ に留まる。
     **しかも $\sqrt\lambda$ の材料はまさにその背中合わせ対にある**（E05-F6・F7、稿 27_）。
  2. **実測の反例が既に台帳にある。** 稿 58_ §4.2 の kill-check は反跳込み（1 ループ較正が E05-F1 に一致）で
     対セクター試行ベクトルが $\frac2{3m}M^{(2)}\to\frac{c_0}2\alpha^2\sqrt\lambda=\delta$ を生むことを示し、
     「対セクターの試行ベクトルは $\sqrt\lambda$ を確かに生む」と判定している
     （~~捕捉率 $\frac12$~~ → **【訂正 2026-09-11 / w143・稿 60_、audit61 (R1) が PASS】捕捉率は厳密に 1**。
     同種ボソン対の Wick 因子 2 が旧稿の前因子で落ちていた。**F33 の棄却判定は変わらない**
     — 捕捉率が上がることは「対セクターは $\sqrt\lambda$ を生む」という根拠を**強める**方向である。
     ただし **audit61 (R2) により捕捉率 1 は $O(e^4)$ での同語反復で、$\Lambda$ 一様性には無情報**）。
  3. **無制限形は踏み台にならない。** 「すべての試行族が $\delta$ に届かない」と読むと、E05-F21
     （$\sup_\varphi M_\varphi=M$）により **Q3 の $\sqrt\lambda$ 問題の否定そのものと同値**になる。
     補題サイズの中間目標ではなく問題全体であり、未証明の予想を経路の状態として登録していたことになる
     （math-research §4）。
- **誤りの由来**: 命題 59-3 で死んだのは **rank-1（1 光子的）**の選択 $\varphi=v_1\psi_0$ である。
  1 光子なら総運動量 $=k$ なので反跳 $\frac{k^2}{2m}$ が確かに付く。**稿はこの rank-1 の失敗を全試行族に一般化した。**
  E05-F7 は稿 59_ 自身の 仮定 節に挙げられており、内部矛盾である。
- **生き残る形**: 「$\varphi=v_1\psi_0$ の rank-1 族に限れば反跳が分母を支配して $\delta$ に届かない」
  ＝ **命題 59-3 そのもの**。新規の内容は無い。
- **判定**: 棄却。**この二律背反を追う発注をしてはならない。**
  対セクター（背中合わせ対）を使う枝は反跳で死なないので、B20 は依然として未解決である。
- 出所: (研究ノート: `59_Zの一様下界_audit60_2026-09-11.md`) (R4)、2026-09-11、audit60（Opus, effort=high）。

---

## F34 B20 の naive 形 $\Lambda$ 一様標的 — 「$\sigma$ の $\Lambda$ 一様下界（＋分母の一様上界）で B20 が閉じる」

> **【親の注記 2026-09-11】本項は独立監査 audit61（S2）を通したうえで連結している。**
> **audit61 の判定**: 中心の算術（Wick 因子 2、捕捉率 1）は **PASS**。ただし
> **(i)「捕捉率 1」は $O(e^4)$ での同語反復で $\Lambda$ 一様性には無情報**、
> **(ii) 閉鎖の理由「naive 形が偽 ⟹ 閉鎖」は non sequitur**（$Z$ の前例 F31 と同型）。
> 正しい閉鎖理由は **(a) 枠組みが飽和して改良余地が構造的に無い（E05-F21）／
> (b) 残る飽和形が目標 $h\ge1+c\alpha^2\sqrt\lambda$ と同値で還元が起きていない／(c) 3 ラウンド無収穫**。
> **B20 に数学的障害は存在しない。** 再挑戦条件は道具条件 **(RC1′)** に書き直した。
> 処方 P-A〜P-M は適用済み（(研究ノート: `patch62.適用記録.md`)、取り残し 6 件は親が処理）。


- **閉じた主張**: 稿 `58_Q3否定側の設計.md` §5 系列と 発注 `w143` が想定していた定式化。
  対試行族 $\varphi=b\psi_0$（$`b=\iint\tilde\beta\,a^*a^*`$）の
  $M_\varphi=\frac{3|N|^2}{D}$、$N=\langle\psi_0,b^*v_1\psi_0\rangle$、$D=\langle\psi_0,b^*[H,b]\psi_0\rangle$ について、
  最低次の値 $N_0,D_0$ と比べる 2 つの $\Lambda$ 一様評価
  **(U1)** $|N|\ge c_1|N_0|$（＝背中合わせ帯上での異常 2 点関数 $\sigma(k,k')=\langle\psi_0,a(k')a(k)\psi_0\rangle$ の
  $\Lambda$ 一様下界）と **(U2)** $D\le C_2D_0$ を取れば
  $h\ge1+c\alpha^2\sqrt\lambda$ が出る、という見立て。
- **正確な障害（初等・無条件）**: **対試行族 $`\{\varphi_\Lambda\}`$ が $\liminf_{\Lambda\to\infty}\frac{3|N_0(\Lambda)|^2}{D_0(\Lambda)}=\infty$ を満たすならば、(U1) と (U2) が $\Lambda$ 一様な定数 $c_1,C_2$ で同時に成り立つことはない（命題 60-2′）。**
  2 つから $\frac2{3m}M_\varphi\ge\frac{c_1^2}{C_2}\cdot\frac{2}{3m}\cdot\frac{3|N_0|^2}{D_0}\to\frac{c_1^2}{C_2}c_0\alpha^2\sqrt\lambda$
  が従う（最低次の最適化と稿 `60_` 命題 60-1）。一方 $h\ge1$（**E05-F3**、無条件）より
  ```math
  \frac2{3m}M_\varphi\ \le\ \frac2{3m}M\ =\ 1-\frac1h\ \lt\ 1
  ```
  も無条件である。$c_1,C_2$ が $\Lambda$ 一様なら左辺は $\lambda\to\infty$ で発散するので矛盾。
  **破綻は $\lambda\sim\alpha^{-4}$ で起きる**（対凝縮 $`\|\beta_0\|_{HS}^2=\frac{\alpha^2}\pi\sqrt\lambda`$ が $O(1)$ になる位置と
  同じオーダー。**係数がともに $\frac1\pi$ で一致するのは偶然であり、構造的一致と読んではならない** — 公理表の警告）。
- **これは「証明できていない」ではなく「主張が偽」である。**
  したがって **「$\sigma$ の $\Lambda$ 一様下界さえ取れれば B20 が閉じる」型の発注をしてはならない。**
- **どちらが劣化するかも決着している**（稿 `60_` 観察 60-3、(研究ノート: `112b_*`)）:
  厳密可解な双極子（$V=0$ で $p$ が c 数なので場について厳密に 2 次形式）では
  naive 評価（自由真空・自由エネルギー分母）は厳密値を**因子 $h$ だけ過大評価**し
  （$\gamma^TK^{-1}\gamma/\gamma^T\Omega^{-1}\gamma=\frac1{1+G}=\frac1h$、$K=\Omega+\frac{\gamma\gamma^T}m$、Woodbury、機械精度）、
  その劣化は**分子と分母の両方**に乗る（$G$ 大で分子 $\sim G^{-1/2}$、分母 $\sim G^{+1/2}$）。
  **ゆえに (U1) を非摂動的に取れたとしても標的には届かない**（根拠は命題 60-2′ そのもの: (U1) が成り立つなら (U2) が破れる、すなわち $D/D_0\to\infty$ が強制される。**観察 60-3 は「どちらがどう劣化するか」の機構の候補であって、この結論の根拠ではない** — 稿自身が未証明・2 実例と格付けしている。audit61 (R5)(a)）。
- **生き残る形（B20 の再挑戦条件。量化子つき）**: 飽和形
  ```math
  \exists c\gt0,\exists\alpha_0\gt0:\ \forall m\gt0,\forall\alpha\in(0,\alpha_0],\forall\Lambda\gt0,\exists\varphi_\Lambda:\quad
  \frac2{3m}M_{\varphi_\Lambda}\ \ge\ \frac X{1+X},\qquad X=c\,\alpha^2\sqrt{\Lambda/m}
  ```
  （$P\to0$ を $\Lambda\to\infty$ より先に取る）。これは $h\ge1+c\alpha^2\sqrt\lambda$ と同値で天井と両立し、
  **双極子では Woodbury により真**である。ただしフル PF（反跳込み、$P_f$ が作用素）での証明手段は現時点で無い。
  同値性より、この標的は欠損率について**必要条件** $\varepsilon(\Lambda)=1-M_\varphi/M\lt\frac1{1+X}\le C/(\alpha^2\sqrt\lambda)$
  **を課す**（audit61 (R4)(b) が独立検算。$1-\frac1h\lt1$ だけから出るので $h$ の真値を要しない。**十分条件ではない**）（命題 58-2 の精度階段の $\sqrt\lambda$ 版。**稿 58_ §4.4 が $\sqrt\lambda$ 標的を
  「精度を要さない」側に分類していたのは誤り**）。
- **判定**: 棄却（naive 形）。**B20 本体は条件付き閉鎖。** 出所: 稿 `60_対セクターのΛ一様性.md` 命題 60-2、
  2026-09-11、w143（Opus, effort=high）。格付け `self-audited`（未監査。再監査等級 S2）。

---

## F35 「B16 の律速は $\eta$（符号不定残差）であり、その $\Lambda$ 一様な上界を取れば B16 が動く」

**棄却する主張**: 「B16 の律速は $\eta$ に移った。$\eta$（$\mathcal E_A$ と密度型 4 次ブロックの
$D_{\rm free}$ に対する相対サイズ）の $\Lambda$ 一様な上界を取れば B16 が進む」
（稿 `36_` §8 冒頭と残タスク 1 末尾の優先度付け、発注 (研究ノート: `w144_B16の律速ηの上界.md`) の前提）。

**⚠ 棄却するのは上の「優先度付け」だけである。B16 という経路そのものは閉じない**
（audit62、2026-09-11。稿 `61_` が提出した「B16 の条件付き閉鎖」は**却下**された。理由は
(研究ノート: `61_B16の律速η_audit62_2026-09-11.md`) の (R1)〜(R4)）。

**正確な障害（$\eta$ 単独では足りない理由。1 本）**

$\eta$ は天井側（36_ 命題W119-4 の $f_{\rm ceil}=\frac{1+L/2-\eta}{1-L/2-\eta}$、$\partial_\eta\gt0$）と
道具側（$f_{\rm out}=\frac{1+\varepsilon^{\rm ub}_{\rm pair}+\eta}{1+\varepsilon^{\rm ub}_{\rm pair}+\eta-L}$、$\partial_\eta\lt0$）に
符号が逆に入る。$\eta$ を完全に $0$ にしても到達点は
```math
h-1\ \ge\ \frac{L}{1+\varepsilon^{\rm pair}_{\rm ub}}
```
に留まり、**現有の対型上界 $\varepsilon^{\rm pair}_{\rm ub}=\mathcal N=\langle N_S(N_S-1)\rangle_0$
（31_ 命題U4-2 を経由する限り）が真値 $\varepsilon_{\rm res}=L/2$ の $88$ 倍緩い**ので、
$\lambda\to\infty$ で $h-1$ は定数 $1/44.1$ に飽和して増大しない。
**ゆえに「$\eta$ さえ取れれば B16 が動く」は偽である。**

**この障害の測り方（稿 `61_` 命題 61-1・61-2、audit62 が独立再導出して PASS）**

**すべての** $\Lambda\gt0$ と**すべての**許容核 $\beta\in\mathcal B_\Lambda$（36_ §1）に対し
```math
\sqrt{L[\beta]}\ \le\ \sqrt{\mathcal N}+\delta,\qquad
\text{（31\_ 命題U4-2 を経由するとき）}\ \ \varepsilon^{\rm pair}_{\rm ub}=\mathcal N .
```
**分子 $L$ と、現存する唯一の対型分母上界が、同じ量 $\mathcal N$ に支配される。**
1 ループ求積で $\mathcal N/L_{\max}=44.1$、真値 $L/2$ に対する緩みは $88.3$ 倍
（(研究ノート: `114_*`)、audit62 の独立再実装 (研究ノート: `115_*`) が 5〜6 桁で再現）。

**⚠ 過大読みの禁止（audit62 が明示を要求した 5 点）**

1. **$\varepsilon^{\rm pair}_{\rm ub}\ge\mathcal N$ を「すべての妥当な上界について」と書いてはならない。**
   真値 $\varepsilon_{\rm res}=L/2=\mathcal N/88$ 自身が妥当な上界であり、その量化子は**偽**である。
   正しくは「**31_ 命題U4-2 を経由する限り** $\varepsilon^{\rm pair}_{\rm ub}=\mathcal N$」。
2. **$h_{\rm B16}\le1+\mathcal N$ は $\lambda$ 一様な kill ではない**（$\mathcal N\to\infty$ で空虚化）。
3. **「$\eta$ の改良は無駄」ではない。** $\partial_\eta f_{\rm out}\lt0$ なので $\eta$ の改良は単調に効く。
   言えるのは「$\eta$ **だけ**では足りない」である。
4. **要求精度は $\eta=o(L)$ ではない。** 到達点 $h-1\ge\frac{L}{1+\varepsilon^{\rm pair}_{\rm ub}+\eta}$ が
   $\asymp L$ になる条件は $\varepsilon^{\rm pair}_{\rm ub}+\eta=O(1)$、すなわち **$\eta=O(1)$** である。
   現有の $\eta$ 上界（30_ §2.4 の $Ce\alpha\lambda^{3/2}\varsigma$）との乖離は $\lambda^{3/2}$ であって $\lambda$ ではない。
   **かつ $\varsigma$（$\beta^*$ の拡がり因子）は 36_ 留保 U-w119-1 で未評価なので、乖離の冪も未確定である。**
5. **$\eta$ の**下界**は証明されていない**（36_ §3.3 が明記）。現有の上界が足りないことは、
   より良い上界が存在しないことを意味しない。**$\mathcal N$ の制御は `FAILED` の F8**
   （殻内 2 光子相関のモーメント法。**事実 `E05-F8` ではない。T48**）**で閉じているが、
   B16 は $\mathcal N$ を抑える必要がない**（下の (a) を取れば $\mathcal N$ は式から消える）。

**生き残る形（B16 で次にやるべきこと。道具条件。量化子つき）**

- **(a) 最優先。** 対型 4 次ブロックの上界を $\langle N_S(N_S-1)\rangle_0$ を**経由せずに**与える。
  定量目標: $\exists c\le1,\ \forall\Lambda>0,\ \forall\beta\in\mathcal B_\Lambda:\
  \frac1m\sum_\nu\|T^*_\nu\psi_0\|^2\le c\,L[\beta]\,D_{\rm free}[\beta]$。
  **現有は $c=\mathcal N/L_{\max}=44.1$、真値は 36_ 命題W119-3 より $c=\frac12$。**
  （$c\gt1$ では $h_{\rm B16}\to\frac{c}{c-1}$ の定数に飽和して増大しないので、$c\lt2$ では足りない。
  $c=1$ でちょうど $h\ge1+L$、$c\to\frac12$ で 36_ 命題W119-4 の天井に到達する。）
- **(a) への現存する具体策**: **36_ §8 残タスク 2 の補題 X1**（30_ 命題1 の等式で捨てている
  $\langle F^*\psi_0,(H-E)F^*\psi_0\rangle$ を回収して分母を鋭くする）。
  36_ が書いた kill-check（1 ループの $\psi_0$ で両辺を求積し比を見る。$\lambda$ 一様なら生存、
  $\lambda$ で減衰なら閉鎖）は **tier C0 で、まだ実行されていない**。**これを先にやること。**
- **(b) 従属。** $\eta$（$\mathcal E_A$ と密度型 4 次ブロック）の $\Lambda$ 一様な上界。目標は $\eta=O(1)$。
  (a) が取れるまでは単独で発注しない。

**したがって禁止される発注**: 「$\eta$ の $\Lambda$ 一様な上界さえ取れれば B16 が動く」型。
**推奨される発注**: 補題 X1 の kill-check → 結果次第で (a) の作用素不等式。

**出所**: 稿 `61_B16の律速η.md` 観察 61-3・命題 61-1・61-2、
監査 (研究ノート: `61_B16の律速η_audit62_2026-09-11.md`)（audit62、総合判定 **FAIL**）、
(研究ノート: `114_B16_reach_bound.py`)・(研究ノート: `115_audit62_pair_prefactor_recheck.py`)（ともに PASS）。
2026-09-11。格付け `verifier-backed`（棄却対象＝「$\eta$ が律速」の同定について）。

---



> **【親の注記 2026-09-11】射程の限定が守られている。** 閉じたのは **36_ §8 残タスク 2 が書いた
> 不等式 (X1) という定式化だけ**で、**$\varepsilon^{\rm pair}$ を $c\le1$ まで詰める (a) 枝も B16 も開**である
> （縮退検査の 2 根拠＝盲目型・計算可能性のどちらも得ていない）。
> **【副産物は決着済み 2026-09-11 / audit63】** 稿 62_ の観察 62-5 が報告した「$L_{\max}$ が $24\pi$ 食い違う」は
> **誤解であって誤りではなかった**: 36_ §4 は**殻 $S=[\Lambda/2,\Lambda]$・$q$ 窓 $|q|\le\sqrt{2m\Lambda}$ に
> 支持を制限した許容核族**での上限、稿 62_ はフルレンジ $(0,\Lambda]$ の**無制約** C–S 最適で、
> **異なる支持域の異なる量**だった（独立検算 (研究ノート: `117_*`) が両方を再現。36_ の値とは $0.0004\%$ 一致）。
> **B16 に関係するのは 36_ 側**（その議論は殻+窓許容核の上に立つ）。
> **⟹ REGISTRY の「88.3 倍／$\mathcal N/L_{\max}=44.1$」と 36_ 注意W119-5 の尺度 $\lambda\sim2.2\times10^5\alpha^{-4}$ は
> いずれも訂正不要で、確定値として引用してよい。**

## F36 — 補題 X1（二重交換子で捨てている項を差し引いて B16 の分母を鋭くする）

**閉じた主張**: 36_ §8 残タスク 2 の不等式
$`\langle F^*\psi_0,(H-E)F^*\psi_0\rangle\ \ge\ (1-o(1))\,\frac1m\sum_\nu\|T_\nu^*\psi_0\|^2`$。
（30_ 命題1 の等式で捨てている第 2 項が共鳴残余を丸ごと相殺し、$\varepsilon^{\rm pair}$ の上界を
$c\le1$ まで詰められる、という筋。）

**正確な障害**: **パリティ選択則が向きを反転させる。** $F^*\psi_0$ の真空成分は
$\langle\beta,\alpha_0\rangle_{HS}=0$（$\beta$ 奇 × $\alpha_0$ 偶、30_ 命題2。非摂動・全次数）。
36_ はこの 0 を「$(H-E)$ が非自明な下界を持ちうる」根拠にしたが、**同じ 0 が $`\|F^*\psi_0\|`$ を
$e$ の 2 乗ぶん削る**。対照的に $T_\nu$ の核 $q_\nu\beta$ は偶なので真空成分が残る。ゆえに
左辺 $=O(e^6)$、右辺 $=O(e^4)$ で、**1 ループでは左辺が恒等的に 0**。
$O(e^6)$ の直接項を求積すると比は $`\mathcal R_A=0.191\,\alpha\ln\lambda-0.46\,\alpha`$
（$\lambda=10^2\ldots10^6$ の 5 段階、最後の 2 段で傾き 6% 以内一致、$\lambda$ の冪なし）。
**摂動論の有効域の端（E05-L4、$\lambda=\alpha^{-5/2}=2.2\times10^5$）でも $\mathcal R_A=1.4\times10^{-2}$ で
要求値の 1/72。** $\mathcal R_A=1$ は $\lambda\sim10^{312}$ で摂動論の外。
一部だけ差し引く弱い版でも $\varepsilon_{\rm res}=L/2$（36_ 命題W119-3）は主要項で不変なので、
命題W119-4 の天井の形は変わらない。

**⚠ 閉じた範囲（量化子つき。過大に読まないこと）**: 閉じたのは**この不等式という定式化**だけ。
**「(a) 枝」（$\varepsilon^{\rm pair}$ の上界を $c\le1$ まで詰める目標。現有 $c=44.1$）は開いている。**
**B16 も開いている。** 縮退検査の 2 根拠（(i) 盲目型・(ii) 計算可能性）はどちらも得られていない。

**出典**: 稿 `62_補題X1.md`（命題 62-1〜系 62-4、`self-audited`、再監査等級 S2）、
(研究ノート: `2026-09-11_w145_補題X1.md`)、(研究ノート: `116_lemmaX1_killcheck.py`)。

---

## F37 混合作用素 $A=F+cT_\nu$（および殻に台を持つ対消滅作用素）で、30_ 命題1 が捨てる第 2 項を**回収**して分母を鋭くする — **族全体の閉鎖**

閉じた日: 稿 63_ 命題 63-1、worklog `2026-09-11_w146_a枝の別実装.md` §1（w146、稿 `63_a枝の別実装.md` 命題 63-1。**audit64 (R3) が「棄却は過大でない」と判定**）。
出所: $A_v^*\psi_0=c_0\Omega+\chi_{\ge1}$ と分けると $\langle\Omega,(H-E)\Omega\rangle=O(e^2)$、$(H-E)\Omega=\frac{e^2}{2m}A^2\Omega-E\Omega=O(e^2)$（Coulomb ゲージで $`P_f\!\cdot\!A\,\Omega=0`$）、$\chi_1=A_v^*\phi_3=O(e^3)$ なので、**真空成分 $c_0$ が消えるか否かに無関係に**第 2 項は $O(e^6)$。F36 の死因（$\beta$ 奇による真空成分の消滅）は特殊事情ではなく、捨てた項の構造そのもの。$c$ をどう選んでも $e$ の冪は戻らない。加えて、混合を「試行状態 $A\psi_0$ の変更」と読むと $T_\nu\psi_0$ の核 $q_\nu\beta$ は偶で分子が 0（E05-F10）、分母には $|c|^2\cdot\frac12\iint q^2|\beta|^2(s+u)$ が足されるだけ（**交叉項は奇×偶×偶の積分で 0**）で単調に損。
**この 2 本目の論法は摂動展開を使わないので、$O(e^6)$ の次数勘定が $\Lambda$ 一様でなくても（E05-L4）閉鎖は保たれる。****第 2 項の回収という族全体が閉鎖**。生き残る鋭化は第 1 項側（稿 63_ 命題 63-2 の分解付き Bessel）。。

> **【親の注記 2026-09-11】audit64（S2）は本棄却を PASS とし、さらに**
> **核の貼り替え + E05-F10 による非摂動の kill を 1 本追加した**（そちらは $\Lambda$ 一様）。
> **⚠ 閉じたのは「第 2 項の回収」という族**であって、(a) 枝でも B16 でもない。
> **生き残る鋭化は第 1 項側**＝分解付き Bessel（`PROVED.md` の **E05-P1**、`verifier-backed`）。

**閉じた主張**: **混合作用素 $A=F+cT_\nu$（あるいは**殻 $S$ に台を持つ核の対消滅作用素** $`A_v^*=\frac12\iint\bar v\,aa`$、パリティ不問）で、30_ 命題1 の等式が捨てる第 2 項 $\langle A^*\psi_0,(H-E)A^*\psi_0\rangle$ を回収して分母を鋭くする**（発注 w146 の候補 (a-1)。F36 の射程拡大）

---



> **【親の注記 2026-09-11】audit65（S2）を通し、処方 P-1〜P-13・§B〜§D を反映したうえで連結している。**
> **恒等式 65-1 は `verifier-backed` に昇格**（正本は `PROVED.md` の **E05-P2**）。
> **⚠ 「$eA(0)$ 側は 1 ループと恒等」は偽**（audit65 (R2)）。**$\Lambda$ 非一様性の局在は
> 非摂動の構造ではなく 1 ループ + 次数勘定の言明**である。
> **⚠ 「$B_{\max}\approx0.08$」は格下げ**（F22 の X 族で 14.4 倍に散り、$L_*$ は E05-L4 有効域の 7 桁外）。
> **値として引用しない。**
> **⚠ 「$B\lt2$ は摂動論なしに従う」は未証明**（**T51**。$\varepsilon_{\rm res}=L/2$ が 1 ループ限定）。

## F38 — (X2-b) の絶対定数版「$`\exists c\ \forall\lambda\ge1\ \forall\alpha\in(0,1]:\ \mathcal N^\perp_{S,Q}\le c\,\alpha\|\alpha_0\|^2_{L^2;W}`$」（2026-09-11、w148、稿 `65_`、self-audited）

- **何を閉じたか**: (X2-b) のうち、定数 $c$ が $\alpha$ にも $\lambda$ にも依らない定式化**のみ**。
  $\alpha=1/137$ 固定で $c=c(\alpha)$ を許す版は**閉じていない**（未決）。(a) 枝・B16 も閉じていない。
- **機構**: 厳密 2 光子 pull-through 恒等式（65-1）の $\frac{q\cdot P_f}{m}$ 側 = $\psi_0$ 内の他の対 (3,4) との反跳結合 $\frac{q\cdot q'}{mE_4}$。
  背中合わせ帯（$|q'|\lesssim$ 数 $Q$、$s'\sim\Lambda$。E05-F7 の免れ領域）で結合は $O(1)$、帯の対の数 $`\propto\|\alpha_0\|^2_{HS}\propto\alpha^2\sqrt\lambda`$。
  1 ループで $`\mathcal N^\perp/\|\alpha_0\|^2_W\ge c_1\alpha+\kappa\alpha^2\sqrt\lambda`$（**光子数成分の直交性により $n=2$ 成分だけを取るのは正当な下界**。audit65 (R4-5)）、$\kappa(10^6)=0.0154$・外挿極限 $\simeq0.0156$（(研究ノート: `121_`)、独立再現 (研究ノート: `124_`)、指数 $+0.007$）。
  $\lambda=M\alpha^{-2}$・$M\ge10^3$・$\alpha\lesssim M^{-2}$（E05-L4 の有効域内）で第 2 項が第 1 項の $\ge3.8$ 倍。
- **教訓**: $\Lambda$ 一様な $c\alpha$ 型の上界を狙うとき、光子放出（反跳で一様化する）だけでなく **$\psi_0$ に既にいる対との反跳結合**を勘定に入れること。
  この項は E05-F6 命題3 の非実装性・E05-L4 の非一様性と同じ量 $\alpha^2\sqrt\lambda$ を持つ。
- **残る道**: 余りの正しい形 (X2-b′)（稿 65_ 標的 65-4）、または射影 $P$ を「$\psi_0$ + 対励起」へ広げて対–対相関を余りから主項へ移す設計（(研究ノート: `w148.次の発注案.md`) (2)）。
- 解析的証明は未了（漸近の主要項の数値 + 次数勘定）。**ただし audit65 (R4-7) が初等的な解析下界の道筋を出した**: 領域 $s,s'\in[\Lambda,2\Lambda]$・$q\in[Q/2,Q]$・$q'\in[\sqrt{s'},\sqrt{2s'}]$ に制限すると $b/A\ge\frac1{7\sqrt2}$ で $G\ge3.4\times10^{-3}$、測度は帯の勘定で $\gtrsim c\sqrt\Lambda$。よって $\overline{\mathcal R_B}\ge c'\alpha^2\sqrt\lambda$ が数値なしで出る。(研究ノート: `w148.次の発注案.md`) (1) で閉形式の下界に直す。

---



> **【親の注記 2026-09-11】audit66（S2）を通し、処方 P-1〜P-14 を反映したうえで連結している。**
> **⚠ w147 の (研究ノート: `REGISTRY`) は連結禁止**（`120_` の余分な $k_2$ 重みによる誤値。本 audit66 版が差し替え）。
> **⚠ $\mathcal E_A^{\rm ord}/D_{\rm free}=-8.47\times10^{-2}\alpha^2/\lambda\to0$**（稿の「$\lambda^0$・$\Lambda$ 一様」は誤り。
> ただし訂正の向きは稿に有利）。**符号が負なのは $\beta^*$ での数値的事実で構造ではない**（「$\Gamma\ge0$」は偽）。
> **⚠ 「$\eta$ は密度型に完全に局在」は過大**（未評価 $O(e^4)$ が 1 本＋30_ のブロック列挙が非網羅）。

## F39 — 「$\mathcal E_A^{\rm ord}/D_{\rm free}$ は $\Lambda$ 一様な定数 $-4.73\times10^{-2}\alpha^2$（$\lambda$ 指数 0）」（撤回。2026-09-11、audit66）

**閉じた主張**: 稿 `64_EAの符号.md` 命題 64-3 のうち $\mathcal E_A^{\rm ord}$ に関する部分、および
系 64-5（$\mathcal E_A$ の符号が $\lambda=2.3/\alpha$ で反転する）、
系 64-4 の「$\eta^{(A)}\le4.73\times10^{-2}\alpha^2+0.107\alpha/\lambda$（$\Lambda$ 一様）」の第 1 項、
(研究ノート: `w147.EVIDENCE.md`)（第 25 回）・(研究ノート: `w147.REGISTRY.md`) の対応記述。

**正確な障害**: (研究ノート: `120_EA_continuum_quadrature.py`) の `A_table` に**余分な $k_2$ の重み**がある。
$A(k_1)=\frac1{16\pi^2}\int_0^\Lambda k_2dk_2\int dX\frac{1+X^2}{s+u}$ に $`dX=\frac{m\,du}{k_1k_2}`$ を入れると
$k_2$ は**約分して消え** $A=\frac{m}{16\pi^2k_1}\int dk_2\int(1+X^2)dz$（$z=\ln(s+u)$）になるが、
当該コードは `np.sum(wr * r * inner)` と書いて $r=k_2$ を残している。このため $A$ が
$\Lambda=65536$ で $`1322\!-\!2348`$（真値 $`0.0273\!-\!0.0648`$）と $\Lambda$ に比例して増大し、
$\mathcal E_A^{\rm ord}/D_{\rm free}$ の真の $\lambda^{-1}$ が見かけ上 $\lambda^{0}$ になった。

**独立検証**（audit66、(研究ノート: `123c_audit66_Acheck.py`)）: $A$ を置換なしの素の 2 重求積で直接計算し、
$\Lambda=64/1024/16384/65536$ × $k_1/\Lambda=0.5/0.75/1$ の **12 点すべてで置換版と 8 桁一致**（比 $1.00000000$）。
誤った版を使うと稿の $-4.622\times10^{-2}$ が再現される（$-1.2585\times10^{-6}\times2280/0.0621=-4.621\times10^{-2}$）。

**訂正値**（audit66 の独立求積 (研究ノート: `123b_audit66_EA_quadrature.py`)、$\lambda=64\ldots65536$ の 6 段、
3 格子で相対差 $\lt10^{-13}$）:
```math
\frac{\mathcal E_A^{\rm ord}}{D_{\rm free}}\ \longrightarrow\ -8.47\times10^{-2}\,\frac{\alpha^2}{\lambda}
\qquad(\lambda\ \text{指数}=-1,\ \text{定義域}:\ \beta^*,\ 1\ \text{ループ}),
```
$`\mathcal E_A^{\rm ord}/\mathcal E_A^{\rm c}\to-0.794\,\alpha`$（$\bar A\to0.0632$ の定数）。
**符号が負であること自体は正しい**（誤った $A$ も正なので符号は動かない）。
**$\mathcal E_A^{\rm c}\to+0.107\alpha/\lambda$ と $L_{\max}$ 較正表（4 桁）は無傷**で、audit66 が独立に再現した。

**教訓（T47 の補強）**: この誤りは $L_{\max}$ 較正を**通り抜けた**。較正が共有するのは測度・偏極・$c_k^2$・
$e^4$・$q_\mu^2$・定義域・$\alpha_0$ の鎖だけで、**$\frac{N^2}{6\pi^2}$（テンソル還元）・$\kappa=\frac m{16\pi^2}$・
$A(k)$ には感度が無い**。稿の「どの因子を 1 つ誤っても 2 倍ずれる」は偽である。
**以後、較正を根拠に書くときは「較正が感度を持つ因子」と「持たない因子」を並べて列挙すること。**

**再挑戦の可否**: 機構の閉鎖ではない（計算の誤りの閉鎖である）。$\mathcal E_A$ の評価自体は
訂正値で生きており、結論の向き（$\eta$ の $\mathcal E_A$ 成分は律速でない）はむしろ強まる。

---

## F40（2026-09-11、audit69）(U4″) と $\mathcal E_A^{\rm ord}$ の 1 ループ数値の一致から構造的関係を探す

> **【親の注記 2026-09-11】audit69（S2）を通し、処方 P1〜P8 を反映したうえで連結している。**
> **⚠ w149 の (研究ノート: `REGISTRY`) は差し戻し**（1 ループの値・符号・$\lambda$ 指数が全面撤回）。
> **⚠ 「1 体部は無条件に $O(\alpha)$」は過大**（(H-$\varsigma$) は定理でなく、稿の量化子の下では**偽**。反例族あり）。
> **⚠ 「(U2′) より $\lambda^2$ 緩い」は誤り**（正しくは **$\lambda^1$**）。**ただし「新しい未証明入力を追加しない」は生存。**
> **厳密な 1 体/2 体分解そのものは PASS** で、`PROVED.md` の **E05-P4・P5** に昇格した。


**閉じた主張**: 稿 66_ worklog §2.3 が記録した
「(U4″) $\to-7.76\times10^{-2}\alpha^2/\lambda$ と $\mathcal E_A^{\rm ord}\to-8.47\times10^{-2}\alpha^2/\lambda$（audit66）は
**同じ符号・ほぼ同じ大きさ**であり、両者を結ぶ構造があるかもしれない」という観察。
稿自身は「一致する構造的理由は示していない（偶然の可能性を排除していない）」と留保していた。

**正確な障害**: **前提の数値が誤りだった。**
(U4″) の 1 ループ縮約公式の 1 体部が $`\frac1{2m}\sum_\nu\mathrm{tr}(\{M_\nu,K'_\nu\}\hat\rho)`$ であるべきところ
$\frac1m\sum_\nu\mathrm{tr}(M_\nu K'_\nu\hat\rho)$ になっており（$\mathrm{tr}A\ne\mathrm{tr}B$、
恒等式 $\mathrm{tr}A-\mathrm{tr}B=\frac12\sum_{ab}\hat\rho_{ab}(\beta^2)_{ab}|k_a-k_b|^2$）、
正しい組み方では **符号が正に反転し、大きさが 50〜70 倍小さくなる**
（$\lambda\times$ratio $\simeq+1\times10^{-3}$ vs $\mathcal E_A^{\rm ord}$ の $-8.47\times10^{-2}$）。
**⟹ 「同符号・同程度」という観察は消滅した。この経路に追うべき信号は無い。**

**再挑戦禁止の範囲**: 「(U4″) と $\mathcal E_A$ の 1 ループ値が近いことを手掛かりに両ブロックの
構造的関係（共通の起源・相殺・同一の閉形）を探す」ルート。
**禁止しないもの**: 訂正後の (U4″) の 1 ループ値そのものの再計算（これは必要な残タスク）、
および $\mathcal E_A$ 側の独立な扱い（E05-P3 の射程内）。

**根拠**: (研究ノート: `66_密度型4次ブロック_audit69_2026-09-11.md`) §(R3)。
(研究ノート: `129_audit69_direct_contraction.py`)（直接 ED、残差 $10^{-16}$、input_hash `56add02d2b99e764`）、
`129b_audit69_traceA_vs_traceB.py`（恒等式、残差 $6.4\times10^{-16}$）、
`129c_audit69_continuum_trB.py`・`129d_audit69_fixed_estimator.py`（連続体 MC。
稿の組み方を 1〜2% で再現したうえで訂正した）。

**⚠ 併せて記録する教訓（T53 候補。(研究ノート: `audit69.PATCH.md`) P7 に処方あり）**:
T52 の 2 列表で右列に「ED で検算済み」と書くときは、
**その ED が検証した式と、数値を出したスクリプトが実装した式が同じであること**を
突き合わせる回帰検査を 1 本置くこと。本件では ED（V2）は正しい対称化公式を検査して合格したが、
求積コードは非対称版を実装しており、**符号が反転するほどの誤りが 2 列表を素通りした**。

---

## F41 — 準自由（Gauss / スクイーズ）型の試行族で (X2-b)＝$\mathcal N^\perp_{S,Q}$ を評価する（2026-09-11、w150、稿 `67_X2bの準自由版.md`）

> **【親の注記 2026-09-11】audit68（S2 → 等級 S1）を通し、処方を反映したうえで連結している。**
> **中核結論（準自由型の kill-check は盲目型）は 3 機構とも PASS で維持**
> （(a) 光子数パリティ／(b) Wick — 監査人がより強い論証を提示／(c) $SO(3)$ 共変 + 横条件）。
> **⚠ 射程の限定（必修）**: 成立は**試行核 $K=\alpha_0^{(2)}|_W$ に固有**で**準自由族全体には偽**
> （階数 1 核で発散する反例）。**閉鎖は「純粋かつ回転不変な準自由族」に限る** — **回転平均 Gauss 混合**
> （回転不変だが準自由でなく奇チャネルを保つ）と $E(0)$ 変分など**別標的の Gauss 族は対象外**。
> **⚠ 別の記録（別の記録）の結論を否定するものではない**（向こうの標的は $E(0)$ の変分上界で、
> **変分上界には Wick で十分**。E05 の $\mathcal N^\perp$ とは別の量）。
> 命題 67-1 の一般不等式は `PROVED.md` の **E05-P6** に昇格した。


**閉じた主張**: 「$\psi_0$ を準自由状態（対核 $K$ の純粋スクイーズ）で代理して
$`\mathcal N^\perp_{S,Q}=\iint_W(\|a_1a_2\psi_0\|^2-|\alpha_0|^2)`$ の $\Lambda$ 一様上界（B16 の第 1 律速 (X2-b)）を判定する」。

**正確な障害**: **計算は通るが、族が障害そのものを持たないため判定能力がゼロである。**
$K=\alpha_0^{(2)}|_{S\times S,|q|\le\sqrt{2m\Lambda}}$ で
$\mathcal N^\perp_{\rm qf}=\Theta(\alpha^4\lambda^{-1/2})$、比は $\Theta(\alpha^2\lambda^{-1})$（稿 `67_` 系 67-1a・漸近 67-1b。
厳密上界 $16.4\alpha^4\lambda^{-1/2}$ が $\forall\alpha\le1,\forall\lambda\ge1$ で付く）。
一方 1 ループ真値は $`\mathcal N^\perp/\|\alpha_0\|^2_W\simeq c_1\alpha+\kappa\alpha^2\sqrt\lambda`$（$c_1\alpha\simeq0.127\alpha$、$\kappa\simeq0.0156$）で、
**この 2 項はどちらも純粋スクイーズ状態では恒等的に 0**（命題 67-2）:

- $c_1\alpha$ は $\psi_0$ の**3 光子成分**（$eA(0)$ による第 3 光子放出）の寄与。純粋スクイーズは光子数パリティ偶で $\Psi^{(3)}=0$。
- $\kappa\alpha^2\sqrt\lambda$ は 4 光子振幅の**連結補正**（対–対反跳 $q\cdot q'/mE_4$）。準自由の 4 点関数は厳密に Wick で連結部が 0。

**⇒ 試行状態が (X2-b) の意味ある検査であるための必要条件**: (i) 非零の奇光子数振幅、
(ii) 非零の切断 4 点関数。**回転不変な純粋 Gauss（準自由）状態はどちらも持てない。**
**⚠ 限定**: 「純粋」を外すと偽（変位スクイーズ $W(f)\Psi_K$ は $f\ne0$ で (i) を持つ）。
「回転不変」を課してよいのは $\psi_0$ の**代理**として使う場合に限る（$H(0)$ が同時回転と可換で
基底状態が非縮退なら $\psi_0$ は回転不変。E05-F10 と同じ非縮退仮定）。
さらに $P_{\rm tot}=0$ で回転共変な 1 光子期待値は $`\langle a(k,\lambda)\rangle=\epsilon_\lambda(k)\!\cdot\!v(|k|)\hat k=0`$（横条件）なので、
**回転不変な試行状態にコヒーレント成分を足しても (i) は作れない**。奇数振幅は非 Gauss 構造（電子–場の絡み、$P_f$ 依存）からしか来ない。

**再挑戦禁止の範囲（狭く取ること）**: 「**回転不変な純粋**準自由（Gauss／スクイーズ／変位スクイーズ）状態を
**$\psi_0$ の代理**にして $\mathcal N^\perp$ の $\Lambda$ 一様上界を論じる」提案は、上の 2 条件に当てて先に殺すこと。
**⚠ 以下は閉鎖に含めない（使える道具として残す）**:
(1) **回転平均した Gauss 混合** $`\rho=\int dR\,U_R|\Psi_{K,f}\rangle\langle\Psi_{K,f}|U_R^*`$。回転不変だが準自由でなく、
    $|f_1|^2\gamma_{22}$ 型の奇チャネル寄与を保つ（各 $R$ で非負なので平均後も残る）。moment は Wick + 回転平均で閉形。
(2) **$\mathcal N^\perp$ 以外の標的**（$E(0)$ や $\langle H\rangle$ の変分上界など）に Gauss 型を使うこと。
    変分上界は 2 点関数だけで厳密に計算でき、奇数振幅も切断 4 点関数も要らない。
**閉じたのは「準自由代理による (X2-b) の判定」であって、(X2-b) でも B16 でもない。** 両者は開のままである。

**閉鎖と同時に残ったもの（閉鎖ではない）**: 命題 67-1（回転不変性 ⟹ $\gamma$ の対角は動径関数 ⟹ 角度条件の
薄い帯 $W$ には集中できない）は**準自由性を使わない**ので、真の $\psi_0$ の非連結部分 $n_0(1)n_0(2)$ に
そのまま適用できる（命題 67-3）。**ただし $\sup_Sn_0^{\psi_0}$ の非摂動上界が無く、$\langle N_S\rangle$ の既知上界は
$\lesssim\alpha^2\lambda^2$（F8）で弱すぎるので、現時点で (X2-b) の証明には使えない。**

**出典**: 稿 `67_X2bの準自由版.md`（`self-audited`、未監査、再監査等級 S2）、
(研究ノート: `2026-09-11_w150_X2bの準自由版.md`)、(研究ノート: `127_w150_Nperp_qf.py`)（`conclusion: PASS`）。

---

## F42（2026-09-11、w153、稿 70_）準最適族 $`\mathcal A_\theta=\{\beta: L[\beta]\ge\theta\max L\}`$ への制限で B16 の $\beta$ 一様性を回復する

- **閉じた主張**: 「許容核を $L$ の準最適族 $\mathcal A_\theta$（$\theta\in(0,1]$ 固定）に制限すれば、(H-$\varsigma$)・$\varepsilon_{\rm res}$ の非摂動下界・
  階数 1 核の排除が $\mathcal A_\theta$ 上で一様に成り立つ」。
- **正確な障害**: (i) $`\max_{V\setminus\{0\}}L=\frac2m\|P_V(s+u)^{-1/2}n_\mu\|^2`$ は $\psi_0$ の 2 光子振幅の量で、B16 の残る障害「$\alpha_0$ の非摂動サイズ」と同一 → 定義が循環。
  (ii) 任意の固定 $\theta\lt1$ で混合核 $`\hat\beta=\sqrt\theta\,\hat w+\sqrt{1-\theta}\,v`$（$v$＝退化核の直交化）が $\mathcal A_\theta$ に入り、
  $\varsigma\gtrsim(1-\theta)\lambda^{-1}$（$\ell=1$ 共変の読み）または $(1-\theta)$（台条件のみの読み。$\varsigma$ は E05-P5 の literal 規約 $`\|\beta\|_2^2=\iint|\beta|^2`$ で測る）で $\lambda^{-3/2}$ を破る → 結論が $\theta$ 依存。
  (iii) E05-P6 の量化子は $\psi_0$ 模型（準自由族）の上を走っており、$\beta$ の族とは独立である。$\mathcal A_\theta$ への制限はこの項を 1 文字も動かさない。
- **転進先**: 量化子を $\exists\beta$（証人 1 本 $\beta_1=P_V(s+u)^{-1}q_\mu\alpha_0^{(1)}$）に書き換える（稿 70_ 命題 70-3・70-4）。
  退化核による 3 件の「一様性の破れ」は下界法では無意味で、障害は $\psi_0$ の性質 O1〜O6 に移る（**本数は減らない**）。
- **射程**: 命題W119-4（B16 の到達点の天井＝上界側）では $\sup_{\beta\in V}$ が本質であり、本 F は上界側の量化子を否定しない。

**監査記録**: (研究ノート: `70_量化子の再設計_audit71_2026-09-11.md`)（audit71、S2 full fresh、Opus、effort=high、**壊しに行く立場**）。
**中心主張の命題 70-3 は (R1) で 4 経路すべてから壊しに行って壊せなかった＝PASS。** 本 F の連結は audit71 (R6) の
処方 P-8（2 件の差し替え）適用後に親が実施。**罠は T56 に登録。**
**⚠ 稿 70_ の格付けは `self-audited` のまま**（記述誤り 1 件＝命題 70-1 の内積空間、列挙の取りこぼし 1 件＝O6 を
audit71 が検出し、処方 P-1〜P-9 適用後の再監査等級は S1。ただし親が P-7 で $V$ の読みを固定した判断のみ S2 相当）。

---

---

## F43 — $\varepsilon_{\rm res}$ の非摂動化を「$|A_\mu|^2/|N_\mu|^2\ge1-C\alpha$ の $\beta$ 一様下界」に帰着させる標的（2026-09-11、w152 / 稿 `69_`、audit72 が S2 監査で支持）

**閉じた主張**。絶対定数 $C$ が存在して
$\forall\Lambda\lt\infty\ \forall\alpha\in(0,1]\ \forall\beta\in\mathcal A:\ \frac{|A_\mu[\beta]|^2}{|N_\mu[\beta]|^2}\ge1-C\alpha$
（$\mathcal A$＝許容核の族。T51 の処方として親が立てた標的 (B)）。

**正確な障害**。$A_\mu[\beta]=\langle\beta,q_\mu\alpha_0\rangle$ と $N_\mu[\beta]=\langle\beta,n_\mu\rangle$ は
**同じ $\beta$ に対する 2 本の線型汎関数**である。許容核の全体 $\mathcal K$ は、その定義条件
（殻台 $W_{S,Q}$・Bose 対称・パリティ奇・$q$ 奇・$\ell=1$（$\mu$ 固定）・$\langle\beta,\alpha_0\rangle=0$・形式領域）が
**1 つの例外もなく $\beta$ の斉次線型条件**であるため**閉部分空間**である
（audit72 (R1-1) が 7 条件を 1 行ずつ検査。不等式・正値性・規格化は 1 つも混じっていない）。
したがって $a:=P_{\mathcal K}(q_\mu\alpha_0)$、$n:=P_{\mathcal K}(n_\mu)$ に対し**二者択一**が成り立つ
（稿 `69_` 命題 69-1、厳密・無条件。**audit72 が独立に再導出して PASS**）:

- **$n\in\mathbb Ca$（$n=ca$）、または $a=0$**：比は $\mathcal A$ 上**恒等的に定数**（それぞれ $|c|^{-2}$、$0$）。
- **$a\ne0$ かつ $n\notin\mathbb Ca$**：$`\beta_0:=n-\frac{\langle a,n\rangle}{\|a\|^2}a\in\mathcal A`$ が
  $A_\mu[\beta_0]=0$・$`N_\mu[\beta_0]=\|n\|^2-\frac{|\langle a,n\rangle|^2}{\|a\|^2}\gt0`$ を満たし、
  $\beta_t=\beta_0+ta$ により**比は $[0,\infty)$ 全体を走る**（$\inf=0$、達成される）。

**中間が無い。** ゆえに「$\ge1-C\alpha$」という $O(\alpha)$ の緩みを持つ形は、
第 1 の枝では**過剰**（比は厳密な定数なので緩みを入れる意味が無い）、第 2 の枝では**任意の $C$ に対して偽**（$\alpha\lt1/C$）。
**⟹ 標的 (B) は量化子が強すぎたのではなく、形が構造的に誤っていた。この判定は枝の同定に依存しない。**
E05-F13 の「重なり $1-O(\alpha)$」は**ベクトル $n_\mu$ と $q_\mu\alpha_0$ の $L^2$ 内積**の言明であって、
$\beta$ 対にわたる一様性ではない（**T50** 型の定義域混同と同族）。

**どちらの枝かについて（射程を限定して書く）**。$O(e^4)$ では第 2 の枝である見込みが高い
（稿 `69_` 命題 69-2、**`self-audited` のまま**）: $r_\mu$ の $O(e^4)$ 主要項の J1 成分は各点で $q_\mu$ に平行だが、
**係数 $\Theta(s,|q|)$ が配位の関数で定数でない**（$G$ の被積分関数が $s$ について各点で狭義単調減少なので
**解析的に**非定数。数値は冗長な確認で、許容窓上の変動は $\lambda=1,10,10^2,10^3$ で $\times2.09,\ 1.63,\ 1.29,\ 1.18$。
(研究ノート: `131_w152_theta_variation.py`)、conclusion PASS。**audit72 が別系統 2 本で独立再現、最大相対差 $4.4\times10^{-5}$**、
(研究ノート: `135_audit72_prop69_independent.py`)）。J2・J3 は偏極テンソル構造がそもそも異なる。
**ただし稿の留保は未閉鎖である**: (a)「$\Theta$ が非定数」と (b)「J2+J3 が $q_\mu\alpha_0^{(2)}$ に比例しない」の
**厳密な相殺が起きないことは証明されていない**。また E05-L4 により $O(e^4)$ の次数勘定は $\Lambda$ 一様でない。
**⟹ 閉鎖の根拠は「形の不適格」（枝に依らず厳密）であって、「枝 (ii) だから偽」ではない。**

**転進先（閉鎖と同時に得られた代替路）**。比を経由する必要が無い。$B=\frac L{1+\varepsilon}$ を
Cauchy–Schwarz で直接押さえると、$\eta^*:=\sup_{\beta\in\mathcal A}\eta[\beta]\lt1$ の下で **$\beta$ 一様**に
```math
\sup_{\beta\in\mathcal A}B[\beta]\ \le\ 2+\frac{\tilde\delta^{\,2}}{1-\eta^*},\qquad
\tilde\delta=\sqrt{2/m}\,\|(s+u)^{-1/2}\tilde r_\mu\|_{HS},\quad\tilde r_\mu=n_\mu-q_\mu\alpha_0^\Omega
```
が出る（稿 `69_` 命題 69-3、`PROVED` の該当項。**$\varepsilon_{\rm res}=L/2$ を使わない**）。**T51 の要求はこちらで満たされる。**
**残る穴は 1 本ではない**（**T45**。「残る唯一の障害は X」と書かないこと）。少なくとも 2 本ある:
1. **$\eta^*\lt1$ の証明**（$\eta$ の $\beta$ 一様上界）。**36_ は $\eta$ を $\beta$ 一様には定義していない**（audit72 (R4)）。
   しかも **T56 が一様性を壊す退化核として名指しする $A_\mu\perp$ は、上の枝 (ii) の証人 $\beta_0$ そのもの**である。
2. **$\tilde\delta$（および $\eta^*$）の $\Lambda$ 一様な上界。**

**再挑戦の可否**: 標的 (B) の**大域形**には戻らない。局所形 (B′)（稿 `69_` 命題 69-4、$C(\theta)\propto\theta^{-1/2}$）は
不等式としては成立するが、(i) 命題 69-3 に包含され、(ii) $\mathcal A_\theta$ の定義が $L_{\max}$ を通じて未知の $\psi_0$ に依存して
**循環する**（**T56 末尾・FAILED の F42** と同じ理由）ので、**これ単体を目的にする発注もしない。**

## F44 （2026-09-11、w151）— $eA(0)$ チャネルを「片ごとに独立にノルムで押さえる」評価鎖

**閉じた主張**: E05-P2 の主項の $eA(0)$ 側 $`\Phi=(1-P)R_{12}\frac{e\,q\cdot A(0)}{m}\psi_0`$ を、
5 つの片（(i) 生成部・主項の真空片／(i′) その随伴片／(ii) 生成部・残差／(iii) 交換子項／(iv) 消滅部）に分け、
**各片を独立に作用素ノルム・Cauchy–Schwarz で押さえて $`\|\Phi\|^2\le c\alpha`$（$\Lambda$ 一様）を出す**という道筋。

**正確な障害（初等・無条件）**: 稿 `68_` 命題 68-3。この評価鎖は
- 片 (ii) から $\frac{\mathcal K}{2m}=O\bigl(\frac{\Lambda}{\ln\lambda}\bigr)$（$`\mathcal K:=\|\pi\psi_0\|^2`$、$\pi=P_f+eA(0)$）、
- 片 (iv) から $\Theta:=\langle H_f\rangle_{\psi_0}=O(m)$

を**同時に**要求する。ところが補題 68-2（$H=\frac{\pi^2}{2m}+H_f$ と $H\psi_0=E_0\psi_0$ だけから出る**厳密な**等式）
```math
\frac{\mathcal K}{2m}+\Theta=E_0
```
により、この 2 つは $E_0=O(\Lambda)$ を含意する。**E05-L4（Lieb–Loss 1999）の $E_0\gt C_1\alpha^{1/2}\Lambda^{3/2}$** と
$\lambda\gt\bigl(c/(C_1\sqrt\alpha)\bigr)^2$ で矛盾する。
**⟹ $\psi_0$ の 1 体量（$\mathcal K$・$\Theta$・$\langle N\rangle$）の上界をどれだけ改良しても、この評価鎖は閉じない。**
根拠には補題 68-2 に加えて **補題 68-2′（audit73、無条件）** $\Theta\le\frac{2\alpha\lambda}{\pi m}\mathcal K$ が要る。
これが無いと、(iv) を pull-through で $\mathcal K$ に帰着させる鎖（要求は $\mathcal K=O(\frac{m^2}{\alpha\lambda})$ のみ、$\Theta$ は自由）が排除できない。
補題 68-2′ を足すと $\mathcal K$ の無条件下界 $\mathcal K\ge\frac{2\pi mE_0}{\pi+4\alpha\lambda}\gtrsim\frac{m^2\sqrt\lambda}{\sqrt\alpha}$ が出て、この鎖も $\alpha^{1/2}\lambda^{3/2}$ 倍の差で死ぬ。

**再挑戦禁止の範囲（狭く取ること）**:
「$eA(0)$ チャネルの各片を**独立に**（片の間の相殺を使わずに）$`\|\pi\psi_0\|`$・$\langle H_f\rangle_{\psi_0}$・$\langle N\rangle_{\psi_0}$ の
上界に帰着させて $\Lambda$ 一様性を出す」提案は、まず上の 2 要求を書き出して $E_0=O(\Lambda)$ に当てて殺すこと。
**「$`\|\pi\psi_0\|`$ または $\Theta$ の非摂動な上界を改良すれば通る」型の発注は、この項で先に殺せる**
（$\Theta$ 側は補題 68-2 で、$\mathcal K$ 側は補題 68-2′ が与える**下界** $\mathcal K\ge\frac{2\pi mE_0}{\pi+4\alpha\lambda}$ で殺す）。
**ただし $`n^{\psi_0}(k)=\|a_k\psi_0\|^2`$ の点ごとの情報を使う鎖はこの項の対象外である**（下の ⚠4 を見よ）。
実際、重み $h$ を動かした Cauchy–Schwarz 族 $`\|a[g]\psi_0\|\le\|g/h\|_2\langle\Gamma(h^2)\rangle^{1/2}`$ の下限は
$`\bigl(\int|g|\,\|a_3\psi_0\|\bigr)^2`$ で、**これがこの評価鎖に残された唯一の逃げ道である**（audit73 §1.2.3）。

**⚠ 閉鎖に含めないもの（明示）**:
1. **$eA(0)$ チャネル自体は閉じていない。** 本項は**評価鎖**の閉鎖であって、
   「$`\|\Phi\|^2`$ が $\Lambda$ 非一様である」という主張では**まったくない**（T43・T49）。
2. **片 (i) は解けている**（命題 68-1、$\Lambda$ 一様・絶対定数 $\frac{32}{3\pi}$・非摂動）。1 ループの $c_1\alpha\simeq0.127\alpha$ は
   この片が担う量である。**成功した部分を閉鎖に巻き込まないこと。**
3. **$\Xi_+$ と $\Xi_-$ の交差項**を使う道は**開**である。本項はむしろ「相殺なしには閉じない」ことを示しており、
   交差項の明示計算を**次の一手として指定する**。
4. $n^{\psi_0}(k)$ の**点ごと**の減衰など、$\Theta$・$\mathcal K$ を経由しない入力を使う道も開。
5. **$\alpha$ を固定して $\lambda$ の実用域に限る**なら、交換子項の再和（係数 $O(\alpha\ln\lambda)$）が使える。
   量化子を弱めた主張としては生きている（$\alpha$ 一様ではない。T40/T50）。
6. (X2-b) も B16 も開のままである。

**付随して確定した事実（閉鎖ではない）**:
- **恒等式 68-4**: $`R_{12}a_3^*=a_3^*D_3^{-1}-\frac{ec_3}{m}R_{12}\bigl[\epsilon_3\!\cdot\!(\pi+q)\bigr]D_3^{-1}`$。
  $[A(0),a_3^*]$ が c 数であることから第 2 項が出る。**発注文の下書き (D4) はこれを欠いていた**
  （有限モード PF での数値確認: 完全形の残差 $7.6\times10^{-15}$、(D4) の形の残差 $O(1)$）。
- **発注の 4 分割（生成部/消滅部 × 主項/残差）は不正確**で、正しくは上の 5 片である
  （「消滅部・残差」は空、「主項」がノルム 2 乗で 2 片に割れ、交換子項が増える）。

**出典**: 稿 `68_c1alpha項の非摂動化.md`、
(研究ノート: `2026-09-11_w151_c1alpha項の非摂動化.md`) §1・§5・§6、
(研究ノート: `130_w151_eA0_channel_checks.py`)（`conclusion: PASS`）。

**監査記録**: (研究ノート: `68_c1alpha項の非摂動化_audit73_2026-09-11.md`)（audit73、S2 full fresh、Opus、effort=high、**壊しに行く立場**）。
**(R1) 結論 PASS / 初稿の証明 FAIL。** 監査人は**反例鎖を 1 本構成した**（(iv) を pull-through で $\mathcal K$ に帰着させると
要求は $\mathcal K=O(m^2/\alpha\lambda)$ のみで $\Theta$ は自由になり、初稿の「$E_0=O(\Lambda)$ で矛盾」という論法が届かない）。
**同じ監査人が補題 68-2′ を 1 行足して穴を塞ぎ、結論はむしろ強い形になった**（「$\mathcal K$ と $\Theta$ のどちらに帰着させても死ぬ」）。
処方 PATCH-1・PATCH-4・PATCH-5 反映後に親が連結。**PATCH-5 以前の版には、生きている $\mathcal K$ 分岐を誤って殺す偽の文が
2 つ含まれていた**（**T60**）。

---

## F45 （2026-09-11、w156、稿 `73_XiPlusMinusの交差項.md`、verifier-backed（audit76））— $eA(0)$ チャネルの**交差項プログラム**と、相殺を使い切った最良形の素朴な鎖

**閉じた主張**: F44 が「次の一手」として名指しした 2 つ、すなわち
(S1) $\Xi_+$ と $\Xi_-$ の交差項、(S2) $\Xi_+$ 内部の交差項 (i)↔(ii)・(i)↔(iii) を明示計算して
$`\|\Phi\|^2\le c\alpha`$（$\Lambda$ 一様・絶対定数）を出すという道筋。および、その相殺を**使い切った**最良形
$\Phi_{\rm tot}=\frac1m(1-P)R_{12}(q\cdot\pi)\psi_0$ を $`\|R_{12}v\|\le\|R_{12}\|\,\|v\|`$ で評価する鎖。

**正確な障害（初等・無条件。2 段構え）**

**(1) 交差項プログラムは内容を持たない**（稿 73_ 帰結 73-4）。$\pi:=P_f+eA(0)$ は定義なので恒等的に
```math
\frac{q\!\cdot\!P_f}{m}+\Xi_++\Xi_-=\frac{q\!\cdot\!\pi}{m}
```
（右辺は **E05-P2 第 2 式の括弧そのもの**で、E05-P2 の証明の記述「固有方程式の代入 + $\pi$ の線形分解」に既記）。
ゆえに 5 片のノルム 2 乗と 6 本の交差項の総和は**恒等的に** $`\|(1-P)R_{12}\Xi\psi_0\|^2`$ に戻り、
$P_f$ チャネルまで含めれば $`\|\Phi_{\rm tot}\|^2`$ に戻る。この最終形は**恒等式 68-4 も 68-5 も 5 片分解も使わずに**書ける。
⟹ **個々の交差項を評価するプログラムは、分割前の 1 本を評価する以上の情報を持たない。**
（交差項が小さいわけではない。有限モードの実測では $\alpha^2$ 層で交差項の和がノルム 2 乗の和の **4.98 倍**あり
層の符号を反転させる。しかしその**大きさの下界**を得ることは分割前の量を知ることと同値で、
Cauchy–Schwarz は上界 $`2\|X_a\|\|X_b\|`$ しか与えない。）

**(2) 最良形でも素朴な鎖は閉じない**（稿 73_ 命題 73-5）。段 (a) $`\|(1-P)\cdot\|\le\|\cdot\|`$、
(b) $`\|R_{12}v\|\le\|R_{12}\|\|v\|\le\frac\rho s\|v\|`$、(c) $`\|v\|^2\le\kappa q^2\mathcal K`$（$v=(q\cdot\pi)\psi_0$）を使うと
$W_{S,Q}$ の最悪点（$s=\Lambda$、$|q|=Q$、$\lambda\gt2$ で到達）で
```math
\|\Phi_{\rm tot}\|^2\le\frac{2\kappa\rho^2\mathcal K}{m^2\lambda}\quad\Longrightarrow\quad
\textbf{(R)}\ \ \mathcal K\le\kappa'\alpha m^2\lambda\ \ \bigl(\kappa'=\tfrac{c}{2\kappa\rho^2}\bigr).
```
**要求は 1 本だけで、$\Theta$ には何も要求しない**（$\Xi_-$ が $\pi$ に吸収されるので F44 の (iv) 由来の要求が発生しない）。
**⟹ F44 の矛盾はこの鎖には届かない。** それでも $\lambda=\alpha^{-2}$（$\alpha\lambda=\alpha^{-1}\to\infty$、**E05-L4 を F44 と同じ漸近域で使う**）で
- (R) ⟹ $\mathcal K\le\kappa'm^2\alpha^{-1}$、
- **E05-P10（補題 68-2）** $\frac{\mathcal K}{2m}+\Theta=E_0$ ＋ **補題 68-2′** $\Theta\le\frac{2\alpha\lambda}{\pi m}\mathcal K$ ⟹
  $E_0\le\frac{\mathcal K}{m}\bigl(\frac12+\frac{2\alpha\lambda}\pi\bigr)\le\kappa'm\bigl(\frac1{2\alpha}+\frac2{\pi\alpha^2}\bigr)$、
- **E05-L4** $E_0\gt C_1\sqrt\alpha m\lambda^{3/2}=C_1m\alpha^{-5/2}$

が $C_1\alpha^{-1/2}\gt\kappa'(\frac\alpha2+\frac2\pi)$ で矛盾する。$\alpha\lt\alpha_0:=(C_1/(1.14\kappa'))^2$ なる**すべての** $\alpha$ で成立し、
余裕は因子 $\alpha^{-1/2}\to\infty$。定数 $c,\kappa,\rho$ の取り方に鈍感である。

**再挑戦禁止の範囲（狭く取ること。T60）**
「$eA(0)$ チャネル（または $P_f$ チャネル）の片の**交差項を個別に評価して** $\Lambda$ 一様性を出す」提案、および
「$\Phi_{\rm tot}$ を $`\|R_{12}\|\le\rho/s`$ で分離してから $`\|\pi\psi_0\|`$ の上界に帰着させる」提案は、
まず上の (1)(2) に当てて殺すこと。**発注の前に「なぜ分割前の形 $\Phi_{\rm tot}$ では足りないのか」を 1 行書かせる。**

**⚠ 閉鎖に含めないもの（明示）**
1. **$eA(0)$ チャネルも $\Phi_{\rm tot}$ も閉じていない。** 本項は**評価鎖**の閉鎖であって
   「$`\|\Phi_{\rm tot}\|^2`$ が $\Lambda$ 非一様である」という主張では**まったくない**（T43・T49）。
   **(X2-b) も B16 も開である。**
2. **矛盾の窓は有限である**: おおよそ $\lambda\lesssim(\frac{\pi C_1}{2\kappa'})^2\alpha^{-3}$。
   **$\lambda\gg\alpha^{-3}$ では矛盾が消える。F44（大 $\lambda$ 全域で殺す）とは性格が違う。**引用時に混同しないこと。
3. **片 (i) は解けている**（**E05-P9**、$\Lambda$ 一様・絶対定数 $\frac{32}{3\pi}$・非摂動）。成功した部分を巻き込まない。
4. **$R_{12}$ とベクトルを分離しない鎖は対象外・開である。** 稿 73_ §5 の標的 (B′)
   $`\langle(q\cdot\pi)\psi_0,R_{12}(q\cdot\pi)\psi_0\rangle\le c\,\alpha m^2s`$ がその定式化で、
   $`\|R_{12}v\|^2\le\frac1s\langle v,R_{12}v\rangle`$ から $`\|\Phi_{\rm tot}\|^2\le c\alpha`$ の**十分条件**になる。
   **負ける段は (b) に一意に局在する**（(c) は **E05-F22** の回転不変性の下で $\kappa=\frac13$ の**等式**。
   (a) の損失は $`\mathrm{Cov}_\nu(E,E^{-1})^2\le\mathrm{Var}_\nu(E)\mathrm{Var}_\nu(E^{-1})=\theta\|\Phi_{\rm tot}\|^2`$、
   $\theta=\frac{q^2\mathcal K}{3m^2(s+u)^2}$＝鎖の出力そのものなので、$(1-P)$ の保持で得られる改善は高々因子 2。
   **audit76 が証明**。稿 補題 73-2′）。
5. **1 次モーメント（f-sum rule・二重交換子）で (b) を改善する道は無効**である（稿 73_ §5.2 の注。
   台 $[s,\infty)$・総質量・1 次モーメントを固定しても $\int E^{-2}d\mu$ の上限は $`\|v\|^2/s^2`$ から改善しない）。
   **改善に効くのは $-1$ 次モーメントだけ。**
6. **F44 ⚠4 の $n^{\psi_0}(k)$ 路線は、(B′) を経由する設計では出番が無い**（$\Xi_-$ が $\pi$ に吸収されるので
   片 (i′)(iv) が存在しない）。点ごとの情報が要るとすれば、$\mu_v$ の高エネルギー側の重みの**下界**としてである。

**付随して確定した事実（閉鎖ではない）**
- **補題 73-2**: 光子パリティ $\Gamma(-1)$ により $X_a(-e)=\varepsilon\Gamma(-1)X_a(e)$（$\varepsilon$ は 4 本共通）なので、
  5 片のノルム 2 乗と 6 本の交差項は**すべて $e$ の偶関数＝$\alpha$ の整数冪**である（位相規約は不要）。
  有限モード数値で 10 組すべて相対差**厳密に $0$**。
- **$\alpha$ 冪表**（数値確認済）: $O(\alpha^1)$ は (i) $`=\|f\|_2^2`$ ただ 1 つ。
  (i′)・$`\|`$(iv)$`\|^2`$・(ii)↔(iii)・(ii)↔(iv)・(iii)↔(iv) が $\alpha^3$、それ以外（$`\|`$(ii)$`\|^2`$・$`\|`$(iii)$`\|^2`$・
  (i)↔(ii)・(i)↔(iii)・**(i)↔(iv)**）が $\alpha^2$。
  **主項と同じ冪を持つ交差項は 1 つも無い。**
- **交差項の符号**（有限モード 1 配位の実測、$e=0.32$）: $(1,2)+$、$(1,3)-$、$(1,4)-$、$(2,3)-$、$(2,4)-$、$(3,4)+$。
- **恒等式 68-4 の第 2 項の必要性を独立再現**（落とすと残差 $O(1)$: $0.056$〜$0.093$。完全形は $3.6\times10^{-14}$）。
- **観察 73-7（示唆。未証明）**: $M_{\hat q}(q,s):=\langle(\hat q\cdot\pi)\psi_0,R_{12}(\hat q\cdot\pi)\psi_0\rangle$ は
  **E05-F21 の $\frac2{3m}M=1-\frac1h$ に現れる双一次形式と同型**で、差はファイバー・シフト・射影の 3 点だけ。
  単調性 $M_{\hat q}(q,s)\le\frac M3$（**未証明**）が言えれば (B′) は $1-\frac1h\le c\alpha$ に帰着し、
  障害は $\lambda$ の**冪**から **$\ln\lambda$** に落ちる。
  **⚠ ただし「$1-\frac1h\le c\alpha$」を標的に書いてはならない（audit76）。** $h$ の上界が現れるのは
  この**十分条件の中だけ**で、(B′) にも (X2-b) にも現れない（T45 の型の裏返し。**(X2-b) についての判定ではない**）。
  しかもその形は **E05-F1 により偽**である（$1-\frac1h=\frac{(8\alpha/3\pi)L}{1+(8\alpha/3\pi)L}$、$L=\ln(1+\frac\lambda2)$ は
  $L\gt\frac{3\pi c}{8}$ で $c\alpha$ を超える。$\lambda$ の閾値は $\alpha$ に依らない）。
  **正しい書き方**: 単調性は無条件に $`\|\Phi_{\rm tot}\|^2\le\frac\Lambda s(1-\frac1h)\le1-\frac1h`$ を与え、
  1 ループでは $O(\alpha\ln\lambda)$。**鎖の $O(\alpha\lambda)$ から冪ひとつの改善**で、$\Lambda$ 一様性には届かない。

**出典**: 稿 `73_XiPlusMinusの交差項.md`、(研究ノート: `2026-09-11_w156_XiPlusMinusの交差項.md`) §2–§7、
(研究ノート: `140_w156_cross_terms_reassembly.py`)（`conclusion: PASS`、入力 hash は `_result.json`）。

**監査記録**: (研究ノート: `73_XiPlusMinusの交差項_audit76_2026-09-11.md`)（audit76、S2 full fresh、Opus、effort=high、**壊しに行く立場**）。
**(R1) 結論 PASS / 証明 PASS＝壊せず。** 監査人が要求 (R)・$\lambda=\alpha^{-2}$・余裕 $\alpha^{-1/2}$ を独立再導出して逐語一致させ、
さらに $\rho\ge(1+\sqrt{2/\lambda})^{-1}\to1$・$\kappa=\frac13$ の等号を示して**「3 定数に鈍感」を証明に格上げ**し、
**窓の真の閾値を $\alpha\lt\frac{\sqrt\pi C_1}{2\kappa'}$ に改善した**（稿より 1 段強い kill）。
**(R2) PASS かつ稿より強い**（恒等式 73-3′: 足し戻すと **E05-P2 第 2 式の左辺**に戻る＝2 チャネル分割ごと完全な円環）。
**(R4) の ⚠4 は本項で殺されていないことを確認済**。ただし**「負ける段は (b) に一意」は稿では未証明の断定**で、
**監査人が補題 73-2′（$\mathrm{Cov}$ 評価）で証明して塞いだ**（上の ⚠4 に反映済）。**再監査等級 S1。**

---


## F46（「$\Delta=\mathcal E_A^{\rm full}-\mathcal E_A^{\rm c}\ge0$ で (H-$\hat Q$) の標的を 3 項から 2 項に減らす」— $O(e^4)$ で偽）

> **【親へ】これは (研究ノート: `w162.FAILED.md`) の差し替えである**（audit77 が (R6) で 2 件の補正を指示した:
> 展開 (iv) 依存の明示／反例族の「パリティ奇」ラベルの削除）。**w162 版は連結しないこと。**

日付: 2026-09-12（w162、稿 `77_E_A_fullの残差の符号.md`）。
格付け: **`verifier-backed`**（audit77、S2 full fresh、(研究ノート: `77_E_A_fullの残差の符号_audit77_2026-09-12.md`)）。

**閉じた主張**: $\Delta\ge0$（したがって $\mathcal E_A^{\rm full}\ge\mathcal E_A^{\rm c}\ge0$）を
$P\ge0$・$\beta^*\beta\ge0$ 型の構造的議論で示し、(H-$\hat Q$) の未評価 3 項
（$R_2$・$R_{\mathcal U}$・$\mathcal E_A^{\rm full}$）を 2 項に減らす。

**正確な障害**: $O(e^4)$ 部は $aa$ 型 1 本に閉じ、1 ループで
$`\mathrm{Re}\,\Delta^{(4)}=-\frac{e^4}{2m^2}\mathrm{tr}(P\{\hat a,\beta^*\beta\})`$、$\hat a\gt0$。
これは **3 つの正作用素の積のトレース**で、$`\{\hat a,\beta^*\beta\}`$ が一般に $\ge0$ でないため構造的な符号を持たない
（**2 作用素なら $\mathrm{tr}(A^{1/2}BA^{1/2})\ge0$ に割れる。違いは作用素の本数である**）。
**決定的な証人は「揃った核」**: $a$ が $`\mathrm{supp}\,\beta`$ 上で定数（$S$ 内の細い部分殻に台を持つ核）なら
$\Delta^{(4)}=-\frac{e^2\bar a}m\mathcal E_A^{\rm c}\lt0$ が**厳密に**出る。
大きさは $\alpha=1/137$ で $`|\Delta^{(4)}|/\mathcal E_A^{\rm c}=\frac{e^2\bar a}m\lesssim0.5\%`$（$\lambda\le512$;
audit77 の延長で $\lambda\le3.3\times10^4$ でも $`\lesssim0.6\%`$ に飽和）。
稿 `77_` §3 の 2 帽族も両符号を実現するが、**この族は空間パリティ偶であり（audit77 (R3)）、
$\ell=1$・$\perp\alpha_0$ も課していないので許容族の内部ではない。証人としては「揃った核」を使うこと。**

**⚠ 次数勘定は展開（$\psi_0$ の $e$ 漸近展開。E05-P12 の 1. が「未証明の解析的前提」と明記したもの）に依存する。
ただし「揃った核で $\Delta^{(4)}\lt0$」は 1 ループ $\alpha_0^{(1)}$ を代入した算術であり、展開の成否に依らず成り立つ。**

**再挑戦禁止の範囲（証明が実際に排除した分岐のみ。T60）**: 「$\Delta\ge0$ が $\beta$ 一様に成り立つ」型の主張、
および「$P\ge0$・$\beta^*\beta\ge0$ の構造的非負性がそのまま $\mathcal E_A^{\rm full}$ に届く」型の論法。

**生きている分岐（本項で殺していない）**:
(a) 許容族（$\ell=1$・$\perp\alpha_0$・窓・$S\times S$ 台）に限った
$`\mathrm{Re}\,\Delta^{(4)}\ge-C\alpha\,\mathcal E_A^{\rm c}`$ 型の $\Lambda$ 一様な**下界**。
**audit77 の数値により見通しは良くなった**（$`\sup_S a\simeq0.066\,m`$、殻上の変動比 $\simeq2.38$ が
ともに $\Lambda$ 一様に飽和する）。**残る真の障害は非可換補正**で、
$\hat a=a_{\max}\mathbb 1-(a_{\max}-\hat a)$ と分けても第 2 項が再び 3 正作用素型になる。
(b) $O(e^6)$ 部（$\rho$・奇成分）の非摂動評価。
(c) **展開 (iv)（$\psi_0$ の $e$ 漸近展開）そのものの証明**（稿 `77_` §5 はこれを挙げていないが、
(a)(b) を埋めても (iv) が無ければ 3→2 は出ない。audit77 (R5)）。

## F47 （2026-09-12、audit79 が w160 の提出を差し替え、稿 `75_単調性M_qの真偽.md`、`verifier-backed`）— 単調性 (M) を「恒等式 + 平方完成 + 横断性 + 窓 + $H=\frac{\pi^2}{2m}+H_f$ の形」だけから証明する道

**【2026-09-12 audit82 の訂正注記】本項の「再挑戦禁止の範囲」末尾の
「『回転不変性を使うと書かなければ受け付けない』という運用にしてはならない（$\langle\pi\rangle_{\psi_0}=0$ だけで
足りる可能性が開いている）」は**偽になった見込みが高い**。$\langle\pi\rangle_{\psi_0}=0$ を対称性から厳密に持ち、
$E(P)\ge E(0)$ も走査範囲で破らない $D_{3h}$ 有限モード模型が (M) 自体を破る（$\max_{\hat q}M_{\hat q}(q,s)/M_{\hat q}(0,0)=1.021$）。
**audit83 が独立再実装で確認した（2026-09-12）。詳細は本台帳の `F50`**
（(研究ノート: `80_V1aのMの破れ_audit83_2026-09-12.md`)。audit82 のコードを読む前の独立実装が 4 点すべてを $10^{-4}$ 以内で再現、
$N_{\max}=14$ まで収束、余裕 $2.08\%$ は収束の揺れの約 95 倍）。
**以後の発注には「等方性 $M_{\hat n}(0,0)=\frac M3$ ／ 連続体の 2 偏極角度構造 の"どちらを"証明のどこで本質的に使うか」を
1 行書かせること。** **⚠ ただし「回転不変性そのものを要求する」のは依然として強すぎる**——2 偏極角度構造だけで
足りる可能性は開いている（F50 の射程 2）。
**⚠ この失効は「$\langle\pi\rangle_{\psi_0}=0$ だけを材料にする」1 点に限る。** 本項の他の記載
（閉鎖の本体、$E(P)\ge E(0)$ を含めない理由、付随して確定した事実）は**すべて有効**。

**⚠ この項は (研究ノート: `w160.FAILED.md`) を差し替えたものである。** w160 の版は閉鎖の射程に
**$E(P)\ge E(0)$** を含めていたが、**反例模型はその材料を満たしていない**（下記「含めない材料」）。
audit79（(研究ノート: `75_単調性M_qの真偽_audit79_2026-09-12.md`) §5）が独立実装で確認し、射程を狭めた。

**閉じた主張**: 発注 w160（および稿 `73_` §6 の「次の一手 1.」）が指示した道筋のうち、
**(M)** $\ M_{\hat q}(q,s)\le\frac M3$ を、次の**5 つだけ**から作用素不等式として導くこと。
1. 恒等式 $H(-q)=H+\frac{q\cdot\pi}m+u$（厳密）
2. 平方完成 $\frac{q\cdot\pi}m+u=\frac{(\pi+q)^2-\pi^2}{2m}$（厳密）
3. Coulomb ゲージの横断性 $`\epsilon_\lambda\!\cdot\!k=0`$
4. 窓 $W_{S,Q}$（$s\ge\Lambda$、$u\le\Lambda$、$|q|\le Q$、および $`\omega=\|k\|`$ が強制する $|q|\le s$）
5. $H=\frac{\pi^2}{2m}+H_f$ の形

**正確な障害（存在言明。初等・数値）**

**この 5 つをすべて満たす有限モード PF が (M) を破る。** 模型: $M=4$ モード、1 偏極/モード、$`\epsilon_j\!\perp\!k_j`$、
$|k_j|=(0.35,0.55,0.78,1.00)\Lambda$、方向の最小 $\cos=-0.52$（**対心対なし**＝15_ の罠を回避）、
$\lambda=\Lambda/m=2$（**この値が要る**。$\lambda\lt2$ では $Q\gt\Lambda$ となり窓の隅 $(|q|,s)=(Q,\Lambda)$ が
運動学的に存在しない）、$H=\frac{(P_f+eA)^2}{2m}+H_f$、Fock 切断 $N\le N_{\max}$、$e=2$。
**$\varepsilon(q)=\min\mathrm{spec}H(-q)-E_0\ge0$ は走査の各点で合否条件として課した**（別立ての診断にしない）。

$R:=M_{\hat q}(q,s)/M_{\hat q}(0,0)$、$R_{M/3}:=M_{\hat q}(q,s)\big/\frac13\sum_\nu M_\nu(0,0)$ の窓上の最大:

| $N_{\max}$（dim） | 6 (210) | 8 (495) | 10 (1001) | 12 (1820) |
|---|---|---|---|---|
| $\max R$ | 1.885 | 1.433 | 1.354 | 1.449 |
| $\max R_{M/3}$ | 2.379 | 1.604 | 1.331 | 1.369 |

モード集合 4 種（$N_{\max}=10$）で $\max R_{M/3}=1.331,\ 1.064,\ 1.518,\ 1.448$（**すべて $\gt1$**）、
$\max R=1.354,\ 0.953,\ 1.289,\ 1.332$（**4 集合中 3 集合で $\gt1$**）。
(研究ノート: `149_audit79_repaired_counterexample.py`)、`149_audit79_finite_mode_window.py`（K4・K5）。
$N_{\max}$ 収束は単調でなく、$N_{\max}\ge8$ で $1.35$〜$1.45$ の範囲に収まる（$N_{\max}=14$ 未実施）。

**⚠ この閉鎖に含めない材料（重要。ここが w160 版との差である）**

- **$E(P)\ge E(0)$（$\forall P$。**E05-F3**／**E05-F9**）は反例模型が満たしていない。**
  $H(P)=H-\frac{P\cdot\pi}m+\frac{P^2}{2m}$ は厳密なので $E(P)\le E_0-\frac{P\cdot\langle\pi\rangle_{\psi_0}}m+\frac{P^2}{2m}$、
  $P=\epsilon\langle\pi\rangle_{\psi_0}$ で $E(P)-E_0\le\frac{|\langle\pi\rangle|^2}m\epsilon(\frac\epsilon2-1)\lt0$（$0\lt\epsilon\lt2$）。
  **⟹ $\langle\pi\rangle_{\psi_0}\ne0$ である限り必ず破れる。** 実測 $E(P)-E_0=-2.65\times10^{-2}$（$|P|=0.23$、
  $E_0=2.80$、`149_audit79_EP_and_projection.py` CHECK L1）。有限標本の $\varepsilon(q)$ 走査は $\forall P$ の検証にならない
  （破れは窓よりはるかに小さい $|P|\simeq0.12$ で起きる。**T54**）。
  **弱い形 (A-min′) $E(P)\ge E(0)-|P|$（E05-P2 が要求するのはこちら）は満たしている。**
- **⟹ $\langle\pi\rangle_{\psi_0}=0$（$E(P)\ge E(0)$ と同値な帰結）を使う証明は、この反例では殺せない。**
  これは**回転不変性より真に弱い**材料である（回転不変性は $\langle\pi\rangle=0$ **かつ** $M_{\hat n}(0,0)=\frac M3$ を与える）。
  実際、**補題 75-1 が使うのは $\langle\pi\rangle_{\psi_0}=0$ と $K\gt0$ だけ**である。

**再挑戦禁止の範囲（狭く取ること。T60）**
「**上の 1〜5 だけ**から (M) を作用素不等式として出す」提案は、まず上の反例に当てて殺すこと。
**発注の前に「$\langle\pi\rangle_{\psi_0}=0$ ／ $M_{\hat n}(0,0)=\frac M3$ ／ 連続体の 2 偏極角度構造 の
どれを証明のどこで本質的に使うか」を 1 行書かせる。**
**「回転不変性を使うと書かなければ受け付けない」という運用にしてはならない**（$\langle\pi\rangle_{\psi_0}=0$ だけで
足りる可能性が開いている）。

**⚠ 閉鎖に含めないもの（明示）**
1. **(M) が偽であるとは言っていない。** これは**存在言明**であって実模型での (M) の反証ではない（**T60**）。
   有限モード ED は**無限次元性・稠密性・$\Lambda\to\infty$・E05-L4 をいずれも検証しない**。
2. **1 ループでは (M) は真である**（稿 `75_` 命題 75-3。各殻ごとに成立、必要条件は $u\le3s$ だけで窓より因子 3 緩い、
   窓上の比の上限は $\frac12$＝**余裕は因子 2**。audit79 が独立に再導出し、$\lambda=1$〜$10^6$ の 11 点を 4 桁一致で再現）。
3. **判定条件 (C)**（稿 `75_` 系 75-2）**は開である。** $E_0$ を含まず（E05-L4 の非一様性を迂回）、
   $\phi_*$ の 1 次モーメントだけを要求する。**次の標的はこちら。**
4. **「$eA(0)$ チャネルが閉じた」とは言えない**（**T49**・**T60**）。(M) は $`\|\Phi_{\rm tot}\|^2\le1-\frac1h`$ の
   十分条件の 1 本にすぎず、厳密な等価形 $`\|\Phi_{\rm tot}\|^2=(s+u)^2\mathrm{Var}_\nu(E^{-1})`$（稿 `73_` §3.2 の 5.）は残る。
   **(X2-b) も B16 も開である。**
5. **代わりに $1-\frac1h\le c\alpha$ を標的にしてはならない**（E05-F1 により偽。緩めた $c\alpha\ln\lambda$ も実質空。**T68**）。
6. **$h(\lambda)$ の datum を含まない。オッズは動かない**（EVIDENCE 第 18 回の恒久判定）。

**付随して確定した事実（閉鎖ではない）**
- **秩序変数は $\rho:=\langle\pi_{\hat q}\rangle_{\phi_*}/(-|q|)$（閾値 1）であって $`\|\pi\psi_0\|/Q`$ ではない。**
  1 ループでは $\rho$ は $\lambda$ 一様に $0.447$ に飽和する（audit79 の独立求積: $\lambda=2,8,64,10^3,10^4,10^5,10^6$ で
  $0.1052,0.2536,0.3993,0.4379,0.4442,0.4459,0.4465$）のに、$`\|\pi\psi_0\|/Q=\sqrt{\alpha\lambda/2\pi}`$ は
  $\lambda=10^6$・$\alpha=1/137$ で $34.08$ に達する（それでも (C) も (M) も成立）。
  **「$`\|\pi\psi_0\|`$ が窓幅 $Q$ を超えるから (M) が危ない」という読みは偽である**（w160 が自己反証、稿 `75_` §5）。
- **反例の「循環でなさ」は $R$ で測る。** $R_{M/3}\gt1$ だけなら $M_{\hat n}(0,0)$ の非等方性で自動的に起きうる。
  $R\gt1$（方向平均を含まない強い形の破れ）が成り立つ集合だけを反例として数えること
  （モード集合 4 種のうち 1 種は $R=0.953\lt1$ で $R_{M/3}=1.064\gt1$＝循環型だった）。

---

## F48 （2026-09-12、稿 `79_pull-throughの再開.md`、`verifier-backed`）— $R_{12}$ を作用素ノルムで括り出す pull-through 評価で $\langle N_S^2\rangle_0$ の冪を下げる道

> **⚠ 親へ（T55）**: F 番号は `F-?` のまま。連結時に採番すること。
> **出所**: 稿 `79_pull-throughの再開.md` は **w164 が導出**、**audit81 が検証して本台帳文を起草した**
> （w164 は 429 で消え (研究ノート: `w164.FAILED.md`) を書けていない）。

---

| ID | 閉じた主張 | 正確な障害 |
|---|---|---|
| F48 | **$R_{12}$ を作用素ノルムで括り出す pull-through 評価の「定数を良くして」$\langle N_S^2\rangle_0$ の冪を下げる** | **$c=1$ が鋭い。改善余地はゼロ**（各点）／**高々 4 倍**（積分後）。実際に走らせると $p=4$（一般）／$p=24/7$（遠紫外）で `E05-P14` より**冪でちょうど 2 悪い** |

**詳細**。$S=[\Lambda/2,\Lambda]$、$q=k_1+k_2$、$s=\omega_1+\omega_2$、$R_{12}=(H(-q)-E_0+s)^{-1}$ とする。
`E05-P2` の第 1 式に $`\|a_1a_2\psi_0\|\le\frac{e^2c_1c_2}{m}\|R_{12}\|\,\|T_{12}\psi_0\|`$ と当てて
$`\langle N_S(N_S-1)\rangle_0=\iint_{S^2}\|a_1a_2\psi_0\|^2`$ を評価する道（**分離型 pull-through**）は、
**E05-F23 によって死因（共線特異性）が消え、未評価因子も残さずに完走する**（`E05-P?`（1 本目））。
しかし次の 3 点で**冪の改善には決して至らない**:

1. **レゾルベント段に余地が無い。** $`\|R_{12}\|=\frac{1}{s+\mathcal E(-q)}`$ は恒等式で、
   背中合わせ点 $k_2=-k_1\in S$ では $\mathcal E(0)=0$ ゆえ $`\|R_{12}\|=\frac1s`$ が**等式**。
   したがって $S\times S$ 上一様な $`\|R_{12}\|\le\frac cs`$ は **$c\ge1$** を強制する（**無条件。公理を使わない**）。
   $\mathcal E(q)$ の下界を持ち込んでも、E05-F20（$\mathcal E\le\min(u,|q|)$）と $|q|\le s$ により
   積分後の利得は**高々 4 倍（振幅で 2 倍）**で、$\lambda$ の冪は 1 つも取れない。
2. **反跳 $u=\frac{q^2}{2m}$ が原理的に入らない。** $S\times S$ 上 $\frac us$ は最大 $\lambda$ に達するが、
   作用素ノルムで括り出す限りこの $\lambda$ は使えない（1. による）。
   1 ループの真値が $p=\frac12$ なのは $R_{12}\Omega=\frac1{s+u}\Omega$ を使っているからである。
3. **走らせた結果**。$\mathcal E=\frac{2E_0}\Lambda$ として
   $\langle N_S^2\rangle_0\le\frac{9\alpha^2\lambda^2}{16\pi^2}(1+4\sqrt{\mathcal E(1+\mathcal E)})^2+\mathcal E$ から
   **$p=4$、$a=4$**（$\mathcal E\le t=\frac{\alpha\lambda}\pi$、E05-P10）、**$p=24/7$、$a=18/7$**（$\mathcal E\le2C_2\alpha^{2/7}\lambda^{5/7}$、E05-L4）。
   `E05-P14` の $p=2$／$p=10/7$ に対し**どちらも冪でちょうど 2 悪い**（定数では埋まらない。**T57**）。
   本経路が勝つのは $t\le0.13863$（$\alpha=\frac1{137}$ で $\lambda\le59.7$）の**有界窓**だけで Q3 に無意味。

**⚠ 再挑戦禁止の範囲（証明が実際に排除した分岐だけ。T60）**。閉じたのは
**「$R_{12}$ を作用素ノルムで括り出し、残りを $`\|T_{12}\psi_0\|`$ に押し付ける鎖の、定数または $\mathcal E(q)$ 下界による改善」**だけである。
**以下は閉じていない（開である）**:
- **$R_{12}$ をベクトルに当てたままにする鎖**——`E05-P2` 第 2 式の前因子 $\frac1{s+u}$、$R_{12}\Omega=\frac1{s+u}\Omega$、
  $K^{-1}$ のスペクトル測度 $d\langle w,E_K(\cdot)w\rangle$（$w=T_{12}\psi_0$）、稿 `73_` §5 の標的 (B′)、
  `PROVED.md` の $M_{\hat q}$ 型。**反跳の $\lambda$ 利得はこちらでは実際に取れている。**
  （`FAILED.md` の $\Phi_{\rm tot}$ の項が既に「$R_{12}$ とベクトルを分離しない鎖は対象外・開である」と書いており、本項はその定量形。）
- **$`\mathcal T=\sup\|T_{12}\psi_0\|`$ 側の改善**（真値は $O(1)$、本経路の評価は $\sim\frac{4\alpha\lambda}\pi$）。
  **原理的な障害は同定されていない。ただし $\mathcal T=O(1)$ を得ても $p=2$ にしかならず `E05-P14` と同じで、改善にはならない。**
- **窓つきの 2 次モーメント $\mathcal N^\perp_{S,Q}$ を pull-through で攻める分岐**（稿 `76_` §2.2 の死因は
  そもそもここに及ばない。**T75**）。窓の中ではレゾルベント段は $1+\sqrt{2/\lambda}\to1$ 以内で鋭いので、
  そこで残る $\sqrt\lambda$ は**レゾルベントの緩さではない**。

**⚠ この項は Q3 のオッズを動かさない（T49）。** $h(\lambda)$ の datum を含まず、上界の発散は反証ではない。

**所在**: 稿 `79_pull-throughの再開.md`（w164）、
監査 (研究ノート: `79_pull-throughの再開_audit81_2026-09-12.md`)（audit81、S2、(R3) で稿の天井の値を $\frac12\to1$ に訂正）、
数値 (研究ノート: `150_w164_pullthrough_measure_and_powers*`)・(研究ノート: `153_audit81_ceiling_and_measure*`)。

## F49（**(C) への**「全域一括の 2 次モーメント経由」の道と、**(C) にも (M) にも届かない**「$\langle\pi\rangle_{\psi_0}=0$ 単独」の道）

- 日付: 2026-09-12。出所: 稿 `80_判定条件Cの攻め方.md` §1・§2・§3（w165 導出、w165b 確定）。格付け: `candidate`（数値は 3 段格子／3 段 $N_{\max}$ で不変）。
- **閉じた道 1（(Q1)-1）**: E05-F23（$K\ge s$、射線 $P=-tq$）から出る (C) の十分条件は
  $\langle H-E_0\rangle_{\phi_*}\le\frac{(u+s)^2}{4u}$（最悪隅で $\le s$）または Cauchy–Schwarz $\sqrt{\langle\pi_{\hat q}^2\rangle_{\phi_*}}\le\frac{m(u+s)}{|q|}$ で、
  いずれも $\phi_*$ の **2 次モーメント**を要求する。1 ループでは $\langle H-E_0\rangle_{\phi_*}/s\simeq\frac32\ln\lambda$（$\lambda=10^6$ で $18.6$）、
  CS 比 $\propto\sqrt{\ln\lambda}$（$1.98$）で発散し、$\lambda\ge2$ で既に不成立
  （$\phi_*$ の UV 重み $\propto k^{-3}dk$、エネルギー $\propto k^2$。固定 $r$ の作用素不等式は異方性抑制 $r(k)\simeq2Q/k$ を見ない）。
  **射程（audit82）**: (i) これらの比は $\phi_*$ の**規格化された**期待値で $e$ に依らないので、十分条件が 1 ループで偽である以上
  **小 $\alpha$ の真の模型でも偽**＝T51 の留保は不要で、kill は稿が言うより強い。
  (ii) **閉じたのは「$k$ に依らない固定の重み」の 2 次モーメントだけである。**
  $`(|k|,\hat k\!\cdot\!\hat q)`$ のセルに局所化した Cauchy–Schwarz（これも 2 次モーメントのみを使う。光子運動量の直交分解なので厳密）は
  $\lambda$ 一様で、$\lambda=10^6$ で $64\times8$ セルの上界 $0.909\lt1$、セル幅 $\to0$ で真値 $0.886$ に収束する
  （(研究ノート: `154_audit82_cellCS.py`)）。**「2 次モーメントを経由する評価は原理的に届かない」と書いてはならない**（**T60**）。
  対して (C) が要る 1 次モーメントは $\rho\to0.447$、$\langle|\pi_{\hat q}|\rangle_{\phi_*}/Q\to0.887$ に飽和する。
- **閉じた道 2（(Q1)-2 単独）**: $\langle\pi\rangle_{\psi_0}=0$ は $\langle K\rangle_{\psi_0}=\sigma$ の 1 等式しか与えず、(C) の左辺
  $\langle K^{-1}\psi_0,(H-E_0)K^{-1}\psi_0\rangle$ を制御しない（補題 80-2）。実証: $\langle\pi\rangle_{\psi_0}=0$ を厳密に持つ $D_{3h}$ 有限モード模型
  （$\lambda=2$、$\varepsilon(q)\gt0$、gap $\simeq1.2$）で $\rho=1.205,1.224,1.217$（$N_{\max}=6,8,10$）。等方性（$T_d$）を加えても $\rho=1.14$〜$1.17$。
- **閉じた道 3（(Q1)-3）**: 平方完成は補題 80-2 の恒等式に吸収され、新情報を出さない。
- **射程**: (C)・(M) 自体の真偽は動かない（1 ループ $\rho=0.447$ で因子 2.2 の余裕）。閉じたのは
  (1)「**$k$ に依らない固定重みの** 2 次モーメントを経由する評価」（局所化版は開いている。上記）と、
  (2)「$\langle\pi\rangle_{\psi_0}=0$ **だけ**を使う評価」で、**(2) は (C) だけでなく (M) も殺す**
  （$D_{3h}$ 模型 V1a: $\rho=1.22$ かつ $\max_{\hat q}M_{\hat q}(q,s)/M_{\hat q}(0,0)=1.021$、$N_{\max}=6,8,10,12$ で収束、
  極角 $`45^\circ\!\sim\!80^\circ`$ の 5 集合すべてで $\gt1$。audit82）。
  **⟹ F47 が「$\langle\pi\rangle_{\psi_0}=0$ だけで足りる可能性が開いている」と書いた道は閉じた。**
  **【2026-09-12 audit83 が独立再実装で確認。正本は `F50`】** 余裕 $2.08\%$ は $N_{\max}$ 収束の揺れの約 95 倍。
  **⚠ ただし下の「E05-F23 を併用する道も同時に殺している」は audit83 が 2 点で訂正した**（正確な形は **`F50` の射程 5**）:
  **(a) 本閉鎖は $E(P)\ge E(0)$ を必要としない**（必要なのは $\langle\pi\rangle_{\psi_0}=0$ の記号的厳密性だけ）。
  **(b) E05-F23 を V1a の根拠に引いてはならない**——E05-F23 は連続体・2 偏極・$\hat\varphi(k)=\hat\varphi(-k)$ の PF についての
  定理で、**1 偏極の有限モード模型＋Fock 切断はその仮定を満たさない**。V1a が $E(P)\ge E(0)$ を破らないことは
  **1550 点の走査＋局所最小化による数値事実**であって $\forall P$ の証明ではない（**T78**）。
  組み合わせるべき材料は**等方性 $M_{\hat n}(0,0)=\frac M3$**（＝回転不変性の残り半分）で、これを足すと $T_d$ 模型では
  (M) だけが復活する（$\max_{\hat q}R=0.979\lt1$、$\rho=1.18\gt1$）。**(C) は (M) より真に強い。**
  この反例は $E(P)\ge E(0)$ も走査範囲（$|P|\le2$、570 点、陽性対照つき）で破らないので、
  **E05-F23 を併用する道も同時に殺している**（F47 の反例との決定的な差。**T78**）。ただし $\forall P$ は有限標本で検証できない。
  有限モード模型で $\rho\gt1$ を駆動したのは、対数スケールの半分が欠損 3（連続体の測度の離散化。動径 ×2.04 が主、角度 ×1.32 が従）、
  残り半分が**第 4 の軸（有限個のモードへの結合集中による多光子増幅 ×3.5）**である（audit82）。
  有限モードの破れは連続体での (C)・(M) の否定にならない。
- **残る設計**: 1 次絶対モーメント $\langle|\pi_{\hat q}|\rangle_{\phi_*}$ を $k$ 依存の異方性抑制を保ったまま押さえる不等式（稿 `80_` 系 80-4・§6 の 4.）。

## F50 （2026-09-12、audit82 が発見・audit83 が独立再実装で検証、稿 `80_判定条件Cの攻め方.md` §4、`verifier-backed`）— 単調性 (M) を「$\langle\pi\rangle_{\psi_0}=0$ **だけ**」を材料にして証明する道

**⚠ 親へ**: 本項は F47 の「再挑戦禁止の範囲」末尾の運用指示を差し替える。F47 は `verifier-backed` なので
**本文を書き換えず**、F47 冒頭の audit82 注記（「audit83 の判定が出るまで撤回済として引用しないこと」）を
**「audit83 が独立再実装で確認した。本項 F50 を参照」に置き換える**こと。

**閉じた主張**: 判定条件 (C)（系 75-2）でも単調性 (M)（$M_{\hat q}(q,s)\le\frac M3$）でもよいが、その証明の材料として
**$\langle\pi\rangle_{\psi_0}=0$（$\Leftrightarrow$ $P=0$ が $E(P)$ の臨界点）だけ**を使うこと。
補題 75-1 が使うのは $\langle\pi\rangle_{\psi_0}=0$ と $K\gt0$ だけなので、この材料しか使わない証明は
**等方性 $M_{\hat n}(0,0)=\frac M3$ を持たない模型でも通らねばならず、その場合の意味のある形は
$R:=M_{\hat q}(q,s)/M_{\hat q}(0,0)\le1$（同一方向。$\frac M3$ との比ではない。**T80**）である。**

**正確な障害（存在言明。初等・数値）**: **$\langle\pi\rangle_{\psi_0}=0$ を対称性から厳密に持つ有限モード PF が $R\gt1$ を与える。**

模型 **V1a**: $m=\frac12$、$\Lambda=1$（$\lambda=\Lambda/m=2$、$Q=\sqrt{2m\Lambda}=1$）、**6 モード**を
$D_{3h}$ の 1 軌道に置く（$|k_j|=\Lambda$、極角 $\theta=70^\circ$、方位角 $0,120,240^\circ$ の上下 2 枚。
**対心対なし**＝15_ の罠を回避）、**1 偏極/モード**で $\epsilon_j\propto\hat z\times\hat k_j$、
$A(0)=\sum_j\frac{\epsilon_j}{\sqrt{2\omega_j}}(a_j+a_j^*)$、$H(P)=\frac{(\Pi-P)^2}{2m}+H_f$、$\Pi=P_f+eA(0)$、$e=1$、
Fock 切断 $\sum_jn_j\le N_{\max}$。窓の最悪隅 $(|q|,s)=(Q,\Lambda)$。

| $N_{\max}$（$\dim$） | 6 (924) | 8 (3003) | 10 (8008) | 12 (18564) | **14 (38760)** |
|---|---|---|---|---|---|
| $\max_{\hat q}R$ | 1.0421 | 1.0260 | 1.0196 | 1.0211 | **1.0208**（audit83 が追加） |

**収束**: 最後の 2 段 $1.02105\to1.02083$ で相対差 $2.2\times10^{-4}$（$0.022\%$）。
**$1$ からの余裕 $2.08\%$ は、この収束の揺れの約 $95$ 倍である。** $N_{\max}=6,8,10$ だけを見ると単調減少で
外挿すると $1$ を割って見えるが、**$N_{\max}=12$ で反転し $14$ で平坦になる**（audit83 が独立実装でも同じ形を再現）。

合否条件は全段で成立: $\varepsilon(q)=0.33\gt0$、gap $=2.46\gt0.3$、$`|\langle\pi\rangle|/\|\pi\psi_0\|\le2\times10^{-15}`$、
$\lambda=2$、$|q|=Q\le\min(s,Q)$、$u=\Lambda\le\Lambda$（**T79** の窓の運動学を満たす）。
$\max_{\hat q}\rho=1.217\gt1$ なので **(C) も同時に破れる**。

**$\langle\pi\rangle_{\psi_0}=0$ が厳密である理由（記号的。数値の $10^{-15}$ ではない）**:
$C_3$（$z$ 軸まわり $120^\circ$）と $\sigma_h$（$z\mapsto-z$）はモード集合を置換し偏極を同変に写すので、
置換ユニタリ $U_g$ が定まり $U_g\Pi U_g^*=g^{-1}\Pi$、$U_gH(0)U_g^*=H(0)$（**切断 $\sum n_j\le N_{\max}$ は置換不変なので
切断空間でも厳密**）。$\psi_0$ は非縮退（gap $=2.46$）だから $\langle\Pi\rangle_{\psi_0}=g\langle\Pi\rangle_{\psi_0}$ が
全 $g\in D_{3h}$ で成り立ち、$D_{3h}$ のベクトル表現の不変部分空間は $`\{0\}`$。**⟹ $\langle\pi\rangle_{\psi_0}=0$ 厳密。**

**検証（`verifier-backed` の根拠）**: audit83 が **audit82 のコードを読む前に**記述だけから独立再実装し
（(研究ノート: `155_audit83_core.py`) ほか）、単位換算（audit82 の $m=\frac12,\Lambda=1,e=1$ は
audit83 の $m=1,\Lambda=2,e=2\sqrt2$ に相似）を合わせて **$N_{\max}=6,8,10,12$ の 4 点すべてを
$10^{-4}$ 以内で再現**した（`155_audit83_exact_replication.py`）。さらに次を独立に潰した:
$N_{\max}$ 収束（$14$ まで。最後の 2 段で相対差 $1.3\times10^{-4}$）、線形代数（CG 許容誤差を $10^6$ 倍変えて $R$ は 11 桁不変、
$K$ の条件数 $161$、分母 $M_{\hat q}(0,0)=0.41$ で小さくない）、$\hat q$ 格子（粗 14 / 細 134 / 球面局所最大化が 5 桁一致。
$R\gt1$ は 134 方向中 4〜7 方向で起き孤立点ではない）、切断規約（$\Pi$ を切断してから 2 乗／$\Pi^2$ を切断、どちらでも $\gt1$）、
$R$ と $R_{M/3}$ の別（$\max R_{M/3}=1.49$ で $1.021$ とは別物。**T80 の循環ではない**）。
記録: (研究ノート: `80_V1aのMの破れ_audit83_2026-09-12.md`)。

**⚠ 射程（T60。ここを狭く取ること）**

1. **閉じたのは「$\langle\pi\rangle_{\psi_0}=0$ だけを材料にする (M)／(C) の証明」だけである。**
   **(M) が偽だとは言っていない。** これは存在言明であって実模型での (M) の反証ではない。
2. **$\langle\pi\rangle_{\psi_0}=0$ を他の材料と組み合わせる道は開いている。** F47 が挙げた 3 材料のうち
   **残る 2 つ——等方性 $M_{\hat n}(0,0)=\frac M3$、連続体の 2 偏極角度構造 $\sum_\lambda\epsilon^i\epsilon^j=\delta^{ij}-\hat k^i\hat k^j$——は
   V1a が持たない**（V1a は非等方かつ 1 偏極）。**どちらを使う証明も本項では殺せない。**
   audit83 が $D_{3h}$ を 2 偏極（横射影は厳密）にして試したが、到達できた $N_{\max}\le6$ は全く未収束で
   **INCONCLUSIVE**。「2 偏極でも破れる」と書いてはならない。
3. **有限モードの破れは連続体での (M) の否定にならない**（**T49**・**T64**）。有限モード ED は
   無限次元性・稠密性・$\Lambda\to\infty$・E05-L4 をいずれも検証しない。連続体では 1 ループで (M) は真
   （命題 75-3、窓上の比の上限 $\frac12$＝余裕は因子 2）、(C) も $\rho\to0.447$ で因子 2.2 の余裕がある。
4. **破れは窓の最悪隅 $(|q|,s)=(Q,\Lambda)$ に接する狭い領域に限られる**（audit83 が新たに測った）。
   $N_{\max}=10$ の実測で $R\gt1$ となるのは $`\{|q|\gtrsim0.94Q,\ s\lesssim1.03\Lambda\}`$ で、
   **2 次元の広がりはある（測度 0 ではない）が小さい**。窓の内部に入ると急落する
   （$|q|$ を $0.75Q$ に下げると $0.942$、$s$ を $1.25\Lambda$ に上げると $0.898$）。
   **「窓上で広く破れる」と書いてはならない。** 隅は E05-P15 の 2. の AM–GM 等号点である。
5. **$E(P)\ge E(0)$ は V1a では「走査範囲で破れなかった」に留まる**（**T78**）。
   audit83 が 1550 点（方向 62 本 $\times$ $|P|\in[0.05,12]$ の 25 点。1 光子放出枝が下がりうる
   $|P|\simeq\Lambda$ とモード方向 $\pm\hat k_j$ を明示的に含む）と 12 点からの局所最小化で調べ、
   最小は常に $P=0$ だったが、**$\forall P$ の証明ではない**。
   **⚠ E05-F23 を V1a の根拠に引いてはならない**——E05-F23 は連続体・2 偏極・$\hat\varphi(k)=\hat\varphi(-k)$ の
   PF に対する定理で、**1 偏極の有限モード模型 + Fock 切断はその仮定を満たさない**。
   なお**本項の閉鎖は $E(P)\ge E(0)$ を必要としない**（必要なのは $\langle\pi\rangle_{\psi_0}=0$ だけで、それは上のとおり厳密）。
6. **モード集合依存性の確認は $N_{\max}$ とセットで読むこと。** 極角 $`\theta=45^\circ\!\sim\!80^\circ`$ の 5 集合すべてで
   $\max_{\hat q}R\gt1$ という確認は **$N_{\max}=8$ での話**である。audit83 が $N_{\max}=10$ に上げると
   $1.0191,1.0196,1.0155,1.0122,\mathbf{1.0049}$ となり、**$\theta=80^\circ$ の余裕は $0.5\%$ しかない**。
   $N_{\max}\ge10$ で確認できているのは $\theta=65^\circ,70^\circ$ である。
7. **$h(\lambda)$ の datum を含まない。オッズは動かない**（EVIDENCE 第 18 回の恒久判定）。
8. **「$eA(0)$ チャネルが閉じた」とは言えない**（**T49**・**T60**）。厳密な等価形
   $`\|\Phi_{\rm tot}\|^2=(s+u)^2\mathrm{Var}_\nu(E^{-1})`$（稿 `73_` §3.2 の 5.）は残り、**(X2-b) も B16 も開である。**

**運用（F47 の当該指示の差し替え）**: 以後、**(M)／(C) を狙う発注には
「等方性 $M_{\hat n}(0,0)=\frac M3$ ／ 連続体の 2 偏極角度構造 のどちらを証明のどこで本質的に使うか」を 1 行書かせる。**
**$\langle\pi\rangle_{\psi_0}=0$ だけを材料にする提案は V1a に当てて殺す。**
（F47 の「『回転不変性を使うと書かなければ受け付けない』という運用にしてはならない」は**この 1 点に関して失効**する。
ただし**回転不変性そのものを要求するのは依然として強すぎる**——2 偏極角度構造だけで足りる可能性は開いている。）


## F51（「有限モード ED で $\Delta=\mathcal E_A^{\rm full}-\mathcal E_A^{\rm c}$ の符号・大きさを直接見て $O(e^4)$ の $aa$ 型 1 本を検査する」— 同次数の汚染で無感度。2026-09-12、w167、稿 `81_` 観察 81-4）

格付け: `self-audited`（数値は (研究ノート: `157_w167_EA_full_split_ED.py`)＝seed 1670912・3 段 $n_{\max}=4,5,6$・`conclusion: INCONCLUSIVE`、および `157b_w167_odd_part_exponent.py`。**⚠ 157b は $n_{\max}=6$ の 1 段のみで、`result.json` に seed・ライブラリ版・入力 hash・`conclusion` が記録されていない**（audit85 が指摘）。**冪の値は 157b 由来、切断不変は 157 の $\mathcal E_A^{\rm odd}$（$n_{\max}=5,6$ が 0.15% 一致）で担保される。**

**閉じた主張**: 有限モード PF（横偏極・非対心・$\lambda\ge2$）の ED で $\mathcal E_A^{\rm full}$ の残差を測り、連続体の $O(e^4)$ 部（E05-P13 の $aa$ 型 1 本 $-\frac{e^4}{m^2}\mathrm{tr}(P\hat a\beta^*\beta)$）の
符号・大きさを検査する（発注 w167 (Q3)）。

**正確な障害**: 有限モードは回転不変でないので $\psi_0$ の 1 光子成分が $O(e^3)$ で生き残り（実測 $`\|\Pi_1\psi_0\|=1.9\times10^{-4},1.3\times10^{-3},6.6\times10^{-3}`$、$e=0.15,0.3,0.6$。局所冪は $2.79$ と $2.34$ で、**$e$ が大きいほど下がる**。$e\to0$ 側の読みが 3）、
$`\{P_f,A\}`$ 部（連続体では $O(e^6)$）が **$O(e^4)$** に落ちてくる（$\log_2$ 比 $3.62\to2.40$）。その大きさは $A^2$ 部の交差項の **8 倍**（$e=0.3$、aligned 核: $+1.17\times10^{-3}$ vs $-1.38\times10^{-4}$）で符号は正。
ゆえに ED の $\Delta$ は連続体の $\Delta^{(4)}$ と同次数の別物に支配され、符号検査は**無感度**（T64。循環ではなく感度の欠如）。
横条件は $\phi_1=0$ を有限モードでも強制するが $\phi_3$ の 1 光子成分には届かない（T78 の含意チェック）。

**再挑戦禁止の範囲（証明が実際に排除した分岐のみ。T60）**: 「回転不変でない有限モード集合の ED で $\Delta$ または $\mathcal E_A^{\rm full}$ の**符号**を測って E05-P13 の $O(e^4)$ 部の符号を判定する」型。

**生きている分岐**: (a) ED で $A^2$ 部と $`\{P_f,A\}`$ 部を**分けて**測ること（分解は厳密。稿 `81_` 命題 81-1 の公式と行列積は 3 段で一致）。
(b) 平方完成の下界（命題 81-2）の成立・鋭さの検査（48 ケースで成立、余裕大）。(c) 回転不変な切断（球面調和展開の $J$ 切断）による ED は本項の射程外。

## F52（「$\Pi_1\psi_0\equiv0$（厳密・全次数）だけで奇部 $\mathcal E_A^{\rm odd}$ の $O(e^6)$ を展開 (iv) 抜きで出す」— 光子数の言明は $e$ 次数の言明に翻訳できない。2026-09-12、w169、稿 `83_`）

格付け: `self-audited`（稿 `83_` §2・§6。数値は (研究ノート: `161_w169_odd_part_vacuum_free_split.py`)、seed 1690912、3 段 $n_{\max}=6,8,10$、`conclusion: PASS`）。

**閉じた主張**: 発注 w169 (Q1)「奇部の次数勘定から展開 (iv) を外す」。

**正確な障害**: $\Pi_1\psi_0\equiv0$ と選択則が与えるのは $\mathcal E_A^{\rm odd}=\frac e{2m}\sum_\nu(\langle\Pi^{\ge2}_{\rm ev}\psi_0,Y_\nu\Pi^{\ge3}_{\rm odd}\psi_0\rangle+\text{転置})$（真空対項の消滅。厳密）まで。
これを $O(e^6)$ にするには $`\|(N+1)^2\Pi^{\ge2}_{\rm ev}\psi_0\|=O(e^2)`$・$`\|(N+1)^2\Pi^{\ge3}_{\rm odd}\psi_0\|=O(e^3)`$ が要り、非摂動在庫（E05-P5・P14: $N_S$ の 1・2 次モーメント）は $O(e)$ 級しか与えず、$`\|\Pi_{\rm odd}\psi_0\|`$ は $N_S$ モーメントでは縛れない（$N\ge3$ でも $N_S=0$ でありうる）。
要る最小の仮定は (iv′)（2 次までの展開 + 剰余の $(N+1)^2$ 重み付き $O(e^3)$ 評価）で、ギャップ無しなので E05-F22 からは従わない。

**再挑戦禁止の範囲（T60）**: 「$\Pi_1\psi_0\equiv0$ と在庫の $N_S$ モーメント（E05-P5・P14・P16）だけから奇部の $e$ 冪（$e^6$ でも $e^4$ でも）を非摂動に導く」型。

**生きている分岐**: (a) (iv′) の証明（$P=0$ ファイバーでの 2 次摂動 + 剰余評価。ギャップ無しなので soft-photon 型の分解能評価が要る。難）。(b) 命題 83-1 の双線形形を CS で重み付き上界にする（`81_` §7.1。重みが全 $N$ か $N_S$ かを先に判定）。(c) $`\|\Pi_{\rm odd}\psi_0\|`$ の非自明な非摂動上界（$\frac12(1-\langle\psi_0,(-1)^N\psi_0\rangle)$ 経由）。


## F53 入力 (i)（$`\|\rho_S\|_{op}`$ の $\lambda^{-1}$ 減衰）で $\mathcal E_A^{A^2}$ を $\Lambda$ 一様にする（w168、2026-09-12）

**閉じた主張**: 命題 81-2（**E05-P19**）の連鎖 $`\frac{(\mathrm{Re}\mathcal E_A^{A^2})_-}{D_{\rm free}}\le\frac{\alpha\lambda}\pi(1+\frac{2\alpha\lambda}\pi)\|\rho_S\|_{op}\varsigma`$ に
**$`\|\rho_S\|_{op}\lesssim\lambda^{-1}(1+\alpha\lambda)^{-1}`$ を入れて $\Lambda$ 一様性を出す**という設計（`92_` 枝 1 の入力 (i)、audit85 が挙げた 2 原因のうちの 1 つ）。

**正確な障害（3 段。稿 `82_rho_Sの作用素ノルム.md`、(研究ノート: `160_w168_rho_S_op_norm.py`)）**:

1. **比は減衰するが、要求は比ではなく絶対量である。**
   $`\frac{\|\rho_S\|_{op}}{\mathrm{tr}\rho_S}\simeq1.47\,\lambda^{-1/2}`$（1 ループ、$\lambda=4,16,64,256,1024,4096,16384$ の 7 段。
   局所傾き $-0.204,-0.322,-0.400,-0.448,-0.476,-0.490$、**最後の 2 段の差 0.014**）。
   すなわち **$`\|\rho_S\|_{op}\le\mathrm{tr}\rho_S`$ は $\sqrt\lambda$ 倍ゆるい**。
   **しかし $`\mathrm{tr}\rho_S=\langle N_S\rangle_0\simeq0.19\,\alpha^2\sqrt\lambda`$ も同時に増える**ので、
   **$`\|\rho_S\|_{op}`$ 自体は $\lambda$ について単調増加**（$0.0166\alpha^2\to0.2568\alpha^2$、15 倍）**し $\simeq0.28\alpha^2$ に飽和する。減衰しない。**
   **⟹ 標的 $\lambda^{-1}$ は 1 ループの係数関数と両立しない**（**T61 により kill ではなく見込みの測定**。81_ §7-3 の枠組み）。

2. **1 ループの真値を入れても冪はちょうど 1 つしか落ちない**（**「真値」は一貫して 1 ループ値である。T61**）。 $`\|\rho_S\|_{op}\simeq0.28\alpha^2`$ を代入して
   $`0.088\,\alpha^3\lambda(1+\frac{2\alpha\lambda}\pi)\varsigma`$、**$p=3\to2$**（$\alpha\lambda\le\pi$ では $2\to1$）。$\Lambda$ 一様には $p\le0$ が要る。

3. **残る $\lambda$ を出す $\langle A^2\rangle_0\lesssim\Lambda^2$ の段も 1 ループでは鋭い。**
   $A_\nu\psi_0=a^*(u_\nu)\Omega+O(e^2)$ より $\langle A^2\rangle_0=\frac{\Lambda^2}{4\pi^2}(1+O(\alpha\lambda))$ で、
   81_ §3 の上界 $\frac{\Lambda^2}{2\pi^2}(1+\frac{2\alpha\lambda}\pi)$ は因子 2 以内。**$\Lambda^2$ は真空ゆらぎであって評価の緩みではない。**
   3 入力（平方完成＝audit85 が破れ比 0.97 で鋭いと確認／$\langle A^2\rangle_0$／$`\|\rho_S\|_{op}`$）をすべて真値にしても
   $`0.044\,\alpha^3\lambda\,\varsigma`$（**$p=1$**）が残る。$\varsigma$ は **(H-$\varsigma$) が偽**（E05-P5 射程 1、audit69）なので使えない。
   **⚠ 訂正（audit86、2026-09-12）— 3 点**:
   **(a) 「因子 2 以内」は $\lambda$ 一様ではない。** 上界と 1 ループ真空値の比は $2(1+\frac{2\alpha\lambda}\pi)$ で発散し、
   因子 2 が言えるのは $\alpha\lambda\lesssim1$、すなわち残余がもともと $\Lambda$ 一様な領域だけである。
   非摂動では $\langle A^2\rangle_0\ge\frac{\Lambda^2}{4\pi^2}$ すら在庫に無い（$\frac{e^2}{2m}A^2\ge0$ はスクイーズする向き）。
   **(b) 「独立検算」は独立ではない。** 命題 81-3 と本経路は平方完成・$D_{\rm free}$ の下界・次数勘定を共有し、
   $\alpha^3\lambda$ への着地は共通構造から強制される。6.3 倍の出所も未特定である（**T75**）。
   **(c) 「残る自由度は $\varsigma$ だけ」は偽。** 整列 3 因子（$h_\nu$ と $\rho_S$ の最大チャネル、$\beta^*u_\nu$ と $\beta$ の最大特異ベクトル、
   $A_\nu\psi_0$ と $c_\nu\psi_0$）が「$`\|\rho_S\|_{op}`$」の 1 語に畳み込まれていて測られていない。**6.3 倍はその存在の証拠である。**
   **(d) ⚠ 窓判定（最重要）**: 残余 $0.044\alpha^3\lambda\varsigma$ が $O(1)$ に達するのは $\lambda\gtrsim23\alpha^{-3}$ で、
   **E05-L4 の摂動有効域 $\lambda\lesssim\alpha^{-5/2}$ の外である**（81_ §4 が命題 81-3 の同じ $\alpha^3\lambda$ に当てた判定と同じ）。
   **⟹ 1 ループの測定は有効域の内側で一度も障害を見ていない。本項の閉鎖は「1 ループ係数関数を真値の代理と見なす限り」である。**

**併せて閉じた小径**: **pull-through + E05-P10 の素朴連鎖**（他のエージェント 意見、親の査読 §1）。
値を正しく入れ形状因子 $c_k$ を戻しても $`\|\rho_S\|_{op}\le\frac{2\ln2}{\pi^2}\alpha^2\lambda^2`$ にしかならず、
$\alpha\lambda\gt\frac{\pi}{2\ln2}=2.27$ では `E05-P5` より悪い（冪が $p=1\to2$）。**この連鎖には戻らない。**
損は三角不等式にあり、捨てているのは $`\{R(k)\epsilon_\lambda(k)\!\cdot\!\pi\psi_0\}_{k\in S}`$ の $k$ についてのほぼ直交性である
（**E05-P10 は 1 ループで飽和するので、損は P10 側ではない**）。

**⚠ 閉じていないこと（T60。射程を広げないこと）**:
- **$\mathcal E_A^{A^2}$ 自体を反証していない。** 上界の発散は反証ではない（81_ §0）。閉じたのは**平方完成連鎖の入力を強くする設計**だけである。
- **$`\|\rho_S\|_{op}`$ の非摂動な $\Lambda$ 一様上界（$\le C\alpha^2$）は未解決で、価値がある**
  （3 項を同じ $p=1$ に揃える。ただしそれでも $\Lambda$ 一様化には足りない）。**この方向の発注を本項で止めてはならない。**
- **$\langle N_S\rangle_0$ の非摂動評価を $\alpha^2\sqrt\lambda$ 級まで締める道**は別問題で生きている。
  **⚠ 「$R_{\mathcal U}$・$R_2$ にも効く」は稿 `82_` では検算されていない**（audit86。**T75**）。E05-P5 第 1 式は $\langle N_S\rangle_0$ に線形なので
  $\mathcal U_1$ には効くが、$R_2$ の $\frac{4\alpha\lambda}\pi\varsigma$（72_ 命題 72-3）と $R_{\mathcal U}$ の $\langle N_S^2\rangle_0^{1/2}$（E05-P14）が
  $\langle N_S\rangle_0$ を経由するかは**発注前に 1 手で確かめること**。**効いても $p=1\to p=1/2$ で $\Lambda$ 一様化はしない。**
- **$\langle A^2\rangle_0$ の非摂動値が真空値より小さい可能性**（audit86 が追加）。$\alpha\lambda\gg1$ で $O(1)$ 以上の低減があれば
  $\langle A^2\rangle_0$ の段は $\Lambda^2$ より小さくなる。**この向きは一度も検査されていない。**
- **$\mathcal E_A^{A^2}$ を平方完成しない扱い**（交差項を $\langle A^2\rangle_0$ に逃がさず真空成分と殻成分を分離する）は生きている。
- 1 ループの数値は非摂動の**下界を与えていない**。「$`\|\rho_S\|_{op}`$ は減衰しない」を非摂動で言うには
  $`\|\rho_S\|_{op}\ge c\alpha^2`$ 型の無条件下界が要る（未着手）。

**副産物（親の懸念の裁定）**: 「pull-through の主要項の像が 3 次元に収まるなら $\rho_S$ はほぼランク 3」という懸念は
**機構としては正しく、比の言い方としては偽**。最大特異値のチャネルは $\lambda=4$ から $16384$ まで
**一貫して $J=1$ 電気型（＝双極子・ランク 3 チャネル）**であり、比が落ちるのは分母 $\mathrm{tr}\rho_S$ の増大だけによる。
**無反跳（双極子）極限では $J=1$ 電気型以外のチャネルが厳密に消え、$r=1/3$ が $\lambda$ に依らず成り立つ**（稿 `82_` 命題 82-2、数値で $0.33312$ が 4 段完全一致）。
**⟹ ランク 3 の絵は双極子近似そのものであり、フル PF で比が落ちるのは反跳 $\frac{|k_1+k_2|^2}{2m}$ が $J\ge2$ を開くからである**（機構は **E05-F7** と同じ）。

**T57 の再確認（4 例目）**: 位相空間勘定は有効チャネル数 $\sim(\lambda/2)^{3/2}$ から $r\sim\lambda^{-3/2}$ を予想するが、
実測は $\lambda^{-1/2}$ で **冪が 1 つ足りない**（$\lambda=1024$ で参加率 $9.46\times10^{-3}$ に対し $r=4.34\times10^{-2}$、4.6 倍の偏り。
トレースの 90% は $J\le13$ に入るのに $J=1$ 電気型だけが突出）。
**次数勘定を根拠に「$\varsigma$ 型の量が $\lambda^{-3/2}$ 減衰する」と書いてはならない。**

## F54（「素朴な pull-through + E05-F23 で $P=0$ の全光子数 $\langle N\rangle_0\lt\infty$ を出す」— 赤外端で対数 1 つ足りない。2026-09-12、w171、稿 `83_` §7.5）

格付け: `self-audited`（稿 `83_` §7.5・§7.6。数値なし。作用素の可換子と光子測度のみ）。

**閉じた主張**: 「在庫（E05-F23 + E05-P10）だけから $\langle N\rangle_0\lt\infty$（$P=0$、$V=0$、$\Lambda\lt\infty$）を出す」。

**正確な障害**: pull-through $(H_{[k]}-E_0+|k|)a_\lambda(k)\psi_0=-\frac{ec_k}m\epsilon_\lambda(k)\cdot\pi\psi_0$（$H_{[k]}=\frac{(\pi+k)^2}{2m}+H_f=H(-k)$）に
**E05-F23**（$E(P)\ge E(0)$）を当てると $`\|(H_{[k]}-E_0+|k|)^{-1}\|\le|k|^{-1}`$ が無条件で出るが、分子を $`\|\pi\psi_0\|=\sqrt{\mathcal K}`$ で押さえると
$`\sum_\lambda\|a_\lambda(k)\psi_0\|^2\le\frac{e^2c_k^2\mathcal K}{m^2|k|^2}`$ となり、$\langle N\rangle_0\le\frac{e^2\mathcal K}{m^2}\frac1{2\pi^2}\int_0^\Lambda\frac{dk}k=+\infty$。
**発散するのは赤外端だけ**（切断は UV にしか掛かっておらず、$H_f\ge|k|N$ は $|k|\to0$ で $N$ を抑えない）。紫外端は収束する。
不足は**ちょうど対数 1 つ**で、$`\|a_\lambda(k)\psi_0\|\le Ce\,c_k`$（$|k|\to0$ 一様）が言えれば $\int c_k^2d^3k\propto\Lambda^2\lt\infty$ で足りる。

**再挑戦禁止の範囲（T60）**: 「pull-through の分子を $`\|\pi\psi_0\|`$（または $\mathcal K$ の任意の上界）で押さえ、分解能を $|k|^{-1}$ で押さえる鎖」だけ。
**$\langle N\rangle_0=+\infty$ を主張するものではない**（上界の発散は反証ではない）。

**生きている分岐**: (a) $\nabla E(0)=0$（E05-F22 の回転不変 + E05-F23 の大域最小）による分子の $|k|$ 線形の相殺を定量化する
（$P=0$ ファイバーにギャップが無いので $(H_{[k]}-E_0+|k|)^{-1}$ の $\psi_0$ 直交成分上の評価が要る。T61 と同型の難所）。
(b) 文献の軟光子評価を 1 手で確認する（Hasler `arXiv:2007.01250` の存在証明はこの型の評価を経由する見込み。**未確認なので帰属は書かない**）。

**⚠ この項は奇部 $\mathcal E_A^{\rm odd}$ の評価を塞がない。** 稿 `83_` §7 の判定により、奇部は $N_S$ と $H_f$ 重みだけで閉じ、$\langle N\rangle_0$ を一度も呼ばない。

---

## F55（「E05-P20 の双線形形 + E05-P22 の分け方 + 在庫だけで、奇部 $\mathcal E_A^{\rm odd}$ に $\Lambda$ 一様な上界を出す」— 6 個の奇射影量がどれも在庫で小ささを持たず、真空変分枝で不足が $(\alpha\lambda)^2$〜$(\alpha\lambda)^{3/2}$。2026-09-12、w172、稿 `85_`。**audit87 が「6 スロットすべてでちょうど $(\alpha\lambda)^2$」と「1 スロットだけを狙う発注は原理的に足りない」を撤回**）

格付け: `self-audited`（稿 `85_` §4・§7・§9。数値は (研究ノート: `165_w172_odd_bound_algebra_checks.py`)、3 段 $n_{\max}=5,6,7$・seed 1720912/1720913/1720914、`conclusion: PASS`。**数値は代数の恒等性と不等式の成立だけを検査しており、奇部の大きさ・符号・$e$ 冪は測っていない（`F51`）**）。

**閉じた主張**: 発注 w172 (A)「E05-P20 の双線形形に CS を当て、E05-P22 が指定した分け方で在庫に落として奇部の $\Lambda$ 一様な上界を得る」。

**正確な障害**: 連鎖は**完走し、$\beta$ 一様な明示上界が得られた**（`E05-P?` 2.・3.）。しかしその冪は $p=2$（遠紫外 $12/7$）で $\Lambda$ 一様でない。原因は 2 つ。
(a) **3 つの奇重み（+ 数え落としの 1 つ）がどれも在庫で小ささを持たない**: $`\|(N_S+2)\Pi_{\rm odd}\psi_0\|\le\|(N_S+2)\psi_0\|`$、$\sqrt{\Theta_{\rm odd}}\le\sqrt\Theta$、$`\|\Pi_{\rm odd}\psi_0\|\le1`$、$`\|P_f\Pi_{\rm odd}\psi_0\|\le\|P_f\psi_0\|`$。これらを在庫値で置くと、**得られる上界はパリティ射影を一切使わない素朴な CS と同じ冪になる**（稿 `85_` §7.1、観察 85-5。$`\{T_\nu,b_\nu\}`$ 項は係数まで一致、他 2 項は定数で 2 倍保守）。**⟹ E05-P20（$\Pi_1\psi_0\equiv0$ の真空対項消滅）は本連鎖では冪を 1 つも生まない。**
(b) **不足量が大きい**: 真空変分枝（$\pi\le\alpha\lambda\lesssim\alpha^{-3/2}$）で 5 スロットは $(\alpha\lambda)^2$、$`\|\Pi_{\rm odd}\psi_0\|`$ だけ $(\alpha\lambda)^{3/2}$ 小さい必要がある（稿 `85_` §7.2、audit87 が訂正）。3 項（$`\{T_\nu,b_\nu\}`$・$`\{P_{f\nu},c_\nu\}`$・$`\{Z_\nu,A_\nu\}`$）は独立に評価されるので**各項につき最低 1 スロットずつ**の改善が要るが、**スロットは独立ではない**: $\epsilon_1\le\epsilon_2$・$\epsilon_N\le\epsilon_2$・$\epsilon_0\le\frac12\epsilon_2$ なので**単一の上界 $`\|(N_S+2)\Pi_{\rm odd}\psi_0\|\lesssim(\alpha\lambda)^{-3/2}`$ が 6 要求のうち 4 つを満たし $`\{T_\nu,b_\nu\}`$ 項を完全に閉じる**。**⚠ 旧記載「1 スロットだけを狙う発注は原理的に足りない」は audit87 が撤回した（T60）。** 独立に改善しうる量は 3 個（$\epsilon_2$・$\epsilon_P$・$\Theta_{\rm odd}$）である。

**再挑戦禁止の範囲（証明が実際に排除した分岐のみ。T60）**: 「**E05-P22 3. の分け方**（非 $S$ 局在因子を隣接する $\psi_0$ 射影に当てる）**と、現在の在庫**（E05-P5・E05-P10・E05-P14・E05-P19 の入力）**だけ**で奇部に $\Lambda$ 一様な上界を出す」型。
**⚠ 以下は禁じていない**: (i) 奇重みのどれかに新しい非摂動上界を付けること（むしろ唯一の道）、(ii) 別の分け方（項の組み替え・可換子の追加挿入・平方完成のような吸収）、(iii) $\mathcal E_A^{\rm odd}$ を 4 項に分けずに扱う評価、(iv) 真の $\mathcal E_A^{\rm odd}$ が $\Lambda$ 一様であること（**本項は上界の発散を述べるだけで、$\mathcal E_A^{\rm odd}$ の下界を一切与えない。上界の発散は反証ではない**）。

**生きている分岐**:
(a) **$`\|\Pi_{\rm odd}\psi_0\|`$ の非自明な非摂動上界**（`F52` の生きている分岐 (c) と同一。$`\|\Pi_{\rm odd}\psi_0\|^2=\frac12(1\mp|\langle\psi_0(e),\psi_0(-e)\rangle|)`$。ギャップ無しで Duhamel が使えない。難）。要る強さは $\lesssim(\alpha\lambda)^{-3/2}$。
(b) **【最優先。audit87】$\Pi_{\rm odd}$ セクターに限った $N_S$ モーメント**（$`\|(N_S+2)\Pi_{\rm odd}\psi_0\|\lesssim(\alpha\lambda)^{-3/2}`$。**旧記載の $(\alpha\lambda)^{-1}$ は弱すぎる** — $\epsilon_1w_2$ の積には $t^{-3/2}$ が要る）。E05-P14 の母不等式を $\Pi_{\rm odd}$ 込みで回せるか。**これ 1 本で分岐 (a)（$`\|\Pi_{\rm odd}\psi_0\|`$）も同時に解決し、$`\{T_\nu,b_\nu\}`$ 項が完全に閉じる。**
(c) **$\Theta_{\rm odd}\lesssim\Theta(\alpha\lambda)^{-4}$**（奇セクターの場のエネルギーが全体より 4 冪小さいか）。
(d) **$`\|P_f\Pi_{\rm odd}\psi_0\|`$**（数え落としの 4 つ目。$[N,P_f]=0$ 以上の情報が要る）。
(e) **平方完成型の吸収**: $\mathcal E_A^{A^2}$ で効いた「正項 $\mathcal E_A^{\rm c}$ を吸収体にする」手（E05-P19）の奇部版。奇部には明示的な正項が無いので、$D_{\rm free}$ 自身か $R_2$ の正部分を吸収体にできるか。**本項は試していない。**
(f) 遠紫外枝の律速（$`\|P_f\psi_0\|`$ の $eA(0)$ 片）を E05-L4 で締め直す（$p=12/7\to11/7$ の見込み。小さい）。

**⚠ この項は (H-$\hat Q$) を閉じない。** むしろ本発注で **(H-$\hat Q$) の 4 項すべてに $\beta$ 一様な上界が揃い**、未決の所在が「上界が無い項がある」から「**上界はあるが 4 項すべて $\Lambda$ 非一様**」に確定した。$h(\lambda)$ の datum を含まない（**オッズは動かない。T49**）。

---

---

## F56（「$R_{\mathcal U}$ の 1 ループ値で (H-$\hat Q$) を摂動有効域の内側で殺す」— 窓が開かない。2026-09-12、w170、稿 `84_`）

格付け: `self-audited`（稿 `84_R_Uの1ループ値.md` §5・§6。数値は
(研究ノート: `163_w170_R_U_oneloop_value.py`)（seed 1700912、$\lambda=8,32,128,512,2048$ の 5 段、$\beta$ 3 族）、
`163c_w170_beta_uniform_schur.py`（seed 1700914、$\beta$ 一様上界、5 段、`conclusion: PASS`）、
`163b_`（規約較正、`PASS`）、`163d_`（代数の独立検査、`PASS`））。

**閉じた主張**: **T61** が「1 ループ数値による kill の発注を止めてはならない唯一の項」と名指しした $R_{\mathcal U}$ について、
1 ループ**値**が有効域 $\lambda\lesssim\alpha^{-5/2}$（E05-L4）の内側で $O(1)$ に達し、(H-$\hat Q$) を殺す——という設計。

**正確な障害（3 段）**:

1. **1 ループ値は $\varsigma$ を含まず、$\lambda\ge32$ では単調に減衰する**（$\lambda=8\to32$ だけは平坦。audit88 (R4)）。
   $\mathcal U$ は光子数保存かつ $\mathcal U\Omega=0$ なので $R_{\mathcal U}$ の $O(e^4)$ 部は**厳密に 2 光子行列要素**
   $\langle\Phi_{\alpha_0},\mathcal U\Phi_{\alpha_0}\rangle$ になる（**`E05-P24`** の 1.）。
   これは $\beta$ について**対角な二次形式**なので $`\|\beta\|_2^2`$ しか使わず、**$\varsigma$ が構造的に現れない**。
   実測 $\frac{|R_{\mathcal U}|}{D_{\rm free}}\simeq C\alpha^2\lambda^{p}\varsigma^{0}$、$C\simeq1.6\times10^{-3}$、$p\simeq-1.2$、符号は $+$。
   **$\varsigma$ の実効指数は $0.00\pm0.04$**（$\lambda=8,32,128$ で $\varsigma$ が $3.7,21.8,151$ 倍違う 2 族
   ——拡がった核 / 対蹠キャップ低階数核——の値の比が $0.97,1.12,0.93$）。

2. **$\beta$ 一様上界が $\lambda$ 一様に小さい。** $`\mathrm{supp}\,\beta\subset W_{S,Q}`$ なるすべての $\beta$ について
   $`\frac{|R_{\mathcal U}|}{D_{\rm free}}\big|_{\text{1 ループ}}\le1.42\,\alpha^2`$（$\lambda\ge8$）で、しかも $\lambda\ge32$ では単調に減衰する。
   $\alpha=1/137$ なら $7.6\times10^{-5}$。**$O(1)$ には到達しない。**

3. **窓判定（T86）**: 窓が有効域の内側に開くには $p\ge1.32$ が要り（$C\simeq1.6\times10^{-3}$、$\alpha=1/137.036$）、
   測定値 $p\simeq-1.2$ との差は **2.5**。有限 $\lambda$ 補正（$O(\ln\lambda/\sqrt\lambda)$、傾きの残り動き $\sim0.1$）では埋まらない。
   **⟹ $R_2$・$\mathcal E_A^{A^2}$（どちらも「有効域の外でなら $O(1)$」）よりさらに強い判定で、窓はどこにも開かない。**

**⟹ T61 の射程限定が更新される**: 「1 ループ数値の篩が届くのは $R_2$ だけ」→ **「$R_2$ と $R_{\mathcal U}$ に届く。
残るのは $\mathcal E_A^{\rm odd}$ だけ」**。ただし**それは kill ではなく、1 ループの測定が有効域の内側で
一度も障害を見ていないという意味である**（**F53**(d) と同じ読み）。

**再挑戦禁止の範囲（証明が実際に排除した分岐のみ。T60）**:
「**$R_{\mathcal U}$ の 1 ループ値**を根拠に (H-$\hat Q$) を（有効域の内でも外でも）殺す」型。
および「**有限モード ED で $R_{\mathcal U}$ の $\lambda$ 冪を測る**」型。**理由は継承ではなく本項固有である（audit88 (R5)）**:
**本項の $O(e^4)$ 還元は $\Pi_1\psi_0\equiv0$（E05-F22 の回転不変性）に立っており、有限モード模型は回転不変でないので
還元そのものが成立せず、連続体には無い $O(e^2)$ の 1 光子寄与が混入する。**加えて **T64**・**F51** と同型の循環と無感度（
回転不変でないので $\Pi_1\psi_0\ne0$ になり、かつ測っているのは殻上の離散近似そのもので、
$\lambda$ を上げると角度分解能が落ちて冪が方向集合に依存する。**T80**）。

**生きている分岐**:
- **(a) $R_{\mathcal U}$ の非摂動評価。** 本項が閉じたのは 1 ループ**値**だけで、非摂動では何も言っていない
  （展開 (iv) 依存。**T60**・**T61**）。**この方向の発注を本項で止めてはならない。**
- **(b) $`\inf_\beta\mathrm{Re}\,R_{\mathcal U}`$ の符号**（1 ループでも未計算。$\beta$ の固有値問題）。
  本項が $\beta$ 一様に言えたのは**大きさ**だけである。
- **(c) $\mathcal E_A^{\rm odd}$ の 1 ループ値**（`92_` 枝 1 で上界が無い唯一の項。**F52**）。**これが本命。**
- **(d) $R_2$ の 1 ループ**値**を同じ方法で測り直す**（表の $R_2$ 行は 1 ループ**上界**に $\varsigma\le1$ を入れたもので、
  $R_{\mathcal U}$ と同じ理由で $\varsigma$ が落ちる可能性がある。稿 `84_` §6-8。**発注前に親が「値か上界か」を裁定すること**）。
- **(e) $`\|\rho_S\|_{op}`$ の非摂動 $\Lambda$ 一様上界**（**F53** の生き残り）。本項の副産物として 1 ループ値
  $`\|\rho_S\|_{op}\simeq\rho_{\rm diag}Q^3\simeq0.15\,\alpha^2`$（$\lambda$ 非依存）が出ており、`82_` の $0.28\alpha^2$ と 2 倍以内。

**⚠ **独立監査による強化（audit88、2026-09-12）**: audit88 が 3 手法（混合重要サンプリング MC・素朴 MC・
Gauss–Legendre 直積求積 2 段格子、(研究ノート: `168*`)）で $\beta$ 一様上界を独立に再実装し、
**$\lambda$ を $131072$（$=1.31\times10^5$、E05-L4 の有効域 $\alpha^{-5/2}=2.2\times10^5$ の 60%）まで伸ばした**:
$\lambda=8,32,128,512,2048,8192,32768,131072$ で $1.418,1.392,0.714,0.342,0.140,0.0457,0.0138,0.0041$（$\times\alpha^2$）、
局所傾き $-0.013,-0.482,-0.531,-0.643,-0.809,-0.862,-0.884$。
**局所傾きは $-1$ へ単調に収束し、解析形 $C\alpha^2\ln\lambda/\lambda$（局所傾き $-1+1/\ln\lambda$）と整合する。**
**$O(1)$ に達するには $B/\alpha^2\ge\alpha^{-2}=1.88\times10^4$ が要るが、測定域の最大値は $1.42$（必要値の $1/13000$）で減衰中である。**

閉じていないこと（T60。射程を広げないこと）**:
- **(H-$\hat Q$) を証明していない。** 3 項のうち $\mathcal E_A^{\rm odd}$ には依然として上界が無い。
- **$\Lambda$ 一様な非摂動上界を与えていない。** 本項の上界は 1 ループの $\alpha_0$ に対するものである。
- **$h(\lambda)$ の datum を含まない。オッズは動かない**（**T49**。**経路の生死は datum ではない**）。

---

## F57（$R_2$ の $\Lambda$ 一様化を $`\|\rho_S\|_{op}`$ の改良で狙う経路 — **$R_2$ については不要になった**。**$R_2$ に限りこの型の発注を出さない**）

**日付**: 2026-09-12（w173、稿 `86_` 命題 86-3）。

**閉じた主張**: 「$R_2$ の上界を $\Lambda$ 一様にするには `92_` 枝 1 の**入力 (i)**（$`\|\rho_S\|_{op}`$ の
$\lambda^{-1}$ 級の上界。audit85 が $\lambda^{-1/2}$ から訂正）が要る。」

**正確な障害**: **要らない。** $R_2$ の**負部分**は $\omega$ との二重交換子だけから来るので（`72_` (3.1)）、
窓 $W_{S,Q}$ が $\sqrt\omega$ の振れ幅を $2\sqrt m$ に縛ることで因子 $\frac{4m}\Lambda$ が出る。
これが $`\|\rho_S\|_{op}\le\langle N_S\rangle_0\le\frac{\alpha\lambda}\pi`$ の $\lambda$ を**ちょうど**打ち消し、
$`\mathrm{Re}\,R_2\ge-\frac{4\alpha}\pi D_{\rm free}`$（$\Lambda$ 一様・$\beta$ 一様・無条件・非摂動）が出る。
**⟹ 粗い在庫のままで $\Lambda$ 一様になるので、$`\|\rho_S\|_{op}`$ の改良を目的とする発注は $R_2$ については無意味である。**

**⚠ 生きている分岐（誤って殺さないこと。T60）**:
- **入力 (i) は $\mathcal E_A^{A^2}$ については生きている。** そこでは $`\|\rho_S\|_{op}`$ は平方完成の別の連鎖に入り、
  窓の $\sqrt\omega$ 差は現れない（**T86 の持ち回り先の型検査**）。`92_` の入力 (i) を消してはならない。
- **$R_2$ の大きさの上界は依然 $\Lambda$ 非一様**（$`4\|\rho_S\|_{op}\le\frac{4\alpha\lambda}\pi`$）。窓は正部分には効かない。
  ただし (H-$\hat Q$) が要るのは負部分だけなので、この非一様性は障害ではない。

---

## F58（$R_2$ の 1 ループ値で (H-$\hat Q$) を kill する道 — 閉じた）

**日付**: 2026-09-12（w173、稿 `86_` 観察 86-4・86-5）。

**閉じた主張**: 「**T61** の射程限定は『1 ループ数値の篩が届くのは $R_2$ だけ』と書いた。
ならば $R_2$ の 1 ループ値を測れば (H-$\hat Q$) を有効域の内側で殺せるかもしれない。」

**正確な障害**: 測った結果 **$|R_2|/D_{\rm free}|_{\text{1 ループ}}\simeq C\alpha^2\lambda^{-1}$（$C\le0.064$、符号 $+$）**で、
$p=-1\lt0$ だから $\lambda\ge1$ の**どこでも $O(1)$ に達しない**（E05-L4 の有効域の外。margin は無限）。
**⟹ 3 項（$R_2$・$R_{\mathcal U}$・$\mathcal E_A^{A^2}$）すべてで、1 ループ数値は有効域の内側で障害を見なかった**
（**⚠ 根拠の所在**: $R_2$ は本項、$R_{\mathcal U}$ は**未監査の稿 `84_`**、$\mathcal E_A^{A^2}$ は `81_`／`E05-P19`。
**本項単独で確立したのは $R_2$ の 1 項だけ**である。**T87**）
（`84_` §0 と同じ読み: **それは kill ではなく、測定が障害を見ていないという意味である**）。

**⚠ 表の訂正（T88 の実例。親へ）**: `92_` 枝 1 の表に「$R_2$ の 1 ループ値 $\alpha^2\sqrt\lambda$」と書かれてきた量は
**上界**（$4\varsigma\langle N_S\rangle_0$ に 1 ループの $\langle N_S\rangle_0$ と $\varsigma\le1$ を代入したもの）であって値ではない。
**真の値は $\alpha^2\lambda^{-1}$ で、$\lambda^{3/2}$ 違う。** 結論の向きは a fortiori で安全だった（値 $\le$ 上界）。

**⚠ 生きている分岐**: $\mathcal E_A^{\rm odd}$ の 1 ループ値は**まだ測られていない**（`92_` の表の奇部行は上界のみ）。
本項は奇部を殺さない。

---

## F59（「ファイバー分解 ＋ 反跳項」の機構を残り 3 項の負部分に持ち回る道 — **型検査の段階で閉じた**）

**日付**: 2026-09-12（w174、稿 `87_ファイバー反跳機構の射程.md` 判定 87-4・87-5）。

**閉じた主張**: 「`E05-P26`・`E05-P28` が $R_2$ の負部分を $\Lambda$ 一様にした 3 段の機構
（1. ファイバー分解 / 2. $\rho$ の厳密な最悪化 / 3. 反跳項 $u$ の復元）を、
$R_{\mathcal U}$・$\mathcal E_A^{A^2}$・$\mathcal E_A^{\rm odd}$ の負部分に持ち回れば $\Lambda$ 一様化できる。」

**正確な障害**（3 つあり、どれか 1 つでも致命的）:

1. **⭐ 反跳は $\lambda$ の冪を生まない（窓の別表示である）。**
   $\kappa(\mathcal C):=\sup_\beta\frac{\iint|q|^2|\beta|^2}{D_{\rm free}}$ は点ごとの上限 $`\mathop{\mathrm{ess\,sup}}\frac{4mu}{s+u}`$ に等しく、
   ```math
   \kappa(W_{S,Q})=2m\ (\lambda\ge2\text{ で達成}),\qquad \kappa(S\times S)=\tfrac{4m\lambda}{1+\lambda}\nearrow4m,\qquad
   \kappa(\mathcal C)\le4m\ \text{（任意の }\mathcal C\subset S\times S).
   ```
   さらに $\mathcal A=W_{S,Q}$ 上では、既存連鎖の粗い 2 段（窓 $|q|\le Q$ ＋ $`D_{\rm free}\ge\frac\Lambda2\|\beta\|_2^2`$）と
   反跳経路が**任意のモーメント $|q|^{2p}$（$p\ge1$）について逐語で同一の上界**を与える。
   **原因**: $Q=\sqrt{2m\Lambda}$ は $\frac{Q^2}{2m}=\Lambda$、すなわち**反跳 $u$ が自由エネルギー $s$ と等しくなる境目**の定義であり、
   窓と反跳は同じ 1 つの事実の 2 つの書き方である。**⟹ 既存 3 項はすでに窓を使っているので追加因子は $\lambda^0$。**
2. **冪が最初から足りない（楽観読みでも）。** 機構が $\lambda^{-1}$ を丸ごと与えると仮定してさえ、残差の冪は
   $R_{\mathcal U}$ で $1$（遠紫外 $4/7$。**⚠ 旧記載 $3/14$ は誤り。$R_{\mathcal U}$ の遠紫外冪が $17/14$ ではなく $11/7$ であるため。
   2026-09-12 audit91 (R6)**）、$\mathcal E_A^{A^2}$ で $2$（$\alpha\lambda\le\pi$ 枝で $1$）、
   $\mathcal E_A^{\rm odd}$ で $1$（遠紫外 $5/7$）で、**いずれも $\gt0$**（(研究ノート: `171_`) (D) で厳密有理数再計算）。
3. **段 1・段 2 の適用条件を 3 項とも満たさない。**
   段 1 は「量が $\mathrm{tr}(X\rho)$ 型（**1 体**）で負部分が $\omega$ の二重交換子だけから出る」ことを要するが、
   $R_{\mathcal U}$ は 2 体（$\langle N_S^2\rangle_0$ が入る）で運動量因子 $`W=q_1\!\cdot\!(2p+q'-q_1)`$ は**電子運動量 $p$** を含み
   $\omega$ の交換子ではない（w173／audit89 の申し送りを確認した）。
   $\mathcal E_A^{A^2}$ の負部分は**対（異常）密度** $\langle\psi_0,a(u_\nu)a(h_\nu)\psi_0\rangle$ を含み $\rho$ の汎関数でない。
   $\mathcal E_A^{\rm odd}$ は光子数を奇数変える項なので $\rho$ の汎関数でない。段 2（$\rho\ge0$ の最悪化）も同じ理由で不可。

**項ごとの固有の障害**:

- **$\mathcal E_A^{A^2}$（`E05-P19`）**: 上界 $`\frac{e^2}{4m}\langle A^2\rangle_0\|\rho_S\|_{op}\|\beta\|_{op}^2`$ に **$q$ が 1 つも現れない。**
  **⟹ クラス拡大すら意味を持たない。** $q=0$ の背中合わせ対（**E05-F7**、$\mathcal A$ に入る）を台に持つ $\beta$ で
  $u\equiv0$ だが分子は消えないので、$\beta$ 一様には反跳は 1 円も払わない。
- **⭐ $\mathcal E_A^{\rm odd}$（`E05-P23`）**: 1. の 3 項のうち $Q$ を含むのは (A)(C) だけで、
  **律速の (B) $`\{P_{f\nu},c_\nu\}`$（$`2U_S\|P_f\psi_0\|w_1\varsigma`$）には $q$ が無い**
  （`E05-P23` 3.「(A)(C) だけなら $p=11/7$」）。**⟹ (A)(C) を完全に消しても $p=2$（遠紫外 $12/7$）のまま。**
  これは 1.・2. とは**独立な**閉鎖である。
- **$R_{\mathcal U}$（`E05-P5` 第 2 式＋`E05-P14`）**: $|q|$ が現れるのは補題 B の
  $`(\sum_\nu\|q_\nu\beta\|_{op}^2)^{1/2}\le C_1Q\|\beta\|_{op}`$ だけで、その $`\frac Q{m\Lambda}=\sqrt2\,m^{-1}\lambda^{-1/2}`$ は
  **すでに $p=2$ の中に算入済み**である。**同じ資源を 2 度数えてはならない。**
  なお補題 B は**作用素ノルム**の主張で、反跳が与える $\iint|q|^2|\beta|^2\le4mD_{\rm free}$ は **HS** の主張なので、
  置き換えると $\varsigma^{1/2}$ を失う（$\varsigma\le1$ なので悪化）。$\beta$ 一様形では両者は厳密に一致する。

**⚠⚠ 生きている分岐（誤って殺さないこと。T60・T88）**

- **⚠ 「$R_{\mathcal U}$・$\mathcal E_A^{A^2}$・$\mathcal E_A^{\rm odd}$ は $\Lambda$ 非一様」とは書けない。**
  閉じたのは**この機構による持ち回り**だけで、扱ったのはすべて**上界の冪**である。
  **上界の発散は反証ではない。** 各項の 1 ループ**値**は別問題で、奇部のそれは依然未計算である（**T88**）。
- **`E05-P28` の価値は否定していない。** 定数 4 倍とクラスの真の拡大（$W_{S,Q}\to S\times S$）は本物であり、
  $R_2$ については $\Lambda$ 一様な負部分下界がこの形で確定している。
  否定したのは「**捨てた項は復元可能な冪の資源である**」という一般化（**T90** の処方 (3) の過大解釈）だけである。
- **反跳の別の使い方は検査していない**: $u$ を $D_{\rm free}$ の下界としてではなく **$\rho$ 側**の評価に入れる道、
  および `E05-P28` 1. の閉形式（$\min_{0\le\rho\le I}\mathrm{Re}\langle\gamma,\rho D\gamma\rangle$ の閉形式。
  **一般の $D\ge0$ で成り立つ**）を、負部分が $\mathrm{tr}(X\rho)$ 型に書ける別の量に当てる道。
  **どの量がそう書けるかは未検査であり、この分岐は生きている。**

**この機構以外の道（必ず 1 つ以上。発注 (C) の要求）**

1. **⭐ $`\|P_f\psi_0\|`$（奇版 $`\epsilon_P=\|P_f\Pi_{\rm odd}\psi_0\|`$）の改良は $R_{\mathcal U}$ と $\mathcal E_A^{\rm odd}$ に
   同時に効く唯一の共通入力である**（稿 `87_` 判定 87-6。**T89** の処方の適用）。
   在庫は `E05-P5` の $`\|P_f\psi_0\|\le cm\lambda(\sqrt\alpha+\alpha\sqrt\lambda)`$、
   要る強さは `E05-P23` 7. の $`\epsilon_P\le\|P_f\psi_0\|t^{-2}`$。
   **$q$ に依らない因子なので窓・反跳・ファイバー分解は構造的に届かない。別の道具が要る**
   （pull-through、$\nabla E(0)=0$、$[N,P_f]=0$ を超える構造）。
2. **入力 (i)（$`\|\rho_S\|_{op}`$ の $\lambda^{-1}$ 級の作用素ノルム上界。`F57`）は $\mathcal E_A^{A^2}$ について生きたままである**——
   本機構では代替できないことが**確定した**（$R_2$ では窓／反跳が $\langle N_S\rangle_0$ の $\lambda$ を打ち消したが、
   $\mathcal E_A^{A^2}$ の分子には $q$ が無いのでその打ち消しが起きない）。
3. **$\mathcal E_A^{A^2}$ の第 3 の入力**: その負部分の最悪化対象は $\rho$ ではなく**対密度 $\kappa$** であり、
   制約 $`|\kappa(f,g)|^2\le(\|f\|^2+\langle f,\rho f\rangle)\langle g,\rho g\rangle`$ に現れる真空項
   $`\sum_\nu\|u_\nu\|^2=\frac{\Lambda^2}{4\pi^2}`$ が $\Lambda$ 非一様性の出所である。
   **「$\kappa$ の側の $\Lambda$ 一様な情報」は在庫ゼロの新しいスロットである。**
4. **奇部**: `E05-P23` 7.／audit87（**T89**）の $`\epsilon_2=\|(N_S+2)\Pi_{\rm odd}\psi_0\|\lesssim(\alpha\lambda)^{-3/2}`$ の
   **1 本**が 6 要求のうち 4 つを満たし (A) 項を完全に閉じる。残るのは $\epsilon_P$（＝1.）と $\Theta_{\rm odd}$。

**数値**: (研究ノート: `171_w174_window_recoil_equivalence.py`)（seed 1740912、`conclusion: PASS`）。
**⚠ 数値は閉形式の再現と不等式の成立だけを検査する**（**F51**・**T64**）。閉鎖の根拠は稿 `87_` §2〜§5 の解析である。

**⚠ オッズは動かない**（$h(\lambda)$ の datum を含まない。**T49**）。

**⚠⚠【2026-09-12 親。audit90 と w174 の突き合わせ】$R_{\mathcal U}$ 行の型検査は再点検が要る。**
w174 は $R_{\mathcal U}$ の上界を $p=2$ として型検査し「機構は届かない」と判定したが、**その $p=2$ は
`E05-P5` 第 2 式（$\varsigma$ で分けた連鎖）から来ている。audit90 は同じ日に、この $\varsigma$ 分割こそが
$\lambda^{3/2}$ の出所で、兄弟の `E05-P26` 2. はその分割を外して $\varsigma$ を消していると指摘した**
（audit89 の「$\mathcal U_1$ には原理的に届かない」を **T90** で反転）。
**⟹ $R_{\mathcal U}$ 行の「届かない」は「$\varsigma$ 分割連鎖の上界には届かない」であって、
量にも、分割を外した別の上界にも届かないとは言えない**（**T88**・**T60**）。
**⛔ この行を根拠に $\mathcal U_1$ 側・$R_{\mathcal U}$ 側の発注を止めないこと。**
$\mathcal E_A^{A^2}$（$q$ が 1 つも無い）と $\mathcal E_A^{\rm odd}$（律速 (B) に $q$ が無い）の 2 行は、
$\varsigma$ 分割に依らない構造的な理由なので、この再点検の影響を受けない。

---

## F60（「$`\|P_f\psi_0\|`$ **だけ**を改良して (H-$\hat Q$) の 2 項を $\Lambda$ 一様にする」— 余地は $\lambda^{1/2}$ しかなく、$\mathcal E_A^{\rm odd}$ では冪が 1 つも下がらない）

**日付**: 2026-09-12（w175、稿 `88_Pfpsi0の1ループ値.md` 判定 88-5）。

**閉じた主張**: 「`E05-P30` 5. が同定した共通入力 $`\|P_f\psi_0\|`$ を改良すれば、
$R_{\mathcal U}$ と $\mathcal E_A^{\rm odd}$ の 2 項が**同時に** $\Lambda$ 一様（$p\le0$）になる。」

**正確な障害**（2 つあり、どちらも致命的）:

1. **⭐ 改良の余地が $\lambda^{1/2}$ しかない（測定値）。**
   1 ループ**値**は $`\|P_f\psi_0\|\to\sqrt{\frac{8\ln2+1}{3\pi^2}}\,\alpha m\lambda=0.47016\,\alpha m\lambda`$（稿 `88_` 命題 88-1、
   閉形式 + 独立な 2 経路）。在庫 `E05-P5` の $`c\,m\lambda(\sqrt\alpha+\alpha\sqrt\lambda)`$ は真空変分枝
   （$\alpha\lambda\ge\pi$）で $\alpha m\lambda^{3/2}$ が支配するので、**$\lambda$ 冪の差はちょうど $1/2$ である。**
   **非摂動でこの因子を 1 ループ値まで締めても、$\varsigma$ 分割連鎖の冪は $\lambda^{1/2}$ しか下がらない。**
   （$\lambda\lesssim\alpha^{-1}$ では在庫の支配項が $\sqrt\alpha m\lambda$ になり $\lambda$ 冪は**同じ**で、
   利得は $\sqrt\alpha$ だけになる。**ただしこの領域は真空変分枝の外である。**）

2. **⭐ $\mathcal E_A^{\rm odd}$ では、この因子を含まない項が同じ $p$ を持つ。**
   真空変分枝・$\varsigma\le1$ の $\beta$ 一様形で `E05-P23` 1. の 3 項を数え直すと（厳密有理数、
   (研究ノート: `172b_w175_power_ledger.py`)、K2 で `E05-P23` 2. の $(\alpha\lambda)^2$ と一致を確認）、
   **(A) $`\{T_\nu,b_\nu\}`$ と (C) $`\{Z_\nu,A_\nu\}`$ はどちらも $p=2$ でありながら $`\|P_f\psi_0\|`$ を含まない**
   （(C) は $\langle A^2\rangle_0$ の $\frac{2\alpha\lambda}\pi$ 経由）。
   **⟹ (B) $`\{P_{f\nu},c_\nu\}`$ を $p=2\to3/2$ に下げても $\mathcal E_A^{\rm odd}$ 全体は $p=2$ のまま。冪は 1 つも下がらない。**
   `E05-P23` 3. の「律速は $`\{P_{f\nu},c_\nu\}`$」は**遠紫外枝**（$\lambda\gtrsim\alpha^{-5/2}$）の記述で、
   そこは **E05-L4** の摂動有効域の外なので 1 ループ値を代入すること自体が正当化されない（**T61**）。

**⟹ 波及の表**（$p\le0$ に届く項は 1 つも無い）:

| 項 | 在庫での $p$ | 1 ループ値を入れた $p$ |
|---|---|---|
| $R_{\mathcal U}$（$\varsigma$ 分割連鎖） | 2 | **3/2** |
| $\mathcal E_A^{\rm odd}$ 合計 | 2 | **2（不変）** |

**再挑戦禁止の範囲（T60。ここを広げないこと）**:
閉じたのは「**$`\|P_f\psi_0\|`$ だけを改良して $\varsigma$ 分割連鎖（`E05-P5` 第 2 式）の $p$ を $0$ 以下にする**」道**だけ**である。
- **$R_{\mathcal U}$ 側の発注を止めるものではない。** $2\to3/2$ は実在の利得で、他の入力の改良と**併せれば**効く。
- **$\mathcal U_1$ 側の発注を止めるものでもない。**
- **$\varsigma$ 分割を外した連鎖（`E05-P24`・`E05-P26` 型）については何も言わない**
  （2026-09-12、audit90 が $\varsigma$ 分割こそ $\lambda^{3/2}$ の出所だと指摘した）。
  なお `PROVED.md` で `\|P_f\psi_0\|` は `E05-P24`・`E05-P26` のブロックにヒットしない（w175 実測）が、
  本文は w175 の読み許可の外なので**別表記の可能性は判定していない**。
- **在庫 `E05-P5` は無条件のまま生きている。** 値が上界より小さいことは上界の誤りではない。
- **$`\|P_f\psi_0\|`$ の非摂動上界の改良そのものを禁じるものではない**（1 ループ値までは締まる余地が実在する）。

**生きている分岐**:
(a) **$\langle A^2\rangle_0$ の相対補正の非摂動上界**（$\frac{2\alpha\lambda}\pi$ を $O(\alpha)$ 級へ）。
  これは $`\|P_f\psi_0\|`$ の $\alpha m\lambda^{3/2}$ 項と $\mathcal E_A^{\rm odd}$ の (C) 項に**同時に**効く
  （稿 `88_` §4.1 の副産物。**$`\|P_f\psi_0\|`$ より広い射程を持つ入力である**）。
(b) **$`\epsilon_2=\|(N_S+2)\Pi_{\rm odd}\psi_0\|`$**（`E05-P23` 7.）。(A) $`\{T_\nu,b_\nu\}`$ を閉じる唯一の道で、
  $`\|P_f\psi_0\|`$ とは独立。
(c) **稿 `88_` 命題 88-2 の和則** $`\|P_f\psi_0\|^2=2m(E_0-\Theta)-e^2\langle A^2\rangle_0-2e\langle P_f\!\cdot\!A(0)\rangle_0`$
  （厳密・非摂動）。要るのは $2m(E_0-\Theta)-e^2\langle A^2\rangle_0$ の相対 $O(\alpha)$ 精度の評価と交差項の上界。

**閉じていない別の道**: pull-through は**閉じたのではなく、素朴な鎖が在庫より $\sqrt\lambda$ 悪いだけ**である
（稿 `88_` §7(a)。$|k|^2$ の重みは `F54` の赤外対数を確かに殺す。障害は分解能を
$`\|(H_{[k]}-E_0+|k|)^{-1}\|\le|k|^{-1}`$ で押さえる 1 段に移り、これは `F54` の生きている分岐 (a) と同じ難所）。

---
---

## F61（$\langle A(0)^2\rangle_0$ の**下界**と $P\ne0$ への拡張 — w176 の汎関数積分論法は原理的に片側でしか働かない）

**閉じた主張**: 稿 `89_` 定理 89-1 の論法（経路に条件付けた Gauss 公式）で、
(a) $\langle A^2\rangle_0$ の**下界**（$\ge$ 側）を得ること、(b) 同じ結論を $P\ne0$ のファイバーに拡張すること。

**正確な障害**:

1. **(a) 下界**: 論法が与えるのは
   $\langle A^2\rangle_{\psi_t}=\langle A^2\rangle_\Omega-\dfrac{\mathbb E_W[w\sum_\nu\rho_\nu^2]}{\mathbb E_W[w]}$、$w=e^{-\frac12\sigma_\ell^2}\gt0$ という
   **有限 $t$ の等式**である（**⚠ audit91 (R5): $\psi_0$ についての等式は未証明。$t\to\infty$ では下半連続性しか使っておらず、
   等式にするには右辺の極限の存在と $`\|\Phi(f)\psi_t\|^2\to\|\Phi(f)\psi_0\|^2`$ の**収束**がもう 1 段要る。
   ⟹ 下界側の障害は「$\rho_\nu$ の経路平均の上界が無い」だけではない**）。
   $\le$ は $\rho_\nu^2\ge0$ から 1 行で出るが、$\ge$ には**$\rho_\nu[b]$（場と確率積分 $\int A_E(b_s,s)db_s$ の共分散）の
   経路平均の上界**が要る。これは $\mathcal K$・$\Theta$ と同型の「非摂動の場の量」で、**在庫ゼロ**。
   ⟹ **`FAILED.md` の「非摂動では $\langle A^2\rangle_0\ge\frac{\Lambda^2}{4\pi^2}$ すら在庫に無い」は本結果の後も生きている。**
   **⚠ 下界が無いこと自体は障害ではない**（`E05-P19`・`E05-P23` が要求するのは上界だけである）。**記録の目的は「両側が付いた」と誤読させないことである。**
2. **(b) $P\ne0$**: Step 3 の経路平均が正の重みであることに依存する。$H(P)$ の表示では重みが
   $e^{-iP\cdot b_t}w[b]$ と**複素**になり、$\rho_\nu^2$ の符号が経路平均で保存しない。
   **これは E05-F23 が $E(P)\ge E(0)$ という不等式で止まり等式を与えないのと同じ境界である**（同じ $|e^{-iP\cdot b_t}|=1$ の使い方しかできない）。
   ⟹ **$P\ne0$ のファイバーの場の揺らぎについては何も言えない。$\mathcal E(P)$ 系の量に本結果を持ち込まないこと。**
3. **(c) 副次的**: 指数が**実**の線形（例えば Nelson 型でスカラー結合を Euclid 化したときに位相が立たない扱い）だと
   同じ Gauss 公式が $+\rho^2$ を与え、**符号が逆転する**。
   **⟹ 本結果を「場の基底状態は常にスクイーズされる」という一般命題として引用してはならない。
   PF の最小結合が Feynman–Kac–Itô で位相になること（反磁性不等式の源）が本質である。**

**出所**: 稿 `89_A2の相対補正.md` §2・§7（R6・R7）、w176（2026-09-12）。
**波及**: `E05-P?`（本セッションの新規 1.〜4.）の射程節に同じ 3 点を明記済。

---

## F62（「パリティ分解 $H=H_{\rm e}+H_{\rm o}$ とギャップ $g=\inf\sigma((H_{\rm e}-E_0)|_{\rm odd})$ で $`\epsilon_0=\|\Pi_{\rm odd}\psi_0\|`$（したがって $\epsilon_2$）の非自明な上界を出す」— **ギャップ経路は恒等的に空**。2026-09-12、w177、稿 `90_`）

**何を試したか**: $\mathcal P=(-1)^N$ で $\mathcal P H(e)\mathcal P=H(-e)$、$H_{\rm e}=\frac12(H(e)+H(-e))\ge E_0$（無条件）、
固有方程式の奇成分 $(H_{\rm e}-E_0)\psi_{\rm od}=-H_{\rm o}\psi_{\rm ev}$ から
$`\delta=\langle\psi_{\rm od},(H_{\rm e}-E_0)\psi_{\rm od}\rangle=-\frac12\langle H_{\rm o}\rangle_0
=\frac{\|P_f\psi_0\|^2+e^2\langle A^2\rangle_0-\mathcal K}{4m}`$ を作り、$\epsilon_0^2\le\delta/g$ を狙った。
在庫で $`\delta\le4.23\,\Lambda t^2`$（真空変分枝、$t\ge1$）まで出る。

**正確な障害**: **$\psi_{\rm od}$ 自身と、soft 光子を着せた $\psi_{\rm ev}$ の 2 本がともに $H_{\rm e}|_{\rm odd}$ の試行ベクトルなので**
```math
\delta\ \ge\ g\cdot\max(\epsilon_0^2,\ 1-\epsilon_0^2)\ \ge\ \frac g2
```
が恒等的に成り立つ。**⟹ $\epsilon_0^2\le\delta/g$ の右辺は常に $\ge\frac12$ で、$\delta$ の改良も $g$ の下界の改良も
$\epsilon_0$ には 1 つも伝わらない。$\lambda$ の負冪はゼロ。標的 $\epsilon_0\lesssim(\alpha\lambda)^{-3/2}$ との不足 $t^{3/2}$ は
1 つも埋まらない。**（第 1 の不等式は変分原理そのもので、$\epsilon_0^2\le\delta/g$ は**恒等式であって評価ではない**。
第 2 の不等式は soft 光子による偶奇の縮退 $\inf\sigma(H_{\rm e}|_{\rm odd})=\inf\sigma(H_{\rm e})$ を使い、
**無質量性と 2 次形式核の仮定 (D1) に依存する**。稿 `90_` 補題 90-5。）

**在庫のどれを改良すれば届くか（＝閉じていないこと）**: **在庫のどの 1 項目の改良でも届かない。**
$`\|P_f\psi_0\|`$ は `F60` が既に閉じており、$\langle A^2\rangle_0$・$\langle N_S\rangle_0$・$\langle N_S^2\rangle_0$・$\Theta$ の改良は
$\delta$ の上界を下げるだけで上の不等式により $\epsilon_0$ に伝わらない。
**この評価の型に足りないのは新しい量**（**⚠ 訂正 audit109 R10: 旧記載「在庫のどの 1 項目の改良でも届かない」は過大。下の分岐 (b) が挙げる Q 空間表示は同じ積分を逆向きに（下から）押さえれば $\epsilon_0$ の**上界**を与え、$F(\sigma)$ を要求しない。`E05-F24` の汎関数積分表示も同様。⟹ 次に要る入力は $F(\sigma)$ か $\langle\psi_0,\mathcal P\psi_0\rangle$ の下界のいずれか 1 つ**）——
```math
\bigl\|\mathbf 1_{[0,\sigma]}\bigl((H_{\rm e}-E_0)|_{\rm odd}\bigr)H_{\rm o}\psi_{\rm ev}\bigr\|\le F(\sigma)\quad(\sigma\downarrow0\ \text{で減衰})
```
すなわち $H_{\rm o}\psi_{\rm ev}$ のスペクトル重みが底から離れていることの評価である。
**これは `F52` の生きている分岐 (a)（$P=0$ ファイバーはギャップを持たないので soft-photon 型の分解能評価が要る）と同じ道具で、
⟹ `F52` の (a) と (c) は独立な 2 本ではない。(c) は (a) の道具を要求する**（逆は主張しない）。

**生きている分岐**:
(a) 上の $F(\sigma)$ 型評価（`F52` 分岐 (a) と合同に扱う。難）。
(b) $\epsilon_0$ の**下界**（標的が偽であることの検査）。$`\langle\psi_0,\mathcal P\psi_0\rangle=\int\psi_0(\phi)\psi_0(-\phi)\,d\mu`$ を
   Q 空間（positivity improving）で上から押さえる道。
(c) $`\epsilon_N=\|N_S\Pi_{\rm odd}\psi_0\|`$ **だけ**を狙う道（殻のエネルギー $H_f\ge\frac\Lambda2N_S$ が効く側）。
   **ただし $2\epsilon_0\le\epsilon_2$ なので、これだけでは $\epsilon_2$ は閉じない。**

**⚠ この kill が禁じる範囲（T60）**: 禁じるのは**「$\mathcal F_{\rm odd}$ 全体の底のギャップ 1 つで $(H_{\rm e}-E_0)^{-1}$ を押さえる」形の発注だけ**である。**⭐ 族の限定（audit109 R8、2026-09-13）: 本項の空虚性は補題 90-5（＝仮定 (D1)、無質量性）に全面依存し、閉じるのは「soft 光子が到達できる部分空間」への制限までである。⛔ 殻セクター $`\mathcal F_{\rm odd}\cap\{N_S\ge1\}`$ に制限した $g_S$ を使うギャップ評価は本項の射程外**（$\psi_{\rm od}$ がその部分空間に入らないので (4.1) が失効し、$|k|\in[\eta,2\eta]$ の着せ替えは殻の外なので (4.3) も移せない）。**⛔ 光子質量つき・赤外切断つきの変種も射程外。** 下の分岐 (c) はこの意味で生きている。
スペクトル測度の低エネルギー端を使う発注、$\epsilon_N$ だけを狙う発注、$\epsilon_0$ の下界を狙う発注を止めてはならない。
**本項は $\epsilon_0$ という量の下界を 1 つも与えていないので、標的 $\epsilon_2\lesssim(\alpha\lambda)^{-3/2}$ の真偽には触れていない。**
**⚠ 「1 スロットだけを狙う発注は原理的に足りない」を復活させてはならない（T89）。**
`E05-P23` 7. の「$\epsilon_2$ 1 本で 6 要求のうち 4 つが閉じる」は本項でも**正しいまま**である
（本項が足すのは**難易度の所在**であって要求の本数ではない）。

**在庫の到達点（参考。改良ではない）**: $\epsilon_2\le\langle(N_S+2)^2\rangle_0^{1/2}\le3.34\max(1,t)$（真空変分枝）。
**冪 $t^{+1}$、標的 $t^{-3/2}$、隔たり $t^{5/2}$。**
## F63（「$\langle\psi_0,\mathcal P\psi_0\rangle$ を上から押さえて $\epsilon_0$ の $\lambda$ 非減衰を示し、標的 $\epsilon_2\lesssim(\alpha\lambda)^{-3/2}$ を殺す」— **kill は発動せず。機構は完成したが入力が 1 つ欠けている**。2026-09-12、w178、稿 `93_`）

> **⚠【2026-09-13 audit98 封印バナー】本項の禁止範囲・閉鎖理由の一部は撤回または条件付きに格下げされた。再挑戦禁止の範囲を引用する前に、FAILED.md 末尾の「audit98 追記注記 → F63」を必ず読むこと（(研究ノート: `93_94_audit98_2026-09-13.md`)）。**

**何を試したか**（発注 (研究ノート: `w178_epsilon0の下界kill-check.md`) の (A)(B)(C)(D)）。
`E05-P33`・`F62` の $2\epsilon_0\le\epsilon_2$ により、$\epsilon_0$ が $\lambda$ 非減衰なら
`E05-P23` 7. の標的 $\epsilon_2\lesssim t^{-3/2}$ は偽になる。そこで
$\epsilon_0^2=\frac{1-\langle\psi_0,\mathcal P\psi_0\rangle}2$（$\mathcal P=(-1)^N$）の右辺を上から押さえに行った。

**到達したところ（`F-?` に送るのは「届かなかった」ことであって、以下は生きている）**
1. **`E05-P?`（符号反転フィデリティ恒等式）**: $\mathcal P\psi_0^{(e)}=\psi_0^{(-e)}$、
   $\epsilon_0^2=\frac{1-\langle\psi_0^{(e)},\psi_0^{(-e)}\rangle}2$。標的は
   「$\Lambda\to\infty$ で $\pm e$ の基底状態が $1-O(t^{-3})$ で一致していく」と**同値**である。
2. **`E05-P?`（母不等式）**: $`\epsilon_0\ge\frac{-\langle K_{\rm od}\rangle_0}{2\|(K_{\rm ev}-E_0)\psi_0\|}`$。
   **在庫初の $\epsilon_0$ の下界**で、緊密度は 0.977〜0.996（有限モード ED 実測、代数のみ）。

**正確な障害（2 つ。律速は 1 つ目）**

**(i) $\langle A(0)^2\rangle_{\psi_0}$ の下界が在庫ゼロ（律速）。** 母不等式の分子
$\Delta'=-\langle K_{\rm od}\rangle_0=\frac{\langle P_f^2\rangle_0+e^2\langle A(0)^2\rangle_0}{2m}+\Theta-E_0$
（＝`F62` の $2\delta$）の**下界**が要る。在庫（`E05-P22` 2.・`E05-P5`・`E05-F4`・`E05-L4`）は**すべて上界**である（**T88**）。
**困難は符号ではなく桁落ち**: $\frac{e^2\langle A^2\rangle_0}{2m}$ も $E_0$ も主要部が $\frac{\alpha\Lambda^2}{2\pi m}$ で、
摂動的には $O(e^4)$ まで厳密に相殺する。
**⟹ 必要なのは絶対定数 $\theta\gt0$ についての $\langle A(0)^2\rangle_{\psi_0}\ge\theta\frac{\Lambda^2}{4\pi^2}$（$\Lambda$ 一様）だけ**で、
これがあれば `E05-L4` の上界 $E_0\lt C_2\alpha^{2/7}\Lambda^{12/7}m^{-5/7}$ と合わせて
$\lambda\ge(\frac{4\pi C_2}\theta)^{7/2}\alpha^{-5/2}$ で $\Delta'\ge\frac\theta2\frac{\alpha\Lambda^2}{2\pi m}$ が出る。
**閾値 $\lambda\gtrsim\alpha^{-5/2}$ は `E05-L4` の「摂動論の有効域 $\alpha\lesssim\Lambda^{-2/5}$」の境界と一致する**
（同じ「$\alpha\Lambda^2$ と $\alpha^{2/7}\Lambda^{12/7}$ の入れ替わり点」）。
**⚠ 不確定性関係 $`\langle\Phi(g)^2\rangle\langle\Pi(g)^2\rangle\ge\frac14\|g\|^4`$ 経由は $\Lambda^1$ しか出ず 1 桁足りない**
（かつ $\langle N\rangle_0$ を要求するので `F54` に当たる）。**この道は本稿で試して閉じた。**

**(ii) $`\|(K_{\rm ev}-E_0)\psi_0\|`$ の上界と定義域 (D1′) $\psi_0\in D(K_{\rm ev})$ が在庫ゼロ。**
在庫は `E05-P14`（$\langle N_S^2\rangle_0$、殻 $S$ 限定）まで。全 $N$・$H_f^2$ はゼロ（**`F54`**）。
**ただし向きが「上界」なので在庫拡張の延長線上にあり、(i) が律速である。**

**閉じた副次経路（再挑戦禁止）**
- **`E05-F24`・`E05-F25`（汎関数積分表示）で $\mathcal P$ を表示する道は原理的に閉じている。**
  $\mathcal P=\Gamma(-1)$ は $Q$ 空間で**反転** $\phi\mapsto-\phi$ であって**乗算作用素でない**。
  Cor 4.3 / Thm 4.2 の挿入は 1 時刻の場の作用素の有界関数（$=$ 乗算作用素）に限られ、
  証明の要 $J_sFJ_s^*=E_s(J_sF)E_s$ が非乗算 $F$ では成り立たない。
  実際 $J_t\mathcal PJ_t^*=\Gamma(-E_t)$ は非乗算である。
  **有界性ではなく乗算作用素性が障害なので、「有界挿入だけ使う」（`E05-F25` の射程注）では回避できない。**
- **$`2m\Delta'\ge\sum_i(\|P_{f,i}\psi_0\|-e\|A_i\psi_0\|)^2`$ の形は現在の在庫では何も出さない。**
  `E05-P5` の $`\|P_f\psi_0\|\le cm\lambda(\sqrt\alpha+\alpha\sqrt\lambda)`$ が $\lambda$ 大で
  $e\langle A^2\rangle_0^{1/2}\sim\sqrt\alpha\Lambda$ を上回るため。$\Delta'\ge\frac{e^2\langle A^2\rangle_0}{2m}-E_0$ の方が強い。
- **フィデリティの上界を「安い一般論」で出す道は原理的に無い。** 摂動論・量子幾何テンソルの測地線長
  $`\arccos|\langle\cdot,\cdot\rangle|\le\int\sqrt{g_{ee}}\,de`$・Jensen はいずれもフィデリティの**下界**（$=\epsilon_0$ の**上界**）しか与えない。
  上界（$=\epsilon_0$ の下界）は「ずれているモードを下から数える」型を要求し、$\psi_0$ の成分の**下界**が要る。
  **これが本発注が kill に失敗した単一の構造的原因である。**

**在庫のどれを改良すれば届くか（＝閉じていないこと）**
**(i) の 1 項目だけで届く。** 母不等式は冪も定数もほぼ失わない（緊密度の実測 0.977〜0.996、
構造的理由は「損失が $\psi_{\rm od}$ 上の $K_{\rm ev}-E_0$ の逆参加率だけ」）ので、
**$\langle A(0)^2\rangle_0$ の定数倍の下界が 1 本付けば、$\epsilon_0$ の下界がそのまま出る。**
**⟹ 本項は「途中で緩んで届かない」型の失敗ではなく、入力が 1 つ欠けているだけの完成した機構である。**

**⚠ この kill が禁じる範囲（T60）**: 禁じるのは
**「`E05-F24`/`E05-F25` の汎関数積分で $\mathcal P$ を表示する」発注**と
**「不確定性関係で $\langle A(0)^2\rangle_0$ の下界を出す」発注**の 2 つだけである。
$\langle A(0)^2\rangle_0$ の下界を別の道具（準自由下界・紫外優勢性）で狙う発注を止めてはならない。
**本項は標的 $\epsilon_2\lesssim(\alpha\lambda)^{-3/2}$ の真偽に触れていない**——
$\epsilon_0$ の下界の**値**を 1 つも出していないので、標的は否定も肯定もされていない。
`E05-P23` 7. の $\epsilon_2$ 経路は**閉じない**。(7.1) の分解の取り直しは**必要と判定されていない**。
**⚠ $\mathcal E_A^{\rm odd}$ という量が $\Lambda$ 非一様という主張ではない**（**T88**・**T60**）。
**⚠ $h(\lambda)$ の datum を含まないのでオッズを動かさない**（**T49**）。

**参考（動機であって根拠ではない）**: (93.4) と `E05-L4` を並べると
**「Lieb–Loss のドレッシングによる自己エネルギーの減少（$\Lambda^{12/7}\ll\Lambda^2$）は、
そのまま基底状態のパリティ奇成分による利得 $\Delta'=-\langle K_{\rm od}\rangle_0$ である」**と読める。
$\epsilon_0$ が $\lambda$ とともに減衰するなら、この利得を生む機構が消えることになるので、
**標的は `E05-L4` と整合しにくい。⚠ ただし $`\|(K_{\rm ev}-E_0)\psi_0\|`$ の上界が無いので $\epsilon_0$ の値には翻訳できず、
これは証明ではない。**

---
## F64（「$K_{\rm ev}\ge\tilde K=H_f+\frac{e^2}{2m}A(0)^2$（$P_f^2\ge0$ を捨てる）で $\langle A(0)^2\rangle_0$ の絶対定数下界を出す」— **厳密な反例で閉鎖**。あわせて「$\Theta$ 経由の形の不等式で $\bar r$ を押さえる」道も原理的に閉鎖。2026-09-12、w179、稿 `94_`）

> **⚠【2026-09-13 audit98 封印バナー】本項の禁止範囲・閉鎖理由の一部は撤回または条件付きに格下げされた。再挑戦禁止の範囲を引用する前に、FAILED.md 末尾の「audit98 追記注記 → F64」を必ず読むこと（(研究ノート: `93_94_audit98_2026-09-13.md`)）。**

**閉じた主張**:
(a) 準自由下界 $K_{\rm ev}\ge\tilde K:=H_f+\frac{e^2}{2m}A(0)^2$ と $\tilde K$ の厳密可解性から、
$\langle A(0)^2\rangle_{\psi_0}\ge\theta\frac{\Lambda^2}{4\pi^2}$（絶対定数 $\theta\gt0$、$\Lambda$ 一様）を導くこと（発注 w179 の道 (a)）。
(b) 形の不等式 $`\sum_\nu\|a(u_\nu)\psi_0\|^2\le\frac{\Lambda}{2\pi^2}\Theta`$（`E05-P22` 5.）と $\Theta$ の上界の改良によって、
同じ標的の唯一の欠落 $`\bar r=\frac{4\pi^2}{\Lambda^2}\sum_\nu\|a(u_\nu)\psi_0\|^2`$ の $\Lambda$ 一様な上界を得ること（発注の道 (c) 双対）。

**正確な障害**:

1. **(a) $\tilde K$ の基底状態自身が標的を破る（厳密）。** $\mathrm d\Gamma(\omega)=\frac14(\Pi\omega\Pi+\Phi\omega\Phi)+$const により
   $`\tilde K=\frac14(\Pi\,\omega\,\Pi+\Phi\,M\,\Phi)+`$const、$M=\omega+4\kappa Q$、$\kappa=\frac{e^2}{2m}$、$Q=\sum_\nu|u_\nu\rangle\langle u_\nu|$（**階数 3**）。
   Gauss 共分散 $C_\Phi=T^{1/2}(T^{1/2}MT^{1/2})^{-1/2}T^{1/2}$ と階数 3 の Woodbury・動径測度 $`d\varrho=\frac{k\,dk}{6\pi^2}`$ で
   ```math
   \frac{\langle A^2\rangle_{\tilde K}}{\langle A^2\rangle_\Omega}=\frac4\pi\int_0^\infty\frac{f(x)dx}{1+\mu f(x)}
   \ \xrightarrow[\mu\to\infty]{}\ \frac2{\sqrt3}\mu^{-1/2}=\sqrt{\frac\pi{\alpha\lambda}}\ \to\ 0,
   ```
   $f(x)=1-x\arctan\frac1x$、$\mu=\frac{4\alpha\lambda}{3\pi}$。
   $K_{\rm ev}\ge\tilde K$ は**基底状態エネルギーの不等式**しか与えず、$\langle A^2\rangle$ は変分量ではないので
   比較も単調性も使えない。**下界側の模型の基底状態が標的を破る以上、この道は原理的に閉じる。**
   **⟹ 「$P_f^2\ge0$ を捨てて下から押さえる」型の下界は、この標的については全滅である**（$\tilde K$ に固有の事故ではない）。
2. **(a) の構造的な読み（転進の指針）**: **標的を救っているのは、道 (a) が最初に捨てる $P_f^2$（反跳）そのものである。**
   $\tilde K$ には反跳が無いので深紫外まで $A^2$ の squeezing が $\omega$ と競争し、$\mu\propto\alpha\lambda$ で潰れる。
   フル PF では反跳が対の分母に $\frac{|k+k'|^2}{2m}$ を入れて squeezing を切り、
   1 ループ相対補正が $-1.389\alpha$（**$\lambda$ 非依存**、`E05-P32`／稿 `88_`・`89_`）に留まる。
   **⟹ 標的の証明は反跳を使わなければならない。反跳を落とす近似はすべて先験的に無効である。**
3. **(b) 形の不等式は階数を見ていない。** $Q$ は**階数 3** なのに $Q\le\frac\Lambda{2\pi^2}\omega$ は
   $\mathrm{tr}(Q\hat\rho)$ を $\mathrm{tr}(\omega\hat\rho)=\Theta$ で押さえており、
   **$\hat\rho$ が $Q$ の 3 次元の像にどれだけ乗っているかを一切見ていない。**
   一方 $\Theta$ を膨らませているのは**背中合わせ対**で（`E05-F7`: 反跳の抑制は総運動量 $k+k'$ のみで決まり背中合わせ対は免れる。
   `FAILED.md` の **F6 命題 3**: 局所 Bogoliubov の対核が背中合わせ対で $`\|\beta_0\|_{HS}^2\simeq\frac{\alpha^2}\pi\sqrt{\Lambda/m}`$
   〔公理表の規約 $`\|\beta\|_{HS}^2=\frac12\iint|\beta|^2`$〕）、
   $\Theta\sim\alpha^2\Lambda\sqrt\lambda$、すなわち $\frac{2\Theta}\Lambda\sim\alpha^2\sqrt\lambda\to\infty$。
   **ところが背中合わせ対は $Q$ の像にほとんど乗らない**——$\varphi_\nu(q)=\int\overline{u_\nu(k)}\beta(k,q)d^3k$ の
   $k$ 積分は $c_k^2\propto1/k$ の重みで軟部 $|k|\ll|q|$ が支配し、背中合わせ部は $\sqrt{m/|q|}$ で抑えられる。
   **⟹ $\Theta$ の上界をいくら改善しても、この段からは絶対定数は出ない。**
   **⚠ $\Theta\sim\alpha^2\Lambda\sqrt\lambda$ と「$\bar r=O(\alpha^2)$」は見積りであって証明ではない**（**T61**）。
   閉じているのは「**形の不等式という道具**が階数 3 を見ない」という構造的事実の方である。
4. **副次的（記録）**: 数値上、$g(r)=1+2r-2\sqrt{r^2+r}$ と $(\sqrt{1+r}-\sqrt r)^2$ は $r$ 大で桁落ちする
   （$r=10^8$ で前者は $0$ を返す）。**安定形 $g(r)=\frac1{(\sqrt{1+r}+\sqrt r)^2}$ を使うこと。**

**閉じていないこと（この標的以外の道を含む。T60）**:

1. **【最有望】pull-through の $k$ 積分の相殺**。`E05-F23`（$E(P)\ge E(0)$、確立済）から
   $`(H(-k)-E_0+\omega(k))a_\lambda(k)\psi_0=-\frac{ec_k}m(\epsilon_\lambda(k)\!\cdot\!\pi)\psi_0`$、$H(-k)-E_0\ge0$、
   ゆえに各点で $`\|a_\lambda(k)\psi_0\|\le\frac{ec_k}{m\omega(k)}\|\pi\psi_0\|`$。
   **⚠ これを三角不等式で $`\|a(u_\nu)\psi_0\|\le\int|u_\nu|\|a(k)\psi_0\|`$ に入れると $\lambda^{12/7}$ 悪化して無情報**（w179 が試算済）。
   必要なのは $k$ 積分の**相殺**を拾う Schur 型・作用素値の評価である。**未着手。**
2. **$\Theta$ を経由せず $`\mathcal K=\|\pi\psi_0\|^2`$ で $R$ を押さえる**（$\mathcal K\le\frac{\alpha\Lambda^2}\pi$ は `E05-P32` 3. から在庫）。
3. **上界 `E05-P32` の等号条件から攻める**。稿 `89_` 系 89-2 の「対振幅が密度を必ず上回る」
   （$\langle f,\hat\rho f\rangle\le|\langle\psi_0,a^*(f)^2\psi_0\rangle|$、全 $\theta$-実 $f$）を Gauss 表示側で定量化する。
4. **標的を迂回**: $\Delta'$ を $\langle A^2\rangle_0$ を通さず $`-\frac e{2m}\langle\{P_f,A\}\rangle_0`$ から直接下から押さえる
   （`93_` §3 の副産物により符号が確定している量なので、`93_` §2.2 の「向きの非対称性」が無い）。
5. **標的そのもの（絶対定数 $\theta$）の真偽は未決**である。$\lambda^{-5/7}$ は上界ではなく**現在の在庫の限界**である。

**⚠ 射程**: 本項は **$\mathcal E_A^{\rm odd}$ という量が $\Lambda$ 非一様であるとは主張しない**（**T88**・**T60**）。
閉じたのは (a) の道具と (b) の道具だけである。**`E05-P23` 7. の $\epsilon_2$ 経路は閉じていない。**
**$h(\lambda)$ の datum を含まない。オッズは動かない（T49）。**

**出所**: 稿 `94_A2の下界.md` §3・§5、(研究ノート: `177_w179_quasifree_A2.py`)（T1〜T4 全 PASS、`COUNTEREXAMPLE`）、
(研究ノート: `177b_w179_A2_lower_bound.py`)（S1〜S4 全 PASS）。w179（2026-09-12）。
**波及**: `F61` の「$\langle A^2\rangle_0$ の下界は在庫ゼロ」は**部分的に解消した**（`E05-P?` 2.）。
ただし `FAILED.md` の「非摂動では $\langle A^2\rangle_0\ge\frac{\Lambda^2}{4\pi^2}$ すら在庫に無い」は**そのまま生きている**
（動いたのは $\theta$ 倍の形の下界だけで、真空値以上の形ではない）。

---

---

## F65（「`E05-P32` の虚シフト Gauss 機構を場 2 本（4 点）に延ばし、$\le$ 真空値型の共分散不等式で $O_C$・$R_{\mathcal U}$ を押さえる」— 4 次で Wick 順序積の符号が反転し、$\Phi$ の法則だけでは数保存 2 次に届かない。2026-09-13、w182、稿 `97_`。audit94 が閉鎖の射程を限定）

格付け: `self-audited`（稿 `97_` §6）＋ **audit94 の逆転監査で (a) 成立・(b) は射程限定**（(研究ノート: `97_場2本_audit94_2026-09-13.md`) (II)）。数値 (研究ノート: `182_w182_four_point_class.py`)（seed 1820913、`COUNTEREXAMPLE`）、`183_audit94_theta_reduction.py`（seed 940914、PASS）、`183_audit94_eom_route.py`（seed 940915、PASS）。

**閉じた主張**:
(a) 経路に条件付けた Gauss 公式（純虚の線形指数・正の経路重み）**だけ**から $\langle\Phi(f)^2\Phi(g)^2\rangle_0\le\langle\Phi(f)^2\Phi(g)^2\rangle_\Omega$ または $\langle:\Phi(f)^2\Phi(g)^2:\rangle_0\le0$ を出すこと。
(b) $\Phi$（$\theta$-実の場）の同時法則についての不等式**だけ**で $`\|a(f)a(g)\psi_0\|`$・数重み・2 点応答核を上から押さえ、$`O_C=\frac e{2m}\sum\langle\{\mathrm d\Gamma(K_\nu),A_\nu\}\rangle_0`$ と $R_{\mathcal U}$ に持ち込むこと。

**正確な障害**:
1. **(a) 符号の交代.** 虚シフト $\phi\to\phi+i\rho$ で Wick 順序 $2n$ 点は $(-1)^n\langle\rho_1\cdots\rho_{2n}\rangle_w$。2 点は $\le0$（`E05-P32`）だが **4 点は $\ge0$**。
   律速は「$\rho_i\rho_j$ 交差積の符号」ではなく **$i^4=+1$**（$f\perp g$ でも正の 4 次項 $\langle\rho_f^2\rho_g^2\rangle_w$ が残る）。
   同構造の有限次元類（$|\Psi|^2d\mu_0$、$\Psi=\sum\nu_ke^{ir_k\phi}$、$\nu_k\ge0$）で櫛 $r_k=\pi k$ が $\langle\phi^4\rangle=3.516,3.529,3.535$（$M=10,20,40$）$\gt3$、
   $f\perp g$ で $\langle\phi_1^2\phi_2^2\rangle=1.196,1.200,1.203\gt1$（各 $M$ が厳密な類の元）。$\nu$ が Gauss なら $\langle\phi^4\rangle=3/(1+2\Sigma)^2\le3$ なので、**PF の $\nu$ の形次第で PF の量は $\le3$ でありうる**。
2. **(b) 数保存 2 次は $\theta$-虚の場を含む.** $a^*(g)a(h)=\frac14[\Phi(g)\Phi(h)+\Pi(g)\Pi(h)+i\Phi(g)\Pi(h)-i\Pi(g)\Phi(h)]$、$\Pi(h)=\Phi(ih)$。$\theta$-実の場の双線形の張る空間に非零の数保存 2 次は無い。
   類で $\Psi=\cos(r_0\phi)$ は sub-Gauss 支配を含む $\Phi$ 側の全制約を満たしつつ $`\|a^2\Psi\|^2=r_0^4`$（非有界）。
   **⟹ $\Phi$ 側の情報だけでは $O_C$・$R_{\mathcal U}$ に要る量は押さえられない。** $O_C$ の $\Phi$ だけの 3 点部分は奇数点で 0。
3. **(b) の上界の冪（トレースノルム経由、経路の限界）.** $\Phi$・$\Pi$ の 4 次モーメント上界が仮にあっても $|O_C|/D_{\rm free}\lesssim C'\sqrt{24\alpha\lambda/\pi}$、$|R_{\mathcal U}|/D_{\rm free}\lesssim C'\sqrt{96\alpha\lambda/\pi}$（$p=1/2$。`95_` §5 表の $`\mathrm{tr}|K_\nu|\le Q\|\beta\|_2^2`$ を未検証のまま使用）。

**再挑戦禁止の範囲（証明が実際に排除した分岐のみ。T60）**: 「虚シフト＋正の重み」の構造**だけ**から (a) の $\le$ 真空値型 4 点不等式を出す型、および $\Phi$ の同時法則**だけ**から数重み・密度・$\mathrm d\Gamma(K)$ を押さえる型。**基底状態性（運動方程式・二重交換子）を併用する型は禁止しない**（類の反例はどの $H$ の基底状態でもない。audit94 II-d3）。

**生きている分岐**:
(i) **⭐ 運動方程式の道（audit94 が実在を確認）**: $\Theta=JV$ 選択則で $`\langle\{\mathrm d\Gamma(L),A_\nu\}\rangle_0`$・$`\langle\{P_{f\nu},\mathrm d\Gamma(L)\}\rangle_0`$ は $L_-=\frac12(L-\theta L\theta)$ だけに依存し、$O_C$ は $\Pi$ ちょうど 1 本の 3 点関数 $\langle\Phi_g\Phi_u\psi_0,\Pi(h)\psi_0\rangle$ に落ちる。
   $`\Pi(\omega f)\psi_0=i(H-E_0)\Phi(f)\psi_0-\frac1{2m}\sum_\mu\{\pi_\mu,\Phi(ik_\mu f)\}\psi_0`$ と、$X=\Phi_g\Phi_u$ の二重交換子（$\Phi$ 類の 2・4 点だけ）で**在庫だけの非摂動上界が付く**。粗い勘定の冪は $p=3/2$（在庫 `E05-P32` 5. の (C) と同冪で改善はまだ無い）。窓つき角 Schur・核の構造を入れる余地は未検査。
(ii) $\Pi(h)$（$\theta$-実 $h$）の非摂動な揺らぎ上界（**十分側の候補であって必要条件ではない**。$O_C$ には 2 次、$R_{\mathcal U}$ には 4 次で足りる。**【2026-09-13 audit95 訂正】「足りる」は過大: $\Pi$ の一様上界があっても障害 3 のトレースノルム経由では $p=\frac12$ が残り、$O_C$ に要るのは殻全方向の $`\|\rho_S\|_{op}`$（$\bar r$ より真に強い）。`F66`・`E05-P40` 参照。**Robertson で $`\langle\Pi(h)^2\rangle_0\ge\|h\|^2`$、上界は在庫ゼロ）。
(iii) PF の $\rho[b]$ 固有の構造（Brown 並進つき伊藤積分）が類より強い制約を与える可能性（**反例は型の kill**）。
(iv) R6 の帰結 $`\|(H-E_0)^{1/2}\Phi(f)\psi_0\|^2\le\langle f,(\omega+\frac{k^2}{2m})f\rangle`$（$\theta$-実 $f$、非摂動。audit94 II-g、未昇格）。
(v) $\Phi$ 4 本の量には `97_` 系 97-3 の絶対定数上界 $C_4=9.26$ がある（閉じていない側の成果）。

**出所**: 稿 `97_場2本の共分散.md` §2・§4・§5、w182（2026-09-13）。射程限定は audit94（2026-09-13）。

## F66（「在庫の非摂動道具（二重交換子・FK の時間微分・数重み・運動方程式経路の尖鋭化）で共役運動量場 $\Pi(h)$（θ-実 $h$）の揺らぎに $\Lambda$ 一様な上界を出す」— どの道具も上界を与えないか $\lambda$ を払う。2026-09-13、w183、稿 `98_`。audit95 が逆転監査で成立・射程を限定）

格付け: `self-audited`（稿 `98_` §6）＋ **audit95 の逆転監査で閉鎖は成立、「欠落の同定」は射程限定**（(研究ノート: `98_Pi揺らぎ_audit95_2026-09-13.md`) M5）。**本項は w183 の (研究ノート: `w183.FAILED.md`) を置き換える。**

**閉じた主張**: θ-実 $h$ について $`\langle\Pi(h)^2\rangle_0\le C\|h\|^2`$（$C$ は $\Lambda$ 一様）を、(i) 二重交換子 $\langle[\Pi,[H,\Pi]]\rangle_0$、(ii) `E05-F24` の汎関数積分で $\Pi$ を時間微分として入れる形、
(iii) $\langle\Pi^2\rangle$ と光子数重みの在庫、(iv) audit94 II-d4 の運動方程式経路の CS 因子の改良、のいずれかで出すこと（発注 w183 (C)、親の追加）。

**正確な障害**:
1. **(iii) 発注の不等式は向きが逆。** $`\langle\Pi(h)^2\rangle_0\le\|h\|^2+4\langle a^*(h)a(h)\rangle_0`$ ではなく、平行四辺形則と `E05-P32` 2. から **$\ge$ が定理**（`98_` 命題 98-1）。
   上界側は $s(\sqrt{1+r}+\sqrt r)^2\le2s+4\rho$ で、**$\Pi(u_\nu)$ の上界は $\bar r$ の上界と、殻の全 θ-実方向の $\Pi$ の上界は $`\|\rho_S\|_{op}`$ の上界と、それぞれ因子 2 以内で同値**（**両者は同一量ではなく後者が真に強い**。audit95 M5 (c)）。在庫（`E05-P22` 5.＋`E05-F4`＋真空変分）では $\bar r\le\frac{\alpha\lambda}\pi$ で **$p=1$**（E05-L4 枝で $5/7$）。
2. **(i) 二重交換子は下界しか与えない（T43）。** $\langle\Pi(h)(H-E_0)\Pi(h)\rangle_0=\langle h,\omega h\rangle+\frac1{2m}\sum\langle\Pi(q_\nu h)^2\rangle_0+\frac{2e^2}m\sum\langle u_\nu,h\rangle^2$ は
   反跳に依らないプラズマ項で $\alpha\lambda$ に増え、右辺に $\Pi$ が再登場する。$\langle\Pi^2\rangle$ への変換はギャップ（F62 で空）か感受率 $\langle\Pi(H-E_0)^{-1}\Pi\rangle$ の上界（在庫ゼロ）を要する。
   **audit95 が実際に試した再帰（EOM で $\Pi(\omega h)\psi_0$ を書き、$\Pi$ 側恒等式と II-g で CS）は $Y=\sup_h\langle\Pi(h)^2\rangle_0\lesssim\lambda^2$（$p=2$）で在庫より悪い。**
3. **(ii) FK の Euclid 時間微分は $\Pi$ 単独に対応しない。** 対応するのは $`i[H,\Phi]=\Pi(\omega g)+\frac1{2m}\{\pi_\nu,\Pi(k_\nu g)\}`$（反跳項が電子を含む）。
   虚シフトの補正 $-C(\tau)$ の曲率から来る符号は（発見的に）**下界向き**。証明はしていないので、この項目は「符号を与える道具が無い」までを閉じる。
   **階数 3 のスクイーズ $`\frac14\{\Phi(\hat u),\Pi(\hat u)\}`$ の hypervirial（audit95）も $\Pi$ を相関 $\langle\Pi(\omega\hat u)\Pi(\hat u)\rangle$ と $\Pi$ 1 本の 3 点関数にしか出さず循環。全殻スクイーズ版はトレースで階数 3 を見ず `F64` 障害 3 と同じ穴。**
4. **(iv) 運動方程式経路（$\Pi$ 上界を要さない。audit94 II-d3）は CS 段で $\lambda^1$ を払い、因子の改良では回収できない。** CS の 2 因子は**値として鋭い**
   （第 2 因子は `98_` 命題 98-4 の恒等式で、1 ループで上界 $\langle h',(\omega+\frac{k^2}{2m})h'\rangle$ と同次）。損は (a) 自由場で行列要素が光子数パリティにより 0 なのに CS 積が $O(1)$、
   (b) EOM の 2 項が各々反跳 $\lambda$ を持ち和で相殺、の 2 つで、97-5 の $\Pi$ 経路 $p=\frac12$ と EOM 経路 $p=\frac32$ の差 $\lambda^1$ は (b) と一致する。
   回収には (a) 奇パリティ成分の非摂動な小ささ（`E05-P23` 7. の $\epsilon_2$ 型）、(b) $(H-E_0)$ スペクトル上の相関が要り、(b) は在庫の中では **$`\|\rho_S\|_{op}`$ 上界**（$\bar r$ ではない）に戻る（**見立て**）。

**射程（T60）**: **$\Pi$ の一様上界が偽だとは言っていない。** 値の側では反跳なし $\tilde K$ で $\sqrt{\alpha\lambda/\pi}$ に膨らむ（反跳を捨てた模型なので $\psi_0$ の証拠ではない。F64 と同じ）が、
1 ループでは $O(\alpha)$ 係数 $\frac{2K(\lambda)}\pi\lt\frac{2K_0}\pi=1.389$、$\bar r_2\to0.550\alpha^2$ で**どちらも $\lambda^0$**（展開 (iv′) 仮定の値。E05-L4・T61）。
**⚠ 欠落の同定の射程（audit95 M5 (h)）**: 「$\bar r$ 上界 1 つで足りる」は **$\Pi(u_\nu)$ の一様上界と $\langle A^2\rangle_0$ の絶対定数下界（`E05-P36` 1. 経由）について**のみ正しい。
**$O_C$ の一様化には足りない**——$O_C$ に要るのは殻の一般方向（$`\|\rho_S\|_{op}`$）で、しかも `F65` 障害 3・audit94 II-e により $\Pi$ の 4 次までの一様上界があっても Π 経路は $p=\frac12$ が残る。
**再挑戦してよい範囲**: 反跳を保持したまま $\bar r$（$u$ 方向の 1 光子密度）または $`\|\rho_S\|_{op}`$ を直接押さえる評価（例: $u$ 方向に射影した pull-through で分母の $\frac{|P_f-k|^2}{2m}$ を残す。`F54` の閉鎖範囲との照合が先）。EOM 経路の損 (a)（光子数パリティ直交）を捨てない**別の分割**は排除していない。
**戻らない範囲**: 二重交換子の単独使用、FK の時間微分の符号論、EOM 経路の**この CS 分割での因子の改良**、$\tilde K$ の基底状態にも同じく適用できる論法での $\bar r$ 上界。

**出所**: 稿 `98_Piの揺らぎ上界.md` §5、(研究ノート: `184_w183_Pi_fluctuation.py`)（PASS）、w183（2026-09-13）。親の追加項目 (iv) は audit94 II-d2〜d4 を前提とする。逆転監査 audit95（2026-09-13、(研究ノート: `187_audit95_IIg_toy_and_oneloop.py`) PASS）。


## F67（「$\mathcal E_A^{\rm odd}$ の 1 ループ値で (H-$\hat Q$) を摂動有効域の内側で殺す」— 窓が開かない。2026-09-13、w181、稿 `96_`。audit96 が射程を補正）

格付け: `self-audited`（稿 `96_奇部の1ループ値.md` §3–§5・§7）＋ **audit96 の破壊監査で閉鎖は壊れず（射程 2 点を補正）**（(研究ノート: `96_99_奇部_audit96_2026-09-13.md`) (R4)）。数値は
(研究ノート: `179_w181_odd_oneloop_value.py`)（jobs `179_w181_scan`、6 族 × $\lambda=64\dots262144$ の 7 段、`conclusion: PASS`）、
T54 検査 `179b_w181_ED_check.py`（`PASS`）、第 2 経路と $\beta$ 一様上界 `179d_`（`PASS`）・`179e_`（`INCONCLUSIVE`＝上界の冪が 2 段安定しない。窓判定は $\lambda_*$ での大きさだけを使い、表の範囲内・外挿なしで余裕 60 倍）、
独立再実装 `188_audit96_odd_C6_independent.py`（audit96、seed 960913、`PASS`。反転対称なしの正四面体群模型で 3 片の核表示と ED を 13 桁／差の比 0.251 で再現）、`188b_audit96_n2sq_quadrature.py`（audit96、上界入力 $n_2^2$ を決定論求積で 0.3% 以内再現、2 点のみ）。

**閉じた主張**: `F56` 生きている分岐 (c)・`92_` 枝 1 が「有効域の内側で (H-$\hat Q$) を殺しうる唯一の未計算量」とした $\mathcal E_A^{\rm odd}$ について、
1 ループ**値**が有効域 $\lambda\lesssim\alpha^{-5/2}$（E05-L4）の内側で $O(1)$ に達し (H-$\hat Q$) を殺す——という設計（**$\alpha=1/137.036$**）。

**正確な障害（3 段）**:

1. **最低次は $e^6$ で、支配片は $`O_B=\{P_f,c\}`$、冪は $\lambda^{-1/2}$。** (iv′) の下で $\mathcal E_A^{\rm odd}=e^6\mathcal C_6+O(e^8)$、$\mathcal C_6=O_A+O_B+O_C$（別の記録 `61_` と同じ分け方）。
   低階数の許容球帽 6 族（`E05-P27` A/B/C 同型・複素位相・パリティ奇 4 球帽・2 方向）で
   $O_B/D_{\rm free}\simeq-C_B\alpha^3\lambda^{-1/2}$（$C_B\le1.5\times10^{-2}$、全 42 点で負）、$O_A\propto\lambda^{-1.9}$（窓の $q=k+k'$ で抑制）、$O_C$ は誤差内 0（奇族の $\lambda\le256$ のみ有意、$\le1.6\times10^{-6}\alpha^3$）。
2. **$\beta$ 一様な 1 ループ上界も小さい**（CS＋窓、全 $\mathrm{supp}\beta\subset W_{S,Q}$。**全階数の窓核を含む**）: $|O_B|/D\lesssim1.3\alpha^3\lambda^{-1/2}$（値と同じ冪）、
   $\alpha=1/137.036$ の有効域端 $\lambda_*=\alpha^{-5/2}=2.2\times10^5$ で $|O_A|/D\lesssim10^{-5}$、$|O_C|/D\lesssim1.7\times10^{-2}$（$`\nu_3=\|a(u)\phi_3\|`$ の紫外成長で最も緩い）。
   **⚠ 上界の CS 連鎖は解析的だが、入力 $t,n_2,n_3,\nu_3$ は 1 ループ量の MC 推定（$\lambda\ge16384$ で裾が重く反復で 20〜30%）で、厳密な上界ではない。** 表は中心値より保守的（2σ・表の最大×2）。
3. **窓判定（T86・T88）**: 値は $p\lt0$ で $\lambda\ge1$ のどこでも $O(1)$ に達しない（**値**・「殺せる」側に使えるが殺せない）。
   上界も有効域の内側で 3 片とも $O(1)$ に遠い（**上界**・「殺せない」側）。**⟹ `92_` 枝 1 の 4 項すべてで、1 ループの測定は有効域の内側で障害を見ない。**
   $\alpha$ を動かすと $O_C$ 上界は $\lambda_*(\alpha)$ で $`\approx0.8\,\alpha^{0.83}`$（表の最後 2 点の傾きで外挿）で $\alpha\le1$ では $O(1)$ に達しないが、$\lambda_*(\alpha)$ が測定域 $\lambda\ge64$ に入るのは $\alpha\lesssim0.19$ だけで、**それ以外の $\alpha$ は外挿**（audit96）。

**再挑戦禁止の範囲（証明・計算が実際に排除した分岐のみ。T60）**:
「**(iv′) を仮定した $\mathcal E_A^{\rm odd}$ の 1 ループ（$e^6$）数値**を根拠に、**$\alpha=1/137.036$ で** (H-$\hat Q$) を有効域の内側で殺す」型。
理由は $\beta$ 一様な上界（稿 `96_` 命題 96-4、入力は MC）であって族の選び方ではない。**有効域の外（$\lambda\gtrsim\alpha^{-5/2}$）は 1 ループが有効でないので対象外**（T61）。
**有限モード ED について（audit96 が理由を訂正）**: 有限モードで禁止されるのは「**$\lambda$ 冪**を測る」ことで、理由は殻の離散近似と角度分解能（T80）・$\Lambda$ 連続体を検証しないこと（F51・T64）である。
「回転不変でない模型では $\Pi_1\psi_0\ne0$ で $e^4$ が混入する」は**対称性の低い模型に限る**: 各 $k$ の安定化群が横ベクトルを固定しない対称模型（`179b_` の軸 6 方向・立方体 8 方向、`188_` の正四面体群 16 モード）では $\Pi_1\psi_0\equiv0$（$\le10^{-15}$）で $e^6$ 係数は清浄に取れ、**代数の検査には使える**。

**生きている分岐**:
- **(a) 奇部の非摂動評価。** 本項は (iv′) 依存の 1 ループだけを閉じた。`E05-P23` の上界は $\Lambda$ 非一様のまま（T60・T61。$`\mathrm{Re}\,O_B`$ は `E05-P38` で窓クラス $\Lambda$ 一様、$O_A$ は稿 `99_` 命題 99-2 で $p=5/4$）。**この方向の発注を本項で止めてはならない。**
- **(b) $O_B$ の $\mathcal E_A^{\rm c}$ への吸収**（稿 `96_` 観察 96-5: 6 族で $O_B\simeq-0.27\alpha^2\mathcal E_A^{\rm c}$、$\beta$ 一様ではない）。非摂動では 別の記録 `61_` の Riesz ベクトル $w_\nu=d(r)P_Te_\nu$ の点ごと評価 $`|e\,d/c|\lt1`$ が要る。
- **(c) 全階数の奇な窓核（`E05-P25` A/C/D）での $O_C$・$O_A$ の値**（上界で窓判定は済み。値は未測定）。
- **(d) $O_A$ の多方向核での交差項の成長**（2 方向で 2 倍を実測、$\propto N$ の可能性）。
- **(e) $`\mathrm{Im}\,O_B`$・$`\mathrm{Im}\,O_C`$**: 連続体ではパリティで擬テンソル項が落ちるが、$\mathrm{Im}$ が $\beta$ 一様に 0 とは示されていない（反転なし有限模型では非零。audit96 (R2)）。

**閉じていないこと（T60。射程を広げないこと）**:
- **(H-$\hat Q$) を証明していない。** $\mathcal E_A^{\rm odd}$ の $\Lambda$ 一様な非摂動上界は無い。
- **符号について $\beta$ 一様な主張をしない**（6 族で負だっただけ）。
- **$h(\lambda)$ の datum を含まない。オッズは動かない**（**T49**）。

---

## F68（「運動方程式・二重交換子・$\Theta$ 選択則で奇部 $`O_A=\frac em\sum_\nu\mathrm{Re}\langle\{T_\nu,b_\nu\}\rangle_0`$ の障害を $\Phi$（$\theta$-実の場）側へ移し、`E05-P32`・`E05-P39`・audit94 II-g だけで押さえる」— **端だけに使う EOM** と $\pi$ 置換では数重みが消えない。2026-09-13、w184、稿 `99_`。audit96 が障害 1 の射程と生きている分岐を補正）

格付け: `self-audited`（稿 `99_` §5、worklog (研究ノート: `2026-09-13_w184_新在庫.md`) §3.3・§4 R10〜R12）＋ **audit96 の破壊監査**（(研究ノート: `96_99_奇部_audit96_2026-09-13.md`) (R8)(R9)。障害 2 は別の書き方でも壊れず、障害 1 は理由が不完全）。**型の kill（経路の限界）であって量の kill ではない（T60・T88）。** 数値なし（型検査のみ）。

**閉じた主張**: 発注 w184 (B)「`95_` §5 (K1) の障害（$T_\nu$ が $\Theta$ 不変でない、反自己共役部が $\Phi(ig)$ と組む）を二重交換子不等式か運動方程式で $\Phi$ 側へ移す」のうち、下の (a)(b)(c) の型。

**正確な障害**:
1. **場の形では $\Pi$ 3 本の相関が残る.** $\beta$ は $\Theta$ で $\theta$-実に帰着でき（$`\mathrm{Re}\,O_A(\beta)=\mathrm{Re}\,O_A(\beta_r)+\mathrm{Re}\,O_A(\beta_i')`$）、そのとき $T_\nu$ は $\Theta$-奇になって (K2) の「$\Theta$ 不変でない」は解消するが、
   $q\beta=i\gamma'$ から $T=M+iP$、$P\ni-\frac18\sum\gamma'_{jk}\Pi_j\Pi_k$ で $`\mathrm{Re}\langle\{T,a(g)\}\rangle_0\ni+\frac1{16}\sum\gamma'_{jk}\langle\{\Pi_j\Pi_k,\Pi_g\}\rangle_0`$。
   $\Theta=K(-1)^N$ の下で $\Pi$ は偶なのでこの項は選択則を通る。**EOM を $\psi_0$ に隣接する $\Pi$ にだけ使うと、中央の $\Pi$ には $\Pi$ の 2 次・4 次モーメント（在庫ゼロ）が残る。**（$\Pi^3$ 項が恒等的に 0 でないことは示していない。）
   **⚠ 射程（audit96）**: EOM の後に $(H-E_0)$ を残りの 2 本に通すと $[H_f,\Pi(h)]=i\Phi(\omega h)$、$`[\pi_\mu,\Pi(h)]=i\Phi(k_\mu h)+2ie\,\mathrm{Re}\langle u_\mu,h\rangle`$ で**中央の $\Pi$ は $\Phi$ に替わり**、$\Phi\Phi\Pi$ 型（`F65` 生きている分岐 (i) と同型）＋ $\pi$ を 1 本含む剰余（$`\|\Phi_f\pi\psi_0\|`$ 型、`P32`/`P39` の射程外）になる。**この経路は検査されておらず、本項は閉じていない。**
2. **$\pi$ 置換の形では真空スケールの項がゼロ.** $`T_\nu=[\pi_\nu,F]-e\,a^*(g_\nu)`$ で厳密に $`O_A=\frac em\sum\mathrm{Re}\langle\{[\pi_\nu,F],b_\nu\}\rangle_0-\frac{e^2}m\sum(\|g_\nu\|^2+2\|b_\nu\psi_0\|^2)`$。
   端の $\pi$ は $\pi\psi_0$ の双対評価（稿 `99_` 補題 99-3）で $\sqrt m\langle[X^*,[H,X]]\rangle_0^{1/2}$（$X=Fb_\nu$）に落ちるが、$X\Omega=X^*\Omega=0$ なので $\langle\Omega,[X^*,[H,X]]\Omega\rangle=0$ で**全項が数重み・密度・対振幅を経由する**。型は直接の CS（稿 `99_` 命題 99-2）と同じで利得なし（audit96 が $H_f$ 部・$\pi^2$ 部を別に書いて前因子 $\sqrt{m\Lambda}$・重み $N^{3/2}$ を再現）。
3. **$\Pi$ 揺らぎの EOM 自己無撞着評価は在庫より悪い.** $`X_\Pi=\sup\langle\Pi(h)^2\rangle_0/\|h\|^2`$（殻上 $\theta$-実）について EOM＋II-g＋二重交換子の主項は $X_\Pi\lesssim\lambda^2/4$、在庫は $X_\Pi\le2+\frac{4\alpha\lambda}\pi$。
   原因は II-g の反跳 $\frac{k^2}{2m}$ が殻上で $\omega$ の $\lambda/2$ 倍になること。

**再挑戦禁止の範囲（証明が実際に排除した分岐のみ。T60）**: (a) $O_A$ を場の形に書いて EOM を**端の $\Pi$ にだけ**使い、$\Pi^3$ 項を $\Phi$ の法則（`P32`・`P39`）と II-g だけで押さえる型。
(b) $\pi$ 置換＋$\pi\psi_0$ の双対評価で $O_A$ の数重みを消そうとする型（真空スケール部がゼロ）。
(c) II-g を殻上の $\Pi$ 揺らぎの自己無撞着評価に使う型。
**禁止しないもの**: $O_A$ の $\Lambda$ 一様上界そのもの、$\Pi$ 揺らぎ・1 光子密度・$\langle N_S^2\rangle_0$ の一様上界を**別機構**で出すこと、$\Phi$ 2 本＋$\Pi$ 1 本の部分への audit94 II-d の道の適用、窓つき角 Schur の精密化、**$(H-E_0)$ を中央の $\Pi$ に通して $\Phi$ に替える経路（障害 1 の射程）**。

**生きている分岐**（稿 `99_` 命題 99-2 の連鎖 $`2.1913\sqrt\alpha\lambda^{-1/4}\mathcal M\|\rho_S\|_{op}^{1/2}`$ を $\Lambda$ 一様にする**十分条件は 1 パラメータ族**で、両端は次の (i)(ii)。**「足りないのは 1 つ」ではない**。audit96 (R9)）:
(i) **殻の数重み $\langle N_S^2\rangle_0\lesssim\alpha^{-2/3}\lambda^{1/3}$**（$`\|\rho_S\|_{op}\le\langle N_S\rangle_0\le\mathcal M`$ で束ねた場合。`E05-P14` の連鎖の床は $p\ge1$ なので別機構が要る）。
(ii) **$`\|\rho_S\|_{op}\lesssim0.51\,\alpha^{-3}\lambda^{-3/2}`$**（$\mathcal M$ は在庫 `E05-P14` 2. の $2t$ のまま。$\langle N_S^2\rangle_0$ とは別の量で、`E05-P32` 2. で対振幅に、1 モード恒等式で殻上の $\Pi$ 揺らぎに結びつく。`F65` (ii) と同じ量）。
(iii) $O_A$ の $\beta$ の二次形式としての角局在（`E05-P38` の角 Schur 型）を 3 点核に入れる精密化（未検査）。
(iv) **障害 1 の射程で開いた経路**: $(H-E_0)$ を中央の $\Pi$ に通して $\Phi\Phi\Pi$ 型＋$\pi$ 剰余に落とす（剰余の $`\|\Phi_f\pi\psi_0\|`$ を押さえる入力が要る。未検査）。


<!-- audit97（2026-09-13）: 本ファイルの (1)(2) は (研究ノート: `w185.FAILED.md`)・(研究ノート: `w186.FAILED.md`) を**置き換える**（あちらは連結しない）。PROVED 側の対応は (研究ノート: `audit97.PROVED.md`) の (1)(2)(3)。親は採番後に「PROVED (k)」「FAILED (k)」を ID に置換すること。 -->

## F69（(1)「pull-through の分子を $`\|\pi\psi_0\|`$ 系で、resolvent を作用素ノルムで押さえる鎖」で $\bar r$ に $\Lambda$ 一様上界を出す — ファイバースペクトルだけでは $p=2$、対角恒等式 $J\le\frac32mS$ と組んでも $`\|T\|`$（全空間・$V_{\rm inv}$ とも）の Jensen 下界で $\ln\lambda$ 1 つ届かない。2026-09-13、w185・w186、稿 `100_`・`101_`）

**【親注記 2026-09-13】本群の (1)(2)(3) ＝ `E05-P46`・`E05-P47`・`E05-P48`、FAILED の (1)(2) ＝ `F69`・`F70`。監査記録 (研究ノート: `100_101_rbar_audit97_2026-09-13.md`)（S0、PATCH 適用済）。**

格付け: `self-audited`（稿 `100_` §5.1・§6、`101_` §2）＋ **audit97 が S2 合同監査で閉鎖を成立と判定**（(研究ノート: `100_101_rbar_audit97_2026-09-13.md`) M8・M9・N4）。数値 (研究ノート: `186_w185_J_identity_oneloop.py`)（`PASS`、値のみ）。

**閉じた主張**:
(a) `E05-F20`・`E05-F23`（ファイバーのスペクトル）と $`\|\pi\psi_0\|`$ の上界だけから $`\bar r=\frac{4\pi^2}{\Lambda^2}\sum_\nu\|a(u_\nu)\psi_0\|^2`$ の $\Lambda$ 一様上界を出す（発注 w185 (A)）。
(b) 対角量の評価 $`J\le c\,mS`$（$c$ は $\Lambda$ 一様。PROVED (1) 2. は $c=\frac32$）と $`\|T\pi\psi_0\|^2\le\|T|_{V_{\rm inv}}\|\,J`$ を組み、**$T$ の（全空間または $V_{\rm inv}$ 上の）作用素ノルム**の評価で $\bar r=O(1)$ を出す。

**正確な障害**:
1. **(a)** 素朴鎖は $`\bar r\le\frac{e^2}{m^2S}\|T\|^2\mathcal K\le\frac{4\alpha^2\lambda^2}{9\pi^2}`$（`E05-L4` 枝で $\lesssim\alpha E_0/m$）。`E05-F20` により $`\|R(k)\|\ge\frac1{2|k|}`$ なので $`\|R(k)\|`$ だけを使う評価は $`\int c_k^2\|R(k)\|\ge\frac\Lambda{12\pi^2}`$ を越えず、$\mathcal K$ の上界は $\alpha\to0$ で値 $\approx e^2S$ を下回れない（`E05-P10`）。**この型では $p=2$ が下限**（在庫 $p=1$ より悪い）。
2. **(b)** $`\|T|_{V_{\rm inv}}\|\ge\frac m{3\pi^2}\ln(1+\frac\lambda2)`$（PROVED (2)。全空間版は PROVED (1) 4.）。ゆえに $`J\le c\,mS`$ 型の評価と組む限り鎖の右辺は $\frac{4c\alpha}{3\pi}\ln(1+\frac\lambda2)$ 以上で発散する。
   1 ループ（値）では $`T_{\rm eff}=\|T\pi\psi_0\|^2/J\to0.063m`$ に飽和し、損は $`\|T\|\to T_{\rm eff}`$ の段にちょうど $\ln\lambda$ として局在する。

**再挑戦禁止の範囲（T60。証明が実際に排除した分岐のみ）**: (a) $`\|R(k)\|`$（各 $k$ のスペクトル情報）と $\mathcal K$ の上界だけを使う評価。(b) **$T$ 全体の作用素ノルム（全空間・$V_{\rm inv}$）を $`J\le c\,mS`$ と組んで** $\lambda^0$ を狙うこと。
**$\bar r$ の一様上界そのものを否定しない。** 1 ループ値は $\bar r_2\to0.55\alpha^2$（$\lambda^0$）。**$J$ 自身が $\lambda$ とともに減る（$J\lesssim mS/\ln\lambda$）ことを示す道は排除していない。**

**生きている分岐**:
(i) **二進殻版**（PROVED (3)）: (N-shell) $\sup_j\tau_j\le C_Nm$、最弱で (N-top) $`\tau_j\le Cm\,2^{j(1-\delta)}`$ なら $\bar r\le C\alpha$。**ただし 3 性質だけからの証明は不可能**（FAILED (2)）。
(ii) (N) $`\|T|_{V_{\rm inv}}\|\le Cm\ln(2+\lambda)`$ が立てば $\bar r\le C'\alpha\ln(2+\lambda)$（$p=0$ の対数）。(N) は成れば鋭い（PROVED (2)）。
(iii) 反跳を保持する $H(-k)$ の作用素下界を PF 固有の構造と組む形（`E05-F23` の引き算 $E_0$ が障害）。
~~(旧 w185 の「$V_{\rm inv}$ の非摂動 $\ln\lambda$ 下界は未証明」「$q$ 分解版」)~~ は PROVED (2)(3) で失効。

**出所**: 稿 `100_rbarの一様上界.md` §3.3・§4・§5、稿 `101_Tの回転不変セクタ.md` §2・§3、w185・w186（2026-09-13）、audit97。

---

## F70（(2)「$H(P)$ の 2 次性（Hessian $\frac1m$）＋ `E05-F23`（$H(P)\ge E_0$）＋ 回転共変（＋作用素単調性・平行四辺形恒等式・期待値の反跳）だけで (N)・(N-shell)・(N-top) を示す」— Landau 玩具で論法の型として閉鎖。2026-09-13、w186、稿 `101_` §4）

**【親注記 2026-09-13】本群の (1)(2)(3) ＝ `E05-P46`・`E05-P47`・`E05-P48`、FAILED の (1)(2) ＝ `F69`・`F70`。監査記録 (研究ノート: `100_101_rbar_audit97_2026-09-13.md`)（S0、PATCH 適用済）。**

格付け: `self-audited`（稿 `101_` §4.3・§7 R11・R12）＋ **audit97 が逆転監査で閉鎖を成立と判定し、玩具族の頑健性を補強**（(研究ノート: `100_101_rbar_audit97_2026-09-13.md`) X1〜X7、独立再実装 (研究ノート: `191_audit97_landau_toy_shell.py`)、seed 970913、`PASS`）。

**閉じた主張**: 発注 w186 (B)(i)「反跳を持つ $H(-k)$ の作用素下界（作用素単調性、`E05-F23`、`E05-F7`）で回転平均した resolvent を $\frac1{|k|}$ より良く押さえる」を、上の 3 性質だけから行うこと。

**正確な障害**:
1. **期待値の水準では分離がある**: 平行四辺形恒等式 $\frac12(H(-k)+H(-k'))=H(-\frac{k+k'}2)+\frac{|k-k'|^2}{8m}$ と `E05-F23` で $X_k+X_{k'}\ge\frac{|k-k'|^2}{4m}+|k|+|k'|$（$X_k=H(-k)-E_0+|k|$）。$V_{\rm inv}$ では反跳の線形項が恒等的に 0（PROVED (2) 1.）。
2. **しかし期待値の分離は resolvent の和を押さえない**。スペクトル部分空間 $\mathbf 1_{[0,2K]}(X_k)$ 上の $`\|(\pi+k)u\|^2`$ の在庫評価は $2m(2K+E_0)$ で $E_0$ が入る。
3. **反例となる玩具**: 方向 $\hat n\in S^2$ の一様磁場 $B\hat n$（対称ゲージ）の直積分 $H=\int^\oplus\frac{(p-eA_{\hat n})^2}{2m}$ は 3 性質をすべて満たし（$e^{ik\cdot x}$ で $H(-k)\cong H\ge E_0=\frac{eB}{2m}$。平行四辺形恒等式も成立）、
   試行 $v_\mu(\hat n)=\hat n_\mu w_{\hat n}$（最低 Landau 準位の軸対称状態 ⊗ 縦方向の幅 $\to\infty$ の Gauss）で、$m\ll K\lesssim\ell^{-1}=\sqrt{2mE_0}$ の殻に $\tau_K\gtrsim c\sqrt{mK}$（audit97 の厳密評価で $c\approx0.03$）。
   **$\Lambda$ 一様性の否定には $B=B(\Lambda)$ と選ぶ。$E_0$ を PF の既知窓 `E05-L4`（$\alpha^{1/2}\Lambda^{3/2}m^{-1/2}\lesssim E_0\lesssim\alpha^{2/7}\Lambda^{12/7}m^{-5/7}$）や真空変分上界 $\frac{\alpha\Lambda^2}{2\pi m}$ 以下に置いても $\ell^{-1}\gtrsim\Lambda^{3/4}\gg\Lambda^{2/3}$ なので、(N)・(N-shell)・(N-top)（全 $\delta\ge0$）がすべて破れる**（audit97 X3）。期待値は $\approx K^2/2m$ で 1. と矛盾しない。
4. **在庫は玩具を排除しない**: 玩具は $E(P)\equiv E_0$（平坦な分散）だが、`E05-F23` は $\ge$ のみ、`E05-F9` は $|P|\ge\Lambda$ かつ窓内の主張で、在庫に平坦分散を排除する非摂動入力は無い（audit97 X5）。

**再挑戦禁止の範囲（T60）**: 上の 3 性質（と作用素単調性・平行四辺形恒等式・期待値の反跳）**だけ**を使う (N)・(N-shell)・(N-top) の証明。
**(N) を反証するものではない**（玩具は PF ではない）。**PF 固有の構造**（$[\pi_i,\pi_j]$ が c 数でなく場の作用素 $`e\,\mathrm{curl}A`$ 型で $H_f$ と非可換＝周波数 $\sim\Lambda$、$H_f$、$\psi_0$ 周りのスペクトル、$E(P)$ の非平坦性を与える新入力）を使う証明は生きている。

**生きている分岐**: (a) Landau 型機構（玩具の機構）が効きうるのは $K\lesssim\sqrt{2mE_0}$ の殻で、真空変分枝では $K\lesssim\sqrt{\alpha/\pi}\Lambda$、`E05-L4` 枝では $K\lesssim\alpha^{1/7}m^{1/7}\Lambda^{6/7}$（**他の機構を排除しない**）。最上殻帯での (N-top) を PF 固有の構造で狙う（`F4` の決定窓と同じ尺度）。そこで立ち、その下で $\tau_K\le C\sqrt{mK}$（**未証明の仮定**）なら $\bar r\lesssim C\alpha(1+\alpha^{3/4}\sqrt\lambda)$（真空変分枝 $p=\frac12$、`E05-L4` 枝 $p=\frac27$）。下の帯で自明な $\tau_K\le\frac K{12\pi^2}$ しか使えなければ $p=1$（`E05-L4` 枝 $\frac57$）で、同じ枝の在庫と同じ冪。(b) 実効磁場の断熱性（サイクロトロン周波数 vs $\Lambda$）の見積り。

**出所**: 稿 `101_Tの回転不変セクタ.md` §4、w186（2026-09-13）、audit97（(研究ノート: `191_audit97_landau_toy_shell.py`)）。

---


**【audit98 追記注記 → F63】（2026-09-13、S2 合同監査 (研究ノート: `93_94_audit98_2026-09-13.md`) (R4c)。本文は改変しない）**
1. **kill 不発という結論は成立。** 母不等式・分子の下界ゼロ・(D) 不発の判定は正しい。
2. **「不確定性関係で $\langle A(0)^2\rangle_0$ の下界を出す」発注の禁止は撤回する（T60 の実害型）。**
   Robertson $`\langle\Phi(u)^2\rangle_0\langle\Pi(u)^2\rangle_0\ge\|u\|^4`$ に `E05-P40` 1.（verifier-backed）の上側 $\langle\Pi(u)^2\rangle_0\le s(\sqrt{1+r}+\sqrt r)^2$ を入れると
   $`\langle\Phi(u)^2\rangle_0\ge s\,g(r)`$ で、**`E05-P36` 1. と値まで同値**になる。本項の「$\Lambda^1$ しか出ない」は真空変分枝 $E_0\le\frac{\alpha\Lambda^2}{2\pi m}$ を入れた値
   （`E05-P36` 2.(i) の大 $\alpha\lambda$ 形と同じ $\Lambda^1$）で、`E05-L4` 枝なら $\Lambda^{9/7}$ が出る。「$\langle N\rangle_0$ を要求する」も誤り（$\langle\Pi^2\rangle$ の上界は $`\|a(u)\psi_0\|^2`$ だけで書け `E05-P22` 5. で有限）。
   **禁止してよいのは「$\langle\Pi^2\rangle$ を $\langle N\rangle_0$ 経由で押さえる形」だけである。**
3. **「`E05-F24`/`F25` で $\mathcal P$ を表示する道は原理的に閉じている。回避策は無い」は射程を 1 時刻挿入型に限定する。**
   $\mathcal P\Omega=\Omega$ と $\mathcal Pe^{-tH_e}=e^{-tH_{-e}}\mathcal P$ から作用素恒等式として
   $\langle\psi_0,\mathcal P\psi_0\rangle=\lim_{t\to\infty}\langle\Omega,e^{-tH_e}e^{-tH_{-e}}\Omega\rangle/\langle\Omega,e^{-2tH_e}\Omega\rangle$（`E05-F22` の $\langle\Omega,\psi_0\rangle\ne0$、ギャップ不要）で、
   右辺は**結合定数の符号を半区間で反転した半群の積**であり挿入作用素を含まない。これが Markov 性で 1 本の経路積分に貼り合わさるかは**未確認**（原典読み許可外）で、監査人は成立を主張しない。
   **閉じたのは「$\mathcal P$ を 1 時刻の挿入作用素として入れる」道だけで、「結合符号の半区間反転として表示する」道の発注を止めてはならない。**
4. 到達点 1. の「標的と**同値**」は「標的の**必要条件**」に訂正（$2\epsilon_0\le\epsilon_2$ は片方向。`E05-P33` 6. は $\epsilon_N$ 条件を併記している）。

**【audit98 追記注記 → F64】（2026-09-13、同監査 (R4a)(R4b)。本文は改変しない）**
1. **(a) の結論（$\tilde K$ との比較から絶対定数 $\theta$ は出ない）は成立するが、障害 1. の理由文「$\langle A^2\rangle$ は変分量ではないので比較も単調性も使えない」は偽。**
   反例: $\eta\gt0$ で $H+\eta A(0)^2\ge\tilde K_\eta:=H_f+\eta A(0)^2$、$\psi_0$ を試行にして $E_{\tilde K}(\eta)\le E_0+\eta\langle A^2\rangle_0$、$E_{\tilde K}(\eta)=\int_0^\eta\langle A^2\rangle_{\tilde K_s}ds$ から
   ```math
   \frac{\langle A^2\rangle_0}S\ \ge\ \sup_{\mu\gt0}\frac1\mu\Bigl[\int_0^\mu F(\mu')d\mu'-\frac{8E_0}{3\Lambda}\Bigr],\qquad F(\mu)=\frac4\pi\int_0^\infty\frac{f\,dx}{1+\mu f}.
   ```
   比較と凹性だけで $\langle A^2\rangle_0$ の非自明な下界が出ており、(研究ノート: `193_audit98_FH_quasifree.py`)（seed 980913、PASS）で $E_0/\Lambda=0.01$〜$1000$ の全点で `E05-P36` 2. の $g(2E_0/\Lambda)$ を上回る（大 $E_0$ で定数 4 倍、$\Theta$ 不使用）。
2. **正しい閉鎖理由（厳密）**: $f(x)\le\frac1{3x^2}$（$\arctan y\ge y-y^3/3$）から全 $\mu$ で $F(\mu)\le\frac2{\sqrt3}\mu^{-1/2}$、ゆえに上の sup は $\le\frac\Lambda{2E_0}$。
   `E05-L4` の下界 $E_0\ge C_1\sqrt\alpha\Lambda^{3/2}m^{-1/2}$ で $\le\frac1{2C_1\sqrt{\alpha\lambda}}\to0$。**「$\tilde K$ 比較 + $E_0$」型は最良でも $S\Lambda/2E_0$ で絶対定数に届かない。**
3. **「$P_f^2\ge0$ を捨てる型の下界は全滅」「反跳を落とす近似はすべて先験的に無効」は族全体への過大な一般化（T84 (f)）。** 閉じたのは (i) $\tilde K$ の基底状態も満たす性質だけを使う議論、(ii) 上の比較 + $E_0$ 型、の 2 つ。
   反跳を捨てつつ $\psi_0$ 固有の入力（$\Theta$・$\mathcal K$・pull-through）を足す議論の発注を止めてはならない。
4. **(b)「$\Theta$ 経由の形の不等式は原理的に閉鎖」は条件付き閉鎖に格下げする。** (94.1) から絶対定数が出ないのは $\Theta/\Lambda\to\infty$ のときで、それは障害 3. 自身が認める T61 の見積り。
   `E05-L4` の下界は $\mathcal K/2m+\Theta$ の和にしか効かず $\Theta=O(\Lambda)$ は未排除。「道具が階数 3 を見ない」は道具の粗さであって閉鎖ではない（T84 (d)(e)）。
5. $\tilde K$ 漸近の中間式（稿 `94_` §3.3 の $\frac4\pi\cdot\frac2{\sqrt{3\mu}}$）は算術の誤記で、正しくは $\frac4\pi\cdot\frac\pi{2\sqrt{3\mu}}$。本項 1. の最終値 $\frac2{\sqrt3}\mu^{-1/2}$ は正しい。


## F71（「反跳を保持する対振幅の恒等式（`E05-P49`＝w187）＋ `E05-P32` 2. ＋ 在庫の $\mathcal K$・$\mathcal M$」で $`\|\rho_S\|_{op}`$ に `E05-P5` より良い上界を出す — 3 点項 C が光子数 $\mathcal M$ でしか押さえられず負ける。2026-09-13、w187、稿 `102_`）

格付け: `self-audited`（稿 `102_` §4・§6）。数値 (研究ノート: `190_w187_rhoS_oneloop_channels.py`)・`190b_w187_tree_pair_kernel.py`（ともに `PASS`、値と定数の検査のみ）。

**閉じた主張**: 恒等式 $(s+\frac{|q|^2}{2m})\kappa=A+B+C$ の 3 項を、木項は Schur、B は CS＋$\mathcal K\le\frac{\alpha\Lambda^2}\pi$、C は CS＋対消滅の HS 評価 $`\|F_\gamma\psi_0\|\le\|\gamma\|_2\mathcal M`$ で押さえ、`E05-P32` 2. で $`\|\rho_S\|_{op}`$ に戻して $\Lambda$ 一様（または $p\lt1$）の上界を得ること（発注 w187 (B)）。

**正確な障害**:
1. **C 項が律速で、在庫では `E05-P5` に負ける。** $`|C|\le\sqrt{t/2}\,\mathcal M`$、在庫 $\mathcal M\le2\max(\sqrt t,t)$ で $`\rho\le\frac{32\alpha}\pi+14.40\alpha^2\sqrt\lambda+5.66\,t\max(1,\sqrt t)`$。全 $\lambda$ で $\ge t$（`E05-P5`）。
   損は (a) $`\|F_\gamma\psi_0\|\le\|\gamma\|_2\mathcal M`$ が対の相関を見ず光子数だけで押さえること、(b) $\sqrt{\mathcal K}$ が真空の $A$ 揺らぎ（1 ループでも $\alpha\Lambda^2$ に飽和、`E05-P10`）であること。
2. **B 項は自己無撞着形で $p=\frac14$ の損を残す。** $`|B|\le1.90\,\alpha\lambda^{1/4}\sqrt\rho`$ ⟹ $`\rho\ni14.40\,\alpha^2\sqrt\lambda`$。損は $\langle\pi_\mu\psi_0,a(h_\mu)\psi_0\rangle$ の CS で $\sqrt{\mathcal K}$ を払う段。
   **⟹ C を $\Lambda$ 一様に押さえても $`\|\rho_S\|_{op}\lesssim\alpha+\alpha^2\sqrt\lambda`$（$p=\frac12$）止まりで、$\Lambda$ 一様にはならない。**

**再挑戦禁止の範囲（T60）**: 「恒等式 102-1 の この 3 分割 を、C は $\mathcal M$、B・C は $\sqrt{\mathcal K}$ で押さえる評価」だけ。

**生きている分岐**:
(i) C の 1 ループ値の測定 → **稿 `103_`（w188）で実施済**: 値 $\alpha^2\lambda^0$、$O(e^4)$ 係数に $\Lambda$ 一様な解析上界（audit99 が verifier-backed と判定）。(N102) は 1 ループでは殺せない。
(ii) B・C の $\sqrt{\mathcal K}$ を相関で置き換える評価（`100_` 命題 100-1 の CCR 変形のように $\langle\pi\cdot$ 場$\rangle_0$ 型へ移す）。
(iii) 恒等式の別分割（例: $\xi_q$ 項を左辺に残し $\langle\psi_0,(H(-q)-E_0+s)^{-1}\psi_0\rangle$ 型の対角 resolvent に移す。稿 `102_` では試算のみで、その形では $`\langle\xi_q,R\xi_q\rangle\le\|\xi_q\|^2/s`$ が $\alpha\lambda$ を払う）。

**⚠ 射程**: $`\|\rho_S\|_{op}`$ の $\Lambda$ 一様上界が偽だとは言っていない。1 ループ値は $\approx0.28\alpha^2$（$\lambda^0$、`F53` と独立再現が一致）。**木項は $\frac{8\alpha}\pi$ で $\Lambda$ 一様**（`E05-P49` 2.）であり、反跳の利得そのものは非摂動で取れている。
$h(\lambda)$ の datum を含まない。オッズは動かない（T49）。

**出所**: 稿 `102_rhoSの作用素ノルム.md` §4・§5、w187（2026-09-13）。

---


## F72（「`102_` 命題 102-1 の C 項 $C[f]=-\langle\xi_q,a(k)a(k')\psi_0\rangle$ を殻の光子数 $`\mathcal M=\|N_S\psi_0\|`$ を因子に持つ評価で $\Lambda$ 一様に押さえる」— $\mathcal M$ の 1 ループ値が $\alpha\lambda^{1/4}$ で増える。**1 ループ値による条件付き閉鎖**。2026-09-13、w188、稿 `103_` 判定 103-3。audit99 が射程と条件の向きを訂正）

格付け: `self-audited`（稿 `103_` §5・§7 R9）＋ **audit99 の逆転監査で結論は条件付きで成立、ラベルを「kill」から「条件付き閉鎖」に改め、条件の向きを訂正**（(研究ノート: `102_103_rhoS_audit99_2026-09-13.md`) K1）。**本項は (研究ノート: `w188.FAILED.md`) を置き換える。**

**閉じた主張**: $`|C[f]|\le c(\lambda)\,\mathcal M`$（θ-実 $f\in L^2(S)$、$`\|f\|=1`$）の形の評価から (N102)「$\sup_f|C[f]|\le C_*\alpha$、$C_*$ は $\Lambda$ 一様」を出すこと。`102_` 命題 102-3 の $c=\sqrt{t/2}$（$t=\alpha\lambda/\pi$）はこの型。

**正確な障害**:
1. **$\mathcal M$ の 1 ループ値が増える。** $\langle N_S\rangle\le\langle N_S^2\rangle$（$N^2\ge N$）と 1 ループの 2 光子支配で $\langle N_S^2\rangle\le2\langle N_S\rangle$、`F53` の $\langle N_S\rangle_0\simeq0.19\alpha^2\sqrt\lambda$ から $`0.44\,\alpha\lambda^{1/4}\lesssim\mathcal M\lesssim0.62\,\alpha\lambda^{1/4}`$（1 ループ値）。
   ⟹ **$c(\lambda)\lambda^{1/4}$ が $\lambda$ について有界でない限り**（$c=\lambda^0$、$c=\sqrt{t/2}$ を含む）、右辺 $c\mathcal M$ は $C_*\alpha$ の形にならない。
2. **量の側は生きている。** C の 1 ループ値は $\approx0.71\alpha^2$（E1 作用素ノルム、$\lambda=65536$）で $\lambda^0$、$O(e^4)$ 係数に $\Lambda$ 一様な解析上界 $\frac{1312}{\pi^2}\alpha^2$（w188 の `E05-P50`、audit99 が verifier-backed と判定）。在庫の損は $`\|F_\gamma\psi_0\|\le\|\gamma\|_2\mathcal M`$（対相関を見ない）と $\sqrt{\mathcal K}$ で、上界と値の差は $\alpha^{-1/2}\lambda^{3/4}$。

**証明の射程（T60・T84(e)(g)。audit99）**: 殺す材料は $\mathcal M$ の **1 ループ値だけ**で、**非摂動の $\mathcal M$ 下界は在庫に無い**。したがって示されたのは「展開 (iv′) の主要項が E05-L4 の有効域 $\lambda\lesssim\alpha^{-5/2}$ の中で $\mathcal M$ を与えるなら、その窓内で $`c\,\mathcal M/\alpha`$ が発散し、$|C|\le c\mathcal M$ 型から $C_*\alpha$ は出ない」まで。**固定 $\alpha$ で $\lambda\to\infty$ の「$\Lambda$ 一様上界が出ない」ことは示していない**（`F53` 障害 1 が同型の論法を「kill ではなく見込みの測定」と書いたのと同じ格）。

**再挑戦禁止の範囲**: 右辺が $\mathcal M$（または $\langle N_S^2\rangle^{1/2}$）を因子に持ち、係数 $c(\lambda)\lambda^{1/4}$ が非有界な評価で $C_*\alpha$ を狙うこと。**(N102) が偽だとは言っていない。** 非摂動の $\mathcal M$ の増大も主張しない。

**再挑戦してよい範囲**: 対相関を保つ評価。稿 `99_` 補題 99-3（`E05-P45`）で $\pi$ 側を $\sqrt{m/2}$ に替える経路は型として入り、残る欠落は **(N103)** $`\sum_\mu\|(H-E_0)^{1/2}F_\mu\psi_0\|^2\le Cm\alpha^2`$（稿 `103_` §6。1 ループ値は未計算で、非連結 2 光子項に $\alpha^2\sqrt\lambda$ 型の上界見積りがある＝未決）。
**audit99 が追加で閉じた型（1 手）**: 対の pull-through $a(k)a(k')\psi_0=-R_2[\cdots]\psi_0$、$R_2=(H(-q)-E_0+s)^{-1}$ に `E05-F23` の $`\|R_2\|\le1/s`$ を当てる型は反跳 $q^2/2m$ を失い木だけで $\frac{7\alpha\lambda}{12\pi}$（$p=1$）。$\langle\pi\rangle_0=0$ と Jensen から $\langle\psi_0,R_2\psi_0\rangle\ge(s+q^2/2m)^{-1}$ は出るが向きが逆で、上界には $H(-q)-E_0$ の定量的下界（`E05-F9`、窓外は $E(P)$ と同難度）を要する。**C 項は反跳を陽に出した代価であり、この型では避けられない。**

**出所**: 稿 `103_B項C項の1ループ値.md` §5、w188（2026-09-13）、audit99 K1・K4。

---


<!-- audit100（2026-09-13）: 本ファイルの (1) は (研究ノート: `w189.FAILED.md`) を、(2) は (研究ノート: `w190.FAILED.md`) を**置き換える**（あちらは連結しない）。F 番号は親が採番する。 -->

## F73（(1)「$R(k)$ を縦成分 $\hat k\cdot\pi$ 1 本の関数で押さえる majorant（＋2 次の摂動展開で $V_{\rm inv}$ の線形項を落とす）で (N-top) を示す」— $e=0$ で型の床が $\sqrt{mK}$。2026-09-13、w189、稿 `104_` §3・§6。audit100 が射程を限定）

**【親注記 2026-09-13】本群の (1)(2) ＝ `E05-P51`・`E05-P52`、FAILED の (1)(2) ＝ `F73`・`F74`。監査記録 (研究ノート: `104_105_audit100_2026-09-13.md`)（S0/S1、PATCH 適用済）。**

格付け: `self-audited`（稿 `104_` 命題 104-2・判定 104-5、worklog §5 D6・D7）＋ **audit100 の逆転監査で証明は成立、閉鎖の射程を「$e=0$ を含む $e$ について一様な型」に限定**（(研究ノート: `104_105_audit100_2026-09-13.md`) A2・A5）。数値 (研究ノート: `194_w189_longitudinal_majorant.py`)（`PASS`、値のみ）。

**閉じた主張**:
(a) 各 $k$ で $R(k)\le f_{\hat k,|k|}(\hat k\cdot\pi)$ となる関数 $f$ を、**$e=0$ でも成り立つ入力だけから**（または $e=0$ を含む $e$ について一様な定数で）作り、$\int_{\rm shell}c_k^2P_T\otimes f$ のノルムで $\tau_K\le Cm(\Lambda/K)^{1-\delta}$（最上殻で $Cm$）を出すこと。
(b) $X_k=X^0_k+\frac{k\cdot\pi}m$ の 2 次の resolvent 展開で、1 次項を $V_{\rm inv}$ で落とし剰余を $`\|R\|\le\frac1{|k|}`$ で押さえること。

**正確な障害**:
1. **(a)** $e=0$ で、1 光子セクタの同時スペクトル $`\{(q,|q|)\}`$ 上の a.e. 不等式から $f_{n,s}(p)\ge(s+|p|+\frac{(p+s)^2}{2m})^{-1}$ が強制され（横運動量 $q_\perp$ の sup）、$`\|\int c_k^2P_T\otimes f\|\ge\frac1{36\pi^2}\sqrt{\frac{2mK}7}\arctan\sqrt{\frac K{56m}}\sim2.36\times10^{-3}\sqrt{mK}`$。**$V_{\rm inv}$ 制限でも同じ下界**（audit100）。真の自由殻ノルムは $\le0.191m$。**損は横方向の位相空間を捨てた段に局在する**（縦成分に $|P_f|$ を 1 変数足すだけで $O(m)$ に落ちる。audit100）。型の中の最良値は `E05-P?`(1) 1. の $\frac1{2\pi}\sqrt{m\max(K,2E_0)}$（$e=0$ での $\sqrt{mK}$ の冪は改善不能、定数は 67 倍の余地）。
2. **(b)** 1 次項は厳密に 0 だが、$`\|\frac{k\cdot\pi}mX_0^{-1}W\|^2\le4\|W\|^2(1+\frac{2mE_0}{k^2})`$ で剰余 $`\le\frac4{|k|}\|W\|^2`$＝自明評価より悪い。危険なベクトル（$\pi\approx-k$）で展開の比が 1 を切らない。

**再挑戦禁止の範囲（T60。証明が実際に排除した分岐のみ）**: (a) **$e=0$ でも成り立つ入力だけから作る、または $e=0$ を含む $e$ について一様な定数で上界を与える**縦成分 1 本の majorant。(b) $`\|R(k)\|\le\frac1{|k|}`$ を剰余に使う 2 次展開（反復を含む）。
**(N-top) を反証するものではない。** 次は生きている（audit100）: $e\gt0$ 固有の入力で $f$ を作る majorant、**同じ $f$ でも $e\gt0$ の $`\|\int d^2n\,P_T(n)\otimes f(\pi_n)\|`$ を $\pi_n$ の方向間非可換性（$[\pi_i,\pi_j]=ie\epsilon_{ijl}B_l$）で方向ごとの sup より良く押さえる評価**（$e\to0$ からはノルムの下半連続性しか出ず、固定 $\alpha$ で $\Lambda$ 一様な床は従わない）、横成分 $\pi_\perp$ を保持する評価、$E_0$ 部分を $\mathcal K/3s$ 級に落とす同型の改良（未決）。

**生きている分岐**: (i) 横被覆 $b_K$（`104_` 命題 104-3）の PF 固有評価——$b_K\lesssim\sqrt mK^{3/2}(\Lambda/K)^{1-\delta}$ で (N-top)。交換子 $[\pi_2,\pi_3]=\pm ie(\mathrm{curl}A)_1$ が作用素値の場合の磁場つき Lieb–Thirring/CLR 型数え上げ。(ii) Landau 型の歯止めは場の大きさ（`E05-P32` 2. の rms 上界は閾値 $\sqrt mK^{3/2}$ を越えうる）ではなく $E_0$ の大きさ: 窓内で $e|\langle B_n\rangle|\le2m(E_0+\Gamma)$ なので、期待値で測る Landau 機構は $E_0\lesssim\frac{\Lambda^{3/2}}{2\sqrt m}$ なら最上殻で働かない（発見法。真空変分枝で $\lambda\lesssim(\pi/\alpha)^2$）。

**出所**: 稿 `104_N-topとPF固有構造.md` §3・§5・§6、worklog (研究ノート: `2026-09-13_w189_Ntop.md`) §3・§5、w189（2026-09-13）、audit100（A2・A5）。

---

## F74（(2) `E05-P41` の Weyl 共役を 2 本の消滅 $F_\mu$ に延ばし、$Y\le$ 二重交換子で (N103) を示す — 対生成の c 数 $\alpha^0$ で次数が届かない。2026-09-13、w190、稿 `105_` §5。audit100 が射程を限定）

**【親注記 2026-09-13】本群の (1)(2) ＝ `E05-P51`・`E05-P52`、FAILED の (1)(2) ＝ `F73`・`F74`。監査記録 (研究ノート: `104_105_audit100_2026-09-13.md`)（S0/S1、PATCH 適用済）。**

格付け: `self-audited`（稿 `105_` 判定 105-4、worklog §5 R11）＋ **audit100 の逆転監査で結論は成立、再挑戦禁止の範囲を狭める**（(研究ノート: `104_105_audit100_2026-09-13.md`) B4）。

- **閉じた主張**: $`Y(f)=\sum_\mu\|(H-E_0)^{1/2}F_\mu\psi_0\|^2\le\sum_\mu\langle[F^*_\mu,[H,F_\mu]]\rangle_0`$（$F^*$ 項を $\ge0$ として捨てる）、または生成子 $F+F^*$・$i(F-F^*)$ の Weyl 共役の $q_{E_0}\ge0$ の $s^2$ 係数で $Y\le Cm\alpha^2$（$\Lambda$ 一様）を出すこと。
- **正確な障害**: 固有状態で $`\langle[F^*_\mu,[H,F_\mu]]\rangle_0=Y_\mu+\|(H-E_0)^{1/2}F^*_\mu\psi_0\|^2`$。第 2 項の最低次は対生成 c 数 $`\|H_0^{1/2}F_\mu^*\Omega\|^2`$ で、和は $2\iint|ff'|^2q^2g\le4m$、E1 の $u$ 型では $q^2g\to2m$ が大部分なので下からも $O(m)$（**$\alpha^0$**）。Weyl 型は 2 つの自己共役生成子の $s^2$ 係数の和が二重交換子の 2 倍になり c 数を避けられない。損は (N103) の標的 $Cm\alpha^2$ に対し $\alpha^{-2}$、1 ループ値 $Y\approx0.14\alpha^3m$（稿 `105_` 判定 105-2、値）に対し $\alpha^{-3}$。
- **再挑戦禁止の範囲（T60）**: **$F^*$ 項を非負として捨てて二重交換子全体を $Y$ の上界に使う評価、および $F\pm F^*$ 型の Weyl 共役で、$\alpha^2$ を狙う発注だけ**。次は禁じない（audit100）: (a) $\alpha$ を捨てて $\Lambda$ 一様だけを取る使い方（作用素項が一様なら $|C[f]|\lesssim\sqrt6$、未検査）、(b) **非対称形** $Y_\mu=\langle F_\mu\psi_0,[H,F_\mu]\psi_0\rangle$（$(H-E_0)\psi_0=0$ から恒等的で c 数を含まない）や $F^*$ を含まない片側の変分・対相関を見る $`\|F_q\psi_0\|`$ の評価、(c) **$F^*$ 項を捨てずに真空値を引き去る形** $`Y=\langle[F^*,[H,F]]\rangle_0-\|(H-E_0)^{1/2}F^*\psi_0\|^2`$ に第 2 項の下界を付ける評価（在庫ゼロ、見込みは薄い）、(d) 窓に集中する $f$ での別の評価。
- **kill-check の記録（不発）**: 同稿で「(N103) の 1 ループ値に $\alpha^4\lambda$ 型が入り 99-3（`E05-P45`）経路が有効域内で死ぬ」疑い（`103_` §6、上界の見積り）を E1・M1 の値で検査し、2 光子対角が $\alpha^4\lambda^{\le0.15}$・比 5% で**窓は開かず kill は発動しなかった**（**E1・M1 の $u$ 型・$e^8$ 対角に限る**。$\sup_f$ と $e^8$ 交差項は未検査なので、経路が $\sup_f$ で 1 ループ生存するとは言っていない）。
- **出所**: 稿 `105_N103の1ループ値.md` §4・§5、w190（2026-09-13）、audit100（B3・B4）。



<!-- audit101（2026-09-13）: 本ファイルの (1) は (研究ノート: `w192.FAILED.md`) を、(2) は (研究ノート: `w191.FAILED.md`) を**置き換える**（あちらは連結しない）。親は (1)(2) の順に F 番号を採番すること。 -->

## F75（(1)「`102_` の B 項 $B[f]=-\frac{2e}m\sum_\mu\langle\pi_\mu\psi_0,a(h_\mu)\psi_0\rangle$ の $\lambda^{1/4}$ を、$\pi$ 側を `E05-P45` の双対評価に替え場側を 1 本消滅の二重交換子で押さえることで除く」— 二重交換子が生成側の c 数を拾って $\lambda^{1/4}$ を払う。2026-09-13、w192、稿 `107_` 判定 107-0。audit101 が障害の所在を訂正）

**【親注記 2026-09-13】audit101（(研究ノート: `106_107_audit101_2026-09-13.md`)）。FAILED の (1)(2) ＝ `F75`・`F76`。**

格付け: `self-audited`（稿 `107_` §2・§5）→ audit101（(研究ノート: `106_107_audit101_2026-09-13.md`) M4）が上界の冪を再計算して成立、**障害の帰属を訂正**。上界の冪勘定による型の閉鎖。

**閉じた主張**: w192 発注 (A)「二重交換子の作用素項の道が B 側にも効くか」。B 版は $`|\langle\pi_\mu\psi_0,a(h_\mu)\psi_0\rangle|\le\sqrt{m/2}\|(H-E_0)^{1/2}a(h_\mu)\psi_0\|`$ と
$`\|(H-E_0)^{1/2}a(h)\psi_0\|^2\le\langle[a^*(h),[H,a(h)]]\rangle_0=\langle h,\omega h\rangle+\frac1{2m}\sum_\mu(\|k_\mu h\|^2+2\|a(k_\mu h)\psi_0\|^2)+\frac{e^2}m\sum_\mu|\langle h,u_\mu\rangle|^2`$。

**正確な障害**:
1. 組み立てると $`|B[f]|\le\sqrt{6\sqrt2\,\alpha}\,\lambda^{1/4}\sqrt{(1+\frac2\lambda)(1+2\rho+\frac{3\alpha}{2\pi})}`$、系 102-4 で $`\rho\ni68\,\alpha\sqrt\lambda`$。**$\lambda$ 冪は `E05-P49` 3. と同じで $\alpha$ の次数は悪化。**
2. **$\lambda^{1/4}$ の所在は二重交換子の段**: $`\langle[a^*,[H,a]]\rangle_0=\|(H-E_0)^{1/2}a(h)\psi_0\|^2+\|(H-E_0)^{1/2}a^*(h)\psi_0\|^2`$ で、右辺第 2 項の c 数部 $`\langle h,\omega h\rangle+\|kh\|^2/2m\sim\frac{\Lambda^2}m\|h\|^2`$（$\psi_0$ にも $e$ にも依らない）が、$`\sup_f\sum_\mu\|h_\mu\|^2\sim\lambda^{-3/2}`$（反対心 2 球帽に集中した $f$）と組んで $\lambda^{1/4}$ を与える。**CS（P45）の段ではない**: 同じ飽和族で第 2 因子に 1 ループの真の値 $`\|(H-E_0)^{1/2}a(h)\psi_0\|^2\sim e^4\lambda^{-1/2}`$ を入れると $|B|\lesssim|e|^3\lambda^{-1/4}$、`102_` の $\sqrt{\mathcal K}$ 版も真の $`\|a(h)\psi_0\|^2\sim e^4\lambda^{-5/2}`$ で同じ $\lambda^{-1/4}$（1 ループ冪勘定。`102_` の損は $`\|a(h)\psi_0\|^2\le\rho\|h\|^2`$ の段）。$\Lambda$ 固定でも $e\to0$ で $a(h)\psi_0=O(e^2)$ に対し c 数部は $O(1)$ なので、損がこの段にあることは確定。
3. 2 本消滅の二重交換子（発注の本体）は C 項にしか現れず B に作用しない。

**再挑戦禁止の範囲（T60）**: 「$\langle\pi_\mu\psi_0,a(h_\mu)\psi_0\rangle$ を CS で切り離し、**場側を $\psi_0$ に依らない量（$`\rho\|h\|^2`$ または 1 本消滅の二重交換子）で押さえる**」型の B 評価だけ。**CS による切り離し一般は閉じていない**（第 2 因子を pull-through 等で $\psi_0$ に即して評価する CS 型は 1 ループ冪勘定では $\lambda^{1/4}$ を払わない）。

**生きている分岐**: 1 本の pull-through で B を木核 × $M_\perp/m$ に厳密に因数分解する経路（(研究ノート: `audit101.PROVED.md`) (1)＝稿 `107_` 命題 107-1）。Schur 型の十分条件は (N-B⊥) $\sup_{r\in S}M_\perp(r)\le\mu_*m$（必要条件ではない。在庫は $c_k^2$ 重み平均 $\le m$＝`E05-P46` のみ）。

**⚠ 射程**: 上界の冪で、B の値ではない。B の $O(e^4)$ 係数は `E05-P50` で $\Lambda$ 一様。B の $\Lambda$ 一様上界が偽だとは言っていない。第 2 段の冪比較は展開 (iv′) の 1 ループ冪勘定（T61）で非摂動の主張ではない。C 側（本発注 (B)）は検査していない（発注規則で未実施）。$h(\lambda)$ の datum を含まない。オッズは動かない（T49）。

**出所**: 稿 `107_二重交換子の作用素項.md` §2、w192（2026-09-13）。監査 (研究ノート: `106_107_audit101_2026-09-13.md`) M4。

---

## F76（(2) kill-check 不発動: (N103) の $\sup_f$ 側を窓集中 $f$ と $e^8$ の安い交差項で殺す — 測った族・測った項の 1 ループ値で窓は開かない。w191、2026-09-13、稿 `106_`。audit101 が射程の文言と比の値を訂正）

**【親注記 2026-09-13】audit101（(研究ノート: `106_107_audit101_2026-09-13.md`)）。FAILED の (1)(2) ＝ `F75`・`F76`。**

**閉じた主張**: 「`105_` の経路（`E05-P45` で C を $\sqrt{3Y/2m}$ に押さえる）は、窓に集中する $f$ か $e^8$ 交差項で 1 ループの $Y$ が $\lambda^{p\gt0}$ に伸びて有効域 $\lambda\le\alpha^{-5/2}$ 内で `E05-P50` の在庫 $132.9\alpha^2$ を超え、死ぬ」。

**正確な障害（値）**: 反対心 2 帽子（$\delta=\lambda^{-1/2}$）の族 A と動径の帯 $\sqrt{m\Lambda}$ を足した族 A′（$`\|\gamma\|_2^2\sim m/\Lambda`$ を実現、$`\lambda\|\gamma\|^2=0.0924`$）で、$y_6$ は減少し A′ で $\propto\lambda^{-1}$（局所冪 $-0.96,-1.01$。A は $-0.79,-0.97$ で未収束）、$y_8^{\rm diag}$ は全段単調に減少（冪 $-0.45\pm0.2$）、値は滑らかな E1 の $10^{-3.4}$〜$10^{-8.8}$。滑らかな E1 の $`X_{V1}=-0.35\,y_8^{\rm diag}`$・$`X_{V2}=+0.19\,y_8^{\rm diag}`$（$\lambda=65536$）はともに $\lambda^0$。**最大/水準は帽子族と交差項で $\le2.6\times10^{-5}$、半球検証と滑らかな E1 の $y_6$ を含めて $\le1.6\times10^{-3}$**（測定範囲は $y_6$ が $\lambda\le262144\approx1.19\alpha^{-5/2}$、$X_{V1},X_{V2}$ は $\le65536$ からの外挿）。機構（次元勘定、証明ではない）: $\phi=\iint\gamma\Psi_3$ は支持測度の縮小と $(k,k')\to(-k',-k)$ の奇部相殺で下がり、$\beta$ の Coulomb 型核は局在関数に $\alpha\lambda^{-1/2}$ しか与えない。数値 (研究ノート: `198_w191_*`)（PASS）。$e^8$ 係数の 4 項分解は (研究ノート: `w191.PROVED.md`)（audit101 N3 で成立）。

**⚠ 再挑戦禁止の範囲（T60）**: **測った族（A: $c=1,4$、A′: $c=c_r=1$、E1 の $j=\perp,z$）と測った項（$y_6$、$y_8^{\rm diag}$、$X_{V1}$、$X_{V2}$）での 1 ループ kill だけ**。次は閉じていない: (1) **$X_{H0}=2\mathrm{Re}\langle\phi^{(3)},H_0\phi^{(5)}\rangle$ の連続体の値**（未測。有限模型 ED では負で対角部の 20〜84%）、(2) 滑らか＋窓の混合 $f$ など他の $f$ の族（$Y$ は $f$ の 4 次で、全 $f$ の $\sup$ は未測）、(3) (N103) の非摂動上界（在庫ゼロのまま）。有効域 $\lambda\gt\alpha^{-5/2}$ については何も言わない（E05-L4）。kill 不発動は (N103) の証明ではなく、オッズは動かない（T49）。

**出所**: 稿 `106_N103のsupf側.md` §3〜§5、w191（2026-09-13）。監査 (研究ノート: `106_107_audit101_2026-09-13.md`) N1〜N5。

---


<!-- audit102（2026-09-13）: 本ファイルの (1) は (研究ノート: `w193.FAILED.md`) を**置き換える**（あちらは連結しない）。F 番号は親が採番。 -->

## F77（(1)「和則の平均（`E05-P53` の $\int c_k^2M_\perp\le\frac m2S_0$）から $M_\perp$ の殻上 sup (N-B⊥) へ移る」— (a) 回転不変性では構造的に空、(b) 動径 $L^2$ ＋ 動径の対数 Lipschitz 評価では型の床 $m\lambda^{1/4}$、(c) 球作用素のベクトル一様版は $e=0$ で $\ln\lambda$。2026-09-13、w193、稿 `108_` §3・§5。audit102 が床の試行関数を修正）

**【親注記 2026-09-13】本群の (1)(2) ＝ `E05-P55`・`E05-P56`、FAILED の (1) ＝ `F77`。監査記録 (研究ノート: `108_B項一様上界_audit102_2026-09-13.md`)（S0、PATCH 適用済）。⚠ audit102 (R6′): C の一様有界性は ρ_S の作用素ノルムの一様有界性と同値（言い換え、T89）。**

**【親注記 2026-09-13】audit102（(研究ノート: `108_B項一様上界_audit102_2026-09-13.md`) R5a・R5b）。PROVED の対応項 ＝ (研究ノート: `audit102.PROVED.md`) (2)。**

格付け: `self-audited`（稿 `108_` 108-2・108-4、w193）→ audit102 が再導出して成立。(b) の試行関数に不備（下記 2.）があり修正版で結論不変。数値 (研究ノート: `201_w193_Mperp_sup_oneloop.py`)（PASS、値のみ）。

**閉じた主張**: `E05-P53` の Schur 型十分条件 (N-B⊥) $\sup_{r\in S}M_\perp(r)\le\mu_*m$ を、(a) 回転不変性（`E05-P47` 1.）で平均から点値へ移して示すこと；(b) 動径プロファイル付き和則の $L^2$ 評価 $\int_0^\Lambda rM_\perp^2\le2m^2\Lambda^2$、$L^1$ 評価、$M_\perp\ge0$、動径微分評価 $|M_\perp'|\le\varphi M_\perp$（$\varphi(r)=\frac1r+\sqrt{2(r+E_0)/mr^2}$、$\varphi(\Lambda/2)=c_S=\frac2\Lambda+\sqrt{(4\Lambda+8E_0)/m\Lambda^2}$）だけから示すこと；(c) $M_\perp(r)\le\frac12\sigma(r)\mathcal K$（$\sigma$＝球作用素 $T^{(r)}$ の $V_{\rm inv}$ ノルム）に $e=0$ を含め一様な $\sigma$ の上界を入れて示すこと。

**正確な障害**:
1. **(a)** $M_\perp(r)$ は既に $SO(3)$ スカラーで $|k|$ だけの関数。回転は $|k|$ を混ぜない。
2. **(b)** 入力集合は $M(r)=H\exp(-|\Phi(r)-\Phi(\Lambda/2)|)$（$\Phi'=\varphi$、$(0,\Lambda]$ 上）で $H\approx m\sqrt{2\Lambda c_S}$ を許す（$\int_0^\Lambda rM^2\le0.96\Lambda H^2/c_S$、$L^1$ は $\Lambda c_S\gtrsim32$ で可）。$\Lambda c_S\ge2\sqrt\lambda$ なので最良 $\gtrsim m(4\lambda)^{1/4}$。実際に得られる上界は $`\sup_SM_\perp\le2\mathrm e\,m(2+2\sqrt{\lambda+2E_0/m})^{1/2}`$ で床と定数 $O(1)$ 倍以内。損の出所は動径の共鳴幅 $\sqrt{m\Lambda}$。**稿の試行 $He^{-c_S|r-r_0|}$ は $r\gt\Lambda/2$ で実入力 $\varphi(r)\lt c_S$ を破り $S$ の外で未定義だった（audit102 R5b）。**
3. **(c)** $e=0$ の 1 光子 $V_{\rm inv}$ ベクトルを $|q|=r$ に集中させると $r^2\sigma_{\rm free}(r)\ge\frac m2[(1+a)\ln(1+\frac1a)-1]$（$a=2m/r$）。共鳴 $|q|=r$ の近対蹠角で $\ln$。数値の比 $r^2\sigma_{\rm free}/(m\ln r)=0.43\to0.46$（$r=16\to2^{20}$、増加中。床から $\liminf\ge\frac12$）。

**再挑戦禁止の範囲（T60。証明が実際に排除した分岐のみ）**: (a) 回転不変性だけによる平均→sup；(b) 上の 4 入力（$L^2$・$L^1$・正値性・$\varphi$ 級の対数 Lipschitz）だけによる sup；(c) $e$ 一様な球作用素ノルムと $\mathcal K$ の積による sup。
**(N-B⊥) を反証するものではない**（1 ループでは $\sup_SM_\perp\to0.826\alpha m$、sup/平均 1.44、単調減少）。生きている分岐: $\pi\psi_0$ 固有の動径正則性 (Mon′) $M_\perp(r)\le C_mM_\perp(r')$（$\Lambda/4\le r'\le r\le\Lambda$、$\mu_*=\frac{16}3C_m$）、(N-reg) $\Lambda|\partial_r\ln M_\perp|\le C_r$、および入力集合の外の情報（2 階微分・凸性など）。
**⚠ 重要度の注記**: **B 項には (N-B⊥) が不要になった**（(研究ノート: `audit102.PROVED.md`) (1) 3.、殻上 $L^2$ で $|B|\le10.48\alpha$）。したがって本項は「B 側の障害」ではなく、$\sup M_\perp$ という量そのものの評価の型の記録である。本項を理由に B 側・$`\|\rho_S\|_{op}`$ 側の発注を止めてはならない。

**出所**: 稿 `108_横成分リゾルベントの殻上sup.md` §3・§5、w193（2026-09-13）。監査 (研究ノート: `108_B項一様上界_audit102_2026-09-13.md`) R5a・R5b。

---


<!-- audit103（2026-09-13）: 本ファイルの (1) は (研究ノート: `w194.FAILED.md`) を**置き換える**（あちらは連結しない）。F 番号は親が採番する。 -->

## F78（(1)「`108_` 命題 108-7 と同型の論法を C 項に当てて $\Lambda$ 一様上界を出す」— C の主部 $C_T=T\mu$ の Schur 量 $I_\mu$ は $\nu_q$ の位置・モーメント型の入力では押さえられない（Landau 玩具、`E05-L4` 窓の変種を含む）。$C_\gamma$ の CS 型は 1 ループで冪を失う。2026-09-13、w194、稿 `109_` §4・§5。audit103 が射程を拡大・理由文と損の所在を訂正）

**【親注記 2026-09-13】(1) ＝ `E05-P57`、FAILED (1) ＝ `F78`。監査記録 (研究ノート: `109_C項_audit103_2026-09-13.md`)（S0/S1、PATCH 適用済）。**

格付け: `self-audited`（稿 `109_` 判定 109-4・109-5・109-8）＋ **audit103 の逆転監査で玩具床を再計算して成立、閉鎖の射程は稿より広い（F9・L4 上界を含む）、光子入力部分は閉鎖から外す**（(研究ノート: `109_C項_audit103_2026-09-13.md`) R3・R4・R5）。**本項は (研究ノート: `w194.FAILED.md`) を置き換える。**

**閉じた主張**: w194 発注 (A)(B)「C 項に 108-7 型の論法が入るか」のうち、下の「再挑戦禁止の範囲」に書いた型。

**正確な障害**:
1. **型の半分は入る**: 2 本目の pull-through で $C=T\mu(|q|,s)+C_\gamma$（PROVED の対応項 1.）。$\mu\ge0$ は $s$ 非増加なので Schur は 1 変数の重み付き $L^1$ $`I_\mu=\int_{|q|\le2\Lambda}\mu g\,d^3q`$ だけを要し、球面トレースも sup も要らない（1 ループの $\sup_q\mu\approx0.37\alpha\ln\lambda$ は増えるが $I_\mu$ は飽和、(研究ノート: `203_w194_*`)、独立再実装 `204_audit103_*`）。
2. **在庫の位置・モーメント入力では $p=1$**: 拘束は $\nu_q$ の平均 $a$・分散 $\frac{|q|^2\mathcal K}{3m^2}$・台 $\ge0$。最良は $\mu\le\min(\frac as,\frac{g|q|^2\mathcal K}{3m^2s})$（分散込みでも定数 $\frac{a^2}{a^2+V}$ の範囲で鋭い）で $|C_T|\le\frac{16}{3\pi^2}\alpha^2\lambda$。
3. **型の床（玩具）**: `F70` の直積分磁場（最低 Landau 準位 ⊗ 縦幅 $\to\infty$）で $\nu_q=\sum_n\mathrm{Poi}(n;\frac{a_\perp}{\omega_c})\delta_{n\omega_c+a_\parallel}$（厳密）。$n=0$ 項だけで $\frac{I_\mu}{m\Lambda}\ge\frac{\pi\sqrt2}{16\mathrm e}\frac{Q'^2-4m\Lambda}{m^{1/2}\Lambda^{3/2}}$、$Q'=\min(\sqrt{2m\omega_c},2\Lambda)$。
   (i) $\mathcal K=m\omega_c=\frac{\alpha\Lambda^2}\pi$ で $\ge\frac{\sqrt2}{8\mathrm e}\alpha\sqrt\lambda-\frac{\pi\sqrt2}{4\mathrm e}\lambda^{-1/2}$（数値 $\alpha=1/137$ で $0.51\to6.69$、$\lambda=256\to16384$）。
   (ii) **audit103**: $\omega_c=2\theta C_2\alpha^{2/7}\Lambda^{12/7}m^{-5/7}$（$\theta\lt1$）は大 $\lambda$ で `E05-L4` の窓の内・$\mathcal K\le\frac{\alpha\Lambda^2}\pi$・$\omega_c\ge2\Lambda$ を満たし、$\frac{I_\mu}{m\Lambda}\gtrsim\theta C_2\alpha^{2/7}\lambda^{3/14}\to\infty$。歯止めは $E_0\lesssim\Lambda^{3/2}m^{-1/2}$（L4 下界の枝）のときだけで床は $\lambda^0$。
   (iii) 床の帯は $2\sqrt{m\Lambda}\le|q|\le\sqrt{2m\omega_c}\lt\Lambda$ にあり、`E05-F9`（$|P|\ge\Lambda$）に触れない。`E05-F20` の天井で PF でも $E(q)-E_0\le|q|\ll a/2$ なので、**スペクトルの位置（分散）の情報では低エネルギー重みの位置は $x\lesssim\Lambda$ に留まり床は消えない**（見立て、非平坦な玩具は 2 次性を壊すので未構成）。
   (iv) 床の帯では $k'\simeq-k$ で偏極因子が正なので、Schur の優関数だけでなく $C_T$ の作用素ノルムにも同じ冪の床が立つ（見立て）。
4. **$C_\gamma$ の CS 型**: $|C_\gamma g|\le\kappa\cdot2\sqrt{\mu(\Lambda+a)/\Lambda}\sqrt{1+E_0/\Lambda}(\sqrt{M_\perp/m}+\sqrt{M'_\perp/m})$ は 1 ループ冪勘定で上界 $\sim\alpha^2\sqrt\lambda\sqrt{1+E_0/\Lambda}$（値 $0.065\alpha^2\lambda^0$）。**損の所在（audit103 訂正）**: (i) $`\|w_k\|^2\le M_\perp/|k|`$（$R(k)^2\le R(k)/|k|$、1 光子側の反跳を捨てる段。数値 204 で比 $\propto\lambda^{-1/2}$）、(ii) CS の支持不一致（$\xi_q$ は一般の $p$、$w_k$ は近対蹠窓）、(iii) $E_0/s$。**稿の「1 光子側に $R_2\le\frac1s$」はこの評価に存在しない。**

**再挑戦禁止の範囲（T60。証明が実際に排除した分岐のみ）**:
(a) $C_T$ を単独で（$C_\gamma$ との相殺を使わず）、$\mu$ または $I_\mu$（$G_\Lambda$）を {`F23` 型の下界、`E05-P45`、$\langle\pi\rangle_0=0$、回転共変、2 次性、$\mathcal K$ の上界、`E05-L4` の $E_0$ 窓、`E05-F20`、`E05-F9`、$\nu_q$ の 0〜2 次モーメントと台} **だけ**から $\Lambda$ 一様に押さえること（玩具 3.(i)(ii) が破る）。
(b) $C_\gamma$ を上の 4. の CS 分割（$`\|w_k\|^2\le M_\perp/|k|`$ と $(\pi+q)^2\le2m(1+E_0/s)R_2^{-1}$）で押さえること（1 ループで冪を失う。上界の冪であって $C_\gamma$ の値の主張ではない）。
**w194 原案の (b)「108-3 型の光子和則を $\mu$ に直接当てること（$\mu$ は光子線を持たない）」は再挑戦禁止に入れない**（audit103 R3(c)）: $\kappa$ 自身が $\mu$ を線形に含む光子期待値であり、「在庫の光子入力（`E05-P32` 2.・`E05-P41`）は $\kappa$ に片側の評価しか与えず、両側は $\rho$ 経由（`E05-P40`・`E05-P55` 4.）」は機構判定で証明ではない。

**C・$`\|\rho_S\|_{op}`$ の一様上界が偽だとは言っていない。** 生きている分岐: (N109) $I_\mu\le Cm\Lambda$ を**重み（重なり）の情報**で示すこと——PF 固有の光子構造（$`q\cdot\pi\psi_0\simeq e\,q\cdot A\psi_0`$ が $H(-q)$ の低エネルギー状態＝運動量 $-q$ を光子が運ぶ状態に当たる振幅の横波性による抑制、`E05-F7` の総運動量構造）、光子場の命題（`E05-P32`・`P39`・`P41`・`P55` 1.）を $\rho$ に戻さずに使う評価；$C_T$ と $C_\gamma$ を合わせて（相殺込みで）押さえる評価；1 光子側の $R(k)$ にも反跳を保つ $C_\gamma$ の評価。**$E(P)$ の下界（分散型）だけを狙う設計は (a) に入り (N109) に届かない。**

**⚠ 射程**: 同値性（`E05-P55` 4.、T89）により C の一様上界は $`\|\rho_S\|_{op}`$ のそれと同値で、C を $\kappa$・$\rho$ 経由で押さえる経路は循環（本項はそれを使っていない）。玩具は PF ではなく、光子場の命題は玩具で**未定義**（満たすのではない）。(N109) は Q3 の $h$ とも `E05-F9` とも両向きの含意を持たない（audit103 R5）。数値は 1 ループの値・上界と玩具の値（T61・T88）。$h(\lambda)$ の datum を含まない。オッズは動かない（T49）。

**出所**: 稿 `109_C項の和則L2型.md` §3〜§5、w194（2026-09-13）。監査 (研究ノート: `109_C項_audit103_2026-09-13.md`) R3・R4・R5、(研究ノート: `204_audit103_Imu_oneloop_reimpl.py`)。

---

## F79（「(N109) の低帯重みを $\pi\cdot\hat q$ の分布の裾（$\mathrm{Prob}_{\psi_0}(|\pi\cdot\hat q|\ge|q|/2)$）で押さえ、それを在庫の光子入力で押さえる」— 最良ケースでも $p=1$、かつ Landau 玩具が同じ入力を満たす。2026-09-13、w195、稿 `110_` §6）

**【2026-09-13】audit104 の PATCH 適用済（「在庫を改善しない」は偽。`E05-P59` を見よ）。**

格付け: `self-audited`（稿 `110_` 判定 110-4、敵対的セルフレビューは同 §8 R7）。数値は (研究ノート: `205_w195_mu_low_band.py`)（PASS、seed 1950913）。

**閉じた主張**: 発注 w195 §1 の鎖（(P-chain)）——
(1) $\mu_{\rm low}\le\frac as\nu_q([0,a/2))$、(2) $`\nu_q([0,a/2))\le C\,P(q)`$、$P(q)=\mathrm{Prob}_{\psi_0}(|\pi\cdot\hat q|\ge|q|/2)$、
(3) $P$ を在庫の光子入力（`E05-P32` 3. の $\mathcal K\le\frac{\alpha\Lambda^2}\pi$、`E05-P39` の sub-Gauss、`E05-P5` の $`\|P_f\psi_0\|`$）で押さえる
——により (N109)（$I_\mu\le Cm\Lambda$）を出すこと。

**正確な障害**:
1. **冪（最良ケースでも $p=1$）**: $\pi\cdot\hat q$ がちょうど分散 $\mathcal K/3$ の Gauss で $\mathcal K$ が在庫上限を飽和するとしても、帯 $\sqrt{2m\Lambda}\le|q|\lesssim\sqrt{\mathcal K}=\sqrt{\alpha/\pi}\Lambda$ で $P=O(1)$・$\frac as\ge1$ となり
   $\frac{I_\mu^{\rm chain}}{m\Lambda}\gtrsim\frac{4\pi}3(\frac\alpha\pi)^{3/2}\lambda$。数値（$\alpha=1/137$）: $0.121,0.809,4.12,18.1,74.6$（$\lambda=256\to65536$、$\lambda$ 4 倍で 4.1 倍＝厳密に線形）。**⚠【audit104 R4-a】この $p=1$ は $\mathcal K$ の上界に `E05-P32` 3. の右端 $\frac{\alpha\Lambda^2}\pi$ を使った場合に限る。同項の中央 $\mathcal K\le2mE_0$ に `E05-L4` を入れると鎖は $p=4/7$、在庫評価そのものは $p=5/7$ に下がる（(研究ノート: `audit104.PROVED.md`)）。閉鎖の理由は「在庫を改善しない」ではなく「$p\gt0$ のままで (N109) に届かない」である。**
2. **玩具が同じ入力を満たす**: `F70`・`F78` の Landau 玩具は $\pi_\perp$ が最低 Landau 準位の 2 つの求積で、$\pi\cdot\hat q$ は分散 $\mathcal K/2$ の Gauss、低帯重みは $\mathrm e^{-q^2/(2\mathcal K)}$ と**同型**（しきい値 $|q|=\sqrt{\mathcal K}$ で重み $0.607$ vs Gauss 裾 $0.480$ なので (2) は literal には玩具で偽、定数込みでも鎖の上界は床と矛盾しない: $\lambda=16384$ で鎖 $33.6$、床 $0.058$）。**⟹ 鎖は光子入力を実質使っておらず `F78` の再挑戦禁止範囲 (a) と同型。**
3. **`E05-P45` 経由の変種**（$X_q+s\ge c(H-E_0)$ 型の作用素比較で P45 に帰着する道）も同じ理由で閉じる（玩具は P45 を満たす。稿 `109_` §6 R8 の再確認）。
4. **横波性は 1 ループの効き所ではない**（親の見立ての否定側、**値**の判定。T88）: 偏極因子 $1-x^2$ を角度平均 $\frac23$ に置換しても低帯寄与は $4.2\sim5.1$ 倍になるだけで $\lambda$ 冪は不変、横波性が冪で効く深帯（$x\lt\Lambda$）の寄与は $\propto\lambda^{-1/2}$（$0.056\to0.0097$、$\lambda=256\to16384$）。$\mu_{\rm low}$ の 1 ループでの小ささは分解能の分母にある電子反跳 $|p+q|^2/2m$ から来る。

**再挑戦禁止の範囲（T60。証明が実際に排除した分岐のみ）**: 低帯重み $\nu_q([0,a/2))$（または $\mu_{\rm low}$）を、**$\pi\cdot\hat q$ の $\psi_0$ における分布（モーメント・裾・sub-Gauss 支配）だけ**から押さえて (N109) を出すこと。
**含まれないもの**: $\pi$ の分布以外の光子入力——分解能 $(X_q+\Lambda)^{-1}$ と組む形（稿 `110_` 命題 110-3 の $D_q$）、ソフト光子（赤外）評価、`E05-F24`/`F25` の汎関数積分表示を使う経路。**横波性が非摂動で効かないとは言っていない**（4. は 1 ループの値の判定）。**(N109) が偽だとも言っていない。**

**生きている分岐**: 稿 `110_` 命題 110-3 の **(N110) $\sup_{\sqrt{2m\Lambda}\le|q|\le2\Lambda}D_q\le C_Dm$**（`E05-P45` のブースト＋帯制限版。1 ループで $0.05\alpha m$ に飽和、玩具では $\gtrsim\frac{\alpha\lambda}{2\pi\mathrm e}m$ で破れる）を、ソフト光子構造で狙うこと。手がかり: 運動量 $-q$ を吸うコヒーレント雲の最小エネルギーは $\frac{3\pi q^2}{32\alpha m\ln(1+\lambda/2)}$ で、**低帯に入る条件は $h_{\rm 1loop}-1\gt1$**（`E05-F1`）、その雲と $\psi_0$ の重なりは赤外で $`\mathrm e^{-\|\alpha\|^2}=0`$（**見立て**。`F54` の生きている分岐 (b) と同じ道具）。

**出所**: 稿 `110_N109と光子入力.md` §6・§7、w195（2026-09-13）、(研究ノート: `205_w195_mu_low_band.py`)。

---


## F80（(1)「(N111) $`\mathcal K=\|\pi\psi_0\|^2\le Cm\Lambda`$（$\Lambda$ 一様）を示して (N110)⟹(N109) を閉じる」— 在庫の $\mathcal K$ 上界は $p=\frac57\gt0$ で届かず、摂動論の有効域では 1 ループ値と両立しない（**厳密な反証ではない。T88・`E05-P59`**）。(2)「運動量 $-q$ を吸うコヒーレント（Weyl）雲で $D_q$ の非摂動下界を作り (N110) を殺す」— 帯の底に届くには $n\gtrsim\lambda$ 光子が要り重なりが $\mathrm e^{-\lambda}$ で潰れる。2026-09-13、w196（稿 `111_` §6.1・§6.2）＋ audit105 の訂正）

**【親注記 2026-09-13】監査記録 (研究ノート: `111_N110_audit105_2026-09-13.md`)（PATCH 適用済）。FAILED は `F80` 以降。**
**【親注記 2026-09-13 後刻・audit108 の申し送り】(1) の「反証されてはいない」はその後 `E05-P62`（audit106、S2）で覆り、(N111) は摂動論抜きで偽と確定した（`F82`）。本節の「生きている経路（$\Theta\le(1-\delta)E_0$）」も `E05-P62` が別経路で同じ結論に達したため不要になった。(1) を「(N111) は未証明の十分条件」と読まないこと。**

**【連結指示】本ブロックは (研究ノート: `w196.FAILED.md`) を置き換える（あちらは連結しない）。audit105 が (1) の根拠を
`E05-P59` の明示的禁止に照らして不適格と判定し、(1) の付随注釈にあった含意の向きの誤りを削除し、(2) の閉鎖理由を差し替えた。
閉鎖の結論（どちらの経路も追わない）は両方とも生き残る。**

### (1) (N111) は「示せる見込みが無い」。ただし反証されてはいない

**在庫の側（厳密）**: `E05-P32` 3. の $\mathcal K=2m(E_0-\Theta)\le2mE_0$ に `E05-L4` を入れると
```math
\frac{\mathcal K}{m\Lambda}\le2C_2\,\alpha^{2/7}\lambda^{5/7}\qquad(\text{`E05-P59` 1.–2.、}p=\tfrac57).
```
(N111) は $p=0$ を要求するので、**在庫の改善の延長線上には無い**。（稿 `111_` の「在庫上限 `E05-P32` 3. を最低次で飽和するので余地なし」は
`E05-P32` の枝についてのみ真で、$\mathcal K$ の上界全体については偽である。`E05-P59` が既に $p=1\to\frac57$ を得ている。）

**摂動論の側（値。厳密ではない）**: 横波性 $k\cdot\epsilon=0$ から $`P_f\cdot A\,\Omega=0`$ なので $\psi_0=\Omega+O(e^2)$、$P_f\Omega=0$ ゆえ
$\pi\psi_0=eA(0)\Omega+O(e^3)$、$\mathcal K=e^2\langle\Omega,A(0)^2\Omega\rangle+O(e^4)=e^2S=\frac{\alpha\Lambda^2}\pi=\frac{\alpha\lambda}\pi m\Lambda$
（audit105 が独立再計算。$\langle\Omega,A^2\Omega\rangle=\frac1{(2\pi)^3}\int_{|k|\le\Lambda}\frac{d^3k}{|k|}=\frac{\Lambda^2}{4\pi^2}=S$）。
これは $\lambda\gt\frac{\pi C}\alpha$ で (N111) を破る。Landau 玩具（`F70`／`109_` §4）でも $\mathcal K=m\omega_c$、枝 $\omega_c=\frac{\alpha\Lambda^2}{\pi m}$ で同じ値。

**⚠ しかしこれは反証ではない（`E05-P59` の逐語の禁止。T88・T61）**: 1 ループ値 $\frac{\alpha\lambda}\pi m\Lambda$ は
$\lambda\gt(2\pi C_2)^{7/2}\alpha^{-5/2}$ で上の**厳密上界を破る**＝そこでは 1 ループ値自体が誤りである。
両立しないと言えるのは窓 $\frac{\pi C}\alpha\lt\lambda\lt(2\pi C_2)^{7/2}\alpha^{-5/2}$ の中だけで、そこでの判定は
「摂動論がその窓で有効である」という**未証明の前提**に乗っている。

**⚠ 削除した誤り（audit105）**: 旧稿は「(N111) が成れば $\Theta\ge E_0-\frac{C\Lambda}2$ で `E05-F4` の仮定 $\Theta=o(\Lambda^2/m)$ が満たされ
$h_{\rm coh}=o(\lambda)$ が出る」と書いていたが、**$\Theta$ の下界から $\Theta$ の上界は出ない（含意の向きが逆）**。
したがって「(N111) は Q3 の劣線形側を含意する主張だった」という結論も**根拠を失う**。
（なお `E05-P10` の $\Theta\le E_0$ と `E05-L4` の $E_0\lt C_2\alpha^{2/7}\Lambda^{12/7}m^{-5/7}$ から $\Theta=o(\Lambda^2/m)$ は
**(N111) を仮定せずに**出るので、この一文は不要でもあった。）

**正しい読み**: (N111) ⟺ $E_0-\Theta\le\frac C2\Lambda$ ＝「**基底エネルギーのうち運動項が $O(\Lambda)$ しか占めず、場のエネルギー $\Theta$ が
$E_0$ のほぼ全部を担う**」。`E05-L4` の下界 $E_0\gt C_1\alpha^{1/2}m\lambda^{3/2}$ と合わせると $\Theta$ が巨大であることを要求する、かなり強い条件である。

**⚠ 再挑戦禁止の範囲**: 閉じたのは「**$\mathcal K$ の $\Lambda$ 一様上界を在庫の延長で示して (N110) を出す**」型のみ。
**(N110)・(N109) 自体は生き残る**（十分条件が偽でも標的は死なない）。また $E_0\gtrsim\Lambda$ の側は (N111) を反証しない
（$\mathcal K=2m(E_0-\Theta)$ で $\Theta$ が担い得る）。
**⚠ 生きている経路（audit105 の提案）**: **$\Theta\le(1-\delta)E_0$（固定 $\delta\gt0$）が 1 本示せれば**
$\frac{\mathcal K}{m\Lambda}\ge\frac{2\delta E_0}\Lambda\gt2\delta C_1\alpha^{1/2}\lambda^{1/2}\to\infty$ で **(N111) は摂動論抜きで厳密に反証される**。
在庫は $\Theta\le E_0$（`E05-P10`、$\delta=0$）だけなので、要るのは定数因子 1 本である。**この 1 本を「1 ループで偽」で代用してはならない。**

### (2) コヒーレント（Weyl）雲による kill は不成立 — ただし障害は赤外ではない

**族内の最小コスト（正しい。audit105 が独立再導出）**: $\alpha_{k\lambda}=\theta\phi(|k|)(\epsilon_\lambda(k)\cdot\hat q)$（$\theta,\phi$ 実・$\phi$ 動径）で
$\langle\pi+q\rangle=0$ の下に二次コスト $\int(\omega+\frac{k^2}{2m})|\alpha|^2$ を最小化すると、最適 $\phi=\frac{c_k}{\omega+k^2/2m}$、
```math
E_{\min}=\frac{3|q|^2}{8e^2}\Bigl[\int\frac{c_k^2\,d^3k}{\omega+\frac{k^2}{2m}}\Bigr]^{-1}=\frac{3\pi|q|^2}{16\,\alpha\,m\,L},\qquad L=\ln(1+\tfrac\lambda2),
```
$E_{\min}\lt\frac a2\iff\alpha L\gt\frac{3\pi}4\iff h_{\rm 1loop}-1=\frac{8\alpha L}{3\pi}\gt2$。
**副産物（PATCH、適用済）**: `110_` §9 残タスク 1.（見立て欄）の $\frac{3\pi q^2}{32\alpha mL}$・閾値「$h-1\gt1$」は因子 2 の誤りで、上の値に訂正した。

**⚠ 旧稿の閉鎖理由は誤りだった（audit105）**: 旧稿は「最適雲の光子数が $`\|\alpha\|^2\propto\int_0\frac{dk}k=+\infty`$（赤外）なので
重なりが恒等的に 0、ゆえにコヒーレント試行から下界は 1 本も出ない」と書いていたが、
(i) $`\|\alpha\|=\infty`$ のとき $W(\alpha)\Omega$ は Fock 空間の**ベクトルではない**ので「$\psi_0$ と直交する」は範疇違いであり、
(ii) 赤外発散は **$\phi$ が実・動径（⟹ $\langle P_f\rangle=0$、運動量を $e\langle A\rangle$ でしか運べない）という部分族の人工物**である。
実際 $\alpha$ を**純虚・非動径**に取れば $`\langle A\rangle\propto\mathrm{Re}\,\alpha=0`$・$\mathrm{Cov}(P_f,A)=0$ のまま
$\langle P_f\rangle=-q$ が作れ、半頂角固定（$\langle\cos\rangle=\bar c$）・殻半径 $\kappa$・光子数 $n$ で
```math
\langle X_q\rangle=\frac{|q|\kappa}{2m\bar c}+\frac{|q|}{\bar c}+\Bigl(\frac{\alpha\Lambda^2}{2\pi m}-E_0\Bigr),\qquad n=\frac{|q|}{\kappa\bar c}.
```
$|q|=2\Lambda$・$\kappa=0.4\Lambda$・$\bar c=0.75$ で $\langle X_q\rangle\approx0.53\cdot\frac a2\lt\frac a2$、$n=6.7$（**有限**）。
Markov で $`\|L_q\phi\|^2\ge1-0.53\gt0`$、重なりは $O(\mathrm e^{-n/2})=O(10^{-2})$ で **0 ではない**。
**⟹ 「コヒーレント試行から下界は 1 本も出ない」は偽である。**

**正しい閉鎖理由（audit105）**: コヒーレント状態は $P_f$ に **Poisson 的な分散** $\mathrm{Var}(P_f)=n\kappa^2$ を持ち、
$\frac{\mathrm{Var}(P_f)}{2m}=\frac{|q|\kappa}{2m\bar c}$ が反跳コストとして残る。**帯の底**（$X_q=O(\Lambda)$）に届くには
```math
\kappa\lesssim\frac{2m\bar cC\Lambda}{|q|}\ \Longrightarrow\ n=\frac{|q|}{\kappa\bar c}\gtrsim\frac{|q|^2}{2m\bar c^2C\Lambda}=\frac{2\lambda}{\bar c^2C}\quad(|q|=2\Lambda)
```
すなわち $n\gtrsim\lambda$ 光子が要り、重なりが $\mathrm e^{-n/2}\le\mathrm e^{-\lambda}$ で潰れる。
帯の中ほど（$X_q\sim\frac a4$）なら $n=O(1)$ で届くが、そこでの下界は $`D_q\lesssim\frac{\|\pi_{\hat q}\psi_0\|^2}{a/4}=O(\alpha m)`$ で $\Lambda$ 一様であり、(N110) を破らない。

**⚠ 再挑戦禁止の範囲（T60。旧稿より狭い）**: 閉じたのは**コヒーレント（Weyl）族**による (N110) の kill のみで、
その死因は**Poisson 反跳分散**であって赤外発散ではない。
**⟹ 光子数を固定した Fock 試行はこの死因を持たない**（$n=\lceil|q|/\Lambda\rceil\le2$、各光子 $|k|\approx\Lambda$、$k+k'=-q$ なら
$(\pi+q)$ の $P_f$ 由来の分散がゼロで $X_q\approx|q|$ ＝帯の底に直接乗る）。**この型を「閉鎖済み」と読んではならない。**
玩具 `F70` には光子が無く $E_{\min}$ は定義されない＝閉鎖の外。

**⚠ audit105 が実際に走らせた kill-check（結果は失敗＝(N110) は生き延びた）**: 上の 2 光子 Fock 試行で
$v^{(2\gamma)}=((k+k')\cdot\hat q)\psi^{(2)}$、$\psi^{(2)}\simeq-\frac{e^2c_kc_{k'}(\epsilon\cdot\epsilon')}{m(|k|+|k'|+\frac{|k+k'|^2}{2m})}$ を
$|q|=2\Lambda$ の帯で評価すると $D_q^{(2\gamma)}\approx\frac{3f\alpha^2}{\pi^2}m$（$f=O(10^{-2})$ は $\lambda$ に依らない測度分率）で **$\Lambda$ 一様**。
帯の底（$|k+k'+q|\lesssim\sqrt{2m\Lambda}$）の寄与は全体の $O(\lambda^{-1/2})$ で劣位。**5 分のスケーリング評価であって数値検証ではない**が、
**「低エネルギー端は真に非摂動」という旧稿の判定 111-7 は誤り**（殻では $n\le2$ ＝ $O(\alpha^2)$、計算可能）であることは確定した。

## F81（「$\psi_0$ の 2 光子セクター（$O(\alpha^2)$）の $D_q$ を数値で出して (N110) $\sup_{\rm shell}D_q\le C_Dm$ を撃破する」— 値は確かに $\Lambda$ 一様でなく $0.033\alpha^2m\sqrt\lambda$ だが、$O(1)$ に達するのは摂動有効域の $1.5\times10^6$ 倍外側で**窓が空**。2026-09-13、w199、稿 `112_2光子セクターのDq.md`）

**【親注記 2026-09-13】監査は未（S2 候補）。各点版と積分版の乖離に数値の裏づけ。⚠ O(alpha2) の交差項 2 種は未計算。**

**【親注記】**本ブロックは `F80` の続き。`E05-P60` の射程欄・`111_` §6.3 末尾にあった
「2 光子セクターでも (N110) は破れない見込み」は**別の理由で取り下げる**（見込みは外れていたが、kill も成立しない）。
処方は (研究ノート: `w199.PATCH.md`)。数値の正本は (研究ノート: `w199.PROVED.md`)（`E05-P?`）。

### 経緯

audit105 R6.3 が「低帯の低エネルギー端に届くには $n\gtrsim|q|/\Lambda$ 光子が要るが、殻は $|q|\le2\Lambda$ なので $n\le2$、
すなわち $O(\alpha^2)$ で計算可能」と指摘し、同 R6.4 が 5 分のスケーリング評価で
$D_q^{(2\gamma)}\approx\frac{3f\alpha^2}{\pi^2}m$（$f=O(10^{-2})$、$\Lambda$ 一様）と見積もった。
w199 が独立に求積した（(研究ノート: `210_w199_Dq_2photon.py`)、$\lambda=64\ldots262144$ の 7 段）。

### 何が起きたか

1. **audit105 の見積りは殻の上端 $|q|=2\Lambda$ でだけ正しい**（実測 $0.00663\alpha^2m$ に飽和、見積り $0.003\alpha^2m$ と factor 2.2）。
2. **$\sup_{\rm shell}$ はそこではない。** 最大点は $|q_*|\to4.82\sqrt{2m\Lambda}$（殻の内点、$a_*\to23.3\Lambda$）で、
   ```math
   \sup_{\rm shell}D_q^{(2\gamma)}=(0.033\pm0.001)\,\alpha^2m\sqrt\lambda
   ```
   （局所指数 $0.896\to0.704\to0.606\to0.554\to0.528\to0.514$、上から $\frac12$ に収束、最後の 3 段で不変）。
   **⟹ 「2 光子でも $\Lambda$ 一様」は偽。**
3. **にもかかわらず (N110) は撃破されない。** $0.033\alpha^2\sqrt\lambda\ge C_D$ は $\lambda\ge C_D^2\cdot3.2\times10^{11}$（$\alpha=\frac1{137}$）を要求し、
   摂動有効域の目安 $\lambda\lesssim\alpha^{-5/2}=2.2\times10^5$ の内側では高々 $8.2\times10^{-4}$。**窓が空**である
   （余裕 $1.5\times10^6$ 倍。摂動有効域が 1000 倍広くても不変。T91 の言う「保留」で、射程が崩れても偽の定理は生じない）。

### 閉鎖の正確な範囲（T60）

**閉じたのは「$\psi_0$ の有限光子セクターの摂動値を数値で出して (N110) を殺す」型**である。理由は数値の大きさではなく**次数勘定**で:

> **足切り**: $O(\alpha^n)$ の項が $`c\,\alpha^n\lambda^p`$ なら、摂動有効域 $\lambda\le\alpha^{-5/2}$ の中で $O(1)$ に達する条件は
> $$p\ \ge\ \frac{2n}5\qquad(n=1\Rightarrow p\ge0.4,\ \ n=2\Rightarrow p\ge0.8,\ \ n=3\Rightarrow p\ge1.2).$$
> 1 光子は $p=0$（`205_`/`207_` で飽和）、2 光子は $p=\frac12$。**どちらも失格。**
> （`E05-P59`／`F80` の (N111) は $n=1,p=1$ で足切りを通っていた。通ったのに反証にならなかったのは別の理由＝
> 1 ループ値自体が `E05-L4` の厳密上界と矛盾する領域があったから。）

**閉じていないもの**:
- **交差項**（$2\mathrm{Re}\langle v^{(1\gamma)},LRV_1Rv^{(2\gamma)}\rangle$ とレゾルベントの 2 次補正）。同じ $O(\alpha^2)$ で未計算。
  ただしこれらも $n=2$ なので同じ足切り $p\ge0.8$ に掛かる（$p\gt\frac12$ を出さない限り kill にはならない）。
- **非摂動の下界**。変分形 $D_q\ge\frac{|\langle\phi,\pi_{\hat q}\psi_0\rangle|^2}{\langle\phi,(X_q+\Lambda)\phi\rangle}$ に 2 光子 Fock ベクトルを入れる道は、
  分母の $\frac{e^2}{2m}(A^2-S)$（ノルム $O(\alpha\lambda\Lambda)$）が $\alpha\lambda\gtrsim1$ で自由部を超えること、および
  Fock ベクトルが $\mathrm{Ran}L_q$ に厳密には入らないことで塞がる。**`111_` 判定 111-5（`F2` 型の壁）と同じ壁。**
- **(N110) そのもの**。生き延びたのであって正しいと示されたのではない（T60）。

### 副産物（(研究ノート: `w199.PROVED.md`) が正本）

- 同じ 2 光子対角項で $`\int_{\rm shell}g\mu_{\rm low}^{(2\gamma)}d^3q=0.514\,\alpha^2m\Lambda(\ln\lambda)^2`$。
  **各点版 (N110) は $\sqrt\lambda$、積分版 (N109) は $(\ln\lambda)^2$**——`E05-P58` 3. の「(N110) は (N109) の各点版＝強化」の定量（T89）。
- $\sup D^{(2\gamma)}/\sup D^{(1\gamma)}$ は $\lambda\approx4.5\times10^4$（**摂動有効域の内側**）で 1 を超え、
  $\lambda=16384$（`207_` の最大値）で既に 58%。**`205_`/`207_` の 1 ループ飽和はその近傍で主要項ではなくなる。**
- **教訓（罠候補）**: audit105 も w199 自身も「殻の 1 点（上端 / 下端）だけを見て $\sup_{\rm shell}$ を語る」誤りを踏んだ。
  $\sup$ の主張は殻の内点で達成されうる。

## F82（「(N111) $\mathcal K\le Cm\Lambda$（$\Lambda$ 一様）を示して (N110)⟹(N109) の鎖を閉じる」— **(N111) は偽である**（厳密・摂動論抜き）。さらに「$\mathcal K$ の上界を詰めて (N110)・(N109) を得る」経路全体が冪 $p\in[\frac27,\frac57]$ に挟まれ $p=0$ に届かない。2026-09-13、w200、稿 `113_` §5・§6.2）

**【親注記 2026-09-13】audit106（S2、(研究ノート: `113_N111反証_audit106_2026-09-13.md`)）が 3 段すべてを独立再導出して成立と判定、PATCH 適用済。命題部分は verifier-backed。**

**【親注記 2026-09-13】本行は `F80` (1) を**格上げ**する。`F80` (1) は「在庫の上界が届かない／1 ループ値と両立しない（**厳密な反証ではない**。T88）」という保留だった。
本行はそれを**厳密な反証**に置き換える。`F80` (1) の判定（1 ループ値は根拠として不適格）自体は正しいまま。対応する PROVED は `E05-P?`（w200）。**

格付け: `self-audited`（稿 `113_ThetaとN111.md` §7、敵対的セルフレビュー 14 項目）。**独立監査は未（S2）。**

**閉じた主張**:
1. **(N111)**: $\exists C$（$\Lambda$ 一様）$`: \mathcal K=\|\pi\psi_0\|^2\le Cm\Lambda`$。⟹ **偽**。
2. 「$\mathcal K$ の上界を在庫より詰めれば (N110)（$\sup_{\rm shell}D_q\le C_Dm$）または (N109)（$I_\mu\le C'm\Lambda$）が $\Lambda$ 一様に出る」
   という型の発注（`E05-P59` 1. の $I_\mu\le\frac{32\pi}3\mathcal K$、同 3. の $D_q\le\frac{\mathcal K}{3\Lambda}$ を通す全経路）。⟹ **原理的に届かない。**

**正確な障害**:
1. **反証の機構（3 段。すべて初等・非摂動）**:
   (i) $\pi_\Lambda=P_f+eA_\Lambda(0)$ は $m$ を含まず、2 次形式核も $m$ に依らないので、$\psi_0(m)$ を $H(m')$ の試行状態に使えて
   $\mathcal K(m)\ge2\bigl(E_0(m')-E_0(m)\bigr)/(\frac1{m'}-\frac1m)$（$m'\lt m$。$E_0$ は $u=\frac1{2m}$ の凹関数、$\mathcal K$ はその優微分）。
   (ii) 光子運動量の伸縮 $\Gamma(D_\sigma)$ で $E_0(\sigma m,\sigma\Lambda)=\sigma E_0(m,\Lambda)$、ゆえに $E_0=m\mathcal E(\alpha,\lambda)$。
   (iii) $m'=m/t$、$t=\frac{4C_2^2}{C_1^2}\alpha^{-3/7}\lambda^{3/7}$ と取り `E05-L4` の**下界を $t\lambda$ で・上界を $\lambda$ で**使うと
   $\frac{\mathcal K}{m\Lambda}\ge\frac{C_1^2}{2C_2}\alpha^{5/7}\lambda^{2/7}\to\infty$。
2. **唯一の光子入力は `E05-L4` の下界指数 $\frac32\gt1$ である。** 同じ抽象構造で $\mathcal E\asymp\lambda^1$ になる結合を取ると
   $\mathcal K\le2mE_0\le cm\Lambda$ で (N111) は**真**になる。⟹ 論法は空虚でない（F70 型の玩具テストを通る）。
3. **上界側も不可欠**: 一般に $\mathcal E\ge L\lambda^a$・$\mathcal E\le U\lambda^b$ から出る冪は $(b-1)-\frac{b-a}{a-1}$ で発散条件は $b(2-a)\lt1$。
   $(\frac32,\frac{12}7)$ は $\frac67$ で通るが、上界を真空変分（$b=2$）で代用すると**ちょうど境界**で定数しか出ない。
4. **経路の両側挟み**: 1. と `E05-P59` 2. で $\frac{C_1^2}{2C_2}\alpha^{5/7}\lambda^{2/7}\le\frac{\mathcal K}{m\Lambda}\le2C_2\alpha^{2/7}\lambda^{5/7}$。
   $\mathcal K$ を通す評価は $p\ge\frac27\gt0$ を免れない。**「$\mathcal K$ の上界をあと少し詰める」型の改善余地は $\frac37$ しか無く、ゼロにはできない。**

**再挑戦禁止の範囲（T60）**:
- (N111) を**示そうとする**発注（偽なので不可能）。
- $\mathcal K$ の上界**だけ**を詰めて（＝標的を $\mathcal K$ の定数倍で支配して）(N110)・(N109) の $\Lambda$ 一様性を得る発注。**$\mathcal K$ を他の量と組み合わせて相殺を取る経路は禁止しない**（audit106 R6、T84 (f)）。
- **禁止しないもの**: (N110)・(N109) 自体（どちらも無傷。(N111) より真に弱い）。(N110)⟹(N109)（w195、audit104 R2 が検算）。
  **`E05-P60` 1.（(N110) ⟺ $\sup_{\rm shell}\mu\le C$）、同 3.（密度型十分条件）、帯に制限した LP** など $\mathcal K$ を経由しない入口。
  **$`\|\rho_S\|_{op}`$・`E05-P5`・C 項の評価一般**（本行は何も言わない。T43）。

**生きている分岐**:
- **(N112)**「$\exists\epsilon\gt0$: $\mathcal E(2\lambda)\ge2^{1+\epsilon}\mathcal E(\lambda)$」を示せば絶対定数 $\delta$（$\Theta\le(1-\delta)E_0$）が出る。
  **`E05-L4` だけからは出ない**（上下包絡の比が $\lambda^{3/14}\to\infty$ で、局所指数 $1+\epsilon$ の長い区間を排除しない）。
  ⟹ **`E05-L4` の外の入力**（例: $E_0$ の上下の指数を一致させる評価、あるいは $E_0$ の漸近の同定）が要る。**⚠ 書誌未確認**: w200 は「`arXiv:2004.06494`（Bach–Hach）の明示定数つき上界」を候補に挙げたが、**本監査の読み許可の外で原典を 1 手も確認していない**。番号・著者・内容が合っているかを確認するまで台帳に固有名で載せないこと（`CITATIONS_PENDING.md` 行き）。
- (N110) への非 $\mathcal K$ 経路（上記）。

**出所**: 稿 `113_ThetaとN111.md`（w200、2026-09-13）、(研究ノート: `2026-09-13_w200_Theta.md`)、
(研究ノート: `211_w200_theta_supergradient.py`)（seed 2000913、`PASS`。**抽象構造のみを検証。PF の反証は検証していない**）。

---



## F83（「$n\ge3$ 光子セクターの冪 $p_n=n-\frac32$ が足切り $p\ge\frac{2n}5$ を通ることを使って (N110) を有効域の内側で撃破する」— 外挿が偽で、実測 $p_3=0.508\to\frac12$。窓の余裕はむしろ $n=2$ より $5\times10^4$ 倍広い。2026-09-13、w202、稿 `114_n光子外挿.md`）

**【親注記 2026-09-13】未監査（S2 候補）。\le3$ の**値**であり、\ge4$ と (\alpha3)$ 交差項は未測（T88）。**

**閉じた主張**: `E05-P63` に「次の一手」として付された次数勘定 $D^{(n\gamma)}\sim c_n\alpha^nm\lambda^{n-3/2}$（$n\ge2$）から、
$p_n\ge\frac{2n}5\iff n\ge\frac52$ ゆえ $n\ge3$ は足切りを通り、$\frac{D^{(n+1)}}{D^{(n)}}\sim\alpha\lambda$ ゆえ
「$D_q$ の真の展開パラメタは $\alpha\lambda$ で制御は $\lambda\lesssim\alpha^{-1}=137$ まで」、したがって
**(N110) $\sup_{\rm shell}D_q\le C_Dm$ は摂動有効域 $\lambda\lesssim\alpha^{-5/2}$ の内側で危うい**、という経路。

**正確な障害（2 つ。独立）**:
1. **振幅**: $\Psi^{(n)}\sim e^n\Lambda^{-n}$ が成り立つのは**中間状態の総運動量がすべて軟らかい**配位に限る。
   $n$ 個の硬い光子を総運動量 $\simeq-q$（軟）に組む一般の配位では部分和 $\sigma_S$ が硬く、
   `E05-F7`（反跳の抑制は総運動量のみで決まる）により中間分母が $\frac{|\sigma_S|^2}{2m}\sim\frac{\Lambda\lambda}2$ になる。
   実際 $n=3$ の全硬配位は $\Psi^{(3)}\sim e^3\Lambda^{-4}$ で、$D^{(3\gamma)}_{\rm 全硬}\sim\alpha^3m\lambda^{-1/2}$（$p=-\frac12$）。
2. **位相体積**: 反跳を免れるには光子を**背中合わせ対**に組み、**各対の総運動量を $\lesssim\sqrt{2m\Lambda}$ に拘束**せねばならない。
   拘束は対ごとに 1 本要るので体積は $\Lambda^{3(n-1)}(m\Lambda)^{3/2}$ ではなく $\Lambda^{3j}(m\Lambda)^{3j/2}$（$j=\lfloor n/2\rfloor$）。
   拘束を外すと振幅が $\lambda^{-2}$・体積が $\lambda^{3/2}$ で差引 $\lambda^{-1/2}$ 損なので、拘束領域が勝つ。

**正しい勘定**: $D^{(n\gamma)}\sim c_n\alpha^nm\lambda^{\lfloor n/2\rfloor/2}$。$\sqrt\lambda$ を買う単位は光子ではなく**背中合わせ対 1 組**で、
1 組あたり $\alpha^2\sqrt\lambda$（余った 1 個は $\alpha$ だけで $\lambda$ を稼がない。$|k|\sim|q|$ で反跳分母が立ち、対数も出ない）。
$p_1=0$・$p_2=\frac12$ の既知の実測を再現し、$n=3$ の実測 $\sup_{\rm shell}D^{(3\gamma)}=0.0197\alpha^3m\sqrt\lambda$（局所指数 $\to0.508$、7 段）と一致する。

**数値の判定**: $p_3=\frac32$ なら一定であるべき $\sup/\lambda^{3/2}$ が 7 段で 3 桁落ちる（$7.06\times10^{-5}\to7.51\times10^{-8}$）。
$\frac{D^{(3)}}{D^{(2)}}=0.60\alpha$ は $\lambda$ に依らず、$\alpha\lambda$ の予言と $\lambda=2.6\times10^5$ で $4\times10^5$ 倍食い違う。
窓判定: $0.0197\alpha^3\sqrt\lambda\ge C_D$ は $\lambda\ge C_D^2\cdot1.7\times10^{16}$ を要し、有効域の内側では高々 $3.6\times10^{-6}$（余裕 $7.8\times10^{10}$ 倍）。

**⚠ 何が閉じて何が閉じていないか（T60）**:
- **閉じた**: 「$\lambda^{n-3/2}$ 型の外挿」と「展開パラメタ $\alpha\lambda$」に基づく発注。$n=3$ は実測で決着。
- **閉じていない**: (i) **$n\ge4$ は実測していない**（$p_4=1$ は次数勘定。対が 2 組になる構造が初めて現れる所で、外挿の最弱点）。
  (ii) $O(\alpha^3)$ の**交差項**は未計算（w201 が $O(\alpha^2)$ で行った仕事の次の次数）。
  (iii) 非摂動の $D_q$ については何も言っていない。**(N110) は撃破もされず証明もされていない＝保留**（T88・T91 規則 3）。
- **⟹ 「$n$ 光子セクターで (N110) を殺す」型の発注を一般に止める文ではない。** 止まるのは上の 2 つの外挿に依拠する発注だけである。

**教訓（TRAPS 候補。親の判断）**: **2 点以上で校正されていない次数勘定を、発注の向きを決める根拠に使わない。**
`E05-P63` の外挿は $n=2$ の 1 点でしか校正されておらず（$n=1$ を入れると $p_1=-\frac12$ で即座に外れる）、
しかも「未検証」と正しく hedge されていたにもかかわらず、「(N110) を殺しうる唯一の未検査量」として発注の最優先に据えられた。
**hedge は射程を守るが向きは守らない。** 安価な整合検査は **1 点（$n=1$）を代入するだけ**だった。

## F84（「形式 $e$ 展開の次数を上げて (N110) を撃破する」経路は**次数に依らず構造的に閉じている** — 各次の値は $D_q$ の上界でも下界でもなく、しかも $n\ge2$ の全ての測定済みセクターが既に $\lambda$ 非有界なので、止めているのは常に摂動論の $\Lambda$ 非一様性だけである。2026-09-13、audit107、(研究ノート: `112_114_数値鎖_audit107_2026-09-13.md`) §1.4・§2）

**【親注記 2026-09-13】audit107（S2、(研究ノート)）の成果物。PATCH 7 件適用済。**

**閉じた主張**: 「$n$ 光子セクター（または $O(\alpha^n)$ の交差項）をもう 1 次計算して、
$\sup_{\rm shell}D_q$ が摂動有効域の内側で $O(1)$ に達することを示し、(N110) $\sup_{\rm shell}D_q\le C_Dm$（$\Lambda$ 一様）を撃破する」。

**正確な障害（3 段。どれも次数を上げても消えない）**:

1. **反証条件が値の大小ではない。** `E05-P58` 3. の (N110) は「**$\Lambda$ に依らない絶対定数 $C_D$ が存在して**」という形なので、
   反証は $\limsup_\lambda\sup_{\rm shell}D_q/m=\infty$（非有界性）である。
   「有効域の内側で $O(1)$ に達するか」は $C_D=1$ を暗黙に置いた補助指標にすぎない。
2. **測定済みの各次は既に非有界である。** $p_2=p_3=\frac12\gt0$（`E05-P61` 1.、`E05-P64` 1.）。
   形式展開が $\Lambda$ 一様なら 2 光子項だけで**どんな $C_D$ に対しても** (N110) は反証される。
   **⟹ 撃破を止めているのは窓の広さでも次数でもなく、ひとえに摂動論の $\Lambda$ 非一様性（`E05-L4`）である。**
   これは次数を上げても改善しない（むしろ高次ほど帯の端が効く。`E05-P63` 射程）。
3. **各次の値は $D_q$ の上界でも下界でもない**（T88）。$O(\alpha^N)$ まで全部足しても剰余の評価が無い以上、
   $D_q$ についての不等式は 1 本も出ない。変分下界への転化も `111_` 111-5 と同じ `F2` 型の壁
   （分母の $\frac{e^2}{2m}(A^2-S)$ が $O(\alpha\lambda\Lambda)$ で $\alpha\lambda\gtrsim1$ では自由部を超える、
   Fock の $n$ 光子ベクトルは $\mathrm{Ran}L_q$ に厳密には入らない）で塞がれている。

**冪の側からの補強（次数勘定。`E05-P64` 3. を audit107 が $n\le4$ で独立再導出）**:
$\lambda$ の指数を稼ぐ単位は**帯の中の硬い背中合わせ対 1 組＝$+\frac12$** だけで、$p_n=\frac{\lfloor n/2\rfloor}2$。
足切りの要求 $\frac{2n}5$ との比は $\frac58$ で $n$ 非依存なので、**冪は $n$ を上げても追いつかない**。
$n=4$ について $p_4=1$ を独立に再現し、$`\{V_2,V_1,V_1\}`$ 配位（$p=0$）・軟光子配位（$p=0$）・
中間スケール $\mu=\lambda^s$ の族（$n=2$ で $D\propto\mu$ ゆえ最硬端が支配）・$\chi$ を殻上端まで動かす道（$D\propto\chi^{-1}$）を
すべて潰し、**$p_4\ge\frac85$ に届く配位が無い**ことを確認した。

**⚠ 閉鎖の範囲（T60。ここを超えて使わないこと）**:
- 閉じたのは「**形式 $e$ 展開の有限次数を計算して (N110) を撃破する**」経路だけである。
  **(N110) が真であるとは言っていないし、非摂動の経路（変分下界・`E05-P62` 型の厳密不等式・汎関数積分）は一切閉じていない。**
- 冪の側の補強は**次数勘定であって証明ではない**（$c_n$ も角度・偏極の相殺も評価していない）。
  実際、「全 $n$ が失格」を言うには $c_n\ll\alpha^{-3n/8}=6.33^n$ という**係数の増大率の仮定**が別途要る
  （`E05-P64` 5. はこの仮定を明記していない。処方は (研究ノート: `audit107.PATCH.md`) の P-7）。
  $c_1=0.05,c_2=0.033,c_3=0.0197$ は減少列なので現状は安全である。
- $n\ge4$ の実測は依然として未了で、**$n=4$（対が 2 組になる最初の場所）は次数勘定の最弱点**である。
  ただし本項により「$n=4$ を測って (N110) を撃破する」ことは目的として成立しない（1.–3. が先に効く）。
  $n=4$ を測る価値は**外挿の検証**にあり、撃破にはない。
- `F81`（2 光子）・`F83`（3 光子）は本項の特別な場合であり、本項はそれらを一般化して
  **「次の次数」型の発注を恒久的に止める**ものである。逆に、`F81`・`F83` が書いている
  「窓が空」という根拠は本項 1. により**補助指標に格下げされる**（結論は変わらない）。

## F85（「原典 Hiroshima 2007 の $D(N^\alpha)$ 伝播補題で $\psi_0\in D(N)$ を出す」— 仮定が $\Phi\in D((N+1)^\alpha)$ なので恒等式経由は循環し、近似経由は $E_0\gt0$ の指数に負ける。2026-09-13、w208、稿 `117_` §4.2）

**【親注記 2026-09-13】audit115 R5 の逆転監査で閉鎖は壊れなかった。PATCH P6・P7a・P7b・P8 適用済（障害の重心は位相因子の絶対値が 1 で減衰因子を構造的に捨てる点。E0 の狭義正値性は E05-L4 の漸近命題のみ）。**

格付け: `self-audited`（稿 `117_` §4.2。数値なし。原典 PDF の直読と初等評価のみ）。

**この評価の型で足りないもの**: 「Hiroshima, JFA **252** (2007) / `arXiv:math-ph/0607014` の $N$ 伝播補題を $\psi_0$ に当てて
$\psi_0\in D(N)$（ひいては $\langle NH_{\rm f}\rangle_0\lt\infty$）を得る」という型。

**原典の逐語**（(研究ノート: `hiroshima2007_fiber.pdf`) p.28 を `Read` で直読。要約経由ではない）:

> **Lemma 3.11** Let $\Phi\in D((N+1)^\alpha)$ with $\alpha\in\mathbb N$. Then $e^{-tH(P)}\Phi\in D(N^\alpha)$ with the
> inequality $`\|N^\alpha e^{-tH(P)}\Phi\|_{\mathcal F_{\rm b}}\le C\|(N+1)^\alpha\Phi\|_{\mathcal F_{\rm b}}`$, where $C$ is a constant independent of $P$.

**正確な障害（2 つ）**:
1. **$\Phi$ のクラスが $D((N+1)^\alpha)$**。恒等式 $\psi_0=e^{tE_0}e^{-tH(0)}\psi_0$ に当てるには $\psi_0\in D((N+1)^\alpha)$ を先に知る必要があり、**循環する**。
   補題は $D(N^\alpha)$ を無から作らず、**伝播させるだけ**である。
2. **定数 $C$ は $t$ 非依存と書かれていない**（証明は Burkholder 型不等式 (3.44) の $t^m$ を経由するので $C(t)$ は $t$ の多項式）。
   $\Omega\in\cap_\alpha D(N^\alpha)$・$\langle\Omega,\psi_0\rangle\ne0$（`E05-F22`）から作る近似 $`\psi_t=e^{-tH(0)}\Omega/\|e^{-tH(0)}\Omega\|`$ では
   $`\|N\psi_t\|\lesssim C(t)e^{tE_0}/|\langle\Omega,\psi_0\rangle|\to\infty`$。**$E_0\gt0$**（**⚠ audit115 R5-b4**: 原典 Cor 3.8 (2) は $e^2$ についての**非狭義**単調増加なので $E_0\gt0$ を与えない。狭義正値を担うのは `E05-L4`（Lieb–Loss の下界 $C_1\alpha^{1/2}\Lambda^{3/2}$）だけで、公理表は同項に「原典は $\alpha$ 固定・$\Lambda$ 大の漸近命題で閾値 $\Lambda_0(\alpha)$ を与えない」と明記している。**ゆえに本フォールバック（$C$ が $t$ 一様でも死ぬ）は「$\alpha$ 固定・$\Lambda$ 十分大」でのみ主張できる。障害 1（循環）は無条件なので本項の結論自体は残る。**）なので
   **指数が多項式に勝つ**。⚠ 仮に $C$ が $t$ 一様であっても $e^{tE_0}$ が残るので結論は同じ。**⚠ 障害の重心は $t^m$ ではない**（audit115 R5-b2）: 補題の証明は汎関数積分表示で $|e^{-ie\mathcal A_1}|\le1$ と評価し Wiener 測度が確率測度であることしか使わないので、**$e^{-tH(P)}$ の指数減衰 $e^{-tE_0}$ が構造的に丸ごと捨てられる**。$P$ 非依存の $C$ にはそれが入りようがない。

**⚠ 書誌の訂正（本項の副産物）**: `E05-F25` はこの補題を「**Lemma 3.10**（e-print `Fiber.tex` 2113 行）」と記録するが、
上記 PDF では **Lemma 3.11**（p.28）である。同 PDF の **Lemma 3.10**（p.26、§3.3.2 "Invariant domains and essential
self-adjointness of $K(P)$"）は別命題で、逐語「Assume that $\omega^{3/2}\hat\varphi\in L^2(\mathbb R^d)$. Then
$e^{-tK_{\rm F}(P)}[D(P_{\rm f}^2)\cap D(H_{\rm f})]\subset D(P_{\rm f}^2)\cap D(H_{\rm f})$」（式 (3.31)）。
`E05-F27` が既に記録した版差（Cor 4.3 ↔ Cor 4.4）と同型のずれで、**内容は一致、番号のみの訂正**。
E05 の $\hat\varphi=\mathbf 1_{|k|\le\Lambda}$ は Lemma 3.10 の仮定 $\omega^{3/2}\hat\varphi\in L^2$ を満たす。

**次に要る入力（1 つ）**: $\psi_0\in D(N)$ を文献から取る経路を続けるなら、**「$e^{-tH(0)}$ の $N$ 依存性が $e^{-tE_0}$ と同じ指数で減衰すること」**の 1 つだけ。原典 Lemma 3.11 はこれを与えない。
（**⚠ audit115 R5-b3 による削除**: 旧稿はここに「$t$ について一様な $N$ モーメント評価」も併記していたが、障害 2 の ⚠ のとおり $C$ が $t$ 一様でも $e^{tE_0}$ が残るので十分入力ではない。）

**⚠ この項は稿 `117_` の主結果を塞がない。** `117_` 命題 117-2 は $N$ を一度も呼ばずに
(D-form) の $H_{\rm f}$ 重みを `E05-F26` だけで閉じており、本項とは独立の型である。

**⚠ 親へ**: 本項を閉鎖として `FAILED.md` に載せるかは、**「閉鎖を壊しに行け」の監査を通してから**判断されたい（w208 は判断しない）。

---

## 本ラウンドの副次判定（新規の F ではない。`F54` の既存範囲内）

素朴な pull-through（分子を $`\|\pi\psi_0\|`$、分解能を $`\|D_k^{-1}\|\le|k|^{-1}`$ で押さえる鎖）を
$`\int dk\|H_{\rm f}^{1/2}a(k)\psi_0\|^2`$ に当てると、$H_{\rm f}\le H(-k)=D_k+E_0-|k|$ から
$\lesssim\frac{e^2\mathcal K}{m^2}\int_0^\Lambda(1+E_0/r)dr$ となり、**第 1 項は収束**（`F54` の $\langle N\rangle_0$ より $|k|$ を 1 つ多く稼ぐ）、
**残る発散は $E_0$ に掛かる対数 1 つだけ**。作用素ノルム経路としてはこれ以上改善できない
（$H(-k)$ のスペクトル変数 $\lambda\ge E_0$ で $\sup_\lambda\lambda(\lambda-E_0+|k|)^{-2}=E_0|k|^{-2}$）。
`F54` の「生きている分岐 (a)」（$\nabla E(0)=0$ による相殺）が要る点まで同型なので、
**`F54` の再挑戦禁止範囲（T60）に既に含まれる。新しい F 番号を立てる必要は無い**（稿 `117_` §4.1）。
⚠ 鋭いのは**この経路**であって量そのものの限界ではない（**T90**）。

## F86（「$\nu_q$ の上帯の 2 次中心モーメント $\Sigma_q^\gt=\int_{[a/2,\infty)}(x-a)^2d\nu_q$ を $Ca\Lambda$ で押さえて (N110) を反証する」案 — **$aJ_q$ の必要形と十分形の取り違えによる誤り**。2026-09-13、w206、稿 `116_` §6 SR11）

**【親注記 2026-09-13】audit116 R7 の逆転監査で閉鎖は壊れなかった（独立再導出、T84 10 項目通過）。PATCH P19 適用済。**

**案の内容**（w206 が自分の敵対的セルフレビューの途中で立て、同じラウンドで自ら棄却した）:
$\sigma_q^2=\Sigma_q^\lt+\Sigma_q^\gt$（$\Sigma_q^\lt=\int_{[0,a/2)}(x-a)^2d\nu_q$）で、
(N110) から $\Sigma_q^\lt\le Ca\Lambda$ が出ると仮定し、さらに $\Sigma_q^\gt\le C'a\Lambda$ を示せば
$\sigma_q^2\le C''a\Lambda$ すなわち $\mathcal K\le\frac{3C''}2m\Lambda$＝(N111) となり、`E05-P62` 3.（(N111) は偽）と矛盾するので **(N110) が偽**になる、という kill 案。

**棄却の理由（厳密）**: 前提「(N110) ⟹ $\Sigma_q^\lt\le Ca\Lambda$」が**偽**である。
稿 `115_` 命題 115-1 により (N110) $\iff$ $`\sup_{\rm shell}a\,J_q\le C`$（$J_q=\int_{[0,a/2)}\frac{d\nu_q}{x+\Lambda}$）。ここから出るのは
```math
\nu_q\bigl([0,\tfrac a2)\bigr)\ \le\ \frac{(\frac a2+\Lambda)}{a}\,(aJ_q)\ \le\ C\Bigl(\frac12+\frac\Lambda a\Bigr)\ \le\ \frac32C
```
という**絶対定数による上界**であって、$\frac{C\Lambda}a$ ではない（後者は 115-1 の**粗い十分形**であり、(N110) から従う必要形ではない）。
したがって $\Sigma_q^\lt\le a^2\nu_q([0,\frac a2))\lesssim a^2$ までしか言えず、$a\ge\Lambda$ なので $a\Lambda$ との矛盾は出ない。
殻の上端では $a=2\Lambda\lambda$ で $a^2/(a\Lambda)=u$ が $\lambda$ とともに発散するので、差は定数因子ではない。

**残るもの**: この誤りは「115-1 の必要形（$aJ_q\le C$）と十分形（$\nu_q([0,\frac a2))\le\frac{C\Lambda}a$）の混同」という型で、
**同じ混同は低帯の質量を扱うどの発注でも起こりうる**。標的を書くときは必ず $aJ_q$（重みつき）で書き、
素の帯質量 $\nu_q([0,\frac a2))$ に読み替えないこと。

**⚠ この項は「$\Sigma_q^\gt$ による kill が不可能」とは言っていない。** 言うのは「上の 1 本の論証が成り立たない」ことだけである。
（$\Sigma_q^\gt$ を $J_q$ の重みつきの形に合わせて立て直す余地は残っている。**⚠ ただし audit116 R7 の 1 手の勘定では、重みつき全帯 $\int\frac{(x-a)^2}{x+\Lambda}d\nu_q\le C''a$ が示せても `E05-P66` 2.・3. の Jensen で出るのは $\bar x_q\ge\frac{\Omega_q}{C''}-\Lambda$、すなわち `E05-P66` 5. の必要条件の再現であって矛盾ではない。kill には $\bar x_q$ の**上界**が要り、在庫に無い。立て直しは kill-check 1 ラウンド上限で。**）

## F87（「$\pi^2$ を $`P_{\rm f}^2+e\{P_{\rm f},A\}+e^2A^2`$ に展開して $\pi^2\psi_0\in\mathcal Q(H_{\rm f})$ を出す」型は循環する — **同じ標的は交換子型で閉じた**ので、記録するのは展開型が使えないことだけ。2026-09-13、w210、稿 `118_` §6）

**【親注記 2026-09-13】audit119 R7 の逆転監査で閉鎖は壊れなかった（N 非有界ゆえ反例は有限 Λ でも生きる）。PATCH P4・P5 適用済。**

**⚠ 最初に**: 標的（$\psi_0\in D(H_{\rm f}^{3/2})\iff\pi^2\psi_0\in\mathcal Q(H_{\rm f})$）は**同じセッションで肯定的に解決した**（(研究ノート: `w210.PROVED.md`) (1)）。
本項は「展開型という**評価の型**が使えない」ことだけの記録で、標的そのものについての否定的記録ではない。

**この評価の型で足りないもの（2 つ）**

1. **$P_{\rm f}^2$ 項**: $`\|H_{\rm f}^{1/2}P_{\rm f}^2\psi_0\|\lt\infty`$ は `E05-F26`（$\psi_0\in D(H_{\rm f})\cap D(P_{\rm f}^2)$）から出ない。
   $H_{\rm f},P_{\rm f}$ は可換な掛け算作用素なので必要なのは $\int\omega|P|^4|\psi_0|^2\lt\infty$ だが、
   **各点不等式 $\omega|P|^4\le C(\omega^2+|P|^4)$ は偽**（$|P|=\omega\to\infty$ で左辺 $\omega^5$、右辺 $O(\omega^4)$）。
   $|P_{\rm f}|\le H_{\rm f}$ から素朴に評価すると $`\|H_{\rm f}^{5/2}\psi_0\|`$ が要り、さらに悪化する。
   （**1 冪だけなら救える**: $`\|H_{\rm f}^{1/2}P_{{\rm f}\mu}\Psi\|^2\le\|H_{\rm f}\Psi\|\|P_{\rm f}^2\Psi\|`$（CS）。稿 `118_` 補助命題 5.1。）**⚠ 射程（audit119 R7）**: これは「`E05-F26` から**出ない**」（抽象的な定義域の含意の否定）であって「$\psi_0$ について実際に無限」ではない。反例は有限 $\Lambda$ でも生きる（全光子を同一方向・$|k_i|\simeq\Lambda$ に取ると $|P|\simeq\omega\simeq n\Lambda\to\infty$ が同時スペクトル上で到達される。$N$ が非有界だから）: $`\|\Psi_n\|^2=n^{-6}`$ で $\Psi\in D(H_{\rm f})\cap D(P_{\rm f}^2)$ かつ $H_{\rm f}^{1/2}P_{\rm f}^2\Psi\notin\mathcal H$。
2. **$A^2$ 項**: $`\|H_{\rm f}^{1/2}A^2\psi_0\|`$ に $`\|H_{\rm f}^sa^\#(f)\Psi\|\le\|f/\sqrt\omega\|\|H_{\rm f}^{s+1/2}\Psi\|`$（`E05-P69`）を 2 回当てると
   右辺に $`\|H_{\rm f}^{3/2}\psi_0\|`$ が現れ、**結論そのものを仮定する循環**になる。
   $`\|H_{\rm f}^{3/2}\psi_0\|\le C_\Lambda(\cdots)+\epsilon\|H_{\rm f}^{3/2}\psi_0\|`$ 型の吸収に持ち込もうとしても、
   $C_\Lambda$ は小さくできない（$\kappa$ は $\Lambda$ とともに増える）ので $\epsilon\lt1$ が保証されない（係数は $`\frac{e^2}{2m}\sum_\mu\|u_{\cdot\mu}/\sqrt\omega\|^2=\frac{e^2\Lambda}{12\pi^2m}`$。$e^2\Lambda/m$ が小さければ $1$ 未満にはなるので「展開型は常に不可能」ではない）。**⚠ さらに第 2 の障害（audit119 R7）**: 吸収には**左辺の a priori 有限性**が要るが、展開型は $`\|H_{\rm f}^{3/2}\psi_0\|\lt\infty`$ をまだ持っていないので、$\epsilon\lt1$ が取れても吸収は正当化されない。**正則化 $T_\delta$ が本質的なのはこの 2 点目のためである。**

**代わりに効いた入力（1 つ）**: $\pi^2$ を**展開しない**こと。
正則化 $T_\delta=H_{\rm f}(1+\delta H_{\rm f})^{-1}$ との**交換子**の厳密等式 $`[T_\delta,a^\#(f)]=\pm R_\delta a^\#(\omega f)R_\delta`$ を使うと
$A$ は 1 回しか現れず、形状因子が $\omega u$（有限 $\Lambda$ で $L^2$）に化けて $\delta$ 一様な $H_{\rm f}^{1/2}$ 有界性が出る。
吸収は $H_{\rm f}^{3/2}$ ではなく $G_\delta^2=\langle T_\delta\psi_0,HT_\delta\psi_0\rangle$（各 $\delta$ で有限）に対して行う。詳細は (研究ノート: `w210.PROVED.md`) (1)。

**再挑戦禁止の範囲（限定）**: 「$\pi^2$ を 3 項に展開し、各項を `E05-F26` と `E05-P69` だけで $\mathcal Q(H_{\rm f})$ に入れる」鎖**だけ**。
展開型でも、$\pi$ 側（$\mathcal Q(\pi^2)$）の評価や他の入力を足す経路は対象外。

## F88（「Weyl 作用素の差分商 $\frac{W_s-1}s\psi_0$ の**形ノルム Cauchy 性**だけで型 B の (D-form) を閉じる」路は循環する — 同じ標的は正則化交換子で閉じたので、記録するのは**この路が使えないこと**だけ。2026-09-13、w212、稿 `120_D-formの残り.md` §3 の前置き）

**【親注記 2026-09-13】audit122 R6 で逆転できず（恒等式を独立再導出）。ただし「循環」は「同値で新情報なし」に狭めた（PATCH P10 適用済）。**

**何を試したか**。`E05-P41` 1. の証明（audit95 M3）が与える次の 2 つを出発点に取った:
$W_s=\mathrm e^{is\Phi(f)}$、$\Psi_s:=\frac{W_s-1}s\psi_0$ とおくと
(a) $`q_{E_0}(\Psi_s)=c_2:=\langle f,\omega f\rangle+\frac1{2m}\sum_\mu\|\Phi(q_\mu f)\psi_0\|^2`$ が**$s$ に依らず厳密に成り立つ**
（$q_{E_0}(W_s\psi_0)=sc_1+s^2c_2$、$c_1=0$、$q_{E_0}(\Psi_s,\psi_0)=0$ による）、
(b) $\Psi_s\to i\Phi(f)\psi_0$（$\mathcal H$、Stone）。
閉形式の下半連続性はここで $q_{E_0}(\Phi(f)\psi_0)\le c_2$（＝`E05-P41` 1.）しか出さない。**等号にするには
$(\Psi_s)$ が形ノルム $`\|\cdot\|_{+1}^2=q_{E_0}(\cdot)+\|\cdot\|^2`$ で Cauchy であればよい**——これを示そうとした。

**なぜ循環するか**。Weyl の群則 $W_s^*W_t=W_{t-s}$ と共役式
$W_s^*(H-E_0)W_s=(H-E_0)+sK_1+s^2K_2$（$K_1=i[H,\Phi(f)]$、$K_2=\frac1{2m}\sum_\mu\Phi(q_\mu f)^2+\langle f,\omega f\rangle$）から
```math
st\,q_{E_0}(\Psi_s,\Psi_t)=s\,g(t-s)+s^2\langle\psi_0,K_2W_{t-s}\psi_0\rangle,\qquad g(u):=\langle\psi_0,K_1W_u\psi_0\rangle,\ g(0)=0
```
（$(H-E_0)\psi_0=0$ で 3 項が落ちる。$s=t$ と置くと $q_{E_0}(\Psi_s)=c_2$ を再現する）。
$s,t\to0$ で $s/t\to r$ とすると右辺は $`g'(0)(1-r)+r\,c_2`$ に向かう。**$r$ に依らず Cauchy であるためには $g'(0)=c_2$ が要る。**
ところが
```math
g'(0)=i\langle\psi_0,K_1\Phi(f)\psi_0\rangle=-\langle\psi_0,[H,\Phi(f)]\Phi(f)\psi_0\rangle=q_{E_0}\bigl(\Phi(f)\psi_0\bigr)
```
であり、これは**示したい量そのもの**である。ゆえにこの路は「形ノルム Cauchy 性 ⟺ $q_{E_0}(\Phi(f)\psi_0)=c_2$」に帰着し、**新しい情報を生まない**。⚠ ただしこの帰着自身が $\Phi\psi_0\in D(H)$ を使う形式的操作であり、厳密になるのは補題 120-2 の**後**である。「路が数学的に不可能」とは言えない（audit122 R6）。
（下半連続性は片側しか与えない、という `E05-P41` 3. の射程注記の理由をこの計算が明示している。）

**転進先と結果**。Weyl を捨て、`E05-P73` と同型の**正則化交換子**（$R_\delta=(1+\delta H_{\rm f})^{-1}$）で
$\Psi_\delta=\Phi(f)R_\delta\psi_0\in D(H)$ を作り、$H$ の閉性で渡す路に替えたところ、$\pi$ 側
（$\pi_\mu\psi_0\in\mathcal Q(H_{\rm f})$）と合わせて**同じ標的が閉じた**（(研究ノート: `w212.PROVED.md`) の (1)(2)(3)、稿 `120_` §2〜§4）。
**したがってここに記録するのは「Weyl の差分商の形ノルム Cauchy 性だけで攻める路が使えない」ことだけである**（標的は生きている）。

**⚠ 射程**: 本項は $\Phi(f)\psi_0$ の形式定義域の問題について何も否定しない。
`E05-P41` 1. の Weyl 経路そのもの（不等式の向き）は有効であり、そこは動かない。オッズは動かない（T49）。

## F89（$H_{\rm e}$ の自己共役性に**使えない** 3 つの道。主張本体は `E05-P?`＝w214 で別途成立している）

**【親注記 2026-09-13】audit123 R6 で逆転できず（3 項維持）。「共通定義域の 2 自己共役作用素の平均だから自己共役」は明示反例で偽（周期／反周期 i d/dx、共通定義域 H¹₀）。PROVED.md にこの型の汚染なし（audit123 が grep）。**

**記録の性質**: これは方針の閉鎖ではない。**標的（$H_{\rm e}$ が $D(H_0)$ 上で自己共役）は同じセッションで証明済**
（(研究ノート: `w214.PROVED.md`)、稿 `122_H_eの自己共役性.md`）。ここに書くのは、**次に同じ問いを見る体が同じ穴に落ちないための、
使えない 3 つの道の記録**である。日付 2026-09-13、w214（監査の型）、稿 `122_` §1・§7 (R1)・§7 (R9)。

1. **⛔（偽の近道。最重要）「`E05-F26` により $H(0;e)$ と $H(0;-e)$ は同じ $D(H_0)$ 上で自己共役。ゆえにその平均 $H_{\rm e}$ も
   $D(H_0)$ 上で自己共役」は成り立たない。** 共通定義域上の 2 つの自己共役作用素の平均（和）は一般に**対称であるだけ**で、
   閉とも自己共役とも限らない。**この 1 行を書いた稿があれば訂正が要る。** 正しくは、$H_{\rm e}$ の摂動 $W=\frac{e^2}{2m}\sum_\nu A_\nu(0)^2$ が
   **非負**であることを使う独立の議論が要る（稿 `122_` §3〜§5）。
2. **⛔「原典 Hiroshima 2007 §2.2 の Thm 2.2 の証明を、線形項 $`\{P_{\rm f},A\}`$ を落とした $H_{\rm e}$ に写す」道は存在しない。**
   原典 p.12 の逆向き評価 (2.7) $`\|H_0F\|\le C\|(H+1)F\|`$ は、逐語「**In [30, 31] it is proved that there exists a constant $C$ such that**」
   とあるとおり**他論文からの引用**で、§2.2 の中に写すべき計算が無い。p.9 に書かれている線形項の相対有界性は**順向き**（$H$ を $H_0$ で押さえる）
   だけで、相対限界の小ささは主張されていない。**「$H_{\rm e}$ の方が易しい」のは正しいが、易しさの所在は「原典の段が易しくなる」ことではなく
   「別の（より初等的な）道が開く」ことである。**（PDF p.7〜12 を `Read` で直読して確認。要約経由でない。T91。）
3. **⛔ 素朴な Kato–Rellich（$W$ を $H_0$ の摂動と見て 1 回適用）は大きい $e$ で通らない。**
   $`\|W\Phi\|\le a_W\|H_0\Phi\|+b_W\|\Phi\|`$、$a_W=\frac{e^2\Lambda}{2m\pi^2}(2+\frac1{\sqrt2})$ で、
   $a_W\lt1$ は $e$（と $\Lambda$）が小さいときだけ。**次に要る入力**は「$\theta$ に一様な逆向き評価」であり、これが入れば
   Kato–Rellich を**$\theta\in[0,1]$ の 1 歩ごとに有限回**使って $\theta=1$ に到達できる（稿 `122_` §5）。
   なお $A(0)^2\ge0$ の正値性だけでは **KLMN（形式）までしか行かず、作用素定義域が $D(H_0)$ に留まることは出ない**。

**⚠ 併せて記録（壊しに行って失敗した攻撃。稿 `122_` §7 (R9)）**
- 「$H_{\rm f}^{1/2}|P_{\rm f}|\le\epsilon P_{\rm f}^2+\frac1{2\epsilon}H_{\rm f}$ で $H_{\rm o}$ を $H_0$ **無限小**相対有界にする」——
  係数 $\max(\epsilon m,\frac1{2\epsilon})$ は $\epsilon$ について下に有界（最小値 $\sqrt{m/2}$）なので**無限小にならない**。
  $H_{\rm o}$ は $H_0$ 相対有界だが相対限界 $0$ ではない。
- 「$W$ を $W(1+sW)^{-1}$ で正則化して単調形式収束 + $s$ 一様評価」——正則化が二重交換子の構造を壊し、逆向き評価が $s$ 一様に取れない。
- 「$H_{\rm e}$ は $H(0;e)$ のパリティセクターへの**圧縮**（$H_{\rm e}=\Pi_{\rm ev}H\Pi_{\rm ev}\oplus\Pi_{\rm odd}H\Pi_{\rm odd}$）だから、
  圧縮の一般論で済む」——**そのような一般論は無い**。自己共役作用素の圧縮は $\Pi D(H)$ 上で対称なだけで、
  形式圧縮の定義域は $\Pi D(H)$ より真に大きいのが普通である。

## F90（「稿 `118_` の吸収論法を、交換子を $\Phi_\delta$ 側に置いたまま $s\gt1$ に繰り上げる」型は冪が足りない — **同じ標的は交換子を $\pi_\mu\psi_0$ 側へ移す型で閉じた**ので、記録するのは素朴な向きが使えないことだけ。2026-09-13、w215、稿 `123_` 注 123-4b・§6 SR8）

**【親注記 2026-09-13】audit125 R5 で逆転できず（冪 2s−1/2 を独立検算、補間でも同閾値）。同じ標的は移項型（E05-P82）で得られている。**

**何を試したか**: 正則化子を $S=g_{s,\delta}(H_{\rm f})\approx H_{\rm f}^s$ に上げ、稿 `118_` (4.2) の一般形

$$2mG_\delta^2=2mE_0\|\Phi_\delta\|^2+e\sum_\mu\langle C^S_\mu\Phi_\delta,\pi_\mu\psi_0\rangle-e\sum_\mu\langle\pi_\mu\Phi_\delta,C^S_\mu\psi_0\rangle$$

の第 2 項を、稿 `118_` と**同じ向き**（$C^S_\mu$ を $\Phi_\delta$ に作用させたまま Cauchy–Schwarz）で評価した。

**何が足りないか（冪の勘定 1 行）**: $g_{s,\delta}$ の交換子は $\omega\lambda^{s-1}$ の重みを持つので
$`\|C^S_\mu\Phi_\delta\|`$ は $`\|H_{\rm f}^{s-1/2}\Phi_\delta\|\approx\|H_{\rm f}^{2s-1/2}\psi_0\|`$ を要求する。
吸収に使える量は $`G_\delta\approx\|H_{\rm f}^{s+1/2}\psi_0\|`$ までなので、成立条件は $2s-\frac12\le s+\frac12$、すなわち **$s\le1$**。
$s=\frac32$（標的の $\psi_0\in D(H_{\rm f}^2)$）では、目標より**半段上**の $`\|H_{\rm f}^{5/2}\psi_0\|`$ を先に要求してしまう。

**次に要る入力はちょうど 1 つだった**: $`\|H_{\rm f}^{s-1/2}\pi_\mu\psi_0\|\lt\infty`$。
$C^S_\mu$ が歪自己共役（$S$ 有界自己共役・$A_\mu(0)$ 自己共役）なので第 2 項を $\langle\Phi_\delta,C^S_\mu\pi_\mu\psi_0\rangle$ に移すと、
要求量がこれに下がる。$s=1$ の段の副産物（E05-P81＝$\pi_\mu\psi_0\in D(H_{\rm f})$）がちょうどこれを供給し、
以後は $\psi_0$ の冪と $\pi_\mu\psi_0$ の冪を**一緒に**繰り上げる帰納で全段が回る。

**射程**: 本項は「稿 `118_` の素朴な向きの繰り上げ」についてのみの記録である。
$\psi_0\in D(H_{\rm f}^2)$ そのものについては否定的なことを何も言わない（**同じ標的は移項型で得られている**）。
$\Lambda$ 一様性・$N$・各点版 (D-form) についても何も言わない。

## F91（型 A の (D-form) を「芯上の等式を $H$ のグラフノルムで閉包へ延ばす」筋で正当化する道は、向きが逆で通らない。代替は共役の縮小）

**【親注記 2026-09-13】audit124 R5 で逆転できず。理由の 1 文（芯の列で近似できない）は稿の芯性と矛盾するため差し替え済（正しい理由は循環＋グラフノルム連続性の不在）。**

**日付・出所**: 2026-09-13、w216。稿 `124_各点pull-throughと芯.md` 注 4-a・§7 SR3。

**内容**: `E05-P46` の仮定欄は型 A の (D-form) を
「$H$ の芯上の等式を $H$ のグラフノルムで閉包へ延ばす筋で、芯の同定は未記述」と記していた
（(研究ノート: `w216_各点pull-throughと芯の同定.md`) の (b) も同じ枠付け）。
**この筋では正当化できない。** 理由は 2 つある: (i) $a_\lambda(k)\psi_0\in D(H(-k))$ は「延長」の前提ではなく**結論**であり、
前提に置くと循環する。(ii) $\mathcal F_{\rm b\infty}$ は確かに $H$ の作用素芯なので $\Phi_n\to\psi_0$（$H$ のグラフノルム）は取れるが、
そこから $a_\lambda(k)\Phi_n\to a_\lambda(k)\psi_0$（$H(-k)$ のグラフノルム）へ渡る**連続性が無い**
（各点消滅核は $H$ のグラフノルムについて有界でない）。

**代替（成立した道）**: 芯は「等式の延長」ではなく「**共役の縮小**」に使う。
$B(k):=\bigl(H(-k)-E_0+|k|\bigr)\restriction_{\mathcal F_{\rm b\infty}}$ とおくと、`E05-F28`＋`E05-F26` から
$\overline{B(k)}=H(-k)-E_0+|k|$、したがって $B(k)^*=H(-k)-E_0+|k|$。
弱形の等式 $\langle B(k)\Phi,a_\lambda(k)\psi_0\rangle=\langle\Phi,G_\lambda(k)\rangle$（$\forall\Phi\in\mathcal F_{\rm b\infty}$）は
共役作用素の定義そのものなので、$a_\lambda(k)\psi_0\in D(H(-k))$ が直ちに出る。
詳細は稿 `124_` §3・§4。

**射程**: 本項は**証明の筋についての記録**であって、型 A の (D-form) が未解決だという意味ではない
（型 A は (研究ノート: `w216.PROVED.md`) の命題 3.・4. で満たされる）。
また型 B（`E05-P78`）・型 C（`E05-P51`）・型 A′（2 光子）の枠付けについては何も言わない。

---

## F92（$O_A$ の対消滅評価の入力を**状態に一様な**不等式で置き換える型の検査 — $`\|N_S^{1/2}\psi\|`$ 型・$`\|\rho_S\|_{op}`$ 単独型・「窓の台制限で $\sqrt{f_*}$」型の 3 つは**許容クラス $W_{S,Q}$ の中の**最小反例で偽、$`\|\gamma\|_{op}`$ 型は**成否未決**だが $\beta$ 一様の最悪ケースで利得 0。2026-09-13、w218、稿 `127_` §5。監査 audit128）

**【親注記 2026-09-13】audit128 R3・R5 の逆転監査: (a)(b) の反例は許容クラス外、(c) は含意の飛躍だったが、監査側が窓クラス内の代替反例を構成して結論は回復（PATCH 適用済）。(d) は未決のまま（見出しの量化子を訂正）。**

**これは $O_A$ についての閉鎖ではない。** 否定されるのは「**全 $\psi\in D(N_S)$ で成り立つ**不等式」であって、
$\psi_0$ 固有の評価は否定されない（T60・T90: 証明の限界と量の限界を書き分ける）。
実際、(研究ノート: `w218.PROVED.md`) の 1. は $\psi_0$ 固有の入力 $`\|\mathcal T_{\psi_0}\|_W`$ 1 つに載せ替えており、そこは生きている。

**記号**: $`F_\gamma^*=\frac12\iint\bar\gamma\,aa`$（対消滅）、$`\mathcal M=\|N_S\psi\|`$、$\rho_S$ は殻の 1 体密度、
$\Gamma^{(2)}$ は 2 体密度、$f_*$ は窓の占有率、$`\varsigma=\|\beta\|_{op}^2/\|\beta\|_2^2`$（**literal 規約。T58**）。

**(a) $`\|F_\gamma^*\psi\|\le C\|\gamma\|_2\|N_S^{1/2}\psi\|`$ なる絶対定数 $C$ は存在しない。**
**窓 $W_{S,Q}$ の中の**背中合わせ 2 モード $\gamma=\frac1{\sqrt2}(\phi_1\otimes\phi_2+\phi_2\otimes\phi_1)$（$`\|\gamma\|_2=1`$）、$\psi=|n,n\rangle$ で左辺 $=\frac n{\sqrt2}$、
$`\|N_S^{1/2}\psi\|=\sqrt{2n}`$ ⟹ 比 $\frac{\sqrt n}2$ は非有界（`246_` C、$n=1..12$）。
⟹ **w217 §7 が挙げた代替入力候補「$`\|N_S^{1/2}\psi_0\|`$」は、$\psi$ 一様な差し替えとしては使えない。**

**(b) $`\|F_\gamma^*\psi\|\le C\|\gamma\|_2\|\rho_S\|_{op}`$ も、$`\|\Gamma^{(2)}\|_{op}\le C\|\rho_S\|_{op}^2`$（Wick 分解型）も成り立たない。**
(a) と同じ**窓の中の** $\gamma$ と $`\psi=\sqrt{1-\epsilon}\,\Omega+\sqrt\epsilon\,|n,n\rangle`$ で前者の比は $\frac1{\sqrt{2\epsilon}}$（`246_` D で $\epsilon=10^{-5}$ に $223.6$）、
後者は $\epsilon n^2$ 対 $\epsilon^2n^2$ でいずれも $\epsilon\to0$ に非有界。
⟹ **準自由性を仮定しない限り 2 体の入力を 1 体の入力に落とせない。** w217 §7 の候補「$`\|\rho_S\|_{op}`$」も同様に不可。**否定したのは作用素ノルムの $\psi$ 一様版だけで、$\psi_0$ が準自由に近いことから来る誤差項つきの近似 Wick 評価は否定していない**（audit128 R3-4）。

**(c) 窓の台制限だけからは $\sqrt{f_*}$ の利得が出ない。**
$`\|\mathcal T_\psi\|_W\le\frac12\sqrt{f_*}\,\mathcal M\|\rho_S\|_{op}^{1/2}`$ 型の $\psi$ 一様な不等式は偽。
窓の中の 1 つの対に台を持つ $\gamma$ と、**光子数を重ね合わせた** $\psi=\frac1{\sqrt2}(|1_1,1_2\rangle+|1_1\rangle)$ で $`\|\mathcal T_\psi\|_W`$ は $f_*$ に依らず $O(1)$
（有限模型 $f_*=0.125$ で $`\|\mathcal T_\psi\|_W=0.35355\gt\frac12\sqrt{f_*}\mathcal M\|\rho_S\|_{op}^{1/2}=0.27951`$。`246_` E。中間段 $\langle\mathcal P_W\rangle_\psi\le f_*\mathcal M^2$ も同じ模型で偽で、その比が `241_` の $0.3536\gt0.1768$）。
**理由**: `E05-P37`・`E05-P38` の角 Schur が効くのは **c 数核 $M_W$ の作用素ノルム**であり、
ここで効かせたいのは**状態の 2 体分布**である。**言えるのは「窓からは $\psi$ 一様な因子 $\sqrt{f_*}$ は取れない」までで、「窓が状態に効かない」ではない**（T60。$\langle\mathcal P_W\rangle_\psi$ 自体が窓で切った状態量である）。

**(d) $`\|\gamma\|_{op}`$ 型は、成り立ったとしても $\beta$ 一様の最悪ケースでは利得 0。**
$`\|F_\gamma^*\psi\|\le C\|\gamma\|_{op}\|N_S\psi\|`$ は有限模型の乱択では反例が出なかった（最大比 $0.239$。**成否は未決**）が、
$\gamma=q_\nu\beta$ に使うと $\varsigma$ が戻る。`E05-P5` 射程 1.（audit69）により
**$\varsigma=O(1)$ は許容クラス $W_{S,Q}$ の中で実現する**（対蹠の 2 球帽に台を持つ低階数核）ので、
最悪ケースで $`\|\gamma\|_{op}\sim\|\gamma\|_2`$ となり冪は改善しない。**`E05-P44` が $\varsigma$ を消した利点を捨てることになる。**

**数値**: (研究ノート: `241_w218_pair_annihilation_inputs.py`)（seed 2410913、numpy、`conclusion: PASS`。
有限モード Fock $M=4$・総光子数 $\le6$。(a) は $n=2..6$ で予測 $\frac12\sqrt{n-1}$ と一致、
(b) は $\epsilon=10^{-5}$ で比 $144.3$、(c) は上記、(d) は乱択 300 本で反例なし）。
**有限模型で示せるのは「$\psi$ 一様な不等式の反例が存在する」ことだけで、$\psi_0$ については何も言わない（T64）。**

**この型で足りないもの（1 行）**: $\psi_0$ 固有の入力——**反跳 $\frac{|k+k'|^2}{2m}$ を保ったままの
$\langle N_S^2\rangle_0$（または窓の中の対の個数 $\langle\mathcal P_W\rangle_0$、$`\|\mathcal T_{\psi_0}\|_W`$）の非摂動評価**。
在庫より $\lambda^{-1/8}$（$\langle\mathcal P_W\rangle_0$ では $\lambda^{-1/4}$）だけ良ければ、
$`\|\rho_S\|_{op}\lesssim\alpha^2`$ と合わせて $O_A$ は窓つきで足りる。

**⚠ 窓からは稼げない（値の上でも）**: 2 光子オーダーの**値**で、低帯 $|k+k'|\le Q$ が $\langle N_S\rangle_0$ に占める割合は
$\lambda$ とともに緩やかに減少し 7 段で $0.347\to0.134$（最後の 1 段で $-2.8\%$。**「$\lambda$ に依らず」とは書けない**が、等方の球帽占有率 $2/\lambda=3.1\times10^{-5}$（$\lambda=65536$）には到底届かない）。
重みは背中合わせ配位に約 4400 倍集中している（(研究ノート: `241b_w218_twophoton_value_scan.py`)、`PASS`）。
**値は上界でも下界でもない（T88）**が、(c) の $\psi$ 一様な不可能性と同じ向きを指す。**稼ぐべきは窓ではなく反跳である。**

**再挑戦禁止の範囲**: (a)(b)(c) の形の**状態に一様な**不等式のみ。
$\psi_0$ 固有の評価、反跳保持型（`E05-P49`・`E05-P53`・`E05-P57` の型）、
光子数セクター構造を使う評価は**この記録の対象外で、推奨される**。

## F93（「奇部の第 3 片 $O_C$ を**場 2 本の 2 次形式** $\mathrm{Re}\langle\Phi(g)\psi_0,\Phi(h)\psi_0\rangle$ に書き換えて `E05-P32` 2.・`E05-P39` の真空支配に落とす」— **作用素恒等式としてこの還元は存在しない（Wick 次数 3 → 2 は不可）。あわせて $Z_\nu$ が（c 数を除き）**双線形＝Wick 次数 2** であることから、親の CCR 見積り $`\|Z_\nu^*\psi_0\|\lesssim\|\gamma\|_2\|N_S^{1/2}\psi_0\|`$ は成り立たず $`\|N_S\psi_0\|`$ になる（**⚠ 原因は光子数保存ではない。対型でも $N$ の冪は 1 である。audit130 R2-e**）**。2026-09-13、w219、稿 `128_` §2、audit129 R6）

**【親注記 2026-09-13】audit129 R6: 閉鎖は生存するが理由は誤同定だった（正しくは Wick 次数 3→2 の還元不能。光子数選択則ではない。偏極で dΓ は場の 2 次式に書ける）。PATCH P6 のうち規約注記（R6-c）と $N_S^{1/2}\to N_S$ の 1 行（R6-b 後半）は**未適用だったので audit130 が補った**（上の P9・P10）。**S1 差分監査は audit130 が完了**（(研究ノート) R2。主判定＝偏極・Wick 次数 3→2 の還元不能・射程はすべて成立。ただし見出しの因果句「光子数保存であることから」は誤帰属で訂正した）。**

**判定**: **作用素恒等式としての**還元の不存在（代数のみ、厳密）。値としての等式（ある $g,h$ で数値が一致する）を否定するものではない。

**（規約: 稿 `128_` §1 の $`F_\gamma=\frac12\iint\gamma\,a(k)a(k')`$ を採る。⚠ 正本 `77_` §1.1 は $`F=\frac12\iint\beta\,a^*a^*`$ で向きが逆＝$F^*$ が $-2$、$T_\nu$ が $+2$。変わるのは $Z_\nu$ の全体符号と $\mathcal K_\nu$ の転置だけで、以下の結論は不変。audit129 R6-c）** $F^*_\beta$ は光子数を $+2$、$T_\nu=F_{q_\nu\beta}$ は $-2$ 変えるので、$Z_\nu=[F^*_\beta,T_\nu]$ は**光子数を変えない成分しか持たない**:
```math
[F_\gamma,F^*_\beta]=\tfrac12\langle\beta,\gamma\rangle_{HS}I+\mathrm d\Gamma(\beta^*\gamma)\qquad(\beta,\gamma\ \text{対称核}).
```
ゆえに $`O_C=\frac e{2m}\sum_\nu\langle\{Z_\nu,A_\nu\}\rangle_0`$ は、c 数部分（$\langle A_\nu\rangle_0=0$ で落ちる）を除くと
「**光子数保存の双線形 $\mathrm d\Gamma(\mathcal K_\nu)$ × 場 1 本 $\Phi(u_\nu)$**」の 3 点関数であって、**場 2 本の 2 次形式ではない**。
したがって「$Z_\nu$ の対消滅を $A_\nu$ と組んで場 2 本の積にし、`E05-P39`（指数モーメント $\le$ 真空）・`E05-P32` 2. で真空値に落とす」という型の書き換えは成立しない。
同じ理由で「$Z_\nu^*\psi_0$ は対生成を $\psi_0$ に当てたベクトルで、そのノルムは $`\|\gamma\|_2\|N_S^{1/2}\psi_0\|`$ 型（CCR）」という見積りも成立しない。**⚠ ただしその理由は光子数保存ではない（audit130 R2-e）**: 対称核 $\gamma$ の Takagi 分解で $F_\gamma=\frac12\sum_j\mu_ja(e_j)^2$ とし、1 モード・$\gamma=f\otimes f$（$`\|f\|=1`$）・$\psi=|n\rangle$ を取ると $`\|F_\gamma\psi\|=\frac12\sqrt{n(n-1)}`$ に対し $`\|\gamma\|_2\|N^{1/2}\psi\|=\sqrt n`$ で、比は $\frac12\sqrt{n-1}\to\infty$。**すなわち対型（光子数を $\pm2$ 変える型）でも $N$ の冪は 1 であり、$N_S^{1/2}$ という基準線は初めから存在しない。**重くなる原因は $Z_\nu$ が線形（$a$ 1 本）ではなく**双線形**であることで、これが `E05-P44` 3. が $`\mathcal M=\|N_S\psi_0\|`$ を担ぐ理由であり、**`126_` §4.3 の $-\frac92$ の出所**でもある（audit129 R6-b）。

**根拠**: 稿 `128_OCのP38型.md` 補題 128-0（代数）。数値 (研究ノート: `242_w219_OC_trace_pairing.py`)（`c1b`: $Z_\nu$ の光子数変化成分は**厳密に 0**、`c1`: 構造の一致 $7.9\times10^{-15}$、`conclusion: PASS`）。
`E05-P42` 1.（$O_C$ が $\mathrm d\Gamma(K_\nu)$ と $`a^\#(u_\nu)`$ で書かれている）・`E05-P44` の記号行（$K_\nu=(q_\nu\beta)\overline\beta$）・`95_` §5 の型検査表（「$Z_\nu=[F^*,T_\nu]=$ c 数 $+\mathrm d\Gamma(K_\nu)$」）と整合する。

**⚠ 射程（過大に引用しないこと）**:
- **これは $O_C$ についての否定的判定ではない。** 消えたのは**この 1 つの書き換えの型**だけで、$O_C$ の一様上界の可能性については何も言わない。**⚠ 特に「場による表示が無い」とは言っていない**: 偏極公式 $`4a^*(f)a(f)=\Phi(f)^2+\Phi(if)^2-2\|f\|^2`$ により $\mathrm d\Gamma(\mathcal K_\nu)$ は場の 2 次式の線形結合で書けるので、$O_C$ は $`\sum\langle\{\Phi(f)^2,\Phi(u_\nu)\}\rangle_0`$ 型の**場だけの 3 点関数**として書ける。死ぬのは**2 次形式（場 2 本）への還元**だけである（audit129 R6-a）。**⚠ さらに、排除されるのは次数つき代数における恒等式である。$g,h$ を $\beta,u_\nu$ から決めたうえで等式は $\psi_0$ 上でのみ（回転不変性などを使って）成り立つ、という型は排除していない（audit130 R2-d）。**
- **`E05-P39` を $O_C$ に使う経路一般を排除しない。** `E05-P39` 射程 2. が言及する経路（$\Theta=JV$ 選択則で $\Pi$ 1 本の 3 点関数に落とし、運動方程式と二重交換子で $C_4$ を部品に $p=3/2$。audit94 II-d2〜II-d4、未昇格）は**別の型**で、本項は触れていない。
- **`E05-F10`（パリティ選択則: 偶な試行核は分子が恒等的に 0）とは別の選択則である**（あちらは $\beta$ の偶奇、本項は光子数）。
- 代替の型は稿 `128_` 命題 128-1（トレース類 × 作用素ノルムの Hölder 対）で、そちらは成立する（(研究ノート: `w219.PROVED.md`)）。

## F94（「ゲート内の状態は殻光子を持つ」から $`\|\Pi_{\mathcal G}\psi_0\|^2\le\langle N_S\rangle_0`$ とする型 — 最小反例で偽。2026-09-13、w221、稿 `129_` §7-6）

**【親注記 2026-09-13】audit131 R5: 2 件とも逆転できず棄却は妥当（T84 10 項目通過）。末尾の過大主張 1 文に訂正を併記済。**

**棄却した主張**: ゲート $`\mathcal G=\{|P_{\rm f}+q|\le Q\}`$（$|q|=\kappa\Lambda$、$\kappa\in[\frac12,1]$、$Q=\sqrt{2m\Lambda}$）の中の状態は
殻 $S=[\Lambda/2,\Lambda]$ の光子を持つので $`\|\Pi_{\mathcal G}\psi_0\|^2\le\langle N_S\rangle_0`$ と押さえられる、という型。

**反例**: $\Pi_{\mathcal G}$ の像は $|K|\ge|q|-Q$ を課すだけで、個々の光子運動量には何も課さない。
$|k_i|=0.4\Lambda$（殻の外）の光子 3 本をほぼ同方向に揃えれば $|K|\simeq1.2\Lambda$ となりゲートに入る。
すなわち $\Pi_{\mathcal G}$ の像 $`\not\subset\{`$殻光子を 1 本以上持つ状態$`\}`$ であり、上の不等式は成り立たない。

**代わりに成り立つもの**: $H_{\rm f}\ge|P_{\rm f}|$（$n$ 光子セクターで対角）と $[\Pi_{\mathcal G},H_{\rm f}]=0$ から
$`\|\Pi_{\mathcal G}\psi_0\|^2\le\Theta_{\mathcal G}/(|q|-Q)`$（`E05-P?` (1) 3.）。自己無矛盾（吸収）は
$`\|\Pi_{\mathcal G}\psi_0\|^2`$ ではなく $V_1$ の**消滅部の内側** $|k'-q|\le2Q$ から取り出せる（同 (2)）。

**射程**: 本項が否定するのは上の**包含関係を根拠とする型**だけで、$`\|\Pi_{\mathcal G}\psi_0\|^2`$ を別の経路で
$\langle N_S\rangle_0$ と結ぶ可能性を否定しない。

---

## F95（$\mathcal G^\perp$ 上の反跳下界を $A^2$ の 2 次形式評価から作る型 — 定数項がゲートのギャップを飲む。2026-09-13、w221、稿 `129_` §5.1）

**【親注記 2026-09-13】audit131 R5: 2 件とも逆転できず棄却は妥当（T84 10 項目通過）。末尾の過大主張 1 文に訂正を併記済。**

**棄却した主張**: $\Pi_{\mathcal G}^\perp$ 上では $\frac{(\pi+q)^2}{2m}\ge\frac12\frac{(P_{\rm f}+q)^2}{2m}-\frac{e^2A(0)^2}{m}$ を使えば
$H(-q)-E_0\gtrsim\frac{(P_{\rm f}+q)^2}{2m}\ge\frac{Q^2}{2m}=\Lambda$ が出て、$`\|R(q)\Pi^\perp\|`$ が改善する、という型。

**壊れる理由（算術）**: $A(0)^2$ の 2 次形式評価 $\frac{e^2}{m}A^2\le\frac{e^2}{m}\bigl(\frac{\Lambda}{4\pi^2}H_{\rm f}+\frac{\Lambda^2}{8\pi^2}\bigr)$ の
**定数項**が $\frac{\alpha\Lambda^2}{2\pi m}=\frac{\alpha\lambda}{2\pi}\cdot m\lambda$ であり、ゲートのギャップ $\frac{Q^2}{2m}=m\lambda$ に対して
$\alpha\lambda\gt2\pi$ で大きい。窓 $\alpha^2\sqrt\lambda\le\kappa_0$ は $\lambda\le\kappa_0^2\alpha^{-4}$ しか課さないので、
**窓の中の $\lambda\gt2\pi/\alpha$ の部分（$\Lambda\to\infty$ で問題になる領域のすべて）でこの不等号は成り立つ。**
すなわち**ゲートの尺度 $Q=\sqrt{2m\Lambda}$ は場の尺度 $\sqrt\alpha\Lambda$ より下**である。

**第 2 の障害（下界を認めても足りない）**: $X(q)+|q|\ge Y$（$Y=\theta\frac{(P_{\rm f}+q)^2}{2m}+|q|-C_0m$）から出るのは
$`\|R(q)\phi\|\le|q|^{-1/2}\|Y^{-1/2}\phi\|`$ までで、$`\|R\phi\|^2\le\|Y^{-1}\phi\|^2`$ は出ない（逆数の 2 乗は作用素単調でない）。
$`\phi=\epsilon\!\cdot\!\pi\psi_0`$ の重みが $|P_{\rm f}+q|\sim\Lambda$ に $\mathcal K\sim\alpha\Lambda^2$ あるため、この補間版は $\alpha\lambda^{-1}$ 止まりで、
要求 $\alpha\lambda^{-3/2}$ に $\sqrt\lambda$ 足りない（2 光子オーダーの値は $\alpha\lambda^{-2}$ なので、落ちているのは評価であって値ではない）。

**この型に足りないもの / 次に要る入力 1 つ**: **(N-loc)**
$`\|R(q)\mathbf 1\{\rho\lt|P_{\rm f}+q|\le2\rho\}\|\le\frac{C_{\rm loc}}{|q|+\theta\rho^2/2m}`$（$Q\le\rho\le2\Lambda$、$q\in S_*$）。
これは「反跳の下界」と「局在と $R(q)$ の交換」を同時に要求する新しい入力で、`E05-F20`（天井）・`F23`（非負性）・
`F26`・`F28` のどれからも出ない。これ 1 つから帯分割（位相体積 $(\rho/Q)^3$ を掛けると最小の $\rho=Q$ が支配）で
`E05-P?` (2) の (H-recoil) が出る。

**射程**: 本項が否定するのは $A^2$ の定数項を素朴に使う経路と、下界のみからの補間であって、
反跳下界そのものの真偽にも、別経路での $\mathcal G^\perp$ 評価にも触れない。**⚠ 訂正（audit131 R4・R5、2026-09-13）: 上の「これ 1 つから帯分割で (H-recoil) が出る」は成立しない。帯分割は「位相体積 $(\rho/Q)^3$ の $\rho$ 一様版」を追加の入力として要し（$\rho=Q$ の場合ですらそれは稿 129_ §3 の結論）、さらに $P_{\rm f}$ が非有界なので (N-loc) の $\rho$ の範囲を $\rho\ge Q$ 全体に広げないと $\rho\gt2\Lambda$ の尾が閉じない。要る入力は 2 つである。**

## F96（ゲート重みの中心減衰仮定を「半径 ＝ 中心の下限」で書く型 — 左端で真空が入り、上界の仮定が $\langle N\rangle_0\ge\frac12$ という下界を含意する。2026-09-13、w222、稿 `130_` §1）

**【親注記 2026-09-13】w222。未監査（audit132 で逆転監査）。**

**検査した型**: 中心 $|P|$ について減衰するゲート重みの仮定を
```math
\bigl\|(N+1)^{1/2}\,\Pi_{P,\rho}\,\psi_0\bigr\|^2\ \le\ c_G\,\alpha^2\lambda^{1/2}\bigl(\rho/|P|\bigr)^{p}\qquad(|P|\ge\rho)
```
の形（**半径 $\rho$ と中心の下限が同じ**）で置く型。2026-09-13 に `PROVED.md` `E05-P88` と稿 `129_` §3.1 へ
$\rho=2Q$・中心 $|P|\ge2Q$ として反映されたのがこの型である。

**判定**: **この型は採れない。冪をどれだけ急にしても直らない。**
左端 $|P|=\rho$（閉条件なので範囲に含まれる）でゲートの像は真空を含む（$P_{\rm f}\Omega=0$、$|0+P|=\rho\le\rho$）ので
```math
\bigl\|(N+1)^{1/2}\Pi_{P,\rho}\psi_0\bigr\|^2\ \ge\ \bigl|\langle\Omega,\psi_0\rangle\bigr|^2=1-\bigl\langle\mathbf 1\{N\ge1\}\bigr\rangle_0 ,
```
右辺の仮定値は左端で $c_G\alpha^2\sqrt\lambda\le c_G\kappa_0$（窓の中）。ゆえにこの仮定は
```math
\langle N\rangle_0\ \ge\ \bigl\langle\mathbf 1\{N\ge1\}\bigr\rangle_0\ \ge\ 1-c_G\kappa_0\ \Bigl(\ge\tfrac12\ \text{if}\ c_G\kappa_0\le\tfrac12\Bigr)
```
を**含意する**——上界を作るための仮定が、全光子数の $O(1)$ の**下界**を窓の中で一様に要求してしまう。
減衰の冪 $p$ は左端 $|P|=\rho$ では何も効かない（$(\rho/|P|)^p=1$）ので、**冪の修正では直らない**。

**射程（何が言えて何が言えないか）**:
- **「偽」とは書かない。** 逐語の反証には「$\alpha\to0$（$\Lambda$ 固定）で $\langle N\rangle_0\to0$」が要り、それは公理表
  （`E05-F20`・`F23`・`F26`・`F28`）に無い。言えるのは「向きが逆の内容を含意する」「支持する数値が無い」ことである。
- **数値はこの型を支持していない**: (研究ノート: `249_audit131_*`)・`250_w222_*` が測るのは**半径 $Q$・2 光子セクター**の量で、
  真空（0 光子）の寄与は原理的に現れない。T88 の変種「測った量 ≠ 仮定した量」が、audit131 の冪の修正後も残っていた。
- 先行する `F94`（「ゲート内の状態は殻光子を持つ」型）とは別の失敗様式である。`F94` は**十分条件が偽**、こちらは
  **仮定の範囲の左端が退化している**（$\rho\le|P|/2$ に狭めれば消える）。

**代わりに採る形**: 半径を中心の下限の半分以下にする。$\rho\le|P|/2$ なら像で $|K|\ge|P|-\rho\ge\rho\gt0$ となり真空も
「$K=0$ の 1 光子」も入らない。稿 `129_` の証明は半径 $2Q$ を一度も使わないので、$\rho=Q$・$|P|\ge2Q$ で十分である
（稿 `130_` §1.2・§4、(研究ノート: `w222.PROVED.md`)）。

**この型の検査で分かった一般則（次の発注で使える）**: **ゲート射影 $\Pi_{P,\rho}$ を含む上界の仮定を書くときは、
中心の範囲を $|P|\ge2\rho$ に取る（余裕をもった形を既定にする）。**⚠ 射程（audit132 R5）: 本項が壊したのは**閉じた左端 $|P|\ge\rho$ の型**だけである。開条件 $|P|\gt\rho$ にすれば $K=0$ は像に入らないので真空の議論は効かず、$P_{\rm tot}=0$ ファイバーには赤外発散が無い（$`\int_{|k|\le\delta}\|a(k)\psi_0\|^2d^3k=O(\delta^2)`$）ので $|P|\downarrow\rho$ でも原子は拾わない。実際、半径 $2Q$・開条件 $|P|\gt2Q$ でも稿 `129_` の証明は通る（(c) の遠方が厳密不等式だから）。**半径 $Q$ 版を採るのは「より弱い仮定だから」であって「開条件では駄目だから」ではない。**
$|P|=\rho$ ちょうどの点は $\psi_0$ の真空成分をそのまま拾う。

## F97（$O_C$ を $\hat\Xi\le\mathcal M$（`E05-P86` 2.＝`E05-P44` 3.）の経路で窓つき一様化する型に、**何が足りないか**。w225、2026-09-14）

**【親注記 2026-09-14】audit133 R5 で逆転できず。値の見通しから「仮定下の厳密な隔たり λ{3/8}」に格上げ（PATCH P18 適用済）。**

**⚠ これは閉鎖の主張ではない。** 書いてあるのは「この評価の型では何が足りないか」と「次に要る入力」だけである。
**FAILED に載せるかは親が決め、載せる前に必ず「これを壊しに行け」の逆転監査（2 段目 `監査の型`）を通すこと。**

**対象の型**: `E05-P86` 2.（$`\hat\Xi\le\mathcal M\,U`$、$`\mathcal M=\|N_S\psi_0\|=\langle N_S^2\rangle_0^{1/2}`$）を
`E05-P86` 1. に入れて $O_C$ を窓つき一様化する経路（＝`E05-P44` 3. の経路そのもの）。

**足りないもの（1 行）**: この型の要求は `126_` §4.3 により $n_M-4p_M\ge\frac32$、
$n_M=1$ 固定なら $\mathcal M\lesssim\alpha\lambda^{-1/8}$（**$\lambda$ について減少**）である。一方
$N_S^2\ge N_S$（整数値作用素）から**厳密に** $\mathcal M\ge\langle N_S\rangle_0^{1/2}$ であり、
$\langle N_S\rangle_0$ の先頭オーダーの**値**は $`0.18\,\alpha^2\sqrt\lambda`$（w218 `241b_`、w224 `253b_`、
w225 `254_w225_Hdens_phase_volume_result.json`、3 系統一致）なので、$\mathcal M$ の値は $`0.42\,\alpha\lambda^{1/4}`$ で
**$\lambda$ 増大**であり、要求と向きが逆になる。**⟹ この型は、どんな各点密度型の仮定を置いても届かない見通しである。** **さらに強く（audit133 E-2）**: 補題 131-D の証明はそのまま $S\times S$ 全体の上界でもあるので、(H-dens)＋(H-dens′-a) の下で**厳密に** $\mathcal M^2=\langle N_S(N_S-1)\rangle_0+\langle N_S\rangle_0\le(\frac76C_{\rm p}+0.020984C_{\rm d})\alpha^2\sqrt\lambda$、すなわち $`\mathcal M\le1.08\sqrt{C_{\rm p}+0.018C_{\rm d}}\,\alpha\lambda^{1/4}`$。**密度型の仮定から取り出せる最良の上界が $\alpha\lambda^{1/4}$ であり、要求 $\alpha\lambda^{-1/8}$ と $\lambda^{3/8}$ 開くことが（値ではなく）仮定の下で厳密に言える。** それでも「不可能」ではない（別種の相殺からより良い上界が出る可能性は排除されない）。

**⚠ 「不可能」とは書かない（T88）。** 上は**値からの見通し**であって判定ではない。
$\langle N_S\rangle_0$ の非摂動**下界**は在庫ゼロで、$\mathcal M$ の非摂動下界も無い。
**値が要求と逆向きであることは反証にならない**（`E05-P65`・`F84` と同型）。

**次に要る入力（1 つ）**: `E05-P86` 3. の経路 B（$`\|\Xi_\nu\|_{op,S}\le\|\rho_S\|_{op}^{1/2}\Upsilon_\nu`$）へ載せ替え、
$`\|\rho_S\|_{op}`$ を**トレース（$\langle N_S\rangle_0$）ではなく作用素ノルムとして**押さえる入力。
w225 はこれを $\rho$ の**非対角減衰**(H-dens′-b) から得た（稿 `131_` 補題 131-C、$`\|\rho_S\|_{op}\le\frac{8C_{\rm b}}{\pi^2}\alpha^2\lambda^{-1/2}`$）。
**⟹ 律速は「トレース型 vs 作用素ノルム型」であって「$\mathcal M$ vs $`\|\rho_S\|_{op}`$」ではない**
（`126_` §4 の訂正をさらに 1 段精密化する。$\mathcal M$ 側にはトレース型しか無いので上げようがない）。

**副次的に記録する罠（w225 のセルフレビュー S2・S3。同じ日に両方向で踏んだ）**
- **$\Upsilon_\nu$ の $G_p$ は Schur ではなく $\mathrm{tr}$ で押さえる。** $G_p$ は Gram 行列（$\ge0$）で本質的にランク 1 なので
  $`\|G_p\|_{op}\le\mathrm{tr}\,G_p`$ が鋭く、Schur は $\sqrt\lambda$ 損をする（$O_C$ が $+\frac12$ から $-\frac12$ に落ちる）。
- **$R_{\mathcal U}$ の対項 $\tilde M$ は $\mathrm{tr}$ ではなく Schur で押さえる。** $\tilde M$ は殻上の帯行列で
  ランクが $(\Lambda/Q)^3\sim\lambda^{3/2}$ あり、$\mathrm{tr}$ は $\lambda^{?}$ 損をする（$n-4p$ が $0$ から $-2$ に落ちる）。
- **⟹ 「$\mathrm{tr}$ か Schur か」は項ごとに逆で、取り違えると $\lambda$ 冪が 2 つずれる。**
  判定の前に**核のランクの見積り**（帯幅 $Q$ の何乗か）を 1 行書くこと。

出所: w225、稿 `131_条件付き定理_H-dens.md` §4.1・§7（S2・S3）、
worklog (研究ノート: `2026-09-14_w225_条件付き定理.md`) §3.2。

## F98（多重スケール帰納の 1 段で Feshbach 核 $K$ の分母を**作用素下界**で $\frac{\Lambda^2}{2m}$ まで上げる型 — 殻セクターには $2\Lambda$ の天井があり、$\lambda$ の 1 乗ぶん届かない。2026-09-14、稿 `134_`（w237）+ 補題 134-1′（audit136））

**⚠ 親へ: 本項は (研究ノート: `audit136.PATCH.md`) の P2（補題 134-1′ の追加）を稿 `134_` に反映した後にのみ連結してよい。**
P2 を入れないと、命題 134-1（$n_{\rm sh}=2$ の試行状態）から (G1) の否定は従わない（audit136 §2A）。

**棄却した主張**（設計稿 `133_` §L2.5 (G1)、`成算.md` S11 の「利得」欄）: 多重スケール帰納の 1 段
$\Lambda\to\Lambda'=\Lambda(1+\delta)$ で、Feshbach 核 $K=W^*(P_{\ge1}A'P_{\ge1})^{-1}W$ の分母は
「中間状態が運動量 $\sigma\in[\Lambda,\Lambda']$ の殻光子を 1 個持つ」ので真の大きさが
$\frac{(q+\sigma+\pi_\lt)^2}{2m}+|\sigma|+|q|\sim\frac{\Lambda^2}{2m}=\mathcal R$ であり、
**未知はスカラー $`p_0=\|P_{\rm f}\psi_0\|`$ のぼけ幅だけ**で「設計として閉じる見込みがある」、という型。

**壊れる理由（厳密・非摂動・無条件）**: $S11$ の分母に現れる $P_{\rm f}^{(\Lambda)}$ は**非有界作用素**であって
$p_0$ のぼけ幅ではない。バルク光子 1 個に $-(q+\sigma)$ を担わせれば反跳項は 0 にでき、代価は $|q+\sigma|\le\Lambda$ だけ。
稿 `134_` 補題 134-1′（`E05-F20` の天井 $E^\Lambda(P)\le E_0^\Lambda+\min(\frac{P^2}{2m},|P|)$ と直積分表示の 3 行）で
```math
\inf\sigma\bigl(P_1A'P_1\bigr)\ \le\ 2\Lambda+(3+2\sqrt2)\,\varepsilon_{\rm sh}\qquad(|q|=\kappa\Lambda,\ \kappa\le1),
```
命題 134-1（殻の背中合わせ 2 光子）で $\inf\sigma(P_{\ge1}A'P_{\ge1})\le|q|+2\Lambda+C_A\varepsilon_{\rm sh}$、$C_A=(\sqrt2+\sqrt3)^2\lt9.9$。
ゆえに $P_{\ge1}A'P_{\ge1}\ge G$（あるいは $B_{11}\ge G$）を満たす任意の自己共役 $G$ は $\inf\sigma(G)\le(2+\kappa)\Lambda+O(\varepsilon_{\rm sh})$ で、
要求 $\mathcal R=\frac\lambda2\Lambda$ には $\frac\lambda{2(2+\kappa)}\ge\frac\lambda6$ 倍だけ届かない。
機構は `F10` 命題4・`E05-F7`（背中合わせ配位の励起エネルギー $\simeq2\Lambda$ は**質量に依存しない**）と**同一**。

**帰結（`F95` の通貨は消えない）**: `133_` §L2.3 の素朴評価の第 1 項 $(\alpha)=\frac{2\alpha\lambda}{\pi\kappa}\delta$ は
分母を $|q|\to|q|+2\Lambda$ に改善しても $\frac{2\alpha\lambda}{\pi(\kappa+2)}\delta$ にしかならず、
$`\int\lambda\,d\ln\lambda=\lambda-1`$ なので窓 $\alpha^2\sqrt\lambda\le\kappa_0$（$\lambda\le\kappa_0^2\alpha^{-4}$）の中で $\alpha\lambda\le\kappa_0^2\alpha^{-3}$ と発散する。

**射程（⚠ これを超えて書かない）**:
- 否定するのは「**$K$ の分母を作用素下界で $\mathcal R$ まで上げる**」という**評価の型**だけである。
  **(G1) という命題そのものの否定ではない。** 真の $\langle\eta,K\eta\rangle$ は $W\eta$ の低帯スペクトル質量が小さければ小さいままであり得る。
- 多重スケール帰納法（候補 1）自体を閉鎖しない。`F10` 命題1 の「Gronwall 型かスケール帰納法でなければならない」という指示とは無矛盾。
- 加法源 $b$（`133_` §L2.4 の 2 次項）にも、audit134 §3.1 (a-3) の帯（各点 ⟹ sup）にも触れない。
- 有限 $\Lambda$ で閉じた命題であり、$\Lambda\to\infty$ の一様性は何も言わない（**T60**）。

**この型に足りないもの / 次に要る入力 1 つ**: **(IH3)** —— $B=P_{\ge1}A'P_{\ge1}$ に関する $W\eta$ の低帯スペクトル質量の上界
$`\mu^{B}_{W\eta}([|q|,t])\le C_3(t/\mathcal R)^p\|W\eta\|^2`$、$p\gt1$、$|q|\ge\kappa_0\Lambda$ で一様（稿 `134_` §4.1）。
**低帯を作るのは「殻光子 $\sigma$ + バルク光子 $\simeq-(q+\sigma)$」の配位なので、(IH3) は実質「$\eta$ が運動量尺度 $\Lambda$ のバルク光子を
どれだけ持つか」＝(N-loc) 型のベクトル値の局在仮定である**（スカラー 1 個には縮まない）。
これを仮定すれば 1 段の係数は $a\le C'[\frac{4\alpha}\pi+\frac{2C_2}{\pi^2\kappa}\alpha^2\sqrt\lambda]\delta$（`133_` §L2.6 の帳尻と一致）で窓の中で有界になる。
1 ループでは $p=2$（`134_` §5）だが、1 ループのスペクトルは床
$E_{\min}=(1+\kappa)\Lambda+\frac{(1-\kappa)^2}2\lambda\Lambda$ を持ち、上の低帯配位を含まないので**(IH3) の証拠ではない**（**T88**）。

**再挑戦禁止の範囲**: 「$(P_{\ge1}A'P_{\ge1})^{-1}\le\frac{C}{\mathcal R}$」「$`P_1A'P_1\ge c\,\mathcal R`$」の形の作用素不等式を
（角度制限・状態制限なしで）目指す評価は書かない。書くなら最初から $W\eta$ に制限した二次形式（(IH3) 型）で書く。

**記録**: 稿 `134_G1中間状態の反跳の二次形式評価.md`（w237、self-audited）、
監査 (研究ノート: `134_audit136_2026-09-14.md`)（audit136、監査の型、S2 full fresh audit）、
処方 (研究ノート: `audit136.PATCH.md`)（P2 が補題 134-1′）、`成算.md` S11 追記（(研究ノート: `w237.成算.md`) + PATCH P12）。
数値 (研究ノート: `268_w237_G1_recoil_gain_result.json`)（1 ループの値。**上下界ではない**）。

## F99 — 「Sellke (Duke 173, 2024) の Gauss 支配（Royen の GCI ＋ 位置ポテンシャルの擬凹性 ＋ 閉じ込め事象 $K_R$）をフル PF に移し、$K_R$ 上の経路ごとの下界 $\frac{e^2}4Q[b]\ge\kappa\frac{|b_T-b_0|^2}T$ を経由して $h$ の下界を出す」— **$K_R$ を変位で定義し $\kappa$ を直線最適値に取る版のみ閉鎖**

- 日付: 2026-09-21（成算 S13 → S44（w281）→ S47（w285）、閉鎖監査 audit156）
- 分類: **経路の一部の閉鎖**（機構そのものの閉鎖ではない。下の「閉じていない枝」を必ず読むこと）
- 向き【T43】: $h$ の**下界**側（Q3 否定側、B16 と同じ向き）。`E05-F19`「反射正値性が安い道具を軒並み否定側にする」の 4 度目の現れ。**Q3 のオッズは動かない。**

**前提（正本）**: 経路測度の重みは `E05-P70` 1.、
$\rho_T=\exp(-\frac{e^2}4\iint_{[0,T]^2}W_{\mu\nu}(b_s-b_r,s-r)db_\mu db_\nu)$、
$W_{\mu\nu}(y,\tau)=\int_{|k|\le\Lambda}\frac{d^3k}{(2\pi)^3|k|}P_\perp(k)_{\mu\nu}\mathrm e^{-|\tau||k|}\mathrm e^{ik\cdot y}$。
$Q[b]$ は**2 時刻の 2 次形式**（w281 §5.3 が書いたランク 1 形 $|\int_0^T\mathrm e^{ik b_s}\mathrm e^{-|k|(T-s)}db_s|^2$ は正本の**下界にすぎない**転記ミス。w285 が訂正、audit156 が正本と逐語照合して確認）。

**閉じた枝（＝この取り方には戻らない）**

> **命題 w281-3** により、$F=\mathbf 1_{K_R}\exp(-\frac{e^2}4Q[b]+\kappa\frac{|b_T-b_0|^2}T)$ が対称擬凹函数の有限積であるためには
> $\kappa\frac{|b_T-b_0|^2}T\le\frac{e^2}4Q[b]$（$\forall b\in K_R$）が必要。
> **$K_R$ を「窓長 $\Lambda^{-1}$ ごとの**変位** $\le R$」と読み、$\kappa$ を直線経路が許す最大値
> $\kappa_{\rm line}=\frac{e^2\Lambda}{8\pi^2}\frac{g(a_{\max})}{a_{\max}^2}$（$g(a)=2[\frac{(1+a^2)\arctan a}a-1]$、$a_{\max}=R\Lambda$）に取り、
> $K_R$ 内の全**連続**経路で量化した版は、偽である。**

- **反例の形**: (i) 変位を両端の短いバーストに時間集中し、(ii) 各バースト内で半径 $R$ の球に張り付いて往復する（弧長が $|\Delta b|$ の 40〜140 倍に伸びる）経路。**周期ジグザグ・螺旋は比 $\ge1.00$ で効かない**（成算 S47 の推論 1 の幾何は外れ）。
- **構造的理由（w285-O1、audit156 が独立に再導出）**: 同時刻バーストの自己コストは $S[\gamma]=\int_{|k|\le\Lambda}\frac{d^3k}{(2\pi)^3|k|}|P_\perp(k)F(k)|^2$（$F_\mu=\int_\gamma\mathrm e^{ik\cdot y}dy_\mu$）で、端点が決める唯一の Fourier データは $k\cdot F=-i(\mathrm e^{ik\cdot y_1}-\mathrm e^{ik\cdot y_0})$、$|k\cdot F|=2|\sin\frac{k\cdot J}2|$ であるが、**Coulomb ゲージの $P_\perp$ がちょうどこの成分を消す**。⟹「横成分の量を端点（縦）の量で下から押さえよ」という形の下界には構造的な向かい風がある。
- **数値**: $N=64$ で 5 セル中 3 セルが必要比 $\rho_{\rm req}=\frac{a^2}{a_{\max}^2}\frac{g(a_{\max})}{g(a)}$ を割る（$0.686\lt0.774$、$0.624\lt0.655$、$0.888\lt0.929$）。セル A は $N=256$ で $0.403$、球内最小化では $0.10$–$0.22$（(研究ノート: `337_w285_verdict.json`)）。audit156 が**別実装**（線分厳密 $F$、自前の解析的勾配、独立な $k$ 求積）で $S_{\min}/S_{\rm line}$ の水準・単調減少・球壁への張り付き・弧長の発散をすべて再現した。

**閉じていない枝（＝ここから再挑戦する。閉鎖と読み違えないこと）**

1. **$\kappa$ を定数倍下げた版は閉じていない。** 反例が下げたのは $\kappa$ の**上限**であって、機構の出力が 0 になるのは
   ```math
   \inf_{b\in K_R,\ \Delta b\ne0}\frac{T\,Q[b]}{|b_T-b_0|^2}=0
   ```
   のときだけ。この $\inf$ が $0$ か正の定数 $c\simeq0.10$–$0.20$ かは**未決**（w285 §6 #7、数値は非収束）。$\inf\gt0$ なら機構は定数を失うだけで、天井の $\lambda$ 冪 $b=\frac12$（$h=O(1)$ 側）〜$b=1$（自己無撞着側）は**変わらない**。
   **解析的傍証（audit156）**: 弧長 $L$ が有界な経路族では $|F(k)-J|\le L|k|R$ から $S\gtrsim c|J|^4/(R^2L^2)\gt0$。$\inf=0$ には $L\to\infty$ が要る。
2. **Brown 台の上での版は閉じていない。** 反例経路は**有限変分**で Gibbs 経路測度の台の a.e. 経路ではない。台の上では $Q$ に経路によらない 2 次変分項 $\frac{\Lambda^2T}{2\pi^2m}$ が乗り、$K_R$ 上で $|\Delta b|^2/T\le a_{\max}^2T$ なので、必要条件は**この定数だけで** $\kappa\le\frac{e^2\Lambda^2}{8\pi^2ma_{\max}^2}$ まで許す（要る $\kappa$ との比は $\frac{\sqrt{\lambda h}}{\pi\sqrt3}\gg1$、$\lambda\gg1$）。**必要条件は破れたのではなく無情報になった**（定数項は $|\Delta b|^2$ 型の擬凹因子を供給しないので、Prop 2.8 の構成には役立たない）。
3. **$K_R$ の $p$-変分版（$p\gt2$）は閉じていない。** $`\{\|b\|_{p\text{-var},\rm win}\le R\}`$ は (i) 半ノルムの球なので**対称凸**（Prop 2.8 の $\mathbf 1_K$ として合法）、(ii) Brown 経路は $p\gt2$ で a.s. に $p$-変分有限なので**正の Wiener 測度**、(iii) 球埋め尽かし反例は振動回数 $n$ に対し $p$-var $\simeq2Rn^{1/p}\to\infty$ なので**排除される**。⟹ 上の反例はこの版を殺していない。
4. **窓長の取り方は 1 つしか試していない。** PF の核は冪減衰（$\propto|s-r|^{-2}$）で相関時間を持たないので $K_R$ の窓の取り方が一意でない（w281 §6 #8）。w285 は窓 $\Lambda^{-1}$ の 1 つの選択で反例を作った。多重スケール版（原典 §5）での可否は未検査。

**死んでいる再挑戦条件（提案しないこと）**

- **$K_R$ を「窓ごとの**弧長**（全変動）$\le R$」に強める**: 対称凸で Prop 2.8 の要件は満たすが、**Brown 経路は a.s. に全変動無限なので Wiener 測度 0**。比較に使えない。
- **$K_R$ を「局所速度 $|\dot b|\le v$」で定義する**: 同じ理由（Brown 経路は a.s. 至る所微分不可能）で測度 0。
- **縦成分を残す非 Coulomb ゲージ版**: (研究ノート: `_公理表_共通.md`)「模型（正本）」が Coulomb ゲージ $\epsilon_\lambda(k)\cdot k=0$ を模型の定義に含むので、$P_\perp$ を外した核は別模型の核であり `E05-P70` 1.（Hiroshima 2007 の表示）から導けない。

**再挑戦条件（優先順）**

1. $\inf_{b\in K_R}\frac{TQ[b]}{|b_T-b_0|^2}\gt0$ を**解析的に**示す（数値は非収束で決まらない）。示せれば機構は定数を落として生き、冪 $b=\frac12\sim1$ は不変。示せなければ（$\inf=0$ なら）機構はこの経路で完全に死ぬ。
2. $p$-変分版 $K_R$（$p\gt2$）で pathwise 下界が成り立つか。成り立てば Prop 2.8 の 3 要件（対称凸・正の測度・反例の排除）が揃う。
3. Brown 台の上で、2 次変分の定数項と分離した $|\Delta b|^2$ 型の擬凹因子を取り出す（S48 の Gauss 尺度混合が使えるか）。

**関連**: `F9`（GHL 型 FKI の Gauss 支配。経路①の入口）・`F26`（FKG/Harris は association を持たない）・`F27`（Gauss 測度の凸×凸型相関不等式は偶関数性で閉じる）の続き。3 つとも `E05-F19` が単一原因。
**射程の限定**: w281 §5.3 の「翻訳先は (H-dens) と同じ量に戻る」は w285 の核訂正（ランク 1 → 2 時刻形）の**後には再確認されていない**。FAILED としては「同じ族の量に還元される」を断定しない。

**記録**: `成算.md` の S13・S44（w281 追記）・S47（w285 追記）、(研究ノート: `2026-09-20_w281_Sellke_GD_PF版_killcheck.md`)、(研究ノート: `2026-09-21_w285_pathwise下界.md`)、監査 (研究ノート: `S13_S44_S47_閉鎖監査_audit156_2026-09-21.md`)（audit156、監査の型、閉鎖の逆転監査。**閉鎖判定は FAIL＝親の暫定文のままでは閉鎖は成立しない**）。数値 (研究ノート: `333_w281_GD_checks_result.json`)・(研究ノート: `337_w285_*_result.json`)・(研究ノート: `337_w285_verdict.json`)。

<!-- 連結 2026-09-25 freeze01 hygiene -->
## F100（候補 B「走る質量つき UV Feshbach 帰納」の (IH-B) を、**細い殻**（$\Lambda\to\Lambda(1+\delta)$、$\delta\le0.5$）の 1 段で **c 数係数の局所 2 次形式族**に吸収する型 — 吸収不能な剰余の相対サイズは $\delta$ に依存せず、径数を 4 倍にしても 0 に収束しない。2026-09-21、稿 `150_`（design03）+ audit158）

反映前の稿の主張 3.・5. と §7 は audit158 が FAIL と判定しており、そのままでは本項の根拠にならない（audit158 の PATCH P1〜P16 は (研究ノート: `_applied_audit158.PATCH.md`) として稿 `150_` に反映済み。以下は反映後の内容）。
**本項は「候補 B の閉鎖」ではない。** 閉じたのは下の「閉じた枝」1 本だけである（**閉じたのは: 方式**。標的＝候補 B の (IH-B) は「閉じていない枝」2.〜3. の別方式待ち）。

**棄却した主張**（稿 `150_` の設計標的、`成算.md` S55 の分岐表）: UV 殻帰納の 1 段
$\Lambda'=\Lambda(1+\delta)\to\Lambda$ を Feshbach–Schur で行うと、有効作用素が
$H_j=\frac1{2m_j}(P-P_{\rm f}^{\lt j}-e_jA_{\Lambda_j})^2+H_{\rm f}^{\lt j}+C_j+V_j$ の形に留まり、
$V_j$ が段の生成項 $\Delta_j$ に対して $\delta\to0$ で相対的に小さくなる（＝殻を細くすれば形の不変性が回復する）、という型。

**壊れる理由（有限モード ED の**値**。上下界ではない【T88】）**: 生成項は $O(e^2)\cdot O(\delta)$ で厳密に
```math
\Delta=-\frac{e^2}{m^2}\sum_\lambda\int_S\frac{d^3k}{(2\pi)^32|k|}(\epsilon_\lambda\!\cdot\!\pi_\lt)\bigl(|k|+H_\lt(P-k)-z\bigr)^{-1}(\epsilon_\lambda\!\cdot\!\pi_\lt)
```
（`E05-P103` 2. の核の作用素版。前因子まで一致。audit158 が独立再導出）。$\Delta$ のうち
$(P_{\rm f},A)$ の 2 次全 span（21 個の対称積 + $H_{\rm f}$ + $I$、異方的質量も走る電荷も許す）に吸収されない成分の比は
$\delta=0.5/0.25/0.125$ で $0.10631/0.10687/0.10713$（**$\delta$ 非依存**）、作用素ノルムでも $0.152$（下界 $0.067$）。
径数を 23→94 本（核が $N$・$H_{\rm f}$・$|\pi|^2$ の 1 次まで）に増やしても $0.0215$ で止まり、
低殻の打ち切りを上げると $0.0215\to0.0276$ と**戻る**（0 に収束しない）。
$`\|\Delta\|/\|H_{00}\|`$ の方は $\delta$ に正確に比例するので、**$`\|V\|/\|H\|`$ で測ると中身に関係なく偽の $O(\delta)$ が出る**【T93】。
正しい量は $`\|V\|/\|\Delta\|`$ で、1 オクターブを覆う段数が $\propto\delta^{-1}$ だから細分では何も買えない。
剰余の源は §2 表の (e)（$\pi^i(H_\lt-z)\pi^i$、$z$ 依存）と (f)（反跳 2 次 $`\pi^i(k\!\cdot\!\pi_\lt)^2\pi^j/m^2`$）で、
どちらも核が resolvent $(H_\lt(P-k)+|k|-z)^{-1}$ そのものを要求する非局所項である。

**閉じた枝（＝この取り方には戻らない）**
> 「**細い殻**（$\delta\lesssim0.5$、1 殻光子・$O(e^2)O(\delta)$ の展開が主）で 1 段の Feshbach を行い、
> **c 数係数の局所 2 次形式族**（PF・異方的 PF・走る電荷・核が $N$／$H_{\rm f}$／$|\pi|^2$ の 1 次までの一般化族）
> に生成項を吸収させ、$\delta$ を細くすることで剰余を小さくする」型。
> $\delta$ を 4 倍細くしても剰余比は 0.106→0.107 で不変であり、この方向に改善の余地は無い。

**閉じていない枝（⚠ ここを広げないこと）**
1. **候補 A（`E05-P103`、$\psi_0$ 期待値の経路）は無傷。** 否定したのは作用素としての形の不変性だけ。
2. **厚い殻（$\Lambda_{j+1}=\epsilon\Lambda_j$、$\epsilon\ll1$）の枝は未判定。** 殻比 $\epsilon$ は自由な設計変数で、
   保持帯は $\rho=\epsilon\Lambda_j$ まで狭められる。1 ループ重み比では 1 段の非 PF 比が $\lambda\to\infty$ で
   $\approx2/\ln(1/\epsilon)$ でしか減らないので救いにはならない見込みだが、**$\epsilon\ll1$ では多殻光子チャネル
   （(W2) 以降）が同位になり稿の解析が及ばない。ここは測っていない。**
3. **非局所核を径数に含む族（(IH-D)）は否定していない。** 本項が言うのは「$W_j$ のクラスは resolvent で
   閉じていなければならない」ことだけで、そのような族が存在しないとは言っていない（需要 D-G3-1）。
4. **$\lambda\to\infty$ の一様性は何も言わない。** 測ったのは $\lambda=2,8,32$（audit158 の再実装）で、
   剰余比は $0.086/0.107/0.118$ と微増する。有限モード ED は無限次元性・稠密性・局在比 $\Xi$ を検証しない（`E05-F5`）。
5. **§5.6 の $z$ 依存性の議論は文献未確認**（BFS の多重スケール解析が実際にどの族で帰納を回しているかは未照合）。

**再挑戦条件（これが揃えば戻ってよい）**
- (a) 厚い殻 1 段の多殻光子チャネルの費用が評価できたとき（上の 2.）。
- (b) resolvent で閉じた有限次元パラメタ化（$W_j$ が有限個の径数で $(H_\lt(P-k)+|k|-z)^{-1}$ の族に収まる形）が 1 つ見つかったとき。
- (c) 作用素命題でなく $\psi_0$ 期待値の版（候補 A）で帰納を回す設計に組み替えたとき（本項は一切触れない）。

**記録**: 稿 `150_候補B形の不変性.md`（design03、`self-audited`。audit158 の PATCH P1〜P16 反映後）、
監査 (研究ノート: `150_候補B_audit158_2026-09-21.md`)（audit158、`監査の型`、S2、逆転監査）。
数値 (研究ノート: `346_design03_feshbach_shell_result.json`)・`346b_*`・`346c_*`（決定的、RNG なし。**値であって上下界ではない**）。
audit158 の独立再実装（模型から書き起こし、最上殻 6/12 モード・低殻 2/3 オクターブ・$\lambda=2,8,32$・設計行列 SVD・作用素ノルム）で 5 桁再現。

## F101(A1 手 A「素朴 M4_ramp の直接 MC で $\lambda=128$ の $h$ を 1.5%」— seed 間 $\chi^2$ 残留と $\tau_D$ の rep 間散乱で届かない。2026-10-05、lead_R1 提案 §2 案 1・audit_R1_a1x10、ユーザー承認 2026-10-05 で A1 締め)

**閉じたのは: 方式。** 標的(Q3 の数値判定、固定 $\alpha$ の $\gamma_{\rm loc}$ 列)は閉じていない(段 A1b `A1b-001_STATEMENT.md` に引き継ぐ)。**命題(Q3)の真偽も閉じていない。**

**棄却した方式**(A1-001 §2 (S1)): 局所更新の M4_ramp 鎖(f32e 核、計算機 2 RTX 5090)で $T=6$・$\lambda=128$ の $h$ を $`x\in\{3,10\}`$ で相対 1.5% まで取り、$`\lambda\in\{32,64,128\}`$ の 3 段で $\gamma_{\rm loc}$ を出す。

**壊れる理由(値であって上下界ではない【T88】)**:
- $x=3$: $h=4.800\pm0.099$(2.06%、rep 10、seed 間 $\chi^2/{\rm dof}=4.93$、NUM-1861)— 1.5% 未達。
- $x=10$: $h(128,10)=10.45\pm0.65$(引用、6.2%)、seed 間 $\chi^2/{\rm dof}=7.03$(r3 低・r5 高の両側で 35 中 29)⟹ $\sqrt{\chi^2/{\rm dof}}$ 倍で $\pm1.73$(16.5%)(NUM-3173)。1 rep 72000 s × 6 = 120 GPU h(24 h 超ジョブの承認済み)でも目標 5% にも届かない ⟹ A1-001 §3 の (K3) 点灯。
- 原因の型: $\tau_D$ が rep ごとに 1 桁散る(189〜2183)、作用の自己相関 $\tau_S$ が $\tau_D$ の 17〜62 倍(NUM-2344・NUM-2782)、局所更新の改良は効率比 1.02 で不通過(NUM-2344)。遅いのは局所の受理ではなく集団モード(準安定な配置)と読める(A1-002 §1)。
- 費用則: 素朴 $O(N^2)$($N=T\lambda^2$)の掃引費用は 1 段 25.6 倍で、$\lambda=256$ は約 1000 GPU h/セル(design_R1 §0)。

**副産物(値、オッズは動かない)**: 固定 $\alpha$ の $\gamma_{\rm loc}$(64→128)は $x=3$ 端で $0.59\pm0.09$(膨らませ後;λ=64 側の形の系統 −0.02/+0.14)、$x=10$ 端で $0.65\pm0.26$(NUM-3174)。S-A1-1 推論 2 の「collapse を仮定した 0.3±0.1」は弱い否定(2σ 前後、audit_R1_a1x10)。$\lambda\le128$ の局所冪は 0.5 前後で、Q3(1/2)と 1 ループ(→0)を区別しない。

**閉じた枝(この取り方には戻らない)**
> 「局所更新の鎖のまま、rep の長さ・本数・適応予算を増やして $\lambda\ge128$ の $h$ を 1.5% にする」型(追加 rep で $x=10$ を 5% にする案 2 は 280〜460 GPU h で、$\gamma$ の漸近に効かない)。

**閉じていない枝(⚠ ここを広げないこと)**
1. **Q3 の真偽**: 何も言わない。$\lambda\le128$ の値は 3 仮説(1 ループ型・1/2・線形)のどれとも整合。
2. **大域更新(前処理つき HMC、design_R1 N2)と階層力(N3)の組**: 本項の対象外。A1b の第 1 段 K2・K4 で判定する。
3. **推定量 D_slope の資格**: 本項は推定量を否定していない(較正が未済なだけ)。A1b K1(双極子 PF 較正)で判定する。
4. **候補 D(殻ごとの数値 RG・合流曲面)**: 族 F1/F2(NUM-1867)は未決のまま。本項は閉じていない。

**再開条件(ID、R1・R9 — いずれも標的と同値でない)**
- (a) S-A1-12(A1b K2:前処理つき HMC の効率比)が合否基準を通る ⟹ 局所更新でなく大域更新で $\lambda=128$ を取り直す(本項の方式そのものには戻らない)。
- (b) S-A1-11(A1b K1:双極子 PF による推定量の較正)が通り、かつ S-A1-14(A1b K4:階層力の成算)が「成算あり」⟹ $\lambda\ge256$ の費用則が変わる。
- (c) 外部文献または他 G の独立入力で $\lambda\ge256$ の $h$ か $\gamma$ が与えられる(`CITATIONS_PENDING.md` か (研究ノート: `INBOX_G3.md`) の行 ID で)。

**記録**: 提案 (研究ノート: `lead_R1_a1.提案.md`) §0〜§2(lead_R1 = 書き下しの型)、監査 (研究ノート: `audit_R1_a1x10.AUDIT.md`)(監査の型、read-only + C0 再計算)、成算 S-A1-1 追記 2・S-A1-7 追記((研究ノート: `lead_R1_a1.成算.md`))、ジョブ (研究ノート: `g3_e05a1_pimc_x10`)(`analysis.json`・`result.json`)。設計 (研究ノート: `design_R1_Q3.提案.md`)。数値 NUM-1861・NUM-2344・NUM-2782・NUM-3173・NUM-3174。

## F102(A1c 段 2「方式 B の木の HMC(緩い木 (16,0.3) の力 + 締めた木 (16,0.15) の f64 受理)で λ=256 の $h$ を F4 直接和より安く取る」— 平衡の配位で木の 1 力が F4 の 3.5〜3.7 倍遅く、(k3) が発火。2026-10-06、稿 174・A1c_w2)

**閉じたのは: 方式の見込み。** 「平衡の配位で方式 B の木の HMC が λ=256 で F4 直接和より安い」という見込み(A1c-001 §6 の木の 1 軌道 1.2〜2.9 s、S-A1-27 推論 2)。**木の力そのもの**(chkT の決定性・CPU 木との一致 3e-5・不一致の sd 0.02〜0.04 は通過)、**λ=512 で木が直接和に勝つ可能性**、標的(固定 α の $\gamma_{\rm loc}$ の λ 推移)、**Q3 の真偽**は閉じていない。

**棄却した方式**(A1c-001 §3・§7 の旧文):λ=256 を方式 B の木の HMC で 1% に取り、λ=128 に木の接続セル (128,11.314) 2% を置いて F4 からの切替の系統を見る。

**壊れる理由(値であって上下界ではない【T88】)**:
- 木の smoke2((研究ノート: `g3_e05a1c_tree_smoke2`)、5090):鎖の中の 1 力は λ=128 で 0.114 s(F4 0.032 s の 3.5 倍)、λ=256 で 1.87 s(F4 0.505 s の 3.7 倍)。遠方対は鎖の中で 4.1 倍(λ=128)・6.3 倍(λ=256)に増える。刻みも短くならない(λ=256 の ε は下限 0.02 に張り付き L 79)。
- GPU h(c=1、V_rel 2.6):木の λ=256 は 1% 790〜1440、1.5% 350〜640、2% 200〜360 — (k3)「1% > 100 かつ 1.5% > 60」を 6〜14 倍で超え、2% でも上限 300 を超え得る((研究ノート: `A1_374_w2_cost_result.json`))。
- 原因の型:平衡の配位は長時間で着衣・短時間で裸の粗さを持ち、MAC $r_I+r_J\le\theta\sqrt{y^2+\tau^2}$ が通らない対が細かい水準と厳密対へ降りる。検査配位(Gauss・自由経路、NUM-3270〜3273)は全尺度で一様な粗さなので、この増加を見逃した。CPU 模型(混合配位)で遠方対 2.2〜4.2 倍・厳密対 5〜7 倍・時間 2.8〜4.9 倍(λ=16〜64、`A1_374_w2_treecount_result.json`)。
- 改良の見当(1 ラウンド):θ 0.3 → 0.5 で 2.5 倍、葉 32 で 1.07 倍 — λ=256 で F4 に届かない。

**閉じた枝(この取り方には戻らない)**
> 「検査配位(Gauss・自由経路)での木の 1 力の速さから、平衡の鎖の費用を見積もって λ=256 の本走の予算を置く」型。木の費用は平衡の配位(または鎖の後半)の遠方対・厳密対の数で見積もる。

**閉じていない枝(⚠ ここを広げないこと)**
1. **Q3 の真偽・$\gamma_{\rm loc}$ の値**:何も言わない(smoke2 は short で $h$ を返していない)。
2. **λ=512 の木**:F4 は λ=512 で 1 力 約 7.9 s(NUM-3274)・1 軌道 約 700 s で不可能。混合配位の厳密対は 1 オクターブ ×5〜7($N^{1.2\sim1.4}$)、F4 は ×16 なので、λ=512 では木が逆転する見当 — 本項は閉じていない。
3. **木の力の正しさ**:否定していない。

**再開条件(ID、R1・R9 — 標的と同値でない)**
- (a) 木の鎖の 1 力が平衡の配位(鎖の後半)で F4 の 1/2 以下になる GPU 実測(厳密対の数を記録した 1 軌道の診断 + MAC・θ の見直し)。
- (b) λ=512 の点が必要になる(A1c の予想の型が λ≤256 で「傾向不明」になり、親が λ=512 を裁定する)— F4 では不可能なので木だけが候補。

**記録**:稿 `174_λ256の経路_木からF4直接和へ.md` §1・§7・§8、worklog (研究ノート: `2026-10-06_A1c_w2.md`) §1、ジョブ (研究ノート: `g3_e05a1c_tree_smoke2`)(tasks 6 本・`smoke_gate.json`)、計算 (研究ノート: `A1_374_w2_cost.py`)・`A1_374_w2_treecount.py`、成算 S-A1-27(木の統合)・S-A1-29(F4 への切替)。数値 NUM-3270〜3274、本稿の NUM-?。

## F103(2026-10-06、w_E1_Nsh_dimcount = 書き下しの型、稿 `176_殻対占有数の制限つき下界の次元勘定_2026-10-06.md`)— (E1) の独立入力 $N_{\rm sh}\to\infty$ を、別の稿 の殻対スクイーズ上界と「殻対の占有数 $\le N_*$」に制限した $H(0)$ の下界の比較で出す方式

- **閉じたのは: 方式**(別の稿 の上界 $E_{\rm trial}=\tau_\Lambda-\Theta(\Lambda^{3/2})$ と $E_0^{(\le N_*)}$ のエネルギー比較)。標的((E1)・$N_{\rm sh}\to\infty$)と命題の真偽は閉じない。
- **理由(値による閉鎖。T88・T84 (e))**: 2 次の対生成の利得を総運動量で分けると、窓外($|k+k'|\gt Q$)が $\sim\alpha^2\Lambda^2/m$、窓内が $\sim\alpha^2\Lambda^{3/2}m^{-1/2}$ で、比は $\sqrt\lambda$。窓外の対は 1 対あたり反跳で抑えられるが位相空間で逆転する。窓外に台を持つガウス試行は $\langle N_{\rm sh}\rangle\sim\theta^4\Lambda^{-1/2}\to0$ なので、$E_0^{(\le N_*)}\le E_0^{(\le0)}\lesssim\tau_\Lambda-c\,\alpha^2\Lambda^2/m\lt E_{\rm trial}$($\lambda$ 大)。$E_{\rm trial}\lt E_0^{(\le N_*)}$ を満たす $N_*(\lambda)$ は無い($N_*=0$ でも不成立)。殻の 1 体光子数 $N_S\le N_*$ に替えても、殻の内側の対の利得 $\alpha^2(\Lambda/2)^2/m$ が残り同じ。
- **再開条件**: 窓外ガウス試行のエネルギーの値(2 次 + 射影誤差 $O(\Lambda^{7/4})$)を厳密化したとき、利得が $o(\Lambda^{3/2})$ に落ちることが示された場合(見込みは低い。摂動論の全次数で $\Lambda^2$ の構造と整合しているため)。
- **残る筋**(本断片の対象外): 比較の相手を E05-L4 の上界 $C_2\alpha^{2/7}\Lambda^{12/7}$ に替え、$E_0^{(\le N_*)}\gtrsim\Lambda^{12/7+\epsilon}$ の非摂動下界を立てる版(稿 `176_` §2.4、判定不能)と、停留条件 $\langle\psi_0,[H(0),B_\beta]\psi_0\rangle=0$ による局所版(同 §5 (β))。
- 数値: (研究ノート: `376_w_E1_Nsh_toy.py`)(4 モードの玩具、INCONCLUSIVE、向きのみ一致。$\sqrt\lambda$ の位相空間比は検証しない)。

## F104(2026-10-06 夜、design_S1_alpha_l4 = 書き下しの型、稿 `183_設計偵察_E05-L4上界との比較_殻対制限と再編成_2026-10-06.md`)— (E1) の独立入力 $N_{\rm sh}\to\infty$ を、E05-L4 の上界 $C_2\alpha^{2/7}\Lambda^{12/7}$ と「殻対の占有数 $\le N_*$」に制限した $E_0^{(\le N_*)}$ の比較で出す方式((α)、`176_` §2.4)

- **閉じたのは: 方式**(L4 上界とのエネルギー比較)。標的((E1)・$N_{\rm sh}\to\infty$)と命題の真偽は閉じない。
- **理由(値による閉鎖。T88)**: L4 の上界を与える Lieb–Loss 1999 の試行状態(積 $\phi\otimes\Psi$、$\Psi$ はガウスのスクイーズ真空、原典 p.9 (2.18)〜(2.24))では、光子対の総運動量は $K\sim\alpha^{1/7}\lambda^{6/7}m\gg Q=\sqrt{2m\Lambda}$ に広がり、窓内の対の数は $\langle N_{\rm sh}\rangle\sim\alpha^{-1/7}\lambda^{-5/14}+\alpha^{4/7}\lambda^{-1/14}\to0$。$N_{\rm sh}$ は $P_f$・$p$ と可換なので、$N_{\rm sh}$ の切断と $P=0$ への並進平均の後も $\mathcal H_{\le N_*}$ に留まり、$E_0^{(\le N_*)}(0)\lesssim C'\alpha^{2/7}\Lambda^{12/7}m^{-5/7}$(値)。標的 $E_0^{(\le N_*)}\gtrsim\Lambda^{12/7+\epsilon}$ はどの $N_*\gt0$ でも成り立たない。殻は窓外の対で再編成される(F103 と同じ機構の非摂動版)。
- **再開条件**: (i) 窓 $Q$ を $K$ 級に広げた数え方で (E1) の入力が組める場合(S-A2-9 の分子が総運動量 $\sim K$ の対で書けることが先に要る);(ii) LL 試行の $N_{\rm sh}$ 切断または並進平均のエネルギー変化が $\gg\alpha^{2/7}\Lambda^{12/7}m^{-5/7}$ と示された場合(値の勘定では $o(E)$・$O(E)$)。
- **残る筋**(本断片の対象外): S63-∞(停留条件・対振幅恒等式の局所版、(I-μ) の kill-check)。エネルギー比較型は F103 と本断片の 2 方式で閉じた。
- 数値: なし(値の勘定のみ)。

## F105(2026-10-07、G3 統括 第 67 陣 = E05 親、chk_E1_s71・s71b・s71c・s71d の 4 体を統合)— S71(重心型の擬似ブーストの残りの費用 $\rho$ が平台で $\Lambda$ とともに減るか)を、有限模型(格子運動量の箱・光子 2 個の Tamm–Dancoff 連続体)の数値で判定する方式
- **閉じたのは: 方式**(有限模型の数値による判定)。S71 の標的と真偽は閉じない(S71 は 0.4 で据え置き)。
- **正確な障害**: (i) 1 次元・3 次元の格子運動量の箱では、比 $\rho$ は全条件で $\Lambda$ とともに単調に減るが、平台がモード数とともに増え、到達できる段($\delta\ge0.30$)は連続体の極限の 1/6〜1/25 で解像不足と区別できない(chk_E1_s71b・s71c);(ii) 光子 2 個の TD 連続体では、2 光子セクターが自己エネルギーを持たないため $\lvert E\rvert\propto\Lambda^2$ の人工的なギャップが残り、$w_0$ は 0.85 付近で止まって E05-P116 の $w_0\to0$ の領域に入れない;その「平台」で $\rho$ は増えるが、ギャップを外した診断(固有状態でない)では $\rho$ は 2 次と同じ冪で減る(chk_E1_s71d)— 方式の性質と打切りの性質が分けられない。4 ラウンドで決着しない(3 ラウンド則)。
- **何が新しければ再挑戦可か**: (a) ギャップを持たない打切りの固有状態(2 光子セクターに自己エネルギーを入れた TD、または光子 3 個までの TD)で $w_0\lt0.85$ に入れること;(b) A1 の HMC による $w_0(\lambda)$ の熱力学積分(ジョブ `g3_e05a1_w0ti`)の値で、平台の位置が分かること;(c) (197-1) の解析的な補題化で $\rho$ の上界が直接書けること。
- 出所: (研究ノート: `2026-10-07_chk_E1_s71*.md`)(4 本)、(研究ノート: `394_*`)〜`397_*`、`成算.md` の S71 の判定更新と親裁定 1・2。


## F106(2026-10-07、chk_E1_s71e = 書き下しの型)— 稿 `199_` 命題 199-E (iii) の交換子項を $\lVert N^{-1/2}\tilde D_\theta\tilde\psi_\Lambda\rVert^2$ で単独に押さえて S71 の $\rho\to0$ を出す上界の経路
- **閉じたのは: 方式**(交換子項 $e^2\lVert J\psi_0\rVert^2$ を Cauchy–Schwarz で $w_0+\langle N^{-1}\rangle$ と止まる量 $Q_{\rm stop}=\lVert N^{-1/2}\tilde D_\theta\tilde\psi_\Lambda\rVert^2$ に分け、$K$ の交差項と別々に評価する経路)。S71 の標的(重心型の擬似ブーストで $\rho\to0$)と命題 199-E の上界の正しさは閉じない。
- **正確な障害**: 止まる量が $\lambda$ とともに減らない。1 ループ(最低次の対)で $Q_{\rm stop}\propto\alpha^2\lambda^{3/2}$(内端支配、求積で冪 1.499)、光子 2 個までの TD の固有状態で平ら(冪 $\le0.003$)か増える、ギャップを外した診断で $\propto\lambda^{1.05}$ — $\theta$ の内端 3 通り × 外端の幅 2 通りのどれでも同じ。比 $\lVert\tilde D\tilde\psi\rVert^2/\langle N\rangle$ も一定か $\sim\lambda$ で、稿 199 §4 の「光子数が重心の広がりより速く増える」の逆。同じ行で $\rho$ 自体は減る(1 ループ 0.29→−0.01、診断 0.55→0.009)ので、減少は交換子項と $K$ の交差項の打ち消しから来ており、分離した上界はそれを失う。
- **何が新しければ再挑戦可か**: (a) 交換子項と $K$ の交差項を合同の 2 次形式として押さえる評価(稿 197 §3 の 2 次の打ち消しの作用素版);(b) $\langle N\rangle\to\infty$ の非摂動の値(光子数の打切りの無い模型)で $Q_{\rm stop}/\langle N\rangle$ 型の比が減ること。
- 出所: (研究ノート: `2026-10-07_chk_E1_s71e.md`)、(研究ノート: `400_chk_E1_s71e.py`)(`_loop`・`_td`・`_gapless`・`_conv1` の `result.json`、全行 PASS)、`成算.md` の S71 判定更新(第 5 手)。



## F107(2026-10-07、design_E1_s71n = 監査の型)— S71 の残る道 (a):稿 `201_` の合同形式 $\mathcal Q_\theta$ を (201-1) の正規順序の形に組み直し、交差項の $A$ 部分と $P_f$ 部分の相殺を `E05-P116` の道具(拡大変換・$q(\tilde\psi)\to0$)で押さえて $\rho\to0$ を出す方式
- **閉じたのは: 方式**(残る道 (a) = 合同形式を P116 の道具で押さえる方式。正規順序の形を含む)。S71 の標的($\rho\to0$)と分岐 (B) の真偽は閉じない。
- **正確な障害**: 縮約は $\lVert J^+\psi\rVert^2$ と $\langle a^*(g)\psi,K^+\psi\rangle$ にだけ現れて $\pm(f_2+f_X)$($f_2=\frac\alpha\pi\lVert(N+1)^{-1}\tilde D_\theta\tilde\psi_\Lambda\rVert^2$、$f_X=4\pi\alpha c_X(\tilde\theta)\langle(N+1)^{-2}\rangle$)、ゆえに正規順序の交差の和は恒等的に $f_2+f_X+R$、$R=-2e\sum_\mu\mathrm{Re}\langle\tilde\pi_\mu\tilde\psi,\tilde K_\mu\tilde\psi\rangle$(稿 `203_` (203-2)、有限 Fock で $\le9\times10^{-15}$)。P116 が押さえるのは $R$($\le2\lvert e\rvert\sqrt{2q}\lVert\tilde K\tilde\psi\rVert$)と $f_X$(P115 で $\to0$;(201-2) の真空項はその $n=0$ 項)だけ。$A$・$P_f$ の相殺は $R\approx-f_2-f_X$(分岐 B:$\lVert\tilde K\tilde\psi\rVert\ge f_2/(2\lvert e\rvert\sqrt{2q})$ の符号つきの下界、道具なし)と同値で、$R\to0$(分岐 A)なら交差の和は $f_2$ に向かい $\mathcal Q_\theta\to\mathrm{comm}^{\rm no}+f_2$。縮約の配分(正規順序の基準状態の取り替えを含む)ではこの二択を回避できない(命題 203-C)。virial 型($\langle[\tilde H,B]\rangle=0$ で $\lambda^{-1}$)は $K$ が $D$ の 2 次、$[\pi,B]$($B$ が $D$ の奇多項式)が奇数次で一致しない。
- **何が新しければ再挑戦可か**: (a) **率つきの光子数の増大** — $f_2\to0$ には $\lVert(N+1)\tilde\pi_z\tilde\psi\rVert\to\infty$ が必要((203-3))で、`E05-P115`・`E05-P116` は $N\to\infty$ と $\lVert\tilde\pi\tilde\psi\rVert\to0$ を率なしで与えるだけ。$\langle N\rangle\lVert\tilde\pi\tilde\psi\rVert$ の向きを決める率(率つきの $w_0\to0$ から命題 189-2 経由、または A1 の HMC の光子数のモーメント)と、$\mathrm{comm}^{\rm no}$ の主項 $\sum_n(n+1)^{-2}\lVert a(\tilde g)\tilde D\tilde\psi_n\rVert^2$ の 1 体密度による評価(粗い評価では $\frac\alpha\pi Q_{\rm stop}$ に戻る)— F106 の再挑戦条件 (b) の精密化;(b) $R$ の符号つきの下界を与える道具。
- 出所: 稿 `203_設計_S71の正規順序の合同形式とP116の道具_2026-10-07.md`、(研究ノート: `2026-10-07_design_E1_s71n.md`)、(研究ノート: `405_design_E1_s71n_toy.py`)(`_result.json`、PASS、代数のみ)、`成算.md` の S71 判定更新(design_E1_s71n)。

## F108(2026-10-17、lead_E05_211 = 書き下しの型、稿 `211_設計偵察_E1の世界線表示と多重尺度RG_2026-10-17.md` §4.2 (b)・§8、成算 S76)— (E1) の L-b の主項 $\mathrm{comm}^{\rm no}$ を、PF の $P=0$ ファイバーの世界線(FK)表示に摂動的な多重尺度 RG(BBS 型の有限レンジ分解 + 弱自己回避歩行の RG)を当て、尺度ごとに $\lambda$ の冪で減らして押さえる方式
- **閉じたのは: 方式**(標的 L-b・(E1) の真偽は閉じない)。
- **理由(構造と値。T88)**:(1) 前提の誤り — PF の重みは $e^{-\frac{e^2}2S_T}$($S_T\ge0$、LHB 2011 Thm 7.48)で引力ではない;(2) 相互作用は増分どうしで時間差に依る(時間非局所)ので、自己交差局所時間の関数でなく、BBS 2019 §11 の BFS–Dynkin 同型・超対称表示が使えない;(3) 最上位の尺度($\lvert k\rvert\sim\Lambda$)で 1 胞あたりの結合が値で $\alpha\lambda^{1/2}$ 級で、小さい結合の展開(LHB §4.3、Gubinelli–Lőrinczi 2007 のクラスター展開も小さい結合・閉じ込めつき)が効かない;尺度ごとの流れの主変数は有効質量で (E1) そのもの(R9);(4) 値:L-b の主項は届く λ の全段で増える(NUM-5751、`414_`)。FRD の正定値性・時間方向の有限レンジ性は成り立つ(閉鎖の理由ではない)。
- **再挑戦条件**:強結合の尺度を先に積分した有効測度の下で下位の尺度に小さい結合が戻ることが示せる場合、または局所時間型でない時間非局所の相互作用の RG の枠が文献で見つかる場合。ただし (E1) には消費者を替える道(S77、稿 `211_` §2)があり、L-b 自体が不要になりうる。

## F109(2026-10-18、w_E05_215 = 書き下しの型、稿 `215_EHdashの相対分散の上側の裾と反跳_2026-10-18.md` §4.2 観察 215-D、成算 S78)— (E-H′) の第 2 連言 $\sigma^2\to0$ を、反跳 $P_f$ を量的に使わない道具(固有方程式と形式の構造、$H_f\ge H_\theta$、$\lVert\pi\psi_0\rVert^2\le2mE_0$、場の 1 体評価、1 体密度行列の正値性 — `76_` の母不等式とその $H_\theta$ 版)だけで示す方式
- **閉じたもの**:**方式**(命題 (E-H′) の真偽ではない)。
- **理由**:(1)(厳密な部分は形だけ)この型の最良の上界(命題 215-B)は $\sigma^2\le(E_0-M)/M+$ 誤差の形で、これで $\sigma^2\to0$ を出すには床 $(\langle T\rangle+\langle H_f-H_\theta\rangle)/M\to0$ が要る〔床が 0 に行かないことは $\nu\to\infty$ の下では値の読み(`416_`)で未証明 —— audit_S2_E1H;閉鎖の厳密な根拠は理由 (2)〕;閾値つきの版(補題 215-A)は $E_0$ の数倍より上の裾を払うが帯 $[M,4\max(E_0,\Lambda)]$ には効かない。
- **理由 (2) 新**:(定理、`216_双極子近似の相対分散の定理と反跳の設計偵察_2026-10-18.md` 定理 216-A、S2 PASS with fixes〔`217_`、audit_S2_216〕)入力 (a)〜(e) は双極子近似(ファイバーで $P_f$ を落とす、F1 の定義)の**動径の胞の有限モード版**でも文字どおり成り立ち(`E05-P117` 型の $mE_0/\Lambda^2\to0$ も成り立つ)、その準自由な基底状態では、$b:=4\kappa\lVert u\rVert^2\gt1$(連続の値 $4\alpha\lambda/9\pi$)と窓の内端 $a$ について $\sigma^2\ge\frac13\bigl[(1-b^{-1/2})^2(1-b^{-1})^2/(1+1/(a\sqrt b))\bigr]^2$、$\nu\ge\frac34\sqrt b(1-b^{-1/2})^2(1-b^{-1})^2I_1\to\infty$。下界は $(b,a)$ だけの普遍な関数で胞の取り方にはこれを通じてだけ依り、幅 $\le1/3$ の胞では $b\ge\frac12\cdot\frac{4\alpha\lambda}{9\pi}$ なので胞に一様;ゆえに $\liminf_{\alpha\lambda\to\infty}\sigma^2\ge1/3$。窓の光子は孤立した基準モード 1 本に入る(重み $h$ の下での割合 $1-O(b^{-1/2})$)。**ゆえに入力 (a)〜(e) から $\sigma^2\to0$ は導けない。** 値(NUM-6199:$\sigma^2\to2/3$)は極限値の読みとしてだけ残す。
- **限定 新**:閉じたのは**方式**で、命題 (E-H′) の真偽ではない — **定理 216-A は双極子近似の定理であって (E-H′) の反証ではない**(双極子は反跳 $P_f$ を落とした別の模型で、E05 族ではない)。有限モード版は Williamson 分解で自足し、方式の閉鎖にはそれで足りる(各 $\alpha\lambda$ で幅の細かい胞の版を取る);連続の版の基底状態の同定(Arai の双極子近似の厳密解 [要確認])は使わない。**射程**:双極子では $\nu\asymp\sqrt{\alpha\lambda}$・$E_0/M=O(1)$(`217_` 系 A-217-2、self-audited)なので、**$\nu$ の増大率($\nu/\sqrt{\alpha\lambda}\to\infty$、補題 215-A の系 (i) が効く条件)や $E_0/M\to\infty$(どちらも双極子が破る向き)を入力に足した方式はこの閉鎖の外;双極子が満たす向きの入力($\nu$ や $E_0/M$ の上界、`E05-P117`)を足した方式は閉じたまま**(その増大率の差そのものが反跳の効果の値)。極限値 $2/3$ は主張しない(下界 $1/3$ だけ)。
- **再開条件**:反跳 $P_f^2/2m$ を量的に使う入力(2 光子の連結相関の窓の上の評価で、双極子と E05 族を区別するもの)が 1 つ供給されたとき。

## F110(2026-10-18、w_E05_218 = 書き下しの型、稿 `218_MS準自由版と運動量相殺の反例_2026-10-18.md` 命題 218-C・系 218-D、成算 S80)— (E-H′) の第 2 連言に要る NC(窓に巨視的なモードが無い:$\lVert\gamma_W\rVert=o(\nu)$)を、反跳に敏感な入力 $\lVert(P_f+eA)\psi_0\rVert^2\le2mE_0$(補題 216-B の形の $\langle P_f^2\rangle$ の上界)と「巨視的なモードは相殺されない運動量を運ぶ」型の状態一般の下界 (MS′) の自己無撞着で出す方式
- **閉じたもの**:**方式**(命題 NC・(E-H′) の真偽ではない)。
- **理由**(解析、値に依らない):(1) 準自由な 2 モード圧搾真空(運動量 $\pm k_0$ の近くの幅 $\epsilon$ の波束 $f_1$、$f_2(k)=f_1(-k)$)は $\langle P_f^2\rangle=2n\sum_j\mathrm{Var}_{f_1}(k_j)\to0$、$\lVert\gamma\rVert/\mathrm{tr}\gamma=1/2$、$\sigma^2\to1+1/n$ — 箱の 2 モード模型では $P_f\equiv0$。ゆえに「$\langle P_f^2\rangle\ge c\lVert\gamma_W\rVert\Lambda^2-C\Lambda^2$」は準自由な状態でも偽。(2) 補題 216-B が状態から読む量 $n_A$($A(0)$ の集団モードの占有)は NC と独立:対の圧搾状態は $n_A$ 大・$P_f=0$・NC 成立、(1) の状態は $n_A\to0$・NC 不成立。
- **生き残るもの**:命題 218-B(準自由・単一モードの凝縮は $\langle P_f^2\rangle\ge n\langle f,\lvert k\rvert^2f\rangle$ を運び、$\alpha\lt\pi a^2/8$ で E05 族の基底状態の形になれない — 仮設の族の中での排除)。
- **再開条件**:2 モード以上の相殺する凝縮を**基底状態のエネルギー**で排除する変分の入力(状態一般の不等式ではないもの)が 1 つ供給されたとき。

## F111(2026-10-18、w_E05_219 = 書き下しの型、稿 `219_変分の入力と消費者の再付け替え_2026-10-18.md` §4.1・§4.2 系 219-C、成算 S81)— 行 E1-H の消費者(補題 212-1)の試行を、(i) 全運動量の射影つきの試行、または (ii) 別のユニタリな 1 体の流れのブースト $\Gamma(u_t)$(反跳を含むもの、流れの場 $V_z\ge0$)に付け替えて、(E-H′) の第 2 連言より弱い要求に移す方式
- **閉じたもの**:**方式**(命題 (E-H′)・(E1) の真偽ではない)。
- **理由**:(i) $P=0$ ファイバーはすでに全運動量の射影の像で、射影で試行の族を広げた最適な試行は $D_0^{-1}\pi_z\psi_0$、要求は (E1) そのもの(R9)。(ii) 補題 212-B の計算は流れの場 $V$ だけで書け、T1 は $\sigma^2(d\Gamma(V_z))$ に替わるだけ;定理 216-A の証明は窓の重みの形を使わず $h\ge0$ と台だけを使うので、$V_z\ge0$ の全ての流れで双極子の有限モード版が $\liminf\sigma^2\ge1/3$ — 新しい要求も双極子で破れる型のまま(系 219-C、定理 216-A〔self-audited、監査中〕に寄りかかる)。
- **限定**:符号を変える流れ、非ユニタリ・2 次元以上の試行(稿 §4.3 の回帰の候補)は閉じていない。
- **再開条件**:§4.3 の 2 次元の試行(対を作る 2 次の生成子を加えた回帰)で、双極子の有限モード版の残差の分散が 0 に行くことが示されたとき。

## F112(2026-10-18、w_E05_220 = 書き下しの型、稿 `220_2次元試行の回帰のkillcheck_2026-10-18.md`、成算 S82)— 行 E1-H の消費者(補題 212-1)の試行を $\mathrm{span}\lbrace B_w\psi_0,S\psi_0\rbrace$($S$ は対を作る 2 次の生成子)に広げ、T1 を $C_z$ の揺らぎの $S$ 方向への回帰の残差に替えて、(E-H′) の第 2 連言より弱い要求に移す方式(`219_` §4.3 の候補)
- **閉じたもの**:**方式**(命題 (E-H′)・(E1) の真偽ではない)。
- **理由**(解析の冪の勘定、値の水準):定理 216-A の双極子の有限モード版を孤立基準モード 1 本に縮めると、状態は圧搾真空($\langle x_0^2\rangle=\frac12e^{-2\rho}$、$n=\sinh^2\rho\to\infty$)で、2 次の作用素の分散が 0 になるのは $x_0^2$ の係数が $p_0^2$ の $e^{4\rho}$ 倍のときだけ。揺らぎを割合 $\delta$ 消す $S$ は $A(0)$ と交換せず(孤立モードは $A(0)$ の結合の方向)、場の副項を平均の 2 乗の $\gtrsim\alpha n\delta^2$ 倍に膨らませる。最良の回帰でも「残差 + 副項」の相対値は $1-O((\alpha n)^{-1})$ で 0 に行かない。
- **限定**:双極子は反跳を落とした別の模型で、これは (E-H′) の反証ではない。$A(0)$ とほぼ結合しない相殺凝縮(F110 の反例の型)では回帰は安く効きうる — 回帰が効かないのは双極子型の集団モードで、それを E05 族で一般に排除する入力は無い(命題 218-B は準自由・単一モードの族の中だけ)。冪の勘定は単一モードへの縮約(連続部分を $O(1)$ として落とす)に依る。
- **再開条件**:双極子型の集団モード($A(0)$ に結合した巨視的な単一の圧搾モード)を E05 族の基底状態で一般に排除する入力が供給されたとき。

## R4 再評価(2026-10-18、G3 統括 第 71 陣 w_G3_185、稿 (研究ノート: `185_R4再評価_3回の規約改定後の閉鎖の点検_2026-10-18.md`) §2.5)
- **再評価不要(まとめて)**: 本ファイルの全件。2026-09-28・09-29・10-17 の規約改定(質量・フェルミオン速度・光子速度の同調)は DM の族の格子切断族(`E06/03_` §8.1 項目 9)の規約で、E05 のフル Pauli–Fierz の模型の定義を変えない。

## F113(2026-10-18、w_E05_223 = 難所の型(w_E05_222 の再開)、稿 `223_WPの正面_pull-throughの判定と有限モードのtauQ_2026-10-18.md` §1、成算 S84)— 行 E1-H の第 2 連言に要る反跳条件 (W-P)〔窓のエネルギーの大半が全運動量 $o(\Lambda)$ の配位に乗る:$\tau_{Q_\Lambda}=\langle H_\theta\mathbf 1_{\lvert P_f\rvert\gt Q_\Lambda}\rangle/M\to0$〕の $P_f$ 側を、pull-through の 1 回目($a(k)\psi_0=-\frac emR(k)g(k)\cdot\pi\psi_0$ の $R(k)$ に入る $(\pi+k)^2/2m$)または $P_f$・$H_f$・$H_\theta$ の関数 $F$ による固有方程式の恒等式 $\langle[H,F]\rangle=0$ から出す方式
- **閉じたもの**:**方式**(命題 (W-P)・(SQ)・(E-H′) の真偽ではない)。
- **理由**(解析、値に依らない):(1) $R(k)$ が縛るのは $\pi+k$ で、窓で積分した $\int s\lVert(\pi+k)a(k)\psi_0\rVert^2$ は正規順序の計算で命題 222-C の $\langle H_\theta\pi^2\rangle$(+ $o(M\Lambda^2)$ の補正)に戻る;(2) (W-P) に要る $\int s\lVert(P_f+k)a(k)\psi_0\rVert^2=\langle H_\theta P_f^2\rangle$ は恒等式($a^*_k(P_f+k)=P_fa^*_k$)で、$eA a(k)\psi_0$ を pull-through で書き直すと交換関係 $[a(k),\pi_\mu]=k_\mu a(k)+eg_\mu(k)$ の同語反復になる;(3) $F=F(P_f,H_f,H_\theta)$ なら $[\pi_\mu,F]=e[A_\mu,F]$ なので、恒等式は $P_f$ を $\pi$ の中でしか見ず、$\pi$ と $eA$ の相関 $\mathrm{Re}\langle F^{1/2}\pi\psi_0,F^{1/2}eA\psi_0\rangle$ を分離できない。補題 223-A(三角不等式)により、(W-P) の第 2 モーメント版は (SQ)〔$e^2\lVert H_\theta^{1/2}A\psi_0\rVert^2=o(M\Lambda^2)$、窓の配位での $A(0)$ の圧搾〕と同値で、壁は「反跳の量」から「場の圧搾」へ言い換わるだけ。
- **限定**:閉じたのは 1 回目の pull-through と $F(P_f,H_f,H_\theta)$ 型の恒等式。2 回目の pull-through($a(k)a(l)\psi_0$、`215_` §4.3 (1) の共線の特異性)、$A$ を含む $F$ の高次の恒等式、位置表示での遮蔽 $p\approx-eA(x)$ のエネルギーの費用の評価、$\langle H_\theta A(0)^2\rangle$ の変分の上界は閉じていない。
- **再開条件**:$\pi$ と $eA(0)$ を窓の配位の上で分けて見る入力(遮蔽の場のエネルギーの費用の下界、または $A(0)$ の圧搾の下界)が 1 つ供給されたとき。

## F114(2026-10-18、w_E05_224 = 難所の型(w_E05_222/223 の再開)、稿 `224_SQの変分_遮蔽の費用のkillcheck_2026-10-18.md` §1〜§2、成算 S85)— 行 E1-H の第 2 連言に要る (SQ)〔窓の配位での $A(0)$ の圧搾 $e^2\lVert H_\theta^{1/2}A\psi_0\rVert^2=o(M\Lambda^2)$、(W-P) の第 2 モーメント版と同値(補題 223-A)〕を、「遮蔽 $p\approx-eA(x)$ を実現する配位(Wilson 線 $\mathcal P\exp(-ie\int A\cdot dl)$ の型)は場のエネルギーの費用が高すぎて基底状態で選ばれない」というエネルギーの比較の不等式から出す方式
- **閉じたもの**:**方式**(命題 (SQ)・(W-P)・(E-H′) の真偽ではない)。
- **理由**(冪の勘定、値に依らない):(1)〔2026-10-18 audit_S2_227(`229_` §6)で訂正〕長さ $\ell$ の直線の Wilson 線の場のエネルギー(真空からの Weyl 変位)は $\mathcal C(\ell)=\frac{e^2}2\int_{\lvert k\rvert\le\Lambda}\frac{d^3k}{(2\pi)^3}(1-\hat k_\parallel^2)\frac{4\sin^2(k_\parallel\ell/2)}{k_\parallel^2}\le\min\lbrace\frac{2\alpha}{9\pi}\ell^2\Lambda^3,\frac\alpha2\Lambda^2\ell\rbrace$、$\ell\Lambda\to\infty$ で $\frac\alpha2\Lambda^2\ell-O(\alpha\Lambda)$(経路にほぼ直交する硬いモードは振動しない;LL 1999 (4.16)(4.17) と同じ勘定;`223_` §1.4 の冪が正しく、当初この括弧に書いた「$\sim\alpha\Lambda$、硬いモードでは $\ell$ 倍にならない」は誤り)。遮蔽が自滅しない $\ell\lesssim1/\Lambda$(理由 (2))では $\mathcal C\le\frac{2\alpha}{9\pi}\Lambda\ll E_0$(補題 205-A:$E_0\ge m[\sqrt{\alpha/\pi}\lambda^{3/2}-\frac98\lambda]$)、LL 型の広がり $\ell=(mE_0)^{-1/2}$ でも $\mathcal C/E_0\le\frac{\pi^{3/4}}2\alpha^{1/4}\lambda^{-1/4}(1+o(1))\to0$;費用が $E_0$ を超えるのは $\ell\gtrsim2E_0/(\alpha\Lambda^2)$ の長い線だけで、それらは理由 (2) で既に自滅する側 —— ゆえに「費用が高すぎて選ばれない」は遮蔽の効く域で成り立たない(閉鎖の結論は不変);(2) 遮蔽が基底状態で選ばれない本当の理由は費用でなく運動学:Coulomb ゲージの $A$ は勾配でないので残差 $\lvert A^{\rm P}(x)\rvert\sim\lvert x-x_0\rvert\lvert B\rvert$ が残り、電子の広がり $\ell\gg1/\Lambda$ では $e^2\langle(A^{\rm P})^2\rangle\sim\alpha\ell^2\Lambda^4$ が遮蔽しない零点 $\alpha\Lambda^2$ より大きい(硬いモードの遮蔽は自滅);(3) (2) を不等式にする 2 本の道((a) $[\pi_\mu,\pi_\nu]=-ie\epsilon B(0)$ と $\pi$ の 4 次モーメントの二重交換子、(b) 平行移動した雲 $e^{iP_fy}\psi_0$ のエネルギーの超過)は、それぞれ $\frac{e^2}{m}\langle B(0)^2\rangle$(左辺の下界の係数の 4 倍で右辺に立つ)+ $\frac em\langle\pi \partial B(0)\rangle$(零点 $\Lambda^5$)、$\frac{e^2}{m}y^2\langle(\partial A(0))^2\rangle$(零点 $\Lambda^4$)を生み、点の場の勾配の零点 $\Lambda^{4+n}$ の階層で止まる。
- **限定**:閉じたのは「場のエネルギーの費用の比較」の方式。運動学の障害(curl)を不等式にする方式は、勾配の階層という障害を名指ししただけで閉じていない(平滑化した場 $A_\ell$ での立て直しは未試行;LL 1999 の下界の技法の照合は `227_` §1 で実施済み —— 非相対論の下界は電場 $\Pi(x)$ との交換子 + 局所モードで、得られるのは電場の反圧搾だけなので (SQ) の道具としては読めない、audit_S2_227 も同判定)。観察 224-A(交差項は光子数パリティで奇;$\psi_0$ がパリティ固有なら (SQ) は命題 222-C から従う;$H$ の奇の項は $\frac emP_f\cdot A$ だけ)により、難しさは「$\frac emP_f\cdot A$ が作るパリティ奇の成分が窓の配位で $P_f$ と $eA(0)$ の巨視的な反相関を作らないこと」に局在する。
- **再開条件**:点の場の勾配の階層を打ち切る入力(電子の広がりで平滑化した場の圧搾の下界、または $\langle B(0)^2\rangle$ を $\pi$ の 2 次モーメントだけで押さえる不等式)が 1 つ供給されたとき。

## F115(2026-10-18、w_E05_226 = 難所の型、稿 `226_K4の判定_準自由の影の変分と固有状態の恒等式_2026-10-18.md` §2・§4、成算 S86)— 行 E1-H の第 2 連言に要る (K4)〔定理 222-B の第 3 条件 $K_4^+=o(M^2)$、$K_4$ は補題 215-C の連結 4 点〕を、$\psi_0$ と同じ 1 体の量の中心化準自由状態との比較(不等式 (226-1))と、窓エネルギーの指示関数による枝の費用(命題 226-D)から出す方式
- **閉じたもの**:**方式**(命題 (K4)・(E-H′) の真偽ではない)。
- **理由**(値に依らない):(1) $\psi_0$ と同じ 1 体密度行列 $(\gamma,\alpha)$ を持つ準自由状態を試行にすると、$H_f$・$A(0)^2$・$\int\lvert k\rvert^2\rho$ の期待値は相殺し、残るのは $\iint(k\cdot l)C+2e\langle P_f\cdot A(0)\rangle\le0$ の 1 本(補題 226-A)—— 重みは符号不定の $k\cdot l$ で、(K4) の重み $s_ks_l\ge0$ とは連結 4 点の別のモーメント。回転不変な対の猫状態 $\psi_p$(A-225-2)は対の運動量が相殺するので左辺 $\le-\Lambda^2(r_1^2p-p^{-2})\lt0$ でこれを満たしたまま $K_4/M^2\to1$(系 226-A′)。(2)〔2026-10-18 audit_S1_226 で撤回:$f(H_\theta)\psi_0$ 型の試行の非負性が固有方程式から自動なのは指示関数で $c\ge E_0$ のときだけ;$c\lt E_0$ と一般の $f$ では最小性の非自明な内容($c\lt E_0$ の指示関数では $\mathrm{Re}\,t(\psi_\le,\psi_\gt)\le0$)で、閉じていない〕。(3) 窓エネルギー $c$ の枝の費用は命題 226-D の経路(固有方程式の帰結で、最小性は使わない)で $(c-E_0)^+$(命題 226-D、補題 215-A と同じ機構)—— 冪ではなく床。$E_0/M$ が 1 から離れている限り(命題 215-B の床、`416_` の値)、$[0,E_0]$ の中の着衣の双峰(枝が $0$ と $2M\le E_0$、$\sigma^2\ge1$、各枝のエネルギーが $E_0$ 近く;存在は示されていない)は 226-D では見えない。ただし反例に使った裸の猫状態 $\psi_p$ は $\langle H\rangle_{\psi_p}\ge E_\Omega+pr_1\Lambda\gt E_0$ で真空との比較に落ちるので、(1) の閉鎖は $E_0$ を消去した 1 本の不等式 (226-1) についてだけ成り立つ。(4) さらに (W-P)∧$\nu\to\infty$ の下では $\lvert\sigma^2-K_4/M^2\rvert\to0$(命題 226-E)で、(K4) は第 2 連言そのもの:「(K4) 専用の、$\sigma^2\to0$ より易しい道」は存在しない。
- **限定**:閉じたのは「(226-1) と 226-D」の方式。**閉じていないもの**(audit_S1_226):$\Gamma$ から作る他の準自由状態(例 $(t\gamma,t\alpha)$)や全ての準自由状態との比較($E_0\le E_{\rm qf}$、(226-1) より真に強い)、一般の $f(H_\theta)\psi_0$ 試行、$\psi_0$ の Bogoliubov 回転の 2 次の安定性 $\langle B\psi_0,(H-E_0)B\psi_0\rangle\ge0$($B$ は 2 次)—— 猫状態はこれらの反例にならない。固有方程式の 2 回の pull-through(全運動量 $k+l$ のレゾルベント)で連結 4 点のクラスタリングを直接評価する方式は、`215_` §5 の共線の非可積分の障害のまま未閉鎖(本稿では試みていない)。双極子では $C\equiv0$ なので、F109〜F114 と違い本方式は双極子ではなく猫状態で閉じる。
- **再開条件**:強結合($\Lambda^2/m\gg\Lambda$)の 4 次の反跳項をもつ基底状態について、窓の縮約状態が準自由状態に $K_4=o(M^2)$ の意味で近いこと(Bogoliubov 型の妥当性)を与える道具が供給されたとき。または類 C の kill-check(S86 第 1 手 (i):族の $\mathrm{Var}(T)/\langle T\rangle^2$ と $\mathrm{Cov}(T,H_f^{\rm out})$)が第 2 連言を否定側に動かしたとき(そのときは方式でなく標的の問題になる)。
- **F115 への追記(2026-10-18、w_E05_232 = 書き下しの型、稿 `232_F115再開条件の文献照合_強結合のBogoliubov近似の妥当性_2026-10-18.md`、成算 S90)**:再開条件の前半(強結合の 4 次の反跳項をもつ基底状態の準自由近似の妥当性を与える道具)は、**読んだ原典 11 本の範囲で文献から供給されない —— 判定 (b) 近いが渡らない**。型が同じ道具(Frank–Seiringer arXiv:1902.02489 Thm 2.3、Brooks–Seiringer arXiv:2207.03156 Thm 1.1・3.13 と 2211.03353 Thm 1.1、Lewin–Nam–Serfaty–Solovej arXiv:1211.2778 Thm 2.2 (iii))は、本質の仮定 (E1) 外部の小さいパラメータ(半古典 $[a,a^*]=\alpha^{-2}$・平均場 $1/N$)、(E2) 非退化な古典解(Pekar・Hartree)への凝縮、(E3) 場が 1 次と 2 次だけ/粒子数の保存 の 3 つで落ちる(E05:拡大と個数の再尺度化の族では $\hbar\to0$ で 4 次の係数が発散 —— 観察 232-A;$\langle a\rangle=0$;2 体の結合は 1 体の $\lambda$ 倍)。PF の準自由の文献(Bach–Breteaux–Tzaneteas arXiv:1301.0936、Bach–Hach arXiv:2004.06494)は準自由状態の上の変分で妥当性を与えない。光子数の高次モーメント(BHLMS math-ph/0106015 Ex. 6.1、LHB 2011 Cor 6.18・6.22・7.47、BCVV math-ph/0702098 Prop 3.1)は固定切断の絶対評価か表示式で、$1+o(1)$ 型は無い(判定 (c);`226_` §5.1 の [要確認] を確定)。**再開条件の前半は当面満たされない**;後半(類 C の kill-check)はそのまま。網羅は主張しない(未読:Feliciangeli–Seiringer のトーラス、Correggi–Falconi 系)。

## F115 への追記(2026-10-18、w_E05_233 = 難所の型、稿 `233_` §3 補題 233-D、成算 S91)— 限定の更新:$(t\gamma,t\alpha)$ 族の準自由試行も同じ理由で (K4) に届かない
- **閉じたもの**:**方式**(F115 の「エネルギーの最小性を試行状態で使う方式」のうち、監査 235 が未閉鎖と名指しした (a)「$\Gamma$ から作る他の準自由状態($(t\gamma,t\alpha)$ 族)との比較」)。命題 (K4)・(E-H′) の真偽ではない。
- **理由**(値に依らない):$\Gamma_t=t\Gamma+(1-t)\mathrm{diag}(0,1)\ge0$ の準自由状態のエネルギーは $E(t)=c_0+c_1t+c_2t^2$、$c_2=\frac1{2m}\iint(k\cdot l)(\lvert\gamma\rvert^2+\lvert\alpha\rvert^2)$(符号不定)。$E(t)\ge E_0$($t\in[0,1]$)は $-X\ge(1-t)[c_1+(1+t)c_2]$($X=\frac1{2m}\iint(k\cdot l)C+\frac em\langle P_f\cdot A\rangle$)で、(226-1)($t=1$)と真空の比較 $E_\Omega\ge E_0$($t=0$)の**内挿**。両者より強いのは $c_2\gt0$ かつ $-2c_2\lt c_1\lt0$ のときだけで、連結 4 点には依然 $k\cdot l$ の重みでしか触れない(エネルギーの 4 次の項は $P_f^2$ だけ)。猫状態は $c_1\gt0$($t_*\le0$)、双極子は $c_2=0$、背中合わせの対の状態は $c_2\lt0$ で、どれも強まらない。「全ての準自由状態との比較」$E_0\le\inf_\omega E^{\rm qf}(\omega)$ は $E_0$ の上界であって $\psi_0$ の 4 点に触れない。
- **限定**:監査 235 の未閉鎖 (b)($c\lt E_0$ の $f(H_\theta)$ 試行)は和則の不等号(変分原理)に含まれ、等式の大きさ(補題 233-A)以上の情報を持たない(`233_` §1.4 注)。(c)(2 次の安定性)の $B=H_\theta$ は補題 233-A そのもので、**閉じていない**:難しさは $\Delta_\phi$ の下界 (GAP-θ) に移った(`233_` §5)。$B$ が対の生成子の場合は未試行。
- **再開条件**:F115 本体と同じ。または (GAP-θ)〔$\Delta_\phi\ge c_ge^2\Lambda^3/(mM)$〕を下から押さえる道具(ギャップ無しの模型で、$\phi=(H_\theta-M)\psi_0$ と赤外の光子の状態との重なり $\mathrm{Cov}(H_\theta,a(f))$ の評価)が供給されたとき —— そのとき系 233-C により (W-P) の下で第 2 連言が出る。

## F116(2026-10-19、w_E05_237 = 書き下しの型、稿 `237_重みつきブーストの消費者_類Cの判定_2026-10-19.md` §2・§3、成算 S93)— 行 E1-H の消費者 `E05-P120` の付け替え:雲のブーストを窓エネルギーのセクターごとに速さ $\propto1/H_\theta$ で行う試行 $\eta=-sK\psi_0$、$K=f^{1/2}B_wf^{1/2}=\frac12\lbrace f(H_\theta),B_w\rbrace$ で、(E-H′) の第 2 連言 $\sigma^2\to0$ を片側の裾 (E-L′)〔$\forall K:\ P(H_\theta\le K\Lambda)\to0$〕に弱める方式
- **閉じたもの**:**方式**(この $K$ の族で (E-L′) と `E05-P117` だけから (E1) を出すこと)。命題 (E-L′)・(E1) の真偽、重みつきの試行一般は閉じていない。
- **理由**:発注の名指した $[B_w,f]$ は無害(補題 237-A:Doppler $\lvert\dot H\rvert\le bH_\theta/\Lambda$ で $\lVert[B_w,f]\rVert\le bc_f/\Lambda$、相対 $O(\delta\Lambda/\eta_0)$)。しかし $[A_\mu,K]\ni\frac12\lbrace[A_\mu,f],B_w\rbrace$ で、$[A_\mu,f]\approx f'(H_\theta)[A_\mu(0),H_\theta]$ が $\psi_0$ ではなく $B_w\psi_0$ に作用する(項 T6)。$B_w\psi_0$ は電子の運動量の共役(雲の重心と電子の相対変位)で、不確定性 $\lVert K\psi_0\rVert\ge\lvert\mathcal G\rvert/(2\sqrt{2mE_0})$(厳密)により $1/\Lambda$ でなく $1/(\delta\Lambda)$ の桁。冪の勘定で T6 の相対の大きさは $\nu\delta^2$ の減少関数(反圧搾の形、目安 $\frac16(e^2\kappa_3/(\nu\delta^2))^2$)で、$\nu\delta^2\to\infty$ でないと消えない —— 圧搾なしの形($\nu\delta$ の減少関数)は $\nu\delta\to\infty$ が定理((237-5)+`E05-P117`)なので消えるが、試行が成功するなら $K\psi_0$ の上で $D_\mu$ は反圧搾される(`E05-P124` の不確定性を $K\psi_0$ に当てる、監査 239 の補題 A-239-1)ので、反圧搾の形が判定を決める;`E05-P124` からは $\nu\delta^2\ge3\pi\alpha\kappa_3-o(1)$ しか出ず、上は $\nu\delta^2\le2mE_0^2/\Lambda^3$。物理:総シフトをセクターで揃えるには光子の放出のたびに各光子のシフトを $\Lambda/H_\theta$ ずつ配り直す必要があり、それが大きな相対変位に掛かる。交差項 T6′ は符号不定だが $D_0^{-1/2}$ の計量で $\phi_{\rm sr}$ に平行な成分しか打ち消せない(稿 §4 R2)。
- **難しさの保存**:212 の T1($\sigma^2$)は T1′ $=(1-q)$ 型と T6 に分かれた。σ² 型ではないが (E-L′) の尺度 $\Lambda$ では払えず、尺度 $\Lambda^3/(mE_0)$ の裾 (E-L″) と $B_w\psi_0$ の拡がりの上界 (R-B) の 2 本になる —— (E-L″) は (E-H′) から従わないので、(E-H′) より真に弱い条件にはならない。
- **限定**:判定は冪の勘定(因子化の目安)で、T6 の下界の定理ではない。$K\psi_0\in Q(H(0))$ も示していない。双極子での (E-L″) は未検査。
- **再開条件**:(i) 稿 `237_` §3.1 の **(E-L″)** と **(R-B)** の 2 本(または $\nu\delta^2\to\infty$〔$E_0\gg\Lambda^{3/2}m^{-1/2}$ 以上の情報、LL 1999 Thm 1.1 の下側の冪 3/2 を超える下界〕と **(R-B)**)が供給されたとき;または (ii) 放出のたびに他の光子のシフトを配り直さない(T6 の機構を持たない)セクター依存の試行が見つかったとき。R9:(E-L″)+(R-B) は (E1) の言い換えではない(静的な分布の裾と相対変位の 2 次モーメントの上界)が、(R-B) は $\lVert D_0^{-1}\phi_{\rm sr}\rVert$ 型で (E1) に近い側の量(稿 §3.2、灰色)。名指しは台帳に出さない(ID は稿の中のラベル)。

## F117(2026-10-19、w_E05_240 = 書き下しの型、稿 `240_否定の試行_準自由と積の族で相殺する凝縮は損_2026-10-19.md` §1・§3、成算 S95)— 行 E1-H の否定の候補:(E-H′) の第 2 連言を、準自由・積の試行の族の中で「運動量を相殺する巨視的な成分 C を足すとエネルギーが下がる」(NEG-CAND)ことから疑う方式
- **閉じたもの**:**方式**(試行の族の中で否定の構造的な支えを立てる筋)。命題 (E-H′)・$\sigma^2\to0$ の真偽ではない。
- **理由**(値に依らない部分):(1) ファイバーの積の状態では、鏡像の 2 モード成分は全ての幅で $n\ge4\alpha/(\pi a)$ なら足すと損、単一モード(双極子の集団モードを含む)は $\langle\pi^c\rangle_{\psi_L}=0$ のもとで $n\gt\alpha/(\pi a^2)$ で損(命題 240-B・系 240-C):成分の $A(0)$ との結合は運動量の広がり $V$ で押さえられ($\le V/\pi^2a$)、同じ $V$ が光子 1 個あたりの反跳を決める —— 相殺で反跳を逃れるほど結合も消える。(2) LL の全空間の積の族では (L) が族の厳密な下限(命題 240-D)で、(L+C) は下がれない。(値)(3) その最小は λ=1e4〜1e7(α=1・0.1)で、任意の 2 次元のモード空間が運ぶ窓のエネルギーの割合 $\rho_2$ が 0.06→0.007 と減る(`441b_`、NUM-?)。
- **限定**:閉じたのは台の分離した積の比較と族 (II)(ガウスの $\varphi$)の最小。**閉じていないもの**:成分 C と残りの雲がもつれた・モードを共有する試行、$\varphi$ が非ガウス・非等方の族、電子と場が相関した一般の試行 —— 基底状態の否定の候補が立つとすれば、台の分離した積と族 (II)(ガウスの $\varphi$)の外 —— 相関した状態、モードを共有する成分、多モードの圧搾の積、非ガウス・非等方の $\varphi$ —— である。
- **再開条件**:族 (II) の最小より低いエネルギーを持ち、窓のエネルギーの割合 $\ge0.2$ を 1 つの 2 次元のモード空間に載せる相関した試行状態の構成(数値または解析)。R9:これは (E-H′) と同値でない((E-H′) の否定は試行状態の構成を要さない)。

## F118(2026-10-19、w_E05_242 = 書き下しの型、稿 `242_もつれた集団成分の排除_2026-10-19.md` §1・§3・§4、成算 S96)— 行 E1-H の第 2 連言を、もつれた集団成分の排除から出す方式:命題 240-B の「成分の $A(0)$ との結合 ≤ 運動量の広がり ⟷ 同じ広がりが反跳」を積の構造なしに基底状態の縮約で書く道(T1)、補題 238-A〜C の単一成分 $\bar\Pi_\mu$ の畳み込みで集団成分の枝を外す道(T2)、補題 226-B と $\pi$ の分布の揺らぎを反跳で押さえる道(T3)
- **閉じたもの**:**方式**(3 道具の組)。命題 (E-H′)・$\sigma^2\to0$・NC・(SQ)・(K4) の真偽ではない。
- **理由**(値に依らない部分):(1) 240-B の Cauchy–Schwarz $\sum_\mu\lvert\langle g_\mu,f\rangle\rvert^2\le V_f/(\pi^2a)$ はモード $f$ だけの性質で状態を押さえず、240-B の結論に効く反跳の加法性 $\langle(P^U)^2\rangle=2nV$ は積の状態でだけ成り立つ。基底状態で同じ競りを書くと反跳の側は $\sum_\mu\lVert H_\theta^{1/2}P_{f,\mu}\psi_0\rVert^2\le2(x+y)M\Lambda^2$ で、エネルギーが押さえる $y$(222-C)と押さえない $x=e^2\sum_\mu\lVert H_\theta^{1/2}A_\mu\psi_0\rVert^2/(M\Lambda^2)$ の和 —— 222-A と合わせて $\lVert\gamma_s\rVert/M\le4u/a+2\sqrt{2u/a}$($u=\sqrt{x+y}$)、すなわち **NC ⟸ (SQ)** に帰着し(F113・F114 の壁)、窓で重みづけた遮蔽型 (S) を通す。(2) 単一成分の畳み込み(P129)とその固定の純粋な殻の状態への一般化は、双極子でも同じ結論を与える(`238_` R10 (iii))—— 双極子盲;もつれた成分は殻の上の固定の純粋状態に乗らない。(3) 226-B の恒等式は $\mathrm{Var}(H_\theta)=\mathrm{Var}(T+H_f^{\rm out})$ で R9 の同値変形;$T$ を鋭くしても、残るのは窓の外の光子のエネルギー $H_f^{\rm out}$ の鋭さ(補集合の窓の同じ型の問題)〔監査 246 §1.3:陽性対照 (L) による「偽に向かう」の判定は、(L) が固有ベクトルでなく $\mathrm{Var}(T)=\mathrm{Var}(H_f)$ を満たさないので成り立たない〕。表(稿 §1.2):双極子型 (D)・遮蔽型 (S)・隙間の無い着衣の広い分布 (C_cont) を同時に外し陽性対照を通す道具は、3 道具と既存の 222-C・P129 の中に無い。
- **生き残るもの**:補題 242-1(一意性 `E05-F22` から、窓エネルギーの分布に幅 $\gt2s_{\max}$ の質量 0 の隙間は無い;verifier-backed〔`246_`・`253_`〕)—— 隙間のある着衣の双峰と A-225-2 の猫を外す(定性的、双極子盲)。
- **限定**:閉じたのは縮約 1 体・2 体(とその畳み込み)で書ける道具。連結 3 点(パリティ奇の成分、観察 224-A)を量的に見る道具、2 回目の pull-through、隙間の無い分布の量的な排除(ギャップの無い $E_0$ のもとでの近縮退の評価)は閉じていない。遮蔽型 (S)・(C_cont) が低いエネルギーの状態として存在するかは未判定(存在すれば第 2 連言の反例の候補)。
- **再開条件**:窓で重みづけた $A(0)$ の圧搾 (SQ) の下界、または遮蔽 $P_f\approx-eA(0)$ の費用の下界(F114 の運動学の障害 —— 横波性で線形の遮蔽が消えること —— を連結 3 点まで延ばした不等式)が 1 つ供給されたとき。R9:(SQ) は第 2 連言と同値でない((SQ) が与えるのは定理 222-B の (W-P) の側〔NC〕までで、(K4) は別に残る —— 命題 226-E・A-225-2)。

## F119(2026-10-19、w_E05_243 = 書き下しの型、稿 `243_パリティ奇の成分とK4_2026-10-19.md` §1・§2、成算 S97)— 行 E1-H の (W-P)・(SQ) を、光子数パリティ $(-1)^N$ 奇の成分 $\psi_-$(ただ 1 つの奇の項 $\frac emP_f\cdot A$ が作る)の窓での小ささから出し、さらに (K4) へ進める方式(観察 224-A の「$\psi_0$ がパリティ固有なら (SQ) は 222-C から従う」の定量化)
- **閉じたもの**:**方式**(命題 (SQ)・(W-P)・(K4)・$\sigma^2\to0$ の真偽ではない)。
- **理由**(値に依らない):(1) $(\pi\psi_0)_{\rm ev}=P_f\psi_++eA\psi_-$、$(\pi\psi_0)_{\rm od}=P_f\psi_-+eA\psi_+$ の直交分解で、(SQ) に要る奇の小ささは窓で重みづけた $\lVert H_\theta^{1/2}P_f\psi_-\rVert$・$\lvert e\rvert\lVert H_\theta^{1/2}A\psi_-\rVert$ の $o(\sqrt M\Lambda)$ で、命題 222-C の下で (SQ)・(W-P)$_2$ と同値(補題 243-A、R9);(2) パリティの固有方程式(`E05-P33` 3.)が与える評価は $p_-\le p_++\kappa\epsilon_0$、$a_-\le2p_++\kappa\epsilon_0$、$p_+\le p_-+\kappa$、$a_+\le2p_-+\kappa$ で縮小しない —— 補題 223-A の三角不等式を偶・奇に割っただけで、遮蔽($p_\pm\approx a_\mp$)を許す(補題 243-B);(3) 重みなしでは (SQ$_0$) ⟺ $\delta=o(\Lambda^2/m)$(補題 243-C)で、$\delta$ の上界は $\lVert P_f\psi\rVert\lVert A\psi\rVert$ を要し循環;(4) 双極子は $\psi_-\equiv0$ で入力 (ODD) を最強の形で満たす(死因の型)—— 死因を免れさせるのは 222-C だけで、それは 223-A に既にある;(5) (K4) へは補題 226-A の右辺が $4m\delta$ になるだけで、重みは $k\cdot l$(F115 の死因)。
- **限定**:閉じたのは「パリティ奇の成分の小ささを入力にする」方式と、パリティの固有方程式からその小ささを出す筋。奇の成分の $P_f$ をエネルギー以外の量(場の配位の運動学)で押さえる方式は閉じていない(F113・F114 の再開条件の型)。値(2 次元横波の戯画 (研究ノート: `443_`)、希薄域)は奇の成分が小さく族 ≈ $H_{\rm e}$ の向きで、(SQ) の否定ではない。
- **再開条件**:F113 または F114 の再開条件(「$\pi$ と $eA(0)$ を窓の配位の上で分けて見る入力」、または「点の場の勾配の階層を打ち切る入力」)が満たされたとき —— そのとき本稿の補題 243-B の 4 本の片側(例 $p_-$)に縮小の係数が付くかを照合する。R9:再開条件は (SQ) の言い換えではなく、道具の型の供給。

## F120(2026-10-19、w_E05_244 = 書き下しの型、稿 `244_2次の応答とDelta_phiの下界_2026-10-19.md`、成算 S98)— 行 E1-H の候補 (iii):窓の分散関係の変形 $\lvert k\rvert\to\lvert k\rvert+ts$($H\to H+tH_\theta$)に対する基底エネルギーの 2 次の応答 $\chi_\theta=\langle\phi,(H-E_0)^{-1}\phi\rangle$ の上界(と CS $\mathrm{Var}^2\le N\chi_\theta$、和則 233-A)から $\sigma^2\to0$ を出す方式
- **閉じたもの**:**方式**(窓 $H_\theta$ の χ の各点の Λ での上界で双極子の死因を免れる筋;どの枝も ν の率を要する —— 監査 246 の A-246-1)。命題 (E-H′)・$\sigma^2\to0$・$\chi_\theta\lesssim M$ の真偽ではない。
- **理由**:(1) 要る強さは $\Gamma_\Lambda=(\chi_\theta/M)(\alpha\lambda/\nu^2)\to0$(補題 244-1:$\sigma^4\le(\chi_\theta/M)\Xi_\Lambda$、$\Xi_\Lambda\le\frac{2\pi\alpha\lambda}{\nu^2}(4\kappa_3g+\frac{2\kappa_4}\nu)+\ldots$)。(2) 確認者の見取りの形 $\chi_\theta\lesssim M$ は**双極子で成り立つ**(値:$\chi/M\to0.036$、$M/\Omega_{\rm coll}\to0.036$、CS の比 $\to0.99$;(研究ノート: `444_w_E05_244_dipole_chi.py`))—— 双極子が満たす入力で F109〜F114 と同じ死因。(3) 双極子を落とす力は $\nu/\sqrt{\alpha\lambda}\to\infty$ か、(W-P) と ν の率 $(\langle T\rangle/\Lambda)\nu^3\gg(\alpha\lambda)^2$ の組(監査 246 の A-246-1;どの枝も ν の率を要する)に移るだけ:前者は $E_0\ge M$ から $E_0/\Lambda^{3/2}\to\infty$(LL 1999 Thm 1.1 の下界の位数の改良 —— 指数の改良ではない)を含み、厳密な $\nu\gtrsim\lambda^{2/7}$(系 227-B と (U-L4c))に $\lambda^{3/14}$ 足りない;後者は未証明(E05-P123 の行)。(4) $\chi_\theta\lesssim M$ そのものも、要る精度の $E(t)$ の下界(誤差 $O(t^2M)$、補題 244-2)が既知の道具に無い —— 単調性 $E(t)\ge E_0$ は誤差 $tM$、凹性は曲率の平均 $\int_0^1\chi(t)dt\le M/2$ だけ(観察 244-3)、LL 型は冪に幅。(5) 新材料:命題 240-D は $E(t)$ の上界(向きが逆)、238 は双極子でも同じ結論(区別しない)。
- **再開条件**:$\nu$ の下界の率 $\nu/\sqrt{\alpha\lambda}\to\infty$ の証明(LL の下界の位数の改良を窓エネルギーで)、または (W-P) の証明と ν の率 $(\langle T\rangle/\Lambda)\nu^3/(\alpha\lambda)^2\to\infty$ が出たとき、補題 244-1 と補題 244-2 の精度の $E(t)$ の下界の組で再検討(閉じたのは窓 $H_\theta$・各点の Λ の範囲;窓のない $H_f$ の χ は λ の平均で無料 —— 監査 246 §3.6・A-246-3)(R9:どちらも標的と同値ではない —— 前者は第 1 連言の率、後者は第 2 連言より強い条件)。
- **副産物**:confirm_A-236 任務 4 の「双極子で $\chi_\theta\gg M$」は誤り(双極子は $M\ll\Omega$ の側)。補題 244-1・244-2・観察 244-3 は verifier-backed〔`246_`・`253_`〕。

## F121 — 「(Y1) 切断の Hellmann–Feynman 恒等式:殻密度 $\rho=\Lambda\partial_\Lambda(2G/m)$ の下界 $\rho\ge c(1-2G/m)$ から (E1)」(稿 245 §3.3・§4 の 1 行目、稿 `248_`、2026-10-19、w_E05_248、成算 S100)
- **閉じたもの**:**方式**(「(E1) への、閉じた変分の全方式の共通点を外した型違いの道」としての (Y1) のうち、恒等式 248-1 の項を別々に評価する形と、殻密度の下界を名指しにする形(R9)。因数分解の型 (RE-248) は閉じていない —— 監査 246 §4.5)。(E1)・Q3 の真偽ではない。
- **理由**(値に依らない部分が主):(i) 恒等式は `14_` 定理 3(流れ恒等式、2026-09-03)の $P=0$ 縮約レゾルベント版で新しい内容がない(稿 248 恒等式 248-1、(D-Λ) つきの形式);(ii) 観察 248-2:和則から $\rho/(1-2G/m)\equiv\Lambda\partial_\Lambda\ln h=\gamma$ —— 殻密度の下界は (E1) の率つきの微分形そのもの(`14_` 定理 5 の局所同値形)で状態の情報を含まず、R9 で落ちる;(iii) R5 系譜(F4・F5・F13)は Q3(上界)の向きで、この量を下から押さえる向きは閉じていない(F5 の値 $\gamma\to\frac12$ は下界の向きでは味方、F13 の天井 $\omega+\mathcal E\le2\Lambda$ は分母の上界で正の表示があれば下界の資源)—— 下からの向きの障害は (iv) の相殺(正の表示の欠如)だけ〔監査 246 §4.2〕;(iv) 恒等式の項で評価すると、双極子で殻の線形応答 $T_3=\kappa/(1+\kappa)\to1$ と 3 次の項 $-\kappa^2/(1+\kappa)^2\to-1$ が $1/h$ の精度で相殺する(補題 248-3、有限モードで厳密、verifier-backed〔`246_` §4.3・`253_`〕)—— 項を別々に評価すると $1/h$ の精度の相殺が要る;稿 245 の「評価が 1 尺度の速度応答に縮む」は双極子では因数分解 $\rho=T_3(1-2G/m)$ を通して真で、族では因数分解の成否 (RE-248) に懸かる〔監査 246 §4.4〕。
- **C0 の記録**:起動前に固定した判定文(双極子で $\rho/(1-2G/m)$ が $\lambda=10^2\sim10^4$ で正かつ単調なら GO)は GO(0.163→0.951、(研究ノート: `445_`))。ただし $r\equiv\gamma$ なので判定文は非識別的($h$ の単調増加を見るだけ)—— 判定文の設計の欠陥として記録。
- **厳密化の障害**(本稿で解かなかった理由):隙間の無い基底状態で Kato が使えない($(Y-\langle Y\rangle)\psi\in\mathrm{Ran}D$ が未知、P91 は $\mathrm{Ran}D^{1/2}$ まで);$P\ne0$ の $\psi_P$ が無い((A4)、E05-P103 の射程);鋭い切断では $\partial_\Lambda H$ が存在しない。厳密化しても (ii) により (E1) に効かない。
- **再開条件 (RE-248)**:反跳つきの E05 族(滑らかな切断)で、$\gamma=\Lambda\partial_\Lambda\ln h$ を**相殺の済んだ形で**明示的に正の殻応答 $T_3^{\rm dr}$(着衣の頂点つき)で表す厳密な恒等式(双極子では $\gamma=T_3$ が成り立つ —— その一般化)。R9:$T_3^{\rm dr}=\langle\xi,K\xi\rangle$($K\ge0$ は殻の場と $H_\Lambda$ から作る作用素、$\xi$ は $\psi_\Lambda$ から陽に作るベクトル)の形で、$h$ の関数に戻らないこと($T_3^{\rm dr}:=\gamma$ の自明な選び方を排除)。加えて滑らかな族から鋭い族(E05 族の定義)への (E1) の移し(または (E1) を滑らかな族で述べ直すこと)が要る〔監査 246 §4.5〕。成算【値】は未定〔監査 246 §4.5:1 ループの $T_3$ と非摂動の $\gamma$ の桁の不一致は双極子でも起きる($T_3\approx\kappa$ から $\kappa/(1+\kappa)\to1$)ので逆風の根拠にならない;F5 の $\gamma\to\frac12$ は下界の向きの値〕。

## F122(2026-10-19、w_E05_254 = 書き下しの型、稿 `254_dFRACの鎖_率bとEDGEの条件付き定理_2026-10-19.md` §1.2)— 候補表 `251_` 行 6:(RE-248) の因数分解 $\rho=T_3(1-2G/m)$(双極子で厳密)を反跳つきの模型へ延ばして (E1) の別経路にする方式

- **閉じたのは: 方式**(因数分解を近似的な恒等式として使う経路)。標的 (E1) と (RE-248) の殻密度の下界そのものの真偽は閉じない。
- **理由(値による閉鎖。T88)**:起動前に固定した判定文(`251_` §2 行 6:3 モード模型、λ=4〜64 で $\lvert\rho/(T_3(1-2G/m))-1\rvert$ が α=1/80 で $\le10^{-2}$、α=0.1 で $\le10^{-1}$)に対し、(研究ノート: `447b_w_E05_254_re248.py`)(`445b_` と同じ戯画・規約、3 モード、打切り N ≤ 12・16・20 で全桁不変)で α=1/80 の λ=64 が $1.8\times10^{-2}$(λ=4・16 は 4.7e−4・3.9e−3)、α=0.1 で 3.5e−3・2.7e−2・9.5e−2。双極子(反跳なし)では $\le3\times10^{-5}$(差分の誤差)。破れは λ とともに増え α に ≈ 線形 —— 反跳の 1 次の効果で、因数分解は双極子固有。
- **再開条件**:反跳つきの有限模型で、破れが $\lambda\to\infty$ で 0 に向かう域(例えば $\alpha\lambda^{2/5}\gtrsim1$ の非摂動域で dev の局所冪が負)を示す数値、または因数分解の補正項を (E1) の向きに符号づける恒等式。どちらも本稿の在庫には無い。
- **射程(T60)**:禁じるのは「$\rho=T_3(1-2G/m)$ を反跳つきの E05 族で近似的に成り立つ恒等式として使う」形の発注だけ。殻密度の下界 (RE-248) を別の道具で狙う発注、補正項の評価を狙う発注は止めない。

## F123(2026-10-19、w_E05_256 = 書き下しの型、稿 `256_EDGE-mean_縁のエネルギーの割合_2026-10-19.md` §2)— 定理 254-A(E05-P137)の名指し (EDGE-mean) を、1 光子の各点 pull-through と $M(k)=\langle\pi\psi_0,R(k)\pi\psi_0\rangle$ の上界(CS 経由)で示す方式

- **閉じたのは: 方式**(評価の型:$\rho(k)=\frac{e^2c_k^2}{m^2}\sum_\lambda\langle v_\lambda,R(k)^2v_\lambda\rangle\le\frac{e^2c_k^2}{m^2\lvert k\rvert}\mathrm{tr}_\perp M(k)$ と $M$ の上界の組み合わせ)。標的 (EDGE-mean) の真偽は閉じない(値の読みでは成り立つ側:保存済みの MPS で族の縁の割合 ≤ 双極子、LL の圧搾の絵で $p_{\rm edge}\approx3c$)。
- **理由(勘定)**:$M$ の最良の上界 $\mathrm{tr}_\perp M\lesssim m$(切断の Hellmann–Feynman の読み〔球面上〕、または殻の結合の単調性の仮定〔殻全体〕)でも $p_{\rm edge}(c)\lesssim\frac{2\alpha}\pi c\lambda\Lambda/M_f$、(LL-low)・(U-L4c) の下で $\sim\alpha c\lambda^{2/7}$ —— 1 体の評価($\alpha c\lambda$)より $\lambda^{-5/7}$ よいが $\lambda^{2/7}$ 足りない。損失は CS $\langle v,R^2v\rangle\le\lVert R\rVert\langle v,Rv\rangle$ そのもので、$M$ をどれだけ改良しても消えない。作用素の下界 $R\le X_\theta^{-1}$ は $R^2$ に渡らない;λ の平均(A-246-3 型)は全光子の拡大の量しか無料にしない。
- **再開条件**:縁の殻の上で $v=\epsilon\cdot\pi\psi_0$ の $H(-k)-E_0$ についてのスペクトル重みが底の近くに小さいことの評価(F62 の $F(\sigma)$・F52 (a) と同じ型)、または 2 光子 pull-through の背中合わせの配置($k+l$ 小)の重みの評価(`215_` §4.3 の共線の特異性を越えるもの)。
- **射程(T60)**:禁じるのは「$M(k)$(1 次のレゾルベントの期待値)の上界だけで縁の 1 光子密度を押さえる」形の発注だけ。$R(k)^2$ を直接見る評価、スペクトル分布の評価、殻ごとの割合の数値(λ=512 以上、殻の数の多い戯画)は止めない。〔注 2026-10-19 w_E05_292:「$\lambda^{2/7}$ 足りない」は固定の幅 $c$ の消費者 (EDGE-mean) に相対的。縁の層の幅を $\Lambda/\nu_f$ の尺度で動かす消費者(定理 292-A、(EDGE-ν))では CS の損失は障害でなく、$\mathrm{tr}_\perp M\le Cm\lambda^\theta$($\theta\lt\frac15$)で足りる(系 292-D、`292_` §3.3)。$M$ の上界そのものは依然無い(観察 292-E)。〕

## F124(「多尺度 —— 殻ごとの LL 型の下界 $\sqrt\alpha\Lambda_s^{3/2}$ の和で $E_0$ の冪 3/2 を超える」— 殻の分解は反跳を見ない。2026-10-19、hard_E05_LLlow_72、稿 `258_` §2.4 行 3)

**何を試したか**:$H_f=\sum_sH_{f,s}$・$A(0)=\sum_sA_s$(二進の殻)に分け、各殻で LL 1999 (2.12)+(2.16) の不確定性(交換子 $[eA_s,\Pi_s]\sim e\Lambda_s^3$、$H_{f,s}\ge c\Lambda_s^{-3}\Pi_s^2-\Lambda_s$)を使って下界を殻ごとに足す。

**正確な障害**:運動項 $(P_f+eA)^2/2m$ は殻で分かれず、不確定性は 1 度しか使えない。$\Pi=\sum_s\Pi_s$ に対して $\sum_s\Pi_s^2\ge(\sum_s\Pi_s)^2/N_s$ なので、殻ごとの和は 1 本の集団モードより $1/N_s$ 弱い。仮に足せても $\sum_s\sqrt\alpha\Lambda_s^{3/2}$ は幾何級数で最上殻の $\sqrt\alpha\Lambda^{3/2}$ の定数倍。12/7 と 3/2 の差 $\Lambda^{3/14}$ は動径の尺度ではなく、最上殻の中の運動量の胞($\lvert k+k'\rvert\lesssim1/L$ の対)の数 $(\Lambda L)^3$ から来る(稿 `258_` §2.2)。

**閉じたもの**:方式(殻ごとの下界の和)。標的 (LL-low) と命題の真偽には触れない。R9:双極子は各殻で同じ下界を満たす(反跳を見ない入力)。

**生きている分岐**:(NC-P)(反跳の無相殺、定理 258-A)と (TRANS)(翻訳コヒーレンス、命題 258-C)—— どちらも $\langle P_f^2\rangle_0$ の冪 θ を読む。

## F125(「反跳の係数の凹性 (REC-s) $E(1-s)\ge(1-Cs)E_0$ を、平方完成と 1 体の形の不等式 $A(0)^2\le\frac{2\Lambda}{\pi^2}H_f+\frac{\Lambda^2}{\pi^2}$ で閉じて (NC-P) を出す」— 在庫の下界は双極子型で反跳を見ず、$s\lesssim1/(\alpha\lambda)$ でしか閉じない。2026-10-19、hard_E05_B2B_72、稿 `262_` §3.2)

**何を試したか**:$H_t=tP_f^2/2m+e(P_f\cdot A+A\cdot P_f)/2m+e^2A^2/2m+H_f$ の基底エネルギー $E(t)$ は凹で $K=\langle P_f^2\rangle_0/2m$ が $t=1$ の上勾配(命題 262-B)、ゆえに $K\le(E_0-E(1-s))/s$。$E(1-s)$ の下界を、平方完成 $H_{1-s}=(1-s)(P_f+\frac e{1-s}A)^2/2m-\frac{s}{1-s}e^2A^2/2m+H_f\ge-\frac s{1-s}e^2A(0)^2/2m+H_f$ と形の不等式 $\sum_\mu A_\mu(0)^2\le\frac{2\Lambda}{\pi^2}H_f+\frac{\Lambda^2}{\pi^2}$ で作った。

**正確な障害**:$H_f$ の係数 $1-\frac s{1-s}\frac{4\alpha}\pi\lambda$ が正なのは $s\lesssim\pi/(8\alpha\lambda)$ だけで、そのとき $\langle P_f^2\rangle_0\le\frac{16\alpha}\pi\Lambda E_0+\frac{8\alpha}\pi\Lambda^2\lesssim\alpha\Lambda^2\lambda^{5/7}$ —— 1 体の自明な水準(θ=−5/7)。$s=O(1)$ で要る下界 $E(1-s)\ge(1-Cs)E_0$ は「遮蔽の状態 $P_f\approx-eA/(1-s)$($A(0)$ 大)が $E_0$ より高い」ことで、(NC-A) $e^2\langle A(0)^2\rangle_0\le CmE_0$ と同じ難しさ(循環)。落とした $(P_f+e'A)^2$ の項は遮蔽の状態でだけ小さく、一般の状態では大きいので、両方を同時に使う評価が要る —— 在庫に無い。戯画(s1、(研究ノート: `454c_`))では $E(1-s)$ が $s\gtrsim s_c(\lambda)$ で $E_0$ の数倍〜十数倍負に崩れるが、これは 1 モードの結合 O(1) の人工物を含み、連続体の (REC-s) の真偽は決まらない(値)。

**閉じたもの**:方式(平方完成 + 1 体の形の不等式)。標的 (NC-P)・(REC-s) の真偽は閉じない。**R9**:双極子は同じ下界を満たす(反跳を見ない入力 —— F124・F14 と同じ死因)。**射程(T60)**:禁じるのは「$E(1-s)$ の下界を $A(0)^2\le C\Lambda H_f$ 型だけで作る」発注。$(P_f+e'A)^2$ と $A^2$ を同時に見る下界(LL 型の不確定性を $H_{1-s}$ に当てる)は止めない。

## F126(E05、(L2.3-X) を LL Lemma 2.3 の直写しで閉じる方式 —— 余り $\mathcal R$ を $\lVert\Pi(0)\psi\rVert\langle G\rangle^{1/2}$ と在庫の不等式で項ごとに押さえる。2026-10-19、w_E05_263 = 書き下しの型、稿 `263_L2.3-X_反跳つきの不確定性と余りの評価_2026-10-19.md` §2.3・§3)
**何を試したか**:LL の Schwarz の型 $\langle\mathcal Q\rangle\le2\lVert\Pi\psi\rVert\langle G\rangle^{1/2}$($\mathcal Q=\sum_ji(\Pi_jY_j-Y_j^*\Pi_j)$、$Y_j=X_jG$)で、余り $\mathcal R=\mathcal B_1+\mathcal B_2+\mathcal D_S+\mathcal D_W$(補題 263-A:磁場 $[X_j,X_l]$ 由来・$\partial\Pi$ の対称・反対称部分)を項ごとに主項 $e\kappa\Lambda^3\langle G+2\mu^2G^2\rangle$ の 1/2 以下へ。道具は (a) $\pm(A^*B+B^*A)\le\epsilon A^*A+\epsilon^{-1}B^*B$、(b) $D$ を $G$ の外へ動かす交換子の展開、(c) $\lVert\Pi(0)\psi\rVert$、(d) $\Lambda^{-2}(\partial\Pi)^2$ 型の誤差を $H_f$ に払う。

**正確な障害**:(1) 命題 263-F:全ての ψ での「$\lvert\langle\mathcal R\rangle\rvert\le C\lVert\Pi\psi\rVert\langle G\rangle^{1/2}$」は (L2.3-X) と**同値**で、項の分け方は難しさを減らさない(反対称部分だけの評価は必要でも十分でもない)。(2) 補題 263-B:余りの作用素 $D_{lj}=-i[\Pi_j,P_{f,l}]$・$E_{jl}=i[P_{f,j},A_l]$ は局所の正準対 $(A(0),\Pi(0))$ の可換子にあり、$\lVert\Pi(0)\psi\rVert$ は可換子のユニタリで不変 —— (c) は余りを見ない。(3) (a) は真ん中の $G$ を $\sup G=\mu^{-2}$ で押さえるほかなく、加法の誤差 $\Lambda^6/\mu^2$ が $\Lambda^4$ に収まるのは $\mu\gtrsim\Lambda$(そこでは (L2.3-X₀) は自明);(b) は $[P_f,D]$ が 2 階の微分を生む塔で、各段の比 $\Lambda/\lvert X\rvert\gg1$($\lvert X\rvert^2\sim mE_0$)。(4) (d):余りは主項と同じく $G$ に比例し(真空で比 $O(1/e)$)、$G$ の重みを持たない誤差には吸収できない。

**閉じたもの**:方式(LL の型の直写しで余りを在庫の不等式で項ごとに押さえる)。標的 (L2.3-X)〔→ 弱化形 (L2.3-X₀)〕の真偽は閉じない —— 値(NUM の 455・455b)は真の向き(余りの和 +0.04〜+0.19 × 主項、可換子のずらしで Hardy 比は増える)。**R9**:双極子 $X\to eA$ では余りは厳密に 0(LL Lemma 2.3)—— 障害は反跳 $P_f$ に固有。**射程(T60)**:禁じるのは「余りを $\lVert\Pi(0)\psi\rVert$・$\sup G$・交換子の展開で押さえる」発注。止めないもの:余りの**和**の下からの評価に「$D$・$B$(可換子の場)のずれに $P_f$ の 2 次の揺らぎが伴って $X$ を広げる」型の符号の情報を使う方式。

## F127(E05、(L2.3-X₀) を局所の Hardy(LL Lemma 2.3)だけから出す方式、および十分条件 (XA-dom) $X^2+\mu^2\ge c_1(e^2A(0)^2+\mu^2)$ 経由の方式。2026-10-19、w_E05_265 = 書き下しの型、稿 `265_L2.3-X0_Hardy比とP_fの揺らぎの下界_2026-10-19.md` §2.4・§4)
**何を試したか**:補題 265-A の分解 $X=MA+N\Pi+P'$($M,N,P'\in\mathfrak A_0'$)で、局所の正準対の上の Hardy(LL Lemma 2.3)に帰着する;その最も簡単な形が (XA-dom)(命題 265-B で (L2.3-X) を与える)。

**正確な障害**:(1) 命題 265-D:係数を c 数に凍らせると $\mathrm{tr}M=3e$ を保ったまま $M$ を階数 1 にでき、局所の問題は 1 次元の Hardy の失敗に落ちて (L2.3-X₀) は破れる —— 局所の構造だけからは出ない(真偽は可換子の量子揺らぎだけにある)。(2) (XA-dom):戯画(diag8、α=1/80、μ²=0.1)で最小の一般化固有値は光子数の梯子 n=3〜7 で 0.493→0.297 と減り、最小化の状態は上の層(多光子の遮蔽の状態 $P_f\approx-eA$)へ移る —— 値で不支持(α=1/800 の σ=1 は格子の $P_f$ の隙間の人工物)。

**閉じたもの**:方式(局所の Hardy への帰着;(XA-dom) 経由は値の限定つき —— 遮蔽の状態が連続体で抑えられる可能性は残るが、(L2.3-X₀) より強い条件を立てる理由が無い)。標的 (L2.3-X₀) の真偽は閉じない(同じ戯画の Hardy 比は下に有界、NUM の 457)。**R9**:双極子では $M=e\mathbb 1$、$N=P'=0$ で (XA-dom) は等号 —— 障害は反跳に固有。**射程(T60)**:禁じるのは「$X$ を局所の変数の作用素として扱い、可換子の係数の揺らぎを使わない」発注と「(XA-dom) を名指しに立てる」発注。止めないもの:可換子の係数の量子揺らぎ(補題 265-C、$P'$ の 2 次の不確定性)を使う下界。

## F128(E05、(L2.3-X₀) の符号の情報を磁場の非可換性 $X_1^2+X_2^2\ge\mp e b_3$($b_3=E_{12}-E_{21}$、$B(0)$ の成分)の平均の形で取る方式。2026-10-19、w_E05_267 = 書き下しの型、稿 `267_L2.3-X0_条件付きの変位の代価とFisher情報_2026-10-19.md` §4)
**何を試したか**:`264_` の監査人の 1 行の観察($X_\perp^2\ge\pm eB$ 型)を作用素の不等式として導き(厳密)、退化した $M$ の近くで $X$ を下から押さえる材料にする。

**正確な障害**:$b_3$ は符号の無い可換子の場(p 型、$D$ の反対称部分と共役 —— 補題 265-C から $[D_{lj},b_3]\propto\delta_{l1}\delta_{j2}-\delta_{l2}\delta_{j1}$)で、2 つの不等式から出るのは $\langle X_\perp^2\rangle\ge e\lvert\langle b_3\rangle\rvert$ だけ;$X_\perp^2\ge e\lvert b_3\rvert$ は作用素としては出ない(Landau 型の下界は磁場が c 数で符号一定のときだけ)。針鼠型も定数の退化も $\langle b_3\rangle=0$ に置ける。

**閉じたもの**:方式(平均の形の使用)。標的 (L2.3-X₀) は閉じない。**R9**:双極子では $[X_1,X_2]=0$ で項自体が無い —— 反跳に固有。**射程(T60)**:禁じるのは「$\langle b_3\rangle$ の大きさで $X_\perp$ を押さえる」発注。止めないもの:$b_3$ の偶数次のモーメント(分布)と $D$ の反対称部分の共役を組み合わせた $X_\perp$ の下限の評価。

## F129(E05、(NPS$_\epsilon$) 近完全遮蔽の排除を、$P_f$ のセクター間の hopping の整合性(「条件付きの変位が $q$ を追う」費用)から**状態ごとの一様な形式の不等式** $\pi^2\ge cP_f^2-C$($C$ は状態に依らない)として出す方式。2026-10-19、w_E05_271 = 書き下しの型、稿 `271_NPS_近完全遮蔽の排除_2セクターの玩具_2026-10-19.md` §3・§4、成算 S115)
- **閉じたもの**:**方式**(命題 (NPS)・(NC-P)・(RATE) の真偽ではない)。
- **理由**:有限モードの玩具 T4(±k の対を持つ最小の玩具)で命題 271-B(self-audited)の明示の族 $\psi_q$ が $r=\langle\pi^2\rangle/\langle P_f^2\rangle=O(q^{-2/3})\to0$ を、1 体の変位の費用 $\kappa^3q^2/8g^2$ と主項で一致する $H_f$ で実現する —— ±k の対の数の圧搾で $n_{+}-n_{-}$ を鋭く保てば、変位を作る $\phi$ の hopping は平均の運動量を出さない。hopping の整合性が費用を生むのは各向きの $P_f$ 成分が非負の玩具(T2、補題 271-A)だけで、連続体には常に $\pm k$ がある。連続体では鋭い運動量のモードの結合が補題 271-C で抑えられるが、多数の細胞モードに分けて各細胞を巨視的に占有すれば同じ構成が移る(勘定、`271_` §4.3)—— 一様な形式の不等式はそこで偽になる向き。
- **R9**:双極子は (NPS) を破る($r_{\rm dip}\to0$)が、本方式の否定は双極子でなく ±k の対の数の圧搾で起こる(F109〜F114 の死因とは別)。F114(Wilson 線の費用比較 —— エネルギーを使う)・F125(1 体の形 $A^2\le C\Lambda H_f$)・F14(1 体閉包)と違い、本方式は 2 モードの hopping の構造を明示に持つ —— そのうえで状態ごとの下界は消える。
- **射程(T60)**:禁じるのは「エネルギー(基底状態の性質)を使わず、全ての状態で一様な $\pi^2\ge cP_f^2-C$ を出す」発注。止めないもの:(i) 基底状態のエネルギーの比較(遮蔽状態 vs EPR 型・双極子型)を使う方式;(ii)〔audit_S2_271_272 で撤回:反跳の大きさ $\lvert P_f\rvert\lesssim\Lambda$ に制限した不等式は、細胞を軟らかい殻へ移すと希薄を強制しない(`272_` §3、`273_` §5、勘定)—— 希薄は細胞の占有でしか書けず、1 体/2 体の数え上げの形は F130 で閉じた〕;(iii) 連続の向きの追跡に 267-B・C の型の代価を当てる方式(`271_` §4.4)。
- **再開条件**:鋭い運動量のモード(±の対;軟らかい殻 $\lvert k\rvert\ll\Lambda$ の細胞を含む —— audit_S2_271_272、`272_` §3)の巨視的な数の圧搾された占有を $\psi_0$ で排除する入力(P130 の積の族の外、もつれた成分を含む)が 1 つ供給されたとき —— 壁の 1 文((研究ノート: `_E1H_背景_72.md`))の一つの形。

## F130(E05、(NPS)/(NC-P$_\eta$) の希薄な枝を、遮蔽に要る 1 体の運動量の 2 乗(背中合わせの打ち消しの数え上げ、命題 272-B)で排除する方式 —— 条件 (DIL) $\theta_\mu(\psi_0)=\langle P_f^2\rangle_0/\langle d\Gamma(k^2)+\mu^2N\rangle_0\gt\frac{32\alpha}\pi(\frac12+\ln\frac\Lambda\mu)$ を供給して (RATE) を出す。2026-10-19、w_E05_272 = 書き下しの型、稿 `272_NPS_希薄な占有の下界と多細胞の玩具_2026-10-19.md` §1〜§3、成算 S116)
- **閉じたもの**:**方式**(命題 (NPS)・(RATE) の真偽ではない)。
- **理由**:命題 272-B(self-audited)は遮蔽の必要条件(θ が $O(\alpha\ln)$ 以下)を全ての状態で与えるが、ψ0 は 1 ループの 2 光子成分で既に $\theta\approx1.8\lambda^{-1/2}$(値、(研究ノート: `466_w_E05_272_oneloop_theta.py`);反跳の分母が対の全運動量を $\lvert k+k'\rvert\lesssim\sqrt{m\Lambda}$ に集める)—— (DIL) は偽の向きで、この必要条件では ¬(RATE) を排除できない。「希薄」を $\lvert P_f\rvert\lesssim\Lambda$ で定義する置き方も、軟らかい殻への尺度の移し(`272_` §3、勘定)で巨視的な占有の道が開くので立たない。
- **R9**:双極子の基底状態は θ=O(1) で (DIL) を満たす(対の向きが揃わない)—— 本方式は双極子では閉じず、反跳が作る背中合わせの集中で閉じる(F14・F9 と同じ機構、ただし 1 体閉包でなく 1 体/2 体の分解の数え上げ)。F129(状態ごとの一様な形式の不等式)とは、本方式が必要条件の不等式を厳密に持ったうえで ψ0 の値で破れる点で違う。
- **射程(T60)**:禁じるのは「$\langle d\Gamma(k^2)\rangle$ 対 $\langle P_f^2\rangle$ の比(背中合わせの打ち消しの量)だけで遮蔽を排除する」発注。止めないもの:交差項 $\langle(P_f\psi)^{(n)},a(c\epsilon)\psi^{(n+1)}\rangle$ の奇偶のコヒーレンスを直接評価する方式、エネルギーの比較の方式(ジョブ `g3_e05_272_multicell` の値を含む)。
- **再開条件**:F129・F117 の再開条件(もつれた成分の巨視的な占有の排除;軟らかい殻の細胞を含む)が 1 つ供給されたとき。〔audit_S2_271_272・R9:旧第 1 の枝「ψ0 の背中合わせの対が条件付きの変位の奇のコヒーレンスを作らないことを示す入力」は、交差項 $4e\,\mathrm{Re}\langle P_f\psi_0,a(c\epsilon)\psi_0\rangle=-4m\delta$ の大きさを抑えることそのもので (NPS) の言い換え(より強い形)に近いので外した〕

## F131(E05、近完全遮蔽の排除((RATE)/(NPS)/(NC-P$_\eta$))を Feynman–Kac の大偏差 —— $Z_t=\mathbb E_W[e^{-\frac{e^2}2\sigma^2_\Lambda(B)}]$ の上界 = $\sigma^2$ の下側の裾 —— で出す方式。2026-10-19、w_E05_274 = 書き下しの型、稿 `274_近完全遮蔽の排除_未着手の5角度_2026-10-19.md` §2.1、成算 S117)
- **閉じたもの**:**方式**(類 C で NO-GO)。命題 (RATE)・(NPS)・(NC-P) の真偽ではない。
- **理由**:(1) R9 —— $E_0=-\lim t^{-1}\log Z_t$ なので、率 $E/S\to\infty$ の下側の裾の評価は (RATE) の言い換えで入力ではない。(2) C0 —— 在庫の $Z$ の上界(反磁性 $\lvert\mathbb E_We^{ie\int\varphi\cdot dB}\rvert\le1$、Gauss 比較・時間の塊の Hölder、Donsker–Varadhan → Pekar 汎関数〔PF では φ=0 が最小、成算 5960 行〕)は双極子の核 $W(0,\tau)$ でも同じ形で立ち、位相の 1 体の扱いは核を単調に弱めて下界を下げる向き(F14)。
- **R9**:双極子は同じ上界を満たし (RATE) を破る —— F9・F14 と同じ死因(反跳を 1 体・Gauss の水準で見る)。
- **射程(T60)**:禁じるのは「経路の 1 時刻の観測量・Gauss 比較・反磁性で $\sigma^2$ の下側の裾を押さえる」発注。止めないもの:位相 $e^{ik(B_s-B_r)}$ の非 Gauss の 2 次カオスの下側の裾を、核の経路依存(背中合わせの 2 体のチャンネル)を使って評価する方式。
- **再開条件**:経路に依る核をもつ 2 次カオスの下側の裾の評価(Hanson–Wright 型の経路依存版)が文献か自作で 1 つ得られたとき。

## F132(E05、近完全遮蔽の排除を LLP・Gross 変換の後の有効ハミルトニアンの下界 —— $H(0)=H_{\rm dip}+R$、$R=(\pi^2-e^2A(0)^2)/2m$、双極子の部分を対角化して残差を下から押さえる —— で出す方式。2026-10-19、w_E05_274 = 書き下しの型、稿 `274_` §2.2、成算 S117)
- **閉じたもの**:**方式**(類 C で NO-GO)。標的の真偽ではない。
- **理由**:LLP は $P=0$ ファイバーの定義そのもの。近完全遮蔽の状態で $\langle R\rangle=T-\Phi\approx-\Phi$($\gg S$)なので下界は「着衣の光子のエネルギーが $\Phi$ を払う」ことに戻り、在庫の $R\ge-e^2A^2/2m$ は $H_f\ge0$、平方完成 + 1 体の形は F125。1 体の変位の費用 $\pi q^2/(4\alpha\Lambda)$ は反跳 $q^2/2m$ より安い($\alpha\lambda\gt\pi/2$、`269_` §2.4)ので 1 体の下界は遮蔽を許す。$P_f$ に条件付きの Gross 型の着衣は $\mathcal V_2$ の残差を残し(F6 命題 4)、変換は試行(上界、C1)としてしか働かない。
- **R9**:双極子では $R$ が無く同じ下界が等号 —— F125・F6 と同じ所。
- **射程(T60)**:禁じるのは「変換後の残差を 1 体の形の不等式で押さえる」発注。止めないもの:残差の 2 体の項($\mathcal V_2$)の下界を直接評価する方式。
- **再開条件**:F6 命題 4 の $\mathcal V_2$ 残差(対項)の下界が 1 つ供給されたとき。

## F133(E05、近完全遮蔽の排除を非摂動の多尺度 —— 尺度ごとの全運動量の予算 —— で出す方式。2026-10-19、w_E05_274 = 書き下しの型、稿 `274_` §2.3、成算 S117)
- **閉じたもの**:**方式**(類 C で NO-GO)。標的の真偽ではない。
- **理由**:(1) 予算 $\langle\pi^2\rangle_0\le2mE_0$ は 1 本で、殻ごとの正の部分は足せず($1/N_s$ の損、F124)、遮蔽 $P_f\approx-eA(0)$ は殻をまたぐ。(2) `273_` §5 の勘定で、近完全遮蔽の構成(軟らかい殻の細胞の条件付きの変位 + UV の圧搾)は要求精度 $\lambda^{-3/14}$ まで含めて窓 $\Lambda\lambda^{-11/14}\alpha^{-17/14}\lesssim\kappa\lesssim\alpha^{53/28}\Lambda\lambda^{-5/8}$ で各尺度の予算 $CS$ に収まる —— 予算の配分では排除できない〔2026-10-19 audit_S2_282_Y(`289_` §4、稿 282 の S2 PASS の後に有効):この構成は補題 282-A・282-B と E05-P121 で軽い裾の回転不変な状態として排除される —— 理由 (2) は無効、理由 (1) は残る;構成側の確認:稿 `291_` は窓を完全な試行状態にして BREAKS-AT(干渉性の雲は自身の反跳 ‖πΨ‖ で、反跳を消した理想化でも窓の光子数〔条件付けによる紫外の脱コヒーレンス〕で破れる;E05-P153・F144);audit_S2_282_X P-9 と同旨〕。
- **R9**:動径の尺度ごとの下界は双極子でも成り立つ(F124)。
- **射程(T60)**:禁じるのは「尺度ごとのエネルギー・運動量の予算と 1 体/2 体の数え上げで遮蔽を排除する」発注。止めないもの:構成と基底状態のエネルギーの比較(F129 射程 (i))。
- **再開条件**:F129・F117 の再開条件(もつれた成分の巨視的な占有の排除;軟らかい殻の細胞を含む)。

## F134(E05、(NC-P$_\eta$) を 2 光子 pull-through の運動量重み(262 A2)—— $\langle P_f^2\rangle=\int k^2\rho+\iint k\cdot k'\rho_2$ を $R_{12}$ の分母で窓 $\lvert k+k'\rvert\lesssim\sqrt{mE_0}$ に集中させる —— で出す方式。2026-10-19、w_E05_274 = 書き下しの型、稿 `274_` §2.4、成算 S117)
- **閉じたもの**:**方式**(類 C で NO-GO)。標的の真偽ではない。
- **理由**:(1) E05-P17 の 1.($\frac1{2s}\le\lVert R_{12}\rVert\le\frac1s$、E05-F20・F23)で、ノルムの水準は背中合わせとそれ以外を 2 倍以内で同じに扱い、双極子($\lVert R^{\rm dip}_{12}\rVert=1/s$)と同じ(C0)。(2) 値(`469_`):1 ループの集中 $\theta\propto\lambda^{-1/2}$ は分母 $q^2/2m$ が天井 $\lvert q\rvert$ を超える域だけから来て、天井で切ると θ=0.843(λ に依らない)—— 集中を出すにはスペクトルの位置の下界(2 光子を抜いたベクトルの $H(-q)$ のスペクトル測度が底から $q^2/2m$ 程度上)が要り、在庫は Chebyshev(λ 盲、F12 (c))と $\mathcal E(P)$ の下界(F13、閉)だけ。
- **R9**:双極子は窓を持たず θ=1;本方式のノルムの部分は双極子でも立つ —— F12 (c)・F48 と同型。
- **射程(T60)**:禁じるのは「$R_{12}$ のノルム(または $\mathcal E(-q)$ の天井・Chebyshev)で窓の外の $\rho_2$ を押さえる」発注。止めないもの:$H(-q)$ のスペクトル測度の底の近くの重みを、ψ0 の構造(エネルギーの比較)で直接評価する方式。
- **再開条件**:2 光子を抜いたベクトルの $H(-q)$ の低エネルギーの重みの λ で減る上界が 1 つ供給されたとき(F12 の再挑戦条件の転進先 (ii)(iii) とは別)。

## F135(E05、(NC-P$_\eta$) を Gibbs 経路測度で翻訳コヒーレンス $g(u)=\langle e^{iu\hat e\cdot P_f}\rangle_0$ を読む方式(262 A5)—— $g(u)=\mathbb E_\mu[e^{-\Delta(u)}]$(時刻 0 をまたぐ対の核のずらし)と Jensen。2026-10-19、w_E05_274 = 書き下しの型、稿 `274_` §2.5、成算 S117)
- **閉じたもの**:**方式**(類 C で NO-GO)。標的の真偽ではない。
- **理由**:形式の恒等式 $\langle(\hat e\cdot P_f)^2\rangle_0=\mathbb E_\mu[\Delta''(0)]-\mathbb E_\mu[\Delta'(0)^2]$ で、線の展開により $\mathbb E_\mu[\Delta'']=\langle d\Gamma((\hat e\cdot k)^2)\rangle_0$【形式】—— Jensen は θ≤1 だけを与え、双極子は θ=1 で飽和(C0)。双極子を外す部分は分散項が $\mathbb E_\mu[\Delta'']$ に相対精度 θ で一致することで、(NC-P$_\eta$) の言い換え(R9);経路測度の在庫(RP・Gauss 参照、E05-F19)は分散の下界を出さず、2 体閉包は F6 命題 3・F7 命題 D で閉。
- **R9**:分散項による (NC-P) の書き換えは同値変形で名指しにしない。
- **射程(T60)**:禁じるのは「$g(u)$ の Jensen・キュムラントの恒等式・RP で $\langle P_f^2\rangle$ を押さえる」発注。止めないもの:$\mathbb E_\mu[\Delta'(0)^2]$ を経路測度の別の構造(時刻 0 をまたぐ相関の正値性と大きさ)で下から評価する方式 —— ただし (NC-P) と同じ難しさ。
- **再開条件**:Gibbs 経路測度の時刻 0 をまたぐ作用の勾配の分散の下界(背中合わせのチャンネルを見るもの)が 1 つ供給されたとき。

## F136(E05、全列への延長:$h$ の λ 単調性・倍尺度の正則性を、凹性・結合凹性(`E05-P107` 1.)・変分の特徴づけ(補題 199-B)・PF の形だけから出す方式。2026-10-19、w_E05_276 = 書き下しの型、稿 `276_全列への延長_hの倍尺度の正則性_2026-10-19.md` §2・§4.1、成算 S119)
**何を試したか**:$E_u$ の $u=1/m$ についての凹性と $(u,uP)$ の結合凹性で、異なる $u$ の $E(p)-E_0$ を比べて曲率 $1/h$ を比べる。
**正確な障害**:(1) どの比較も $E_0$ の凹性の欠損 $\beta=E_u+(u'-u)\langle Q^2/2\rangle_u-E_{u'}\ge0$(運動量に依らない)を含み、$p^2$ で割ると消えない;$u'\to u$ と $p\to0$ を組むと微分の水準に落ち、結合凹性の Hessian は $E_0''\lt0$ の点で $\partial_w^2\mathcal G\le0$ 以外を課さない(S-A3-2 推論 2 の MON-m の向きの記録と同じ型)。(2) 値:有限モードの戯画(反跳つき、殻 1 つ 4 モード、α=0.1、打切り n≤10・12 で収束)は上の構造を全て満たして $h$ が λ≈8 から 21% 下がる((研究ノート: `471_w_E05_276_toy_h_fine.py`)・`471b_`)—— 構造だけの議論は単調性も倍尺度の正則性も出せない(有限モードの飽和 E05-F5 の型;A3-05 の別の幾何では (CONC-Λ) が生存しており、向きはモードの幾何に依る)。
**閉じたもの**:**方式**(構造だけの議論で (a)(b) を出す形)。命題 (a)・(b)・(REG-δ$_a$) の真偽ではない(E05 族の連続体の値は単調:A1 の倍尺度の比 1.40〜1.57)。戯画の $h$ は解析的で (REG-δ$_a$) を満たす —— (REG-δ$_a$) はこの閉鎖の外。
**再開条件**:連続体のモードの分布($\lvert k\rvert\lesssim m$ の層)を使う比較の道具(相関不等式、FK の Λ 単調性の $P\ne0$ 版、または K3 の加速項の符号)が在庫に入ったとき。R9:(a)(b) は (E1) の同値変形でない($h\equiv$ 定数)。

## F137(E05、二分の経路の ¬(RATE) の枝:近完全遮蔽の情報(2 点量 $T,K,\Phi$ と 3 点量 $\delta$、補題 269-B)を変位型(C1、Weyl 変位 $W(f)\psi_0$ = 補題 275-A)の試行に入れて $h\to\infty$ を直接出し、(RATE) を迂回する方式。2026-10-19、hard_E05_dichotomy_72 = 難所の型、稿 `275_二分の経路_近完全遮蔽の枝でhを直接_2026-10-19.md` §4〜§5、成算 S118)
- **閉じたもの**:**方式**(¬(RATE) の枝の命題 (N-prop$_R$)〔$E_0\le R(\lambda)S$ の列で $h\to\infty$〕を、269-B の遮蔽の構造を変位型の試行に入れて出すこと)。(E1)・(RATE)・(N-prop) の真偽、二分の定式化(命題 275-B、正しい並べ替え)、補題 275-A の下界の形は閉じていない。
- **理由**(値に依らない部分):(1) 遮蔽の 2・3 点の情報をそのまま受け取れる消費者は変位型の試行(`E05-P118` の族の中の Weyl 変位、補題 275-A)だけ —— P120 は $\sigma^2$(4 点)、和則のスペクトル形は $\pi_z\psi_0$ の低エネルギー端(F3 の B8)を要る(稿 §1.2)。(2) 補題 275-A の費用 $\sum_j\langle\Phi(k_jf)^2\rangle_0$(変位モードの反跳の直交位相)は、遮蔽が圧搾する量 $\Phi(k\phi)+e\Phi(c\epsilon)$ とは別物で、¬ の枝では $A(0)$ が圧搾されていない($\Phi\gg S$、269-B)ので真空級に残る —— 平均場の勘定で $h_W\lesssim\frac32$(稿 §5)。(値)(3) 戯画(`422_` 核、1 殻 12 モード、α=1/80、λ=64)で遮蔽を作った族 $H_s$ は $T/K$ 14 → 0.4 で $h_W$ 0.55 → 0.75(真空 1.22、n=6→8 で安定);fam の基底状態は遮蔽域に届かず INCONCLUSIVE(METHOD)((研究ノート: `470_`))。
- **共通点**:**F2**(2026-09-02、ψ0 に錨を下ろしたコヒーレント試行、判定基準 $\mathcal N(k)=\langle\Phi(h_k)^2\rangle_0/\lVert h_k\rVert^2\asymp1$)と同型 —— 遮蔽の情報は $\mathcal N$ を下げない。試行側 C1「1 体生成子 × 同じ ψ0」(245 §3.1)の線形生成子の版。
- **限定**:判定は平均場の勘定と 1 殻の戯画の値で、¬ の枝の列($K\approx\Phi\approx\delta$、相対精度 $\lambda^{-3/14}$、$\sqrt{\alpha\lambda}$ 個の光子)を模していない。(N-prop) 自体の真偽は未判定(¬(RATE) の点での (E1) そのもの、R9)。
- **再開条件**:(i) ¬(RATE) の列で変位モードの反跳の直交位相の圧搾 (SQZ) $\sum_j\langle\Phi(k_j\tilde f)^2\rangle_0=o(e^2)$($d=1$)を与える入力(2 点の不等式でない、$B_\perp$ または $\partial A$ の圧搾の情報〔2026-10-22 監査 626 §5.3:**向きが逆** —— 補題 620-C(Robertson)で $\Phi(k_j\tilde f)$($\tilde f$ が A のモード関数の実の倍なら ∂E 型)の圧搾は ∂A・$B_\perp$ 型 $\Phi(ik_j\tilde f)$ の**反圧搾**と組。要る入力は「∂E 型(場の運動量の直交位相)の圧搾、同値に ∂A・$B_\perp$ 型の反圧搾」;偏光の規約に依らない〕)が供給されたとき;または (ii) $\pi_z\psi_0$ のスペクトル測度の低エネルギー端(質量 $\frac{2m}3T$ のほぼ全部が $E_0+O(S)$ 以下)を 269-B の型の入力から出す道具が見つかったとき。R9:(i) は (E1) の言い換えではない(2 点量の圧搾;補題 275-A で (E1) の十分条件)。

## F138(E05、行 E1-H の第 2 連言 σ²→0 を、準自由の 4 分解 $\sigma^2=\mathrm{Poi}+\Gamma_2+\mathrm A_2+K_4/M^2$ の各項 → 0 から直接組み、(RATE) を通らない (E1) への道にする方式。2026-10-19、w_E05_278 = 書き下しの型、稿 `278_ANGBBと準自由の4分解_σ²の各項_2026-10-19.md` §2・§3・§4、成算 S121)
**何を試したか**:ジョブ 251r2(J1 GO・J2 QF、NUM-6466・6467)の 4 分解を受け、双極子を止めている項を特定してその → 0 を在庫の 1 体・2 体の評価で出す。
**正確な障害**:(1) 双極子を止めるのは $\Gamma_2$ だけ($g=\frac13$、補題 278-A (ii) の上限;$\mathrm{Poi}\le1/\nu$ は消え、$\mathrm A_2\le1/\nu+g$ は従属、$K_4=0$)で、$\Gamma_2\to0\iff$ NC。(2) NC ⟹ (RATE)(補題 278-B、A-246-2 の 2 行の系)—— 項ごとの経路は (RATE) を必ず通る。(3) 在庫で NC に届く入口は補題 222-A の (W-P) だけで、(W-P) を出す方式は F113・F114 で閉、(W-P) ⟹ (RATE)(系 278-D)。(4) (RATE) を通らない枝(¬(RATE) の列)では、σ²→0 は $K_4/M^2\le-3g_C^2$ の巨視的な負の連結 4 点を要する(命題 278-C)—— $K_4$ に戻る。(5) 値:24 モードの戯画は $g\ge\frac1{12}$ に縛られ、NC と ¬(RATE) の枝を判定できない。
**閉じたもの**:**方式**(項ごとに → 0 を示して (RATE) を迂回する形)。命題 σ²→0・(E-H′)・NC・(RATE)・(K4) の真偽ではない。
**再挑戦条件**:¬(RATE) の列(近完全遮蔽、補題 269-B)の基底状態で、$A(0)$ 方向の凝縮の多重項について連結 4 点の負の符号と大きさ($K_4\le-(1-o(1))\mathrm{QF}$、凝縮の反束化)を評価する道具 —— 数状態型の集団モードを扱える非摂動の入力。または (RATE) の証明(このときは既存の消費者 254-A・269-A が先に (E1) を密度つきで与える)。

## F139(2026-10-19、w_E05_283 = 書き下しの型、稿 `283_SPEC-GとRATE_頂点補正つきの帯の模型_2026-10-19.md`)— (SPEC-G) を (RATE) から独立に立てる読み「反跳で 1 光子の帯の G の重みが δ より上へ逃げ、遮蔽なしに $r(\delta)\to0$」(`280_` §2・§4)

- **閉じたのは: 方式(読み)**。標的((SPEC-G)・(E1))と命題の真偽は閉じない。
- **理由(値 + 1 段の解析、T88)**:280 自身の模型(反跳 1 次の RPA)で、遮蔽前の帯の G の重みは $d\nu_0=\frac{g dr}{1+\lambda r/2}$ —— エネルギーについて $[\Lambda/\lambda,\Lambda\lambda/2]$ で対数一様で上端に集まらない。$r(\Lambda\lambda^a)\approx\frac{1+a}{1-a}\frac1{h-1}$(475b の値で α=10:$r(h-1)$ = 3.38→3.55、α=100:4.22→3.73、極限 4.09)—— $r\to0$ を運ぶのは $\lvert1+\kappa\chi_0\rvert^{-2}$ の遮蔽で、$h\to\infty$ に依る。系 277-C が要る系自身の尺度 $\delta=\epsilon^{1/2}E_0$ では $r$ = 0.32・0.35・0.35・0.35(α=1、λ=10²→10⁵)で減らない。頂点 $P_f\cdot A$ を入れた模型 M1(小結合)は重みを補題 283-A の底(≤2Λ)の側へ動かし、系の尺度の $r$ を上げる。
- **生き残るもの**:(SPEC-G) の機構は全模型で「遮蔽 $r_{\rm band}\approx W_{\lt\delta}/h^2$」—— 裸の反跳の読みなら $h\to\infty$ だけで足り、底の読みなら $h\gg\sqrt{\alpha\lambda}$((RATE) の率)が要る(`283_` §6)。どちらかを決める強結合で頂点つきの値は未(正値性を保つ連続運動量の Tamm–Dancoff が要る)。
- **再開条件**:E05 族(または $(P_f+eA)^2$ の正値性を保つ強結合の模型)で、1 光子の通路の G の重みが反跳の側($\gg\delta$)に、遮蔽と無関係に乗ることを示す値か評価。

## F140(E05、(RATE) 本体・角度 A の変種:双極子に反跳の 1 体の部分 $d\Gamma(k^2)/2m$ を加えた 2 次形式 $H_q=H_f+d\Gamma(k^2)/2m+e^2A(0)^2/2m$(および $A(0)^2$ の正の係数を持つ任意の 2 次形式 $Q$)を厳密に対角化し、$H(0)-Q$ の下界で (RATE) を出す方式。2026-10-19、hard_E05_RATE_A_72 = 難所の型、稿 `281_RATE_角度A_双極子の着衣を外した後の下界_2026-10-19.md` §3.3、成算 S123)
- **閉じたもの**:**方式**(類 C で NO-GO)。(RATE)・(NPS) の真偽ではない。角度 A 本体(双極子だけを対角化)は F132 と同型で新しい F 番号を立てない(`281_` §1)。
- **理由**:(1) $H(0)-H_q=(\sum_{i\ne j}k_i\cdot k_j+e\lbrace P_f,A(0)\rbrace)/2m$ は下に有界でない(背中合わせの相殺で $\sum_{i\ne j}k_i\cdot k_j\to-d\Gamma(k^2)$;族の基底状態の $\rho_{\rm B2B}$ 0.93→0.996、NUM-6432)。一般に $H(0)\ge Q$ が作用素不等式として成り立つには $\pi\varphi\approx0$ の状態で $\langle Q\rangle\le\langle H_f\rangle$ が要り、$A(0)^2$ の正の係数を持つ $Q$ はそこで破れる —— 「$H(0)\ge Q+(\text{反跳を見る正の項})$」の入力は (NPS) そのもの。(2) 値【T88】:連続体で $E_q$ の冪は 1.000($E_q\approx0.16\alpha\lambda\Lambda$、摂動の $e^2\langle A^2\rangle/2m$ の位数で LL の上界 5/7 より上);戯画(s1 n=10、λ=256)で $E_q\approx2E_0$。2 体の項は $E_q-E_0\sim E_q$ の大きさで摂動でなく主役。
- **R9**:双極子($R=0$)では $Q=H_{\rm dip}$ で等号(下界 0 = (RATE) の境目)。(RATE) の同値変形ではない(方式の話)が、要る入力は (NPS) のエネルギー比較(`274_` §3)。
- **共通点**:F14(1 体閉包の一般化された閉鎖:反跳を 1 体・Gauss で繰り込む閉包は双極子の線形上界を破らない)の**下界の向きの現れ**。F125・F132(1 体の形の残差の下界)と同じ場所。
- **射程(T60)**:禁じるのは「反跳の 1 体の部分を 2 次形式に繰り込んで対角化し、残りを下から押さえる」発注(分散の変更・Gauss 閉包・自己無撞着の 2 次形式を含む)。止めないもの:2 体の項の下界を非摂動で直接評価する方式(F132 の再開条件)。
- **再開条件**:F132 の再開条件(F6 命題 4 の $\mathcal V_2$ 残差の下界)が 1 つ供給されたとき。

## F141(E05、(RATE) を Lieb–Yamazaki の交換子 $a(k)=\lvert k\rvert^{-2}k\cdot[a(k),P_f]$ で**相互作用の上界**として当てる方式(ポーラロンの LY・Lieb–Thomas の型の直写し)、およびポーラロンの強結合の下界の段(局在 + コヒーレント状態の Pekar 汎関数、Brooks–Seiringer の $E(P)$ の段、Dybalski–Spohn の有効質量の公式)を $E_0$ の下界に移す方式。2026-10-19、hard_E05_RATE_B_72 = 難所の型、稿 `282_` §1、成算 S124)
- **閉じたもの**:**方式**((RATE)・(NPS) の真偽ではない。(RATE) 自体は同じ稿の定理 282-C で別の形〔LY を $\pi$ との不確定性に組み替える〕により candidate で閉じた)。
- **理由**:(a) ポーラロンでは相互作用が線形で負なので LY の上界 $\lvert\langle\phi(v)\rangle\rvert\le C\lVert p\psi\rVert\lVert N^{1/2}\psi\rVert$ が下界の主役で、$p^2$ が局在の費用を払う。PF のファイバーでは「相互作用」は平方 $\pi^2\ge0$ の中にあり、負の項 $2eP_f\cdot A(0)$ の上界は CS(遮蔽 = CS の飽和)が最良;LY で紫外を $\lVert P_f\psi\rVert$ に払わせると遮蔽の状態($\lvert P_f\rvert\sim e\Lambda\sqrt N$)では CS より弱く、出るのは「遮蔽には $N\gtrsim1/(\alpha\ln)$ の光子が要る」だけ。$P_f$ の費用が $H$ に無いので、$\lVert P_f\psi\rVert$ を含む上界はエネルギーに戻らない(F129 と同じ所)。(b) コヒーレント状態(Berezin–Lieb)の下界は PF の古典汎関数の最小が $A=0$ で空(成算 5960 と同じ);Brooks–Seiringer・Dybalski–Spohn は $E(P)-E(0)$ の道具で $E_0$ の Λ 依存に向かない(Λ 固定、`E05-L8`)。
- **R9**:(a) は双極子で止まるのではなく、$P_f$ の費用の不在で止まる(F129 の型)。(b) は全ての交換子を落とす C0 の極端な形。
- **射程(T60)**:禁じるのは「LY の恒等式を相互作用の上界として使う」「Pekar 型の古典汎関数を PF の主項にする」発注。止めないもの:LY の恒等式の**不確定性への組み替え**(定理 282-C)、その冪の改良(多殻・2 次モーメントの精密化)。
- **再開条件**:なし(同じ稿で別形が立ったため、この方式に戻る理由は無い)。

## F142(E05、二分の経路の ¬(RATE) の枝:近完全遮蔽の情報(補題 269-B の 2 点量 $T,K,\Phi$・3 点量 $\delta$)から、σ² を経ない消費者 —— B8($\pi_z\psi_0$ のスペクトル測度の二峰・低エネルギー端 $E_H\to\frac43T$)、(SQZ)(変位モードの反跳の直交位相の圧搾)、$P_f\psi_0$ 型の試行 —— の入力を出して $h\to\infty$ を示し、(RATE) を迂回する方式。F137 の拡張。2026-10-19、hard_E05_SQZ_B8_72 = 難所の型、稿 `285_¬RATEの枝のE1_SQZとB8_2026-10-19.md` §1〜§3、成算 S126)
- **閉じたもの**:**方式**(¬(RATE) の枝で、遮蔽の 2・3 点の情報から σ² を経ない消費者の入力〔勾配モードの直交位相の圧搾、または $\mu_{\pi_z\psi_0}$ の低エネルギー端の下界〕を出すこと)。(E1)・(RATE)・(N-prop)・(SQZ)・(SQZ-N) の真偽、組んだ形(命題 285-A:(U-L4c) ∧ (EDGE-mean) ∧ (SQZ-N$_R$) ⟹ (E1) on 2/7 の集合、正しい合成)は閉じていない。
- **理由**(値に依らない部分):(1) σ² を経ない消費者(B8 の単峰形・変位型 275-A・$P_f\psi_0$ 型・2 体生成子)が要るのは、勾配モード $k_jg$・$k\times g$($g=c\epsilon$ = $A(0)$ のモード、または変位モード)の直交位相(位置型 $\Phi(k_jg)$ か運動量型 $\Pi(k_zc\epsilon_j)$)の真空比 $o(\alpha)$〜$R^2/\lambda$ への圧搾、または $\mu$ の低エネルギー端の下界(稿 §1.2)。(2) 遮蔽(269-B)が縛るのはモード $g$ 自身の 2 点量と $P_f$ との 3 点相関で、$\int k_j\lvert g\rvert^2=0$(偶)により勾配モードは $g$ に直交し、準自由の読みでは独立 —— 情報は伝わらない(F137 の理由 (2) を全消費者に拡張)。(3) $P_f\psi_0$ 型の試行は利得 $\frac{4m}3(K-\delta)\lesssim\frac{4m}3\sqrt{TK}$ が 269-B で上から押さえられ、$\frac2mG\lesssim\frac{32\pi TK}{3\alpha\lambda^2\Lambda^2}\to0$(稿 §1.3)。(値)(4) 2 モード多光子玩具((研究ノート: `481_`)、γ=4、n=64〜96)で近完全遮蔽($T/K$ 0.003、$K/\Phi$ 0.9〜0.96)を作ると $1/h_{\rm ex}$ は 0.0016(部分遮蔽)→ 0.904:遮蔽は $\pi\psi_0$ の柔らかい成分を消し、$\mu$ は単峰のまま、反跳の直交位相は反圧搾(真空比 118)。3D の 422 核は遮蔽域に届かず INCONCLUSIVE(METHOD)。
- **共通点**:**F137**(変位型の試行に遮蔽の情報を入れる)・**F2**(ψ0 に錨を下ろしたコヒーレント試行、$\mathcal N\asymp1$)・**F3/F4**(B8 = 低エネルギー端は 2 点関数から出ない —— 向きが逆〔今回は下界〕でも同じ壁)。試行側 C1「1 体生成子 × 同じ ψ0」の線形(Weyl)・2 次($P_f$)の版がともに閉じた。
- **限定**:玩具は 1D・2 モード・離散の反跳・回転群なし(1 点関数 $\langle\Phi_+-\Phi_-\rangle_0\ne0$ が $\int E\,d\mu$ を遮蔽とともに減らす —— (E1) に有利な向きの変形でも $h\to1$)。¬ の枝の列(連続体、$\lambda^{-3/14}$ の相対精度、LL の尺度)は模していない。(N-prop) 自体の真偽は未判定。
- **再開条件**:(i) ¬(RATE) の列で勾配モードの直交位相の圧搾((SQZ-N$_R$)、または $B_\perp$・$\partial A(0)$ の真空比 $R^2/\lambda$ の圧搾)を与える入力(2 点の不等式でない;F137 (i) と同じ);(ii) $\mu_{\pi_z\psi_0}$ の低エネルギー端の下界(質量 $\frac{2m}3T$ のほぼ全部が $E_0+\frac43T(1+o(1))$ 以下)を 269-B の型の入力から出す道具(F137 (ii) と同じ);(iii) 2 体生成子の試行の利得(対の核 $\langle a^*a^*\rangle_0$ の $k_z$ 重み)が ¬ の枝で巨視的になる入力(新)。R9:(i)〜(iii) は (E1) の言い換えではない((SQZ-N) ⟹ (E1) は片向き)。

## F143(E05、定理 282-C〔E05-P151〕の冪 3/5 を、(a) 多殻・全ての窓の同時使用、(b) P121 の 2 次モーメントの定数の精密化、(c) $G_h$ の $h$ 積分の精密化、(d) 紫外殻への選択的適用(助言の提案 7)、(e) 実空間の IMS の箱 + 局所の双極子変換(助言の提案 2)、および (f) 多重 Lieb–Yamazaki(Frank–Seiringer §5 の型の交換子の反復)で $\beta\gt2/3$ に上げる方式。2026-10-19、hard_E05_exponent_72 = 難所の型、稿 `290_` §2、成算 S128)
- **閉じたもの**:**方式**((RATE) の冪の真偽ではない。定理 282-C の冪が 3/5 で最良とも言わない)。
- **理由**:282 の固定点は 3 つの尺度 —— (1) $n_g\le a\lVert N_w\psi_0\rVert x$(コヒーレンスの減衰 $1/\lvert h\rvert$ の $h$ 積分)、(2) $\lVert N_w\psi_0\rVert\le C_NF$、(3) $x\ge\kappa'\sqrt\alpha/(1+2\sqrt{n_g})$ —— で決まり、$x^2=2F'$ から $F^{5/3}\sim\lambda$。(a)(d) は (3) の c 数と (1) の $\lVert f\rVert_\infty^2/\lVert f\rVert^2$ を定数倍しか変えず、窓を広げると (2) が悪化;(b) は $\lVert N_w\psi_0\rVert\lesssim2\sqrt{\nu F}+2(\alpha\lambda)^{1/4}(\nu F)^{1/4}$ まで精密化しても $g(1-g)^{1/3}F^{5/3}\gtrsim\lambda$ で冪は同じ;(c) の $\int dh/\lvert h\rvert$ と $\lVert d\Gamma(B_h)\psi\rVert\le\lVert B_h\rVert\lVert N_w\psi\rVert$ はコヒーレントな占有で等号の桁;(e) は箱の幅 $L\gtrsim\sqrt{\lambda/F}/\Lambda\gg1/\Lambda$ で紫外の殻の $A(x)-A(x_n)$ が $A$ と同じ大きさになり、282 の固定点を決める殻に届かない;(f) は $X=d\Gamma(M_h)$ が $\mathrm{ad}_{P_f}$ の固有ベクトルなので $n$ 重交換子が $\lvert h\rvert^n X$ に戻り、2 重交換子は反交換子の恒等式(補題 290-E)になって $G_h$ の減衰を上げない。
- **冪を決める段**:$G_h$ の減衰の冪 $p$(282-A は $p=1$)。一般に $\beta(p)=\frac{2+p}{4+p}$(命題 290-D、条件付き);$p=3$ で LL 1999 の 12/7 と α の冪 2/7 まで一致。
- **R9**:閉じたのは「同じ 3 尺度の中で定数を動かす」方式で、双極子ではなく固定点の代数で止まる。
- **射程(T60)**:禁じるのは (a)〜(f) の形で冪を上げる発注。止めないもの:(DEC-$p$)($p\gt2$)の供給 —— エネルギー(全場のエネルギーの分散 $\mathrm{Var}(H_f)$ と反交換子の評価、または平行移動したモードの占有と $H_f$ の局所の下界〔LL Thm 1.2 (2.28) のファイバー版〕)からコヒーレンスの減衰を出す方式。
- **再開条件**:(DEC-$p$) が $p\gt2$ で供給されたとき(そのとき命題 290-D で $\beta\gt2/3$、254-A1 で密度 1)。

## F144(E05、`273_` §5 の「軟らかい雲の窓」を ¬(RATE) の明示の試行状態として完成させる方式 —— 主運動量に条件付けた軟らかい雲 × 紫外の圧搾で $\langle H\rangle_\Psi\le CS$ を作る。2026-10-19、w_E05_291 = 書き下しの型、稿 `291_軟らかい雲の窓の完全な試行状態_2026-10-19.md`、成算 S129)
- **閉じたもの**:**方式**(273 §5 の勘定に沿って ¬(RATE) の状態を構成する筋)。(RATE) は定理 282-C(E05-P151)で既に閉で、本項はその構成側の検査の記録。
- **理由**:(1) 干渉性の条件付きの雲(族 F1、補題 291-A の恒等式で全項を帳簿に載せた正規化された状態)は、雲自身の反跳のため主運動量の運動エネルギーを $(1+\frac{8\alpha}{3\pi}\ln\frac{\kappa_1}{\kappa_0})^{-1}$ 倍にしか下げられない(補題 291-C);胞のモデルで $\langle H\rangle\ge\frac{\alpha\lambda}{2\pi}\Lambda(1-\frac{2\alpha}{\pi^2}(1+D_{\rm cl}))$(稿 §5.3)—— 破れの項は $\lVert\pi\Psi\rVert$。(2) 反跳を手で消した理想化(273 の数の圧搾の胞)でも、遮蔽 $\eta\to1$ は雲の位置の広がり $\sigma\ge\sqrt3\pi\eta/(e\kappa_1)$ を強い、硬い場を位置 $\Theta$ で見せるので局在した(双極子型の)圧搾が消える(運動量方向の脱コヒーレンス;雲の形を問わない形は補題 291-B)—— 圧搾は幅 $\delta\lesssim e\kappa$ の運動量対角の胞 $(\Lambda/\delta)^3$ 個に替わり、費用 $\sim\sqrt{\alpha\lambda}(e\kappa)^{-3/2}$ —— 破れの項は窓の光子数。勘定の最小は $E_*=\alpha^{2/7}\lambda^{5/7}\Lambda$(LL 1999 の上界の尺度)【値】、C0((研究ノート: `486f_`))の局所冪 0.80〜0.83。273 §5 は「UV の圧搾の費用 $\sim S$」を 1 モードで数えていた。
- **限定**:閉じたのは単一尺度の条件付けの雲(干渉性、および反跳を消した理想化)の族。尺度ごとに条件付ける階層の雲の最小の冪(5/7 と 3/5 の間)は計算していない —— (RATE) には効かない(282-C)。
- **再開条件**:無し(標的 (RATE) は E05-P151 で閉)。282-C の冪の上界側の対照として階層の族の冪を問うときに参照する。R9:本項は (RATE) の言い換えでない(構成側の検査)。

## F145(E05、名指し (DEC-$p$)〔窓のコヒーレンス $G_h$ の減衰の冪、E05-P152 の 290-D〕を $p\gt1$ で供給する方式 —— (β) 平行移動したモード $f_y$ の占有と局所の $H_f$ の下界(LL Thm 1.2 (2.28) のファイバー版)、そのファイバー版の「$\hat h\cdot\pi$ のスペクトルのずらし」(補題 293-A)、$M_h$ の $A(0)$ モードへの直交化、(α) 全場の $\mathrm{Var}(H_f)$ + 反交換子の恒等式。2026-10-19、hard_E05_DEC_72 = 難所の型、稿 `293_` §1、成算 S131)
- **閉じたもの**:**方式**((DEC-$p$) の真偽ではない)。
- **理由**:(β) 位置の読み —— ファイバーでは位置 $y$ の LL 不確定性が $\pi(y)=P_f+eA(y)$ と組み、$\lvert y\rvert\gg1/\Lambda$ で $\langle\pi(y)^2\rangle_0\sim\alpha\Lambda^2$(場の脱相関、電子は原点)なので $y\ne0$ の Π モードに反圧搾は要らない;偶模型の $(\Lambda L)^3$ の勘定は位置でなく $P_f$ のセクター($\langle P_f^2\rangle\le2mE_{\rm e}$)で出ていて、PF では $P_f$ のセクターが広い。ファイバー版(ずらし、293-A)—— $[Y,X]=-\lvert h\rvert X+eL$ の $L$(線形な場、$\langle L\rangle_0=0$ だが作用素としては 0 でない)が $\Phi(Y)$ の切断の中で $1/\lvert h\rvert$ の項として残り、目標との比 $R_2=23.8$(全ての $N$・α で定数)、$R_3\to\infty$ —— $p=1$ に戻る。直交化($L=0$)は窓の Π モードと A モードの重なり $0.968$ で不可。(α) は 290-E(恒等式から $\lvert h\rvert^2G_h$ が消える)。
- **共通点(設計のやり直しのための 1 行)**:**$[eA(0),X]$ の線形な場の項が $1/\lvert h\rvert$ で残る** —— 偶模型と PF の差がここに局在する(偶模型は $L\equiv0$)。
- **R9**:閉じたのは経路で、双極子では 282-A と同じ所(ずらしの項 $-\lvert h\rvert X$ が無い)で止まる。
- **射程(T60)**:禁じるのは (β)・ずらし・直交化・反交換子で $p\gt1$ を出す発注。止めないもの:$L$ の項を厳密に打ち消す 2 次の補正 $X'=X+e\Xi$ の構成、全空間の位置表示での LL (2.28) と電子の位置の射影の組み合わせ、戯画で真の $p$ を読む数値。
- **再開条件**:$\langle\Phi(Y)\psi_0,L\Phi(Y)\psi_0\rangle$ が $\lvert h\rvert$ で減衰することを与える入力、または $L$ を消す構成が 1 つ供給されたとき。

## F146(2026-10-19、w_E05_292 = 書き下しの型、稿 `292_EDGE-mean_消費者の照合と282の道具_2026-10-19.md` §4.2・§4.3・§3.4)— 定理 282-A・282-B(E05-P151)の機構(反跳を見る不確定性・電子に局在したモードの占有の上界)と 282-C 型の窓の電場の不確定性で、縁の殻の場のエネルギー (EDGE-ν) を押さえる方式

- **閉じたのは: 方式**(標的 (EDGE-ν)・(EDGE-mean) の真偽は閉じない;値は成り立つ側 —— 双極子 $p_{\rm edge}\approx3c$、2 次の摂動論 $\lesssim1.4c$、(研究ノート: `487_`))。
- **理由(勘定)**:補題 292-C で縁のエネルギーの非自明な部分は縁の殻の局在モード $G_j=c_kP_\perp e_j\mathbf 1_{\mathrm{Sh}_c}$ の占有に落ち、282-B はこの型の量に当たるが、$\lvert\mathrm{Re}G_h\rvert\lesssim1/\lvert h\rvert$ を直径 $2\Lambda$ の弦の全体で積分するので薄い殻で縮まず、$n_{G_j}/\lVert G_j\rVert^2\lesssim6x\nu_f^2\sqrt{2v_f+2p}/\omega$ —— 1 体の評価 $p\nu_f$ より $\approx6x\nu_f^{3/2}$ 倍弱い(値の絵で $\lambda^{13/14}$)。282-C/227-A 型の不確定性は縁の殻の場の揺らぎの**下界**しか与えず、(RATE) の下では真空以下で空。CS $\lvert\langle B_c\rangle\rvert\le\frac{\lvert e\rvert}m\lVert\pi\psi_0\rVert\lVert A_{\mathrm{Sh}}\psi_0\rVert$ + 1 体の占有は自己無撞着に $p\lesssim\alpha\omega\lambda/\nu_f$(不足 $\alpha\lambda/F$、`254_` §3.6 と同じ)。
- **再開条件**:$G_h$ の減衰の冪 $p\gt1$ の評価((DEC-$p$)、稿 290 の命題 290-D)で 282-B の弦の積分が殻の厚さで縮むこと;または殻の結合を強めた模型のエネルギーの下界 $E(s)\ge E_0-o(M_f)s$($s\downarrow0$、観察 292-E)。
- **射程(T60)**:禁じるのは「282-B の $1/\lvert h\rvert$ の上界、または窓の電場との LL 型の不確定性だけで縁の殻の占有を上から押さえる」形の発注だけ。(DEC-$p$) 型の減衰、2 光子の背中合わせの配置の重み、$E(s)$ の下界は止めない。

## F147(E05、(DEC-$p$)、$p\gt2$ を (a) 線形な場の項 $L$ を打ち消す着衣 $X'=X+e\Xi$ + $\hat h\cdot\pi$ のスペクトルのずらし、(b) 全空間の位置表示で LL (2.28) と電子の位置の射影 $\mathbf 1_{\lvert x\rvert\le L}$、(c) 3 重交換子の直接評価、で出す方式。2026-10-19、hard_E05_Lcancel_72 = 難所の型、稿 `295_` §1・§3、成算 S132)
- **閉じたもの**:**方式**((DEC-$p$) の真偽ではない。$p=2$ は同じ稿の定理 295-E で条件付きに立った)。
- **理由**:(a) 線形の $\Xi$ で $[\hat h\cdot\pi,X']=-\lvert h\rvert X'+e^2c'$ は厳密に作れ、$L$ の障害は消える(補題 295-A)が、ずらしの尾に要る成分のモーメント $\langle(\hat h\cdot\pi)^{2p}\rangle\lesssim(x\Lambda)^{2p}$ が真空で既に破れる($\langle\pi_1^4\rangle_\Omega/\langle\pi_1^2\rangle_\Omega^2=3+0.94/\alpha$:成分では反跳の項 $k_1g_1\ne0$、全体の $\pi^2$ では $k\cdot g=0$ で消える —— LL (2.10) と同じ Coulomb ゲージの構造)。(b) 全空間でも各点の不確定性は $\pi(y)=p+eA(y)$ と組み、$\lvert y-x\rvert\gg1/\Lambda$ で遮蔽されない(293-B の全空間版);E05-F23 でファイバーに戻すには $P$ 積分が要る。(c) 3 重交換子の直接評価は成分の混合 2 次モーメント $\sum_j\lVert(\hat h\cdot\pi)\pi_j\psi_0\rVert^2$ を要し、$\lVert\pi_i\pi_j\psi\rVert^2+\lVert\pi_j\pi_i\psi\rVert^2\ge\frac12e^2\lVert B_{ij}(0)\psi\rVert^2$ の磁場の床(真空並みなら目標の $10\alpha^{0.2}N^{0.8}$ 倍)を持つ(補題 295-F)。
- **共通点(1 行)**:**$\pi$ の成分(非可換:$[\pi_i,\pi_j]=ieB_{ij}(0)$)の 2 次以上のモーメントは、遮蔽($\pi\psi_0$ 小)では小さくならない —— 全体の $\pi^2$ だけが $2m(E_0-H_f)$ で制御される。** $p=2$ は全体の $\pi^2$ だけで済む(295-C)ので届き、$p\ge3$ は成分が要る。
- **R9**:双極子では (DEC) 偽(ずらしの項なし)のまま;閉じたのは PF の側の評価の方式。
- **射程(T60)**:禁じるのは (a)(b)(c) の形で $p\ge3$ を出す発注。止めないもの:(VAR-f)・(N3) の供給で 295-E を無条件に;(SQZ-B)(電子の位置の磁場の揺らぎの圧搾)の類 C;消費者側の閾の境界($\beta=2/3$、$\kappa_0=0$)の対数の改良。
- **再開条件**:(SQZ-B) が供給されたとき、または成分の混合 2 次モーメントを使わない $p\ge3$ の恒等式が見つかったとき。

## F148(E05、行 E1-H の A-246-3 (4) を経由しない (E1) の消費者:2 体生成子(対の生成・消滅、背中合わせ $k+k'\approx0$ と同方向)を含む接ベクトル $\eta=K\psi_0$ のブーストで、(RATE)〔E05-P151〕・補題 282-B・E05-P121 から全ての λ の $h\to\infty$ を出す方式。2026-10-19、w_E05_296 = 書き下しの型、稿 `296_E1の別の消費者_2体生成子のブースト_2026-10-19.md` §1〜§5、成算 S133)
- **閉じたもの**:**方式**(この入力の組で 2 体生成子の試行から全ての λ の (E1) を出すこと)。(E1)・(E-H′)・2 体生成子の試行一般の真偽は閉じていない。F115 の限定欄「$\psi_0$ の Bogoliubov 回転の 2 次の安定性」・F115 追記(233-D)の「$B$ が対の生成子の場合は未試行」・F142 の再開条件 (iii) への答え。
- **理由**(値に依らない部分):(1) 恒等式 296-0 $x(K)=\langle C_z\rangle^2/(\lVert C\psi_0\rVert^2+\mathrm{Re}\langle\pi\cdot D\rangle+mW_f)$($C=[K,\pi]$、$D=[K,C]$)と命題 296-B($K=V_z$ で $\langle C_z\rangle=\langle S\rangle$、$\lVert C_z\psi_0\rVert\ge\lVert S\psi_0\rVert$、$S=\frac13\sum_a[V_a,\pi_a]$)から、$h\to\infty$ に要るのはスカラーの 2 次形式 $S$ の相対分散 → 0 —— 雲のブースト(P120)では $S=-H_\theta/\Lambda$ で σ² そのもの、対では異常 2 次形式で、分解(準自由の部分 + 連結 4 点)は補題 215-C と同型。(2) 背中合わせの対は補題 296-A(空間パリティ × 回転 × 交換の対称性 × 横波性:$J=1,m=0$・パリティ奇の対の核は $q=k+k'=0$ で消える)で厳密に寄与 0;寄与する $q\ne0$ の対は E05-F7 の反跳の抑制を受け、非スカラーの部分 $\gtrsim2\mathrm{Var}(S)$ を足す(雲のブーストと違い $q\otimes\vec\beta$ は単位行列になれない)。(3) 逃げ道は交差項 $\mathrm{Re}\langle\pi\cdot D\rangle$(相対 $O(\delta)$;効くには $D\psi_0$ の $1/\delta$ 倍の拡がり —— F116 の T6 と同型)、正規と異常の 2 次形式の $\psi_0$ の上での一致(連結 4 点)、光子数パリティ奇の 3 点(F119)だけ;線形 + 対で反跳の直交位相を消すと対自身の分散が $1/\alpha$ 倍で損。(4) (RATE)・282-B・P121 は 2 点の上界と $O(1)$ の 2 次モーメントで、$1+o(1)$ の精度も連結 4 点も与えない(282-B は電子に局在した集団モードの巨視的な占有を外すが、$k$ 局在の細胞と $K_4$ は残し、σ² と σ_S² に同じだけ効く)。(5) 条件は各 λ の 4 点量で $F$ の形の性質でないので、命題 290-A の族を排除しない。
- **双極子の検算**:消費者は双極子で正しい —— 線形の $K$、$f\propto\omega^{-1}g_z$ で $C_z$ が c 数、$h=1+\frac{4\alpha}{3\pi}\lambda$ を厳密に再現;双極子では対の利得は 0(対の利得は $P_f$ からだけ)。
- **共通点**:**P120(雲のブースト)の σ²**・**F116 の T6**・**F137 の反跳の直交位相**の 3 つに分かれて戻る(難しさの保存)。B20 の $\varphi=b\psi_0$ の型(E05-F21 の飽和形が目標と同値)と同じ枠で、2 次の生成子に限っても飽和の条件は σ² 型の 4 点量。
- **限定**:恒等式 296-0・命題 296-B は定義域の仮定 (H-dom) の下の形式の計算;費用の各項の冪は因子化の目安で、交差項と正規・異常の一致の不可能性は示していない(逃げ道として残す)。値((研究ノート: `491_`)・`491b_`、1 次元 6 モード、摂動域)は背中合わせの対の寄与 0 と双極子の一致を再現するだけで、(E1) の域を模していない。次数 3 以上の生成子は扱っていない。
- **再開条件**:(i) 正規と異常の 2 次形式の $\psi_0$ の上での一致(連結 4 点の情報)を与える道具;(ii) 交差項で $\mathrm{Var}(S)$ を打ち消し反圧搾の費用が消える機構;(iii) 次数 3 以上の生成子で相対分散の型が 4 点から下がることの勘定。R9:(i)〜(iii) は (E1) の言い換えではない(静的な 4 点量・機構・勘定)。

## F149(E05、消費者の境界 β=2/3(κ₀=0)を (a) A-246-3 (4) の曲率の閾 $K$ の対数の改良、(b) (VAR-f)〔$\mathrm{Var}(H_f)\le C_VT^2$〕の 254-A1 への直接投入、(c) 290-A の反例の族の (VAR-f) による排除、で越える方式。2026-10-19、hard_E05_kappa0_72 = 難所の型、稿 `299_` §1、成算 S135)
- **閉じたもの**:**方式**(密度 1 の (E1) の真偽ではない)。
- **理由**:(a) β=2/3 ちょうどで 254-B の $\nu_f\ge c'\lambda^{4/7}$ と (U-L4c) から 254-A1 の括弧 $Q\le512C_U^7\alpha/c_L^9$ は λ に依らない定数($c_L\propto\alpha^{1/3}$ で $\propto\alpha^{-2}$、小さくもない)—— 密度 1 には $K\to\infty$ が要り、そのとき $v_f\lesssim\sqrt{KQ}$ は発散:損は対数でなく定数倍で、$K$ の取り方では直らない。(b) (VAR-f) は $v_f\le C_Vg^2/(1-g)^2$ しか与えず、冪則($g=\beta$)では消えない;$v_f\to0$ に要る $g\to0$ の集合は $\int g\,d\ln\lambda=\ln F\ge\frac23\ln\lambda$ から密度 1 になれない。(c) $F$ は状態の 1 階の応答($T,M_f$)と 2 階の応答の上界しか決めず、(VAR-f) は分散の上界で $F$ の形に制約を与えない(ファイバーにギャップが無く $\chi_f\le2\mathrm{Var}/\mathrm{gap}$ は空);境界の族は $Q$ が有界だが正の対数密度で $O(1)$(`494_`)。
- **共通点(1 行)**:**境界では $Q$ が 0 に行かず定数に留まる —— 越えるのに要るのは冪でなく発散因子 $F/\lambda^{2/3}\to\infty$ で、それは供給側の量(命題 299-A)。**
- **R9**:閉じたのは消費者側の 3 つの工夫で、双極子($F\sim\sqrt{\alpha\lambda}$)とは無関係。
- **射程(T60)**:禁じるのは消費者側だけで境界を越える発注((a)(b)(c) とその変種:$K$ の λ 依存の工夫、(VAR-f) の形の投入)。止めないもの:供給側の発散因子($p=2+\epsilon$、または (DEC-2) の定数 $C_2(x)\to0$)、(VAR-f) を「$\mathrm{Var}(H_f)\le\epsilon(\lambda)M_f^2$」の率つきの形で供給すること(それは $v_f\to0$ そのもの)。
- **再開条件**:(LL-low$_{2/3}^+$) が供給されたとき(命題 299-A でそのまま密度 1)。

## F150(2026-10-19、w_E05_301 = 書き下しの型、稿 `301_EDGE-nu_縁の殻のtrMの上界_2026-10-19.md` §2・§3)— (EDGE-ν) の縁の密度 $o(\nu_f)$ を、(b) 定理 282-C 型の(変分原理でない)下界で殻の結合を強めた模型の $E(s)$ を下から押さえて $\langle B_c\rangle$ の符号を出す、(c) 補題 296-A の選択則で $\mathrm{tr}_\perp M$ の背中合わせの底の重みを消す、の 2 方式

- **閉じたのは: 方式**((EDGE-ν) の真偽は閉じない;値は成り立つ側)。
- **理由**:(b) 282-C 型の下界は冪の精度($c\alpha^{2/5}\lambda^{3/5}\Lambda$ 対 上包絡 $C\lambda^{5/7}\Lambda$)で、要る 1 階の応答の精度 $E(s)-E_0\ge-o(M_f)s$ に届かない(下界の冪が予想に達しても定数の比が 1 でなければ届かない);(S4) 型の不確定性は交換子(虚部)を押さえ、$\langle B_c\rangle$ は反交換子(実部)なので CS にしかならず、不足 $\alpha\lambda/F$ に戻る;停留の恒等式の書き直しは負の 1 体の大きさの項 $-\frac83eJ_c\langle T\rangle$ を出し、反跳の項との打ち消しが要る。(c) 296-A は試行の生成子の $J=1$・パリティ奇の対の核に効き、$\mathrm{tr}_\perp M$ の底の重みの主の源(観察 301-B (iii):$eA$ が $\psi_0$ 自身の背中合わせの対の片方を消す成分)は $\psi_0$ の $J=0$ の対の核で選択則の外;さらに $R(k)$ は $k$ の向きを固定して回転対称でない。296-A と同じ $q$ の重みが効くのは $\epsilon\cdot P_f\psi_0$ の成分 (ii) だけ。
- **再開条件**:縁の背中合わせの対の密度($\langle a^*(k)a^*(-k)a(-k)a(k)\rangle_0$、$\lvert k\rvert\approx\Lambda$)の上界、または殻だけが違う 2 つの模型のエネルギーの差の下界を与える道具。
- **射程(T60)**:禁じるのは「冪の精度のエネルギーの下界、または交換子型の不確定性だけで $\langle B_c\rangle$ を下から押さえる」形と「生成子の選択則を $\psi_0$ の対の核に当てる」形の発注だけ。2 光子 pull-through の背中合わせの配置の評価、格子の戯画での重みの分解は止めない。

## F151(2026-10-19、w_E05_304 = 書き下しの型、稿 `304_EDGE-nu_縁の背中合わせの対の密度_2026-10-19.md` §1・§2)— (EDGE-ν) の残り 1 点(観察 301-B (iii):縁の背中合わせの対の密度)を、(a) 2 回の pull-through $a(k)a(k')\psi_0$ の表示と E05-P150(通路の底)・補題 291-B(条件付けの脱コヒーレンス)で、(b) $P_f$ の分布の Chebyshev((NC-P) に依る)で押さえる方式

- **閉じたのは: 方式**((EDGE-ν) の真偽は閉じない;値は成り立つ側)。
- **理由**:(a) 背中合わせ $q\approx0$ で 2 光子のレゾルベント $R_2$ は反跳を失い $\le1/(2\Lambda)$(1 体と同じ級);$A^2$ の頂点の項は無害だが、残りの項は縁の 1 光子密度 $a(k)\psi_0$ を係数 $\sim\alpha\lambda F$ で戻す —— 縁の 1 光子密度と縁の対の密度が循環する。P150 は通路の底の上界で逆向き;291-B は主運動量に依る雲の期待値の費用で、全運動量 ≈0 の対には費用を課さない。(b) Chebyshev は (NC-P)(名指し)に依り、しかも $R(k)$ が $P_f$ と可換でないので底の重みに渡らない;在庫だけでは $\langle P_f^2\rangle\lesssim\alpha\Lambda^2\nu_f$ で空。
- **共通点(族 EDGE の 3 体:F146・F150・本行)**:縁の局在モード/背中合わせの対の密度を 1 体・2 体の pull-through と不確定性で上から押さえようとした —— 背中合わせの配置では反跳が無いので、どの段も 1 体の水準 $\lVert R\rVert\le1/\lvert k\rvert$ に戻る。
- **再開条件**:反跳を持たない 2 光子相関(背中合わせの対の振幅)の独立な上界、または殻だけが違う 2 つの模型のエネルギー差の下界。
- **射程(T60)**:禁じるのは「2 回の pull-through の各項を作用素ノルムで押さえる」「291-B を背中合わせの対に当てる」「$P_f$ の分布だけで $\mathrm{tr}_\perp M$ の底を押さえる」形の発注だけ。消費者の側で縁を使わない窓の流れの再検討、格子の戯画の拡大(モード数・光子数)は止めない。

## F152(E05、2/3 の位置の発散因子 (LL-low$_{2/3}^+$)〔$F/\lambda^{2/3}\to\infty$、命題 299-A の入力〕を供給側で、(α) (DEC-2) の定数 $C_2(x)$ の $x\to0$ での減少($C_V$・$C_3$・295-D の $\sqrt2/\sqrt g$ に隠れた $x$・$g$ の負の冪)、(β) $2\lt p\lt3$ の中間の減衰(成分の混合 2 次モーメントを避ける恒等式:スペクトル射影の分数モーメントの補間・部分的な磁場の圧搾・$\rho'$ の項の交換子による書き換え)、(γ) 282-C の窓の LL 不確定性と (DEC-2) の同時使用(固定点を 2 本の不等式の交わりに)で出す方式。2026-10-19、hard_E05_RATE23_72 = 難所の型、稿 `300_LL-low23plus_2_3の位置の発散因子_2026-10-19.md` §1〜§3、成算 S136)
- **閉じたもの**:**方式**((LL-low$_{2/3}^+$) の真偽ではない。値の側は LL の上界 $\lambda^{5/7}$ が肯定の向き)。
- **理由**:(α) 2 重交換子の厳密な恒等式(補題 300-A)で $C_2=2(\sqrt{C_V}+\langle N_w\rangle_0/\lVert N_w\psi_0\rVert)(1+o(1))$ まで下がるが、$C_V=\mathrm{Var}(H_f)/T^2\to0$ は $g\in(0,1)$ の内側で $v_f\to0$(E1-H の第 2 連言の窓なし版)そのもの(R9)で、298-A/233-A 型の $\mathrm{Var}(H_f)\le TM_f$ は定数しか与えない;$\rho'=\sum_j\pi_j\lvert\psi_0\rangle\langle\psi_0\rvert\pi_j$ の項は $SO(3)$ 不変なので 282-A が当たるが、右辺は成分の混合 2 次モーメント $\lVert(\hat h\cdot\pi)\pi_j\psi_0\rVert$(295-F の磁場の床:真空並みなら自明な評価より $\sqrt\alpha/x$ 倍悪く、最大限の圧搾でだけ $\alpha^{1/8}N^{-1/8}$ の利得 = (SQZ-B) 相当)。隠れた負の冪は無い($\sqrt2/\sqrt g$ は $g\to0$ で悪化、$C_3$ は 298-B で定数)。(β) 3 重交換子の (γ) 項は $-\lvert h\rvert\,\mathrm{tr}(M_h\gamma_{\rho'})$ で同じ量(観察 300-B:(DEC-$(2+q)$) ⟸ (DEC-$q$) for $\rho'$);分数モーメントの補間は端点 $\langle Y^4\rangle$ が真空で破れ(295-B)、部分的な圧搾 $n_b\sim\sqrt{\alpha N}N^\epsilon$ には $B(0)$ が $H$ に現れないので機構が無く、交換子の書き換えは $v_f$ 型・反交換子型($\langle X(h\cdot\pi)\rangle$、$1/x$ 倍悪化)・$L$ の項(293-C)に分かれる。(γ) 固定点 $n_g\sim\sqrt{\alpha N}$・$x^2\sim\sqrt{\alpha/N}$ は「局在モードに $n_g$ 個(反圧搾)+ 運動量相殺の胞(背中合わせの対)に $\sim N$ 個」の配置で LL 不確定性と (DEC-2) for $\rho'$ を同時に飽和し(観察 300-C)、交わりは空でない(双極子では空で、それが 282-C の機構);この配置を基底状態で排除する在庫は無い(P130 は積の族、F129 は排除の道具を禁じる側)。
- **共通点(1 行)**:**$\pi$ で持ち上げた状態 $\rho'$ は遮蔽されていない($\lVert Y\pi_j\psi_0\rVert$ の床 $e\Lambda^2/\sqrt{1+n_b}$)ので、$\psi_0$ の 2 点量の不等式は $\rho'$ の窓のコヒーレンスに届かない —— 2/3 の位置の発散因子は $\rho'$ の (DEC-$q$)($q\gt0$)か $v_f\to0$ のどちらかで、どちらも E1-H の壁と同じ所。**
- **R9**:閉じたのは供給側の 3 方式で、双極子では補題 300-A の左辺が無く各段は空(難しさの保存)。
- **射程(T60)**:禁じるのは (α)(β)(γ) の形で発散因子を出す発注(定数の精密化、分数モーメントの Hölder 補間、2 本の不等式の交わり)。止めないもの:$\rho'$ の構造を $\psi_0$ と独立に読む道具($(H-E_0)\pi_j\psi_0=(-ie\Pi_j+\frac{ie}{2m}\lbrace\pi_i,B_{ij}\rbrace)\psi_0$ の高エネルギー励起の評価)、戯画で $\mathrm{tr}(M_h\gamma_{\rho'})/\mathrm{tr}\gamma_{\rho'}$ の $h$ 依存を読む数値、運動量相殺の胞の凝縮を基底状態で排除する入力((E1) の壁の族)、(SQZ-B) の類 C。
- **再開条件**:(DEC-$q$) for $\rho'$($q\gt0$)が供給されたとき(そのとき観察 300-B で $p=2+q$、299-A で密度 1);または $\mathrm{Var}(H_f)=o(TM_f)$ の率が供給されたとき(それは $v_f\to0$ で E1-H の本体)。

## F153(2026-10-19、w_E05_305 = 書き下しの型、稿 `305_EDGE_球面に接する窓の流れ_2026-10-19.md` §3)— 球面に接する窓の流れの消費者(定理 305-A)の移り先 (ANI)〔場のエネルギーの四重極の揺らぎ $Q_2\to0$〕を、282-A 型の不確定性(回転不変性)と P121・298-A の 2 次モーメントで押さえる方式

- **閉じたのは: 方式**((ANI) の真偽は閉じない)。
- **理由**:282-A 型が与えるのは 1 点関数 $\langle D_2\rangle_0=0$ だけで、$\langle D_2^2\rangle$(対角の 4 点)には効かない;P121・298-A は $D_2^2\le\frac49H_f^2$ から $Q_2\le\frac49E_0/M_f(1+o(1))=O(1)$;和則 $\mathrm{Var}(D_2)^2\le\frac{\chi_D}2S_D$ は $\chi_D\le KM_f$ が点ごとにあれば (RATE) で閉じるが、等方の $H_f$ に効いた拡大の族(A-246-3 (1))は $\ell=2$ の摂動に無く、$t$ について平均した曲率の上界は $t=0$ の点に渡らない;異方的な拡大は切断球を楕円体に変えて縁の項を戻す。
- **共通点**:第 2 連言(σ²→0)と同じ「巨視的な集団モードの排除」の $\ell=2$ 版 —— $\ell=0$ は拡大の族で供給できたが、$\ell=2$ には族が無い。
- **再開条件**:四重極の感受率 $\chi_D=-\partial_t^2\inf\sigma(H+tD_2)\vert_0$ の点ごとの上界(λ の悪い集合の議論に乗る族)、または殻・角度だけが違う模型のエネルギー差の下界の道具。
- **射程(T60)**:禁じるのは「1 点関数の消滅と 2 次モーメントの上界だけで $Q_2\to0$ を出す」形の発注だけ。異方的な拡大の族の解析、格子の戯画での $Q_2$ の値は止めない。

## F154(E05、$\rho'=\sum_j\pi_j\lvert\psi_0\rangle\langle\psi_0\rvert\pi_j$ の窓のコヒーレンスの減衰 (DEC-$q$)、$q\gt0$〔観察 300-B で (DEC-$(2+q)$)、299-A で (LL-low$_{2/3}^+$) の最後の供給の筋〕を、高エネルギー励起 $(H-E_0)\pi_j\psi_0=(-ie\Pi_j+\frac{ie}{2m}\lbrace\pi_i,B_{ij}\rbrace)\psi_0$ のエネルギーの経路(pull-through の反跳の分母・磁場の着衣)で出す方式。2026-10-19、hard_E05_rhoprime_72 = 難所の型、稿 `306_rhoprime_窓のコヒーレンス_2026-10-19.md` §1〜§2、成算 S140)
- **閉じたもの**:**方式**($\rho'$ の (DEC-$q$) の真偽ではない;戯画 `501_` は INCONCLUSIVE(METHOD))。
- **理由**:(a) pull-through(補題 306-A (i))で窓の 1 光子の付加・除去は反跳 $\lvert k\rvert^2/2m=\frac\lambda2(\lvert k\rvert/\Lambda)^2\Lambda\gg\Lambda$ の高エネルギー励起 —— 電場の項の $\rho'$ への寄与は $\lVert(H-E_0)^{-1}e\Pi_j\psi_0\rVert\lesssim8e\Lambda/\lambda$ で $\lVert\pi_j\psi_0\rVert=x\Lambda/\sqrt3$ に対し $e/(x\lambda)\sim\alpha^{3/4}N^{-5/4}\to0$(親の推論 1「電場の項が主」は励起の大きさでは正しいが $\rho'$ への寄与では逆);(b) $\rho'$ の主体は磁場の項で、同じ成分では $b_j(k)\cdot f_j(k)=0$ 点ごと ⟹ $[B_j(0),X^{(j)}]=0$ 厳密(補題 306-A (ii))—— 磁場の着衣は $M_h$ コヒーレンスを保ち、エネルギーの経路は $\mathrm{tr}(M_h\gamma_{\rho'})\approx c\cdot\mathrm{tr}(M_h\gamma_{\rho'})$ の自己無撞着式に退化して $q$ を決めない;交差成分は $L$ 型の線形な場の項(293-C、$1/\lvert h\rvert$ の減衰なし);(c) 反跳の分母 $\lvert k\rvert^2/2m$ は $k$ に滑らか(窓で比 ≤4)で $k$ と $k+h$ を脱相関させない。
- **共通点(1 行)**:**$\rho'$ の $q$ を決める情報は $\pi\psi_0$ の遮蔽されない成分の構造(運動量相殺の胞)にあり、$H$ の励起のエネルギー・磁場の着衣・反跳の分母のどれにも無い。**
- **R9**:双極子では反跳が無く励起は $\omega\sim\Lambda$、$\rho'$ は局在モード 1 個の着衣で $q=0$ が正しい —— PF で $q\gt0$ を出す段は双極子で空だが、PF でもその段が $q$ を決めない(難しさの保存)。
- **射程(T60)**:禁じるのは $\rho'$ のエネルギー分布・pull-through・磁場の着衣から $q\gt0$ を出す発注。止めないもの:戯画の C1(格子 $\lbrace-2..2\rbrace^3$、光子数 ≤4、λ 3 段)で $q$ を読む数値;運動量相殺の胞の凝縮を基底状態で排除する入力((E1) の壁の族);(SQZ-B) の類 C(NUM-6538 は圧搾の向き)。
- **再開条件**:$\pi\psi_0$ の遮蔽されない成分の窓の構造(胞の幅・背中合わせの対の重み)を与える入力が供給されたとき;または戯画の C1 で $Q_{\rho'}(h)$ の傾きが λ の 3 段で $\le-0.5$ と読めたとき。

## F155(2026-10-19、w_E05_307 = 書き下しの型、稿 `307_ANI_異方的な拡大の族_2026-10-19.md` §1〜§3、成算 S141)— (ANI) の供給のために、四重極の感受率 $\chi_D$ の点ごとの上界 $\chi_D\le KM_f$ を異方的な拡大の族(楕円体の分散 $\lvert k\rvert_\epsilon$・異方的な質量・$H+tD_2$)の基底エネルギーの 2 階の応答と、A-246-3 型の凹性・λ の悪い集合の議論で出す方式

- **閉じたのは: 方式**((ANI) と $\chi_D\le KM_f$ の真偽は閉じない)。
- **理由**:(1) 応答は書ける(補題 307-B:$\chi_D\le\frac49(-E_\epsilon''(0))-\langle d\Gamma(\lvert k\rvert Y_2^2)\rangle_0$、Peano 点で)が、$E(\epsilon)$ を既知の $F$ に戻す点変換は分散が球面上で一定でないので切断の球面を動かす(補題 307-A;線形の $M_\epsilon$ では異方的な質量 + 楕円体の切断、境界の法線変位 $\frac32\epsilon\Lambda Y_2$)—— 縁の項が戻る。(2) 異方的な質量は切断を動かさないが応答は運動エネルギーの四重極 $K_2$ で、$D_2$ と結ぶビリアルに切断の変形が入る;球面に接する非線形の流れで縁を消すと $\chi_{K_2}$(同じ型)に移り、縁の残りは (EDGE-ν) 型。(3) $\ell=2$ の曲率は 1 次斉次の凹関数 $\hat G(u,v,t)=\inf\sigma(uT_1+vH_f+tD_2)$ のヘッシアンの独立な固有値:在庫の全ての入力($F$ の全情報・凹性・斉次性・$E_t\le E_0$・$-\frac13H_f\le D_2\le\frac23H_f$ の包絡・回転不変性)を満たしつつ $\chi_D$ を λ の窓の上で一様に任意に大きくする関数がある(補題 307-C (3))—— 点ごとにも λ の平均でも出ない。$\ell=0$ で効いたのは $H+tH_f=(1+t)[T/(1+t)+H_f]$ の括り出しで、曲率の方向が質量の方向と一致したから。
- **双極子(値、(研究ノート: `502_`))**:$\chi_D/M_f$ は 0.034→0.0048(α=1、λ=10²→10⁶)で段「$\chi_D\le KM_f$」は**成り立つ**;偽になるのは (RATE)($\nu_f^2/\alpha\lambda\to0.079$)だけ —— 双極子は標的の反例でない。
- **共通点**:F153 と同じ —— 「巨視的な集団モードの排除」の $\ell=2$ 版に、族のパラメータの方向(質量・λ)と一致する変形が無い。
- **再開条件**:(α) 殻・形だけが違う 2 模型の基底エネルギー差の 2 次の下界(在庫なし、305 §4);(β) 運動エネルギーの四重極の感受率 $\chi_{K_2}$ と縁の残りを同時に押さえる道具;(γ) 基底状態の 2 体の角度の相関を直接押さえる道具。E05 族を滑らかな切断に替えるのは族の定義の変更で承認事項。
- **射程(T60)**:禁じるのは「点変換で等方の族に戻す」「$\hat G$ の凹性・斉次性・作用素の挟みだけで $t=0$ の曲率を押さえる」形の発注だけ。在庫の外の入力 (α)〜(γ) の探索、格子の戯画の $Q_2$ の値は止めない。

## F156(2026-10-19、w_E05_308 = 書き下しの型、稿 `308_SQZ-B_磁場の揺らぎの圧搾の判定_2026-10-19.md` §2〜§3、成算 S142)— (DEC-3) を補題 295-F の磁場の床と (SQZ-B)「$\langle B(0)^2\rangle_0\lesssim x^4\Lambda^4/e^2$」で出す経路($q=1$・$p=3$・$\beta=5/7$)

- **閉じたのは: 経路**(類 C の値による閉鎖。(SQZ-B) の偽の証明ではない —— 値であって上下界ではない【T88】)。
- **理由**:有限モードの玩具 4 種(z2・z4・c6・s1、$\alpha=1/80$、光子数切断を収束まで、(研究ノート: `503_`))で $r_B=\langle B(0)^2\rangle_0/\langle B(0)^2\rangle_\Omega$ は下がる(z2 の局所冪 −0.43→−0.50、λ=16〜4096)が、要る量 $x^4/\alpha$ との比は全ての玩具で λ とともに増える(z2 で 12.7→161、局所冪 +0.39〜+0.49)—— 起動前に固定した判定文(S140)の NO-GO。λ に依らない形で $r_B\simeq C_0x^2/\alpha$($C_0\approx0.08$、α=1/20・1/80・1/320 で確認)、$r_B/r_A\to1^+$、$e^2\langle B(0)^2\rangle_0\approx\Lambda^2\langle\pi^2\rangle$(1.005〜1.11)—— $B$ は $A$ と同じだけ圧搾され、(SQZ-B) には $1/x^2$ 倍足りない。双極子は $r_B=1$(厳密)。
- **共通点(1 行)**:**$B(0)$ の圧搾の機構は $P_f^2$ を介した $A(0)$ の集団モードとの対の相関だけ($P_f=x_sx_d+p_sp_d$ 型)で、その深さは $A$ の圧搾($\propto x^2$)を越えない。**
- **R9**:双極子では $B(0)$ は手つかず($r_B=1$)で (SQZ-B) は偽 —— 族でだけ圧搾が起こるが、要る冪($x^4$)に届かない(難しさは 295-F の床の高さ $e^2\langle B^2\rangle_0\sim\Lambda^2\langle\pi^2\rangle$ に残る)。
- **射程(T60)**:禁じるのは「295-F の床($\sum_j\lVert(\hat h\cdot\pi)\pi_j\psi_0\rVert^2\gtrsim e^2\langle B(0)^2\rangle_0$)を経て $p=3$ を出す」形の発注。止めないもの:床を経ない $p\ge3$ の恒等式(F 行 295 系の再開条件の後半);多モードの真の族で $B(0)$ が $A(0)$ より深く圧搾されるかの値(MPS 系の核で $\langle B(0)^2\rangle$ と $\langle\pi^2\rangle$ を同時に測る —— 玩具の外)。
- **再開条件**:真の族の値(モード数が $\Lambda^3$ で増える核、例 MPS)で $e^2\langle B(0)^2\rangle_0/(\Lambda^2\langle\pi^2\rangle)\to0$ が λ の 3 段で読めたとき;または $B(0)$ を $A(0)$ と独立に圧搾する $H$ の項が見つかったとき。

## F157(E05、近完全遮蔽・観察 300-C の配置の排除を「1 次の場 $A(0)$ と 2 次の $P_f$ の同時の遮蔽の 4 次モーメントの不適合」(他のエージェント 提案 8)—— 状態に依らない 4 次の形式の不等式 $\langle(P_f+eA(0))^4\rangle\ge c\langle P_f^4\rangle-C$、または準自由の部分だけでは遮蔽できないこと —— で出す方式。2026-10-20、w_E05_318 = 書き下しの型、稿 `318_2_3の壁の角度の成算_2026-10-20.md` §2 (D)、成算 S148)
- **閉じたもの**:**方式**(運動学の形。(NC-P)・(LL-low$_{2/3}^+$)・(K4) の真偽ではない)。
- **理由**:(1) 遮蔽 $\langle P_f\cdot A(0)\rangle_0$ は光子数パリティ奇の 3 点量(224-A)で、平均 0 の準自由の状態では恒等的に 0 —— 「Gauss では同時遮蔽できない」は自明で、非 Gauss の $\psi_0$ について何も言わない。(2) 横波の 2 モードの玩具((研究ノート: `510_w_E05_318_toy_screen.py`):$\pi_z=kn_i+ec\,q_j$、$\lvert m\rangle_i\otimes D(q_*)S(r)\lvert0\rangle_j$)で $\langle\pi_z^2\rangle$ は $m$ に依らず、尖度 3、$\langle P_z^4\rangle=m^4$ —— 4 次の一様な形式の不等式は偽(F129 の 2 次の形と同じ機構の 4 次版)。費用は場のエネルギー($n_j\approx m^2/(2(ec)^2)$)に移り、エネルギーを入れれば総費用の比較(S148 (B)、定数倍しか動かない)に戻る。(3) 300-C の主部(運動量相殺の対 + 局在モードの圧搾)は 2 モード圧搾型で準自由と両立し、278-C の「$K_4$ が巨視的に負」は σ²→0 の側の条件で 2/3 の壁の配置には要らない。
- **限定**:玩具は成分($z$)の形で、ベクトルの横成分の費用(モード $j$ の $P_x$)は扱っていない —— ベクトルの 2 次の形は F129 で既に閉。値【T88】。
- **R9**:双極子は Gauss で遮蔽 0・$K_4=0$ —— 段は双極子で排除すべき配置を持たず、PF の配置も排除しない。
- **射程(T60)**:禁じるのは「エネルギーを使わない 4 次(以上)のモーメントの形式の不等式」「準自由の部分の不適合」で遮蔽の配置を排除する発注。止めないもの:エネルギーを入れた比較で 300-C の配置の実現可能性そのものを問う道具、真の族の値(S144 のジョブ)。
- **再開条件**:エネルギーに依る高次モーメントの下界(例:$\langle(H-E_0)\cdot\rangle$ を重みにした 4 次の評価)で、双極子では偽・300-C の配置では破れる形が 1 つ示されたとき。

## F158(2026-10-20、w_E05_317 = 書き下しの型、稿 `317_SPEC族の成算_RATEの後_2026-10-20.md` §3・§4.1)— (1) (SPEC-G) を (RATE)・系 298-D・補題 254-B の下界から出す読み;(2) SPEC 族の型の移送(補題 199-B の試行を運ぶ)で E05-P164 の対数密度 1 の集合の穴(乗法的に有界な区間)を跨ぐ方式

- **閉じたのは: 方式(読み)**。標的((SPEC-G′)・(E1))と命題の真偽は閉じない。
- **理由 (1)(1 段の解析)**:$r_u(\delta)$ は δ に増加し、要る閾 δ(系 277-C の $\epsilon^{1/2}E_u$、系 317-B の $\theta\epsilon E_u$)は $E_0$・$M_f$ に比例する。(RATE)(E05-P151)・298-D(E05-P158)・254-B は $E_0$・$M_f$ の**下界**なので、閾を上げる向きにしか入らない。283 §6 の「合流」で要る率は $h\gg\sqrt{\alpha\lambda}$(有効質量の率)で、(RATE) の $F=E_0/\Lambda\gg\sqrt{\alpha\lambda}$(エネルギーの率)とは別の量(双極子は $F\sim\sqrt{\alpha\lambda}$ で $h\sim\alpha\lambda$);両者を結ぶ v-b の不等式は無い(E05-P147 の $h_W$ は平均場で ≲3/2)。
- **理由 (2)(厳密な必要条件 + 値)**:命題 317-C:補題 317-A の右辺が ε を固定して 0 に行くには、各 κ で $\nu_u([0,\kappa M_f(u')))\to0$((SPEC-G$_1$))が必要。双極子(G の重みの大部分が極 $\omega_c\approx\frac43M_f$)では偽で、どの試行でも右辺 $\ge\min(\frac{1-f}2,\frac{\epsilon(1-f)}{64(1+\epsilon)})$ —— (E1) を満たす模型で方式が働かない。280・283 の模型の値でも系の尺度の $r$ は λ ≤ 10⁵ で減らない。〔audit_S2_317 の監査人の補題 A-322-1:317-A の鎖(穴の中の点を経由する細かい段)でも、比 $u_N/u_0$ を固定して右辺 → 0 には鎖のどこかの点で (SPEC-G$_1$) 型が要る —— 段を細かくしても避けられない〕
- **生き残るもの**:自然密度の $S$(β>2/3)の上の SPEC 族(道 1、系 317-B);$S'$ の上の比の比較(道 2:系 276-C (a)・(b))。
- **再開条件**:(2) は「E05 族で G の重みが $M_f$ の尺度に集団モードを持たない((SPEC-G$_1$))」を示す値か評価;(1) は h の率と $E_0$ の率を結ぶ不等式。

## F159(2026-10-20、hard_E05_fullSPEC_72 = 難所の型、稿 `324_全列2_SPECと有効質量の単調性_2026-10-20.md` §2.2・§3)— 319-A 型の正値性(Hiroshima 2007 の汎関数積分表示の経路ごとの順序・同時凸性)から、有効質量 $h$ の形状因子(切断 Λ)についての単調性(系 276-C (a))・倍尺度の比の比較 (b)・(SPEC-G′) の率を出す方式

- **閉じたのは: 方式**。標的((E1) 全列、$h$ の単調性、(COV))と命題の真偽は閉じない。
- **理由(厳密な恒等式 + 既知の型の照合)**:補題 324-A(有限 $t$):$\partial_s\mathrm{Var}_{\mathcal N^s_t}(b_{t,z})=-\frac{e^2}2\mathrm{Cov}_{\mathcal N^s_t}(\Delta q,b_{t,z}^2)$ —— $h$ の形状因子についての応答は Gibbs 測度の**3 次**の結合キュムラント。正値性(正測度の Laplace 変換の log の同時凸性)が符号を与えるのは 1 次(319-A:$\partial_wE_0\ge0$)と 2 次(分散)まで。$P$ の位相 $e^{iP\cdot b_t}$ は Girsanov で正に書け、壊れるのは被積分関数の符号でなく求める量の階数。要る (COV) は GHS 型で、FKG(増分に単調でない)・GKS/GHS(強磁性型でない)・Hargé/Brascamp–Lieb($\Delta q$ は反跳 $e^{-ik\cdot b}$ のため凸でない:1 行の反例)のどれも当たらない。(c) の $E_0$ の単調性は $p$ に依らない定数 $c_{\rm sh}\asymp\alpha\Lambda^2/m$ を残し、比の形は分母 $\mathbb E[e^{-\Delta q}]\approx e^{-t\Delta E_0}$ で $t$ に指数的。(b) の (SPEC-G′) は速度自己相関の減衰率で、正値性は率を与えない。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `515_hard_E05_fullSPEC_cov.py`):反跳つき UV 殻の対 (4,16) で (COV) は z = −1.2〜+1.7(0 と区別がつかない)—— 符号は構造で決まっていない(軟らかい殻・双極子では正)。
- **生き残るもの**:条件付き命題 324-B((COV) ∧ (LIM) ⟹ 全ての λ で (E1)、E05-P170 経由);(COV) の予想(値で生存);設計の候補「$\lvert k\rvert\lesssim m$ の層だけの単調性 + UV 殻の寄与の加法的な上界(312 §3 の (STAB) の非摂動版)」。
- **再開条件**:(1) 3 次キュムラントの符号を与える新しい相関不等式(経路の二重確率積分の重みに対する GHS 型)の文献または構成;(2) E05 族の値で $\partial_\Lambda h\lt0$ の区間が見つかれば単調性の経路そのものを閉じる(標的の閉鎖);(3) (LIM) の供給(PF の Gibbs 測度の CLT と $m_{\rm eff}$ の同定、Betz–Spohn 2005 の PF 版)。

## F160(2026-10-20、w_E05_331 = 書き下しの型、稿 `331_鎖の格子への移送_iii-bとLAT4_2026-10-20.md` §1.4)— 格子切断族 13 で、282 の (S2)〔$\langle a(\varphi)\rangle_0=0$〕の代わりを対称性(点群 $O_h$・パリティ・時間反転)で作る方式
- **閉じたのは: 方式**。標的(282-C・(RATE) の族 13 版)は閉じない —— 稿 §3 の恒等式(補題 331-A・331-L)で通る。命題の真偽も閉じない。
- **理由(厳密)**:(1) 族 13 の 1 光子空間 $\lbrace\varphi:s(k)\cdot\varphi=0\rbrace$($s=\frac2a\sin\frac{ak}2$)に $O_h$ の不変ベクトル $u=w(\lvert k\rvert)P^s_\perp(k)(k_1^3,k_2^3,k_3^3)\ne0$ がある(符号つき置換で同変)—— 点群から 1 点関数の消滅は出ない(連続で $SO(3)$ を $O_h$ に落としても同じ)。(2) 必要なのは実の奇の場 $u$ の $\mathrm{Re}\langle a(u)\rangle_0=0$ で、パリティは $u$ を固定し、時間反転は $\langle a(u)\rangle_0\in\mathbb R$ を与えるだけ。(3) 粗い評価 $\lvert\langle a(u)\rangle\rvert\le\lVert u\rVert\langle N_w\rangle^{1/2}$ は 282 §3.2 (i) で c 数 $ec_3\Lambda^3$ に比 $\sim\sqrt{F/\alpha}\to\infty$ で負ける。
- **生き残るもの**:モードを向きで選んで項を作用素として消す方式(補題 331-A:$e_n\perp f\perp s$;補題 331-L:$P^s_\perp P^c_\perp e_j$)。代償は $h$ 積分の対数。
- **再開条件**:族 13 の基底状態の 1 点関数 $\langle a(u)\rangle_0$ の上界で $\langle N_w\rangle^{1/2}$ より良いもの(例えば pull-through で $\langle\pi\rangle_0=0$ を使う形)が出たとき —— 対数の損を外す用途に限る。

## F161(E05、2/3 の位置の発散因子 (LL-low$_{2/3}^+$)〔$F/\lambda^{2/3}\to\infty$、命題 299-A の入力〕を今日の道具(319-A/S・316-1・314-A・291・300-A・317-A)で出す方式 —— (1) 結合密度 $\rho=\lvert\hat\varphi\rvert^2$ についての $E_0$ の凹性(補題 323-A)による殻ごとの超加法性で 2/3 の下界を殻ごとに足す、(2) 汎関数積分の 2 点の符号(Φ 側の圧搾、E05-P39)で観察 300-C の配置を排除する、(3) 291-B の運動量の脱コヒーレンスで (DEC-$p$)、$p\gt1$ を出す、(4)〜(6) 316-1 の圧搾の試行の比較・314-A の正値性・300-A と 317-A の符号の自由度。2026-10-20、hard_E05_full23_72 = 難所の型、稿 `323_全列1_LLlow23plus_新しい道具で_2026-10-20.md` §1〜§3、成算 S150)
- **閉じたもの**:**方式**((LL-low$_{2/3}^+$) の真偽ではない。補題 323-A 自身は立った —— 利得が無いだけ)。
- **理由**:(1) 323-A は厳密(Hölder の 1 行 + 319-S)で、F124 の「予算 $\langle\pi^2\rangle\le2mE_0$ は 1 本」を回避する新しい不等式 $E_\alpha(\sum\rho_s)\ge\sum\theta_sE_{\alpha/\theta_s}(\rho_s)$ を与えるが、薄い殻 $N_s$ 枚の各殻の模型(結合 $N_s\alpha$)に 282-C/298-D の固定点を当てると、LL 不確定性は中立(c 数と $\langle\Pi_s^2\rangle_\Omega$ が共に $1/N_s$ 倍)、(DEC-2) の $h$ 積分は $\lVert f_s\rVert_\infty^2=N_s/\mathrm{vol}$ で $N_s$ 倍(球殻の差集合は球で、薄くても狭まらない)、ゆえに殻の下界 $F_s\ge c(\alpha/N_s)^{1/3}\lambda^{2/3}$;重み $1/N_s$ と結合の $N_s$ 倍で足すと $c\alpha^{1/3}\lambda^{2/3}$ —— **$N_s$ に依らず厳密に中立**(観察 323-B、$b=1/3$)。2 進の殻・α の弦も定数倍以下。(2) 場の挿入つきの FI から出る 2 点の符号は $\langle\Phi(u)^2\rangle_0\le\lVert u\rVert^2$(全ての実モードで A 直交位相は圧搾、$\gamma+\alpha\le0$)で、E05-P39 に供給済み;300-C は胞(2 モード圧搾)も局在モード(Π 反圧搾 = Φ 圧搾)も Φ 圧搾なので排除されない;Π 側(Euclid 速度)は反圧搾の向きで 300-C と整合。(3) 遮蔽のために胞が局在モード系の運動量を精度 $x\Lambda$ で追跡することに 291-B を当てると、窓の 1 体行列のコヒーレンス $\le2x\Lambda/\lvert k-k'\rvert$ —— 282-A の (DEC-1) と同じ冪(282-A ≡ 運動量の脱コヒーレンス)。(4) 上界は下界に使えず、差は積の族の外(P130・F117);(5) 314-A の符号は (2) と同じ情報;(6) 基底状態の期待値に試行の符号の自由度は無い(F152 (α))。
- **共通点(1 行)**:**新しい道具 6 本のうち 2 点量を超える情報を持つのは FI の表示だけで、そこから出る平均の量の不等式(単調・凹・Φ 側の符号)は全て 300-C の配置が満たす —— 2/3 の固定点は結合密度の分割について尺度不変で、300-C を縛るのは Π 側・4 点・追跡の 2 次。**
- **R9**:閉じたのは方式。双極子では (1) の凹性の段は空でないが標的の段(殻の 2/3 の下界)は双極子で偽;(2)(3) の段は双極子で空(難しさの保存)。
- **射程(T60)**:禁じるのは「凹性・超加法性で殻の 2/3 の下界を足して発散因子を出す」「FI の Φ 側の 2 点の符号で 300-C を排除する」「291-B の脱コヒーレンスで $p\gt1$ を出す」形の発注。止めないもの:E05-F25 の有界挿入を Π の生成関数に広げて Π 側の 2 点・4 点の符号を出す道具;薄い殻で幾何的な重なりを見る $\lvert G_h\rvert$ の上界((DEC-2) の精密化、$b\lt1/3$ なら凹性で発散因子);運動量相殺の胞の凝縮を基底状態で排除する入力(E1-H の壁の族)。
- **再開条件**:Π 側の 2 点・4 点の符号が FI から出たとき;または (DEC-2) の $h$ 積分が薄い殻で狭まる精密化(殻の下界 $\propto N_s^{-b}$、$b\lt1/3$)が供給されたとき(そのとき観察 323-B の超加法性で発散因子 $N_s^{1/3-b}$ 級)。

## F162(2026-10-20、hard_E05_softUV_72 = 難所の型、稿 `334_全列3_軟らかい層と紫外の殻_2026-10-20.md` §2)— 324 §3 の設計候補「$\lvert k\rvert\lesssim m$ の軟らかい層だけの単調性(Hargé 型)+ 紫外の殻の寄与の加法的な上界((STAB) の非摂動版)」を、その字面のまま (E1) 全列の十分条件にする方式;および加法的な上界を Cauchy–Schwarz・試行の移送(276-F)・殻についての摂動で出す方式

- **閉じたのは: 方式(設計の字面)**。標的((E1) 全列、$h$ の単調性、(LLC)、(COV))と命題の真偽は閉じない。
- **理由 (1)(字面の照合)**:$\Lambda\ge m$ で Λ→Λ′ の差の重みは $\mathbf 1_{\Lambda\lt|k|\le\Lambda'}$ で常に紫外。「軟らかい層の単調性」は $\partial_\Lambda h$ の層への分解ではなく、324 の C0 の「(COV) が正になる殻の対」の所在の記述。尺度則 $h=h(\Lambda/m)$ で殻の追加を $m$ の減少に移しても、反跳 $k/\sqrt m$ と $\omega$ が全モードで同時に変わり層に分かれない。(S) の成分は空で、標的は (U) だけ。
- **理由 (2)(Hargé 型の適用条件)**:Hargé(Gauss 底 + 凸な摂動)・Brascamp–Lieb は $q_w$ の経路についての点ごとの凸性を要る。2 階変分の反跳項 $-\cos(k\cdot(b_s-b_r))(k\cdot(\phi_s-\phi_r))^2\dot b^\perp_s\cdot\dot b^\perp_r$ は局所速度の大きい経路に沿って下に非有界で、$w$ の台(軟らかいか)は係数 $|k|^2$ の大きさを変えるだけ —— 「$w$ についての条件」で凸になることは無い。経路の切り詰めは Gauss 底を壊す。期待値の凸性は $\mathcal N$ の速度自己相関((SPEC-G) 型)に帰着し、定理の形を持たない。当たったとしても与えるのは $h$ の下界(F99・S13 の側)で 3 次の応答ではない。
- **理由 (3)(加法的な上界の止まる段)**:(LLC)(3 次キュムラントの率の下界 $\ge-2C/(e^2m\ln\lambda)$)に対し、Cauchy–Schwarz は $t^{3/2}$ で $\sqrt t$ 足りず;$O(t)$ は連結 3 点関数 $\langle\Delta q_\tau;\dot b_s;\dot b_r\rangle$ の時間減衰を要る(在庫に無い)。試行の移送(276-F、$u=1/m$)は損失 $\epsilon M_f/\delta+(1+E_u/\delta)^{1/2}\lVert\psi_{u'}-\psi_u\rVert$ で (SPEC-G)・(FID);殻についての摂動は底 $\mathcal N^\Lambda$ の 3 点関数そのもので、底の経路は切断の尺度で Brown 的でない($H(\mathcal N^\Lambda_t|W_t)/t\le E_0$ は $\gg\Lambda$ になり得る、P117 の機構)。3 経路とも同じ 1 段。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `517_hard_E05_softUV_cov.py`)(324 の C0 を時間格子で解像、$\omega\,dt\le1/4$):反跳つき 27 セル全てで (COV) 正(z = +0.7〜+49);324 の「UV 殻 (4,16) で 0 の縁」は未解像($\omega\,dt=2.7$)の人工物だった。応答比 $R=\mathrm{Cov}_{\mathcal N}/\mathrm{Cov}_W\approx f_{\rm base}^{\,p}$、双極子 $p=2.00\pm0.03$、反跳 $p\approx1.5$〜1.6 —— UV 殻の $h$ への寄与は摂動値の $h_{\rm base}^{1/2}$ 倍(単調性は非摂動の底で強まる向き)。方式の閉鎖の理由は (1)〜(3) の字面で、値は使わない。
- **生き残るもの**:補題 334-A((LLC) ∧ E05-P170 ⟹ 全列の (E1)、self-audited);名指し (LLC)((COV)∧(LIM) を 1 本に置き換える向き);(COV) の予想(解像した玩具で生存)。
- **再開条件**:(1) 底の測度 $\mathcal N^\Lambda$ の連結 3 点関数の時間減衰(行 E1-H の壁 (SPEC-G) と同じ対象)の評価;(2) E05 族の値で $\partial_\Lambda h\lt0$ の区間(λ=256→512 の $\Delta f\gt0$)が見つかれば単調性($C=0$)を閉じ (LLC) の $C\gt0$ の見積もりへ;(3) 経路の二重確率積分の重みに対する GHS 型の相関不等式(F159 (1) と同じ)。

## F163(2026-10-20、w_E05_342、成算 S159)— 「族 13 の pull-through の縦の項 $\frac12u\cdot k\,R(k)\psi_0$ を主項と分けて、$\lVert R(k)\psi_0\rVert\le1/\hat\omega$ で別に押さえ、(EDGE-ν) の消費者に $o(M_f)$ で入れる」(`340_` §4.2 の勘定)
- **閉じたのは**:方式(縦横に分けた別評価)。命題((LONG13) の言明)の真偽ではない。標的(族 13 の後半の消費者)は補題 342-B で縦横を分けずに閉じる。
- **なぜ落ちたか**:比が $\lambda^{10/7}t^4\times10^{-4}$ で発散するのは評価の粗さ —— 分けた後の交差項 $\mathrm{Re}\,\bar\ell\langle\psi_0,Rw\rangle$ は符号不定で、縦の部分だけを押さえると主項との相殺を失う。消費者の両側(292-C (i) と 301-A)は同じ完全平方 $\sum_\lambda\langle v_\lambda,Rv_\lambda\rangle$ で書ける。
- **残るもの**:補題 342-A・342-B、系 342-C・342-D(`342_` §2)。
- **再開条件**:再開しない(閉じたのは方式で、標的は別経路で閉じた)。

## F164(E05、観察 300-C の配置(局在した反圧搾のモード $n_g\sim\sqrt{\alpha N}$ + 運動量相殺の胞の凝縮)を、汎関数積分の **Π 側(Euclid 速度)・4 点・混合の符号**(E05-F25 の有界挿入を Weyl 作用素 $e^{i\lambda\Pi(u)}$ に広げた補題 338-A・系 338-B)で基底状態から排除し、(LL-low$_{2/3}^+$) の発散因子を出す方式。2026-10-20、hard_E05_PiFI_72 = 難所の型、稿 `338_全列4_汎関数積分のΠ側と4点_2026-10-20.md` §2〜§3、成算 S156)
- **閉じたもの**:**方式**((LL-low$_{2/3}^+$)・300-C の真偽ではない。補題 338-A・系 338-B 自身は立った —— 向きが逆なだけ)。
- **理由(厳密な表示 + Gauss 状態の構造)**:(1) Π の挿入の FI 表示は存在し(Weyl 作用素は Cameron–Martin のずらし)、被積分関数は Gibbs 核 × $e^{ie\lambda\ell}$($\ell$ = 奇の核の実の経路汎関数)。Φ 側(虚のずらし、$\cosh$)と鏡像で、**正値性が与える向きは Π 側では下界**:$\langle\Pi(u)^2\rangle_0=\lVert u\rVert^2+e^2\mathbb E_w[\ell_u^2]\ge\lVert u\rVert^2$、$\langle:\Pi^{2n}:\rangle_0\ge0$、$\langle:\Phi^{2a}\Pi^{2b}:\rangle_0(-1)^a\ge0$、$\langle\lbrace\Phi,\Pi\rbrace\rangle_0=0$。(2) この符号の全体は、平均 0・軸圧搾・$\Delta C_{\Phi\Phi}\le0\le\Delta C_{\Pi\Pi}$ の**全ての Gauss 状態**が満たす(Isserlis:正規順序モーメントは $\Delta C$ の対の和で因子ごとに符号が一致)。300-C の主部はその類(2 モード圧搾の胞の位相は P39 で固定され、その側では Π 側の符号も満たす;C0 `519_` で確認)。(3) 300-C を縛るには $e^2\mathbb E_w[\ell_f^2]$(紫外の局在モードの反圧搾の深さ)の**上界**が要り、Gibbs 測度の下での線形汎関数の分散の上界 = Brascamp–Lieb/Hargé 型で、重みの経路についての凸性が反跳 $e^{-ik\cdot b}$ で破れる(324 §2.2・F159・334-C)。局在モードは紫外の殻で、核の時間尺度 $1/\Lambda$ に $\lvert k\rvert\lvert b_r-b_s\rvert\sim\sqrt\lambda\gg1$ —— 非凸性が最大。(4) Hilbert 空間の迂回(f-sum + 感受率、Weyl 共役 $H+\lambda\Pi(f)\cong H_f+\frac1{2m}(\pi-\lambda\Pi(kf/\omega))^2$)は $\Pi(kf/\omega)^2$ の上界を要り循環。$\Xi_u$ 自身の生成関数は反跳項が場の 2 次で Weyl 族の外。
- **共通点(1 行)**:**FI の正値性が符号を与える量(1 次の単調・2 次の下界・Wick 符号)は Gauss 状態で等号が実現でき、300-C(Gauss の主部)を排除するには Gibbs 測度の 2 次以上の量に正値性の外の入力(反跳で破れる相関不等式)が要る —— F159 の段と同一。**
- **R9**:閉じたのは方式。段 (b)(分散の上界)は双極子で真(Gauss、Loewner)だが双極子に 300-C の配置は無い —— 障害は反跳の非凸性に移り消滅していない。
- **射程(T60)**:禁じるのは「FI の Π 側・4 点・混合の符号(Weyl 族の有界挿入から出る不等式)で 300-C の配置を排除する」形の発注。止めないもの:反跳つきの重みの下での線形汎関数の分散の上界(Gibbs 測度の相関不等式の族 —— 紫外の殻の $\ell_f$、全体の $b_t$ = (COV) の 2 次の版);運動量相殺の胞の凝縮を基底状態で排除する入力;補題 338-A の表示を他の量($\Pi$ の時間相関、$P\ne0$)に使うこと。
- **再開条件**:反跳つきの Gibbs 測度の下で経路の線形汎関数の分散が Wiener の分散の定数倍を超えないことを示す相関不等式(文献または構成)が 1 つ出たとき(そのとき $n_g=O(\alpha)$ で 300-C の (3) の飽和が壊れ、2/3 の位置の発散因子になる);または E05 族の値で $\langle\Pi_f^2\rangle_0/\lVert f\rVert^2$ の λ 依存(紫外の局在モード)が読めたとき。

## F165(2026-10-20、w_E05_344 = 書き下しの型、稿 `344_族13の連続な経路とL′_2026-10-20.md` §1.3)— 定理 341-T の連続な経路版を、331〜342 の定数の $t$ についての一様性と、連続体との値の比較(補題 344-A)だけから出す方式
- **閉じたのは: 方式**。標的(連続な経路の (iii)-b の (E1))と命題の真偽は閉じない。
- **理由**:A-302-3 (iii) が使う A-246-3 (3) は、固定の模型での $\int_{\lambda_0}^{2\lambda_0}\lvert F''\rvert=F'(\lambda_0)-F'(2\lambda_0)$ の望遠鏡和で曲率の悪い集合の測度を押さえる。経路では各 λ の模型 $t(\lambda)$ の $\partial_\lambda^2F_{t(\lambda)}(\lambda)$ が要り、値の比較は 1 階の微分に $\sqrt\delta$ の損、2 階には何も与えない;定数の一様性は各 $t$ の上下界で、$t$ をまたぐ曲率の比較を与えない;$t$ で平均する論法は、経路が曲率の悪い集合の和集合に沿う可能性を排除できない。
- **生き残るもの**:補題 344-A(値の比較)・補題 344-B(A-302-3 の経路版、悪い集合の疎な構造は連続の $F_0$ で作れる)。
- **再開条件**:族 13 の $F_t(\lambda)$ の曲率の $t$ についての比較(混合微分 $\partial_t\partial_\lambda F$ の評価、または λ の dyadic 区間ごとの曲率の質量の $t$ についての連続性)が得られたとき —— 名指し (CURV-path)。

## F166(2026-10-20、w_E05_346 = 書き下しの型、稿 `346_族13のCURVpath_2026-10-20.md` §3)— (CURV-path) を承認の窓 $t\lambda^{5/14}\to0$ の全ての経路で出す 2 つの方式:(1) 模型の間で $v_f$ を 2 次の試行状態で比べる;(2) A-246-3 (3) の曲率を均した感受率と値の 2 階差分(補題 346-A)に組み替え、値の比較(補題 344-A)で模型をまたぐ
- **閉じたのは: 方式**(承認の窓について)。標的と命題の真偽は閉じない。
- **理由**:(1) $v_f$ は基底状態の性質で変分量でなく、無質量で $H(0)$ にギャップが無いので、基底エネルギーが近くても基底状態はノルムで近いとは限らない。(2) CS の $\eta\mathrm{Var}$ の項から $s\ll\lambda^{-2/7}$、値の比較の誤差は $\delta/s^2$、$\langle T\rangle/E_0$ の在庫の下界は $\lambda^{-3/7}$ —— 要る精度 $\delta\ll\lambda^{-1}$ に対し、補題 344-A の $\delta\asymp et^2\sqrt\lambda$ は窓 5/14 で $o(\lambda^{-3/14})$ しか与えない。
- **生き残るもの**:補題 346-A(模型に依らない)、命題 346-B(狭い窓 $t=o(\lambda^{-3/4})$ での経路版、candidate)。
- **再開条件**:(a) (EQUIP)〔$\langle T\rangle\ge c_0E_0$ かつ $M_f\ge c_0E_0$ が対数密度 1 の λ で〕—— これがあれば $s\asymp1/K$ でよく、窓 5/14 に届く見込み(連続でも未証明、(LL-low$_\beta$, β>2/3) と同じ種類の難しさ);(b) 補題 344-A の値の比較の改良(交差項 $\langle\pi\psi,A_\delta\psi\rangle$ に遮蔽の構造を使って $\sqrt\lambda$ を外す)。

## F167(E05、全列(行 E1-H の内側)の設計のやり直しの候補 C1・C2 —— (C1) 到達点を「自然密度 1 の集合の上で $h\to\infty$」に下げ、(LLC) の区間平均版と和則(負の殻密度の総量)で E05-P170 の対数密度 1 を自然密度 1 に上げる方式;(C2) $b_t$ の分散の上界($h\ge1$)と同じ Hilbert 空間の変分(ファイバーの変分、276-F の試行の移送の Π 側版)で紫外の殻の局在モードの反圧搾 $\langle\Pi(f)^2\rangle_0$ の上界を出す方式。2026-10-20、hard_E05_C1C2_72 = 難所の型、稿 `345_全列5_自然密度と変分の分散_2026-10-20.md` §1〜§2、成算 S161・S162)
- **閉じたもの**:**方式**((E1) 全列・(LLC)・反圧搾の上界の真偽ではない。補題 345-A・345-B 自身は立った —— 消費者の側の到達点が下がらないだけ)。
- **理由 C1(初等・厳密)**:(1) 区間平均版 (LLC-av)(倍尺度の区間での $f$ の正の変動 $\le C/\ln\lambda$)は P170 と組むと**全ての λ**で (E1)(補題 345-A):損失が倍尺度ごとに**加法的** $O(1/\ln\lambda)$ で、穴の比が $\lambda^{o(1)}$ で非有界でも $o(\ln\lambda)$ 回の和は $o(1)$(276-C (b) の乗法的な損失と対照的)。(2) 和則と負の部分の総量が有限 (LLC-Σ) なら平均版すら要らず全列(補題 345-B:有界変動 ⟹ 極限が存在 ⟹ P170 で 0)。(3) 自然密度 1 は中間の到達点にならない(観察 345-C):片側の対数 modulus の下で自然密度 1 ⟺ 全列;分かれるのは対数幅 $\to0$ の針だけで、針を許しつつ外を縛る供給側の入力は在庫に無い(全て modulus か変動の型)。ゆえに到達点を下げても要る供給は同じ = 負の殻密度の上界(334-C の 3 次キュムラントの率の下界)。
- **理由 C2(向きの議論 + 厳密な恒等式)**:$h\ge1$ は運動量の族 $H(P)$(c 数のずらし)の曲率 $1/(mh)$ が**正**で、上界 $1/m$ が試行 $\psi_0$ の向き。Π の族 $H+\lambda\Pi(f)$ の曲率は $-2\chi_\Pi$ で**負**;反圧搾 $\langle\Pi^2\rangle_{0,c}\le\sqrt{\chi_\Pi F}$(f-sum $F$ は Φ 側で有界)の上界には $\chi_\Pi$ の上界 = 底の 2 次の**下界**(安定性の向き)が要り、試行 $\psi_0$・Weyl 共役の試行($\chi_\Pi\ge\frac12\lVert f/\sqrt\omega\rVert^2-\frac1{2m}\langle\Pi(kf/\omega)^2\rangle_0$)・276-F の移送は全て下界。Weyl 共役は $\Pi(kf/\omega)$ の作用素のずれを残し運動量のずらしに還元できない(双極子では c 数で真)。FI(338-A の連続挿入、形式)では $(\Omega,e^{-t(H+\lambda\Pi(f))}\Omega)=\int e^{-\frac12\lVert eK-\lambda L_t\rVert^2}e^{\lambda^2\lVert L_t\rVert^2}db$ で、2 次の下界 ⟺ Gibbs 測度の下での $e\lambda\langle K,L_t\rangle$ の Gauss 型の裾 = 338 の段;Hölder は 1 次止まり。
- **共通点(1 行)**:**全列の候補 C1・C2 は消費者の再設定と変分の向きの問題で、どちらも供給の段(反跳つきの Gibbs 測度の下での 2 次の上界 / 3 次の符号)を動かさない —— 324・334・338 と同じ段。**
- **R9**:閉じたのは方式。C1 の段は双極子で空でない($h_{\rm dip}$ 単調、標的も真);C2 の段は双極子で真(c 数化)、配置は無い。障害は消滅していない。
- **射程(T60)**:禁じるのは「到達点を自然密度 1 に下げて供給を軽くする」「試行状態・試行の移送(下界の変分)で $\chi_\Pi$ または $\langle\Pi(f)^2\rangle_0$ の上界を出す」形の発注。止めないもの:(LLC)/(LLC-av)/(LLC-Σ) のどれか 1 形の供給(同じ段);反跳つきの Gibbs 測度の相関不等式(文献・構成);(LLC) の梯子ジョブ(334 §5)と紫外の局在モードの反圧搾の値。
- **再開条件**:(C1) 針を許しつつ針の外を縛る供給側の入力(例:$f$ の Lebesgue 測度についての弱い評価)が自然に出たとき;(C2) Π の族の底の 2 次の下界(安定性)を与える新しい型(例:反跳つきの重みの下での線形汎関数の指数モーメントの上界)が出たとき。

## F168(2026-10-20、w_E05_347 = 書き下しの型、稿 `347_窓の全ての連続な経路_EQUIPと値の比較_2026-10-20.md` §2・§3.4)— (CURV-path) を窓 5/14 の全ての連続な経路で、(a) 在庫の不等式だけから (EQUIP)〔$M_f\ge c_0E_0$〕を出す方式、(b) 値の比較(補題 344-A)の改良で在庫の $m_f\gtrsim\lambda^{-1/7}$ に届かせる方式
- **閉じたのは: 方式**(標的と命題の真偽ではない)。
- **理由**:(a) 在庫の類(凹・非減少、$c_L\lambda^{2/3}\le F\le C_U\lambda^{5/7}$)に、$\lbrace M/F\lt0.05\rbrace$ の対数密度が正の $F$ がある(区分定数の $M$ の構成、528:対数の割合 0.56)。ゆえに在庫の不等式だけでは (EQUIP) も、要る弱い形 $m_f\gtrsim\lambda^{-3/56}$ も出ない。(b) 偏極のずれは Gram の単調性とゲージで払える(命題 347-P)が、結合の規格化 $(2\hat\omega_t)^{-1/2}$ と $(2\lvert k\rvert)^{-1/2}$ のずれ(横の結合の点ごとの拡大 $1+O(t^2)$)は、$\Delta_s$ の混合の応答 $\partial_\sigma\Delta_s$(3 つの基底状態の $\mathrm{tr}_\perp M$ の差)を要し、凹性・単調性は 1 階しか与えない;改良の候補 $\alpha t^2\lambda/F$ でも窓 5/14 には届かない。
- **生き残るもの**:補題 347-A・347-M・347-G、命題 347-P、系 347-B(在庫の狭い窓 $t=o(\lambda^{-15/28})$)、定理 347-T((LL-low$_{37/53}$) の下での窓 5/14)。
- **再開条件**:(LL-low$_\beta$, β ≥ 37/53)〔E05 の全列の道 1 の入力;F164・F159 の段〕が出たとき;または混合の応答 $\partial_\sigma\Delta_s$ を押さえる道具(結合の拡大についての 2 次の応答の比較)が出たとき。

## F169(E05、全列(行 E1-H の内側)の供給 (α)(反跳つき Gibbs 測度の下での線形汎関数の分散・指数モーメントの上界)・(β)(3 次キュムラントの率の下界、(LLC) 族)を、ポーラロン型の **Gauss 測度の混合表示**(Mukherjee–Varadhan 2020、Betz–Polzer 2022・2023、Polzer 2026 の点過程・再生表示)の PF 版で出す方式。2026-10-20、hard_E05_corrineq_72 = 難所の型、稿 `348_全列6_反跳つきGibbs測度の相関不等式_2026-10-20.md` §2〜§3、成算 S165)
- **閉じたもの**:**方式**((α)・(β)・(LLC)・(E1) の真偽ではない。補題 348-A〔Nelson 型の (α)〕は立った —— 模型が違うだけ)。
- **理由(文献の字面 + 厳密な表示)**:(1) 混合表示が立つ 2 条件は (M1) 対相互作用が $|x|^2$ の完全単調関数($\frac1{|x|^\gamma}=\int\nu(du)e^{-u^2|x|^2/2}$、Polzer 2026 Assumption 1「$|k|^2\mapsto|v|^2$ completely monotone」)、(M2) 指数の符号が正(Nelson 型のスカラー結合の FK は実 Gauss 場の実の指数 $e^{+\frac12\iint w}$)。(2) PF の重み $e^{-\frac{e^2}2\iint db_s\cdot D(b_s-b_r,s-r)db_r}=\mathbb E_{\mathcal A}[e^{ie\int\mathcal A\cdot db}]$ は HS の場が**虚**(FK–Itô の位相、反磁性不等式の側)で (M2) が逆;核 $D\propto\int|\hat\varphi|^2e^{-\omega\tau}\delta^\perp\cos(k\cdot x)dk$ は $|x|^2$ の完全単調関数でなく(Bochner の分解は複素位相)、増分の**双線形形式**に位置依存の係数が掛かるため冪級数の各項が符号を持たない —— (M1) も逆。(3) 逃げ道(双極子核で割って残りを展開・符号を変えた HS・虚の漂移の Girsanov・Φ 側の実の指数・PZW ゲージ)はいずれも正測度の混合にならない(稿 §2.2 3.)。(4) 混合が立っても与えるのは (α)(成分の共分散 ≤ Wiener、2 次)だけで、(β)(3 次の応答)は混合測度の上の 2 つの正の量の共分散を残し符号不定 —— Fröhlich ポーラロンでも $\alpha\mapsto m_{\rm eff}$ の単調性は MV2020・BP2022・BP2023・Polzer2026・DS2020 のどれにも無い。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `529_hard_E05_corrineq_kurtosis.py`):反跳つき玩具で $b_{t,z}$ の尖度超過は全セル正の向き(z ≤ +3.6)、負なし —— 抽象的な正値 Gauss 混合は**排除されない**(CONSISTENT)。閉鎖の理由は (1)〜(4) の字面で、値は使わない。
- **共通点(1 行)**:**文献の唯一の「非凸でも線形汎関数の分散が Wiener 以下」の型(完全単調性による正値 Gauss 混合)は、Nelson 型の実の HS 場と Coulomb 型の核に固有で、PF の虚の HS 場(FK–Itô)と反跳核には移らず、移っても 2 次((α))止まりで (LLC) 族((β))には届かない —— F159・F164・F167 と同じ段(正値性の外の入力)。**
- **R9**:閉じたのは方式。段は双極子で空(成分 1 個の Gauss)、Nelson 型(CM)で (α) は真(348-A)—— 障害は PF の符号と核に局在し消滅していない。
- **射程(T60)**:禁じるのは「MV–BP–Polzer 型の正値 Gauss 混合表示を PF の重みで立てて (α)・(β) を出す」形の発注。止めないもの:抽象的な正値混合の存在の判定(Bernstein:線形汎関数の特性関数が $\theta^2$ の完全単調関数か;6 次の Hankel 条件の値);Nelson 型の梯子の段への 348-A の適用;反跳つきの重みの下での他の型の相関不等式(文献・構成)。
- **再開条件**:(1) PF の重みを正の重みで Gauss(または Wiener-dominated な対称 log-concave)測度に分解する表示が出たとき;(2) ポーラロンで $\alpha\mapsto m_{\rm eff}$ の単調性(3 次の応答の符号)が文献で立ち、その道具が核に依らないと分かったとき((β) の型の候補)。

## F170(E05、全列(行 E1-H の内側)の単調性・摂動の族 —— (i) 結合 α についての $h$ の単調性を尺度則で λ 方向に移して (LLC)$_{C=0}$ を出す方式;(ii) 殻 $[\Lambda,\Lambda']$ を足す摂動の 2 次の符号(負定値)と非摂動の残差の (EDGE-ν)・319-B による上界で (LLC) を出す方式;(iii) Bach–Fröhlich–Sigal(BCFS 2003・2007)の作用素理論的 RG(平滑 Feshbach 写像で殻を 1 つずつ積分)を紫外の側で Λ に一様に回す方式。2026-10-20、w_E05_354 = 書き下しの型、稿 `354_全列10_単調性と摂動の族_2026-10-20.md` §1〜§3、成算 S171)
- **閉じたのは: 方式**。標的((E1) 全列、(LLC)、(COV))と命題の真偽(α についての単調性を含む)は閉じない。
- **理由 (i)(厳密な恒等式 + 尺度則)**:(a) $q_w$ は $w$ に線形なので α 方向の応答は補題 324-A を $\Delta w=w$ で使ったもの(3 次キュムラント、F159 の段)。(b) 拡大のユニタリで $U_sH_{m,\Lambda,e}U_s^*=sH_{m/s,\Lambda/s,e}$、$h=h(\alpha,\lambda)$、$\lambda\partial_\lambda=-m\partial_m$ —— 拡大は $(\alpha,\lambda)$ を両方固定し、α 方向は λ 方向と独立;形状因子の点ごとの順序でも $\mathbf 1_{\le\Lambda'}$ と $\sqrt{1+s}\mathbf 1_{\le\Lambda}$ は比較できない。(c) 観察 354-A:$-\alpha\partial_\alpha f=\int_0^\Lambda\varrho(\mu;\lambda)\frac{d\mu}\mu$(内側の全殻の応答の対数積分)、$-\lambda\partial_\lambda f=\varrho(\Lambda;\lambda)$(端点)—— α の単調性(積分の符号)は (LLC)(端点の下界)を与えない。双極子では $h$ が αλ の関数で両方向が一致し、反跳で比が $1/\ln(\lambda/2)$ に崩れる(1 ループ)。
- **理由 (ii)(既閉の再確認 + 補強)**:方式は F162 (3)「殻についての摂動」の射程の内。補強:殻の結合の 2 次 = $\Delta w$ の 1 次 = 端点の汎関数微分;非摂動の残差($\Delta w$ の 2 次)は細い殻の望遠鏡和で $n\cdot O(\delta^2)\to0$ で障害でない(残るのは和則そのもの);主項の大きさを Cauchy–Schwarz と作用素の分母で押さえると双極子の値 $\sim\sqrt{\alpha\lambda\delta}$【値】で要る $C\delta/\ln\lambda$ に届かない;(EDGE-ν)・命題 319-B は縁の占有と $E_0$ の 1 階の応答(1 次キュムラント)だけで主項(生成の側、占有に依らない)に触れない。
- **理由 (iii)(次元勘定 + 原典 + E05-P93)**:尺度 μ の無次元の結合 $g(\mu)^2\sim\alpha\mu/m$ は赤外で無関係・**紫外で関係**;BFS/BCFS の縮小は赤外の向きでだけ効き、BCFS 2007 は紫外の正則化を $[0,1]$(Λ = m の単位で O(1))に固定し §2.1 で紫外のくりこみを扱わないと明記、§11 の最初の decimation は小さい $g$ で紫外の全域を 1 段で処理。作用素ノルムでの Feshbach の評価は補空間の天井 $\lvert q\rvert+2\Lambda+C_A\varepsilon_{\rm sh}$(E05-P93・F98;自由なレゾルベントでも $q=-k$ で $2\lvert k\rvert$)で反跳の分母を使えず、殻ごとの展開パラメータは双極子の値(1 オクターブあたりの $h$ の相対変化が αλ ≫ 1 で $O(1)$)。F100 の形の不変性の障害は BFS の一般の核の空間で回避できるが、Neumann 級数の収束 = 同じパラメータの小ささに移るだけ。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `534_w_E05_354_alpha_vs_shell.py`):α 方向の (COV) は z = +136・+123、足す UV 殻(端点、底の切断 8 → 16)は z = +0.61・−0.18;`534_w_E05_354_rg_param.py`:作用素の評価の 1 オクターブのパラメータは α=1/137 で λ≈64 から 0.1 超。閉鎖の理由は (i)〜(iii) の字面で、値は使わない。
- **共通点(1 行)**:**単調性・摂動・作用素 RG はどれも「平均の量(α 方向の内側の積分・1 次キュムラント・作用素ノルムの sup)」を扱い、(LLC) が要るのは反跳の分母が効く端点の 3 点関数 —— 平均・sup の型は双極子の値を返す(F109〜F114 の死因と同じ向き)、端点は F159・F162 の段。**
- **R9**:閉じたのは方式。(i) の段は双極子で空(両方向が一致);(ii) の段は双極子で真(Gauss、Loewner);(iii) の段は双極子でも立つ(双極子の $h$ も αλ で線形に増え、紫外で縮小しない)—— 障害は反跳の端点の構造に局在し消滅していない。
- **射程(T60)**:禁じるのは「α(または全殻の一様な倍率)についての単調性・凹性を尺度則で λ 方向に移す」「殻の結合の摂動の 2 次の符号と残差の上界で (LLC) を出す」「BFS/BCFS 型の作用素 RG(Wick 順序の核の polydisc の縮小)を紫外で Λ に一様に回す」形の発注。止めないもの:端点の応答 $\varrho(\Lambda;\lambda)$ の値(350 の梯子ジョブ);反跳の分母を作用素の評価で使える新しい型(天井の配置を基底状態の重みで排除する入力);反跳つき Gibbs 測度の 3 点関数の時間減衰((LLC) の供給の本体)。
- **再開条件**:(1) $\varrho(\mu;\lambda)$ の μ についての単調性(または端点を内側の平均で押さえる比較)が出たとき(そのとき (i) の α の単調性が (LLC) に移る);(2) 作用素の評価で Feshbach の補空間の分母を $\Lambda^2/2m$ の次数で下から押さえる入力(E05-P93 の天井の配置の重みの上界)が出たとき(そのとき (iii) の殻ごとのパラメータは 1 ループの $\frac{8\alpha}{3\pi}\delta$ になり、和は $\alpha\ln\lambda$ で、なお αlnλ ≲ 1 の窓に限られる)。

## F171(E05、全列(行 E1-H の内側)の文献の網羅 —— Λ→∞ の有効質量・質量くりこみの厳密な結果(Hiroshima–Spohn 2005・Lieb–Loss 2002・Hainzl–Seiringer 2002・Bach–Chen–Fröhlich–Sigal 2007・Hiroshima–Ito 2007・Chen 2008・Betz–Spohn 2005・Betz–Hiroshima 2009・Könenberg–Matte 2013/2014・Dybalski–Spohn 2020、追加で Sellke 2024・Hiroshima 2024 総説)から、全列・$h$ の単調性・(LLC) 型の主張か、それを出す道具を取り出す方式。2026-10-20、w_E05_356 = 書き下しの型、稿 `356_全列12_文献の網羅_2026-10-20.md` §1〜§4、成算 S173)
- **閉じたのは: 方式**(照合範囲の文献に型が無い)。標的((E1) 全列)・命題の真偽は閉じない。
- **理由**:(a) 曲率の $m_{\rm eff}$ の Λ 依存についての定理は全て「各固定 Λ で、α が Λ に依存して十分小さい」量化子(HS 2005 (1.26) の直後、Hainzl–Seiringer (3.40) と序文、Chen 2008・Könenberg–Matte 2014 の抄録、BCFS は UV を扱わない);HS 2005 p.5 は大きい λ の技法が無いと明記;Lieb–Loss 2002 p.3 は曲率の質量について「cannot prove」。(b) 単調性の定理は $E(e^2)$ の単調・凹性(Hiroshima 2007 Cor 3.8、2024 総説 Cor 6.3 = 323-A の在庫)だけで、$h$ の λ・α についての単調性は HS 2005・Dybalski–Spohn 2020 が期待として述べるだけ。(c) 各点の下界の形を持つ唯一の道具(Sellke 2024 の Royen GCI)は **F99** で既に当てた(閉じていない枝 1〜4 はそのまま)。
- **再挑戦条件**:Spohn の本(CUP 2004)の量子部(手元は arXiv の古典部のみ、[要入手])か、2025 年以降の文献(稿 357 の担当)に非摂動の $h$ の単調性・殻密度の下界があったとき。F99 の再挑戦条件は F99 のとおり(この項で変えない)。
- **数値**:(研究ノート: `536_w_E05_356_qc.py`)・`536_w_E05_356_qc2.py`(`_result.json`)—— 素の $q$ の準凸性の破れ 0、双極子形の 0.9 倍を差し引くと破れ(値)。

## F172(E05、全列 (9):観察 300-C の配置(局在した反圧搾のモード $n_g\sim\sqrt{\alpha N}$ + 運動量相殺の胞の凝縮)を**エネルギー**で基底状態から排除する方式 —— (a) 反圧搾を緩める 2 次の変分・反圧搾の費用 $\omega n_g$ と反跳の釣り合い、(b) 胞の運動量の打ち消しを崩す変分、(c) IMS 局在・pull-through の光子数の上界(反跳の分母)。2026-10-20、w_E05_353 = 書き下しの型、稿 `353_全列9_300Cの配置のエネルギーによる排除_2026-10-20.md` §1〜§3、成算 S170)
- **閉じたもの**:**方式**((LL-low$_{2/3}^+$)・300-C の真偽ではない。補題 353-B・観察 353-C 自身は立った —— 排除に届かないだけ)。
- **理由**:(a) $E_0=\langle H_f\rangle_0+\langle\pi^2\rangle_0/2m$ は厳密に 2 項で、300 §3.1 の固定点は $\Lambda[N+\lambda x^2/2]$ を (DEC-2)・LL 不確定性の下で最小化した解そのもの;$n_g$ 方向の勾配 $\Lambda[1-\lambda\kappa'^2\alpha/(8n_g^2)]$ は 300-C の域($n_g\ll n_g^*=\kappa'\sqrt{\alpha\lambda/8}$)で負 —— エネルギーは反圧搾を深めたがり、止めているのは運動学;$\langle[S,[H,S]]\rangle_0\ge0$(反圧搾の生成子)は安定性の向きで F167 C2 と同じ。(b) 打ち消しを崩すと運動 $\lambda\delta P^2/2\Lambda$ を払う —— 打ち消しはエネルギーが強制する側。(c) $(H(-k)+\omega-E_0)a(k)\psi_0=\frac em g\cdot Q\psi_0$ と E05-F23 で $\lVert a(f)\psi_0\rVert^2\le\frac{2\ln2}{3\pi}\alpha\lambda^2x^2$(353-B)は 300-C の $n_g$ より $\alpha^{2/3}\lambda^{4/3}$ 倍大きい;素の反跳の分母を入れた形 $n_g\le C\alpha x^2$ は LL と 316-1 の上界から偽(353-C)—— 自然な枠 $H(-k)$ では反跳がファイバーの運動量に吸収され、分母の抑圧は $g\cdot Q\psi_0$($\rho'$ の成分)の $H(-k)$ のスペクトルの重みの問題(F154 の射程)。
- **共通点(1 行)**:**エネルギーの 2 点の勘定は 300-C で最小になり、勘定の外に残る費用は「胞が局在モードの光子の運動量を精度 $x\Lambda$ で追跡する可能性」だけ —— それは (DEC-$p$, $p\gt2$)/反圧搾の深さの上界(F161 (3)・F164 段 (b))と同じ段。**
- **R9**:閉じたのは方式。双極子では $P_f$ が無く胞も追跡も無い(段は空);PF の段は追跡に移り消滅していない。
- **射程(T60)**:禁じるのは「エネルギーの 2 点の勘定(費用の比較・2 次の変分・pull-through の光子数の上界)で 300-C の配置を排除する」形の発注。止めないもの:追跡の可能性(胞の数 $N$ で $n_g$ 個の光子の運動量を精度 $x\Lambda$ で追う状態の $G_h$ の上界)を与える新しい道具;$g\cdot Q\psi_0$ の $H(-k)$ のスペクトルの重みの評価;C1 の玩具(胞の幅・数の分岐を持つもの)での値。
- **再開条件**:追跡の可能性の上界、または $g\cdot Q\psi_0$ の $H(-k)$ のスペクトルの重みが $E_0$ より上に集まることを示す入力が出たとき。

## F173(E05、全列(行 E1-H の内側)の供給 (LL-low$_{2/3}^+$)〔$F/\lambda^{2/3}\to\infty$〕を、E05-P170 の $h\to\infty$(対数密度 1)を下界 282-C/298-D の機構に戻す**自己無撞着(ブートストラップ)**—— 反跳 $k^2/2m$ を着衣の $k^2/(2mh)$ に置き換えて殻の分極を強め、$F/\lambda^{2/3}$ に $h^\gamma$ の因子を付ける方式。2026-10-20、hard_E05_bootstrap_72 = 難所の型、稿 `352_全列8_自己無撞着のブートストラップ_2026-10-20.md` §1〜§3、成算 S169)
- **閉じたのは: 方式**。標的((LL-low$_{2/3}^+$)・(LL-low$_{37/53}$)・(E1) 全列)と命題の真偽は閉じない。
- **理由(厳密な恒等式 + v-b の冪)**:(段 1)下界の鎖で $m$ が入るのは $T=\langle\pi^2\rangle_0/2m\le E_0$ の 3 箇所((L4) $x\le x_E$、298-A の $\lVert\pi^2\psi_0\rVert$、295-D の $Z$)だけで、$H(0)$ の運動項は裸の $m$ で厳密、$m_{\rm eff}$ はファイバー $P=0$ に現れない。Feynman–Hellmann(A-246-3 (2))で $T/E_0=\lambda F'/F$、$c\lambda^{2/3}\le F\le C_U\lambda^{5/7}$(P158・P167)からその対数平均は $[2/3,5/7]$、$\lbrace T/E_0\le\epsilon\rbrace$ の対数上密度 $\le\frac1{3(1-\epsilon)}$(補題 352-A)—— P170 の集合の大部分で反跳は $E_0$ の定まった割合で、$h\to\infty$ は $\lVert\pi\psi_0\rVert$ を抑えない。(段 2)$h$ が入る唯一の不等式は 199-B の交換子形 $\lvert\langle[X,\pi_z]\rangle_0\rvert^2\le m(1-1/h)\langle[X,[H,X]]\rangle_0$(観察 352-B)で、$h\to\infty$ は右辺を大きくする向き、$X=d\Gamma(B_h)$ では二重交換子が反跳 $h^2/2m$ を裸の $m$ で数えて $h$ 減衰を失う。精密化 $x_E\to x$ の固定点は微分不等式 $F\lambda F'\gtrsim\alpha^{2/3}\lambda^{4/3}$ で冪は 2/3 のまま(観察 352-C;F161 の尺度不変と同じ型)。双極子は $h\to\infty$ かつ $F\asymp\sqrt{\alpha\lambda}$ で含意そのものが偽(難しさは $P_f$ の反跳に保存)。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `532_hard_E05_bootstrap_72_recoil_toy_b.py`):4 モード玩具の強結合の隅で $f=1/h=0.14$〜$0.28$ の収束セルでも $T/E_0=0.55$〜$0.69$、運動量ずらし $X\psi_0$ の平均励起は裸の反跳の 3.9〜4.1 倍(PASS)。λ の梯子版 `532_…toy.py` は $f\to1$ に戻り仮定を実現しない(INCONCLUSIVE)。
- **生き残るもの**:補題 352-A(反跳の割合の対数密度、self-audited);観察 352-B(199-B の交換子形 —— $h$ の下界の道具としては使える);観察 352-C($x_E\to x$ の定数倍の精密化)。
- **再開条件**:(1) 左辺が $G_{\rm sr}$ 型(resolvent つき)で右辺が $h$ について減少する新しい不確定性(199-B の線形の試行の外);(2) $T/E_0\to0$ が対数密度 $\gt1/3$ で起こること(= $F\ge c\lambda^{2/3}$ と矛盾するので起こらない —— 標的の側の閉鎖ではなく、再開は (1) に限る)。

## F174(E05、全列(行 E1-H の内側)の供給 (α)(反跳つき Gibbs 測度の下での紫外の線形汎関数の分散 ≤ Wiener の定数倍)・(LLC)(334-C の連結 3 点関数の時間減衰)を、**紫外の殻の時間局所の小結合**(殻ごとの結合 $\sim\alpha$・核の時間到達距離 $\sim\Lambda_j^{-1}$)から Dobrushin–Shlosman・Holley–Stroock・log-Sobolev のテンソル化(高温・短距離の Gibbs 系の型)で殻に一様に出す方式。2026-10-20、hard_E05_dobrushin_72 = 難所の型、稿 `351_全列7_紫外の殻の時間局所の小結合_2026-10-20.md` §1〜§2、成算 S168)
- **閉じたもの**:**方式**((α)・(LLC)・(COV)・(E1) 全列の真偽ではない。補題 351-C〔(α) の対角部分〕は立った —— 非対角が残るだけ)。
- **理由(2 つの時間尺度、厳密な 2 次モーメントの勘定)**:(1) 殻 $j$ には核の到達距離 $\Lambda_j^{-1}$ と反跳時間 $\tau_0=m/\Lambda_j^2$ の 2 つの尺度があり、$\mathrm{Var}_W(q_j)\sim t\Lambda_j^2/m$ の半分は反跳時間より短い対から来る。相互作用が $O(\alpha)$ なのは反跳ブロックの単位でだけで、コヒーレンス時間あたりは $\alpha\sqrt{\lambda_j}$。(2) 反跳ブロックをサイトにすると到達距離は $\lambda_j$ サイト分で、距離 $n$ の対の結合は sup(閉じた経路 $b_s=b_r$、反跳の抑制なし)で $\alpha e^{-n/\lambda_j}$、Gauss 平均の rms で $\alpha n^{-3/4}$(殻の形に依らない)。影響係数の和は sup $\alpha\lambda_j$・rms $\alpha\lambda_j^{1/4}$ で $\lambda_j$ に一様でない($\lambda_j\lesssim\alpha^{-1}$〜$\alpha^{-4}$ の窓だけ)。符号の相殺つきの和 $O(\alpha)$ は一様だが、Dobrushin・Dobrushin–Shlosman・Zegarlinski・Holley–Stroock は三角不等式型で相殺を使えず、使う評価は底の測度の連結相関の時間減衰そのもの(F162 理由 (3) の段)。変数の取り方(コヒーレンス時間・大ブロック・粗い経路・Hessian 型・位置の対相互作用の形)を変えても同じ(稿 §1.4)。(3) 消費者の照合:混合が立っても殻あたり $|\lambda\partial_\lambda f|\lesssim\alpha\tau_c/\tau_0=O(\alpha)$ で $j$ に依らず、(LLC) の $C/\ln\lambda_j$ の尺度は出ない(合うのは $\lambda\le e^{C/\alpha}$ の窓だけ);(α) は一様な定数で足りるが、対角は補題 351-C で一様に出て、非対角(反跳ブロック間の連結相関)が (2) の段。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `531_hard_E05_dobrushin_72_kernel_rms.py`):核の Gauss 平均の局所冪 $-0.69$($n\in[8,64]$)→ $-0.78$($n\in[64,1024]$)で $-3/4$ に近づく;$S_{\rm rms}$ は $\lambda=10^2\to10^4$ で比 4.97、$S_{\sup}$ は比 100.7($\propto\lambda$)。相殺和の比は 1.208 で固定した閾値 1.2 を超過(値では未確定)。閉鎖の理由は (1)〜(3) の字面で、値は使わない。
- **共通点(1 行)**:**紫外の殻の「時間局所・小結合」は反跳時間の単位での像で、核の到達距離はその $\lambda_j$ 倍 —— sup 型の小ささを入力にとる高温の型は、閉じた経路で反跳の抑制が消えるために一様に立たず、一様性は符号の相殺(連結相関の時間減衰)に依る —— F159・F162・F164・F167・F169 と同じ段(正値性・sup 型の外の入力)。**
- **R9**:閉じたのは方式。双極子では核が位置に依らず $\ell$ は Gauss で段は空(Loewner);Nelson 型では 348-A(混合表示)で (α) は真。障害は PF の反跳(位相の非有界な振動)に局在し消滅していない。
- **射程(T60)**:禁じるのは「殻ごとの小結合を Dobrushin・Dobrushin–Shlosman・Holley–Stroock・LSI のテンソル化(sup 型の混合条件)で一様化して (α)・(LLC) を出す」形の発注。止めないもの:反跳ブロック間の連結相関の時間減衰を符号の相殺を取り込む方法(Fourier 側の振動性・HS の複素混合の上の cluster 展開)で出す角度(F169 再開条件 (1) と同じ対象);補題 351-C の対角の評価を他の消費者に使うこと;$\lambda\le e^{C/\alpha}$ の窓での評価(E-np N4 の側、E05 の全列には届かない)。
- **再開条件**:(1) 反跳つきの重みの下で反跳ブロック間の連結相関の時間減衰を与える、sup 型でない相関不等式または展開が 1 つ出たとき;(2) E05 族の値で紫外の $\ell_f$ の非対角の和($\mathbb E_{\mathcal N}[\ell_f^2]/\mathrm{Var}_W(\ell_f)$ の λ 依存)が読めたとき。

## F175(E05、全列(行 E1-H の内側)の供給 (α)(反跳つき Gibbs 測度の下での線形汎関数の分散・指数モーメントの上界)を、**共分散の表示の型**で出す方式:(i) Helffer–Sjöstrand の共分散表示・Witten ラプラシアン・Bakry–Émery の曲率、(ii) 抽象的な正値 Gauss 混合の存在(Bernstein / Stieltjes・Hausdorff の積率条件)、(iii) 凸(Gauss)+ 有界摂動の分解(Brascamp–Lieb + Holley–Stroock)。2026-10-20、w_E05_355 = 書き下しの型、稿 `355_全列11_共分散の表示の族_2026-10-20.md` §2〜§4、成算 S172)
- **閉じたもの**:**方式**((α)・(β)・(LLC)・(E1) の真偽ではない;$\mathcal N_t$ の Poincaré・LSI の真偽でもない)。
- **理由**:(i) HS 表示で (α) を出すには 1 形式の Witten ラプラシアンの底 $\ge1/C$ が要り、在庫の下界は点ごとの $I+\mathrm{Hess}V\ge1/C$;UV 殻の反跳の Hessian は局所の振幅 $c$ に $\propto c^2$ で ess-inf $=-\infty$(334-B の数値の確認)、典型の経路でも物理の殻の重みで $g\lambda_{\min}\propto-\kappa^{\approx2.4}$(値、N で安定、双極子の対照で人工物でない)。平均形(補題 355-A (b))は $\mathbb E_{\mathcal N}D^2V$ = 速度相関((SPEC-G) 型)と非線形汎関数 $D_\Phi V$ の 2 次モーメント(F159 の段)に戻る。Fock 側は重みが複素で正測度が無い(348-B)。(ii) 混合の存在は分散について何も言わず(分散 = 混合の平均)、指数形 ⟺ 混合の台 ⟺ $L$ の裾そのもの —— (α) と同値な量しか運ばない;消費者 $\ell_f$(338-A)は位相つきの確率積分で線形汎関数でない。(iii) どの凸 + 有界の分解でも直線上 osc$(V_b)\ge\max(V-V^{**})$、その gap は局所の振幅に $\propto c^2$ で ess-osc $=\infty$ —— Holley–Stroock の因子が有限にならない;Lipschitz・指数可積分の摂動版は (i) の段に戻る。
- **値の裏づけ(【T88】)**:(研究ノート: `535_w_E05_355_{hess,hessdip,hankel,osc,osc2,osc3}.py`)(計 30 s)。Hankel 6・8 次は全セルで矛盾なし(検出力なし)。典型の経路の 1 殻の gap は $g\cdot$gap ≤ 0.2(κ ≤ 16)。閉鎖の理由は構造と振幅の伸びで、典型値の大きさは使わない。
- **共通点(1 行)**:**3 本とも (α) を「経路について点ごとの凸性の代用品」(曲率の下界・混合成分の Loewner 順序・有界な非凸部分)に求め、その代用品が UV 殻の反跳の非凸部分(局所の電流の 2 次 × $|k|^2$、経路について非有界)で落ちる;平均形は (SPEC-G) 型と非線形汎関数の (α) に戻る —— F159・F162・F169 と同じ段。**
- **R9**:閉じたのは方式。段は双極子で空(Hessian は定数で正、混合は成分 1 個、分解は自明)—— 障害は反跳に局在し消滅していない。
- **射程(T60)**:禁じるのは「HS 表示・Bakry–Émery の点ごとの曲率」「抽象的な正値 Gauss 混合の存在」「凸 + 有界の大域分解(sup ノルムの Holley–Stroock)」で (α) を出す形の発注。止めないもの:典型集合 + 裾の勘定による局所化(Dobrushin・ブロックのテンソル化、稿 351 の族);Nelson 型の梯子への 348-A。
- **再開条件**:(1) 反跳の非凸部分を典型集合の外で指数的に小さい確率に閉じ込める裾の評価が $\Lambda$ に一様に出たとき(局所化の族の産物);(2) PF の重みの構成的な正値分解(F169 の再開条件 (1))。

## F176(E05、全列(行 E1-H の内側)の供給 (α) の非対角部分(反跳ブロック間の連結相関の時間減衰、334-C の連結 3 点関数)を、**符号の打ち消しの型**で出す方式:(i) 振動の打ち消し(反跳の位相の停留位相・非停留位相の評価で $(\Lambda|t|)^{-N}$ 型の減衰)、(ii) 複素の重みのクラスター展開(Gauss 場を積分する前の虚の HS 混合の上の Kotecký–Preiss 型の多体展開を殻ごとに)、(iii) 局在化(典型集合の上の Dobrushin・Holley–Stroock + 裾の大偏差)。2026-10-20、w_E05_360 = 書き下しの型、稿 `360_全列13_符号の打ち消しの族_2026-10-20.md` §2〜§4、成算 S175)
- **閉じたもの**:**方式**((α)・(β)・(LLC)・(E1) の真偽ではない;$\mathcal N_t$ の混合・連結相関の非摂動の大きさの真偽でもない)。
- **理由**:(i) 直接の対の閉じた経路の重みは Wiener で $(\tau_0/\tau)^{3/2}$(親の推論 1 はここで正しい)、非停留の部分は 1 次で $e^{-n/2}$;しかし停留の部分は時刻を跨ぐ閉じた対(多体の位相)にもあり、その数は 3 次元の過去と未来の交点で $\approx0.53\sqrt{\lambda_j}$ 本、2 次の摂動で連結相関を $\approx-c\alpha^2n^{-1/2}$ に落とし和は $\alpha^2\sqrt\lambda$ —— Hiroshima–Spohn 2005 Thm 4.1(有効質量の 2 次の係数が $\sqrt\lambda$ で発散)と同じ冪で、打ち消しの評価の出力(大きさ)が λ に一様でない;$\mathcal N$ への移送に要る局所の CLT(尺度 $1/\Lambda$ の反集中)は在庫に無く、(α)(分散の上界)と逆向き。(ii) 絶対値の評価は $|e^{ieX}|=1$ で sup 型に戻る(351-A);位相を保つ版の λ に一様な解析性は P117 と矛盾(命題 360-B:1 次の $A^2$ 項 $\frac\alpha{2\pi}$/ブロックが高次で主要部ごと打ち消される;Lieb–Loss 1999 の注意)、殻 1 枚でも同じ。(iii) rms の和 $\alpha\lambda_j^{1/4}$ は bulk の量で裾を切っても減らない;増分をスピンにすると両側の仕様が跨ぐ閉じた対で rms $\alpha\lambda_j^{1/4}$ 傾き、位置をスピンにすると自由な Gauss 鎖が臨界(Dobrushin の和 1);補題 360-A で $\mathcal N$ は Wiener の典型集合に乗らない;悪いサイトの浸透の勘定 $\sum_nn\cdot P(n)\sim\sqrt\lambda$ は多重尺度の収束の境界の外。
- **値の裏づけ(【T88】)**:(研究ノート: `537_w_E05_360_straddle.py`)(MEAN_ONLY:跨ぐ閉じた対の数の平均 $\propto\lambda^{0.57}$、平均/√λ 0.41〜0.56)・`_straddle_ext.py`(INCONCLUSIVE:中央値の冪が規則の帯の外、平均/√λ 0.42〜0.48)・`_dipF.py`(双極子で収束半径 $3\pi/(4\lambda)$、非摂動の値は 1 次の値に近づく)。閉鎖の理由は構造・在庫の定理・HS 2005 の定理で、値の大きさは使わない。
- **共通点(1 行)**:**3 本とも連結相関の大きさを λ に一様に小さく出す方式で、その大きさが 2 次の摂動ですでに $\alpha^2\sqrt\lambda$(跨ぐ閉じた対、HS 2005)、非摂動では対の統計が O(1) ずれる(360-A)—— 有界にするのは打ち消しでなく符号(復元の向き、$f\le1$ の側)で、F159・F164・F169 と同じ段(正値性の外の相関不等式)。**
- **R9**:閉じたのは方式。段は双極子で空(核が位置に依らず閉じる・跨ぐの区別が無く、Loewner 順序で符号が出る)—— 障害は反跳の位相の多体性に局在し消滅していない。
- **射程(T60)**:禁じるのは「停留位相・部分積分(Cameron–Martin)の大きさの評価」「複素の重み・符号つきの対の Mayer 展開の λ に一様な KP」「Wiener の典型集合の上の Dobrushin・Holley–Stroock + 大偏差の裾」で (α) の非対角・334-C を出す形の発注。止めないもの:符号の族(相関不等式・復元の向きの単調性);再総和された参照測度のまわりの展開・RG(F108 の再開条件);(α) の消費者 $\ell_f$ の 2 次の項の符号の計算(類 C の kill-check)。
- **再開条件**:(1) 跨ぐ閉じた対の寄与に符号を与える構造(復元の向きの相関不等式)が出たとき;(2) 遮蔽の済んだ参照測度($\theta\to0$ を示す殻の RG)が構成されたとき;(3) (α) の消費者 $\ell_f$ の 2 次の跨ぐ対の項が消える(形状因子・位相で $c_f=0$)と分かったとき。

## F177(E05、全列(行 E1-H の内側)の供給 (α) に対する類 C の懸念 ——「2 次の摂動の時刻を跨ぐ閉じた対の項 $\pm c_f\alpha^2\sqrt\lambda$(稿 360 観察 360-C)が (α) の消費者 $\ell_f$ に増幅の向きで乗り、摂動の窓 $\lambda\gtrsim\alpha^{-4}$ で (α) を偽にする」という否定の筋。2026-10-20、w_E05_363 = 書き下しの型、稿 `363_跨ぐ対の符号のkill-check_2026-10-20.md`、成算 S175 の追記)
- **閉じたもの**:**否定の筋(懸念)**((α) の非摂動の真偽ではない)。
- **理由**:跨ぐ部分の符号は増幅で厳密(補題 363-A:$\mathbb E_{\mathcal N}[xy]=-n_f/e^2\le0$、$\mathbb E_{\mathcal N}\ell_f^2=\mathbb E_{\mathcal N}\rho_f^2+4n_f/e^2$)だが、2 次では $n_f\le4\lVert\Psi\rVert_{\rm op}^2\lVert f\rVert^2$ で、反跳のない 2 光子の帯($k_1\approx-k_2$、360-C の Fock 側の像)は対の核の Hilbert–Schmidt ノルム(全光子数 $\sim\alpha^2\sqrt\lambda$)にだけ効き、作用素ノルムは反跳の領域が支配して λ に一様(対数まで)—— 1 つの $f$ に √λ は乗らない。
- **値の裏づけ(【T88】)**:(研究ノート: `539_w_E05_363_pairkernel.py`)(1 s):A(0)_z のモードの比 MODE_UNIFORM(局所冪 0.03)、全光子数 TRACE_SQRT(局所冪 0.58)、作用素ノルムの Schur の上界 OPNORM_UNIFORM(比 1.16/10 倍、対数の伸びは否定しない)。
- **共通点(1 行)**:**跨ぐ閉じた対の √λ は「多数のモードの和」(trace)の量で、(α) が要る「1 モード」(作用素ノルム)の量ではない —— 360-C の非一様性は (α) を摂動の窓で壊さない。**
- **再開条件**:作用素ノルムが λ の冪で伸びると分かったとき(角運動量の成分ごとの最大固有値の精密化);非摂動で 1 つの集団モードへの凝縮($n_g\sim\sqrt{\alpha N}$)の機構が示されたとき(それは 300-C の否定側)。

## F178(E05、全列(行 E1-H の内側)の道 1 の kill-check —— 観察 300-C の配置(局在した反圧搾のモード + 運動量を打ち消す胞の凝縮)を**明示の試行状態**(Gauss 状態 + 胞の 2 モード圧搾、$P=0$ ファイバー;運動量の濾過・平均つきの準自由・雲の中心を指針にする着衣を含む)にして $\langle H\rangle\le C\lambda^{2/3}\Lambda$ を出し、(LL-low$_{2/3}^+$) を偽にする〔または上界を $\lambda^{2/3}$ に下げる〕方式。2026-10-20、w_E05_365 = 書き下しの型、稿 `365_全列14_300Cの配置の試行状態のエネルギー_2026-10-20.md` §2・§3、成算 S178)
- **閉じたもの**:**方式**((LL-low$_{2/3}^+$)・$E_0$ の冪・300-C の配置の実現可能性の真偽ではない。補題 365-A 自身は立った —— 試行の族を縛るだけ)。
- **理由**:(1) 発注の字面の試行は平均 0 の準自由でパリティが偶 —— 交差項 $\langle\lbrace P_f,eA(0)\rbrace\rangle$ が 0 で、補題 365-A により $\langle H\rangle\ge\inf\sigma(H_{\rm e})$(偶模型 = 交差項を落とした模型の底)、LL 1999 Thm 1.2 の下で $\ge C_1\alpha^{2/7}\lambda^{5/7}\Lambda$;族の実際の最小は λ に線形(光子 1 個ずつが反跳を払う、胞の内側の打ち消しは胞の幅までしか効かない)。(2) 運動量の濾過 $\chi(P_f)\Psi_G$ も偶で同じ;構造としては濾過の幅が電子の局在の役を担い LL の積の族(5/7)に戻る —— 雲は $A(0)$ の圧搾の範囲を狭めない。(3) 平均つきの準自由は横波性で交差項を作らず結合を強めるだけ(読み)。(4) 雲の中心を指針にする着衣 $e^{ieA(0)\cdot X_c}$ は $e\,X_c\cdot\nabla A$ の項と雲の局在の費用の積で $\langle\pi^2\rangle\gtrsim\sqrt\alpha\Lambda^2$(線形、値)。(5) 300-C そのものは交差項が偶の運動の項を相対 $\lambda^{-2/3}$ まで打ち消すことを要り(365-C の下限 $\lambda^{-1/21}$ よりはるかに精密)、非可換な $\pi$ の 3 成分の追跡(磁場の床 295-F)を含む。
- **共通点(1 行)**:**交差項 0 の試行は全て偶模型の底 $\lambda^{5/7}$ より下がらない(365-A + LL Thm 1.2);$\lambda^{2/3}$ に届く試行は交差項で偶のエネルギーをほぼ全部打ち消すパリティの定まらない状態で、その構成は追跡の壁(F161 (3)・F164 段 (b)・F172)と同じ段。**
- **R9**:閉じたのは方式。双極子は $P_f$ が無く、偶模型の底が $\lambda^{1/2}$ —— 365-A と矛盾せず、障害は PF の $P_f$ の 2 次の追跡に移り消滅していない。C0 `541_`(4 モードの十字)は箱の鏡像の対で $P_f\equiv0$ になり Gauss が基底と 0.4% 以内で一致 —— 連続体の段を持たず判定に使わない。
- **射程(T60)**:禁じるのは「平均 0 の準自由・パリティの固有状態・$\langle A\rangle=0$ の積・運動量の濾過・指針の着衣で 300-C 型の試行を作り $O(\lambda^{2/3})$ の上界を出す」形の発注。止めないもの:交差項がほぼ全部打ち消す状態の構成(基底状態の連結相関を入力にするもの);LL Thm 1.2 の下界の連続体版の証明(系 365-B の定量形);奇の割合 $2\delta/\langle H_{\rm e}\rangle_0$ の上界((δ-FRAC)、251 行 1 —— 冪 5/7 の確定に効く)。
- **再開条件**:$-\langle H_{\rm o}\rangle_\Psi\ge(1-o(1))\langle H_{\rm e}\rangle_\Psi$ を満たす状態の明示の族(数値または解析)が 1 つ出たとき;または連続体の値(MPS・PIMC)で $2\delta/\langle H_{\rm e}\rangle_0$ が λ とともに 1 に近づく向きが読めたとき。

## F179(E05 / G3-2、難問 #1 紫外のくりこまれたフル PF 模型の構成を、**Gross 変換の最小結合版**(c 数の係数の線形の生成子 $e^{iT}$ で $P=0$ ファイバーの 1 次の項 $\frac em P_f\cdot A(0)$ を消し、残差を Nelson 1964 型の小さい相対有界で扱い、くりこみ族 $H_\Lambda(m_0(\Lambda))-E_\Lambda$ の (i) ノルム・レゾルベント / (ii) 強レゾルベント収束を元の Fock 空間で出す)で行う方式。2026-10-20、hard_E05_renorm_72 = 難所の型、稿 `366_難問1_くりこまれた模型の構成の設計_2026-10-20.md` §1〜§4、成算 S179)

- **閉じたもの**:方式(標的 #1 と「くりこまれた極限が存在する」命題の真偽は閉じない)。
- **止まる段**:(1) $P=0$ ファイバーに消すべき c 数の 1 次の項が無い:$P_f\cdot A(0)\Omega=0$(横波性)、回転不変な基底状態で $\langle a(f)\rangle_0=0$(`E05-F22`)—— Weyl 型の線形の着衣は $P=0$ の基底状態の着衣になれない(補題 366-B (B1))。(2) 発散を担うのは 1 次の項でなく対の項 $\frac{e^2}{2m}A^2$(真空の値 $\frac{\alpha\Lambda^2}{2\pi m}$、$H_f$ に対する相対有界の定数 $\propto\alpha\lambda$)で、線形の変換では消えない;対の着衣(Bogoliubov)の Shale ノルムは背中合わせの対($\lvert k+k'\rvert\lesssim\sqrt{mk}$、反跳の分母が効かない)で $\lambda^{1/2}$ の冪で発散(C0 (研究ノート: `542_hard_E05_renorm_72_shale.py`) POWER、局所冪 0.58、【値】)—— Nelson の「線形の着衣が Fock 空間のユニタリに収束する」段が最低次で既に無い。(3) くりこみ族に沿って裸の速度の揺らぎ $\langle v^2\rangle=2\langle T\rangle/m_0\ge\lambda_0(1+\frac{9\pi}{4\alpha\lambda_0})^{-1}\to\infty$(`E05-P119` 系 205-F (i)、v-b):c 数の係数で扱える平均の速度は 0、残差は揺らぎで決まり小さくない。(4) 循環:正しい 1 光子の振幅の尺度は $e\nabla E(P)$(有界)で、裸の $eP/m_0$ とは $h(\lambda_0)\to\infty$ 倍ずれる —— 生成子にくりこまれた速度(未知の $h$)が要る。Nelson でこれを断つのは質量のくりこみの有限性で、PF では双極子の段で既に $\delta m=\frac{4\alpha}{3\pi}\Lambda$。(5) 作用素値の係数 $T(P)=(P-P_f)\cdot\Phi(0)$ は対称に定義できるが、$e^{-iT}a_ke^{iT}$ の級数が $-ka_k\cdot\Phi(0)$ の項で閉じず、変換後の Hamiltonian に閉じた形が無い。
- **(i)(ii) を元の Fock 空間で立てることについて**:$m_0\to0$ で運動項 $\frac1{2m_0}\Pi^2$ は拘束 $\Pi\approx0$ になり、有界なエネルギーの状態は拡大像で弱 0 に逃げ(`E05-P116` 命題 194-1)、拘束の解集合は Fock 空間で $\lbrace0\rbrace$(同 (5))。極限はあるとしても元の表現の外(標的の誤設定)。
- **難しさの移り先**:(a) 分散関係の収束 (iii) の非退化 = 運動量 $p$ での $m_{\rm eff}$ の上からの評価(FR-G3-9 と同じ壁、難問 #3 の上側);(b) 着衣の表現の正則性(軟らかいモードの占有の Λ 一様性)。圧縮性(部分列の局所一様収束)は補題 366-A(Fröhlich 型の移動不等式)で条件なし。
- **再試行しない条件**:線形(Weyl 型)の生成子、または係数を c 数に置き換えた自己無撞着の処方(ポーラロン型)で $P=0$ ファイバーを扱う限り。再開条件:着衣の表現の正則性 (R) が(数値で)肯定され、かつ $m_{\rm eff}$ の上側の道具が 1 本立ったとき。

## F180(E05 の外・難問 #1 の (iii-2) 非退化〔くりこみ族 $m_0(\Lambda)$ に沿って固定の $p\ne0$ で $\mathcal E_\Lambda(p)\ge c(p)\gt0$〕を、稿 367 の Cramér–Rao + Green–Kubo(E05-P192)と補題 369-A で出す方式。2026-10-20、w_E05_369 = 書き下しの型、稿 `369_難問1と3_非退化と冪の改良_2026-10-20.md` §1・§5)
- **閉じたもの**:方式(命題の真偽ではない。値の水準では窓の崩壊を示唆する値は無い、366 §6.2)。
- **止まる段**:(s1) ファイバー $p\ne0$ に基底状態が無く(無質量の光子)、定常測度と Green–Kubo が立たない。分散(2 次のキュムラント)は $\lVert e^{-T(H(p)-E_0)}\rVert$ の減衰を与えない。(s2) 族に沿う一様性:$m_0h_{\rm sr}\le m_0+\Phi_a+\Phi_c$ で、作用素ノルムの型の $\Phi_a$ の上界は 366-A の $\mathcal E(k)\le\lvert k\rvert$ のため、どんな $\mathcal E$ の下界を入れても $\ge\frac{2\alpha}{3\pi}\Lambda$。367 の反跳項の評価は $\lVert Q\psi_0\rVert^2\ge m_0^2\lambda_0$(E05-P119)に当たる。369-A はそれを避けるが、$\Phi_c\le\frac{4\alpha}{81\pi}\Lambda\lambda_0$ が残る。
- **共通の段**:ψ0 の $H(k)$ のスペクトル測度の低エネルギーの重み $\mu_k([0,\eta])$ の上界(経路の増分の特性関数の反集中)。#1 の非退化・#3 の上側の一様版・FR-G3-9 の $h_{\rm sr}$ 版(369 §5)が同じ 1 本を要る。在庫の FK の正値性・試行状態・和則は、どれも上界の向きか 2 次までしか与えない。
- **再開条件**:$\mu_k([0,\eta])\le\epsilon(\eta,k)$ 型の反集中の評価($k\gg m_0$、族に一様)の道具の文献、または構成。

## F181(E05、難問 #2 と全列(行 E1-H の内側)の供給 (LL-low$_{2/3}^+$)〔$F/\lambda^{2/3}\to\infty$〕を、下界 298-D の固定点 2/3(323-B、F161)を破る 4 つの機構 —— (a) 殻をまたぐ相関(跨ぐ閉じた対、補題 363-A の増幅の符号)を下界の鎖に入れる、(b) 反跳の割合の対数密度(補題 352-A)と 5/7 の上界の間の情報($F$ の凹性 + 2 点の評価)、(c) 2 光子・4 点の FI の符号(338、F164)と 4 重交換子を下界の側で使う、(d) 2 ループの値で冪の補正(対数の因子)の符号を読む —— で出す方式。2026-10-20、hard_E05_exp23_72 = 難所の型、稿 `364_難問2_下界の冪を2_3より上げる_2026-10-20.md` §2〜§3、成算 S177)
- **閉じたもの**:**方式**((LL-low$_{2/3}^+$)・(NC-A)・(δ-FRAC)・$E_0$ の冪の真偽ではない)。
- **理由(在庫の同値形 + 整合模型 + 値)**:(0) 発散因子は E05-P137(258-B)+ E05-P191(365-C)で (NC-A$_\eta$) $e^2\langle A(0)^2\rangle_0\le C_AmE_0\lambda^\eta$、$\eta\lt1/21$ ⟺ $A(0)$ の圧搾の率 $\langle A(0)^2\rangle_0/\langle A(0)^2\rangle_\Omega\lesssim\lambda^{-2/7+\eta}$ ⟺ $A(0)$ に結合するモード $\hat g$ の縮約状態がほぼ純粋な圧搾状態($|\langle a_{\hat g}^2\rangle_0|^2\ge n_g(n_g+1)(1-O(\lambda^{\eta-1/3}))$)に帰着する(観察 364-A)。(a) 363-A は Fock では $4n_g=\langle:\Pi_{\hat g}^2:\rangle_0+\langle:\Phi_{\hat g}^2:\rangle_0$(282 §3.2 (iii) の $|\langle a^2\rangle|^2\le n(n+1)$)で、FI の Π 側の符号 $\langle:\Pi^2:\rangle\ge0$ は向きだけで純粋性の率を与えず、殻間の相関は 323-B の鎖の変数($x$・$N_s$・$n_{g,s}$・$G^{(s)}_h$)に現れない。(b) $F_0=c\alpha^{1/3}\lambda^{2/3}$ は在庫の $F$ の全制約(凹・非減少・両側の冪・352-A の対数密度・352-C の点ごとの微分不等式・290-A の族)を満たす整合模型で、$F$ の関数形は $\delta$ を含まない(Feynman–Hellmann $\alpha\partial_\alpha E_0=\frac{e^2}{2m}\langle A^2\rangle_0-\delta$ は差しか与えない)。(c) 4 点の符号は平均 0・軸圧搾の全 Gauss 状態で等号(F164 (2))、4 重交換子の期待値は $\rho'$ 型のコヒーレンスと反圧搾の quadrature($G_h$ 自身の階数)に分かれ、Jacobi でどう並べても 300 §2.1 の「$\rho'$ は遮蔽されていない」か磁場の床に戻る。(d) $P=0$ ファイバーの $e^4$ 項は反跳が分母を支配して $-c_2\alpha^2\lambda\Lambda$($\lambda J\to2.75$、LINEAR)で 1 ループと同じ $\lambda^1$;$\lambda^{2/3}$ の領域($\lambda\gtrsim\alpha^{-2}$)は再総和の先で、固定次数の符号は対数の因子の向きを決めない。
- **値の裏づけ(【T88】)**:(研究ノート: `540_hard_E05_exp23_72_twoloop.py`)(0.4 s、LINEAR:$J$ の局所冪 −0.76→−0.99、帯の割合 $\lambda^{-0.55}$)、`540_hard_E05_exp23_72_oddfrac.py`(25 s、4 モード玩具、ODD_TO_ONE:奇の割合 $2\delta/\langle H_e\rangle_0$ = 0.62→0.993、$E_0/\inf\sigma(H_e)$ = 0.36→0.06、λ=2→128、α=0.1・0.3)。閉鎖の理由は在庫の定理と整合模型で、値の大きさは使わない。
- **共通点(1 行)**:**4 本とも「有限モードでも成り立つ入力(CCR・パリティ・$H_f\ge0$・LL 型の不確定性・FI の符号・Feynman–Hellmann・$F$ の関数形)」の組み合わせで、有限モードの玩具では奇の割合が 1 に行く(観察 364-B)ので (NC-ε)/(δ-FRAC) はその類からは出ない —— 要るのは連続体の入力(モード数、298-D の鎖の型)で 300-C の (II) 型(反圧搾の $A$ を $P_f$ との交差項で打ち消すもつれた追跡)を排除する率;F161 (3)・F164 (b)・F172・365 §3 と同じ段。**
- **R9**:閉じたのは方式。段は双極子で空($P_f$ が無く $\delta=0$、(NC-A) は $\frac{e^2}{2m}\langle A^2\rangle=\frac12E$ で自明に成立)—— 障害は反跳と $A(0)$ のもつれた打ち消しに局在し消滅していない。
- **射程(T60)**:禁じるのは「跨ぐ対の符号(363-A)・殻間の相関・FI の 4 点の符号・4 重交換子・$F$ の関数形の制約・固定次数の摂動の値」で (LL-low$_{2/3}^+$)/(NC-A$_\eta$) を出す形の発注。止めないもの:連続体の入力で $A(0)$ の圧搾の率を出す角度(298-D の鎖の型の拡張、モード数を使う不確定性);値の側の kill-check(連続体の試行の族・A1 の PIMC で $e^2\langle A(0)^2\rangle_0/(2mE_0)$ の λ 依存)。
- **再開条件**:(1) 連続体の入力で (NC-A$_\eta$)、$\eta\lt1/21$ を出す機構が 1 つ出たとき;(2) 値で $e^2\langle A(0)^2\rangle_0/(2mE_0)$ が λ で伸びない(5/7 側)と分かったとき;(3) 300-C の (II) 型が基底状態でないことの率つきの排除(F172 の再開条件と共通)。

## F182(E05、難問 #1 の非退化 (iii-2)・#3 の上側の一様版・FR-G3-9 の $h_{\rm sr}$ 版を「$\psi_0$ の $H(k)$ についてのスペクトル測度 $\nu_k$ の低エネルギーの重み $\nu_k([0,\eta])$ の反集中」1 本で進める方式(369 §1 (s2)・§5 の特定)—— (a) Mourre・正の交換子 /(b) Feynman–Hellmann・凹性・Tauber /(c) TRK 369-A + モーメント(Chebyshev・モーメント問題)/(d) 値 の 4 候補。2026-10-20、hard_E05_anticonc_72 = 難所の型、稿 `373_難問1と3_スペクトル測度の反集中_2026-10-20.md` §1・§3・§4、成算 S182)
- **閉じたもの**:方式(標的 (iii-2)・Q3 の上側・FR-G3-9 の真偽は閉じない)。
- **理由(厳密 + 値)**:(1) 消費者の照合(§1):族に沿う $m_0h_{\rm sr}\le m_0+\Phi\le Cm_{\rm ph}$ に要る形は $\nu_k([0,\delta k^2/2m_0])\lesssim h/\lambda_0$ で、2026-09-13 の (N110)(`E05-P58` 3.・`E05-P60` 1.・2.:$\lambda^{-1}$ 減衰は (N110) からしか出ない)と同じ型 —— F78〜F86 で 9 本の方式が閉じ、F84 が形式展開の次数に依らず構造的に閉と記録済み。(2) (c):台・平均の LP の最適値 $a/\Lambda$(`E05-P60` 4.)、2 次モーメント(`E05-P66` 1.)の Chebyshev は壁 $4\mathcal K/3k^2$ が殻の下端で $\gg1$(`E05-P62` 3.);縦の TRK(369-A の $\hat k\hat k^{\rm T}$ 版)は Stratonovich の中点で $v_k=\frac m{|k|}A_k\psi_0$、$\langle v_k,A_k^{-1}v_k\rangle=m/2$ の等式に退化。(3) (a):Mourre はスペクトルの型を与え、特定のベクトルの重みの上界を与えない;閾値 $E_0+|k|$ の 1 光子状態は $H_f$ の連続体の底で、無質量では交換子が正に有界でない。(4) (b):$k\ne0$ の基底状態が無い(FH 不可);凹性は結合密度について;$\nu_k$ からは $E(k)$ の上界しか出ない(`E05-P58` 4. の「エネルギー的排除は原理的に無い」)。(5) **反集中が立っても消費者は閉じない**:補題 373-A(厳密、367 の恒等式の極限)$1/h_{\rm sr}=1-\Phi/m+\Psi$、$\Psi=\lim\frac Tm\mathrm{Var}_\mu(D_hV)\ge0$ で(⟺ $\Phi-m\Psi=2G_{\rm sr}$)、Cramér–Rao は $\Psi\ge(\Phi/m)^2/(1+\Phi/m)$ と同値(緩みはその差;改良に要るのは $\mathrm{Var}_\mu(D_hV)$ の精密な下界で、(α)〔分散の上界〕とは向きが逆 —— 監査 376 §3);$\Phi_c$ の形式 2 次の値は閾値帯(F20 の配置)から $0.0176\alpha^2m\lambda^{3/2}$(C0 548、局所冪 1.503、SUPER)で、族に沿う $\Phi\le Cm_{\rm ph}$ は $h\gtrsim\alpha^2\lambda_0^{3/2}$ を要し非終端の族($h/\lambda_0\to0$、`E05-P131`)と両立しない向き【値、T88】。
- **共通点(1 行)**:**$\psi_0$ の測度の反集中は $\Phi_a$ の中の量にしか効かず、律速は $u_k=P(k)Q\psi_0$ の測度の閾値帯($\Phi_c$)と $\Phi-m\Psi=2G_{\rm sr}$ の打ち消し($\mathrm{Var}_\mu(D_hV)$ の精密な下界 —— 元の問いの書き換えで、(α)〔分散の上界〕とは向きが逆、監査 376 §3)—— 369 の「1 本」は「(N110)」と「$\Phi_c$ の閾値帯 + $\mathrm{Var}_\mu(D_hV)$ の精密な下界」の 2 本。**
- **射程(T60)**:禁じるのは「$\nu_k$ の反集中を (a)〜(d) の型で立てて Cramér–Rao の供給(367)を族に沿って一様化する」形の発注。止めないもの:(N110) の 2026-09-13 の再開条件;(α) の壁の直接の評価(全列の総攻撃の行);$\Phi_c$ の非摂動の値の測定(値の問題として);(iii-2) の「$p$ についての凸性 + 窓の一様性」の設計(ただし凸性は F170 の射程)。
- **再開条件**:(1) $\Phi_c$ の非摂動の上界が $\lambda$ の 1 次(閾値帯の重みの非摂動の抑制)で出たとき;(2) (N110) が v-b で載ったとき;(3)〔削除(監査 376 §3・indep_376 §I-376):旧の「$\Psi$ の上界が λ に一様に出たとき」は向きが逆($\Psi$ の上界は $h_{\rm sr}$ の下界を与えるだけ)で、向きを直した「$\Psi$ の Cauchy–Schwarz の値を超える下界」は $G_{\rm sr}$ の族に一様な上界(#3 の上側の一様版の字面 $m_0h_{\rm sr}\le Cm_{\rm ph}$)と同値で、それは E05-P118 から $C=1$ で自明に成り立つ(観察 378-1、稿 `378_` §1)—— 消費者((iii-2)・FR-G3-9・Q3 の上側)を持たないので再開条件にしない〕。

## F183(E05、全列(行 E1-H の内側)の供給 (α)(反跳つき Gibbs 測度 $\mathcal N$ の下での紫外の位相つき線形汎関数 $\ell_f$ の分散の上界)・(LLC) を、**4 つの新しい型**で出す方式 —— (a) Polchinski 流の多重スケール Bakry–Émery(Bauerschmidt–Bodineau–Dagallier 2023 Thm 3.6:Wiener の時間尺度の分解に沿うくりこまれたポテンシャル $V_t$ の Hessian の下界)、(b) 確率局在化(Eldan、Chen–Eldan;BBD Cor. 3.22 の局在化した測度の共分散の上界)、(c) 反射結合(Eberle 2016 の $\kappa(r)$ による Wasserstein 縮小)、(d) Hilbert 空間の側の感受率(369-A の TRK 型の正値性で $\Psi=\lim\frac Tm\mathrm{Var}(D_hV)$ を上から)。2026-10-20、hard_E05_newtype_72 = 難所の型、稿 `374_全列15_壁への新しい型_多重スケールと確率局在化と結合_2026-10-20.md` §2〜§5、成算 S183)
- **閉じたもの**:**方式**(4 本)。(α)・(LLC)・全列の真偽ではない。
- **理由 (a)(原典照合 + 雑な計算 + C0)**:Thm 3.6 の仮定 (3.32) は**全ての φ**(点ごと)。粗い尺度 $t\gg\tau_0^{(j)}=m/\Lambda_j^2$ ではブロックを跨ぐ直接項は細かい揺らぎの Gauss 平均で $e^{-O(t/\tau_0)}$ に減衰し(玩具で 0.12、$t/\tau_0=16$)、殻 $j$ の非 Gauss 性が粗い場に残るのは質量のくりこみ(凸)と生成項だけ —— ここまでは親の推論 1 の向き。しかし 2 階微分の恒等式 $\mathrm{Hess}V_t=\mathbb E_{\rm tilt}[\mathrm{Hess}V]-\mathrm{Var}_{\rm tilt}(\nabla V)$ の**分散の項**は、ブロック内の直線の粗い配位(速度 $v$)で、重なる対($|s-s'|,|r-r'|\lesssim\tau_0$)の連結部分 $\cos(\kappa v(\tau-\tau'))$ が振動せず $\propto v^4\min(\tau_0,1/\kappa v)\sim v^3$ で発散する(観察 374-A;C0-a′ `551_…_a2_polchinski_var.py` で傾き 2.82、J-a3 VAR_UNBOUNDED【値】)。$v\ge\Lambda_j/m$ のブロックは Wiener 確率 $e^{-t/2\tau_0}\gt0$ の bulk の事象で除けず(360 §4 (3))、尺度 $t\lt1/m$ では未積分の殻($\Lambda_j\lesssim\sqrt{m/t}$)が常にある。ゆえに全ての尺度で $\inf_\varphi\mathrm{Hess}V_t=-\infty$。負の曲率の**蓄積**($1/\gamma\sim\lambda^{O(\alpha)}$)は (α) の消費者($o(\sqrt{\alpha N})$)の許容内で、止まる段ではない。平均の判定・典型集合・周波数帯・HS 側(複素)は 355 §2.3・360 §4・348-B で閉。
- **理由 (b)**:等方の局在化では局在化した測度の族 = Cameron–Martin のずらし × 質量 $m(1+t)$ の PF 測度で、要る入力(Cor. 3.22 (3.107)、∀φ の共分散の上界)は $t=O(1)$ での (α) の共分散の行の版 —— 循環;自動の利得は質量の増加($\lambda_t=\lambda/(1+t)$)だけで、分散の分解の Gauss の重みのうち $1/(1+\lambda)$。非等方(Polchinski 型)では (3.78) の型 $\mathrm{Hess}V_t=\frac1t-\frac1{t^2}\mathrm{Var}_{\mu^\varphi_t}$ により共分散の上界 ⟺ (a) の分散の項。「スペクトル独立」型の入力は Dobrushin(F174)。
- **理由 (c)**:$\kappa(r)$ は対について inf(線分平均の曲率)で、白色座標の $\mathrm{Hess}V$ の ess-inf $=-\infty$(355 C0-(i)、振幅 $c^2$)から $\kappa(r)=-\infty$;非凸「領域」は全空間で、典型集合に限っても次元 $3t/dt$・距離 $\sqrt{2d}$ で指数 $KR^2$ が発散、成分ごとの結合は Dobrushin(F174)。C0-c(乱数方向・振幅 ≤ 4)では非凸は検出されず(線分平均曲率 ≥ 0.957)—— 裾の現象。
- **理由 (d)**:恒等式 373-A(監査 376 で v-b)は $2G_{\rm sr}=\Phi-m\Psi$ の分解にすぎず(A-376-1)、$\Psi$ の非自明な上界 ⟺ $G_{\rm sr}$ の下界 = P118 の変分;FK/TRK の正値性(369-A)はレゾルベントの 2 次形式の**上界**で逆向き;Feynman–Hellmann の 2 階は $k\ne0$ の基底状態を要る。補題 374-B(Jensen):$\Phi_a\ge\Phi_a|_{\nu_k=\delta_a}=\frac{8\alpha m}{3\pi}\ln(1+\lambda/2)$ で $\Psi\ge\frac{8\alpha}{3\pi}\ln(1+\lambda/2)-1+1/h_{\rm sr}\to\infty$ —— 「$\Psi\le C$」は偽。全列の $\ell_f$ 側の Hilbert 対応物 $\langle:\Pi_f^2:\rangle$ の上界は F164 (4) の循環。
- **共通点(1 行)**:**4 本とも「くりこまれた/局在化した/結合した測度の曲率(共分散)の、配位について一様な評価」を入力に要り、PF の反跳では粗い尺度に移しても一様性が粗い速度の裾で破れる —— 破るのは平均項でなく分散の項(重なる対の非振動部分 = 371 §7 の「対角の閉じる確率」の多重スケールでの現れ);F174・F175 (i)(iii)・F176 (iii) の 1 段先、同じ段。**
- **射程(T60)**:禁じるのは「Polchinski 流・確率局在化・反射結合の点ごとの曲率/共分散の条件(BBD (3.32)・(3.107)、Eberle の $\kappa(r)$)を裸の、または時間尺度でくりこんだ反跳の重みに当てて (α)・(LLC) を出す」形の発注、および「$\Psi$ を Hilbert 側の正値性で上から押さえて $h_{\rm sr}$ を縛る」発注。止めないもの:多重スケールの枠で**分散の項**(重なる対の非振動部分の和)を λ に一様に押さえる道具(= 閉じる確率の評価、F169 再開条件 (1)・371 §7 と同じ対象);跨ぐ直接項の減衰(374-A の肯定の部分)を他の消費者に使うこと;$\lambda\le e^{C/\alpha}$ の窓での評価。
- **再開条件**:(1) くりこまれたポテンシャルの分散の項 $\mathrm{Var}_{\mu^\varphi_t}(D_\phi V)$ の、粗い速度の裾を含む一様な上界(例:$v$ の裾を次の尺度の積分で指数的に抑える機構が λ に一様に示されたとき);(2) PF の重みの構成的な正値分解(F169 再開条件 (1))。

## F184(E05、難問 #3 = HP-G3-1 の Q3 の上側の「一様版」—— くりこみ族 $m_0h_{\rm ls}(\lambda_0)=m_{\rm ph}$ に沿う $h_{\rm sr}$ の一様上界(⟺ 反跳つき Gibbs 測度の拡散定数の下界 $\lim\frac{m_0}T\mathrm{Var}X_T\ge\frac1{Ch}$、監査 376 §I-376 の I-11)を新しい行として立てる置き方。2026-10-20、w_E05_378_diffusion = 書き下しの型、稿 `378_難問3_一様版_拡散定数の下界_2026-10-20.md`、成算 S185)
- **閉じたもの**:**標的の置き方**(行として立てない)。命題の真偽については:字面の形 (L1) $m_0h_{\rm sr}\le Cm_{\rm ph}$ は**真**(閉じた、$C=1$、観察 378-1);Cramér–Rao の供給の一様性 (L2) $m_0+\Phi\le Cm_{\rm ph}$ と $h$ の族に沿う有界性 (L3) は値で偽の向き(真偽は閉じない)。
- **理由(厳密 + 字面 + 値)**:(1) E05-P118(補題 199-B)の試行 $\eta_\epsilon=\frac1m(A_0+\epsilon)^{-1}\pi_z\psi_0$、$\epsilon\downarrow0$ で $2m\limsup_{p\to0}(E(p\hat z)-E_0)/p^2\le1/h_{\rm sr}$、すなわち各 λ で $h_{\rm sr}\le h_{\rm ls}$;族の上で $m_0h_{\rm sr}\le m_0h_{\rm ls}=m_{\rm ph}$。I-11 の 3 つの同値形は全て $C=1$ で成り立つ。(2) 消費者の字面:#1 の非退化 (iii-2) は $p\ne0$ 固定の $\mathcal E_\Lambda(p)\ge c(p)$(366 §6.2;$p\to0$ の曲率は族の定義で固定済みで、$p=0$ の量はどの形でも届かない)、FR-G3-9 の $h_{\rm sr}$ 版は固定の裸の質量の各 λ の比較(369 §5)、Q3 の上側は $h_{\rm ls}$ の上界で $h_{\rm sr}$ の上界は移らない(367 R1)—— どれも (L1)〜(L3) を消費しない;(L2) は真でも定理 367-1 を通して (L1) しか出さない。(3) 値【T88】:1 ループの族の固定点は $h\simeq\frac{8\alpha}{3\pi}\ln(\Lambda/m_{\rm ph})$ の発散(形 A)か有限の Λ での終端(形 B);A1 の局所冪 $\gamma\approx0.65$〜$0.73$(NUM-3883)で $h\sim(\Lambda/m_{\rm ph})^{\gamma/(1-\gamma)}$;(L2) の比は $\lambda_0^{1.5-\gamma}$ で伸びる(NUM-6721)。(研究ノート: `557_w_E05_378_diffusion_family.py`)。
- **共通点(1 行)**:**くりこみ族は $p=0$ の曲率の有効質量 $h_{\rm ls}$ で定義されているので、族に沿う $p=0$ の量の「一様版」は $h_{\rm ls}$ との比較に退化し、変分原理の向き($h_{\rm sr}\le h_{\rm ls}$)では只、逆向き($h_{\rm ls}\le Ch_{\rm sr}$、(H-curv) の量化版)では族と無関係な各 λ の問い —— 実質は (iii-2) の有限の運動量の窓と (H-curv) にある。**
- **R9**:再開条件に (L1) を書かない(真)。(L2)・(L3) は消費者が無いので再開条件にしない。
- **射程(T60)**:禁じるのは「族に沿う $h_{\rm sr}$ の一様上界・拡散定数の $1/(Ch)$ 型の下界・Cramér–Rao の供給の族に沿う一様性」を難問 #1・#3 の行として発注すること。止めないもの:(iii-2) の有限の $q$ の窓の評価、(H-curv) の量化版 $h_{\rm ls}\le Ch_{\rm sr}$(これと定理 369-1 で $h_{\rm ls}\le C'\lambda^2$)、λ の陽な関数での拡散定数の下界(= Q3 の上側、族と無関係)。
- **再開条件**:(1) 消費者の側で、族に沿う $p=0$ の量の一様性を入力にする定理が現れたとき(その入力の形を字面で照合し直す);(2) 族の定義を $h_{\rm ls}$ 以外(例えば有限の運動量の曲率)に替える承認があったとき。

## F185(E05、全列(行 E1-H の内側)の供給 (α)(反跳つき Gibbs 測度 $\mathcal N$ の下での紫外の位相つき線形汎関数 $\ell_f$ の分散の上界)・(LLC)・(LL-low$_{2/3}^+$) を、**点ごとの曲率なしの Poincaré**で出す方式 —— (a) Lyapunov 関数の条件 $LW\le-\theta W+b\mathbf 1_K$ と $K$ の上の局所 Poincaré の組(Bakry–Barthe–Cattiaux–Guillin 2008、Bakry–Cattiaux–Guillin 2008 Thm 3.6・Cor. 3.4)、(b) 負の曲率が積分可能なときの Bakry–Émery の変種(F.-Y. Wang の型)、(c) (a)(b) を Polchinski 流の殻ごとに当てて積を取る。2026-10-20、w_E05_377_lyapunov = 書き下しの型、稿 `377_全列16_裾の事象とLyapunov型のPoincaré_2026-10-20.md` §1〜§3、成算 S184)
- **閉じたもの**:**方式**((α)・(LLC)・(LL-low$_{2/3}^+$)・全列の真偽ではない;$\mathcal N$ の Poincaré の真偽でもない)。
- **理由(消費者の字面 + 厳密な補題 377-A)**:(1) Lyapunov の方法の出力は carré du champ の形 $\mathrm{Var}_\mu F\le C_P\int\Gamma(F)d\mu$(BCG Def. 3.2・Cor. 3.4;$\mathcal N$ の Langevin の生成子の Γ は漂移に依らず白色座標の $|DF|^2$)。(2) (LLC) は分散でなく 3 次キュムラントの率の下界(334-C):Poincaré + CS は $t^{3/2}$ で $\sqrt t$ 足りず、$t$ を取り戻す半群の表示は点ごとの曲率(F175 (i)・F183 (a))か生成子の有限伝播(核の赤外の裾 $\propto\tau^{-2}$)を要る。(3) (LL-low$_{2/3}^+$) へ行く (α)(338 §0・363-A:$e^2\mathbb E_{\mathcal N}\ell_f^2=o(\sqrt{\alpha N})\lVert f\rVert^2$)は分散だが位相つきで、**補題 377-A(厳密)**:Wiener の下で 1 モードの型 $F$ について $\mathbb E_W\Gamma(F)/\mathrm{Var}_WF\to1+\frac{k^2}{2m\omega}$(平均のカオスの次数;$\omega=|k|$ で $1+\lambda_k/2$)—— 理想の $C_P=1$ でも上界は真の値の $\lambda$ 倍。許容は $o(\sqrt{N/\alpha})\mathrm{Var}_W\ell_f\lesssim\lambda^{6/7}\mathrm{Var}_W\ell_f$($N\le E_0/m\le C_U\alpha^{2/7}\lambda^{12/7}$、316-1)で、Γ 形の経路は「$\mathcal N$ が打ち切った位相つきの汎関数の 2 次モーメントを Wiener の値の $\lambda^{-1/7}$ 以下に抑える」入力を要る —— (α) を λ の冪だけ強めた同じ型(系 377-A′;値 363-B では偽の向き)。$C_P$ を小さく取る道は細かい時間尺度の方向で $C_P\ge1-o(1)$(雑)。(4) 供給の側は止まる段でなかった:裾の事象 × 分散の項の期待値は $t/\tau_0$ だけの関数で殻に一様に有限、1 ブロックの drift 条件は 1 階の量(tilt の平均)だけを使い 374-A の分散の項が現れない;壁は経路全体での局所 Poincaré の定数(drift が外れる集合が典型集合を含み、Holley–Stroock の $e^{\mathrm{osc}V_t}$ が示量的)とテンソル化(F174 の段)。(5) 殻ごとの積 $\lambda^{O(\alpha)}$ は許容内だが、377-A の損失は消費者のモードの位相から来る 1 因子で殻の数に依らない。
- **値の裏づけ(【T88】)**:(研究ノート: `556_w_E05_377_lyapunov_drift.py`)(32 s;374 の玩具):J-L1 DRIFT_OK($|r|\le1.1\times10^{-3}$)、J-L2 FINITE_UNIFORM($T(\kappa)\in[1.00,1.40]$)、J-L3 EXP_FINITE(Bv の傾きの中央値 1.01;κ=8 は 2.1〜3.3 で ESS 6〜81)。`556_w_E05_377_lyapunov_chaosloss.py`(1.5 s):J-P MATCH(比 2.00・5.09・16.4・64.1 対 2・5・17・65)。閉鎖の理由は (1)〜(3) の字面と 377-A で、値は使わない。
- **共通点(1 行)**:**Γ 形(勾配形)の不等式は Wiener でも第 1 カオスでだけ鋭く、位相つきの UV の消費者では平均のカオスの次数 $\approx\lambda/2$ を払う —— 点ごとの曲率を外しても、出力の型が消費者に合わない;(LLC) はそもそも分散でない。F159・F174・F175・F183 と同じ段(正値性・Itô の等長の外の入力)を、出力の型の側から特定。**
- **R9**:閉じたのは方式。双極子では消費者に位相が無く($e^{ik\cdot b}\to1$、$\ell_f$ は第 1 カオス)損失は 1、Hargé/BL が当たる(F99 の側)—— 障害は反跳の位相に局在し消滅していない。
- **射程(T60)**:禁じるのは「Lyapunov 関数・局所 Poincaré・積分可能な曲率・殻ごとの積など、出力が Γ 形の Poincaré・LSI である方式で (α)・(LLC)・(LL-low$_{2/3}^+$) を出す」形の発注。止めないもの:Γ 形でない分散の評価(∥ 成分での条件づけ・反射対称・Itô の等長を使う型;平面波では横の増分の条件付き共分散の作用素ノルムに落ちる —— 稿 §2.4)、ブロックの再標本化の Dirichlet 形式(損失は出ないが間隙は Dobrushin–Shlosman の型);双極子・Nelson 型の梯子への適用。
- **再開条件**:(1) 局在モードの $\ell_f$ を、位相の微分を取らずに(条件づけ・等長で)$\mathcal N$ の下の線形の量の評価に落とす表示が出たとき;(2) PF の重みの構成的な正値分解(F169 再開条件 (1))。
- **F183 の再開条件 (1) への注記**:「分散の項の粗い速度の裾を含む一様な上界」は、裾の側は Lyapunov の drift で処理でき(本稿 §3.1)、満たしても出力が Γ 形なら全列に届かない(本稿 §2.3)—— 再開条件としては (1) の「Γ 形でない」限定を付けて読む。

## F186(E05、全列(行 E1-H の内側)の供給 (α) の対角部分と Schur の道の非対角の減衰(371 §7・377 §8.1 (A2))を、**経路の増分の反集中**(反跳つき Gibbs 測度 $\mathcal N$ の下での $\mathbb E_{\mathcal N}e^{iq\cdot(b_s-b_r)}$ の尺度 $1/\Lambda$ での減衰)で出す方式 —— (a) 条件付きの Gauss・Girsanov・Cameron–Martin、(b) Donsker–Varadhan・局所時間の指数モーメント、(c) Hilbert 側の表示。2026-10-20、w_E05_380_anticonc_path = 書き下しの型、稿 `380_全列17_経路の増分の反集中_閉じる確率_2026-10-20.md` §1〜§3、成算 S188)
- **閉じたもの**:方式((α)・(N109)・(N110) の真偽は閉じない)。
- **理由(観察 + 在庫の勘定 + 値)**:(1) 消費者の字面(§1):要るのは時刻差について Laplace 変換した特性関数で、P=0 ファイバーの FK の読みで $\langle\psi_0,(H(-q)-E_0+s)^{-1}\psi_0\rangle=g(1+\mu(|q|,s))$($s=\omega+\omega'$)= **E05-P57 の $\mu$**;殻に広がるモードの対角部分は $G_\Lambda$((N109) の量)と同じ桁 —— (c) は (N109)/(N110) の衣替え(F182 と同じ型の同一視)。違いは許容が $o(\sqrt{N/\alpha})\lesssim\lambda^{5/14}$ に緩むことだけ。(2) 緩めた (N109$_w$) にも在庫の型は届かない:在庫 5/7(P59 2.)、$\mathcal K$ 経由は F82 4. の公式に $a=5/3$(P158)・$b=12/7$(P167)で $\mathcal K/(m\Lambda)\ge c\lambda^{9/14}$、$\pi$ の分布型 4/7、LP 1。(3) (a)・(b):絶対連続性に基づく移送(DV・Pinsker・Hölder・Föllmer の漂移)は閉じる事象の相対精度($P_W\sim\lambda^{-3/2}$)を運ぶのに窓 $1/\Lambda$ のエントロピー $\lesssim\lambda^{-8/7}$ を要るが、在庫は全時間の $tE_0$ だけで窓に局在せず、双極子(厳密に Gauss、標的の積分版の比は 1.002〜1.28 で値は真の向き)でも窓の KL は λ とともに発散し DV の出力 / $P_W$ は局所冪 ≈ 2(C0 `560_`)【値、T88】;厳密な条件付き Gauss は双極子にだけあり、PF では $b\cdot\hat q$ が全方向のモードの位相に入る;Cameron–Martin の複素のずらしは重みの解析接続で $e^{O(\lambda)}$ を拾う。(4) 親の推論 2(局所の量なら (N110) より弱い)は否定:(N109)/(N110) は元から $s=\Lambda$ の量で、低帯の重みがそのまま時間 $1/\Lambda$ の閉じる確率。推論 1 は点ごとには偽(双極子で指数の比が O(1) ずれる)、時間積分では値で正しい。
- **共通点(1 行)**:**経路の反集中は (N109) の量の言い換えで、経路の測度の道具は窓のエントロピーを払うので相対精度 $\lambda^{-1}$ の小ささを運べない —— 全列の (α) 経由の道は (N109$_w$)(冪 $\lt5/14$)と (A1) 反跳の分母の下界の 2 つに帰着し、どちらも 2026-09 以来の閉じた段。**
- **射程(T60)**:禁じるのは「経路の増分の特性関数・閉じる確率・局所時間を、Wiener との絶対連続性の比較(エントロピー・DV・Pinsker・Hölder・Girsanov)で λ に一様に押さえて (α) に入れる」形の発注と、「Hilbert 側の表示に移せば (N110) より弱い局所の量になる」という読み。止めないもの:(N109)・(N109$_w$) そのものへの $\mathcal K$ を通さない入口(F82 の禁止しないもの);(A1) の反跳の分母の下界;(LLC) の道。
- **再開条件**:(1) 窓 $1/\Lambda$ の周辺分布の相対エントロピー(または $L^p$ の密度比、$p\gt14/5$)が $\lambda^{-8/7}$ の桁(Hölder なら一様)で在庫に載ったとき;(2) (N109) の在庫の冪が 5/14 未満に下がったとき(E05-P59 2. の改良)。
- **再開条件への注(2026-10-20 親、稿 384 §1・385 観察 385-B)**:(1) の字面は過剰 —— 消費者(定理 381-1 の証明)が要るのは**積分形** $\int_{1/E_0}^{1/\Lambda}B\,d\tau\lesssim m\Lambda\lambda^{5/14}$(各点なら Wiener からの一様な損 $\le\lambda^{1/2}$ か、短い端からの減衰指数 $\gamma\ge3/10$)だけ(384 §1)。字面の各点の形 $B(\tau)\lesssim(m/\tau)^{3/2}\lambda^{o(1)}$ は (N109$_w$) が成り立つ双極子で偽(385-B、384 C0 564:窓で台地)。必要条件として短時間の有効質量 $h_*=h_{\rm eff}(1/\Lambda)\lesssim\lambda^{4/7}$(補題 385-A、candidate)。台帳の行は改変しない。

## F187(E05、全列(行 E1-H の内側)の供給 (LLC) 族〔(LLC)・(LLC-av)・(LLC-Σ)、E05-P175・P183〕を、(α) を経由しない**直接の道**(3 次キュムラントの率 = 殻密度 $\rho$ の負の部分の上界)で出す 5 族 —— (K1) Feynman–Hellmann の 3 階($e(\theta,m)=\inf\sigma(K_m-\theta V_z)$ の結合凹性、$\rho=-m\partial_m\chi=m\partial_P^2\langle H_f\rangle_P$)、(K2) 相関不等式(GKS・Ginibre・FKG・GHS・Lebowitz・EMN)で 3 次キュムラントの符号、(K3) 1 ループの $\rho^{(2)}=\frac{8\alpha}{3\pi}\frac\lambda{\lambda+2}\gt0$ + 非摂動の補正の上界、(K4) 殻の振幅についての $m_{\rm eff}$ の凹性(凹 + 下に有界 ⟹ 単調)、(K5) 値の外挿。2026-10-20、w_E05_382_llc_direct = 書き下しの型、稿 `382_全列19_LLCの直接の道_3次キュムラントの候補表_2026-10-20.md` §2〜§5、成算 S190)
- **閉じたもの**:**方式**((LLC)・(COV)・(E1) 全列の真偽ではない;(LLC)$_{C=0}$ は値で真の向き)。
- **理由 (K1)(雑な計算 2 本 + C0)**:(1) 結合凹性は $\theta=0$ で 3 階の符号を与えず、$\theta\ne0$ の Hessian の CS で大きさを押さえると $m\lvert\partial_m\chi\rvert\lesssim2\sqrt{F\lambda}/h$ —— (LLC) には $h\gtrsim\sqrt{F\lambda}\ln\lambda\ge c\lambda^{5/6}\ln\lambda$ が入力に要る(循環、値で偽の向き)。(2) 固定のスペクトル径数の正の形 $\lVert H_f^{1/2}RV_z\psi_0\rVert^2$ と基準の移動 $\langle H_f\rangle\lVert RV_z\psi_0\rVert^2$ は 2 ループ以上でどちらも赤外で対数発散($\lVert RV_z\psi_0\rVert^2\propto e^2f^2\int dk/k$)し、有限な差は符号を持たない;交差項は符号不定の 3 点関数 —— F121 (iv) の相殺と同じ型。(3) C0((研究ノート: `562_w_E05_382_llc_direct_toyFH.py`)):同じ代数の型(結合凹性・FH・$B\ge0$・Fock の $V=P_f+gA$)の反跳つき 1 次元玩具で、打切りの収束域の中で $\chi(m)$ が非単調(λ ≳ 1.3 で $\rho\lt0$;双極子の対照は単調)—— 型だけの証明は無い。単調性は鋭い切断の族(軟らかいモードを全て含む)に固有で、殻の応答(3 点関数)を通してしか入らない。
- **理由 (K2)(原典照合 + C0)**:Ginibre 1970 Prop. 2・3 は $-h\in Q(S)$(正係数)を要る;PF の $-h=-\frac{e^2}2q$ は $S$ = 増分でも $\lbrace e^{ik\cdot b}\rbrace$ でも全ての対で負係数(双極子の核は正、反跳の部分は回転子の強磁性と逆符号)で、3 点でフラストレーション(± のゲージで強磁性にできない)。$h\ge1$ の物理(速度の負の自己相関)そのものが反強磁性の向き。双極子の (COV) は Wick の $2\mathrm{tr}(ACBC)\ge0$ で GKS の機構ではない。C0(`562_w_E05_382_llc_direct_frustration.py`):離散双極子の共分散の非対角は全 16 セルで全て負、全てフラストレーション。
- **理由 (K3)**:$\rho=\rho^{(2)}R$、(LLC) ⟸ $R\ge-3\pi C/(8\alpha\ln\lambda)$ = 応答比(3 点関数)の下界 —— F162 (3)・F170 (ii) の段への移し;主項の支配は $\lambda\le e^{c/\alpha}$ の窓だけ。
- **理由 (K4)**:初等の事実(凹 + 下に有界 ⟹ 非減少)は立つが、入力の凹性が値で偽の向き:334 の応答比 $\partial_sh=f_{\rm base}^{p-2}\partial_sh\rvert_W$、$p\approx1.5\lt2$ は超モジュラ(凸)の向き;主導対数の再和 $h=(1+(p-1)c\alpha\ln\lambda)^{1/(p-1)}$ は α について凸。変種「$h$ が λ について凹」は値と整合するが供給の機構が無い(Q3 の上側の道具なし、FR-G3-9)。
- **値の裏づけ(【T88】)**:`562_w_E05_382_llc_direct_values350.py`:350 の梯子(λ=8〜32、α=1.33)で全段 $\rho\gt0$、$R=\rho/\rho^{(2)}\approx f^{p}$、$p\in[1.17,1.73]$(T=3 で 1.30〜1.44)。閉鎖の理由は字面と雑な計算で、値は向きの裏づけだけ。
- **共通点(1 行)**:**直接の道の型(正値性・凸性・FH・相関不等式・摂動)はどれも 2 階の量か強磁性の正値性を運ぶだけで、(LLC) が要る「反跳つき Gibbs 測度の連結 3 点関数(応答比 $R$)の下界」には、PF の反跳の位相と $h\ge1$ の反強磁性の向きのために届かない —— F159・F162・F170・F174 と同じ段。**
- **R9**:閉じたのは方式。K1 の段は双極子で空(Gauss で $h$ は加法的、玩具でも単調);K2 の段は双極子でも立つ(反強磁性は双極子の核の正値性から来る)が、双極子の符号は Wick で別に出る —— 障害は「非 Gauss の 3 点関数の符号を出す型が無い」ことに局在し、消滅していない。
- **射程(T60)**:禁じるのは「$e(\theta,m)$ の結合凹性・$m$ の FH・固定の $z$ の正の形で $\rho$ の符号・大きさを出す」「GKS・FKG・GHS 族を電子の座標を含む表示(増分・平面波の位相)で当てる」「1 ループ + 補正の上界」「$m_{\rm eff}$ の結合についての凹性」の形の発注。止めないもの:値の梯子(379 と合わせた $p(\lambda)$ の表);電子の座標を含まない表示(場の側)での正値性の探索;(N109$_w$)(稿 381)。
- **再開条件**:(1) PF の重みに強磁性(正係数)の表示を与える変数の選び方(電子の座標を積分した場の側の表示など)が見つかったとき;(2) (RE-248) 型の、赤外で有限な正の形の殻応答の恒等式($T_3^{\rm dr}=\langle\xi,K\xi\rangle$、$K\ge0$、赤外の ∞−∞ を含まない)が出たとき;(3) 値で $p(\lambda)$ が 2 を超えるか 1 を下回る段が見つかったとき(K4 の向き・K5 の外挿の見直し)。

## F188(E05、全列(行 E1-H の内側)の供給 (α) の対角部分が帰着した **(N109$_w$)**((N109) の許容を $O(1)$ から $o(\sqrt{\alpha N})\lesssim\lambda^{5/14}$ に緩めた形、380 §2)への新しい十分条件を、設計のやり直し(テンプレート C)の候補表 —— K1 2 次形式のまま押さえる・Schur(親の推論 1:在庫 5/7 は CS の損)/ K2 Mourre・正の交換子(光子の拡大の生成子)/ K3 Hardy・不確定性の局所評価($P_f$・$\pi$ の分布)/ K4 光子数の高い冪のモーメント(F85 の非循環版)/ K5 ファイバーの $q$ についての凸性・単調性 / K6 格子・切断の数値(類 C)/ K7 反磁性 + $q$ 積分(熱核の対角)—— で出す方式。2026-10-20、hard_E05_n110_redesign_72 = 難所の型、稿 `381_全列18_N110の設計のやり直し_2026-10-20.md` §1〜§3、成算 S189)
- **閉じたもの**:**方式**(7 本;(N109$_w$)・(N109)・(α)・全列の真偽ではない)。
- **理由(字面 + 厳密 + 値)**:(1) **消費者の照合**(§1.2):要るのは積分版 $G_\Lambda/(m\Lambda)\lesssim\lambda^{5/14}$ だけで、底の層の重みでは殻平均 $\overline{\nu_q([0,\Lambda])}\lesssim\lambda^{-9/14}$((N109) は $\lambda^{-1}$、在庫 5/7 は $\lambda^{-2/7}$);sup((N110))は要らない(双極子で sup は破れ積分版は成る、560)。(2) **K1**:在庫 5/7 の損は $\frac1{s+x}\to\frac1s$ の切り落とし(P66 3. の Jensen の上端)で Cauchy–Schwarz ではなく、$|q|=2\Lambda$ で下端との比は $1/\lambda$;戻すには低帯の重みの位置(P60 3.)が要る = F78 (a) の段。C0 561 J1:双極子で上端は冪 $\ge1$ を失う【値】。(3) **K2**:低帯で $H_f\gtrsim\Lambda$ でも交換子の交差項 $-\frac e{2m}(\pi+q)\cdot A(0)$ は符号不定;LAP の出力は状態密度の一様な上界で特定のベクトルの重みの小ささを出さない(F182 (3) の段)。(4) **K3**:$L_q$ は $(\pi+q)^2$ の射影と可換でなく $\nu_q([0,T])\le\mathrm{Prob}_{\psi_0}(|\pi+q|^2\lt4mT)$ は立たない;立っても F79 の鎖で $\mathcal K^{3/2}/\Lambda\ge m\Lambda\lambda^{13/28}$(F82 の下界)$\gt\lambda^{5/14}$。(5) **K4**:光子数のモーメントは光子の運動量の向きを見ず低帯への翻訳が無い(F85 の段)。(6) **K5**:$q\mapsto\langle\psi_0,e^{-\tau X_q}\psi_0\rangle$ は $\Delta b_\tau$ の特性関数で、$q$ 積分は密度 $p^{\mathcal N}_\tau(0)$ = 反集中(F186 の段)。(7) **K6**:値は真の向き(双極子 1.0〜1.3、2 光子 $(\ln\lambda)^2$)—— 類 C でなく類 B。(8) **K7(唯一の新しい段)**:補題 381-A・定理 381-1 で $G_\Lambda/(m\Lambda)\le C_1+C_2F^{3/2}\lambda^{-1/2}\le C\lambda^{4/7}$(P167;在庫 5/7 の改善、candidate)だが、$F\ge c\alpha^{1/3}\lambda^{2/3}$(P158)で尾の項は $\ge\lambda^{1/2}\gt\lambda^{5/14}$ —— 経路の床(T90)。損の段 = $\tau\in[1/E_0,1/\Lambda]$ で $q$ 平均の閉じる関数が $e^{-\tau E_0}$ を払わずに $\tau^{-3/2}$ で減ること(時間窓の正規化の局所性)= F186 (3)・371 §7 の閉じる確率と同じ対象。
- **共通点(1 行)**:**低帯の「重み」を重みを見ない入力(モーメント・$\mathcal K$・状態密度・光子数・密度比・反磁性の熱核)で押さえる限り、同じ入力を満たす玩具(Landau・双極子の点ごと)で (N110) が破れ、積分版でも $E_0$ の分の重みの時間局所性(窓の正規化)が無いので冪 $\ge1/2$ で止まる;F78〜F86・F182・F186 の段の積分版での再現。**
- **R9**:閉じたのは方式。双極子では (N109$_w$) は値で真(560)—— 障害は PF の反跳の位相に局在し消滅していない。
- **射程(T60)**:禁じるのは「(N109$_w$) を K1〜K7 の型で λ に一様に出す」形の発注、および「在庫 5/7 は CS の損で平方根で戻る」という読み。止めないもの:定理 381-1 の S2 と在庫値の更新(冪 4/7);$\tau\in[1/E_0,1/\Lambda]$ の閉じる関数の時間局所の正規化(F186 再開条件と同じ);(LLC) の道;(A1) 反跳の分母の下界。
- **再開条件**:(1) 時間窓 $[u,u+\tau]$($1/E_0\le\tau\le1/\Lambda$)の $\mathcal N$ の周辺分布について、$e^{\tau E_0}$ を払わない閉じる確率の上界($B(\tau)\lesssim(m/\tau)^{3/2}\lambda^{o(1)}$)が λ に一様に出たとき;(2) (N109) の在庫の冪が 5/14 未満に下がったとき(380 と同じ)。
- **再開条件への注(2026-10-20 親、稿 384 §1・385 観察 385-B)**:(1) の字面は過剰 —— 消費者(定理 381-1 の証明)が要るのは**積分形** $\int_{1/E_0}^{1/\Lambda}B\,d\tau\lesssim m\Lambda\lambda^{5/14}$(各点なら Wiener からの一様な損 $\le\lambda^{1/2}$ か、短い端からの減衰指数 $\gamma\ge3/10$)だけ(384 §1)。字面の各点の形 $B(\tau)\lesssim(m/\tau)^{3/2}\lambda^{o(1)}$ は (N109$_w$) が成り立つ双極子で偽(385-B、384 C0 564:窓で台地)。必要条件として短時間の有効質量 $h_*=h_{\rm eff}(1/\Lambda)\lesssim\lambda^{4/7}$(補題 385-A、candidate)。台帳の行は改変しない。

## F189(E05、全列(行 E1-H の内側)を E05-P170 から**切断の窓の比較** $`h(\lambda')\ge c\,h(\lambda)`$(または $f(\lambda')\le Cf(\lambda)+o(1)$)で上げる方式 —— 窓の形の確定(対数窓 $[\lambda,\lambda^{1+\epsilon}]$ と A-302-3 の閾値ごとの有界比の窓)、比較の型と (LLC) 族の照合、供給の候補 3 本(c1 P118 の変分の試行を切断 Λ の基底状態から作る移送、c2 作用素不等式 $H_u\le H_{Ru}\le RH_u$ と $\Phi(u,v)=E_u(P)-uP^2/2$ の同時凹性・Lieb–Loss の質量のくりこみの比較、c3 $h_{\rm sr}\le h_{\rm ls}$〔P198〕の向きの組み合わせ)。2026-10-20、w_E05_388_cutoff_compare = 書き下しの型、稿 `388_全列24_切断の倍率窓の比較_2026-10-20.md` §1〜§3、成算 S195)
- **閉じたもの**:**方式**((E1) 全列・(LLC)・窓の比較の真偽ではない;比較の型は値で真の向き)。
- **理由(字面 + 初等 + 原典)**:(1) **加法の版は R9**:窓の上で一様な $o(1)$ つきの比較は標的 $f\to0$ から自明に従い、P170 と組んで標的を出す —— 窓が対数窓(334 §1.2 の (ULLC))でも有界比((W$_K$)、276-B の型)でも P170 の下で (E1) と同値で、構造的な内容を持たない。(2) **乗法の版は (LLC) の真の弱化でない**:$\lambda\partial_\lambda\ln h=h\rho$ で、対数窓の比較は粗い (MLLC)〔$\rho\ge-Cf/\ln\lambda$、(LLC) の $f$ 倍の強さ;$f\le1$ で (MLLC) ⟹ (LLC)〕、有界比の比較(系 276-C (b))は (POLY$_\gamma$)〔$\rho_-\le\gamma f$〕—— 許す上昇が $f$ に比例し、$f\to0$ の領域で (LLC) より強い供給を要る((POLY) が軽いのは $h\lesssim\gamma\ln\lambda$ の領域だけで、入力にできない)。親の推論 1「乗法は $f\to0$ で弱い可能性」は向きが逆。(3) **c1**:試行は $\psi_0'$ との重なりを要り、$\psi_0\otimes\Omega_{\rm sh}$ の移送の損失は殻の真空確率(P116・P129)で $O(1)$、さらに $f(\lambda)$ の下界($h$ の上側の道具、FR-G3-9)が要る —— 334-C の Hamiltonian 側の段。**c2**:作用素不等式はエネルギーのずれ $(R-1)E_0$ が曲率を飲み込む;同時凹性は $\partial_u^2E_u(0)\lt0$(大きさ $u^{-2}\langle T\rangle$、A-246-3 (2)(3))の下で $v\to0$ の曲率の $u$ 依存に制約を与えない;Lieb–Loss 2002 の質量は束縛エネルギーの質量で、曲率の質量について「cannot prove」と明記(原典 p.3)、Hainzl–Seiringer 2002 は固定の Λ・小さい α の 1 ループ。**c3**:P198 は同じ切断の中の比較で、切断を跨ぐ組み合わせは右辺の $h$ の上界(FR-G3-9)を要る。
- **値の裏づけ(【T88】)**:(研究ノート: `568_w_E05_388_cutoff_compare_ratio.py`):350・379(部分)の 27 対で $f(\lambda')/f(\lambda)\gt1$ が 2σ を超える対は 0(唯一の上向き 1.19 ± 0.21 は λ=64、n=2 のセル);1 ループの倍尺度の比 0.81〜0.95。閉鎖の理由は字面と初等の言い換えで、値は向きの裏づけだけ。
- **到達点(閉じた方式の副産物)**:観察 388-A —— P170 の $S'$ の出所 A-302-3 の字面で、閾値ごとの良い点は窓 $[\lambda'/(8K_\varepsilon),\lambda']$(乗法的に有界)にある(334-A の $\lambda^{o(1)}$ は対数密度の定義だけからの読み);ゆえに系 276-C (b) ∧ P170 が全列を出すかは $K_\varepsilon$ と 254-A の保証値 $\Phi(\eta)$ の率の両立に依る(334 §1.2 の「足りない」の精密化;(b) の供給は (LLC) より軽くないので台帳は動かない)。
- **共通点(1 行)**:**窓の比較は、加法なら標的の言い換え(R9)、乗法なら「$f$ に相対な負の殻密度の上界」で、どちらも供給の段(反跳つき Gibbs 測度の連結 3 点関数の時間減衰、334-C)を動かさない;切断を跨ぐ変分・作用素の比較はエネルギーの尺度のずれか $h$ の上側の道具の不在で止まる —— F159・F162・F167・F170・F187 と同じ段。**
- **R9**:閉じたのは方式。段は双極子で空でない(双極子では $h$ が αλ の単調な関数で比較は真、供給は Gauss で別に出る);障害は消滅していない。
- **射程(T60)**:禁じるのは「窓の比較(加法・乗法、対数窓・有界比)を到達点に置き換えて供給を軽くする」「P118 の試行を別の切断の基底状態から移送して $f$ の比を保つ」「ファイバーのエネルギーの作用素不等式・同時凹性で切断を跨ぐ曲率の比較を出す」形の発注。止めないもの:A-302-3 の $K_\varepsilon$ と 254-A の $\Phi(\eta)$ の率の照合(消費者の側の記録、類 A;〔済 2026-10-20:補題 387-T (B)、E05-P201 —— $c\gt2^{-1/7}$、監査 `389_`〕);(LLC) 族の供給の本体(3 点関数);値の梯子(379)。
- **再開条件**:(1) $h$ の上側の道具(切断 Λ で $h$ を上から押さえる型、FR-G3-9)が出たとき;(2) 殻 $[\Lambda,\Lambda']$ の結合を足したときの $f$ の相対変化を、エネルギーの尺度でなく曲率の尺度で押さえる比較の型(例:$\psi_0'$ と $\psi_0\otimes$(殻の着衣)の重なりの下界)が出たとき;(3) 値で $f(\lambda')/f(\lambda)\gt1$ が有意に出たとき(類 C の見直し)。

## F190(E05、全列(行 E1-H の内側)の 3 入口 ① (N109$_w$)・② 閉じる関数 $B(\tau)$ の窓 $[1/E_0,1/\Lambda]$ の $e^{\tau E_0}$ を払わない上界・③ (LLC) を、**2015〜2026 年の数理物理・確率論の道具**で出す方式 —— (a) ポーラロンの有効質量の証明(Bazaes–Mukherjee–Sellke–Varadhan 2023 の Gauss 表示 + 点過程の FKG、Brooks 2024・Brooks–Seiringer 2022 の擬似ブースト、Mukherjee–Varadhan・Betz–Polzer・Polzer の点過程・再生の表示、Dybalski–Spohn)、(b) 反集中・小球確率(Carbery–Wright、Nazarov–Sodin–Volberg、Littlewood–Offord の連続版・Rudelson–Vershynin、Li–Shao・Anderson・GCI、**Wegner の推定・スペクトル平均**)、(c) Nelson・PF の汎関数積分(**Gubinelli–Hiroshima–Lőrinczi 2014 の対角の相殺**、Matte–Møller、Hinrichs–Matte、Betz–Polzer の FK)、(d) 厳密な RG(Bach–Fröhlich–Sigal・Chen–Fröhlich–Pizzo・Hasler–Herbst、Bauerschmidt–Brydges–Slade)。2026-10-20、w_E05_386_tooljourney = 書き下しの型、稿 `386_全列22_道具探しの旅_2015年以降の数理物理と確率論_2026-10-20.md` §2〜§5、成算 S193)
- **閉じたもの**:**方式**(照合した 4 族 18 行の道具の移送)。①②③・全列の真偽ではない。
- **理由**:(a) BMSV(2307.13058v3 抄録 "Gaussian representation of the Polaron measure"、§3.3 の FKG)・MV・BP・Polzer は正値 Gauss 混合(F169 (M1)(M2) の段)と FKG(PF は全ての対で負の結合、382 K2);Brooks の下界は雲の分位点で切った重心の擬似ブースト((1.21))を試行に入れる型で、PF には局在した雲が無い(F141 (b))—— E05 の擬似ブースト系(F105〜F107)・P120 と同じ型。(b) Carbery–Wright・NSV は対数凹(F183 の $\inf\mathrm{Hess}V=-\infty$ で落ちる)、Littlewood–Offord・Rudelson–Vershynin は独立和、Li–Shao・Anderson・GCI は小球確率の下界(集中の向き);Wegner・スペクトル平均は正の微分 $\hat e\cdot(q+\pi)/m\ge c\,s/m$ があれば ① の的 $C/\lambda$ に届く形だが、低帯 $X_q\in[0,\Lambda]$ では $\lvert q+\pi\rvert\lesssim\delta\Lambda$(P117)で微分は小さく符号不定(C0 で負)—— F182 (3)・381 K2 の段。(c) GHL(1304.6662 抄録:対数発散の項を対の相互作用の対角部分として取り出す;本文「uniformly in the paths」の余り)は Nelson の対角が決定的な定数 + 経路に一様な余りになることに依り、PF の対角は $\cos(k\cdot\Delta b)$ で経路に依る($1/\Lambda$ の時間で $k\lvert\Delta b\rvert\sim\sqrt\lambda$)ので一様な余りにならない(F183 の粗い速度の裾);Hölder で指数モーメントに移す型は 323-A の凹性で損の向き。(d) BFS 系は赤外・Λ 固定(F170 (iii)、F171 (a));BBS は余りの評価が殻の連結 3 点関数 = F162 (3)。
- **値の裏づけ(【T88】)**:C0 (研究ノート: `566_w_E05_386_tooljourney_wegner_toy.py`)(1 光子・1 次元の LLP 玩具):低帯の固有ベクトルの $\langle\partial_sH\rangle/(s/m)$ の最小 = −0.021・−0.236・−0.368(λ=8・16・32)—— スペクトル平均の下限は無い。閉鎖の理由は字面で、値は使わない。
- **共通点(1 行)**:**照合した全ての道具は、基準の測度の構造(対数凹・独立・正値 Gauss 混合・実の指数)か、重みの対角の決定的な相殺か、雲の半古典的な局在を前提に置き、PF の反跳の位相がその全てを壊す —— 双極子では全ての道具が入口を自明に満たす(F169・F183・F188 の共通点の文献の側からの再確認)。**
- **R9**:閉じたのは方式。双極子では ①② は真(Gauss)—— 障害は位相に局在し消滅していない。
- **射程(T60)**:禁じるのは「照合した 18 行の道具をそのまま PF の ①②③ に移す」形の発注。止めないもの:Fable 384 の時間局所の正規化(② の本体);Malliavin の密度の上界(385);低帯で正の交換子を持つ新しい生成子の構成;原典未照合の行([要確認])の字面の照合。
- **再開条件**:(1) 非対数凹・位相つきの重みの経路測度で、点ごとの曲率なしに増分の密度の上界を出す一般の定理が文献に現れたとき;(2) 低帯のスペクトル部分空間の上で正の交換子を持つ母数が見つかったとき;(3) 経路に依る対角の相殺項について、閉じた経路と開いた経路の窓の重みの比の比較原理が立ったとき(384 の成果に依る)。

## F191(E05、全列(行 E1-H の内側)の供給を**確率量子化**(Parisi–Wu:反跳つき Gibbs 測度 $\mathcal N$ を不変測度に持つ Langevin 方程式と過程の結合;場の変数の Langevin を含む)で出す方式。2026-10-20、w_E05_387_longshots = 書き下しの型、稿 `387_全列23_可能性の低い未検討事項の成算_2026-10-20.md` §2 (1)、成算 S194)
- **閉じたもの**:方式((α)・(N109$_w$)・(LLC)・全列の真偽ではない)。
- **理由**:同期結合の縮小率は $1+\mathrm{ess}\inf\mathrm{Hess}V$ で PF は $-\infty$(355 C0-(i)・374-A)、反射結合は Eberle の $\kappa(r)$(F183 (c));縮小が出ても出力は Γ 形の Poincaré で 377-A の損失 λ/2(F185);場の変数では不変測度 $K_A\gamma(dA)$ の対数凹性が在庫に無く、在っても BL は $\Pi$ の下界(377 §8.2 型 B)。
- **共通点(1 行)**:**過程の結合は測度の曲率(点ごと)か Γ 形の出力に帰着し、F183・F185 と同じ段。**
- **射程(T60)**:禁じるのは「$\mathcal N$ または場の周辺分布の Langevin の結合・縮小で (α)・(LLC) を出す」発注。止めないもの:数値の標本法としての Langevin(値)。
- **再開条件**:F183・F185 の再開条件と同じ(Γ 形でない、分散の項の一様な上界)。

## F192(E05、全列の供給を **Stein の方法**(Stein 核・交換可能な対・Malliavin–Stein、依存グラフの型)で、(α) の分散と (LLC) の 3 次キュムラントの大きさを Gauss 近似の誤差から押さえる方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (2)・§5 R8、成算 S194)
- **閉じたもの**:方式。
- **理由**:$\mathcal N$ の下の Stein 核の大きさは Poincaré 定数の型(F185);Malliavin–Stein は Wiener の下の滑らかな距離の加法的な誤差で、(α) が要る傾けた測度の相対精度 $\lambda^{-1}$(閉じる事象の Wiener 確率 $\sim\lambda^{-3/2}$)を運べない(F186 (3));(LLC) の側は大きさだけで足りる(補題 387-T (A′))が、3 次キュムラントの示量性($\propto t$)に要る時間の脱相関を Stein の依存構造の型が入力に取る(334-C・F174・F176)。
- **共通点(1 行)**:**Gauss 近似の誤差は加法的で相対精度を運ばず、時間について示量的な評価には脱相関を入力に要る —— F185・F186・334-C の段。**
- **射程(T60)**:禁じるのは「Stein の方法で $\mathcal N$ の下の (α) の分散・(LLC) の 3 次キュムラントを λ に一様に押さえる」発注。止めないもの:数値の制御変量(eff_R1a の Stein 制御変量、値)。
- **再開条件**:連結 3 点関数の時間減衰(334-C)が別の道で在庫に載ったとき(そのときは Stein は不要)。

## F193(E05、全列の供給を**最適輸送**(Caffarelli の縮小定理、Kim–Milman 2012 の熱流の写像、Wiener から $\mathcal N$ への輸送写像の Lipschitz 性)で出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (3)、成算 S194)
- **閉じたもの**:方式。
- **理由(原典照合 + 字面)**:Caffarelli の定理(Kim–Milman 2012 §1 の引用)と Kim–Milman Thm 1.1 はどちらも摂動 $V$ の**凸性**を仮定(原典 arXiv 1002.0373 の字面で確認);PF の $V$ は白色座標で $\mathrm{ess}\inf\mathrm{Hess}V=-\infty$。半対数凹の版も点ごとの曲率(F183 (a)(c))。1-Lipschitz の写像が在っても出力は Γ 形で 377-A の損失(F185)。
- **共通点(1 行)**:**輸送写像の Lipschitz 性は凸性(点ごとの曲率)の言い換えで、出力は Γ 形 —— F183・F185・F175 (iii) と同じ段。**
- **射程(T60)**:禁じるのは「$\mathcal N$(または殻ごとのくりこまれた測度)への輸送写像の Lipschitz 定数で (α)・(LLC) を出す」発注。
- **再開条件**:F183 の再開条件 (1)(Γ 形でない限定つき、F185 の注記)。

## F194(E05、全列の供給 (N109$_w$)・$B(\tau)$ を**超縮小性・Nelson 型の評価**($e^{-tH_f}$ の $L^p\to L^q$ の縮小、Glimm の $N_\tau$ 型の評価)で低帯の重みとして出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (4)、C0 J-H、成算 S194)
- **閉じたもの**:方式。
- **理由**:無質量では $\lVert e^{-t\omega}\rVert=1$ で超縮小なし;殻 $\omega\le\Lambda$ に限っても窓 $\tau\le1/\Lambda$ では $e^{-\tau\omega}\ge e^{-1}$ で指数の改善は λ に依らない有界(C0 J-H、$q_{\max}(p=2)\le1+e^2$)。出力は $N$・$H_f$ の $L^p$ ノルム・モーメントで、光子の運動量の向きを見ない(F188 K4・F85)。
- **共通点(1 行)**:**重みを見ない入力(モーメント・ノルム)で低帯の重みを押さえる型 —— F188 の共通点そのもの。**
- **射程(T60)**:禁じるのは「場の自由半群の超縮小・Nelson/Glimm 型のモーメントで (N109$_w$)・$B(\tau)$ を出す」発注。止めないもの:有質量の光子の模型(赤外の切断)での使用。
- **再開条件**:F188 の再開条件と同じ。

## F195(E05、全列の供給 ② $B(\tau)$ の窓の上界を**富田–竹崎のモジュラー理論・KMS**(相対モジュラー作用素・Araki の相対エントロピー)で重みの比として出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (5)、成算 S194)
- **閉じたもの**:方式。
- **理由**:零温度の基底状態は $B(\mathcal F)$ 上で純粋(忠実でない)—— モジュラー理論は部分環でだけ非自明で、出る不等式は凸性・単調性の型;KMS は β=∞ で空。② に要る窓の周辺の密度比は、可換な経路の環では相対モジュラー作用素 = 密度比の掛け算・相対エントロピー = KL で、制限についての単調性は $S_{\rm win}\le S_{\rm full}\sim tE_0$(窓に局在しない)。
- **共通点(1 行)**:**相対エントロピーの単調性は全時間のエントロピーを窓に運ぶだけ —— F186 (3) の段。**
- **射程(T60)**:禁じるのは「相対モジュラー作用素・相対エントロピーの単調性で窓の閉じる確率を出す」発注。
- **再開条件**:F186 の再開条件 (1)。

## F196(E05、全列の供給 (N109$_w$) と (LL-low$_{2/3}^+$) を**相空間の局在**(Fefferman 型の箱の数え上げ・Lieb–Thirring 型の殻ごとの評価)で出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (6)、成算 S194)
- **閉じたもの**:方式。
- **理由**:殻ごとのエネルギーの下界を足す型は超加法性(P174)で固定点 2/3(323-B、F161 (1));箱に分けた局在の誤差は殻をまたぐ $\pi$ の交差項(F181 (a))。低帯の重みは 1 体の固有値の数え上げでなく、$L_q$ は $(\pi+q)^2$ の射影と可換でない(F188 K3);局在が立っても F79 の鎖で冪 $\ge13/28\gt5/14$。
- **共通点(1 行)**:**相空間の局在は殻ごとの加法性か 1 体の不確定性に帰着 —— F161・F181・F188 K3 の段。**
- **射程(T60)**:禁じるのは「Fefferman・Lieb–Thirring 型の殻ごと・箱ごとの評価で 2/3 を超える下界や低帯の重みの上界を出す」発注。
- **再開条件**:F161・F181 の再開条件。

## F197(E05、全列を**計算機援用の証明**(有限の λ を区間演算、大きい λ を漸近で接続)で出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (7)、成算 S194)
- **閉じたもの**:方式(置き方)。
- **理由**:全列は λ→∞ の主張で、漸近の部分が要るのは $\lambda\ge\lambda_*$ での (A′)(補題 387-T)か (LLC) の陽な定数の版 = 供給の全体(帰着);固定の λ でも $m_{\rm eff}$ の厳密な囲い込みは無い(無限次元・間隙なし);漸近を有限の計算に落とす写像の固定点の構造は無い(作用素 RG は紫外で一様でない、F170 (iii))。
- **共通点(1 行)**:**有限の計算は漸近の主張を運ばず、漸近の部分は元の供給そのもの。**
- **射程(T60)**:禁じるのは「区間演算と漸近の接続で全列を出す」発注。止めないもの:値の梯子(379・350)。
- **再開条件**:尺度について不変な写像の固定点の表示(紫外で Λ に一様な RG)が在庫に載ったとき。

## F198(E05、全列の (LLC) 族を **λ についての解析性・単調性の関数論**(Nevanlinna・Pick 表示、作用素単調関数、扇形の解析性の Cauchy の評価)で出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (8)・§5 R9、C0 J-S、成算 S194)
- **閉じたもの**:方式。
- **理由**:Λ 単位の $\lambda T+H_f$ は λ にアフィンで $F$ は凹(在庫と同じ向き)だが、$1/h$ は λ に依る $\psi_0$ のレゾルベントの形で Pick 構造なし;結合凹性の 3 階は F187 K1;基底状態は連続スペクトルの端で解析性は在庫に無く、仮に扇形 $|\arg\lambda|\lt\theta$ で有界正則でも Cauchy は $|\rho|\le C/\theta$ だけ(C0 J-S:固定幅の帯の正則関数が穴の上で $\approx1$ を取れる、観察 387-S)。単調性は (LLC)$_{C=0}$(F170 (i)・F187 K4)。
- **共通点(1 行)**:**λ の関数論は凹性(2 次の向き)か有界な導関数までしか出さず、3 次の符号・穴の上の小ささに届かない —— F170・F187 の段。**
- **射程(T60)**:禁じるのは「$h$ または $f$ の λ についての Pick 表示・作用素単調性・扇形の解析性で (LLC) 族を出す」発注。
- **再開条件**:$f$ が $\ln\ln\lambda$ の変数で固定幅の帯に有界正則に延びる表示(または $\ln\lambda$ の帯の幅 $\gtrsim\ln\lambda$)が見つかったとき。

## F199(E05、全列を **Tauber 型の定理**(P170 の対数密度 1 + λ の正則性)で出す方式の**供給の側**。2026-10-20、w_E05_387_longshots、稿 `387_` §3、成算 S194)
- **閉じたもの**:方式の供給の側(消費者の側は補題 387-T として成立、PROVED の断片)。
- **理由**:要る正則性は (LLC) から (A′)「$\rho\ge-o(1)$、任意の率」・(A)・(B)「$c\gt2^{-1/7}$」に弱まる(387-T)が、(A′) の供給は 334-C の段(3 次キュムラントの率は時間 $t$ について Cauchy–Schwarz で $\sqrt t$ 足りず、連結 3 点関数の時間減衰が要る)で、λ の率の緩みはこの段に効かない;(B) は 276-C (b) の型で F159 (b) の段。
- **共通点(1 行)**:**消費者の率を緩めても、供給を止める時間の勘定(334-C)は動かない —— F187・F159・F174 の段。**
- **射程(T60)**:禁じるのは「Tauber 型の正則性を (LLC) の代わりの新しい標的として、同じ型の道具(相関不等式・FH・凹性・摂動)で発注する」こと。止めないもの:387-T の S2;値の梯子で $\rho$ の下側の値を読むこと。
- **再開条件**:334-C の連結 3 点関数の時間減衰が λ に一様に在庫に載ったとき(そのときは (A′) で率は不要)。

## F200(E05、全列の供給 ② を**均質化・2 尺度展開**(電子の遅い運動と場の速い運動の分離;向きを逆にした速い電子の平均を含む)で出す方式。2026-10-20、w_E05_387_longshots、稿 `387_` §2 (10)・§5 R10、C0 J-R、成算 S194)
- **閉じたもの**:方式。
- **理由**:殻 $\lvert k\rvert\sim\Lambda$ で反跳/光子のエネルギー比は $\lambda/2\to\infty$(C0 J-R)—— 紫外では電子が速く、仮定の向きが逆;電子が遅いのは $\lvert k\rvert\ll2m$ の軟らかい層(双極子・1 ループの対数)だけ。逆向きの 2 尺度は Wiener で平均した核(1 次の閉包)を与え、補正子 = 尺度 $1/\Lambda$ の閉じる確率 $B(\tau)$(F186・F188 の再開条件 (1))。
- **共通点(1 行)**:**2 尺度の補正子は閉じる確率そのもの —— F186・F188 の段。**
- **射程(T60)**:禁じるのは「電子と場の時間尺度の分離(どちらの向きでも)で ② を出す」発注。止めないもの:軟らかい層の均質化(双極子の側、全列に効かない)。
- **再開条件**:F188 の再開条件 (1)。

## F201(E05、全列(行 E1-H の内側)の供給 (α) の対角部分 —— 定理 381-1(E05-P200)の尾の項の損の段 = 時間窓 $[1/E_0,1/\Lambda]$ での閉じる関数 $B(\tau)=\int\chi(q)\langle\psi_0,e^{-\tau X_q}\psi_0\rangle d^3q$ の $e^{\tau E_0}$ を払わない λ に一様な上界(F186・F188 の再開条件 (1))を、(a) 基底状態の局所化(分散関係 $\mathcal E(q)=E(q)-E_0$ の下界)、(b) Duhamel・半群の比較(窓の中の相互作用の回数)、(c) 時間局所の Gibbs 測度の比較(窓の周辺分布の Wiener との相対エントロピー)、(d) 値(双極子)で出す方式。2026-10-20、hard_E05_window_72 = 難所の型、稿 `384_全列20_閉じる関数の時間局所の正規化_2026-10-20.md` §1〜§3、成算 S191)
- **閉じたもの**:方式((N109$_w$)・(α)・全列の真偽は閉じない)。
- **理由(字面 + 厳密 + 値)**:(1) **消費者の照合**(§1.1):定理 381-1 の証明で要るのは積分形 $\int_{1/E_0}^{1/\Lambda}B\,d\tau\lesssim m\Lambda\lambda^{5/14}$ だけで、各点の形では「Wiener からの一様な損 $\le\lambda^{1/2}$」または「短い端の在庫 $B(1/E_0)\le eC_\chi(mE_0/2\pi)^{3/2}$(381-A)からの減衰指数 $\gamma\ge3/10$」で足りる(字面の $\lambda^{o(1)}$ は要らない);スペクトル側では殻平均 $\overline{\nu_q([0,T])}\lesssim(F/\lambda)^{3/2}(T/E_0)^\gamma$($T\in[\Lambda,E_0]$)= 低帯の重みの $T$ についての Hölder 型の減り。観察 384-1(Jensen):$B(\tau)\ge(2\pi m/\tau)^{3/2}(1-o(1))$ は常に成る(下は閉じている、上が問題)。(2) **(a)**:E05-F20・366-A の天井 $\mathcal E(q)\le|q|\le2\Lambda$ で、窓 $\tau\le1/\Lambda$ では $e^{-\tau\mathcal E(q)}\ge e^{-2}$ on $|q|\le2\Lambda$ —— 重みを見ない評価は自明な $36\pi\Lambda^3$ と定数倍しか違わず、窓の積分 $\gtrsim m\Lambda\lambda$ で許容に $\lambda^{9/14}$ 届かない(厳密に閉;F78 (a)・E05-P57 射程「分散では床を消せない」の段)。(3) **(b)**:相互作用の時間尺度は反磁性項の真空の値 $O(\alpha\lambda\Lambda)$ の逆数で、窓の短い端でも相互作用の回数は $\alpha\lambda/F\ge c\alpha\lambda^{2/7}\gg1$;比較作用素 $H'$ の 0 次は Jensen で $e^{\tau(E_0-\langle H'(0)\rangle_0)}$ を失い、Wiener の率に収まるには $\psi_0$ がほぼ $H'$ の基底状態 = 循環(F84・F80 (2) の段)。(4) **(c)**:Gibbs の変分恒等式 $H(\mathcal N_t|W_t)=tE_0-\mathbb E_{\mathcal N}\Phi$ で窓の KL は $\sim c\tau E_0\ge c$、最弱の形でも DV は $H\lesssim\lambda^{-1}\ln\lambda$ を要る;双極子では KL が発散しても密度の損は有限で KL は粗すぎる物差し(F186 (3) と同一の段)。(5) **(d)・C0 564**(双極子、値【T88】):増分の分散 $v(t)$ が $t\in[\kappa^{-1/2},\kappa^{1/2}]$ で $t$ に依らない(台地)ため、窓で $B^{\rm dip}\approx(mE_0^{\rm dip})^{3/2}$、損 $(t/v)^{3/2}$ の最大の局所冪 0.76(→ $\kappa^{3/4}$)、減衰指数 $\gamma\to0$ —— **字面の標的は双極子で偽**;積分形の窓の寄与の局所冪 0.23〜0.25(→ 1/4 $\lt$ 5/14)—— **最弱の形は双極子で真**。
- **共通点(1 行)**:**閉じた経路(窓の中で $b_\tau\approx b_0$)の Euclid の振幅が開いた経路と同じ率 $e^{-\tau E_0}$ で減ることは、双極子では偽(全モードが増分に直接の二次の罰を課し閉じる経路が得をする)で、PF で真になるとすれば硬いモード $|k|\gtrsim\sqrt{m/\tau}$ の反跳 $e^{ik\cdot b}$ が閉じる/開くを区別しないことによる —— その分離は F78〜F86・F182・F186・F188 の段(反跳の位相)そのもの;重みを見ない入力(分散関係・比較半群の 0 次)と絶対連続性の物差し(KL・$L^p$)では届かない。**
- **R9**:閉じたのは方式。字面の標的は双極子で偽、PF では未決;最弱の形は双極子で真。障害は PF の反跳の位相に局在し消滅していない。
- **射程(T60)**:禁じるのは「$B(\tau)$ の窓の上界を分散関係の下界・比較半群の展開・窓の相対エントロピー(KL・$L^p$ の密度比)で λ に一様に出す」形の発注、および「双極子の積分版の比 1.0〜1.3 を (N109$_w$) が値で真である証拠に使う」読み(比は双極子の $F'=O(\sqrt{\alpha\lambda})$ が小さいための見かけ;窓の寄与は $\alpha^{3/4}\lambda^{1/4}$)。止めないもの:**類 C の値の判定「PF の窓の台地」**(§3.3:PF の $B(\tau)$ の窓の減衰指数 $\gamma$;$\gamma\lt\gamma_{\rm crit}(\theta)=1-\frac{5/14+(1-\theta)/2}\theta$($F=\lambda^\theta$;θ=5/7 で 3/10、θ=2/3 で 3/14)か窓の積分の局所冪 $\gt5/14$ が 2 段で安定なら (α) 経由の道は値で偽 —— 定理 381-1 の尾の項 $F^{3/2}\lambda^{-1/2}\ge\lambda^{1/2}$ が鋭い;監査 391 §5);定理 381-1 の S2;(LLC) の道;(A1) 反跳の分母の下界。
- **再開条件**:(1) 最弱の形で:$\int_{1/E_0}^{1/\Lambda}B\,d\tau\lesssim m\Lambda\lambda^{5/14}$(⟸ 一様な損 $\le\lambda^{1/2}$、または減衰指数 $\gamma\ge3/10$;殻平均 $\overline{\nu_q([0,T])}\lesssim(F/\lambda)^{3/2}(T/E_0)^{\gamma}$)が λ に一様に在庫に載ったとき;(2) 硬いモード $|k|\gtrsim\sqrt{m/\tau}$ の反跳による「閉じる/開く」の非区別を、軟らかいモードと分離して評価する型(F78〜F86 の再開条件「$\mathcal K$ を通さない入口」と同じ)が出たとき;(3) PF の窓の台地の値の判定が $\gamma\ge0.3$ で安定したとき(標的が値で真と確定、類 B に戻す)。
- **処方(親へ、F186・F188 の再開条件 (1) の字面の緩和)**:F186 再開条件 (1)「窓 $1/\Lambda$ の周辺分布の相対エントロピー … $\lambda^{-8/7}$ の桁」と F188 再開条件 (1)「$B(\tau)\lesssim(m/\tau)^{3/2}\lambda^{o(1)}$ が λ に一様に出たとき」に、本行の再開条件 (1)(積分形・一様な損 $\lambda^{1/2}$・$\gamma\ge3/10$)を「最弱の形(384 §1)」として併記する(1 行の注記、台帳の行は改変しない)。

## F202(E05、全列(行 E1-H の内側)の供給 (α) の対角部分が帰着した (N109$_w$) を、**Malliavin の密度公式**(Nualart 2006 Prop. 2.1.1 の型を Wiener の構造 + Gibbs の重み $e^{-V}$ で;Nourdin–Viens の密度公式;Bally–Caramellino の局所の非退化性による局在版)で、窓 $[1/E_0,1/\Lambda]$ の増分 $\Delta b_\tau$ の $\mathcal N$ の下の密度の 0 での値(閉じる関数 $B(\tau)$)を $e^{\tau E_0}$ も冪も払わずに上から押さえる方式。2026-10-20、w_E05_385_malliavin = 書き下しの型、稿 `385_全列21_Malliavinの密度の上界と閉じる確率_2026-10-20.md` §1〜§3、成算 S192)
- **閉じたもの**:**方式**((N109$_w$)・(α)・全列の真偽ではない)。
- **理由(厳密な恒等式 + 値)**:(1) 部分積分の重み $G_h=m\int\dot h\,db+D_hV$ は任意の許容な $h$($h_s-h_r=1$)で $p(0)=\mathbb E_{\mathcal N}[\mathbf 1_{F\gt0}G_h]$ を与え、上界 $\mathbb E|G_h|\ge p(0)$、$\lVert G_h\rVert_{L^2(\mathcal N)}^2$ = ずらしの Fisher 情報 $\ge1/\mathrm{Var}_{\mathcal N}F$(Cramér–Rao の型)—— 上界は真値より良くならず、真値に近いのは $h$ が $\mathcal N$ の応答の形(= 増分の分散 $V(\cdot)$ = 電流のスペクトル測度 $K$)のときだけで循環。(2) Wiener の標準の重み(窓で傾き $1/\tau$)は双極子で長時間の有効質量 $m_{\rm eff}(0)/\tau$ を、局在したテントは $m_{\rm eff}(1/\tau)/\tau$ を拾い、**標的が成り立つ双極子でさえ**積分版 $I/(m\Lambda)$ は真値 88→101 に対し 353→11105(標準)・624→4768(テント)(α=0.1、λ=10²→10⁵、最後の 10 年の局所冪 0.87・0.62)【値、T88、C0 `565_`】。(3) 非 Gauss では $\mathbb E_{\mathcal N}(D_hV)^2$ は位相の 4 点以上の量で在庫に無い(360 §3 の勘定と同じ);Hölder で Wiener に移すと $e^{c(p-1)tE_0}$。(4) 真値の側:補題 385-A(candidate)で $G_\Lambda/(m\Lambda)\ge\frac\pi{3e}\min(8\lambda,h_*^{3/2}\lambda^{-1/2})$、$h_*=h_{\rm eff}(1/\Lambda)$;双極子は平台 $h_*\approx\nu_c/\Lambda\propto\sqrt{\alpha\lambda}$ で、$B(\tau)$ は窓で $\tau^{-3/2}$ に減らない。離散時間の反跳の玩具(位相の対、MCMC)では重みの損は小さい(比 2.2〜3.7)が、真値 / Wiener が 1.5〜5.8 で τ とともに増え、密度は分散の尺度 $V^{-1/2}$ の 4 倍に達する。
- **共通点(1 行)**:**密度の上界の道具(部分積分・反磁性・エントロピー)は、窓の中の $\mathcal N$ の応答(短時間の有効質量 $h_{\rm eff}(\tau)$ = $K$ の重みの位置)を入力に要り、在庫の和則($\int K$、$T\le E_0$、凹性)の最悪 $h_*\asymp F$ は双極子で実現する —— F186・F188 の段の分散の言葉での再現。**
- **R9**:閉じたのは方式。双極子では (N109$_w$) は値で真(F の冪が 1/2)—— 障害は PF の $F\ge c\lambda^{2/3}$ と $K$ の位置に局在。
- **射程(T60)**:禁じるのは「Wiener の Malliavin 構造(標準・局在の重み)+ Girsanov / Gibbs の重みのモーメントで閉じる関数を λ に一様に押さえる」形の発注。止めないもの:$h_*$(短時間の有効質量)の PF での大きさの類 C の数値・評価;分散の尺度での反集中;(LLC) の道;有効質量の上側の評価(#3)。
- **再開条件**:(1) $J:=\frac1{m\Lambda}\int_{1/E_0}^{1/\Lambda}V(\tau)^{-3/2}d\tau\lesssim\lambda^{5/14-\epsilon}$ と、窓での分散の尺度の反集中 $B(\tau)\lesssim C(m\,h_{\rm eff}(\tau)/\tau)^{3/2}$ が λ に一様に出たとき(監査 391・A-391-2:$h_*\lesssim\lambda^{4/7}$ は $J$ の必要条件で、反集中と組んでも十分でない);(2) $\mathbb E_{\mathcal N}(D_hV)^2$ の在庫(応答の形の $h$ での Fisher 情報が $C/\mathrm{Var}_{\mathcal N}F$)が出たとき。
- **F188 の再開条件 (1) への注**:「$B(\tau)\lesssim(m/\tau)^{3/2}\lambda^{o(1)}$」は (N109$_w$) が成り立つ双極子で偽(385 観察 385-B)。上の再開条件 (1) に読み替える提案(親が照合)。

## F203(E05、難問 #2(HP-G3-1 の Q2 の値)の数値の判定:$E_0/\Lambda$ の冪が 2/3 か 5/7 かを、(i) 固定 α の局所冪の当てはめ、(ii) モード数を固定した有限モードの戯画(MPS `g3_e05_234_mps_tau`・小 Fock `422_`/`447_`・4 モード玩具 `514_`/`540_`)の局所冪・奇の割合・$A(0)$ の圧搾の再解析で決める方式。2026-10-20、w_E05_394_exponent_method = 書き下しの型、稿 `394_難問2_2_3か5_7かを効率よく見分ける数値_2026-10-20.md` §2、成算 S198)
- **閉じたもの**:**方式**(冪の真偽ではない)。
- **理由**:(i) 局所冪は Hellmann–Feynman で 1 点の観測量 $p=1-\langle H_f\rangle_0/E_0$(観察 394-A)なので律速は精度ではなく前漸近 —— LL の積の族(441b、α=1)でさえ λ=1e4 で 5/7+0.029、ずれは λ の約 −0.23 乗;局在と圧搾の予算で局在長は $(\lambda/\alpha)^{1/7}$ でしか伸びない。(ii) 戯画は ±k の鏡像対で $P_f=0$ の 2 光子(反跳なし)を厳密に作り、連続体では幅 $\lambda^{-1/2}$ の帯が有限の重みになる → 冪は 1/2 へ落ち(観察 281-3)、1 偏極の玩具では Π が可換で交差項が偶のエネルギーをほぼ全部消す($Z$=1.1e4、`576_…_reread540.py`);対の無い一般のモードを選ぶと逆に摂動に張りつく。どちらも連続体の機構を再現しない。MPS の在庫は $\langle A(0)^2\rangle$・$\langle P_f^2\rangle$ を保存しておらず ckpt も無い。
- **値の裏づけ(【T88】)**:(研究ノート: `576_w_E05_394_exponent_method_reread540.py`)(HF_OK)・`_llcrude.py`(S52、発現 $\lambda_c=4.3\times10^3\kappa\alpha^{-5/2}$)・`_twoloop_ratio.py`(CONVERGED、$R_2$ 0.49・0.62・0.67 → 0.70)。
- **共通点(1 行)**:**2/3 と 5/7 はどちらも上下界でしか特徴づけられていないので、エネルギーの比・漸近の観測量の差は最小で λ の 1/21 乗 —— 差を O(1) にするのは交差の位置の α の冪($s$=2 対 5/2)と交差の点の機構(交差項の割合 $Z$)だけ。**
- **再開条件**:λ≳1e5(α=1)の連続体の値が手に入ったとき((i));モード数が局在長 $\ell\sim(\lambda/\alpha)^{1/7}$ の立方で増え、鏡像対の反跳なしの帯の重みが連続体の $\lambda^{-1/2}$ と一致する離散化が示されたとき((ii))。

## F204(E05、全列(行 E1-H の内側)の消費者「悪い λ(擬キンク)の上での $f$ の正則性」を、**Hilbert 側の凸性**(曲率の $h_{\rm ls}$ を同時凹な $\tilde E(\lambda,q)=\inf\sigma(\lambda\frac12\pi^2-q\cdot\pi+H_f)$ の $q=0$ の曲率として、同時凹性・弦・接平面・2 次の試行の組)で出す方式。2026-10-20、hard_E05_strategy2_72 = 難所の型、稿 `393_全列26_大局の戦略の見直し_2026-10-20.md` §4 観察 393-C)
- **閉じたもの**:方式(標的・命題の真偽は閉じていない)。
- **理由**:$\tilde E$ は $(\lambda,q)$ について affine な作用素の底なので同時凹・$q$ について偶で、$E(p;\lambda)=\tilde E(\lambda,\lambda p)+\lambda p^2/2$、$f_{\rm ls}=1-\lambda c(\lambda)$。同時凹性が与えるのは弦(下界)と接平面($q=0$ の勾配は $(\langle T\rangle,0)$ で $q$ に依らない上界)だけで、2 次の試行の上界 $\tilde E\le E_0-q^2G+O(|q|^3)$ と組むと $q^2G(\bar\lambda)\le\Delta_0+\frac{q^2}4(1/\lambda_1+1/\lambda_2)+C|q|^3$($\Delta_0$ は $E_0$ の凹性の欠損)—— **$G$ の上界(= $f$ の下界、TRK の向き)だけ**。$f$ の瘤を消すには $G$ の下界が要る。擬キンクでの試行の移送も誤差がキンクの角 Δ で $p$ について $O(1)$、$D/p^2$ に届かない。
- **共通点(1 行)**:**凸性・正値性は Hilbert 側でも $f\ge$ の向き(TRK)しか返さず、悪い λ の上での $f$ の上界(瘤の排除)には届かない —— 経路測度側の共通点(F159・F164・F175・F187)と同じ向きの壁が Hilbert 側に再現する。**
- **再開条件**:$G$ の下界を与える新しい型の相関不等式(ℓ=1 の低帯の重みの下界)が立ったとき。
- **成算**:S197(条件付き 1 割前後;本方式は 0)。

## F204(E05、全列の類 C の否定の筋 ——「$E_0(\lambda)$ の擬キンク(疎な一次転移型の構造変化、曲率の悪い集合 $C_{n,K}$)の上で $f=1/h$ が $O(1)$ の瘤を持ち、全列が偽になる」という筋。2026-10-20、hard_E05_strategy2_72、稿 `393_` §2)
- **閉じたもの**:否定の筋(全列が偽である機構の候補)。全列の真偽は閉じていない。
- **理由**:P170・P201 の下で全列が偽なら $f$ は有界な段数の倍尺度の窓で $O(1)$ の瘤を持ち、瘤の位置は $B_\varepsilon$(三分法 (iii) の振動の場合だけ)か擬キンクに限られる。巨視的に異なる 2 つの ℓ=0 構造の擬交差では $\pi$(ℓ=1)が 2 構造を結ばず ℓ=1 の励起もブロック対角なので $f\approx\cos^2\theta f_1+\sin^2\theta f_2$(内挿);軟らかい転移では軟モードが ℓ=1 応答に足され $f$ は窪む;重なりが $O(1)$ の 2 構造は隙間が大きく鋭い擬キンクにならない(稿 §6 R6)。瘤には「転移の中心で ℓ=1 の低帯の重みが混合を超えて消える」機構が要り、候補なし。1 ループ・2 光子にも λ の振動因子はない(離散の内部尺度が無い)。C0 575(4 モードの玩具)に擬キンクは現れず、$f$ の非単調は有限モードの反断熱的な脱結合(値【T88】、NUM-6796)。
- **共通点(1 行)**:**擬キンクは (E-H′) 型の消費者($H_f$ の相対分散)を本当に落とすが、ℓ=1 応答 $f$ は内挿か窪みで、瘤にならない —— 鎖が擬キンクで止まることと全列が偽であることは別。**
- **注(値)**:モード数を固定した切断(有限模型・少数殻)では大きい λ で $f$ が必ず戻る(反断熱的な脱結合)ので、(LLC)$_{C=0}$ は有限模型で偽;値の梯子(350・379)の単調は人工物が効く前の帯の値。
- **成算**:全列が偽である可能性【値】1 割未満(S197 推論 2)。

## F205(E05、全列(行 E1-H の内側)の三分法(観察 393-T)の (iii)「$F$ が $\lambda^{2/3}$ と $\lambda^{5/7}$ の間を無限回振動」を**模型の構造**で排除する方式 —— (a) 殻の劣加法性(積の試行)と 323-A の超加法性の組、(b) 虚時間・光子の尺度変換(A-246-3 (1))の恒等式、(c) 300-C 型(2/3)と Gauss 型(5/7)の 2 構造の交替を P191・P194・P196 で縛る。2026-10-20、w_E05_396_oscillation = 書き下しの型、稿 `396_全列28_三分法の振動の排除_2026-10-20.md` §2、成算 S201)
- **閉じたもの**:**方式**((iii) の真偽・$E_0$ の冪の真偽ではない)。(iii) の排除は冪の決定(難問 #2)と同じ段。
- **理由**:(a) 2 つの殻の不等式は未知の殻の関数 $F_{\rm sh}$ を挟み、$F_\alpha=\alpha^bG$($b\in[\frac27,\frac13]$、$G$ 任意の凹・非減少)、$F_{\rm sh}=\frac34F$ で両方が成る(C0 578 J4:超加法の係数の最大 0.798・0.818 ≤ 1、劣加法は $G(\lambda)/G(\lambda/2)\le2$ で自動)—— 再帰は対数尺度の $O(1)$ オクターブの平滑化で、(iii) の 1 周期(対数の長さ $\ge\frac16\ln\lambda$)に触れない。(b) A-246-3 (1) は作用素の束 $aT+bH_f$ の底の 1 次斉次性そのもので、同時凹性 ⟺ $F$ の凹性(透視関数);双対の凸関数 $\varphi(x)=\inf\lbrace\langle H_f\rangle:\langle\frac12\pi^2\rangle\le x\rbrace$ の凸性は 254-B と同じ強さしか与えない;α と λ を結ぶ尺度も無い。(c) 固定した試行状態のエネルギーは λ について affine(凹性の接線)で、2/3 の帯の状態を大きい λ に運ぶとちょうど (iii) の凍結の帯になる(C0 578 J1:接点 $\mu_{n+1}=\mu_n^{5/4}$ の接線の階段は凹・両側の冪を満たし $\tilde Q$=12.9→4.5 で有界);打ち消しの精度(365-C の奇の割合)の λ 依存を縛る在庫は無い。
- **共通点(1 行)**:**在庫の構造(凹性 = 束の斉次性・両側の冪・殻の分割・試行の族の床)は全て λ の 1 点か $O(1)$ オクターブの比較で、(iii) の振動は対数の長さ $\ge\frac16\ln\lambda$ に住み、殻の関数・試行の精度という同じ類の未知関数に吸収される。**
- **R9**:閉じたのは方式。ただし (iii) の排除は全列に不要になる候補:補題 396-W($M^{-2}$ の望遠鏡和)で崩れと曲率の積 $W$ の 2 進平均が無条件に $O(\lambda^{-1/7})$、全列の壁は (REG-ω) 1 本(定理 396-D・命題 396-F、candidate、S2 待ち)—— 難しさは消えずに「曲率の急な立ち上がり」(擬キンク)に移る。値:NUM-6420・6785 の局所冪は滑らか【T88】。

## F206(E05、全列(行 E1-H の内側)の名指し (REG-W)〔$F\in C^1$ ∧ $\kappa_p\tilde Q\to0$〕を**崩れ $\tilde Q$ の側**(κ が大きい所で $\tilde Q$ が小さい)から供給する方式 —— (a) 擬キンクでの $M=\langle H_f\rangle$ の急増 ⟹ $\tilde Q$ の低下を、凹性と $M=F-\lambda F'$ だけから各点の 2 量の連動の不等式に、(b) (LL-up$^-$)〔$F/\lambda^{5/7}\to0$〕を在庫の型で(395-T′ で $\tilde Q\to0$ に直結)、(c) 凍結の帯(396-S)の長さの上界で 396-W の望遠鏡和を各点に。2026-10-20、w_E05_403_regw_qside = 書き下しの型、稿 `403_REGW5_崩れの側_2026-10-20.md` §1・§2.4)
- **閉じたもの**:**方式**((REG-W) の真偽ではない)。(REG-W) は $F$ だけの性質で、在庫が $F$ に課す制約からは原理的に出ない。
- **理由**:(a) 丸めた接線の階段(凹、$F'$ 非増加、$0.97c\lambda^{2/3}\le F\le0.81\lambda^{5/7}$)で角の対数の幅を $\lambda^{-1/7-0.05}$ にすると $W_{\max}$=2.9→155(λ=10³→10⁴²、C0 585 J1);$M$ が増えるのは角の後で、立ち上がりの始点の $W\sim\lambda^{-1/7}/\delta$ は幅 δ だけで決まる。(b) 同じ族が $F/\lambda^{5/7}\ge0.55$ を満たす;(LL-up$^-$) は冪の段(F205・394、5/7 寄り 65% なら偽)で、しかも $\tilde Q\to0$ だけでは κ の側が残る。(c) 帯の長さの上界は (iii) の排除そのもの(F205);各点化に要るのは帯の長さでなく終わりの角の幅。
- **共通点(1 行)**:**崩れ $\tilde Q$ を下げる機構($M$ の増加)は曲率の窓の積分にしか反応しないので、在庫だけの各点の形は「窓の積分 × 端の崩れ = $O(\lambda^{-1/7})$」(補題 403-A)で尽き、点の曲率と窓の平均の比(擬キンクの幅 = 擬交差の相対の隙間)は崩れの側に無い。**
- **R9**:閉じたのは方式。崩れの側の成果は補題 403-A と十分形の弱化 (REG-ω) → (REG-L)〔幅 $\gg\lambda^{-1/7}$、閾は鋭い〕(E05-P206 = 稿 403 §2)。難しさは消えずに「擬交差の相対の隙間 $g/\Delta\langle T\rangle\gg\lambda^{-1/7}$」に移る(393 §3.4 (b) の段)。**再開条件**:擬交差の隙間を量で下から押さえる道具(在庫に無い)か、$\langle T\rangle$ の λ についての 2 階の応答の各点の比の評価(曲率の側の族)。

## F207(E05、全列(行 E1-H の内側)の唯一の名指し (REG-W)〔$F\in C^1$ ∧ $\kappa_p\tilde Q\to0$〕とその十分形 (REG-K)・(REG-ω) を、**ビリアル・光子の拡大・Mourre(ℓ=0)・hypervirial** で供給する方式 —— (a) ビリアルの恒等式の λ 微分で $F''$ を境界項の応答で書き $\chi_T$ の上界へ、(b) ℓ=0 の Mourre 推定で低帯の重みを押さえる、(c) hypervirial(F66 行 2618 の型)、(c′) ℓ=0 の和則。2026-10-20、w_E05_401_regw_virial = 書き下しの型、稿 `401_REGW3_ビリアルと拡大とMourre_2026-10-20.md` §1〜§3、成算 S204)
- **閉じたもの**:**方式**((REG-W)・(REG-K)・(REG-ω)・全列の真偽ではない)。
- **理由(代数 + 雑な計算;値は使わない)**:(1) 光子の拡大 $U_sa(k)U_s^*=e^{3s/2}a(e^sk)$ は $U_sH(\lambda,c)U_s^*=e^{-s}H(e^{-s}\lambda,e^sc)$($c$ は切断)を与え、ビリアル $\langle i[G,H]\rangle_0=0$($i[G,H]=\lambda T'-2\lambda T-H_f$)は尺度則 $E_0(\lambda,c)=cF(\lambda c)$ の Feynman–Hellmann 形 —— F205 (b) の「次元解析は尽きている」と同じ内容。(2) 2 階:恒等式 401-1 $\chi_{TT}=\chi_{TT'}-M/(2\lambda^2)$、$\chi_{T'T'}=\chi_{TT}+(\langle T''\rangle-2F')/(2\lambda)$ —— $(\lambda,c)$ 平面の 2 階の応答は全て $F''$ と 1 次の量で決まり、Cauchy–Schwarz は循環。(3) 観察 401-2:$(T'\psi_0)^c=(T\psi_0)^c-\frac i\lambda(H-E_0)G\psi_0$ —— 切断の縁の演算子の低帯は $T$ の低帯と一致;一般に hypervirial $X\mapsto X+i[H,B]$ は低帯の重みを $O(\eta\lVert B\psi_0\rVert)$ しか動かさず、$\chi_{TT}$ を厳密に書く $B\psi_0=-iRT\psi_0$ は $\int\mu^{-2}d\nu_T$ を要る(より強い)。(4) 和則 (c′) は Jensen で $\chi_{TT}$ の**下界**しか出さない。(5) Mourre の出力は型と LAP で、特定のベクトル $T\psi_0$ の閾値での重みを与えない(F182 (3));擬交差の相手(準固有状態)の上ではビリアルの定理で正の交換子が $O(\Gamma)$ に消え、評価はそれをコンパクトな余りに吸う —— 隙間 $2\lvert V\rvert$ の下界は交換子の射程の外。C0 583((研究ノート: `583_w_E05_401_regw_virial_c0.py`)、11 s):J1・J2・J4 PASS(恒等式・低帯の不変性・$\lVert RT\psi_0\rVert\propto1/V$)、J3 は固定の判定で FAIL(窓の取り方;事後の読みは同じ向き)【T88】。
- **共通点(1 行)**:**拡大・ビリアル・交換子の代数は $(\lambda,c,t)$ の族を 1 変数の $F$ に畳む尺度則の言い換えで、2 階の量を $F''$ と 1 次の量に戻すだけ;$T\psi_0$ の低帯の重み(擬交差の隙間)は $\mathrm{Ran}(H-E_0)$ の外にあり、交換子はそこを見ないか、擬交差の相手の上で消える —— F66・F78・F155・F182 (3)・F188 K2・F205 (b) と同じ段(393 §3.4 (a)(b))。**
- **R9**:閉じたのは方式。(REG-W) は値で真の向き(NUM-6800)。
- **射程(T60)**:禁じるのは「光子の拡大のビリアル・hypervirial・二重交換子の和則・Mourre の正の交換子(固定の生成子 $A$)を ℓ=0 の $T$(または $H_f$)の応答に当てて (REG-W)・(REG-K)・(REG-ω) の κ の上界を出す」形の発注。止めないもの:2 構造の間の有効結合 $V_{\rm eff}$ の非摂動の下界・ℓ=0 の低帯の構造の非存在を扱う方式(交換子はその量化の補助としてなら使ってよい);滑らかな族での恒等式 401-1 の他の消費者への利用。
- **再開条件**:(1) 擬交差の相手の構造の非存在、または $V_{\rm eff}$ の λ に一様な下界が別の方式で出たとき(そのとき Mourre・ビリアルは $\nu_T$ の閾値の率の量化に使える);(2) $T\psi_0$ を $\mathrm{Ran}(H-E_0)$ と「低帯の重みが量的に分かる部分」に分ける表示が出たとき。
- **射程への追記(2026-10-20、稿 401 §5′、標的の弱化 (REG-L) への当て直し)**:(REG-L)〔擬交差の相対の隙間 $g/\Delta\langle T\rangle\gg\lambda^{-1/7}$〕に対しても同じ段 —— ビリアル・hypervirial の恒等式は $\chi_{TT}$ が両辺に同じ形で出る循環で定数の損の問題でなく、Mourre は隙間 $g$ を見ないので許す損の大きさに依らない。和則は下界のまま。

## F208(E05、全列(行 E1-H の内側)の名指し (REG-W) を**解析的摂動論・作用素の繰り込み群による $E_0(\lambda)$ の正則性**で供給する方式(族 K4)—— (a) 赤外を切った模型の Kato 型 $C^2$ と赤外の除去;(b) RG の固定点の近くでの λ の流れの滑らかさ;(c) 紫外で一様な定数;(d) 複素 λ の帯の解析性と Cauchy の評価;(e) 有限モードの Rellich 解析性の極限。2026-10-20、w_E05_402_regw_rg = 書き下しの型、稿 `402_REGW4_解析性と繰り込み群_2026-10-20.md` §0〜§2、成算 S205、C0 584)
- **閉じたのは: 方式**。標的((REG-W)、全列)と命題の真偽は閉じない。
- **理由 (a)**:赤外は障害でない(Hasler–Herbst 2011 Thm 1 は IR 切断 σ≥0 について一様・連続);Kato 型の評価 $\chi_T\le\mathrm{Var}(T)/d$ は重みを見ない入力で、Gauss 型で $\kappa\le\frac43pF/d$ —— 隙間が $O(\Lambda)$ でも $\lambda^{5/7}$ を失う(F188・393 §3.4 (a) の段)。C0 584【値】で損は殻の数と λ で増える(実際の κ は O(1))。
- **理由 (b)**:作用素 RG は赤外へ回り、初期の Hamiltonian を多円板に入れる段が小さい結合を要る;紫外は無次元の結合 $\alpha\lambda$ が大きい強結合で制御された固定点が無い。強結合の固定点 $F\approx c\lambda^\beta(1+o(1))$ の存在は難問 #2 の冪の決定を含む(396 §2、F161・F181 の段)。
- **理由 (c)**:原典逐語で Griesemer–Hasler 2009 Thm 1(「g < g0」、近傍 V0、双極子近似)・Hasler–Herbst 2011 Thm 1(「g ∈ D_g0」、UV 切断 Λ は fixed)—— λ→∞ に一様な定数を持たない(F170 (iii)・F171 (a) と同じ量化子)。
- **理由 (d)(e)**:消費者の側は効く(観察 402-C:$\ln\lambda$ の固定幅の円で有界正則、または (REG-3)「$|F_{ss}|\le C_2F$、$|F_{sss}|\le C_3F$」⟹ $W=O(\lambda^{-1/21})$、全列;self-audited、名指しにしない)。供給は、帯の幅 = 擬交差の分岐点までの距離 $g/\Delta$ の下界(393 §3.4 (b)、F22 は正確な交差を禁じるだけ)と、連続スペクトルの底での解析接続(F198)・$T$ の 3 次の応答の評価(F159・334-C)の段。有限モードの解析性の帯の幅はモード数に一様でない。
- **弱化 (REG-L)(稿 403)への再照合**:要る擬キンクの対数の幅 $\gg\lambda^{-1/7}$ は隙間 $g\gg\lambda^{4/7}$($M$ の尺度)に当たり、Kato の収束半径は隙間 $O(\Lambda)$ でも幅 $\gtrsim\lambda^{-5/7}$ しか出さない($\lambda^{4/7}$ 不足);巨視的に異なる 2 構造のトンネルは $e^{-c\lambda^{4/7}}$ の型で、幅の下界は擬交差の不在の証明に等しい。判定は変わらない(稿 `402_` §2.6)。
- **共通点(1 行)**:**解析性・RG の定理は小さい結合・固定の切断の近傍で立つ局所の正則性で、λ→∞ の漸近には隙間(または固定点)の量的な下界を要る —— それが擬交差の隙間の下界・冪の決定と同じ段(393 §3.4 (b)・難問 #2)。**
- **R9**:閉じたのは方式。(REG-W) は値で真の向き(NUM-6800)で、名指しは残る。
- **射程(T60)**:禁じるのは「GH・HH・BFS・BCFS 型の解析的摂動論・作用素 RG・Kato–Rellich の正則族の理論で、$E_0$ の λ についての正則性を λ→∞ に一様に出す」発注。止めないもの:観察 402-C の消費(他の族が (REG-3) の形を出したとき);擬交差の隙間の下界・3 次の応答の新しい入力。
- **再開条件**:(1) 巨視的に異なる 2 構造の擬交差の隙間を λ に一様に下から押さえる入力;(2) $T$ の 3 次の応答(連結 3 点関数)の相対評価 $|F_{sss}|\le CF$($s=\ln\lambda$);(3) 強結合の尺度不変な固定点の存在(難問 #2 を含む)。どれかが出たら観察 402-C で全列。

## F209(E05、全列(行 E1-H の内側)の名指し (REG-W) の κ を、保存済みの A1 の HMC のブロック平均から Kubo(虚時間の連結自己相関の積分)で直接測る方式 —— 閉じたのは**方式**(値の測定法)。2026-10-20、w_E05_400_regw_value、稿 `400_` §2.1)
- **方式**:$\kappa=\lambda\lvert F''\rvert/F'=2\chi_K/K_E$、$\chi_K=\int_0^\infty\langle\delta K(\tau)\delta K(0)\rangle d\tau$($=\chi_f$)を、(研究ノート: `lam{32,64,128}.json`)(4 rep × 10 ブロック × 40 枚、T=6)の primitive の運動エネルギー推定のブロック分散から読む。
- **止まった段**:片側の積分 $S$ は自由 Brown の接触項 $0.75/dt\propto\lambda^2$(768・3072・12288)が支配し、$S$ の統計誤差 / 目標 $\chi_K\approx\kappa K_E/2$ = 61・59・115(C0 `582_w_E05_400_regw_value_kubo_feas.py`、INCONCLUSIVE:few_data)。配位そのもの(snap)はこの機械に無い。
- **再開条件**:接触項を持たない推定量(virial・centroid、あるいは λ の再重み付けの差分)を入れた新しい鎖、または約 $60^2$ 倍のデータ。値の出所は差分の θ(577)で足りるので優先度は低い。

## F210(E05、全列の名指し (REG-W) の本体「$\kappa p\tilde Q\to0$」を、$C^1$ の道具(Hellmann–Feynman の不等式・基底状態の族のコンパクト性・2 次の試行)で供給する方式 —— 閉じたのは**方式**。2026-10-20、w_E05_400_regw_value、稿 `400_` §4 行 K2-3)
- **止まった段**:HF の不等式とコンパクト性が出すのは 1 階(上勾配の一点性 = $C^1$、定理 400-1)だけ;2 次の試行 $\psi-h(H-E)^{-1}Q(T-\langle T\rangle)\psi$ は $F(\lambda+h)\le F+hF'-h^2\chi_T+O(h^3)$、すなわち 2 次の欠損の**下界**で向きが逆。上界には真の 2 次摂動の等式(基底状態の λ についての微分可能性)か ℓ=0 の低帯の重みの上界が要る —— 393 §3.4 (a)(c)・F188 と同じ段。各点の $\chi_f\lt\infty$ も赤外(1 軟光子)の寄与しか押さえず、擬交差の低帯は押さえない(393 §3.4 (b))。
- **再開条件**:擬交差の隙間の量的な下界、または λ について基底状態が微分可能であることの道具(連続スペクトルの底で)。

## F211(E05、全列(行 E1-H の内側)の名指し (REG-W)〔$F\in C^1$ ∧ $\kappa p\tilde Q\to0$;十分形 (REG-ω)・(REG-K)∧$\tilde Q\to0$・(REG-L)〕を、**正値性の改良(Perron–Frobenius)と擬交差の隙間**で供給する方式 —— (a) 量的 PF(Doeblin・Birkhoff–Hopf の射影的縮小・最小の遷移確率)で ℓ=0 の 2 構造の重なり → 隙間の下界、(b) 2 軟光子の連続体を除く Feshbach 縮約で有効 2 準位、(c) 393 §2 の内挿(擬交差 ⟹ $f$ の瘤なし)を κ の上界に読み替え、(d) 虚時間の転送作用素の PF(Ruelle 型の 1 次元の解析性)、(e) 正値性から 3 階の符号(GHS 型、$F'''\ge0$)。2026-10-20、w_E05_404_regw_pf = 書き下しの型、稿 `404_REGW6_正値性と擬交差の隙間_2026-10-20.md` §1〜§5、成算 S207)
- **閉じたもの**:**方式**((REG-W) の真偽・擬交差の有無ではない)。
- **理由(計算 + 値)**:(1) **消費者の照合**(観察 404-A、2 準位):交差の中心で $W_c=\alpha\lambda\Delta\langle T\rangle^2/(4tM_c^3)\le2\alpha/(t\Delta\tau)$;(REG-W) が交差で成るには相対の隙間 $t/\Delta\langle T\rangle\gg s_*$、$s_*\le\frac{\alpha}{2c_1^2}\lambda^{-1/7}$(稿 403-C の (REG-L) の閾と同じ冪)、絶対の隙間で $t\gg\alpha\lambda^{2/7}$〜$\alpha\lambda^{3/7}$ —— 下界でなく **λ とともに増える隙間** が要る。(2) (a):量的 PF は真の隙間を超えない(C0 586 J2:PF の成る確率的な鎖で隙間は障壁の長さに指数的に閉じ、Birkhoff–Hopf の保証は真の隙間の 98〜99%);巨視的に異なる 2 構造(光子数の差 $\ge\Delta\langle T\rangle\gtrsim\lambda^{4/7}$)を結ぶ鎖は長く、保証は指数的に小さい;無限次元の Fock/Q 空間では射影的直径が無限で保証は空。393 §3.4 (b)・E05-P132 の非主張と同じ段。(3) (b):連続体の $\chi_T$ への寄与は赤外で有限(密度 $\sim x^3$、値)で障害でない;縮約後の量は有効トンネルで (a) と同じ;λ に一様な Feshbach は F170 (iii)・F171。(4) (c):擬交差で $\kappa_c\propto1/t$ は本当に大きく(J2 の $\kappa_{\max}\cdot$gap = 1.60 一定)、内挿は $f$ の性質。(5) (d):解析性の半径 = 擬交差の幅 = (a) の $t$;時間方向の相互作用 $\tau^{-2}$ は $\sum rJ(r)$ の境界;F198。(6) (e):λ は外場でなく質量で GHS の型の外;J3 で PF の族の擬交差の前後で $F'''$ が符号を変える。
- **共通点(1 行)**:**正値性(PF・転送作用素・相関不等式の符号)はトンネル振幅の正しか与えず大きさを与えない —— (REG-W) の各十分形が擬交差に要るのは λ とともに増える隙間(相対 $\gg\lambda^{-1/7}$)、すなわち鋭い一次転移型の構造変化の不在で、それは結合の大きさの量的な情報。**
- **射程(T60)**:禁じるのは「(REG-W)(または十分形)を正値性の型 (a)〜(e) で供給する」形の発注。止めないもの:強結合での 2 構造のトンネルの大きさの直接の評価(正値性でなく結合の量の評価);構造ごとに条件づけた消費者((I1) の $v_f$ の置き換え、観察 404-B);命題 404-G の監査。
- **再開条件**:(1) 擬交差しうる 2 構造の間のトンネル振幅が相対 $\gg\lambda^{-1/7}$ で下から押さえられる量的な評価(正値性以外の入力)が在庫に載ったとき;(2) λ についての $\langle T\rangle$ の凸性(ℓ=0 の静的感受率の単調性)を与える相関不等式が立ったとき(命題 404-G で全列)。
- **副産物**:命題 404-G($F'_+$ 凸 ⟹ 全列、率 $\lambda^{-1/14}$、candidate;(REG-L) の特別な場合)、観察 404-B((REG-W) は全列の必要条件でない)。

## F212(E05、全列(行 E1-H の内側)の唯一の名指し (REG-W)〔$F\in C^1$ ∧ 各点の $W_-=\kappa p\tilde Q\to0$;十分形 (REG-ω)・(REG-K)∧$\tilde Q\to0$〕を、**パラメータについての基底エネルギー(自由エネルギー)の正則性の道具**で供給する方式 —— (a) 結合定数・切断についての解析性・滑らかさ(Abdesselam–Hasler 2012、Griesemer–Hasler 2009、Hasler–Herbst 2011、Faupin–Møller–Skibsted 2011、光子質量つきの Kato の解析的摂動)、(b) 一次転移の不在の一般論(Lee–Yang、GKS・GHS・Lebowitz、Aizenman–Wehr、相関の減衰 ⟹ 解析性・1 次元の転送作用素、Gerlach–Löwen 1991、「一次転移 ⟺ 平衡状態の非一意」、Pirogov–Sinai)、(c) ポーラロン・Nelson の近年の結果のパラメータ正則性の面(Lampart–Mitrouskas–Myśliwy 2023、Polzer 2023、Brooks–Seiringer・Betz–Polzer、Dybalski–Spohn)。2026-10-20、w_E05_405_regw_journey = 書き下しの型、稿 `405_REGW7_道具探しの旅_2026-10-20.md` §1・§2、成算 S208)
- **閉じたもの**:**方式**((REG-W) の真偽・全列の真偽ではない;(REG-W) は値で真の向き、NUM-6800)。照合した 15 行の全てが成算 1 割未満。
- **理由**:(1) 物差し(稿 §1.2、C0 587 J2):隙間 $g$ の擬交差で $W$ の峰は $\propto1/g$、2 進平均は $g$ に依らない(補題 396-W の $O(\lambda^{-1/7})$)ので、各点の $W\to0$ には擬交差の隙間の冪の下界 $g\gtrsim M$ が要る;巨視的に異なる 2 構造のトンネルの隙間は $e^{-c\lambda^{4/7}}$ 型。(2) (a) の解析性の域は全て**結合**についての小結合($g^2\int^\Lambda\lvert k\rvert^{-2}\lesssim1$、Abdesselam–Hasler Thm 1.1 を本文照合)で λ→∞ で 0 に縮む;光子質量つきの Kato は定性の実解析(分岐点までの距離 = 隙間)。(3) (b) Lee–Yang・GHS は λ が強磁性の指数族の「場」として入る構造を要るが λ は電子の拡散定数;零点の無い扇形 ⟺ 隙間の下界(稿 §1.3);GHS 族は F187 (K2) で閉;Aizenman–Wehr は乱れを要り、λ の平均で代えた到達点は定理 396-D;相関の減衰の型は虚時間の核 $\approx4\pi/\tau^2$ で $\sum rJ(r)\approx4\pi\ln R$ の対数発散(C0 587 J3、1 次元の $1/r^2$ の境界)かつ結合の強さが $\alpha\lambda$ で増える;Gerlach–Löwen は適用域が頂点が電子の運動量に依らない結合で PF の $p\cdot A$ は域の外、機構も定性;非一意 ⟺ 一次転移の原理は $C^1$ の句だけ(補題 405-C)。(4) (c) は正則性が全運動量 $P$ についてか、α の漸近(単調密度定理で 1 階まで)。
- **共通点(1 行)**:**パラメータ正則性の道具は隙間(孤立・指数減衰)・強磁性の場の構造・小結合か乱れのどれかを要り、出力は定性の解析性か平均の量 —— (REG-W) が要る擬交差の隙間の冪の下界(= 擬交差の不在)に届かない。393 §3.4 (b)・F198・F187 (K2)・F170 (iii) と同じ段。**
- **R9**:閉じたのは方式。双極子(Gauss)では $F$ は冪で擬交差なく段は空;障害は「非 Gauss の構造変化の有無を λ について縛る量が無い」ことに局在し、消滅していない。
- **射程(T60)**:禁じるのは「結合・切断についての解析性の定理(小結合の量化子)を λ→∞ に運ぶ」「Lee–Yang・GHS・Lebowitz を λ を場として当てる」「乱れの丸め・相関の減衰の解析性を無質量の虚時間の核で回す」「ポーラロンの相転移の不在(Gerlach–Löwen)を PF に移す」形の発注。止めないもの:(CPT$_{\rm loc}$) の照合(補題 405-C、$C^1$ の句);λ の 3 階の符号を出す新しい表示(補題 405-G の消費者)。
- **再開条件**:(1) F187 の再開条件 (1)(場の側の強磁性の表示)で λ の 3 階の符号 $F'''\ge0$ が出たとき(補題 405-G で (REG-W) が率 $\lambda^{-1/7}$ で閉じる);(2) 擬交差の不在を言う λ についての単調量(RG の極限周期の排除の型)が見つかったとき;(3) Gerlach–Löwen 1991 の原典(RMP 63、[要入手])に速度結合への拡張の議論があったとき。

## F213(E05、全列(行 E1-H の内側)の名指し (REG-W)〔$F\in C^1$ ∧ $\kappa_p\tilde Q\to0$;十分形 (REG-K)∧$\tilde Q\to0$・(REG-ω)・(REG-L)〕を、**経路測度の上の位相のない ℓ=0 の量の分散**(K1)で供給する方式 —— (a) 運動エネルギーの作用 $\int\frac\lambda2|\dot b|^2$ の λ についての 2 階を反跳つき Gibbs 測度 $\mathcal N$ の分散として書き Wiener の分散と比較(Cameron–Martin・尺度変換 $b\mapsto b/\sqrt\lambda$)、(b) 電子を先に積分した場の測度の下での $\int H_f$ の分散(正値の混合・Brascamp–Lieb)、(c) 両者の組(場 | 経路 の条件付き Gauss)、(補) Hilbert 側のモーメント・和則で $\int E^{-1}d\mu_{T\psi_0}$。2026-10-20、hard_E05_regw_path_72 = 難所の型、稿 `399_REGW1_経路測度の位相のない量の分散_2026-10-20.md` §1〜§2、成算 S202)
- **閉じたもの**:**方式**((REG-W)・(REG-K)・全列の真偽ではない)。
- **理由(厳密な恒等式 + 雑な計算 + C0)**:(1) **観察 399-A**(離散 FK で初等):λ の微分は Wiener 測度の拡散定数の微分 = くりこんだ運動エネルギーの作用 $\mathcal T_\epsilon=\sum_i|\Delta b_i|^2/(2\lambda\epsilon)-3n/2$ で、位相を持たないが $\mathrm{Var}_W(\mathcal T_\epsilon)=3t/2\epsilon\to\infty$($L^2$ の外);恒等式 $\kappa=\lambda|F''|/F'=2+[\mathrm{Var}_{\mathcal N}(\mathcal T_\epsilon)-\mathrm{Var}_W(\mathcal T_\epsilon)]/(t\langle T\rangle)$ により (REG-K) ⟺ 発散する 2 つの分散の差が $(K-2)t\langle T\rangle$ 以下(相対精度 $\epsilon\langle T\rangle\to0$)。有限な観測量に直す(尺度変換の Euler 作用素 $\mathcal LV=\frac12w\cdot\nabla_wV$)と $\cos(k\cdot y)\mapsto-\frac12(k\cdot y)\sin(k\cdot y)$ で反跳の位相が因子 $k\cdot\Delta b$ つきで戻り、(REG-K) ⟺ $\mathrm{Var}_{\mathcal N}(\mathcal LV)\le\mathbb E_{\mathcal N}\mathcal L^2V+(K-1)t\langle T\rangle$ の右辺は位相つきで符号不定(C0 581b:$|\mathbb E\mathcal L^2V|/\mathrm{Var}(\mathcal LV)$=85→3.6、λ=1→16);場を残せば観測量は位相なしだが測度が複素(F169 (M2))。**「位相なし」「有限な分散」「実で正の測度」は 2 つまでしか取れない。**(2) **(a)**:Γ 形(Poincaré・BL)は 2 次の汎関数で Wiener でも因子 2 を失い(377-A の型)、$\mathcal T_\epsilon$ では損 $\approx\mathrm{Var}_W\propto1/\epsilon$ —— 対数凹で厳密 Gauss の双極子でも BL の見積り $\Delta_{\rm BL}/(t\langle T\rangle)$=38→2673(ε=1/4→1/256、C0 581a、傾き −1.02〜−1.33)、真の差は有界([−1.96,−1.65]);有限の ε では測度の非対数凹性(F183)が壁。$\mathcal T_\epsilon$ は超関数として $\frac12(|\nabla V|^2-\Delta V)$ = 355-A の方向の和で、(α)・(SPEC-G) 型に戻る(355 の段)。(3) **(b)**:$\int H_f$ は場の Euclid 作用($\dot\Phi^2$)で同じ $1/\epsilon$ の特異性、有限形は A-246-3 (1) で $\chi_f=\lambda^2\chi_T$ = (a) と同じ観測量;場の測度 $K_{\mathcal A}\gamma$ は時間依存の場で各点の正値性が立たず、正値の混合の下でも 2 次の汎関数の分散は $\ge$ Gauss の平均(平均の分散の項:377 §8.2・338 の向き)、BL の前提の対数凹性は在庫に無い。(4) **(c)**:条件付き Gauss(複素のずらし)の分解は全分散に位相つき 2 体汎関数の $\mathrm{Var}_{\mathcal N}$ を残す(= (α) の 2 体版)。(5) **Hilbert 側**:正のモーメントは和則型で計算できるが $E^{-1}$ の重みは重みを見ない入力で押さえられない(F78 (a)・F182 (c)・F188 (a) の ℓ=0 版)。(6) 標的の弱化 (REG-L)(稿 403、$\lambda^{1/7}$ の損の許容)でも判定不変:止まるのは損の冪でなく「上界を返す道具が無い」こと。
- **共通点(1 行)**:**経路測度の上で ℓ=0 の量の位相を外すと観測量は $L^2$ の外に出て、分散の比較は発散する量どうしの差(相対精度 $\epsilon\langle T\rangle$)になる;有限にすると位相が戻って 355-A・F169・F183 の段に落ちる —— 393 §5 の「道具は上界(TRK の向き)しか返さない」の FK の表示での再現。**
- **R9**:閉じたのは方式。双極子では (REG-K) は真(C0 581a:κ=0.04〜0.30、$\theta\in(0,1]$)—— 障害は反跳の位相に局在し消滅していない。
- **射程(T60)**:禁じるのは「$\chi_T$・$\chi_f$ を FK の位相のない量の分散として Gauss 比較・BL・条件付き Gauss・正値の混合で押さえる」「場の測度の正値分解で $\int H_f$ の分散の上界を出す」「ℓ=0 の $T\psi_0$ の低帯の重みをモーメント・和則で押さえる」形の発注。止めないもの:(REG-W) の $F\in C^1$ の部分(基底状態の λ 連続性、F210 の行);(REG-L) の点と窓の比較(3 階の応答の型);値の判定(400 の K2)。
- **再開条件**:(1) PF の重み $e^{-V}$ の Gauss 比較を Γ 形でない**exact な**形($\mathrm{Var}_{\mathcal N}(Q)\le\mathrm{Var}_W(Q)+o(t\langle T\rangle)$、$Q$ は 2 次の汎関数)で与える定理が、対数凹でない重みの族について在庫に載ったとき;(2) F169 の再開条件 (1)(構成的な正値分解で測度が実の正値の Gauss 混合**かつ**混合の分散の項を押さえる入力)が出たとき;(3) ℓ=0 の $T\psi_0$ の $H$ についてのスペクトル測度の低帯の重みの上界が、重みを見る入力(擬交差の隙間の下界 = 393 §3.4 (b))で出たとき。

## F214(E05、全列(行 E1-H の内側)の名指し (REG-W)〔$F\in C^1$ ∧ $\kappa p\tilde Q\to0$;十分形 (REG-K)∧$\tilde Q\to0$・(REG-ω)・(REG-L)〕を、**分配関数 $Z(\beta,\lambda)=\mathrm{tr}\ e^{-\beta(\lambda T+H_f)}$ の完全単調性(BMV = Stahl の定理、Bernstein の Laplace 表示)と対数凸性**で供給する方式(候補表 K8 (3))。2026-10-20、w_E05_406_regw_longshots = 書き下しの型、稿 `406_REGW8_可能性の低い型の一括_2026-10-20.md` §3 (3)・§2、成算 S209)
- **閉じたもの**:**方式**((REG-W) の真偽ではない)。
- **理由**:Stahl(arXiv:1107.4875、有限次元)で $Z_\beta(\lambda)=\int e^{-\lambda s}d\mu_\beta$、$\mu_\beta\ge0$。$E_0=\lim-\beta^{-1}\log Z$ は率関数の Legendre 変換で、正値の測度は任意の凹関数を作れる(2 原子で角)。補題 406-U(凹・非減少・非負の任意の $F$ は対角の $T,V\ge0$ で実現できる)と系 406-U1 により、全ての $T,V\ge0$ で成り立つ性質は凹性を超えない。C0 588 bmv:κ=113 の 2 準位族で前進差分 10 階まで交代(β=1・10・50)。対数凸性は PROVED 6474 の型(凹性)、$(\beta,\beta\lambda)$ の同時凸性は透視関数の凹性(F205 (b))。
- **共通点(1 行)**:**完全単調性・対数凸性は全ての $\lambda T+V$ で成り立つ普遍の性質で、$E_0$ に凹性しか課さない(系 406-U1)。**
- **R9**:閉じたのは方式。言い換え(名指しにしない):(REG-K) ⟺ 時間平均した運動エネルギーの率関数の一様な強凸性 $s\varphi''(s)\ge\lambda(s)/K$。
- **射程(T60)**:禁じるのは「分配関数の λ についての完全単調性・Laplace 表示・対数凸性から κ の上界を出す」発注。止めないもの:率関数の強凸性を模型固有の入力(トンネル振幅)で出す方式。
- **再開条件**:F211 の再開条件 (1)(2 構造の間のトンネル振幅の量的な下界)。

## F215(E05、全列の名指し (REG-W) を**作用素単調関数・Löwner の理論**($\lambda\mapsto f(\lambda T+H_f)$ の作用素単調性・作用素凹性、レゾルベント $(\lambda T+H_f-z)^{-1}$ の作用素凸性)で供給する方式(候補表 K8 (4))。2026-10-20、w_E05_406_regw_longshots = 書き下しの型、稿 `406_` §3 (4)、成算 S209)
- **閉じたもの**:**方式**。
- **理由**:出るのは $f(E_0)$ の凹性(作用素単調な $f$)と $1/(E_0+c)$ の凸性で、どちらも $E_0$ の凹性から従う(より弱い)。レゾルベントの形式の 2 階 $2\langle\varphi,RTRTR\varphi\rangle\ge0$ は下界で、向きが逆。全ての $T,V\ge0$ で成り立つので系 406-U1 に当てはまる。
- **共通点(1 行)**:**作用素の単調性・凸性は普遍の性質で、1 次か向きが逆(393 §5 の共通点)。**
- **R9**:閉じたのは方式。**射程(T60)**:禁じるのは「Löwner・作用素単調・作用素凸の性質で κ の上界を出す」発注。**再開条件**:F211 の再開条件 (1)。

## F216(E05、全列の名指し (REG-W) を**確率論の結合**(λ と λ′ の反跳つき Gibbs 測度の結合で $F'(\lambda)-F'(\lambda')$ を押さえる;同期の結合・指数型族の相対エントロピー・Pinsker)で供給する方式(候補表 K8 (9))。2026-10-20、w_E05_406_regw_longshots = 書き下しの型、稿 `406_` §3 (9)、成算 S209)
- **閉じたもの**:**方式**。
- **理由**:$\lvert F''\rvert=2\chi_T$ は $T$ の虚時間の自己相関の積分。結合の縮小は相関時間の上界と同じで、擬交差では準安定な 2 構造の切り替えの時間 ~$1/g$ が入る(2 準位で $\chi\approx\Delta\langle T\rangle^2/(4g)$)。縮小定数は隙間 $g$ の下界を要する。作用が λ について線形なら、相対エントロピーの率は Bregman の欠損 $D(h)$ そのもので、Pinsker の向きは「$D$ 小 ⟹ 近い」(循環)。PF の Feynman–Kac では λ は Brown 運動の分散に入り、$T$ は経路の汎関数として接触項を持つ(F209)。
- **共通点(1 行)**:**結合の縮小定数は混合の時間 = 擬交差の隙間の逆数で、F211(トンネル振幅)と F186・F201(経路の反集中・$B(\tau)$)の段。**
- **R9**:閉じたのは方式。**射程(T60)**:禁じるのは「λ と λ′ の Gibbs 測度の結合・相対エントロピー・輸送距離で κ の上界を出す」発注(縮小定数を別の入力で持つ場合は除く)。**再開条件**:F211 の再開条件 (1)、または F186 の再開条件。

## F217(E05、全列の類 C の否定の筋 ——「PF 型の数モードの反跳の玩具 $\lambda\frac12(P_f+eA)^2+H_f$ で、擬キンク(κ ≫ 1)の最小の模型を作り、(REG-W) の真の向きを疑う」筋(候補表 K8 (10))。2026-10-20、w_E05_406_regw_longshots = 書き下しの型、稿 `406_` §3 (10)・§4、C0 588)
- **閉じたもの**:**否定の筋の少数モード版**((REG-W) の真偽ではない;値【T88】)。
- **理由**:Fock の切断 12/16/20 で収束した 2 モードの 12 試行の $\kappa_{\max}$ は 0.25〜2.29(中央 1.13)。収束しない試行の大きな値(〜160)は切断の人工物。1 モードの解析:実のコヒーレントな第 2 構造は $\mathrm{Var}(\pi)$ が真空と同じ $c^2$ で $\langle T\rangle$ が等しく、$H_f$ だけ高い(反跳 $P_f$ の揺らぎが $A$ を打ち消す利得をちょうど相殺する)ので交差しない。一般の $\lambda T+V$ の 2 準位なら $\kappa\approx1.13/\epsilon$。
- **共通点(1 行)**:**PF 型の擬交差の相手は多モードの集団的な構造(光子数 $\gtrsim\lambda^{4/7}$)でしかあり得ず、少数モードの Fock の切断では作れない —— (REG-W) の真の向き(NUM-6800)の弱い支え。**
- **R9**:閉じたのは否定の筋の少数モード版。弱い結合・少数モード・1 次元射影に限る。**再開条件**:多モードの数値(MPS・HMC の梯子)で $E_0(\lambda)$ を擬交差の幅より細かく見る手段が入ったとき。

## F218(E05、全列の名指し (REG-W) を、**既存の閉鎖と同じ段の 6 型**で供給する方式(候補表 K8 の (1) Temple・Lehmann、(2) 和則の高次(TRK の $T$ 版・$H_f$ 版)、(5) Lieb–Thirring・相空間の殻ごとの $\chi_T$、(6) 区間演算 + 漸近、(7) 尺度変換の恒等式の 2 階、(8) 対称化・再配置・GHS 型の 3 階の符号)。2026-10-20、w_E05_406_regw_longshots = 書き下しの型、稿 `406_` §1・§3 (7)、成算 S209)
- **閉じたもの**:**方式**(照合だけで閉じた。新しい計算は (7) の言い換えだけ)。
- **理由**:(1) = F208 (a)(Kato 型 $\mathrm{Var}/d$;PF には隙間が無い);(2) = F207 (4)(和則は Jensen・CS で下界)と F207 (1)〜(3)(上界に要る交換子の表示の生成子は光子の拡大);(5) = F196;(6) = F197;(7) = F207 (2)(3)(2 階の応答は $F''$ と 1 次の量に戻る)。言い換えの観察 406-C:$\kappa\le2$ ⟺ 固定した $m$ で $\Lambda\mapsto E_0$ が凸 ⟺ 固定した Λ で $m\mapsto E_0$ が凸、$\kappa\le1$ ⟺ $\lambda F'$ が非減少。PF 型の 2 モードの玩具では κ=2.29 で破れる(C0 588 toy2)ので、構造の定理ではない。(8) = F211 (e)・F22・F175。
- **共通点(1 行)**:**6 型とも、既存の閉鎖の共通点(隙間の不在・下界の向き・尺度則の循環・殻の加法性・有限の計算は漸近を運ばない・正値性は大きさを与えない)のどれかに当たる。**
- **R9**:閉じたのは方式。**射程(T60)**:F196・F197・F207・F208・F211 の射程に従う。**再開条件**:同じ。

## F219(E05、全列(行 E1-H の内側)を (REG-W) を経ずに出すため、消費者 (I1)〔E05-P172 の (332-1)〕を**擬交差の近くで構造ごとに条件づけた形**に替える方式(族 K9)—— (a1) 2 構造への鋭い分解(ℓ=0 の 2 準位の射影、または $H_\theta$ の谷で切る)の各成分に一様ブースト、(a2) 連続な条件づけ $K=\frac12\lbrace f(H_\theta),B_w\rbrace$、$f\approx\eta_0/\max(H_\theta,\eta_0)$、(b) 2 構造の試行の線形結合で $G$ を下から、(c) 擬交差の点の集合の疎さ(396-D)と内挿の厳密化で擬交差の点の $f$ を両側の良い点の値で押さえる。2026-10-20、w_E05_408_consumer_redesign = 書き下しの型、稿 `408_REGW9_消費者の設計し直し_2026-10-20.md` §1・§2・§4、成算 S210)
- **閉じたもの**:**方式**(構造ごとに条件づけた消費者で (REG-W) を経ずに、台帳を増やさずに全列を出すこと)。全列・(REG-W)・(R-B) の真偽は閉じていない。
- **理由**:(0) 擬交差で落ちるのは命題 212-C の主項 $2\sigma^2$(一様ブーストの試行の比 $\langle H_\theta\rangle^2/\langle H_\theta^2\rangle$ の Cauchy–Schwarz)の 1 段だけ(稿 §1、404-B の字面の確定)。(a1) 条件づけた分散の上界にトンネルの極を除いた感受率と谷の重みの小ささ(量的な猫の構造)が要り、2 準位の縮約 = 擬交差の隙間の量(393 §3.4 (b)、F207〜F211 と同じ段)。(a2) **F116(稿 237)と同じ方式**:T1 は $(1-q)$ 型に消えるが、$[A,f]$ が $B_w\psi_0$ に作用する T6(放出のたびのシフトの配り直し)に (R-B) が要る。F116 の再開条件 (i) のうち $\nu\delta^2\to\infty$(393-T・298-D で $\ge c\lambda^{5/21}$)と (E-L″)(新しい補題 408-L・系 408-L1)は今の在庫で満たせるが、(R-B) は弱い形(目安 $R=o(\lambda^{10/21})$)でも在庫の評価($R\lesssim\lambda^{15/7}$、値)に $\lambda^{4/3}$ 以上届かず、改良は $\pi_z\psi_0$ の窓つきの $\int\rho x^{-2}$ の λ に一様な上界(ℓ=1 の赤外、F170・F171・F188 の ℓ=1 版)。(b) 試行を $\psi_0$ から作るには (a1) の分解か (a2) の条件づけが要り、独立の型でない。(c) 内挿の $f_i$ は交差点での構造ごとの値で、良い点の値へ運ぶには $f$ の λ についての連続性((LLC)・P201 の型、R9 寄り)か (a1) が要る。
- **共通点(1 行)**:**構造ごとの消費者は損(2σ²)を本当に消せるが、構造を見分ける操作(鋭い分解か $H_\theta$ による連続な条件づけ)が、前者は ℓ=0 の擬交差の隙間、後者は ℓ=1 の赤外の低帯(配り直しの費用 T6 の (R-B))に難しさを移す —— 消せない。**
- **R9**:閉じたのは方式。(a2) の残り「(R-B) の弱い形 ⟹ 全列」は (REG-W) を (R-B) に取り替える帰着で、台帳を減らさない(書き下していない;ラベルは稿 237 のまま、台帳に出さない)。副産物の補題 408-L は条件なし(self-audited)。
- **再開条件**:(1) $\pi_z\psi_0$ の窓つきの 2 次の逆モーメント $\int\rho(x)x^{-2}dx$ の λ に一様な多項式の上界($\lambda^{10/21}$ の余裕)が在庫に載ったとき —— そのとき F116 の方式が (REG-W) なしで全列を出す見込み(稿 237 の T1′〜T6′ を 408-L の尺度で書き直し、定義域 $K\psi_0\in Q(H(0))$ を補う);(2) 擬交差の隙間の量的な評価(F211 の再開条件 (1))が立ったとき、(a1) の条件づけた分散の上界が立つ。
- **射程(T60)**:禁じるのは「構造ごとに条件づけた消費者(鋭い分解・$H_\theta$ の関数による条件づけ・2 構造の試行の結合・疎な擬交差の内挿)で、(R-B) も擬交差の隙間の量も使わずに全列を出す」形の発注。止めないもの:(R-B) の弱い形の供給(ℓ=1 の赤外の上界);補題 408-L の監査と、その局在版(注 (ii))の改良。

## F220(E05、全列(行 E1-H の内側)を (REG-W) を経ずに出す道の供給側 (R-B)$_w$〔稿 409 の (ii) $X_1=\langle B_w\psi_0,H_\theta^{-3}\mathbf 1_*B_w\psi_0\rangle\to0$、(iii) $X_2\to0$〕を、**ℓ=1 の赤外の上界**で供給する方式 —— (a) 軟光子の放出の振幅(pull-through・Fröhlich・Hasler–Siebert 2023 の赤外評価)、(b) ℓ=1 の低帯に擬交差の問題が無いことの字面の照合、(c) F22・P118・369-A・366-A・P193 の組み合わせ、(c′) 経路測度の拡散定数の上界(Gauss 相関不等式)、(d) 保存済みの A1・2 殻 MPS の値。2026-10-20、hard_E05_rb_attack_72 = 難所の型、worklog (研究ノート: `2026-10-20_hard_E05_rb_attack_72.md`) §2、成算 S212、C0 592)
- **閉じたもの**:**方式**((a)(c)(c′)(d) の型で (ii)(iii) を λ に一様に供給すること)。命題 (R-B)$_w$・全列の真偽は閉じていない。(b) の字面は肯定(下記)。
- **理由**:(1) 原典 Hasler–Siebert 2023(Lemma 8〜13 を本文で照合)の赤外の評価は全て (15) $\lVert R_m(k)\rVert\le\omega^{-1}$ と (20) の $\lvert k\rvert e_m$ の項を通り、定数は $e_m=\lambda F$ の多項式 —— 408 R8 の $E_0/\lvert k\rvert$ の損と同じ段で、λ に一様な赤外の正則性の道具ではない。(2) TRK($G_{\rm sr}\le m/2$)を HS Lemma 10 (a) の積の形で、反跳の不等式 $D_0\le(1+\lvert k\rvert)(D_0(-k)+\lvert k\rvert)+\lvert k\rvert E_0+\frac\lambda2(\lvert k\rvert+k^2)$ と組むと $\lVert R(k)\pi_z\psi_0\rVert\le\frac12\lvert k\rvert^{-1/2}(1+o(1))$(369-A で横成分は $\lambda^{-1/2}\lvert k\rvert^{-1/2}$;C0 592 J1 で代数を検算)—— 在庫の $\delta/\lvert k\rvert$ の赤外の $1/a$ の損は消える。またセクターごとの点ごとの CS で $X_1\le16\eta_0^{-2}J$、$J=\int\lVert\Pi_\perp\partial_{k_z}(w\,a(k)\psi_0)\rVert^2d^3k$(光子数の因子なし)。しかし $\partial_kR=R(\lambda(\pi-k)_z-\hat k_z)R$ の $\lambda(\pi-k)R$ を作用素ノルム($\lVert\lambda^{1/2}(\pi-k)R^{1/2}\rVert^2\le2(1+F/\lvert k\rvert)$)で評価する段が残り、$J\lesssim\alpha\lambda^3F\ln\lambda$、$X_1\lesssim\alpha\lambda^{18/7}\ln\lambda$ —— 409 の在庫 $\alpha\lambda^{17/7}$ と同じ桁。(3) **損の正体**:$\lambda\pi R(k)$ = 速度 × 放出時間 $1/\lvert k\rvert$ を弾道的(速度一定)に数えること。速度の相関時間は $1/F$ で、拡散的な変位との比が損の因子 $\sqrt{F/\lvert k\rvert}$。速度の脱相関 = ℓ=1 のスペクトル測度の 2 次の逆モーメント(TRK・369-A は 1 次まで)。(4) 雑な計算(値):$I_0=\lVert B_w\psi_0\rVert^2=I_1/\bar x$、$I_1\approx\frac\lambda2\langle H_\theta^2\rangle$ で、(ii) ⟸ $\bar x\gg\lambda^{3/7}$;雲の変位の読み $B_w=H_\theta(Y-x)_z$ と虚時間の拡散 $\langle(Y-x)^2\rangle\sim\lambda\tau/h_{\rm eff}(\tau)$ で **(ii) ⟺(値)$h_{\rm eff}(1/\bar k)\bar k\gg\lambda^{3/7}$** —— 全列 $h\to\infty$ の量的な形(F116 R9 の灰色の具体化:(R-B)$_w$ は $h\gtrsim\lambda^{3/7}$ を含意する側の量)。(5) (c′):双極子では $W$ が経路の正の 2 次形式で Gauss 相関不等式により $E_\mu\lvert X_t-X_0\rvert^2\le3\lambda t$ が出るが、本物の模型では核の $e^{ik\cdot(X_s-X_t)}$ で $W$ が経路の凸関数でなく、動く経路ほど $W$ が小さい(相関の向きが逆)。(d):保存値に ℓ=1 の測度も $B_w\psi_0$ も無い(NUM-6808 の型)。
- **(b) の肯定(字面)**:ℓ=1 の低い状態は(ℓ=0 の構造)⊗(光子)でエネルギー ≥ 光子のエネルギー;擬交差の相手 $\psi_1\otimes\gamma_k$ は $\Delta+\lvert k\rvert\ge\lvert k\rvert$ で低帯を増やさない。(R-B)$_w$ は擬交差の隙間を要さない(409 §5 の読みと整合)。要るのは隙間でなく速度の脱相関。
- **難しさの保存**:(REG-W)(ℓ=0 の隙間)→ (R-B)$_w$(ℓ=1 の赤外)→「電子の速度の脱相関の λ に一様な評価」= 全列の量的な形。
- **限定**:判定は冪の勘定(値)と字面の照合。(2) の 2 つの不等式は厳密だが self-audited 未満(worklog に記録、PROVED 断片にしない)。C0 592 は有限玩具の代数の検算で、赤外の連続体・極限を検証しない【T88】。
- **再開条件**:(i) ℓ=1 のスペクトル測度の 2 次の逆モーメント $\int\rho_{\pi_z\psi_0}(x)x^{-2}dx$(窓・重みつき)の λ に一様な多項式の上界、または同値な「速度の自己相関の積分」$\int_0^\infty\lvert\langle\pi_z\psi_0,e^{-tD_0}\pi_z\psi_0\rangle\rvert t\,dt$ の上界が供給されたとき;(ii) 本物の模型の経路測度で拡散定数の上界 $E_\mu\lvert X_t-X_0\rvert^2\le C\lambda t$($t\le1$、λ に一様)が出たとき((c′) の GCI の非凸の障害を回避する道具);(iii) 全列の量的な形 $h\ge c\lambda^{3/7+\epsilon}$ が別の道で出たとき(そのときは (R-B)$_w$ は要らない —— R9)。

## F221(E05、全列(行 E1-H の内側)の量的な形 —— (R-B)$_w$〔稿 409 の (ii) $X_1\to0$〕の本体「電子の速度の脱相関(ℓ=1 の測度の 2 次の逆モーメント)」と「本物の模型の経路測度の拡散定数の上界」を、(A) 非凸 $W$ での GCI の代わり(場のモードで条件づけた Gauss の支配・Brascamp–Lieb/Caffarelli の縮小写像・α と核についての拡散定数の単調性・Lieb–Thomas 型の比較・双極子との比較不等式)、(B) ℓ=1 の閾値の LAP・Mourre(FGS 型)、(C) Green–Kubo・和則の補間(TRK と f-和則の高次)、(D) 定理 396-D の自然密度 1 を λ の正則性で全 λ に延ばす、(E) 保存済みの A1 の HMC の配位の値 の 5 型で供給する方式。2026-10-20、hard_E05_diffusion_72 = 難所の型、worklog (研究ノート: `2026-10-20_hard_E05_diffusion_72.md`) §2、成算 S213、C0 595・595b)
- **閉じたもの**:**方式**((A)〜(D) の型で (ii) を λ に一様に供給すること)。命題 (R-B)$_w$・全列の真偽は閉じていない。(E) は値を与えた(下記)。
- **理由(厳密な恒等式 + 雑な計算 + 値)**:(1) **拡散の恒等式**(worklog §2.1 (A-0)、厳密、C0 595 J1 で代数を検算):$P=0$ の経路測度で $E(t):=E_\mu[(X_t-X_0)_z^2]=\lambda t-2\lambda^2\int_0^t(t-\tau)C(\tau)d\tau$、$C(\tau)=\langle\pi_z\psi_0,e^{-\tau D_0}\pi_z\psi_0\rangle\ge0$。ゆえに $E(t)\le\lambda t$ は本物の模型でも**自明**(GCI も $W$ の凸性も要らない;F220 の再開条件 (ii) の字面は $C=1$ で既に成立)、$E$ は凹、$E(t)=\lambda t/h_{\rm sr}+2\lambda^2\int\min(\tau,t)C$、速度の脱相関の積分 $2\lambda^2G_2$ は自由拡散からの**切片**で、拡散定数の上界では捉えられない。(2) **要る量の再特定**(値):$B_w\psi_0=\sum_iw_i^2(y_i-x)_z\psi_0$ の可干渉の和で $I_0=\lVert B_w\psi_0\rVert^2\approx\nu_*^2E(1)$(窓のエネルギーは $\lvert k\rvert\sim1$ の光子が運ぶ)、ゆえに (ii) ⟺ $E(1)\ll\lambda^{4/7}$ ⟺ $h_{\rm eff}(1):=\lambda/E(1)\gg\lambda^{3/7}$;切片の値は $\lambda/F\sim\lambda^{2/7}$ で無害なので**律速は $h_{\rm sr}$(TRK の和則の飽和 $1-2\lambda G_{\rm sr}\ll\lambda^{-3/7}$)であって赤外ではない**(発注の推論 1「律速は赤外の低帯」を否定)。(3) **(A)**:5 枝はどれも「$E\le C\lambda t$ 型」(自明で不足)か「$E^{\rm real}\le E^{\rm dip}$ 型」に落ち、後者は 237-3($I_0\ge\nu^2\lambda/(8F)$、厳密)の読みで $E(1)\gtrsim\lambda/(8F)\sim\lambda^{2/7}\gg1/\alpha\approx E^{\rm dip}(1)$ なので向きが偽(本物の電子は双極子より速く拡がる —— 自己エネルギー $F\ll\alpha\lambda$ と同じ機構)。道具は自由拡散との比較(上界)しか返さず、要るのは $h$ の下界(F213 の共通点の再現)。(4) **(B)**:$[H,iA]$ の反跳の項 $\lambda\pi\cdot P_f\sim\lambda^{6/7}\lvert k\rvert$ が $H_f$ を圧倒し Mourre の定数は λ で悪化;LAP は特定のベクトルの重みを与えず、重みは $B_w\psi_0$ の拡がりそのもの(F182 (3)・F207 (b) の段)。(5) **(C)**:負のモーメントの補間は下界のみ($I_{-2}\ge I_{-1}^2/I_0\sim\lambda^{-12/7}$、要る上界は $\lambda^{-10/7}$)、$x^{-2}$ の重みは 369-A の 2 次の正値性から出ない(F218 (2)・F182 (c))。(6) **(D)**:(I1) 型の消費者の率の天井は $\lambda^{-1/14}$(396-W の平均 $\lambda^{-1/7}$)で、要る $\lambda^{6/14}$ に $\lambda^{5/14}$ 届かない;$h$ の λ 正則性は在庫に無く、$h_{\rm eff}(1)\le h_{\rm sr}$ で向きも違う。P206〜P209 の十分形は全て同じ段。(7) **(E)(値【T88】、C0 595b)**:571_partial(A1 の HMC、α=1、T=6)の $V(\ell)$ は平均 2 乗変位 = $E(t)$ そのもので、$h_{\rm eff}(1)$ = 2.00・2.51・3.32(λ=32・64・128)、$h_{\rm eff}(1)/\lambda^{3/7}$ = 0.453・0.422・0.414(減少)、局所冪 0.33→0.40(増加、3/7=0.43 に近づく途中)—— (ii) は**境界上で否定寄り**。
- **共通点(1 行)**:**(R-B)$_w$ の (ii) は、全列の結論(409-P の率 $\lambda^{-1/14}$、$h\gtrsim\lambda^{1/14}$)より $\lambda^{5/14}$ 強い量的な全列($h_{\rm eff}(1)\gg\lambda^{3/7}$)を値で前提する —— F116 R9 の「灰色」は黒(同値変形より強い仮定)。供給の道は量的な全列を先に証明する以外に無い。**
- **難しさの保存**:(REG-W)(ℓ=0 の隙間)→ (R-B)$_w$(ℓ=1 の赤外)→ 速度の脱相関(410)→ **TRK の和則の飽和 $1-2\lambda G_{\rm sr}\ll\lambda^{-3/7}$ の全 λ での証明**(本件)。
- **限定**:(2) の可干渉の和 $I_0\approx\nu_*^2E(1)$ は値の読み(厳密な下界 $I_0\gtrsim\nu^2E(1)$ は経路の CS が逆向き $I_0\ge\Theta_t^2/E(t)$ しか与えず、予算内で出ない)。(1) の恒等式は厳密だが self-audited 未満(worklog に記録、PROVED 断片にしない;稿にするなら 373-A の設定での $\xi$ の 2 階の正当化が要る)。(7) は α=1・T=6・λ≤128 の限定。
- **再開条件**:(i) $h_{\rm sr}\ge c\lambda^{3/7+\epsilon}$(または $h_{\rm eff}(1)\ge c\lambda^{3/7+\epsilon}$)が全ての大きな λ で出たとき(そのときは (R-B)$_w$ も 409-P も要らない:全列が直接閉じる —— R9);(ii) 可干渉の和の厳密な上界 $I_0\le C\nu_*^2E(1)+o(\lambda^{12/7})$ が出たとき(そのときも (ii) は $h_{\rm eff}(1)\gg\lambda^{3/7}$ に帰着するだけで、供給は (i) に戻る);(iii) A1 の鎖を λ=256 以上で伸ばして $h_{\rm eff}(1)$ の局所冪が 3/7 を明確に越えたとき(値の再評価のみ)。

## F222(E05、全列(行 E1-H の内側)の設計のやり直し第 3 版 —— **模型固有の構造を使う十分条件の候補表 N1〜N8・N10**:(N1) 擬交差の 2 構造の ℓ=1 応答の非混合($G$ の内挿)で消費者 (I1) の $2\sigma^2$ を避ける、(N2) $\lambda\langle T\rangle$ の λ 単調性を殻の応答の反磁性で、(N3) (α, λ) の 2 変数の同時凹性(PSD 錐)、(N4) 殻の写像の不動点の安定性、(N5) 配位ごとの運動量のずらし(TRK の飽和の直接評価)、(N6) Ward 恒等式・Lorentz 力の和則で負のモーメントを補間、(N7) 指数型族の共分散で $E(t)$ の λ 正則性、(N8) Karamata 型($M$ の単調性 + 密度 1)、(N10) $G$ の下半連続性。2026-10-20、hard_E05_strategy3_72 = 難所の型、稿 `415_全列の設計第3版_模型固有の構造_2026-10-20.md` §3〜§4、成算 S214・S214a〜j)
- **理由**:(N1) 交差項 $\langle\pi_z\psi_1,D_0^{-1}\pi_z\psi_2\rangle$ の在庫の上界は CS の $\sqrt{G_1G_2}$ で主項と同桁;小ささは 2 構造の間の ℓ=1 の行列要素 = トンネル振幅の量(F211 (1)、F219 (a1)、F220 (b) と同じ段)。(N2) 尺度則 $\Lambda\partial_\Lambda E_0=E_0+\lambda\langle T\rangle$ で単調性 ⟺ $\kappa\le1$ = (REG-K) の言い換え(R9;F207 (a))。(N3) 模型は PSD 錐の縁(線織面)で、縁の線分は射線だけ;中点は $A^2$ の質量項を足した別の模型で、$F(\lambda,e)$ に 1 変数の凹性以外を課さない(393-C = F204 の 2 変数版、406-U1)。(N4) 在庫は積の試行と超加法性だけで、縮小は F170 (iii) 再開条件 (2) そのもの。(N5) 配位ごとのずらしは 237・409 の流れで、誤差が $X_1,X_2$(409-P)か $2\sigma^2$(212-C、F219 (0))。(N6) $\ln I_j$ の凸性から負のモーメントは下界のみ(F221 (C))。(N7) 共分散の各点の上界 = F213 (a) の分散の量。(N8) $M$ 非減少でも $M'$ の各点は縛れず、A-411-1 が満たす(406-U1)。(N10) $f_{\rm sr}$ は上半連続で、上向きの孤立した瘤を許す(向きが逆)。
- **閉じたもの**:方式(10 角度)。標的(全列)・命題の真偽は閉じていない。消費者の最弱の形は観察 415-A(稿 §2:396-D で窓を相対幅 $\lambda^{-1/7+2\gamma+\epsilon}$ に狭める)で、(REG-L) の鋭い閾と一致 —— 消費者の側の余地はそこで尽きる。
- **R9**:閉じたのは方式。難しさは消えずに「巨視的に異なる 2 つの ℓ=0 構造の間のトンネル振幅(隙間、または ℓ=1 の交差項)の λ の冪での量的な評価」(F211 (1) と同じ量)に留まる。**11 族の共通点**(稿 §1):各点の 2 階の量の上界を、$F$ だけの道具(406-U で凹性に退化)か下界・平均の向きの道具で狙い、トンネル振幅の量的な入力を持たなかった。
- **射程(T60)**:禁じるのは「N1〜N8・N10 の型で (REG-W)・(R-B)$_w$・全列を出す」発注。止めないもの:トンネル振幅(隙間・ℓ=1 の交差項)を量的に評価する新しい入力が立ったときの N1 の再開;反証の側(N9、稿 §5)の値の照合(412a・310);F210 の行の残り半分($h$ の上半連続性)。
- **再開条件**:(1) F211 (1)(2 構造の間のトンネル振幅の量的な評価 —— 上からでも下からでも)が在庫に載ったとき(N1 と N2 が再開);(2) 412a・310 で $F$ か $\langle T\rangle$ の局所冪に 1/4 オクターブ以下の幅の段が見えたとき(反証の側 N9 の第 1 手:平均場の 2 極小の交替の検証)。

## F223(E05、全列(行 E1-H の内側)の名指し (REG-W)〔$F\in C^1$ ∧ $\kappa p\tilde Q\to0$;十分形 (REG-L)〕に要る「擬交差しうる 2 つの ℓ=0 構造の間のトンネル振幅の量的な下界」(F211 (1)・F219 (2)・F222 N1 の再開条件)を、**半古典の二重井戸のトンネルの型**で供給する方式 —— (a) Agmon 型の指数減衰とその逆向き(Carleman・一意接続の量化)、(b) instanton(Feynman–Kac の明示の経路による Jensen の下界)、(c) Helffer–Sjöstrand・Simon 1984 の二重井戸の分裂の漸近 + 集団座標への縮約、(d) Harnack・Li–Yau・Wang の log-Harnack による熱核の下界。2026-10-20、hard_E05_tunnel_72 = 難所の型(利用枠切れの後、w_E05_418_tunnel_finish_nft = 書き下しの型 が締めた)、稿 `417_全列_トンネル振幅の道具の旅_2026-10-20.md` §1〜§2、成算 S215)
- **閉じたもの**:**方式**(トンネル振幅の冪の下界を半古典・正値性の量化の型で出すこと)。(REG-W)・全列の真偽、擬交差の存在・不在は閉じていない。
- **理由**:(0) **向きの判定**(稿 §1、値【T88】):障壁で隔てられた 2 構造の擬交差では半古典の作用 $S\asymp2\sqrt{\Delta N\,B/\bar\omega}$、巨視的な $\Delta N\gtrsim\lambda^{4/7}$ で $S\gg\ln\lambda$ ⟺ 障壁 $B\gg\lambda^{-4/7}(\ln\lambda)^2$;ゆえに $t\lesssim E_0e^{-c\lambda^{4/7}}$ で、要る $t\gg\alpha\lambda^{2/7}$〜$\alpha\lambda^{3/7}$(404-A)に**下界の道具は原理的に届かない**(冪的になるのは 2 極小が量子揺らぎの中で 1 つに溶けて擬交差でないときだけ)。(a) 上界(光子数の指数モーメント)は向きを支えるだけ;下界は無限次元の Carleman 評価が在庫・標準の文献に無く、在っても $e^{-C\Delta N}$(F211 (a) と同じ段)。(b) 経路の下界はコヒーレント状態の重なり $e^{-\lVert g_1-g_2\rVert^2/2}$ が上限で指数的(F213 (a)・F175 と型は別、止まる段は (a))。(c) 出るのは指数的に小さい分裂の精密な漸近($e^{-d_{\rm Agmon}/h}(1+O(h))$、$h=1/N$)で偽の向きの精密化だけ;無限次元の断熱縮約は F170 (iii)・F171 の段(1%)。(d) $n=\infty$ で Li–Yau は空、log-Harnack は曲率の下界(F175 (i)、反跳の非凸部分で落ちる)が要り、出ても Cameron–Martin 距離の Gauss 型で指数的。(e) 玩具 C0 597(3 モード)・597b(2 モード)は切断で不安定、$\Delta N\le2.2$ 光子 —— 少数光子では障壁で隔てられた第 2 構造が立たず、向きは未決(406 §3 (10)・F217 と同じ)。
- **共通点(1 行)**:**半古典・正値性の量化の下界はどれも 2 構造の重なり(障壁の作用)で指数的に小さく、λ とともに増える隙間を要する (REG-W) の閾に原理的に届かない —— 障壁で隔てられた擬交差が在れば (REG-W) は偽で、在らなければ障害そのものが無い。**
- **R9**:閉じたのは方式。難しさは「トンネル振幅の量的な評価」から「障壁で隔てられた ℓ=0 の 2 構造の擬交差が λ 大で無いこと」(NFT、厳密な形は補題 417-B・系 417-B1:$\langle T\rangle_{\psi_\lambda}$ の急な落ちの不在)へ移った —— 消滅ではない。
- **射程(T60)**:禁じるのは「トンネル振幅(擬交差の隙間)の冪の**下界**を Agmon・instanton・二重井戸の漸近・Harnack の型で出す」発注。止めないもの:擬交差の**不在**を直接示す型(平均場・準自由の汎関数の極小の一意性と安定性、$F'$ の凸性〔404-G〕など;後続 `w_E05_418_tunnel_finish_nft`);(ii) の内挿の厳密化(F220 再開 (i) と同じ量)。
- **再開条件**:(1) 2 構造の間の中間状態の 1 段の比 $r\ge1$(障壁なし)を λ に一様に示す結合の量的な評価が在庫に載ったとき(そのとき擬交差は鋭くならない);(2) F220 の再開条件 (i)(ℓ=1 の測度の 2 次の逆モーメントの λ に一様な多項式の上界)が満たされたとき((ii) の内挿の道が開く)。

## F224(E05、全列(行 E1-H の内側)の名指し (REG-W) と同値な **(NFT$_{\rm s}$)**〔系 417-B1:$\langle T\rangle_{\psi_\lambda}$ の落ちの率 $R(\lambda_-,\lambda_+)$ の窓の上の sup → 0;物理の読み (NFT$_{\rm p}$)「λ 大で障壁で隔てられた ℓ=0 の 2 構造の擬交差が無い」〕を、**擬交差の不在を直接示す型**で供給する方式 —— (a) 平均場・準自由の汎関数の最小化子の一意性 + 強圧性(Lieb 1977・Lenzmann 2009・Frank–Seiringer 2019 の型)、(b) 厳密な凸性(コヒーレント・準自由の多様体、測地凸、λ についての $F'$ の凸性)、(c) Lee–Yang・Griffiths 型の解析性と Kato–Rellich、(d) 単調性・変分の比較。2026-10-20、w_E05_418_tunnel_finish_nft = 書き下しの型、稿 `418_NFT_構造の擬交差の不在_2026-10-20.md` §3、成算 S216)
- **閉じたもの**:**方式**((NFT)・(REG-W)・全列の真偽ではない;値は真の向き)。
- **理由**:(a) PF の文字どおりの平均場(コヒーレント)は $g=0$ が唯一の最小で $\asymp\alpha\lambda\gg E_0$(補題 418-C)—— 基底状態を近似しない;有効の汎関数は少なくとも準自由の段で、Wick の 4 次が不定符号の非凸の問題、Lieb の対称再配置・Lenzmann の動径 ODE は型が合わない;さらに (NFT$_{\rm s}$) を割るのは $S\gg\ln\lambda$ の任意の障壁の擬交差で揺らぎの尺度 $\sqrt N$ の構造まで排除が要り、強圧性の型では Bogoliubov の精度(絶対誤差 $O(1)$)の縮約と λ に一様な非退化が要る —— Pekar で Frank–Seiringer 2019 の水準、PF ではその前段が F115 の再開条件(強結合の準自由近似の妥当性)で 2%。(b) コヒーレントでは凸性は成るが自明;準自由では凸でない;状態の上の凸性(線形)は λ 依存を言わない;λ の凸性は 404-G の仮定で F187 (K2)・F212 再開 (1) と同じ段(1% 未満)。(c) Lee–Yang・GHS は F212 (b) と同じ段;Kato–Rellich は $E_0$ が連続スペクトルの底で孤立しない(F198)、光子質量では半径 ≲ $m_{\rm ph}$;Cauchy で要る帯の半幅 ≫ λ は擬交差の不在の言い換え(0)。(d) $F$ だけの道具は凹性に退化(406-U);最良の 403-A(E05-P206)は $R\lesssim\lambda^{-1/7}/s$ で相対幅 $\gg\lambda^{-1/7}$ の窓だけ;409-A〜C は ℓ=1 の消費者の側(0)。値:412a の partial(C0 598)・4 モードの玩具の準自由の縮約(C0 598b)に跳びなし【T88】。
- **共通点(1 行)**:**(NFT$_{\rm s}$) を割るのは任意の障壁の擬交差で、揺らぎの尺度の構造まで排除せねばならず、どの道具も「Bogoliubov の精度の縮約」か「相対幅 $\lesssim\lambda^{-1/7}$ の窓の各点の情報」を要る —— 在庫は平均(396-W)・広い窓(403-A)・定性(一意性・正値性)までで狭い窓に届かない。**
- **R9**:閉じたのは方式。難しさは「準自由(相関)の段の有効汎関数の同定・一意性・非退化と、それへの Bogoliubov の精度の縮約」に移った(F115 の再開条件と同じ場所)—— 消滅ではない。
- **射程(T60)**:禁じるのは「古典(コヒーレント・Pekar 型)の汎関数の一意性で擬交差を排除する」「Lee–Yang・Kato–Rellich を λ に当てる」「変分の比較・$F$ だけの道具で狭い窓の落ちを押さえる」発注。止めないもの:準自由の段の有効汎関数の同定と、その一意性・非退化の数値の偵察(有限モードでなく連続の殻での準自由の変分);F115 の再開条件の族。
- **再開条件**:(1) F115 の再開条件(強結合の 4 次の反跳項をもつ基底状態の準自由近似の妥当性)が Bogoliubov の精度で満たされ、かつ縮約先の汎関数の最小化子の一意性・非退化が示されたとき;(2) λ についての $F'$ の凸性(404-G)の供給が立ったとき(F211 再開 (2)・F212 再開 (1) と共通)。

## F225(E05 の外・難問 #1 の残る壁 (iii-1) 一意性・(iii-2) 非退化〔くりこみ族 $m_0h_{\rm ls}(\lambda_0)=m_{\rm ph}$ に沿う分散関係 $\mathcal E_\Lambda(p)=E_\Lambda(p)-E_\Lambda(0)$ の極限、366 §6.2〕を、(a) $a=\lvert P\rvert^2$ についての凹性で 1 点の下界に縮める、(b) 1 点 $p_1$ の下界(光子放出の費用・逆向きの Lipschitz・TRK)、(c) 凹性・曲率の条件 $\mathcal E''(0)=1/m_{\rm ph}$ からの一意性、(d) CFP 2009・HH 2008 の固定の切断・小さい α の結果の移送、で出す方式。2026-10-20、w_E05_419_p1_nondeg = 書き下しの型、記録 (研究ノート: `2026-10-20_w_E05_419_p1_nondeg.md`) (0)-1〜(0)-6、成算 S217)
- **閉じたもの**:**方式**((iii-1)・(iii-2) の真偽、$\lvert P\rvert^2$ の凹性 (LC-PF) の真偽は閉じない)。
- **理由(厳密 + 字面 + 原典)**:(1) **整合模型(厳密、初等)**:$g_m(p)=\frac{p^2}{2m}$($\lvert p\rvert\le m$)、$\lvert p\rvert-\frac m2$($\lvert p\rvert\ge m$)、$f_\Lambda=\min(g_{m_{\rm ph}},\Delta_\Lambda+g_{M_\Lambda})$、$\Delta_\Lambda\downarrow0$、$M_\Lambda\uparrow\infty$ は、366-A(1-Lipschitz・$0\le\mathcal E\le\lvert p\rvert$)・E05-F23・くりこみ条件($a\lt2m_{\rm ph}\Delta_\Lambda$ で $f=\frac{p^2}{2m_{\rm ph}}$)・裸の上界 $\le\frac{p^2}{2m_0}$・HH 2008 Prop. 2 の型の凹性($f-\frac{p^2}{2m_0}$ が $p$ に凹)・**$a$ についての凹性**を全て満たし、$f_\infty\equiv0$(崩壊);偶奇で $g_{m_{\rm ph}}$ と交互に取れば部分列の極限が 2 つ —— (a)(c) は在庫 + 凹性からは出ない。(2) (b):FK で $\mathcal E(p_1)=\lim_T-\frac1T\log\hat{\mathbb E}_T[\cos(p_1\cdot\Delta b_T)]$、族に一様な 1 点の下界 ⟺ 窓増分の特性関数の一様な指数減衰 = F180 の共通の段;光子放出・移動不等式・CFP (I 4) の $E_{P-k}\gt E_P-C_\alpha\lvert k\rvert$ は $\mathcal E$ の上界の向き;大きな $p$ の粗い下界 $E(\xi)\ge(\lvert\xi\rvert-\frac m2-C/\epsilon)/(1+\epsilon)$ は発散する $E(0)$ を $O(1)$ で引けない;TRK・和則は $\psi_0$ の巡回部分空間の量で $\inf\sigma(H(p))$ を下から押さえない(F182 (4))。(3) (d):CFP 2009 Thm III.1(本文照合)は「Λ ≈ 1 固定、α 十分小」、域 $S=\lbrace\lvert P\rvert\lt1/3\rbrace$ は裸の質量の単位で、族の上では物理の $\lvert p\rvert\lt m_{\rm ph}/(3h)\to0$;HH 2008 は $E-\xi^2$ の凹性と「large ξ で $E=\lvert\xi\rvert+O(1)$」(定数は Λ に依る)で、$\lvert P\rvert^2$ の凹性は主張せず、著者自身が紫外に依る小さい結合の結果は足りないと注記。
- **値の裏づけ(【T88】)**:(研究ノート: `599_w_E05_419_consistency_and_oneloop.py`)(0.4 s):J1 CONSISTENT+COLLAPSES(整合模型の検算)、J2 BARE_SCALE(1 ループの $q$ 依存の自己エネルギー $D(q)\to\frac{2\alpha}\pi J(q)$ は λ に依らず、族の上の窓は $h^{-3/2}$ で潰れる —— 1 ループの崩壊の機構)、J3 ONELOOP_QUARTIC_EXCLUDED(NUM-3940 の 4 次 $a_2=0.0036\pm0.0073$ は 1 ループの 0.170 から 22.8σ、着衣の尺度 $\frac1{2h^3}\approx0.0038$ と同じ桁)。閉鎖の理由は (1)〜(3) で、値は使わない。
- **共通点(1 行)**:**凹性・曲率の条件・Lipschitz・天井・HH 型の凹性はどれも $\mathcal E$ を上から押さえる型か形の制約で、崩壊する整合模型を排除できない;下からの評価は「窓増分の特性関数の一様な指数減衰」(F180・F182)か「発散する $E(0)$ を $O(1)$ で引く精度」(曲率の評価、FR-G3-9)に落ちる —— F180〜F184 と同じ段。**
- **R9**:閉じたのは方式。双極子(366 §5)では族が終端し段は空;固定の Λ・小さい α では CFP (I 3) で非退化が立つ —— 障害は「族に一様」の側に局在し消滅していない。
- **射程(T60)**:禁じるのは「$\lvert P\rvert^2$ の凹性・$P$ についての単調性・曲率の条件・Lipschitz・天井だけで (iii-1)/(iii-2) を出す」「固定の切断・α 小の結果(CFP・HH・Fröhlich 型)を族に移す」形の発注。止めないもの:(LC-PF) そのものの証明(難問 #1 の非退化には十分でないが、上側の放物線 $\mathcal E_\Lambda\le\frac{p^2}{2m_{\rm ph}}$ と「1 点 ⟺ 全て」を与える);窓増分の特性関数の一様な指数減衰の評価(F180 の再開条件);族に沿う 2 点以上の λ での 4 次の係数の値(類 C の値)。
- **再開条件**:(1) F180 の再開条件(反集中・特性関数の減衰の道具);(2) Λ についての単調性(F170);(3) 「崩壊する整合模型」を排除する下からの入力 —— 例えば $\mathcal E_\Lambda(p)\ge c\,\mathcal E_\Lambda(p')$ 型の 2 点比較で族に一様なもの、または fiber $p$ の下端の「重い枝」(エネルギー $E(0)+\Delta$、$\Delta\to0$、質量 $M\to\infty$)の排除。

## F226(E05、難問 #3 = HP-G3-1 の Q3 の冪の隙間 —— 下界の冪 $\lambda^{1/14}$(密度 1)を (L1) 396-W の望遠鏡和の改良・(L2) 395-B の各点の不等式の率の改良・(L3) 393-T (ii) の量的な形・(L5) $h_{\rm ls}$・$h_{\rm eff}(t)$ で出す、上界の冪 2 を (U1) P118 の試行 η の改良と雲の相関・(U2) $h_{\rm sr}$ と $h_{\rm ls}$ の差・(U3) 拡散の恒等式 (A-0) で下げる方式。2026-10-20、w_E05_421_p3_growth = 書き下しの型、稿 `421_難問3_増大則の冪の隙間_2026-10-20.md` §2.2・§4、成算 S219)
- **閉じたもの**:**方式**(上の 7 候補)。命題(真の冪)は閉じていない。下界側の残り 1 候補 (L4)「密度 1 を捨てる」は定理 421-1(下対数密度 ≥2/7 で $\gamma\lt\frac16$、self-audited)に結実。
- **理由**:(1) **下界の構造**(補題 421-A・396-W):(I1) の余り $C_1\lambda^{-1/14}$ は窓の釣り合い(319-B の縁の損 $\propto c\lambda/M$ と勾配の費用 $\propto1/(cM)$)の最小値 $\lambda^{1/2}/M$ に $M\ge c_1\lambda^{4/7}$ を入れた値で、396-W の 2 進平均の $v_f\lesssim\lambda^{1/2}/M$ も同じ量 —— 鎖の率は $M/\lambda^{1/2}$ の冪だけで決まる(観察 421-C)。(L1)(L3) は $M$ の下界の冪 = $F$ の局所冪の片側評価 = 難問 #2(F205 の段);(L2) は同じ量か、319-B の縁の評価の改良 = (EDGE) の族(F123・F146・F150・F151・F163)の段;(L5) は $h_{\rm ls}\ge h_{\rm sr}$ で下界が移るだけ、$h_{\rm eff}(t)\le h_{\rm sr}$ の下界はより強い主張で道具なし。(2) **上界の構造**:冪 2 は 369-1 の $\Phi_c$ で、反跳の各 $k$ に TRK 型 369-A($\le m$)を $\lvert k\rvert\le\Lambda$ 全体で当てた形。(U1) は $u_k=P(k)Q\psi_0$ の負のモーメントの上界 = 反集中(F182 (c))、雲の相関は $\mathrm{Var}_\mu(D_hV)$ の CS を超える下界(373-A、F184 の段);(U2) は $h_{\rm sr}\le h_{\rm ls}$(P198)で向きが逆、$h_{\rm ls}$ の上界は道具なし(367 §0 (a)(i));(U3) (A-0) は Green–Kubo(367-A)の t 形で、要る長時間の $e(t)$ の下界は Cramér–Rao(367-B)そのもの。
- **共通点(1 行)**:**下界は「$M$ の下界の冪」(在庫の両側の冪と凹性から全ての λ で 4/7、オクターブの 2/7 で 2/3)、上界は「$\lvert k\rvert\sim\Lambda$ の反跳のスペクトル測度の反集中」で止まる —— どちらも新しい入力(F の局所冪の片側評価、または低エネルギーの重みの量的な評価)が無い限り、和則・変分・窓・望遠鏡和・Green–Kubo・Cramér–Rao の組み替えでは動かない。**
- **値(【T88】、C0 601)**:$h_{\rm sr}$ の局所冪は λ=64〜128 で 0.55〜0.6(上昇中)—— 下界の鎖の絶対の天井 3/14(316-1、観察 421-C)の上、上界の冪 2 の下。
- **再開条件**:(i) $F$ の局所冪の片側評価(難問 #2、例えば全ての λ で $M\ge c\lambda^{4/7+\mu}$)が在庫に載ったとき((L1)〜(L3) が再開、率 $\frac1{14}+\mu$);(ii) 縁のエネルギーの割合の冪の上界(319-B の改良)と $v_f$ の各点の冪が出たとき((L2)、天井 3/14 を越える);(iii) F182 の反集中か F184 の分散の下界が出たとき((U1))。

## F227(E05、難問 #2(HP-G3-1 の Q2):自己エネルギー $E_0$ の冪を、(上界側)交差項 $\langle H_{\rm o}\rangle$ が負の試行で 5/7 より下げる —— (U1) スクイーズ(Bogoliubov)の雲(変位つきを含む)、(U2) 電子の運動量と光子の相関(LLP 型の変換の後の試行・PZW 型の着衣による追跡)、(U3) 奇の成分を入れたコヒーレント状態の重ね合わせ、(U4) 殻ごとに位相をずらした試行 —— と、(下界側)2/3 の固定点を F181 と別の段で破る —— (L1) 偶模型の底(E05-P194)と奇の割合の組み合わせ、(L2) 393-T の三分法の (ii) の量 $\tilde Q$・$M$、(L3) 395-B の各点の不等式の逆向き、(L4) 交差項の符号を下界の鎖に入れる(365-A の逆)—— 方式。2026-10-20、w_E05_420_p2_exponent = 書き下しの型、worklog (研究ノート: `2026-10-20_w_E05_420_p2_exponent.md`) §1・§2・§4(稿なし、(0) で停止)、成算 S218)
- **閉じたもの**:**方式**($E_0$ の冪・(LL-low$_{2/3}^+$)・(δ-FRAC)・(NC-A$_\eta$) の真偽ではない)。
- **理由(厳密 + 値)**:上界側 —— (U1)(U3) コヒーレント状態 $W(\beta)\Omega$ は $\langle H(0)\rangle=\langle H(0)\rangle_\Omega+\frac1{2m}(\lvert P_c+ea_c\rvert^2+\int k^2\lvert\beta\rvert^2)+\int\omega\lvert\beta\rvert^2$ で真空以上(観察 420-A:横波性 $k\cdot\varepsilon(k)=0$ で揺らぎの交差が消え、交差項は平均場 $\lvert P_c+ea_c\rvert^2$ に畳まれる);平均 0 の準自由状態 $S$ の変位 $W(\beta)S$ は、交差項の揺らぎの部分が運動量の移り $\lvert k\mp k'\rvert$ で重みづけた $S$ の核だけで決まり、変位の利得は $S$ に残った $\frac{e^2}{2m}\langle A(0)^2\rangle_S$ 以下(観察 420-B′);局在 ℓ の相関では利得 $\sim\lambda\alpha n/\ell^2$ が自身の反跳 $\sim\lambda n/\ell^2$ の O(α) 倍で λ の 1 次(値)。真空の近くの奇の混ぜ $\Omega+\epsilon a^*(f)\Omega$ は 1 次の交差が 0;有限個のコヒーレント状態の重ね合わせは重なりで非対角が抑えられ、個数を増やすと族の制限が消える。(U2) PZW 型の着衣は λ の 1 次の係数だけを動かし(α≳10 まで利得なし、値)、残りの $B$ の圧搾は $\alpha^{1/7}\lambda^{5/7}$(394 §2.2)。(U4) $U_\theta=e^{i\sum_s\theta_sN_s}$ は $P_f$・$H_f$・パリティと可換で 365-A (i)〜(iii) の族を保つ(厳密);一般の状態では殻の分割の尺度不変(323-B)で冪は動かない。下界側 —— (L1) 要るのは奇の割合の**上界**で (δ-FRAC) そのもの(F181 (0));(L2) $M=\varphi F$、$\tilde Q=\alpha\lambda/(\varphi^3F^2)$ は $F$ の関数形だけで決まり整合模型 $F_0=c\alpha^{1/3}\lambda^{2/3}$ が満たす(F181 (b));物理の入力が入る形は観察 420-C(冪 > 2/3 ⟺ $\varphi=\langle H_f\rangle_0/E_0$ の対数平均が 1/3 を割る)だけで、それは 298-D の鎖の冪則を破ることを要する(F161 (1)・323-B);(L3) 逆向きの不等式は $f\le1$ と組んで $F$ の曲率の上界になるだけ(F181 (b));(L4) 符号 $\delta\ge0$ は偶の量の下界で鎖の予算に対し向きが逆、効くのは $\delta$ の上界 = (δ-FRAC)。
- **値の裏づけ(【T88】)**:(研究ノート: `600_w_E05_420_crossterm_check.py`)(PASS:箱の有限モードで並進不変なら揺らぎの交差 $X=0$〔3.4e-17〕、一般の状態で 0 でない〔中央値 0.16〕)。閉鎖の理由は横波性の恒等式と在庫の段の照合で、値の大きさは使わない。
- **共通点(1 行)**:**横波性 $k\cdot\varepsilon(k)=0$ により、交差項の揺らぎの部分は運動量を移す相関でしか生じず、その相関は反跳を加算的に払う —— 交差項で利得を出す試行は光子の全運動量と $A(0)$ の集団のもつれ(300-C の (II) 型の追跡)しか残らず、下界側の新しい形(420-C の光子の割合 < 1/3)も鎖の極値の配分 1/3 で同じ固定点に当たる;F161 (1)(3)・F164 (b)・F181・S178 と同じ段。**
- **R9**:閉じたのは方式。双極子では交差項が無く(段は空)、障害は反跳と $A(0)$ のもつれに局在し消滅していない(F181 と同じ)。
- **射程(T60)**:禁じるのは「コヒーレント状態・平均 0 の準自由状態の変位・PZW 型の着衣・殻の位相・有限個のコヒーレント状態の重ね合わせ」を試行にして 5/7 を割る形、および「奇の割合の下界・$\tilde Q$ の上下界・395-B の逆向き・$\delta$ の符号」で下界を 2/3 より上げる形の発注。止めないもの:光子の全運動量と $A(0)$ の集団のもつれを率つきで作る試行(S178 の破れる条件);$\langle H_f\rangle_0\le(1/3-c)E_0$ を連続体の入力で出す角度;値の側(394 §8.4 の α=1/4・1/2 の 6 セル、392 の α=2・4 の部分が済んだ後の $q$・$Z$)。
- **再開条件**:(1) 集団のもつれの試行の族で $-\langle H_{\rm o}\rangle\ge(1-o(1))\langle H_{\rm e}\rangle$ を明示に満たすもの(F172・S178 と共通);(2) 光子のエネルギーの割合の上界 $\varphi\le1/3-c$ の連続体の機構;(3) 値で 2/3 側の兆候(394 §8.4 の (A))。
- **成算**:S218(なし、1 割未満)。

## F228(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕の移り先「準自由の段の有効汎関数の一意性・非退化と、それへの Bogoliubov の精度の縮約」(F224 の R9・F115 の再開条件の族)を、(K1) Bogoliubov 汎関数の凸性(Bach–Lieb–Solovej 1994 の一般化 Hartree–Fock の型)、(K2) Hessian の非退化(Lewin–Nam–Serfaty–Solovej 2015 の (A2) の型)、(K3) Bogoliubov の精度の縮約の誤差評価(同 Thm 2.2 の型)、(K4) 可能性の低い型(BLS Thm 2.14 の「$H_\rho$ の一意な基底状態」、準自由の $F_{\rm qf}$ の滑らかさ、余りの帯の解析性)で供給する方式。2026-10-21、w_E05_424_nfts_bogoliubov = 書き下しの型、worklog (研究ノート: `2026-10-21_w_E05_424_nfts_bogoliubov.md`) §2・§3(稿なし、(0) で停止)、成算 S221、C0 603)
- **閉じたもの**:**方式**(F115 の族の型で (NFT$_{\rm s}$) を供給すること)。(NFT$_{\rm s}$)・(REG-W)・全列の真偽は閉じていない。
- **理由**:(K1) BLS(原典本文:§1・Thm 2.9〜2.14・Lemma 2.10)はフェルミオンで、使うのは許容な 1-pdm の集合の凸性と $E(\Gamma)$ の固有値についての多重アフィン性(極値性:inf は純粋な準自由状態で取れる)、2 体の $V$ が正定値なら対なし(Thm 2.11)—— 最小化子の一意性の定理も $E(\Gamma)$ の凸性も無い。PF の $\frac\lambda2P_f^2$ の 2 体の核 $\lambda\,k\cdot l$ は対称な 2 光子の空間で不定(対 $(k,-k)$ で負)で、Thm 2.11 の仮定の逆向き(運動量 0 の対のスクイーズ状態は $\langle P_f^2\rangle=0$);Wick の 4 次の Hessian は $\mathrm{tr}(XKXK)$ 型で不定符号(1% 未満)。(K2) LNSS の (A2) は 2 次の変分 $\ge\eta_H\gt0$(帰結として本質スペクトルの隙間);PF では軟光子の $\lvert p\rvert+\lvert q\rvert$ が本質スペクトルを 0 まで届かせるので $\eta_H\gt0$ は立たない(無質量の構造の障害;F198 の準自由版);局所の非退化は遠い枝との交差を排除しない(1% 未満)。(K3) Thm 2.2 の型は F115 追記(232)の (E1)〜(E3) と (A2) で落ちる;さらに仮に成っても、**加法的な誤差の縮約は (NFT$_{\rm s}$) に届かない**(観察 424-A:凹 $C^1$ の $G$ と任意の $\delta_0$ に、$0\le F-G\le\delta_0$、$0\le F'-G'\le\delta_0/\lambda$ で (NFT$_{\rm s}$) が偽の凹 $C^1$ の $F$ がある)—— エネルギーの誤差 δ の縮約が与えるのは窓の幅に依らない落ちの上界 $\lesssim\sqrt{\delta\lvert G''\rvert}$ だけで、制御される窓は相対幅 $s\gg\alpha\sqrt\delta\,\lambda^{-5/14}$(値の勘定、凍結の帯;$\delta\asymp\lambda^{3/7}$ で 403-A の $s\gg\lambda^{-1/7}$ に一致)(1% 未満)。(K4) 一意なのは平均場の作用素 $H_\rho$ の基底状態(線形化の隙間)で (K2) と同じ段;$F_{\rm qf}$ の (NFT$_{\rm s}$) は元の問題の写し;余りの帯の解析性は 418 (c) と同じ量(0)。
- **R9**:閉じたのは方式。(NFT$_{\rm s}$) は $\langle T\rangle_{\psi_\lambda}$ の相対幅 → 0 までの Lipschitz 型の主張なので、縮約から出すには余り $F-F_{\rm red}$ そのものの 2 階($\chi_T$ の水準、$\langle\delta T\psi,(H-E_0)^{-1}\delta T\psi\rangle$)の評価が要る —— (REG-W) を余りに当てたもので、F115 の族は (NFT$_{\rm s}$) の供給先として**黒**。F224 の移り先は「余りの静的な感受率 $\chi_T$ を縮約の精度で押さえること」に精密化される(Bogoliubov の精度は必要だが十分でない)。消滅ではない。
- **射程(T60)**:禁じるのは「準自由・Bogoliubov の汎関数の凸性・一意性・非退化、またはエネルギー・状態・⟨T⟩ の水準の縮約(誤差の大小によらず)で (NFT$_{\rm s}$)・(REG-W) を出す」発注。止めないもの:余りの $\chi_T$(ℓ=0 の静的な感受率)の直接の評価;準自由の段の値の偵察(真偽の値として);E05 の (E3) の道具としての Bogoliubov 近似(エネルギーの漸近の標的)。
- **再開条件**:(1) 縮約の余りの 2 階($\chi_T^{\rm full}-\chi_T^{\rm red}$)が $o(M^3/(\alpha\lambda^3))$ で λ に一様に押さえられる道具(レゾルベントの水準の Bogoliubov の縮約;無質量の閾値での赤外の正則性を含む)が供給されたとき;(2) λ についての $F'$ の凸性(404-G)の供給が立ったとき(F224 再開 (2) と共通)。

## F229(E05、難問 #3 = HP-G3-1 の Q3 の下側 —— (I1) 型の鎖(212-C の窓 + 319-B の縁 + 396-W の望遠鏡和)と在庫の制約だけで、冪 γ∈[1/14,1/6) の下界の密度を $d(\gamma)=\frac{4(3-14\gamma)}{7(1+2\gamma)}$ より上げる方式;端点の議論の凸結合(弦)。2026-10-21、w_E05_425_p23_followup = 書き下しの型、稿 `425_難問3の交換曲線と難問2の値_2026-10-21.md` §3、成算 S222)
- **閉じたもの**:**方式**(この鎖と在庫の制約の中での密度の改良)。命題(模型の真の $F$ での密度・真の冪)は閉じていない。
- **理由**:接線の階段 J1(在庫の制約を全て満たす凹な関数)で $\lbrace M\ge\lambda^\beta\rbrace$ の下対数密度がちょうど $\frac{20}{7\beta}-4$(観察 425-B)、かつ鎖の率は $M/\lambda^{1/2}$ の冪を越えない(観察 421-C (a))。極限の模型の値反復(C0 604)も全ての β で同じ値。$d$ は狭義凸で、端点の弦は達成されない(γ=0.1 で弦 0.786 対 0.762)。
- **越えるのに要るもの**:$M$ の下界の冪(= $F$ の局所冪の片側評価、難問 #2、F205 の段)か、319-B の縁の評価の改良((EDGE) の族)。


## F230(E05 の外・難問 #1 の弱い構成 (K5)(K6):GHL 2014 型 —— 固定の参照 Wiener 測度の上の Gibbs 密度の収束(自己エネルギーを重みの対角部分から引く)で PF のくりこまれた経路測度・半群を構成する方式、および Gross 型の失敗の 1 項を Euclid 側で別に処理する方式。2026-10-21、w_E05_432_p1_construct = 書き下しの型、稿 `432_難問1_くりこまれた模型の構成の弱い形_2026-10-21.md` §3、成算 S227)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(弱い極限の存在・非自明性の真偽は閉じない)。
- **理由(厳密、命題 432-A)**:PF の質量くりこみの反項は重みでなく参照の Brown 運動の拡散係数 $1/m_0(\Lambda)$ に入る(F9 (3))。(FK) の重みは正で a.s. 有限なので $\mu_{m_0,\Lambda,T}\ll W^{(1/m_0)}$ で、Lévy の 2 次変分 $3T/m_0$ が a.s. に決まり、裸の質量が違う族の元は互いに特異(全変動 2)。全変動で収束する部分列は無く、固定の参照 $\nu$ に対する密度 $\rho_j$ の $L^1(\nu)$ 収束の表示も無い —— GHL 2014 Thm 2.2 の証明(固定の $P^x$ 上の $C_\varepsilon(F,G)$ の Cauchy 性)の骨組みが最初の段で立たない。Gross の失敗の項(F6 命題 4・F179 の対の項)を Euclid 側で別に処理する = 参照の拡散係数を族で動かす = 同じ所。原典:GHL 2014 の導入 (1.9) と同所の著者の注(2 重の確率積分の対ポテンシャルは一様な指数評価を許さない)。
- **共通点(1 行)**:**Nelson 模型の構成(Nelson 1964・GHL 2014)は質量をくりこまないので参照測度を固定できる;PF の質量くりこみは参照測度そのものを族で動かし、強い位相(全変動・密度・作用素ノルム)の極限を全て禁じる —— 残るのは弱収束だけ。**
- **R9**:閉じたのは方式。双極子では族が $\Lambda\gt3\pi m_{\rm ph}/4\alpha$ で終端(段は空);Nelson 型(質量のくりこみなし)では 432-A の障害は無い(GHL が立つ)—— 障害は PF の質量くりこみに局在。
- **射程(T60)**:禁じるのは「固定の参照測度に対する Gibbs 密度の収束・全変動の収束・自己エネルギーの引き算の後の重みの一様な可積分性」で PF のくりこみ族を構成する発注。止めないもの:弱収束(Prokhorov)の緊密性の判定(K1、次の F 断片の外)、着衣の座標(LLP の後の重心)の経路測度。
- **再開条件**:(1) 参照の拡散係数を族で固定できる座標(着衣の座標)の 2 次変分が裸の質量に依らないこと;(2) 2 重の確率積分の対ポテンシャルの一様な指数評価の新しい型(GHL の注・GL09 の障害を越えるもの)。

## F231(E05 の外・難問 #1 の弱い構成 (K3)(K4):Euclid の特性関数 $\varphi_\tau(p)=\langle\psi_0,e^{-\tau(H(p)-E_0)}\psi_0\rangle$ で $\mathcal E_\Lambda(p)$ の族に沿う非退化・点ごとの極限を出す方式、および有界な観測量の OS の再構成の部分列極限で非自明な極限の模型を出す方式。2026-10-21、w_E05_432_p1_construct = 書き下しの型、稿 `432_` §4・§2、成算 S227)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(非退化 (iii-2) と OS の極限の非自明性の真偽は閉じない)。
- **理由(厳密、命題 432-B (ii)(iii))**:$e^{-\tau p^2/2m}\le\varphi_\tau(p)\le e^{-\tau\mathcal E(p)}$、$-\frac1\tau\log\varphi_\tau$ は非増加で極限は $\mathcal E$ 以上 —— Euclid の表示は $\mathcal E$ の**上界**だけを与え、下界は F225・F180 の段(窓増分の特性関数の族に一様な指数減衰)のまま。OS の部分列極限は対角線論法と Gram 行列の正値の閉性で只に在るが、非自明性(1 次元に潰れない・$\mathcal E_\infty$ を見る)の判定量は $\varphi_t(p)$ の極限で、潰れれば退化(432-B (iii))、広がれば $\varphi\to0$ で何も見えない。
- **共通点(1 行)**:**Euclid の汎関数の極限は正値性・凸性で只に在るが、内容(非自明性)は全て「族に一様な下からの評価」(F225 の共通点)か「物理の時刻での着衣の完了」(下の K1)に落ちる。**
- **R9**:閉じたのは方式。双極子では族が終端して段は空;固定の Λ・小さい α では CFP 2009 (I 3) で非退化(F225 の R9 と同じ)—— 障害は族に一様の側に局在。
- **射程(T60)**:禁じるのは「特性関数・Laplace 変換の凸性・正値性・OS の閉性だけで (iii-2) または非自明な極限を出す」発注。
- **再開条件**:F225 の再開条件 (1)〜(3);または K1 の緊密性が値で肯定されたとき(広がりも潰れもしない $\varphi^\infty_t$)。

## F232(E05 の外・難問 #1 の弱い構成の低い型 (K2)(K7)(K8):族に一様な不変原理(着衣の時間より長い時刻で Brown 運動 $1/m_{\rm ph}$)、2 次の摂動・双極子・RG 改良の有効模型との一致の弱い形、Wightman・実時間の極限。2026-10-21、w_E05_432_p1_construct = 書き下しの型、稿 `432_` §2、成算 S227〔各 0.5〜3%〕)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(成算 1 割未満の確認;命題の真偽は閉じない)。
- **理由**:(K2) 固定の λ の長時間の極限は定義上 $h_{\rm ls}$ で済み、本体は λ→∞ との順序の交換 = 着衣の時間 $T_{\rm dress}(\lambda)$ の族に一様な制御 = K1 と同じ量(432-B (i) の比 $r(\lambda)$)。(K7) 1 ループの族は極 $\lambda_L=2(e^{3\pi/8\alpha}-1)$(α=1 で 4.50)で終端、双極子の族は $\Lambda\gt3\pi m_{\rm ph}/4\alpha$ で終端(366 §5);RG 改良の族 $(1+\lambda/2)^{8\alpha/3\pi}$ は在るが比べる定理の側に道具なし(626 の値では短い時刻の着衣が未了)。(K8) 非相対論で軸の大半が適用外、実時間の極限は Euclid より弱い制御しかない。
- **共通点(1 行)**:**比べる相手(摂動・双極子)の族が先に終端するか、比べる量が K1 の判定量 $r(\lambda)$ に落ちる。**
- **R9**:閉じたのは方式;双極子では族が終端(段は空)。
- **射程(T60)**:禁じるのは「1 ループ・双極子の族との比較だけで #1 の弱い形を出す」発注。
- **再開条件**:K1 の値(在庫の HMC で $r(\lambda)$ が平ら)が出たとき (K2) を再評価。
- **再開条件の照合(2026-10-21、監査 449 §0′、同上)**:再開条件「K1 の値(在庫の HMC で $r(\lambda)$ が平ら)」は **NOT_MET**(F255 の末尾と同じ値:λ=256 で $r$ の傾きは −0.60/−0.56/−0.50)。(K2) は再評価しない。値であって上下界ではない【T88】。


## F233(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕を、**光子質量 μ で基底状態を孤立させ μ に一様な解析性(Griesemer–Hasler 型)と、新しく $(\lambda,\mu^2)$ の同時凹性**で供給する方式。2026-10-21、w_E05_429_lens_analytic = 書き下しの型、稿 `429_全列_複素解析と作用素論のレンズ_2026-10-21.md` §2 A1・§3、成算 S224、C0 611 J1)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((NFT$_{\rm s}$)・全列の真偽ではない)。
- **理由**:(1) $\omega_s(k)=\sqrt{k^2+s}$ は $s=\mu^2$ について凹で $d\Gamma$ は線形、ゆえに $E_0(\lambda,s)$ は同時凹(初等)—— しかし境界 $s=0$ には 1 変数の凹性しか課さない($F(\lambda)+c\sqrt s$ は同時凹な延長)。(2) 質量は 2 構造を光子数の差に比例してずらし、擬交差の線を $(\lambda,s)$ 平面で動かすだけ;2 準位の証人で例外点の実軸からの距離 $2\varepsilon/\Delta t$ は s に依らない(C0 611 J1 PASS)。Kato の半径 = min(μ, 内部の擬隙間)/Δτ。GH 2009・HH 2011 の量化子は F208 (c)。(3) 観察 429-U(PF・孤立・整な正則族・2 径数の同時凹性を全て満たして (NFT$_{\rm s}$) が偽の族)。
- **共通点(1 行)**:**光子質量は連続スペクトルの端を外すが内部の擬隙間を外さない;μ に一様な半径は擬隙間の下界そのもの —— F198・F208 (d)・418 (c) の段。**
- **R9**:閉じたのは方式。**射程(T60)**:禁じるのは「光子質量で孤立させた $E_0$ の λ についての解析性・Cauchy の評価を μ に一様にして (NFT$_{\rm s}$)・(REG-W) を出す」「$(\lambda,\mu^2)$ の同時凹性から λ の 2 階を出す」発注。**再開条件**:内部の擬隙間の λ に一様な冪の下界(F211 の再開条件 (1))。

## F234(E05、全列の (NFT$_{\rm s}$) を、**λ についての Stieltjes の表示と λ についての Birman–Schwinger** で供給する方式 —— $z\lt E_0(\lambda_0)$ で $\langle\phi,(H(\lambda)-z)^{-1}\phi\rangle=\int d\nu(x)/(1+(\lambda-\lambda_0)x)$(導関数が値で押さえられる)、$F^{-1}(z)=\lambda_0-1/\lVert K(z)\rVert$。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A2・§3、C0 611 J3)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:Stieltjes の正則性の尺度は $(E_0-z)/g$ = スペクトルまでの距離(Kato の自明な尺度)で、擬交差を解くには $E_0-z\ll$ 擬隙間が要る(C0 J3:$\eta=100\varepsilon$ で滑らか、$\eta\le\varepsilon$ では窓の中で z がスペクトルに入る);$\lVert K(z)\rVert$ の頂は擬交差で同じく近縮退(言い換え)。全ての $T\ge0$ で成る性質なので 429-U の証人でも成る。
- **共通点(1 行)**:**レゾルベントの λ についての正値の構造は、スペクトルまでの距離の尺度でしか正則性を与えない —— F215(Löwner)・F198 の段。**
- **R9**:閉じたのは方式。**射程(T60)**:「λ についての Stieltjes・Pick・Birman–Schwinger の表示で $\chi_T$・(NFT$_{\rm s}$) を出す」発注。**再開条件**:F211 の再開条件 (1)。

## F235(E05、全列の (NFT$_{\rm s}$) を、**J=0 セクターの局所の隙間と単調族のスペクトルの流れ**で供給する方式 —— 光子は J≥1 なので J=0 の連続体は 2 光子から;T≥0 で枝は増加、擬交差の相手は交差の手前 δλ で $E_0+\Delta\tau~\delta\lambda$ の J=0 の重みとして見える。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A3・§3)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:連続体の $\chi_T$ への寄与は既に無害(F211 (3));残る量は内部の擬隙間で、「各 λ で J=0 の離散部分の隙間 ≥ Δ_*(λ)」は (NFT$_{\rm p}$) より強い言い換え(R9)—— 量の入力が無い。
- **共通点(1 行)**:**対称性のセクターへの制限は連続体を外すが、同じセクターの 2 構造の擬交差は外さない(PF の一意性で基底状態のセクターは固定、相手も同じセクター)。**
- **R9**:閉じたのは方式。**射程(T60)**:「J=0 への制限・スペクトルの流れ・Krein のスペクトルのずれで擬交差を数え、各点の隙間の下界を仮定して (NFT$_{\rm s}$) を出す」発注。**再開条件**:J=0 の離散部分の隙間の λ に一様な冪の下界(値の偵察は止めない:連続の殻の準自由の変分で 2 番目の J=0 の極小の有無 —— F224・F228 の「止めないもの」と同じ族)。

## F236(E05、全列の (NFT$_{\rm s}$) を、**有限温度の正則化**($\lvert f_\beta''\rvert=\beta(\delta T,\delta T)_{\rm Duh}\le\beta\mathrm{Var}_\beta T$ を各点で、凹性で $F$ に移す;Dyson–Lieb–Simon・Falk–Bruch)で供給する方式。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A4・A11・§3、C0 611 J2・J2b)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:凹関数の比較で窓 w の落ち $\le K_\beta w+4\sqrt{\delta_\beta K_\beta}$、$\delta_\beta\approx S_\beta/\beta$ で窓に依らない項 $\sqrt{S_\beta\mathrm{Var}~T}$ は β に依らない(観察 424-A = E05-P218 の型);$S_\beta\ge O(1)$(無質量・無限体積では $f_\beta=-\infty$)、$\sqrt{\mathrm{Var}_{\psi_0}T}$ は $g$ の尺度。C0 611:起動前の判定 J2 は判定量の誤設定で FAIL(札 INCONCLUSIVE、規則は緩めない);事後の J2b(事後と明記)で最良の上界 / 真の落ち = 1.03〜1.41(ε に依らず)—— $F''$ を知る以上の情報なし。Falk–Bruch は T=0 で $\chi\ge4\mathrm{Var}^2/(\text{f-sum})$ の下界(F207 (4)・F218 (2))。
- **共通点(1 行)**:**有限温度は加法の誤差の縮約で、窓に依らない誤差が落ちの全量の尺度 —— F228 (K3)・424-A の段。**
- **R9**:閉じたのは方式。**射程(T60)**:「有限温度・Duhamel の内積の上界($\beta\langle A^2\rangle$)で $F$ の 2 階・(NFT$_{\rm s}$) を出す」発注。**再開条件**:F228 の再開条件 (1)(余りの 2 階をレゾルベントの水準で押さえる道具)。

## F237(E05、全列の (NFT$_{\rm s}$) を、**Lee–Yang の零点のない領域を β に一様に**(分配関数 $Z_\beta(\lambda)$ の複素 λ の零点)で供給する方式 —— 418 (c)(F224 (c))で 0 と判定された型の「何が欠けて 0 か」の確認。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A5・§3、C0 611 J4)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(1) 2 準位で $Z_\beta=0$ ⟺ $D^2=-4\varepsilon^2-((2k+1)\pi/\beta)^2$、最も近い零点の虚部 / $(2\varepsilon/\Delta t)$ = 1.86・1.012・1.0001(βε=1・10・100、C0 J4)—— β に一様な零点のない帯 ⟺ 擬交差の不在(R9)。(2) **欠けているのは β の一様性でなく構造**:λ は強磁性の系の線形の場でなく運動項の係数で、$Z_\beta(\lambda)$ は正値の測度の Laplace 変換(BMV、F214)にすぎず零点を実軸の任意に近くに置ける(観察 429-U)。(3) 逆に「零点は有限本の縦線の上」の Lee–Yang 型が在れば足りる(有限個の交差は (NFT$_{\rm s}$) を割らない —— 418 §2 C1;線から離れた点では扇形の解析性で観察 402-C の消費者に入る)。
- **共通点(1 行)**:**零点の位置の定理は強磁性の表示(場が線形に入る正値の構造)を要り、PF の λ にはそれが無い —— F212 (b)・F214 の段。**
- **R9**:閉じたのは方式。**射程(T60)**:「λ を Lee–Yang の変数として零点のない帯を出す」発注(β の一様性を足しても同じ)。**再開条件**:λ(または λ と同値な径数)が線形に入る強磁性の表示 —— F187 の再開条件 (1)・F212 の再開条件 (1) と同じ族。

## F238(E05、全列の (NFT$_{\rm s}$) を、**例外点・幾何の勘定**で供給する 2 型 —— (a) 有限モードの判別式 $D(\lambda)$ の零点(Kato の例外点)の Jensen の公式・Cartan の補題による勘定、(b) 基底状態の射影空間の経路(Fubini–Study の長さ、忠実度感受率 $\chi_F$)で擬交差の個数を縛る。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A6・A7・§3)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(a) Cartan は「半径の和 ≤ε の円板の外で $\lvert D\rvert\ge(\epsilon/e)^d\max\lvert D\rvert$」—— 悪い点の集合の大きさ(密度の命題、396-D の型)で次数 d(Fock の次元)に依り一様でない;各 2 進区間に 1 個の鋭い交差は零点 O(1) 個で Jensen が許す。(b) 擬交差 1 つの経路長は ε に依らず π/2、滑らかな部分の長さは 2 進区間で $\sim\sqrt N\sim\lambda^{2/7}$ で埋もれる;$\chi_T\le\sqrt{\mathrm{Var}~T\cdot\chi_F}$ は強い量 $\chi_F$ を要る(向きが逆)。
- **共通点(1 行)**:**勘定の型は個数・測度を与え、各点(狭い窓)の情報を与えない —— 396-W・F189 の段。**
- **R9**:閉じたのは方式。**射程(T60)**:「例外点・判別式の零点の勘定、射影空間の経路長で (NFT$_{\rm s}$) を出す」発注。**再開条件**:なし(各点の情報は勘定の型の外)。

## F239(E05、全列の (NFT$_{\rm s}$) を、**Gerlach–Löwen 型**(虚時間の 1 次元の有効系で結合についての非解析性の不在;F212 の再開条件 (3) の当て直し)で供給する方式。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A13・§3)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(原典は未入手 —— Gerlach–Löwen 1991 RMP 63, 63・Löwen 1988 PRB 37, 8661 は「無料の PDF なし」、`[要入手]`;判定は原典に依らない)。
- **理由**:(1) 出力は定性の解析性で、有限の λ での真の非解析性は既に無い(E05-F22 の一意性・E05-P207);要る量は λ→∞ で幅の縮む擬交差の排除。(2) 1 次元の有効系の解析性の半径は有効結合($\alpha\lambda$ で増える)と到達距離に依り λ に一様でない(F212 (3) の $\sum rJ(r)$ の対数発散も同じ向き)。(3) 無質量のボソンの 1 次元の長距離の類には結合について不連続な転移の例(Ohmic のスピン–ボソン、$1/r^2$ Ising)があり類全体の定理にならない —— 模型固有の超 Ohmic 性が要るが (1) が残る。
- **共通点(1 行)**:**相転移の不在の定理は定性(真の非解析性の排除)で、擬交差の幅の量を与えない。**
- **R9**:閉じたのは方式。**射程(T60)**:「ポーラロンの相転移の不在の定性の定理を PF に移して (NFT$_{\rm s}$) を出す」発注。**再開条件**:原典(入手後)に解析性の半径の結合に一様な量の形があったとき(そのときは超 Ohmic の結合で半径 ≳ 相対 O(1) を確かめる)。

## F240(E05、全列の (NFT$_{\rm s}$) を、**このレンズの既に閉じた型への当て直し 5 型**で供給する方式 —— α(電荷)についての解析性を λ へ運ぶ、$\mu=-F''$ の Borel 変換(Herglotz)の調和優関数、$s=\ln\lambda$ の帯の Phragmén–Lindelöf・3 線(402-C へ)、Falk–Bruch・二重交換子の和則、Rellich の解析的な枝 + PF の一意性。2026-10-21、w_E05_429_lens_analytic、稿 `429_` §2 A8〜A12)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(照合だけで閉じた)。
- **理由**:α の解析性は小結合の量化子で半径が λ で 0 に縮む(F208 (c)・F212 (a));Herglotz の境界値は尺度 y の窓の平均で、y → 0 が (NFT$_{\rm s}$)(R9、406-U で μ は任意の正測度);固定幅の帯は F198 の再開条件そのもの(相対幅 O(1) の擬交差の不在で (NFT$_{\rm s}$) より強い);和則は下界(F207 (4)・F218 (2));Rellich は定性で半径がモード数に一様でない(F208 (e))。全て観察 429-U の証人でも成る。
- **共通点(1 行)**:**正則族・正値性の普遍の性質は 429-U で凹性に退化する(406-U1 の正則族・PF 版)。**
- **R9**:閉じたのは方式。**射程(T60)**:このレンズ(正則族・扇形の Cauchy・光子質量・同時凹性・Lee–Yang の帯・Stieltjes/Pick・例外点の勘定・Rellich・有限温度)で、模型固有の量の入力なしに (NFT$_{\rm s}$)・(REG-W) を狙う発注は観察 429-U で止める。**再開条件**:F211 の再開条件 (1)(2 構造の間のトンネル振幅の量的な評価)、または F228 の再開条件 (1)。


## F241(E05、全列(行 E1-H の内側)の消費者の鎖 395-B の κ(左の 2 次の欠損の無限小の limsup)を**有限幅の割線**(相対幅 $s\gg\lambda^{-1/7}$)に替えて 403-A で閉じる方式(V1)と、**試行状態の比較の改良**で 403-A の閾 $\lambda^{-1/7}$ を外す方式(V7)。2026-10-21、w_E05_430_lens_variational = 書き下しの型、稿 `430_全列_変分と凸解析と消費者のレンズ_2026-10-21.md` §3、成算 S225)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(全列・(REG-W)・(NFT$_{\rm s}$) の真偽ではない)。
- **理由**:補題 430-A・系 430-A1(self-audited):2 次の試行 $\psi-t(H-E_0)^{-1}P_\epsilon\phi$ で、相対幅 $s$ の割線が縛るのは場のエネルギーの感受率のうち**励起エネルギー $\gt\epsilon\approx2sE_0$ の部分**だけ($W_{\gt\epsilon}\le18R$)。観察 430-C(値):二重交換子 $N=\Xi M^3$ だけでも $\mathrm{Var}_{\gt2sE_0}(H_f)/M^2\lesssim\lambda^{-1/7}/s$ —— 403-A と同じ閾が窓なしで出る;閾は $\alpha\lambda/M_{\min}^2$(254-B)で決まり、$M\asymp\lambda^{5/7}$ でも $\lambda^{-3/7}$ に下がるだけ。鎖 395-B が要るのは $\chi_f$ の全体で、残りの $\mu_\phi([0,\lambda^{-1/7}E_0])$($\phi=\delta H_f\psi_\lambda=-\lambda\delta T\psi_\lambda$)に擬交差の相手が住む(C0 616 J2:2 構造の玩具の交差の中心で $\chi_{\le\epsilon}=263$ 対 $\chi_{\gt\epsilon}=0.05$、値)。その量の上界は擬交差で偽になり得る($\sigma^2$ の猫の分散、f は内挿)ので名指しにしない。
- **共通点(1 行)**:**窓の比較・割線・二重交換子は励起エネルギー $\gtrsim sE_0$ のスペクトルの部分しか見ず、鎖が要る低エネルギーの部分(擬交差の相手)に届かない —— 403-A の閾 $\lambda^{-1/7}$ はこの対応の閾。**
- **R9**:閉じたのは方式。難しさは「低エネルギーの ℓ=0 のスペクトルの重み $\mu_\phi([0,\lambda^{-1/7}E_0])$」= F224・424-A の移り先(余りの $\chi_T$)と同じ場所 —— 消滅ではない。
- **射程(T60)**:禁じるのは「割線・試行状態の比較・二重交換子・窓の情報だけで鎖の κ を置き換えて全列を出す」発注。止めないもの:低エネルギーの重みの λ についての局所の比較(稿 §7 の次の 1 手)。
- **再開条件**:$\mu_\phi^{(\lambda)}([0,\epsilon])$ を隣の λ の値か在庫の量で押さえる入力(擬交差の相手の出現を禁じる量;F224 の再開条件 (1) と共通)が立ったとき。

## F242(E05、全列の消費者の f の λ 正則性を **(λ, q) の 2 径数の結合凹性**($\tilde E(\lambda,q)=\inf\sigma(\lambda T-q\pi_z+H_f)$、$t=1/\lambda$ の $\tilde\varepsilon(t,\mu)$ を含む)から出す方式(V3)。2026-10-21、w_E05_430_lens_variational、稿 `430_` §4、成算 S225)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:観察 430-B(self-audited):厳密に凹な $C^2$ の任意の $F$ と任意の $\varphi\gt0$ に、$\tilde E=F-\varphi q^2/2$ は $\lvert q\rvert\le q_0$ で結合凹で、接平面の下限は $\mathbb R^2$ で結合凹 —— $f=1-\lambda\varphi$ の輪郭(狭い上向きの瘤を含む)は結合凹性・偶性・$\tilde E(\lambda,0)=F$ と両立する。C0 617(λ=1000 に相対幅 $10^{-3}$・高さ 0.5 の瘤で NSD、中点凹性の違反 0/4000、値)。
- **共通点(1 行)**:**結合凹性は $f$ の輪郭と $F$ を結ばない(406-U の 2 変数の局所版)—— F204 の「TRK の向きだけ」の厳密化。**
- **R9**:閉じたのは方式。F204 の再開条件(ℓ=1 の低帯の重みの下界を与える新しい相関不等式)は不変。

## F243(E05、全列の**片側の消費者**(瘤は急な上昇と急な下降の両方を要るので、「$f$ は λ の増加で急に上がらない」の片方で足りる)の供給(V2)と、396-D の良い点からの**試行の移送** $\eta_g=R_g\pi_z\psi_g$ で悪い点の $G$ を下から押さえる方式(V8)。2026-10-21、w_E05_430_lens_variational、稿 `430_` §1・§5、成算 S225)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(片側の形は消費者として正しい:415-A は左の窓でも同じに通る)。
- **理由**:片側の比較を出す変分の表示は試行の移送しか無く、移送の誤差 $2\mathrm{Re}\langle\eta_g,\pi_z(\psi_b-\psi_g)\rangle$ は $\lVert\pi_z\eta_g\rVert\sim1/\lambda$ と擬交差を跨ぐ $\lVert\psi_b-\psi_g\rVert=O(1)$ で $G$ と同じ桁;$\lVert\partial_\lambda\psi\rVert^2=\int d\mu_T/x^2$ は ℓ=0 の 2 次の逆モーメント。$T$ の項は ℓ=1 の応答が $\bar x\approx\frac43\langle T\rangle$ に集中するなら $w/\lambda$ で効かない(値;赤外の尾は F220 の量)。片側でも誤差の型は同じ。有限モードの玩具で $f$ は戻る(F204 注)。
- **共通点(1 行)**:**片側にしても、悪い点への情報の運搬は ℓ=0 の構造の変化 $\psi_b-\psi_g$ を通り、擬交差を跨ぐと $O(1)$ —— F219 (c) と同じ段。**
- **R9**:片側の形は全列から自明に従い 396-D の下で全列と同値(消費者の形、名指しにしない)。再開条件:F219 の再開条件 (2)(擬交差の隙間の量的な評価)。

## F244(E05、全列の各点の正則性を **α 方向**(α についての平均・a.e. α・α と λ の交差変数)から λ に移す方式(V4)。2026-10-21、w_E05_430_lens_variational、稿 `430_` §5、成算 S225)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:λ と α を結ぶ厳密な恒等式が無い —— 次元で $E_0=\Lambda F(\Lambda/m,\alpha)$、光子の拡大は Λ を動かす恒等式 $\Lambda\partial_\Lambda E_0=E_0+\lambda\langle T\rangle$ だけで α を含まない;場の振幅の尺度変換は $H_f$ を対角に保たない;$\alpha\lambda$ の組で決まるのは双極子(反跳なし)だけ。擬交差は $(\lambda,\alpha)$ 平面の曲線で全ての α の直線を横切り得るので、α の平均・a.e. α は曲線を除けない(a.e. α は標的の変更)。
- **共通点(1 行)**:**α は λ の各点の情報を運ばない(F170 (i) と同じ:結ぶ尺度が無い)。**

## F245(E05、全列の (NFT$_{\rm s}$) を **Legendre の双対** $\varphi(x)=\inf\lbrace\langle H_f\rangle_\rho:\langle T\rangle_\rho\le x\rbrace$ の量的な強凸性として出す方式(V5)と、固定の生成子の試行 $G\ge\langle A\rangle^2/\langle C\rangle$ の期待値の内挿で擬交差の点の $f$ を押さえる方式(V10)。2026-10-21、w_E05_430_lens_variational、稿 `430_` §5、成算 S225)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(V5) $dM/dg=-\lambda$、$d^2M/dg^2=1/\lvert F''\rvert$ で、(NFT$_{\rm s}$) ⟺ 双対の $\varphi''$ の窓の平均 $\gg\alpha\lambda^3/M^3$(R9 の同値変形);凸性は混合の凸包で、狭義の改良は重ね合わせの交差項 $\langle\psi_1,T\psi_2\rangle$・$\langle\psi_1,H_f\psi_2\rangle$(巨視的に異なる 2 構造で指数的、417);φ は $F$ と同じ情報(406-U)。(V10) 期待値は擬交差で内挿するが $x^2/y$ の凸性で内挿の比は平均以下、損は構造の間の相対の分散 = 212-C の 2σ²(F219 (0))。
- **共通点(1 行)**:**状態の上の凸性(混合)は擬交差を平らにし、狭義にするのは交差項(トンネル振幅)だけ。**

## F246(E05、全列の消費者の量を**有限の P の割線** $f_P=(E(P)-E(0))/(\lambda P^2/2)$ に替える方式(V9)と、上下界の冪の隙間 2/3・5/7 と凹性から落ちの測度 $-dg$ の各点の上界を出す方式(V6)。2026-10-21、w_E05_430_lens_variational、稿 `430_` §5、成算 S225)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(V9) $q(P)=E(P)-\lambda P^2/2$ は凹・偶だが $q''(0)$ と $[0,P]$ の平均の間に向きの不等式が無く $f\le f_P+o(1)$ は出ない(標的の変更でもある)。(V6) 上下界の比が 1 に近づいてもサンドイッチ(424 §3)で窓は相対幅 $\gtrsim\sqrt{\delta/F}$ まで、観察 424-A(P218)でどんな加法的な精度でも (NFT$_{\rm s}$) は出ない。
- **共通点(1 行)**:**$F$ の水準・P の平均の水準の情報は、各点の 2 階の量に向きの不等式を与えない。**


## F247(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕の静的感受率 $\chi_T=\lvert F''\rvert/2$ を、**双対の変分(Thomson の原理・Kipnis–Varadhan の $H^{-1}$ ノルム・容量)**で上から押さえる方式 —— 319-A の正値性による基底状態変換の Dirichlet 形式で $\chi_T=\inf$(試行の流れのエネルギー)。2026-10-21、w_E05_428_lens_prob = 書き下しの型、稿 `428_全列_確率論と経路測度のレンズ_2026-10-21.md` §3 P1、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((NFT$_{\rm s}$)・(REG-W)・全列の真偽ではない)。
- **理由**:向きは正しい(Dirichlet の原理は下界、Thomson は上界 —— 在庫の変分が全て下界の向きだった 415 §1 (b) の逆)が、(1) 2 構造の玩具で流れは隘路を通り、エネルギーは容量の逆 $\approx w/(2t)$($w=\Delta\tau^2/4$、$2t$ は擬交差の隙間)—— 上界の入力は隘路の伝導度 = 中間の配位の $\psi_0$ × 跳びの率 = トンネル振幅(F223 (d) の量);(2) 明示の流れは対称性からしか作れず、光子の拡大 $D$ で $i[H,D]\psi_0=(\lambda\delta T+\delta C_\Lambda)\psi_0$(固有方程式の $\delta H_f\psi_0=-\lambda\delta T\psi_0$ を使う)の余りが殻の応答の感受率 $\chi_C$ を含み、尺度則で $F''$ に戻る(415 N2・F207 (K3));正確な流れは $\nabla(\partial_\lambda\psi/\psi_0)$ で循環。
- **共通点(1 行)**:**上界の向きの一般原理(Thomson)も、流れの構成に隘路の伝導度(= トンネル振幅)を要る —— F211・F223 と同じ段。**
- **R9**:閉じたのは方式。双極子では $T$ の揺らぎは Gauss で隘路がなく、流れは明示(段は空)。
- **射程(T60)**:禁じるのは「Thomson・Kipnis–Varadhan・容量の上界を、対称性(拡大・尺度)から作った流れか、構造を知らない流れで当てる」発注。止めないもの:粗い変数($H_f$・$N$)による 2 尺度の流れ(GOVW 型)の数値の偵察(稿 §4)。
- **再開条件**:(1) 「構造の変数」(擬交差の 2 構造を分ける粗い変数)が同定され、その周辺分布の谷の深さが λ の対数で押さえられたとき;(2) F223 の再開条件 (1)。

## F248(E05、全列の (NFT$_{\rm s}$) の物理の読み「擬交差なし」を、**基底状態の光子数の分布の単峰性**で出す方式 —— BHLMS 2002 Example 6.1 型の Poisson 混合表示(跨ぐ対の積分 $\mu$ が混合変数)+ $\mu$ の対数凹性 ⟹ 混合 Poisson の対数凹性。2026-10-21、w_E05_428_lens_prob、稿 `428_` §3 P2、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(1) 消費者の強さ不足:等重みの 2 つの Poisson の混合が 2 峰になるのは $\Delta N/\sqrt N\ge2.1$〜2.6(C0 (研究ノート: `606_w_E05_428_lens_prob_horizon_poisson.py`) B、値)—— 単峰性が排除するのは $\Delta N\gtrsim2\sqrt N$ の擬交差だけで、(NFT$_{\rm s}$) は小さい $\Delta N$ の擬交差・連続の急な遷移(418 C3・C4)も禁じる;(2) 供給:$\mu$ の対数凹性は経路の重みの凸性の型で、PF の重みは対数凹でない(F175 (i));(3) PF 版の表示(跨ぐ二重確率積分の符号)は未照合。
- **共通点(1 行)**:**分布の形(単峰性)は巨視的な擬交差しか見ず、供給は凸性の段 —— F175・F224 (b) と同じ段。**
- **R9**:閉じたのは方式。双極子では $N$ は Poisson で単峰(段は空)。
- **射程(T60)**:禁じるのは「$N$・$H_f$ の分布の単峰性・対数凹性から (NFT$_{\rm s}$) を出す」発注。止めないもの:単峰性の値の偵察(類 C の (NFT$_{\rm p}$) の値)。
- **再開条件**:跨ぐ対の積分の分布の対数凹性が PF の重みで在庫に載り、かつ消費者が巨視的な擬交差の排除だけで足りる形に弱まったとき。

## F249(E05、全列の $\chi_T$ を、**Donsker–Varadhan の 3 段の変分**(定常過程 $Q$ の上の比エントロピー $\bar H(Q\mid W_\lambda)$ + エネルギー)の最小化子の一意性・強凸性で押さえる方式。2026-10-21、w_E05_428_lens_prob、稿 `428_` §3 P3、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:比エントロピーはエルゴード分解についてアフィン、エネルギー項は線形 —— 汎関数はアフィンで、強凸性は相共存(混合)の方向でちょうど落ちる;準安定な構造の定常過程の余剰は擬交差の中心でエネルギーの分裂(トンネル)。λ は二次変分を決め $W_\lambda\perp W_{\lambda'}$(相互に特異)、包絡の微分は接触項の繰り込みを要る(F213 の 399-A)。
- **共通点(1 行)**:**3 段の変分の量化の定数は準安定な構造の余剰 = トンネルの率;アフィン性は F212 (b) の「一次転移 ⟺ 非一意」の 3 段版。**
- **R9**:閉じたのは方式。双極子(Gauss)では最小化子は Gauss の定常過程で一意、余剰は 2 次で正(段は空)。
- **射程(T60)**:禁じるのは「DV の 3 段の変分(比エントロピーの凸性・最小化子の一意性)で $F''$・(REG-W) を出す」発注。
- **再開条件**:F211 の再開条件 (1)。

## F250(E05、全列の $\chi_T$ を、**時間の界面の貼り合わせ・fidelity の感受率**($\chi_T\le(\mathrm{Var}_{\psi_0}T\cdot\chi_F)^{1/2}$、$\chi_F$ = 重なり $\langle\psi_\lambda,\psi_{\lambda'}\rangle$ の 2 階 = λ と λ′ の半直線の経路測度の界面の自由エネルギー)で押さえる方式;特異性($W_\lambda\perp W_{\lambda'}$)は時間の伸縮で除く。2026-10-21、w_E05_428_lens_prob、稿 `428_` §3 P5、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(1) $H(\lambda')=\frac{\lambda'}{\lambda}(\lambda T+\frac{\lambda}{\lambda'}H_f)$ の伸縮は λ の変化を $H_f$ の尺度の変化に写し、$\delta H_f\psi_0=-\lambda\delta T\psi_0$ で $\chi_{H_f}=\lambda^2\chi_T$ —— **恒等的に循環**;経路の側の特異性は場の OU の率(定常の分散を保つと二次変分の率)へ移るだけ。(2) 伸縮なしの貼り合わせ(左右の場を独立に)は時刻 0 の場の真空の挿入で $p_0=\lvert\langle\Omega,\psi_0\rangle\rvert^2$ を払う;Poisson 混合の表示なら $p_0\ge e^{-\langle N\rangle}$、典型は $e^{-O(\langle N\rangle)}$($\langle N\rangle\gtrsim\lambda^{4/7}$、値)—— 重なりの $1-O(\delta\lambda^2\chi_F)$ に届かない。
- **共通点(1 行)**:**時間の界面の費用は場の記憶(光子の雲)の切断で、半古典の作用と同じ指数 —— F223・417 §1 と同じ段。**
- **R9**:閉じたのは方式。
- **射程(T60)**:禁じるのは「λ と λ′ の経路測度の貼り合わせ(Jensen・Gibbs の変分)や時間の伸縮で $\chi_F$・$\chi_T$ を上から押さえる」発注。
- **再開条件**:場の記憶を切らずに界面を作る表示(真空の挿入でない貼り合わせ)で、界面の自由エネルギーが λ の対数で押さえられたとき。

## F251(E05、全列の (NFT$_{\rm s}$) を、可能性の低い確率論の 3 型で出す方式 —— (a) λ→∞ の Brown の尺度極限の一意性 ⟹ $g$ の正則変動、(b) 虚時間の断熱の傾斜(Jarzynski・Crooks の虚時間版)、(c) 時間方向のキンクの気体(Peierls・反射正値の chessboard・赤外の評価)。2026-10-21、w_E05_428_lens_prob、稿 `428_` §3 P4・P6・P7、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(3 本)。
- **理由**:(a) 正則変動 ⟹ (NFT$_{\rm s}$) は偽:$g(\lambda)=\lambda^{-\theta}(1-\lambda_n^{-1/7}\sigma((\lambda-\lambda_n)/\lambda_n^{1/2}))$ は正則変動だが相対の落ち/相対幅 $=\lambda^{5/14}\to\infty$;要るのは滑らかな変動(各点の 2 階);尺度極限そのものも難問 #2 で未確定。(b) 傾斜の係数は $\int d\mu_T/E^3$ で $\chi_T=\int d\mu_T/E$ より赤外に強い;Jarzynski・Crooks は恒等式で Jensen の向きは凹性。(c) chessboard はキンクの事象の確率の上界(秩序の向き、逆);赤外の評価(Gauss の支配)は線形の観測量で $h\ge1$ を返すだけ(E05-F19 の型);キンクの費用の下からの評価は界面の切断と同じ指数。
- **共通点(1 行)**:**3 本とも量が強いか向きが逆で、各点の $\chi_T$ に届かない。**
- **R9**:閉じたのは方式。
- **射程(T60)**:禁じるのは「尺度極限・正則変動」「虚時間の傾斜」「反射正値・chessboard・Gauss の支配」で (NFT$_{\rm s}$) を出す発注。
- **再開条件**:(a) は率つきの滑らかな変動の供給(F205 の段)が出たとき;(b)(c) はなし。

## F252(E05、全列の (NFT$_{\rm s}$) を、**有限の時間の地平線の確率論の道具**(多項式の時間までの混合・集中不等式・結合・有限時間の CLT・数値の鎖)で出す方式 —— このレンズ全体の型の閉鎖。2026-10-21、w_E05_428_lens_prob、稿 `428_` §3 観察 428-A・P8、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(有限の地平線・一様ノルムの出力の型の全体)。
- **理由(観察 428-A、厳密・初等、self-audited)**:$(0,\infty)$ 上の有限正測度 μ に原子 $w\delta_{w/K}$ を足すと、$C(\tau)=\int e^{-E\tau}d\mu$ は全ての時刻で高々 $w$ しか変わらず、$\chi=\int d\mu/E$ は $K$ 増える。擬交差の中心の原子は $w=\Delta\tau^2/4$・$E=2t$、半古典では $t\lesssim E_0e^{-c\lambda^{4/7}}$(417-A)—— 多項式の地平線のどの評価も見ない。要るのは全ての時刻での $C_T$ の可積分な減衰を λ の冪の定数で出す型で、それは F174・F175・F185・F211 (d)・F212 (b) で閉;1 次元の Gibbs の理論の量的な出力は典型として相関の長さ $e^{C\lVert J\rVert}$ の型(値;F174 で $\lVert J\rVert\sim\alpha\lambda^{1/4}$〜$\alpha\lambda$)の型で、トンネルの $e^{-S}$ と同じ形。
- **共通点(1 行、レンズ版)**:**確率論の道具は有限の地平線の量か無限の時間の定性を返し、(NFT$_{\rm s}$) が要る $\chi_T=\int_0^\infty C_T$ の地平線の外の重みを量で押さえない —— それは時間方向のキンクの率 = トンネル振幅そのもの(親の共通点の確率論の側の形)。**
- **R9**:閉じたのは方式。観察 428-A は模型によらない。
- **射程(T60)**:禁じるのは「多項式の時間の混合・集中・結合・有限時間の CLT・配位の鎖の数値から (NFT$_{\rm s}$)・(REG-W) の真偽を結論する」発注(値の偵察としては止めない)。
- **再開条件**:全時間の量的な減衰を、多項式に減衰する(隙間なし)相関について λ の冪の定数で与える型が在庫に載ったとき(本稿の P1 の 2 尺度の流れが唯一の候補)。

## F253(E05、全列の類 C の否定の筋 —— 「(NFT$_{\rm s}$) を偽にする機構」の候補 2 本:(P9)1 次元の $1/r^2$ の Thouless 型の跳び(ACCN 1988)が虚時間の核の赤外の尾 $\approx4\pi/\tau^2$(F212 C0 587 J3)から起きる;(P10)λ→∞(断熱極限)で Holstein 型の自己捕獲の交差が鋭くなる。2026-10-21、w_E05_428_lens_prob、稿 `428_` §3 P9・P10、成算 S223)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**標的**(偽の向きの機構の候補として、2 本とも)。(NFT$_{\rm s}$) の真偽は閉じない。
- **理由**:(P9)ACCN の跳び(原典の抄録・§1.1 を照合:強磁性の Ising・Potts、$J\sim J_+/r^2$、$M(\beta_c)\ge(\beta_cJ_+)^{-1/2}$)は秩序変数の平均と強磁性の $r^{-2}$ の線形の結合から来る;PF の核は速度の双線形で、ℓ=0 の両構造とも速度の平均 0 —— 線形の結合が消え、揺らぎの 2 次は核の 2 乗 $\tau^{-4}$ で可和(値)。(P10)静的な横の場の中の電子のエネルギーは反磁性不等式で自由の値以上、場の費用は正 —— Born–Oppenheimer の汎関数は $A=0$ が唯一の最小;$P=0$ ファイバーでは補題 418-C;断熱極限の鋭い交差の型の帰属は Gerlach–Löwen 1991〔要確認、無料の PDF なし〕。
- **類 C の値**:418 の 5〜9%(主は C2 の準自由・相関の段の構造の梯子)を**変えない**。
- **R9**:閉じたのは標的(機構の候補)。
- **再開条件**:(P9)ℓ=0 の 2 構造が平均の違う量で核の赤外の尾と線形に結合することが見つかったとき;(P10)古典の段より上(準自由の段)で自己捕獲型の第 2 の極小が見つかったとき(418 C2 と同じ)。


## F254(E05、難問 #3 = HP-G3-1 の Q3 の上界側 —— 上界の冪 2(E05-P195)を下げる型 (U1) 試行状態(ブーストした雲・LLP の後の試行・Pizzo 型の着衣)と双対の「$h\le1+C\langle N\rangle$」、(U2) 和則・Ward(f-和則の高次)、(U3) Cramér–Rao の方向の最適化、(U4) $\Phi_c$ の $k$ ごとのレゾルベントの上界、と逆向きの比較 $h_{\rm ls}\le Ch_{\rm sr}$((H-curv) の量化版)を (R1) Dybalski–Spohn 2020 の型(CLT + スペクトル)、(R2) Polzer 2026 Thm 3 の型($\lvert P\rvert^2$ の凹性 + 真空の重みの右連続)、(R3) 光子質量の正則化、(R4) 凹性・正値性・反磁性で、さらに (E1) 強結合(Brooks–Seiringer)・(E2) 単調性で出す方式。2026-10-21、w_E05_434_p3_upper_hls = 書き下しの型、稿 `434_難問3_増大則の上界と逆向きの比較_2026-10-21.md` §2・§3、成算 S229、C0 636)
- **注記(2026-10-21、w_E05_498、稿 `498_`)**:ジョブ 490 の非摂動の値 $\Phi_c$ = 1.581・5.320・17.42(λ=32・64・128、α=1)、局所冪 1.751 ± 0.061・1.711 ± 0.037(札 ABOVE_3HALF)。同じ λ の 1 ループの局所冪は 1.640・1.593(C0 905)で、1 ループの形でも札は ABOVE —— 札は (1) の「U3 の型の天井は値で冪 3/2」(漸近の 1 ループ)を否定しない;非摂動/1 ループの比は 0.66→0.77(1 未満)で、局所冪の超過 0.11 は格子の刻みの系統の幅の内。再開条件 (4) は F182 (1) を「上界の冪 3/2」と引くが、F182 (1) の字面は「λ の 1 次」—— 1 次版は値で偽の向き(F-?、稿 498)、3/2 版は値で否定されない。

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(上の 10 候補)。命題(上界の冪・逆向きの比較・(H-curv)・真の冪)の真偽は閉じていない。U1 の双対形「$h\le1+C\langle N\rangle$、C は α に依らない」だけは**真偽**(小さい α で偽)。
- **理由(厳密 + 原典 + 値)**:(1) **上界**:冪 2 は 369-1 の $\Phi_c$(反跳の各 $k$ に TRK 369-A の $\le m$)。U1 の試行は $E(P)$ の上界 ⟹ 曲率の上界 ⟹ $h$ の下界で向きが逆;双対形は $P=0$ で 1 光子の生成が横波性 $k\cdot\varepsilon(k)=0$ で消えるので $\langle N\rangle_0=O(\alpha^2)$、一方 $h-1=\frac{8\alpha}{3\pi}\ln(1+\frac\lambda2)+O(\alpha^2)$。U2 は $S_{-1}=G$ の上界に励起の下限(ギャップ)が要り、Cauchy–Schwarz は $S_{-1}\ge S_0^2/S_1$ の向き。U3 は局所核の上の反跳の二次形式で端点の条件からランプが定数倍まで最適(雑な議論)、改良は $\Phi_c$ の非摂動の評価だけで、その 1 ループの値は $0.0176\alpha^2m\lambda^{3/2}$(NUM-6721)—— この型の天井は値で冪 3/2。U4 は $\lVert u_k\rVert^2\lt m(E(k)-E_0)\le m\lvert k\rvert$(366-A)が要り、値で $\lVert Q\psi_0\rVert^2\sim2m\langle T\rangle_0$、$\langle T\rangle_0\sim E_0\gg\Lambda$。(2) **逆向きの比較**(観察 434-A):問いは各 λ の赤外の問い;光子質量 μ\gt0 では Kato の (A) 型の解析族で $h^\mu_{\rm ls}=h^\mu_{\rm sr}$ が自明、μ に一様な曲率の下界が標的そのもの(R3)。DS2020 Thm 3.2(本機の原典)は Condition C(ii) $\omega\ge c_0\gt0$ と Lemma 3.1 の孤立固有値・$\lvert\langle\Omega,\psi_P\rangle\rvert\gt0$・解析性が要る(R1);Polzer 2026 Thm 3 (2)(本機の原典)は Nelson 型(完全単調・Bernstein)の $\lvert P\rvert^2$ の凹性と $\rho(P)$ の $P=0$ での右連続が要り、PF では凹性の道具が移らず(F169)、$\rho(0)\gt0$(Hasler–Siebert 2021)と $\nabla E\ne0$ の点の $\rho(P)=0$(Hasler–Herbst 2008 Thm 3)で右連続が落ちる(R2);PF の経路測度の CLT は文献に無い(Betz–Hiroshima 2009 は無限体積の存在だけ)。観察 434-B:CLT を仮定しても、極限の曲率 = $\frac1{2mh_{\rm sr}}$ ⟺ 底の窓 $[E(p),E(p)+\eta p^2]$ の $\psi_0$ のスペクトルの重みの liminf が正 —— 後者は CLT の下で標的と同値。R4 は全て $E$ の上界か $E(P)\ge E_0$。(3) E1:Brooks–Seiringer 2022 Part II は光学フォノン(ギャップ)と Pekar の強結合極限;E2:単調性は F170。
- **値(【T88】、C0 636)**:416 の長い窓の推定量で局所冪 0.98 ± 0.22(衛生の外)、$h_{\rm eff}(t)$ は t=1・2・4 で 0.55・0.60・0.65 —— 予想の冪 1/2・4/7・3/5 は値で下側。閉鎖の理由は (1)〜(3) で、値は使わない。
- **共通点(1 行)**:**上界の冪は「$\lvert k\rvert\sim\Lambda$ の反跳のスペクトル測度の非摂動の抑制」(F182・F226 と同じ段;Cramér–Rao の型の天井は値で 3/2)、逆向きの比較は「固定の切断の赤外 —— 経路測度の CLT と、底の窓の $\psi_0$ の重み(赤外粒子の着衣の重なり)」で止まる;E05 の紫外の在庫はどちらにも触れず、試行状態・凹性・和則は向きが逆。**
- **R9**:閉じたのは方式。双極子では CLT は厳密で底の窓の重みも 1 に戻る(赤外の対数を $p^2$ が殺す)—— 段は空;2 構造の擬交差の梯子では固定の λ で $\Delta\gt0$ なので底の窓の重みは真。障害は「無質量の赤外」と「非摂動の $\Phi_c$」に局在し消滅していない。
- **射程(T60)**:禁じるのは「試行状態・凹性・和則・正値性・光子質量の正則化だけで $h$ の上界(冪 2 未満)や $h_{\rm ls}\le Ch_{\rm sr}$ を出す」「DS2020・Polzer 2026 の型を無質量 PF に字面で移す」形の発注。止めないもの:PF の経路測度の CLT そのもの;赤外粒子の着衣の重なりの評価;$\Phi_c$ の非摂動の値の測定(値の問題として);小さい α・固定の Λ の既知の $E''(0)$ の式と $1/(mh_{\rm sr})$ の字面の照合(類 A)。
- **再開条件**:(1) PF の経路測度の拡散の尺度の CLT(特性関数の形)が文献か在庫に出たとき、かつ (2) 底の窓 $[E(p),E(p)+\eta p^2]$ の $\psi_0$ の重みの下界(赤外の着衣の重なり)が出たとき —— 434-B で $h_{\rm ls}=h_{\rm sr}$;(3) PF で $\lvert P\rvert^2$ の凹性 (LC-PF) と $\rho$ の右連続の代わりの量が出たとき(Polzer の型);(4) F182 の再開条件 (1)(上界の冪 3/2)。


## F255(E05 の外・難問 #1 の弱い構成 (K1):裸の位置 $x$ ―― および LLP の変換の後の全運動量に共役な座標(= $x$ 自身)―― の P=0 の経路を物理の時刻で緊密にし、Prokhorov の弱い極限でくりこまれた経路測度を作る方式。2026-10-21、w_E05_432b = 書き下しの型〔w_E05_432_p1_construct の再開〕、稿 `432_難問1_くりこまれた模型の構成の弱い形_2026-10-21.md` §9・§10 (i)、成算 S227)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(値の判定で否定寄り【T88】;弱い極限の存在の真偽は閉じない)。
- **理由**:(1) 432-B (i)(E05-P220)で物理の時刻の分散は $V_{\rm phys}(t)=\frac t{m_{\rm ph}}\cdot\frac1{r(\lambda)}$、$`r=h_{\rm eff}(\lambda;t\,m_{\rm ph}/h)/h`$。(2) 在庫の HMC(571b 表 A、α=1・T=6、λ=32・64・128)で $r_c$($c=1,2,4$)は λ に減り、$\log r_c$ の傾き $-0.369\pm0.005$・$-0.333\pm0.005$・$-0.288\pm0.005$ —— 起動前に固定した札 **NOT_TIGHT_LEAN**(C0 627);$\hat h$ を短い時刻に替えても全て負。1 ループ(626)の向きと一致。(3) LLP の $U=e^{iP_f\cdot x}$ は $x$ と可換なので、LLP の重心の座標は $x$ 自身で同じ所に止まる(432-D (i));強い位相は 432-A(F230)で既に閉。
- **共通点(1 行)**:**くりこみ族の物理の時刻は固定の裸質量の模型の短い時刻 $`t\,m_{\rm ph}/h\to0`$ に当たり、そこでは低い運動量の光子の着衣が済んでいない —— 裸の位置は族の物理の時刻で広がり続ける。**
- **R9**:閉じたのは方式。双極子では族が終端して段は空;着衣の座標(432-D)ではこの障害は比 $h_{\rm ls}/h_{\rm sr}$ に移り、消滅も確定もしていない。
- **射程(T60)**:禁じるのは「裸の位置(または LLP の座標)の経路の緊密性・弱い極限で #1 を構成する」発注。止めないもの:着衣の座標(432-D)の経路、逆向きの比較 $h_{\rm ls}\le Ch_{\rm sr}$。
- **再開条件**:λ=256 以上の短い時刻の $h_{\rm eff}$ の曲線で $r$ の傾きが 0 に向かう(平らになる)こと;または値の推定量の系統(T=6 の有限 T、領域 A)が傾きを作っていると分かったとき。
- **再開条件の照合(2026-10-21、監査 449 §0′、監査人の C0 (研究ノート: `audit449_F255_r256.py`) → `_result.json`、light_house_73 が書き写し)**:再開条件の前半「λ=256 以上の短い時刻の $h_{\rm eff}$ の曲線で $r$ の傾きが 0 に向かう」は **NOT_MET**。426 の λ=256 の曲線で $r_c$ の 1 オクターブごとの傾き(32→64・64→128・128→256)は c=1 で −0.33・−0.40・**−0.60±0.02**、c=2 で −0.29・−0.36・**−0.56±0.01**、c=4 で −0.25・−0.32・**−0.50±0.01**(傾きは平らになるどころか急になる向き)。門(t=2・4 の局所冪 0.6074・0.6463 の再現)は通過。値であって上下界ではない【T88】。後半「T=6 の窓の系統」は 446 の回収時に 1 行で照合する(未了)。
- **再開条件の後半の照合(2026-10-21、監査 457 §2 項目 3、light_house_73b が書き写し)**:再開条件の後半「値の推定量の系統(T=6 の有限 T、領域 A)が傾きを作っている」は **NOT_MET**。族 T(稿 446、NUM-6938・6939)で T の窓の系統は $\lvert\delta p_T\rvert\lesssim0.003$、刻みの系統は保守でも 0.023 で、$r_c$ の 1 オクターブの傾き −0.50〜−0.60(NUM-6944)を作る大きさに 1 桁以上届かない。446 は $t=1$ の量で測ったもので、$r_c$ の時刻 $t=c/\hat h\approx0.1\sim0.4$ への当てはめは読み。前半(監査 449 §0′)と合わせ、F255・F232 の再開条件は全て NOT_MET。値であって上下界ではない【T88】。


## F256(E05、全列の (NFT$_{\rm s}$) を、**Gerlach–Löwen 1991・Löwen 1988 の解析性の定理の型**(HVZ 型の連続スペクトルの端で孤立 + 正値性の改良で一意 + Kato の型 (B) の正則族で実解析)を PF の λ に移して供給する方式 —— F239 の原典照合。2026-10-21、w_E05_429b(= w_E05_429_lens_analytic の続き、書き下しの型)、稿 `429_全列_複素解析と作用素論のレンズ_2026-10-21.md` §7)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((NFT$_{\rm s}$)・全列の真偽ではない)。
- **理由**:(1) 原典の出力は**定性**(札 QUAL):GL 1991 Statement 1 は条件 (3.1)(光学の分散 $\omega(k)\ge\omega_0\gt0$・劣加法性)の下で $E(\alpha,Q)$ が孤立・単純で $0\lt\alpha\lt\infty$ の実解析関数 —— 複素の半径の結合・質量の冪の形はない;Statement 3(自由エネルギー)は有限温度の正値の級数;Löwen 1988 も光学フォノンの基底状態で同じ型。音響(無質量)の分散の基底状態はどちらも扱えないと明記。(2) 型の移植:正値性の改良と Kato の型 (B) は PF の $P=0$ ファイバーで成り、孤立は光子質量なら (3.1) を満たす —— 移る出力は「光子質量つきの $E_0(\lambda,\mu)$ の定性の実解析性」で、観察 429-U(E05-P221)の証人が全て満たし、その証人で (NFT$_{\rm s}$) は偽。(3) 原典の模型は密度型の頂点 $g(k)a(k)e^{ik\cdot r}$ で、$A$ は一様磁場だけ —— 量子化された場との速度結合の議論はない。
- **共通点(1 行)**:**相転移の不在の定理は有限の結合での真の非解析性を排除する定性の命題で、λ→∞ で幅の縮む擬交差の量を与えない;証明の隙間は光学フォノンの $\omega_0$ から来て、無質量では前段から立たない —— F208 (c)・F212 (b) の段。**
- **R9**:閉じたのは方式。**射程(T60)**:「ポーラロンの相転移の不在の定理(GL・Löwen 型:孤立 + PF + Kato)を PF の λ・光子質量に移して (NFT$_{\rm s}$)・(REG-W) を出す」発注。
- **F212 の再開条件 (3) の判定**:原典は入手・照合済みで、速度結合への拡張の議論は無い —— 再開条件は満たされず、**F212 は閉じたまま**。
- **F239 への訂正注記**:F239 の見出しと理由 (2)(3) の「虚時間の 1 次元の有効系」は原典を読む前の推測で、基底状態の定理の証明は作用素論(稿 429 §7.2)。F239 の判定(方式の閉鎖)は不変。
- **再開条件**:無質量の分散で孤立なしに解析性の領域の幅を結合の冪で下から押さえる定理が出たとき(原典の時点では存在しない);それでも 429-U の型の外の入力(トンネル振幅の量)が要る。


## F257(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕を、**物理のレンズ(対称性・半古典の勘定・磁場の描像・尺度の離散性・離散化・重み直し・対数凹性)** で供給・制限する方式 —— (Q1) 対称性の量子数で擬交差の候補を減らす、(Q2) 半古典の作用 $S$ と窓 $\lambda^{-1/7}$ の勘定、(Q3) 準自由・コヒーレントの段からの擬交差の議論、(Q6) $[\pi_x,\pi_y]=-ieB_z(0)$ の Landau 準位の描像で競合を最低準位に制限、(Q7) 離散的な尺度不変性(対数周期・Efimov 型)、(Q8) 離散の殻の玩具の擬交差を連続の模型の向きに使う、(Q9) 経路積分の重み直しで $g(\lambda)$ を連続に、(Q10) 基底状態の Q 空間の対数凹性(Brascamp–Lieb 型)、(Q11) 結合数域 $W(T,H_f)$ の境界の曲率、(Q12) 多フレーバーの極限($N_f$ 個の場)の平均場。2026-10-21、w_E05_431_lens_physnum = 書き下しの型、稿 `431_全列_物理と数値のレンズ_2026-10-21.md` §2・§3、worklog (研究ノート: `2026-10-21_w_E05_431_lens_physnum.md`) §2・§3、成算 S226、C0 621・622・623)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(10 角度)。(NFT$_{\rm s}$)・(REG-W)・全列の真偽、擬交差の存在・不在は閉じていない。
- **理由**:(Q1) E05-F22(非縮退・回転不変・偶)と P207(ノルム連続)で基底状態の 1 次元表現は λ に依らず一定(観察 431-A、self-audited)—— 擬交差の 2 構造は全ての量子数が同じ部分空間の 2 枝で、梯子の指標は量子数になり得ず、対称性は振幅の大きさを言わない(0)。(Q2) 2 準位で (NFT$_{\rm s}$) を割る閾 $S_*\approx(0.3\sim0.7)\ln\lambda$、擬交差の幅が 403-A の窓より狭くなる閾も同じ桁(C0 622)—— 存在の問いを動かさない言い換え(0)。(Q3) 平均 0 の準自由状態では横波性で交差項が消え、準自由・その変位・コヒーレントの試行は λ の 1 次(F227 (U1) の値・418-C)、$E_0\le C_U\lambda^{5/7}$ は $P_f$–$A(0)$ の集団のもつれ —— 準自由の段は基底状態の桁を再現しない;初等に出るのは $\langle H\rangle\ge c\sqrt{\alpha\lambda}$(不確定性)だけで P158 より弱い(0〜1%)。(Q6) 作用素の不等式は $\pi_x^2+\pi_y^2\ge\pm eB_z(0)$ だけで、回転不変な状態で期待値 0;作用素値の $B(0)$ は π と非可換で Landau の床の作用素の形が無い(1%)。(Q7) 鋭い切断で尺度は固定、離散の内部尺度なし;412a の κ_j の 4 段では周期と雑音を分けられない(1% 未満)。(Q8) 離散の殻の「担う殻の切替」は離散化の人工物で、連続の模型に移らない(否定・肯定の両向きで)(1% 未満)。(Q9) 刻み $N=64\lambda$ で重みの比の対数の分散 $\approx\frac N2(\Delta\lambda/\lambda)^2$、使える幅 $\lesssim1/\sqrt{32\lambda}$;連続極限で Wiener 測度が互いに特異;段の検出は粗い格子で足りる(0)。(Q10) $P_f$ は Q 空間で 1 階の回転の生成子(磁場型)で凸ポテンシャルの形にならない(PF の正の錐の表示でも);経路の側は F175 (i)・F183(0)。(Q11) 結合数域は凸で、急な落ち ⟺ 下側の境界のほぼ平らな辺、その「ほぼ」の量は支持点の $\chi_T$ —— 境界は $F$ の Legendre 変換で 406-U の段(0)。(Q12) 光子場は経路に線形に結合した Gauss 場で $N_f$ 個の和は元と同じ 2 次形式;集団の場以外は x 空間で分離し、$P=0$ で $E_{\rm orig}(-q)+H_{\rm others}\ge E_{\rm orig}(0)$(E05-F23)ゆえ基底エネルギーは元と同じ —— $1/N_f$ の展開は無い(0)。
- **共通点(1 行)**:**物理のレンズの道具は、どれも「擬交差の 2 構造は同じ量子数の部分空間の 2 枝」という段に落ち、その 2 枝の間の振幅の大きさ(縮約の余りの $\chi_T$)に触れない —— 対称性は枝を分けず、半古典の勘定は存在の問いを言い換え、Gauss の段(準自由・コヒーレント)は基底状態の桁を再現しない。**
- **R9**:閉じたのは方式。難しさは 424 の移り先「余りの静的な感受率 $\chi_T$」に留まる(消滅ではない)。その記述を訂正する(読み 431-R、値):余りを評価すべき段は準自由の有効汎関数でなく、$P_f$ と $A(0)$ の集団のもつれ(300-C の (II) 型、F227 の再開条件 (1)・S178)。双極子(交差項なし)では移り先の段は空。
- **射程(T60)**:禁じるのは「Q1〜Q3・Q6〜Q12 の型で (NFT$_{\rm s}$)・(REG-W)・全列を出す、または擬交差を排除・制限する」発注。止めないもの:類 C の値の判定(ジョブ `g3_e05_431_hysteresis`〔[64,128]〕と、その GPU 版 [128,256]);$P_f$–$A(0)$ の集団のもつれの段での余りの $\chi_T$ の定式化;412b の回収(ただし Q8 のとおり、多モードの玩具の擬キンクは連続の模型の否定にならない)。
- **再開条件**:(1) 作用素値の $B(0)$ の「最低準位への射影」を作用素の形で定義し、射影した問題の隙間を λ の冪で押さえる道具が立ったとき(Q6);(2) 集団のもつれの段の有効の記述(縮約先)が、エネルギーの桁 $\lambda^{5/7}$ を再現する形で同定されたとき(Q3、F227 再開 (1) と共通);(3) ジョブ 431(または GPU 版)が COUNTEREXAMPLE を出したとき(類 C の側の再開、415 §5 の再開条件 (a))。
- **成算**:S226(証明の道はなし、12 本とも 1% 以下;類 C の値の道はあり)。


## F258(E05、難問 #2(HP-G3-1 の Q2):自己エネルギー $E_0$ の冪を、(K2)連続体に忠実な少数モードの圧縮(補題 433-D)の厳密な対角化の最良値で 5/7 より下げる証拠を作る、(K3)LL 1999 の積状態の族の中で 5/7 を割る、(K6)Feynman–Kac の大偏差(Donsker–Varadhan)で冪を決める —— 方式。2026-10-21、w_E05_433_p2_exponent2 = 書き下しの型、稿 `433_難問2_自己エネルギーの冪の新しい角度_2026-10-21.md` §2・§4、成算 S228)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**($E_0$ の冪の真偽ではない)。
- **理由(厳密 + 値)**:(K2)補題 433-D:部分 Fock 空間への圧縮は反跳の分散項 $\frac\lambda2d\Gamma(Q\lvert k\rvert^2Q-\sum_i(Qk_iQ)^2)\ge0$ を必ず持ち、固定のモード集合では $\inf\sigma$ の圧縮した運動エネルギーが正なので λ の 1 次;5/7 を割るにはモード数 $\sim\ell^3\sim(\lambda/\alpha)^{3/7}$ の多モードのもつれが要り少数モードでは読めない。値(C0 634):11 モードで局所冪 → 1、交差項の利得は相対 0.06%(α=0.1)・2.7%(α=1)。(K3)LL の積状態 $\varphi\otimes\Psi$ の場のエネルギーは厳密に $\frac12\mathrm{Tr}[\sqrt{-\Delta+\alpha\varphi^2}-\sqrt{-\Delta}]$(LL (2.22))で、最適の点($\alpha\varphi^2\gg k^2$)では平方根の劣加法性の段は定数しか失わない;積状態は $\langle p\cdot A\rangle=0$ で P191(365-A)の族 —— 5/7 は族の中で最適。(K6)Jensen は上界(自由な経路の 1 次の値 $c_1\alpha\lambda$)しか出さず、下界は正値性・Gauss の優越が要り 298-D の鎖の型(F161 (1))に戻る。
- **値の裏づけ(【T88】)**:(研究ノート: `634_w_E05_433_p2_exponent2_faithful_compression.py`)(PASS)。閉鎖の理由は圧縮の恒等式と在庫の段の照合で、値の大きさは使わない。
- **共通点(1 行)**:**少数モード・積状態・自由な経路の Jensen はどれも「場と電子のもつれのない族」か「モード数が λ で増えない族」で、5/7 と 2/3 の差(λ の 1/21 乗)を作る多モードの集団の配置に届かない;忠実な圧縮では戯画の「奇の割合 → 1」(F203 (ii))が消える。**
- **R9**:閉じたのは方式。双極子では交差項が無く(段は空);障害は多モードのもつれに局在(F227 と同じ)。
- **射程(T60)**:禁じるのは「固定の少数モードの圧縮の最良値の局所冪」「積状態の族の改良」「Jensen・自由な経路の大偏差」で冪を決める形の発注。止めないもの:モード数を $\ell^3$ で増やす忠実な圧縮の DMRG(費用は 392 の GPU の格子より重い);K1(配位表示の BO + (MAG))。
- **再開条件**:(1) 忠実な圧縮でモード数 $\gtrsim(\lambda/\alpha)^{3/7}$ を扱える多モードの解法(DMRG の結合次元の見積もりが 392 の費用を下回る);(2) Gauss の優越・正値性の新しい道具が経路の作用の下界に出たとき(K6)。
- **成算**:S228(K2 2%、K3・K6 1% 未満)。

## F259(E05、難問 #2 の下界側:LL 1999 Thm 1.2 の場の側の不等式 $H_f\ge\Lambda^6\int w(x-y)A(y)^{-2}dy-\Lambda^4\int w$ を、そのまま全模型の配位表示の Born–Oppenheimer の下界(補題 433-B)に入れて 5/7 の下界を出す方式。2026-10-21、w_E05_433_p2_exponent2 = 書き下しの型、稿 `433_` §3 観察 433-C、成算 S228)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(K1 の方式全体ではない —— 速い部分 $A_\gt$ への置き換えは開いたまま、律速 (MAG))。
- **理由(厳密)**:観察 433-C:有界な台の $w$ で、ほぼ一様な大振幅の配位 $\lbrace\sup_{B_{2R}}\lvert A-c\rvert\lt\delta\rbrace$(Cameron–Martin 空間の閉包が台なので正の測度)の上で、試行 $e^{-iec\cdot x}\phi_R$ により電子の側はゲージで $\lambda(C/R^2+e^2\delta^2)$、場の側の罰は $\Lambda^6\lVert w\rVert_1(\lvert c\rvert-\delta)^{-2}$ —— ess inf は $-\Lambda^4\int w$ 以下で自明。障害は交差項でなく、$1/A^2$ の罰がゲージで消える大振幅(遅いモード)を罰しないこと。
- **共通点(1 行)**:**LL の偶模型の機構は配位ごとの古典の議論で、全模型ではゲージの自由度が $A$ の大きさの罰を無効にする —— 罰はゲージ不変な量(速い部分・磁場)で書く必要がある。**
- **R9**:双極子では $A(0)$ が一様で、BO の下界はゲージで常に自明(内容は Born–Huang の項にある)—— 障害は全模型の遅いモードに局在。
- **射程(T60)**:禁じるのは「$1/A(y)^2$ 型の場の側の罰を、全模型の BO にゲージ不変な量へ替えずに入れる」形。止めないもの:$A_\gt$・$\mathrm{curl}A$ の罰に替えた版(稿 433 §5、ジョブ `g3_e05_433_mag_adversary`)。
- **再開条件**:なし(言明は厳密;直した版は K1 として開)。
- **成算**:S228。


## F260(E05、難問 #1・#3 の合流点 —— 逆向きの比較 $h_{\rm ls}\le Ch_{\rm sr}$(Q の有界性)を、(0) 類 A の照合(小さい α・固定の切断で文献の $E''(0)$ の式 $=1/(mh_{\rm sr})$)と、(U-ms 安い版) FP 2010・CFP 2009 の評価の黒箱の組み合わせ、(M-IR) 赤外の単調性、(R-μ) 光子質量・赤外切断の正則化、(X-ex) 435-A の近似固有ベクトル版、(P-pos) 正値性、(C-lit) PF の経路測度の CLT の文献、(D-msd) $\mathrm{MSD}_Y$ の凹性、(F-sh) Feshbach、(PT-N) 引き戻しと光子数の一様な上界で出す方式。2026-10-21、w_E05_435_reverse_compare = 書き下しの型、稿 `435_逆向きの比較_hlsとhsr_2026-10-21.md` §1・§4、成算 S230)
- **親注記(2026-10-21 02:5x、G3 第 73 陣)**:再開条件 (1)(U-ms)は第 2 段 `w_E05_435b` で済 —— 定理 435-F(E05-P228、self-audited、稿 `435_` §17〜§21):FP 2010 の範囲(λ≈1・α≤α₀)で $h_{\rm ls}=h_{\rm sr}$。S2 は `audit_S2_435`(監査稿 `440_`)。

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたのは: 方式**(上の 10 本)と、(0) の**標的の置き方**「文献 + 在庫の合成で小さい α の $h_{\rm ls}=h_{\rm sr}$」(類 A でなく類 B)。命題(小さい α の等号・一般 α の Q の有界性・(H-curv))の真偽は閉じていない。U-ms の本体(FP の帰納法の中で $\eta^{(\sigma)}$ のスペクトル測度を尺度ごとに追う書き下し)は開。
- **理由(原典 + 厳密 + 値)**:(0) Hiroshima–Spohn 2005(模型は E05 と同一)は赤外切断 κ > 0 で $m/m_{\rm eff}=1-\frac2mG_{\rm sr}$(Lemma 3.1)を示し、κ=0 は式 (1.13) の直後で「We assume that this formula remains valid also when κ = 0.」と仮定;BCFS 2007 は繰り込み群の比 (14.15) で σ > 0 だけ同定(Thm 15.1)、σ→0 の交換は Condition 14.8 の仮定;Chen 2008(スピン 1/2)・Fröhlich–Pizzo 2010 は $\partial^2E^{(\sigma)}$ の σ→0 の極限の存在だけで、極限を σ=0 の $G_{\rm sr}$ で書かない。合成で出るのは 435-D($\Sigma_0=1-2\lim G^{(\sigma)}$)と 435-L(下半連続)で、合わせて P198 の向きだけ。(U-ms 安い版) 稿 §4.1:ギャップ由来の $\lVert\eta^{(\sigma)}\rVert\le C/\sigma$ と FP Lemma III.2 の差の評価を中間尺度で繋ぐと、第 2 項が $\sigma_J\gg\epsilon$、第 3 項が $\sigma_J\ll\epsilon^4$ を要り両立しない(冪の不足)。(M-IR) 経路積分の再重みづけ $e^{-V_{\lt\sigma}}$ で分散が減る相関不等式は PF に無い(F169);C0 642 は反例なし(値)。(R-μ)・(X-ex) は (U) に帰着。(P-pos) 正値性は底のスペクトルの形に触れない。(C-lit) Betz–Spohn 2005 はスカラーの対ポテンシャル・赤外条件つき、「$D^{-1}$ は物理的に有効質量」は定理でない;PF の CLT は文献に無く、在っても 434-B (ii) が要る。(D-msd) 凹性は 367-A で只だが曲率に届かない。(F-sh) 無質量でギャップなし。(PT-N) 光子数の一様な上界は $\int\mu\ln(1/e)$ の型で、要る $\int\mu/e$ に 1 冪足りない。
- **共通点(1 行)**:**変分・下半連続の側(P198 の向き)は只、逆向きは「赤外切断 σ→0 で $v=\pi_z\psi_0$ のスペクトル測度の底の窓の $1/e$ の重みが逃げない」(U)(434-B (ii) の κ 版)に集まり、文献の多尺度は $G^{(\sigma)}$ の値の収束までで底の窓の位置を追わない。**
- **R9**:(U) は 435-D の下で標的と同値(名指しにしない)。双極子では (U) は真(1 ループの積分が σ について連続);2 構造の擬交差の梯子(固定 λ、ギャップ Δ > 0)でも真;偽になるのは底に重い枝が集積する場合で F225 の再開条件 (3) と同じ形。
- **再開条件**:(1) FP 2010 §II〜III の帰納法に $\nu^{(\sigma_j)}([\rho\sigma_k,\rho\sigma_{k-1}])\le C\alpha$($k\le j$、j に一様)を足す書き下し(U-ms、成算 2 割);(2) PF の経路測度の CLT と底の窓の重みの下界が文献に現れたとき;(3) PF の Gibbs 測度の赤外の再重みづけの相関不等式(M-IR の道具)。
- **射程(T60)**:禁じるのは「文献の $E''(0)$ の式の照合だけで σ=0 の $h_{\rm ls}=h_{\rm sr}$ を出す」「ギャップ由来の評価と $G^{(\sigma)}$ の差の評価の組み合わせで (U) を出す」形の発注。止めないもの:U-ms の帰納法の書き下し;小さい α・λ≈1 以外への 435-D の移送(FP の Λ 依存の定数の追跡)。


## F261(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕を、**擬交差の相手の低エネルギーの重み $\mu_T^{(\lambda)}([0,\epsilon])$ を隣り合う λ の間で比べる型**(連続性・単調性・ある λ の重みが近くの λ の重みを支配する不等式)で供給する方式(R1)。2026-10-21、w_E05_436_lowenergy_weight = 書き下しの型、稿 `436_全列_低エネルギーの重みの3角度_2026-10-21.md` §2、成算 S231、C0 647)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((NFT$_{\rm s}$)・(REG-W)・全列の真偽ではない)。模型によらない比較の命題は**偽**(観察 436-A)。
- **理由**:$T\ge0$・$H_f\ge0$ の線形の族の 2 準位($T=\mathrm{diag}(\tau_1,\tau_2)$、$H_f$ の非対角 $-t$)で $\mu_T^{(\lambda)}=w \delta_E$、$E=\sqrt{\Delta\tau^2(\lambda-\lambda_c)^2+4t^2}$、$w=\Delta\tau^2t^2/E^2$(厳密)—— 相対幅 $s$ の比較が全ての $t$ で立つにはエネルギーの窓 $\ge s\lambda_c\Delta\tau$($\le sE_0$)が要り、同じ窓なら定数 $\ge1+(s\lambda_c\Delta\tau/2t)^2$。ゆえに比較が届くのは励起 $\gtrsim sE_0$ の側だけで、補題 430-A・系 430-A1(割線)・403-A と同じ双対(窓の相対幅 $s$ ⟷ エネルギー $s\lambda\Delta\tau$)。模型固有の比較で定数を λ に一様に置く条件は 2 準位で $t\gtrsim s\lambda\Delta\tau$ = (NFT$_{\rm s}$) の言い換え。値:浴つきの確率的な玩具(C0 647 B)で尖りの半値幅は 2 準位の予言と 1% で一致、浴は尖りを均さない;598b・412b は有限モードで隙間があり問いに答えない。
- **共通点(1 行)**:**λ の近くの比較は、比べる窓の相対幅 $s$ に応じてエネルギー $\gtrsim s\lambda\Delta\tau$ の部分しか見ず、壁 $[0,sE_0]$ の重みを見ない —— 割線(F241)と同じ段。**
- **R9**:閉じたのは方式。双極子($\mu_T$ は滑らか)では比較は空に成り立ち、擬交差の梯子の候補では定数がトンネル $t$ に依る。名指しにしない。
- **射程(T60)**:禁じるのは「低エネルギーの重み・$\chi_T$ を隣の λ の値・窓の平均・摂動で比べて (NFT$_{\rm s}$)・全列を出す」発注。止めないもの:t の下界を与える型(F223 の再開条件)。
- **再開条件**:(1) F223 の再開条件 (1)(トンネル振幅の量的な下界);(2) 擬交差の原子だけを取り出す入力($\mu_T$ の $[0,sE_0]$ の部分を滑らかな背景から分ける量)が立ったとき。
- **成算**:S231(なし、0〜1%)。

## F262(E05、全列の $\chi_T$ を、**$H_f$(または $N$)を粗い変数にした 2 尺度の双対の変分**(Thomson の上界 = 粗い 1 次元の Hardy・Muckenhoupt の部分 + 条件付きの細かい部分;稿 428 §4 の P1 の次の 1 手、F247 の射程が止めなかったもの)で上から押さえる方式(R2)。2026-10-21、w_E05_436_lowenergy_weight = 書き下しの型、稿 `436_` §3、成算 S231、C0 648)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(I1) $\delta H_f\psi=-\lambda\delta T\psi$ で被駆動の関数は $H_f$ の関数;粗い試行 $g(H_f)\psi$ に制限した Dirichlet $\bar\chi$ は $\chi$ の下界、残り $\chi-\bar\chi$ は最適な粗い試行の残差の $(H-E_0)^{-1}$ ノルムに等しい(観察 436-B、厳密)。ゆえに 2 尺度の上界は「粗い部分の入力 = $H_f$ の周辺の谷の伝導度の下界」と「細かい部分 = 同じ $H_f$ の層の中の条件付きの隙間」の 2 つを要し、トンネルはどちらかに必ず移る。値(C0 648、確率的な玩具):2 構造が y でも分かれると $\bar\chi/\chi\propto t$(巨視 ΔM=12:0.40 → 6.3·10⁻⁴、微視 ΔM=2:0.83 → 2.3·10⁻³)で隘路は細かい部分;構造 = $H_f$ の単一の鎖では $\bar\chi=\chi$ で谷の伝導度が t とともに下がる(8·10⁻⁷ → 3.6·10⁻¹⁰)。粗い谷の下界は F248(単峰性・凸性)の段、細かい部分は無質量で隙間なし(F247 (1) の隘路)。Fock の玩具(598b・412b)は Fock の基底で確率的でない(負の伝導度 5〜38%)。
- **共通点(1 行)**:**2 尺度に分けてもトンネルは消えず、細かい部分(構造の切り替え)か粗い周辺の谷のどちらかに移る —— $H_f$ は構造の変数でない;F247・F248 と同じ段。**
- **R9**:閉じたのは方式。双極子では $H_f$ の周辺は単峰で細かい部分も Gauss(段は空)。
- **射程(T60)**:禁じるのは「$H_f$・$N$ を粗い変数にした 2 尺度の Thomson・Kipnis–Varadhan・容量の上界」の発注。止めないもの:構造の変数の同定(F247 再開 (1))。
- **再開条件**:(1) F247 の再開条件 (1)(構造の変数の同定と、その周辺の谷の深さの λ の対数の評価);(2) 同じ $H_f$ の層の中の条件付きの隙間を λ の冪で押さえる入力。
- **成算**:S231(なし、0〜1%)。

## F263(E05、全列の余りの $\chi_T$〔縮約の余りの 2 階、F228 再開 (1) の量〕を、**$P_f$–$A(0)$ の集団のもつれの段(300-C の (II) 型、431-R の移り先)で 1 つの量として書き、在庫(P158・P167・P201・P206)と冪の勘定で上から押さえる方式**(R3)。2026-10-21、w_E05_436_lowenergy_weight = 書き下しの型、稿 `436_` §4、成算 S231)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**、加えて**標的の側の未定義**((II) 型の段の縮約が未構成で「余り」が定義されない)。
- **理由**:(a) 冪の勘定:滑らかな部分は $\lvert F''\rvert\approx M/\lambda^2$、$R\approx\alpha\lambda/M^2\le\alpha c_1^{-2}\lambda^{-1/7}$(403-A の閾そのもの);余りには $M^2/(\alpha\lambda)\in[\lambda^{1/7},\lambda^{3/7}]/\alpha$ 倍の多項式の余裕があるが、競いうる 2 枝($\Delta M\sim M$)は $t\gg\alpha\lambda/M\ge\alpha\lambda^{2/7}$ を要し、集団の配置の間の振幅は半古典で $e^{-c\lambda^{4/7}}$(417-A、値)—— 余裕は競合を 1 本も許さず、上界の形は「(II) 型の縮約の最小化子が全ての λ で一意」に帰着。(b) 在庫は P158・P167 がエネルギーの水準で 424-A により相対幅 O(1) の窓だけ、P206 は $\gg\lambda^{-1/7}$、P201 は消費者の側。(c) 3 段の壁:段の縮約の構成(F227 再開 (1)・S178・F257 再開 (2))、最小化子の一意性・非退化(F224 (a)・F228 (K2))、レゾルベントの水準の縮約(**424-A は凹 $C^1$ の関数の言明なので縮約の段によらない** —— F228 (K3) の閉鎖は (II) 型の段にそのまま移る)。
- **共通点(1 行)**:**縮約の段を準自由から集団のもつれに替えても、余りの 2 階は 424-A に当たり、上界の形は縮約の最小化子の一意性 = 擬交差の不在そのものに帰着する —— F228・F227 と同じ段。**
- **R9**:閉じたのは方式。双極子ではもつれが無く段は 1 枝(空);擬交差の梯子の候補では 2 枝の競合そのもの。名指しにしない。
- **射程(T60)**:禁じるのは「(II) 型の段の有効の汎関数・冪の勘定・エネルギーの水準の在庫で余りの $\chi_T$・(NFT$_{\rm s}$) を押さえる」発注。止めないもの:(II) 型の段の縮約の構成そのもの(難問 #2 の側、F227 再開 (1));レゾルベントの水準の縮約の道具。
- **再開条件**:(1) F227 再開 (1) と F228 再開 (1) が**両方**立ったとき;(2) λ についての $F'$ の凸性(404-G、F224 再開 (2))。
- **成算**:S231(なし、0〜1%)。


## F264(E05、逆向きの比較の小さい α の等号 —— 着衣の導関数の一様有界 (Y)「$\sup_\sigma\lVert\partial_P\Phi^\sigma_P\rvert_{P=0}\rVert\lt\infty$」を引き戻しの自己無撞着(ブートストラップ)で示し、雲 $B_\sigma\psi$ を明示で抜いて (U) を出す方式。2026-10-21、w_E05_435b = 書き下しの型、稿 `435_逆向きの比較_hlsとhsr_2026-10-21.md` §18 (a)〜(c)、成算 S230)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたのは: 方式(この標的には不要として打ち切り)**。命題 (Y) の真偽は閉じていない(冪の勘定では真の向き)。標的(λ≈1・小さい α の等号)は別の方式(FP (III.2) を使う §19、定理 435-F)で書けた。
- **理由(冪の勘定 + 比較)**:雲の寄与は二重交換子で σ 一様に $\le C\alpha(s+\epsilon\ln(\Lambda/s))$(注 435-E)。残り $Y$ の振幅は、1 光子で $\lvert k\rvert^{-1/2}\ln^{1/2}$、2 光子で $\lvert k\rvert^{-1/2}\ln$ と勘定でき、有限になる。ただしこれは、ずらしたファイバー $H(-k)$ の電流のベクトルの底の重み $\mu_w([0,e])\lesssim Ke^2$ を前提にした自己無撞着の勘定である。厳密化には FP の帰納法を導関数の水準でやり直す必要がある(多光子の分母の帳尻を含む)。FP (III.2) の $\lVert\eta_j\rVert^2\le C\sigma_j^{-2\delta}$ で足りるので、(Y) の厳密化は不要と判断した。
- **R9**:(Y) は双極子で真($Y=0$:着衣の状態は P に依らない)、2 構造の梯子(固定 λ・ギャップ Δ > 0)でも真の向きで、標的と同値ではない(より強い)。名指しにしない(不要)。
- **射程(T60)**:禁じるのは「λ≈1・小さい α の等号のために (Y) を書き下す」発注。止めないもの:λ→∞ の族で FP の型が使えないときの代替としての (Y)。


## F265(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕に要る「擬交差しうる 2 つの同じ量子数の枝の間のトンネル振幅 t の(λ の多項式の)下界、または t の小さい擬交差の不在」を、**半古典以外の 7 型**で供給する方式 —— (C1) 量的 PF(Harnack 定数・Doeblin)で基底と第 1 励起の隙間を下から、(C2) Cheeger・Lawler–Sokal の伝導度、(C3) 擬交差を数える型(Sturm・振動定理・Courant の節)、(C4) λ の複素の零点・分岐点の不在(Lee–Yang)、(C5) Wigner–von Neumann の非交差則の定量版、(C6) 擬交差の幾何学的位相、(C7) 和則・正のモーメント。2026-10-21、w_E05_438_tunnel_lower = 書き下しの型、稿 `438_全列_トンネル振幅の下界の型_2026-10-21.md` §2・§3、成算 S232、C0 651・652)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((NFT$_{\rm s}$)・(REG-W)・全列の真偽、擬交差の存在・不在ではない;値は真の向き)。
- **理由(厳密 + 値)**:(C1)(C2) 2 状態の stoquastic な擬交差の中心で、隙間・Doeblin の隙間の下界・構造の切断の伝導度の 2 倍は全て $2\varepsilon$ に等しく、Harnack 比は 1(観察 438-A (1))—— 出力は t そのもの(R9);浴つきの toyz で $\psi_1/\psi_0$ の掃引の最良の切断の伝導度は 0.57〜0.86 × 隙間で ∝ t、Doeblin の下界は隙間の 1 − 3·10⁻⁶(C0 652);素朴な切断は隘路でなく、切断の選択は構造の変数の同定(F247 再開 (1));模型では 2 構造の間の核は障壁で指数的(F211 (a)・F223 (d))、無質量では全体の Cheeger 定数は軟光子の切断で 0。(C3) 有限の Jacobi 行列では振動定理(節の数)が完全に成り、観察 429-U(E05-P221)の有限の切断は節の数・PF・単純性・交差の数と位置(1 オクターブに 1 個)を固定したまま落ちの率 R ∝ 1/ε で発散する(観察 438-A (3)、C0 651 J:ε 10⁻³ → 10⁻⁵ で R 25〜167 → 2.8·10³〜1.7·10⁴);数の上界は 396-W の望遠鏡和(在庫)で 1 オクターブに O(1) 個を許し、(NFT$_{\rm s}$) を割るのは 1 個で足りる;節は隘路の場所を与え大きさを与えない。(C4) 帯の幅 = 相対の t(C0 611 J4)か、零点の線の本数の有限性(= C3)のどちらか —— 欠けているのは t の下界そのもの(か C3)で、λ は強磁性の場でない(429 A5・F212 (b))。(C5) 避けた隙間 = 有効 2 準位の非対角の 2 倍で、定量版は t の下界そのもの;縮約は F211 (b)。(C6) stoquastic な拡大では基底状態の符号反転は無く(定性)、量的版(量子計量)は F250。(C7) 正のモーメントの局所有界な関数は負のモーメント $\chi_T$ を上から縛らない(観察 438-A (2)、原子の移動);toyz で $m_1$ は t に依らず(相対 5·10⁻⁵)、t の分は全体の 10⁻⁵〜10⁻⁸;F207・F218 の段。
- **共通点(1 行)**:**t の下界を与える型は、2 構造を分ける切断を通る流束 $\sum_{x\in S,y\notin S}c_{xy}$(2 準位で t に等号)を入力にするか、t か交差の数に落ちるか、t を外して数しか出さないか、高エネルギーの側しか見ない —— 正値性は流束の符号を、節は切断の場所を与え、流束の大きさは与えない。**
- **R9**:閉じたのは方式。「隙間の下界」は (NFT$_{\rm s}$) の各点の言い換えより強い(429 A3 と同じ);双極子では空、擬交差の梯子の候補では標的そのもの。難しさは「2 構造の間の流束の量的な評価(模型固有の構造の分類と障壁)」に留まり、消滅していない(F211 (1)・F223・F222 N1 と同じ場所)。
- **射程(T60)**:禁じるのは「量的 PF・Harnack・Doeblin・Cheeger・Lawler–Sokal・非交差則・幾何学的位相・和則・Sturm/Courant の節で、t の下界か擬交差の不在を出す」発注。止めないもの:擬交差の数の有限性を模型の構造の分類(300 §3.1 の固定点の型)から出すこと(0〜1%、難問 #2 の側);類 C の値(ジョブ 431・GPU 版)。
- **再開条件**:(1) 2 構造の分類(擬交差しうる ℓ=0 の枝が λ 大で有限個であること)が難問 #2 の側で立ったとき(C3 が数の有限性で (NFT$_{\rm s}$) を出す);(2) 2 構造の間の流束の多項式の下界を与える模型固有の入力(F211 再開 (1)・F223 再開 (1))が在庫に載ったとき。
- **副産物**:観察 438-A(self-audited、初等)。**全列の証明の角度は尽きた**(稿 438 §4:第 73 陣だけで 55 本、全て成算 1 割未満;残るのは類 C の値の判定)。


## F266(E05、全列(行 E1-H の内側)の名指し (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕を、**擬交差の数の有限性を構造の型・冪の分類(稿 300 §3.1 の固定点の型:2/3 と 5/7)から出し、F265 の C3(数える型)に入れる方式**(族 R-a)。2026-10-21、w_E05_438_tunnel_lower の再開(w_E05_438b)= 書き下しの型、稿 `438_全列_トンネル振幅の下界の型_2026-10-21.md` §8、成算 S232(追記)、C0 653)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((NFT$_{\rm s}$)・全列・難問 #2 の真偽ではない)。
- **理由(厳密 + 照合)**:(1) 300 §3.1 の「固定点の型」は在庫の 4 本の不等式の同時飽和の冪(2/3、観察 300-C は飽和する配置の同定で基底状態とは非主張)と試行の上界の冪(5/7)で、固有値の枝の分類ではない;ℓ=0 の構造が有限個の型に尽きる言明は在庫に無い。(2) 冪の異なる型の間の交差は λ 大で無い(冪の比較、自明)—— 残るのは同じ型の中の交差だけで、それは冪・定数の情報で制限されない:**観察 438-B**(429-U〔E05-P221〕の系)—— $G=\lambda^p$、$\mu_{n+1}/\mu_n\to1$ の 429-U は $E_0/\lambda^p\to1$(型 1 つ、冪と定数が正確)のまま擬交差が無限個で (NFT$_{\rm s}$) が偽;g の段は $\to0$ で値の観察 431-V1(段 ≤ 4.5%)とも両立。C0 653:$E_0/\lambda^{5/7}\in[1.000,1.012]$ で交差 11 個。(3) 難問 #2 は型の間の交差だけを消す。(4) 条件付きの形「(K1 型の分類の完全性)∧(K2 同じ冪の型の交差が有限)」が出すのは (NFT$_{\rm p}$) だけで、(NFT$_{\rm s}$) には (K3 各枝の 2 階が冪どおり、各点)が要る。
- **共通点(1 行)**:**冪の型は接線(固定した状態の 1 次式)の包絡として現れ、型の中で状態が入れ替わること自体が冪の実体 —— 入れ替わりが鋭いか滑らかかは冪・定数・型の数の情報に現れず、壁は型の中の 2 構造の間の流束 t に残る(F265 の共通点)。**
- **R9**:双極子では K1〜K3 とも空;擬交差の梯子の候補(429-U・438-B)では K1 は自明(型 1 つ)、K2 は交差の列そのもの、K3 は滑らかな部分の (NFT$_{\rm s}$) —— K2 ∧ K3 は標的と同値。名指しにしない。
- **射程(T60)**:禁じるのは「構造の型・冪・漸近の定数の分類(難問 #2 の解決を含む)から擬交差の数の有限性や (NFT$_{\rm s}$) を出す」発注。止めないもの:難問 #2 そのもの(全列とは独立の価値);類 C の値。
- **再開条件**:型の中の接点の入れ替わりの鋭さ(2 構造の間の流束)を量的に与える模型固有の入力(F211 再開 (1)・F223 再開 (1)・F265 再開 (2))が在庫に載ったとき。
- **副産物**:観察 438-B(self-audited、初等)。


## F267(E05、全列(行 E1-H の内側)を**別の径数・別の族への移送**で出す方式の族 Q1〜Q9 —— (i) α–λ 平面での擬交差の曲線の向き(α の単調・凹性、α→0 の摂動域);(ii) 形状因子の族で窓が動くことからの Borel–Cantelli(a.e. の族の元)と鋭い ↔ 滑らかの補間の移送(319-D・P165・P166);(iii) 光子質量 μ の経路;(iv) 族の選び方の自由度(連続な正則化の経路・不連続な選択);双極子 θ=0 からの反跳の係数 θ のホモトピー;2 次元の Fubini・Hessian の質量;殻の結合の経路で 2 進の点を結ぶ;量化子の線の取り替え(α=α(λ) の光線)。2026-10-21、w_E05_443_strat_params = 書き下しの型、稿 `443_全列の戦略_別の径数と族への移送_2026-10-21.md` §2〜§5、成算 S235、C0 666)

親(G3 第 73 陣)が連結 2026-10-21

- **閉じたもの**:**方式**(全 9 本)。Q2(a.e. の形状因子)・Q4 の経路・Q5・Q9 は加えて**標的の変更**に当たる(STATEMENT の案は採用しない)。標的(全列・(NFT$_{\rm s}$))と命題の真偽は閉じない。
- **理由**:(1) 観察 443-U (a)(429-U〔E05-P221〕の系、厳密):PF・整な正則族・(λ,s) の同時凹・s について単調・擬交差の位置が s とともに窓より速く動く —— を全て満たし、**全ての** $s\in[0,1]$ で (NFT$_{\rm s}$) が偽の族がある(第 2 径数の対角の項 $sN$)。(2) 443-U (b)(値、C0 666):非対角を s で育てると、s=1 で急な擬交差 0・s=0 で 11 個(λ∈[4,8192])、在庫の構造は保たれる —— 一方の端の全列は他方の端に運ばれず、擬交差の曲線が途切れるのは t が育つ所だけ。(3) 観察 443-I(厳密・初等):拡大の族では連続な経路 ⟺ 全列、不連続な選択 ⟺ 定理 396-D(E05-P205)から自明;一般の族では急な集合が径数の左右の辺を結ぶ連結集合を含めば全ての連続な経路がそれと交わる。(4) 両変数の別々の凹性・単調性は曲線の向きを決めない(稿 §2 Q1)。2 次元の Hessian の質量の評価は 1 次元の評価を超えない(Q7)。α→0 の摂動域では h は 1 ループで有界(Q9)。
- **共通点(1 行)**:**第 2 径数を足しても擬交差は (λ,s) 平面の曲線になるだけで、曲線が径数の全域に渡る限りどの線・どの連続な経路も横切る(中間値);曲線が途切れるのは t が育つ所だけ —— t を要らなくする読み(不連続な選択)は 396-D に潰れる。** 第 72〜73 陣の共通点(2 構造の間の t)は外れず移る:Q1 → α 方向の t、Q2 → 曲線の端点、Q3 → $\partial_s\log t$ の一様性、Q4 → 内部の擬隙間(F233)、Q6 → θ 方向の t、Q8 → 殻の経路の t。
- **R9**:各候補の新しい条件は双極子で空に成り、梯子(429-U・438-B・443-U)では径数を固定した切り口で (NFT$_{\rm s}$) そのもの —— 標的と同値なので名指しにしない。
- **射程(T60)**:禁じるのは「第 2 径数(α・形状因子・光子質量・反跳の係数・殻の結合)の在庫の構造(PF・解析性・同時凹・単調・窓の移動)と、ある径数の値での全列(または擬交差の不在)から、固定 α・鋭い切断の全列を出す」形の発注、および「族の選び方の自由度で量化子を弱めて t を外す」形の発注。止めないもの:模型固有の入力(θ を動かしたときの第 2 構造の誕生の位置と t の θ 依存、形状因子を動かしたときの t の変化の下界)。
- **再開条件**:(1) 2 構造の間の t の径数依存の量的な下界(擬交差の曲線が径数の内部で途切れること)が模型固有に出たとき —— F211 の再開条件 (1) と同じ段;(2) STATEMENT の (E1) の量化子をユーザーが「a.e. の形状因子」等に変えたとき(そのときも (1) が要る、443-U (a))。


## F268(E05、全列を回避する道のうち「**全ての くりこみ族で裸の質量が 0 へ**(くりこみ族の一意性の向き)」を到達形にする型(候補 C6)。2026-10-21、w_E05_441_strat_avoid = 書き下しの型、稿 `441_` §2・§4、成算 S233)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(回避の型として;命題の真偽ではない)。
- **理由**:A-247-2(E05-P131)で (E1) ⟺ 最も重い裸質量 $M(\Lambda)\to0$ —— 標的と同値(R9)。密度 1 の版にも落とせない:相対幅 $\lambda^{-1/7}$ の針 1 本で、$\Lambda/\lambda$ の像は対数の長さ $\sim\ln K$ の Λ の区間を覆い、そこで $m_0\ge m_{\rm ph}/K$ の くりこみ族がある。C0 656 J4(玩具、値【T88】):針 1 本/オクターブで、$\Lambda\in[10^3,10^7]$ の全ての Λ で $M(\Lambda)\ge0.257m_{\rm ph}$。
- **共通点(1 行)**:**くりこみ族の一意性は針の上の h の値そのものを問い、2 構造の間の t に戻る。**
- **R9**:双極子で真、針の梯子で偽 —— 標的と同値。
- **再開条件**:全列(E1-H)が閉じたとき(そのとき自動に成る)。

## F269(E05、全列を回避する道のうち「**一般の切断の形・ほとんど全ての径数**」(族の形 s の残留集合・a.e. s で全列)を到達形にする型(候補 C8)。2026-10-21、w_E05_441_strat_avoid、稿 `441_` §2・§4、成算 S233)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:同じ量子数の 2 準位の擬交差は 1 径数族で安定(摂動で消えず位置が動くだけ;von Neumann–Wigner の非交差則の型、出典は照合していない [要確認])—— 悪い集合は $(\lambda,s)$ 平面の曲線で全ての s の直線を横切り得る(F244 の α の議論と同じ)。
- **共通点(1 行)**:**径数を足しても λ の各点の情報は増えない(F244・F170 (i) と同じ)。**
- **R9**:閉じたのは方式。
- **再開条件**:族の形について擬交差の曲線の傾きの横断性(λ の直線に沿う交差が有限)を与える入力が出たとき。

## F270(E05、全列を回避する道のうち「**有限時間の有効質量**」(Euclid の平均 2 乗変位 / 3τ を到達形に)の型(候補 C9)。2026-10-21、w_E05_441_strat_avoid、稿 `441_` §2、成算 S233)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(回避にならない)。
- **理由**:Kubo の形式の計算(値)で $C_\pi\ge0$ ゆえ有限時間の量は τ について減少して $f$ に近づく —— 到達形にすると標的より**強い**;多項式の地平線の道具で示す道は F252(観察 428-A)で閉。
- **共通点(1 行)**:**有限の地平線の量は t を見ないが、到達形にすると標的より強くなる。**
- **R9**:標的より強い。
- **再開条件**:F252 の再開条件と同じ。


## F271(E05、全列(行 E1-H の内側)の (NFT$_{\rm s}$)〔系 417-B1 で (REG-W) と同値〕を、**λ→∞ の極限模型・繰り込み群の固定点・その基底状態の一意性と安定性の枠組み**の 6 型で出す方式 —— L1 状態の水準の共変な極限模型($C^1$ 収束 + 極限の構造の隙間)、L2 300-C の配位の汎関数の極限(相関の段の Frank–Seiringer)、L3 二重尺度の極限(α→0、$\alpha^a\lambda$ 固定)と接合、L4 双曲型の固定点と安定多様体(2 階まで)、L5 爆発の解析(背理法 + 窓ごとの 2 準位の極限)、L6 双極子(拘束の極限)からの変形。2026-10-21、w_E05_444_strat_limitmodel = 書き下しの型、稿 `444_全列の戦略_極限模型と固定点_2026-10-21.md` §3〜§5、成算 S236、C0 672)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(6 型)。標的(全列)と命題の真偽は閉じていない。
- **理由**:(L1)観察 444-B(稿 §2.2、self-audited、初等):有界な生成子の枠で $\Phi_\lambda=e^{i\theta}U_\lambda\psi_\lambda$ が $\lVert\lambda\partial_\lambda\Phi\rVert\le C_\Phi$ なら $\lambda^2\chi_F\le(C_U+C_\Phi)^2$、かつ $R\le2\alpha\lambda_-^3\sup\sqrt{\mathrm{Var}T\cdot\chi_F}/M^3$ —— 極限の存在・非退化は何も足さず、供給は $\chi_F=\int d\mu_T/E^2$ の上界(F250・438-A (2)・F261 の段);$C^0$ の収束は巨視的な擬交差を排除するが微視的な交差を許す;自然な枠は膨張(Λ を変える恒等式だけ)か Gauss(準自由、431-R と逆向き)。(L2)観察 424-A と F228 再開 (1) そのもの。(L3)二重尺度の変数が難問 #2 の冪で決まる($\alpha^2\lambda$ か $\alpha^{5/2}\lambda$)、接合は固定 α の標的(R9 同値)。(L4)写像 $R_b$ の構成に L1 の共変な枠が要る;双曲性 = $DR$ の隙間 = t;438-B で固定点への $C^0$ 収束は無限個の交差と両立。(L5)抽象の性質(PF・単純・解析・節の数)は全て 2 準位の極限に残り(429-U・438-A)、模型の恒等式は 2 枝で別々に成る —— 剛性 = (NFT$_{\rm p}$)。(L6)$\frac\lambda2(\theta P_f+eA)^2+H_f$ は $(\lambda\theta^2,\alpha/\theta^2)$ の模型で、変形は (α,λ) 平面の経路(F244・F222 N3);θ=0 は冪の類の特異摂動。
- **共通点(1 行)**:**極限の模型は、エネルギーの水準なら (NFT$_{\rm s}$) に届かず(424-A・438-B)、届く水準($C^1$・解消核)では $\chi_F$(または $\chi_T$)の有界と同値で、極限の存在は何も足さない —— 壁 t は「極限の模型の構造の隙間」に名前を変えるだけ。**
- **R9**:双極子では L1〜L6 の条件が全て成り、擬交差の梯子(429-U・438-B)では全て破れる —— 標的より強いか同値;名指しにしない。
- **射程(T60)**:禁じるのは「極限の模型(古典・準自由・相関の段・二重尺度)の存在・一意性・非退化・固定点の双曲性・爆発の極限の剛性から、$\chi_F$・$\chi_T$ の一様な評価を経ずに (NFT$_{\rm s}$)・(REG-W)・全列を出す」発注。止めないもの:$\chi_F$ の上界の模型固有の入力;極限の模型の同定そのもの(難問 #2 と共通の価値)。
- **再開条件**:(1) $\chi_F$(または余りの $\chi_T$)を λ に一様に上から押さえる模型固有の入力(F250 再開・F261・F228 再開 (1) と共通);(2) 300-C の配位を含む極限の汎関数の同定と、解消核の水準($C^1$)の縮約の誤差評価。

## F272(E05、全列(行 E1-H の内側)の極限の模型として、**有限モードの切断ごとの λ→∞ の極限(最低 Landau 準位型の射影・縮退の摂動)と、有限体積の箱で一様に示して V→∞** を使う方式の**標的**。2026-10-21、w_E05_444_strat_limitmodel = 書き下しの型、稿 `444_` §2.1・§4、成算 S236、C0 671)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**標的**(「有限モード・箱の λ→∞ の極限の模型が全模型の λ→∞ を表す」)。全列の真偽は閉じていない。
- **理由**:観察 444-A(稿 §2.1、self-audited、初等):±k の対で閉じた有限モード(周期箱を含む)では対ごとの 2 モードのスクイーズの試行で $P_f\psi=0$、$\langle A^2\rangle=e^{-2r}S_A$ となり $F\le\min(\lambda e^2S_A/2,\sqrt{e^2S_AW\lambda/2})$(双極子の類 1/2);対なしでは $F/\lambda\to\inf\sigma(T)$(線形)。連続の模型では $W=\infty$ で在庫の下界 $c\alpha^{1/3}\lambda^{2/3}$ と矛盾しない —— λ→∞ とモードの除去・V→∞ は可換でない。箱では非局在の対スクイーズ $\lesssim\sqrt{\alpha\lambda V}$ が $\lambda\gtrsim(\alpha V)^{7/3}$ で局在の構造と競合(値;箱は第 2 構造を新たに作る)。C0 671(2 モード):対ありの局所冪 0.836→0.529、対なし 0.987〜1.000。
- **共通点(1 行)**:**有限モード・箱の極限は別の普遍類(双極子の 1/2 か線形)で、全模型の 2/3〜5/7 の帯は中間の漸近としてしか現れない。**
- **R9**:閉じたのは標的。壁には触れない。
- **射程(T60)**:禁じるのは「有限モード・箱の模型の λ→∞ の極限(またはその一様性)から全模型の大きい λ の構造・(NFT$_{\rm s}$) を出す」発注。止めないもの:有限の λ の窓 $[1,\lambda_c]$ での有限モードの数値(値)—— ただし大きい λ の局所冪を連続の証拠に読む前にモードの集合が ±k で閉じるかと $\lambda_c$ を照合する。
- **再開条件**:なし(標的の閉鎖)。

## F273(E05、全列(行 E1-H の内側)を、**ポーラロンの全ての α の有効質量の発散(Lieb–Seiringer 2020、arXiv 1902.04025)の機構の移植**で出す方式 —— 有効質量を基底状態の 1 次の期待値だけで上から押さえる試行(LS (2.1)・(2.4))と、その期待値の λ→∞ の極限を「補助の摂動についての基底エネルギーの凹性 + 尺度の極限の汎関数の微分可能性」(Griffiths の補題の型、LS Lemma 1 の証明 (2.19)〜(2.30))から出す道(候補 X1;平均場・スピングラスの同型〔最小化子の一意性 ⟹ 全てのパラメタで微分可能〕を X10 として含む)。2026-10-21、w_E05_445_strat_transfer = 書き下しの型、稿 `445_全列の戦略_他分野の解決例の移植_2026-10-21.md` §2・§3.1・§4、成算 S237、C0 676)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(全列・(NFT$_{\rm s}$)・(REG-W) の真偽ではない)。
- **理由**:(1) LS で全ての α が取れたのは、量が α 方向の 2 階の量を含まず(1 次の期待値)、その極限を一意な Pekar の最小化子が決めたから(Lemma 1:$E^P(\vec\lambda)$ の微分可能性 ⟸ 一意性;(2.18) の Euler–Lagrange の恒等式で極限の試行の値が相殺)。(2) PF への移植には (L1) λ→∞ の尺度の極限の汎関数 $e(x,s)=\lim E_0(\mu x,\mu^qs)/E_0(\mu)$(補助の摂動つき)の存在と s=0 での微分可能性、(L2) $f_{\rm sr}$ を 1 次の期待値だけで押さえる試行で極限の値がちょうど −1 になる恒等式、が要る。(L1) は難問 #2(冪 2/3 か 5/7、F227・F258)を定数・摂動・一意性つきに強めたもので、PF の極限の対象は在庫に無い(補題 418-C:コヒーレントの段の最小は $g=0$ で $\inf\asymp\alpha\lambda\gg E_0$;準自由の段は非凸、418 (a) 2%)。(L2) は $f$ がレゾルベントの量(2 次)であることと LS (2.18) の類似の不在で止まる。(3) **値(観察 445-A、C0 676、【T88】)**:429-U 型の有限 Jacobi($G=\lambda^{5/7}$)で、微視的な梯子 $\mu_n=n^2$ では 1 次の量 $\lambda g/F$ の振れ幅 0.091 → 0.011(5/7 に収束)で R は大きいまま、巨視的な梯子 $\mu_n=2^n$ では振れ幅 0.140 で一定 —— X1 の仮定は (NFT$_{\rm s}$) と同値でなく、微視的な擬交差(小さい t)を許し巨視的な繰り返しの跳びだけを禁じる。
- **共通点(1 行)**:**他分野で全てのパラメタが取れた例は、(α) 2 階の量を使わない量の選び方と (β) 1 次の量の極限を決める一意な有効の対象を持ち、t の問題を解いたのでなく回避した —— PF は (β) を持たない。**
- **R9**:閉じたのは方式。条件 (L1) は双極子で真、微視的な梯子で真、巨視的な梯子で偽 —— 標的と同値でない。壁 t は外れるが、難しさは (L1)(L2)(難問 #2 の強い形と 1 次だけの消費者の恒等式)へ移り、移り先は閉じた場所(418 (a)・F227・F258)。
- **射程(T60)**:禁じるのは「LS 2020 の試行 + Griffiths の型を、PF の尺度の極限の汎関数なしに当てる」発注。止めないもの:準自由の段の有効汎関数の構成と一意性(418 (a) の再開)、1 次の期待値だけで $f$ を押さえる試行の探索(稿 10 の LS の型の再訪)。
- **再開条件**:(1) PF の λ→∞ の尺度の極限の汎関数(補助の摂動つき)が立ち、その最小化子が一意(s=0 で微分可能)と示されたとき;(2) $f_{\rm sr}$ を基底状態の 1 次の期待値だけで上から押さえ、極限で −1 に相殺する試行が見つかったとき(LS (2.18) の PF 版)。(1)(2) の両方が要る。

## F274(E05、全列(行 E1-H の内側)を、**他分野で「全てのパラメタ」の基底状態の正則性・準位の交差の不在・有効質量の増大を解決した型 8 本の移植**で出す方式 —— X2 LS Lemma 1 の双対(固定の $B$ によるエネルギーだけの作用素不等式の証明書)、X4 Brooks–Seiringer I・II・Frank–Seiringer 2019(一意な Pekar の最小化子 + Hessian の強圧性)、X5 ポーラロンの経路測度の正値性(Sellke 2024 の GCI・Betz–Polzer・BMSV・Polzer 2026 の完全単調性)、X6 Lieb–Mattis・Marshall の符号則・反射正値(量子数の区画による準位の順序)、X7 1 次元の非交差則(Sturm・Gantmacher–Krein・Wigner–von Neumann の定量版)、X8 原子(Solovej 2003 の多重尺度の遮蔽・Fefferman–Seco)、X9 相転移の鋭さ・連続性の微分不等式(Aizenman–Barsky・Duminil-Copin–Tassion・Aizenman–Duminil-Copin–Sidoravicius)。2026-10-21、w_E05_445_strat_transfer = 書き下しの型、稿 `445_` §2・§3.2・§4、成算 S237)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(8 本)。
- **理由**:X2:固定の作用素 $X$ の試行の値は ρ について線形だが、係数の最適化 $\inf_\kappa\Phi=-a^2/b$ は ρ について凹で、擬交差の猫での損は $w_1w_2b_1b_2(\kappa_1-\kappa_2)^2/(w_1b_1+w_2b_2)$(観察 445-B、初等)—— 命題 212-C の $2\sigma^2$(F219 (0))と同じ型;係数を構造ごとに変える条件づけは F219 (a2)・F116。X4:F141・418 (a)(PF の古典の段は自明、補題 418-C)。X5:F99・F220 (c′)・F190 (a)(重み $e^{-\frac{e^2}2Q}$ は準凹でない);Polzer 2026(2607.05286)Thm 1 は Assumption 1(完全単調・Bernstein)の下の $E(P)-E(P_0)$ の**下界**で、有効質量の上界の向き。X6:431-A(2 枝は J=0・パリティ・時間反転が同じ)、区画の中の t は F211。X7:F265・観察 438-A (3)。X8:殻の再帰は片向き(F161・F170 (iii));原子の微分量の振動は離散の内部尺度(殻)が源で PF には無い(類 C の値の補強のみ)。X9:鋭さの定理は微分の下界(向きが逆)、連続性は強磁性の正値性(switching lemma)に依り F212 (b)・F187 (K2) の段;要る $\chi_T$ の上界は標的の量。X8・X9 の帰属は原典未照合 [要確認](閉鎖の理由は在庫の F で足りる)。
- **共通点(1 行)**:**移植元の道具は、区画を分ける量子数・正値の構造・一意な比較の理論・強磁性の単調性のどれかを要り、PF の擬交差の梯子の候補(429-U・438-B)はそれらを全て保つか、PF がそれらを持たない。**
- **R9**:閉じたのは方式。どの型も壁 t を外さないか、閉じた場所(F219 (a2)・418 (a)・F99・F211・F265・F161・F212 (b))へ移すだけ。
- **射程(T60)**:禁じるのは X2・X4〜X9 の型で全列・(NFT$_{\rm s}$) を出す発注。止めないもの:F の各行の既存の再開条件。
- **再開条件**:各型の既存の F の再開条件に従う(新しい条件なし)。


## F275(E05、全列の類 C・難問 #2 の値の読み:**NUM-6420 の 24 モードの MPS の族の $E_0$ の大きい λ の局所冪(0.856→0.711 の減少)を連続の模型の冪(2/3・5/7)の証拠として読む**こと。2026-10-21、w_E05_444b = 書き下しの型、稿 `444_全列の戦略_極限模型と固定点_2026-10-21.md` §9.1、成算 S236(追記)、C0 673)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**標的**(この読み)。全列・難問 #2 の真偽は閉じていない。
- **理由**:MPS の模型は ±k で厳密に閉じた 24 モード(`k422.py`:偏極は k の符号に依らず、$g=(2\lvert k\rvert)^{-1/2}$)で、観察 444-A(E05-P234)の仮定 (P) を満たす —— λ→∞ で $E_0=O(\sqrt\lambda)$(上界 $3.567\sqrt\lambda$)。殻ごとの対スクイーズの Gauss 試行は MPS の $E_0$ の 1.150 倍(λ=16)から 1.054 倍(λ=256)へ寄り、その局所冪は MPS の局所冪と並走して 1/2 へ下がる(C0 673)—— 在庫の λ は有限モードの交差の中。
- **共通点(1 行)**:**±k の対を含む有限モードの数値は、大きい λ で双極子の類(1/2)の通路に乗り、連続の冪の帯を一時的に横切るだけ。**
- **R9**:閉じたのは標的(数値の読み)。
- **射程(T60)**:禁じるのは「±k で閉じた有限モード・周期箱の数値の、444-A の交差の λ 以上での局所冪を、連続の模型の冪・全列の値として読む」こと。止めないもの:連続の運動量で光子を積分する数値(A1 の HMC、426・416 —— 444-A の仮定に当たらない、§9.2);交差より十分小さい λ の有限モードの数値。
- **再開条件**:なし(読みの閉鎖)。モードの集合から ±k の対を除いた(または対のスクイーズを罰した)有限モードの数値を作るなら別の標的。


## F276(E05、全列(行 E1-H の内側)を**窓の尺度の blow-up と Liouville 型の分類**で出す方式(背理法:例外列 $\lambda_n$ と窓 $w_n$ で $s\mapsto\psi_{\lambda_n(1+sw_n)}$ の極限の対象に急な落ちが無いことを示す)。2026-10-21、w_E05_442_strat_contra = 書き下しの型、稿 `442_全列の戦略_背理法とコンパクト性_2026-10-21.md` §2 B1・§5、成算 S234)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(全列・(NFT$_{\rm s}$) の真偽ではない)。
- **理由**:窓の上で $H$ の変化 $\lambda_nw_nT$ はエネルギー $\sim wF\gg1$(光子の尺度)で、標準の極限の Hilbert 空間・極限の作用素が無い;抽象の極限は 2 準位・Jacobi で、観察 429-U(E05-P221)が「極限の対象に急な落ちが無い」を偽にする。極限の分類は 2 構造の間の t の情報そのもの。
- **共通点(1 行)**:**背理法の仮定から引き出せる例外列の構造は 406-U・429-U・438-B の証人で全て実現される —— 証人が持たない模型固有の性質を使わない背理法は止まる(稿 442 の物差し W)。**
- **R9**:「窓の極限に急な落ちが無い」は (NFT$_{\rm s}$) の窓の尺度の言い換え(同値)。名指しにしない。
- **再開条件**:PF の窓の尺度の極限の対象(有効模型)が構成され、その分類に模型固有の入力(稿 442 §1 の (P1)〜(P5))が入ったとき。

## F277(E05、全列を**大域の尺度の Γ 収束・集中コンパクト性**($F(\lambda s)/F(\lambda)\to s^p$ と極限の汎関数の最小化子の一意性)で出す方式。2026-10-21、w_E05_442_strat_contra、稿 `442_` §2 B2・§5、成算 S234)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(1) 極限の汎関数は準自由の型(補題 418-C:コヒーレントの汎関数は $\asymp\alpha\lambda\gg E_0$)で、その一意性 + 強圧性の道は 418 (a) で 2%(Bogoliubov の精度の縮約 F115・F228 の段);(2) 凹な F の正則変動は $\lambda g/F\to p$ を出すが率を出さず、(NFT$_{\rm s}$) に要る相対幅 $\lambda^{-1/7}$ の窓の率は、冪も定数も正確な族で擬交差が無限個ある観察 438-B が独立と示す。
- **共通点(1 行)**:**コンパクト性は 0 次の情報(冪・定数・極限の対象)を運び、2 階の率(= t)を運ばない。**
- **R9**:率つきの版は (NFT$_{\rm s}$) と同値。
- **再開条件**:難問 #2 の正確な漸近に 2 次の項の率($\lambda g/F=p+O(\lambda^{-1/7-\delta})$)がついたとき。

## F278(E05、全列を**最小反例・最初の擬交差**(小さい λ の解析的な域から連続に追い、最初の悪い窓から矛盾)で出す方式。2026-10-21、w_E05_442_strat_contra、稿 `442_` §2 B3、成算 S234)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(NFT$_{\rm s}$) は漸近の主張で有限の λ の擬交差は許されるので、「最初の」悪い窓は矛盾を生まない;帰納には λ と 2λ を結ぶ写像(光子の拡大で λ ⟺ 切断、殻の追加 = Wilson の RG)が要り、1 殻あたりの結合の縮小が O(α) で小さくない(F170 (iii)・F171・F208・415 N4 と同じ段)。
- **共通点(1 行)**:**最小反例の議論は帰納の写像を要し、PF の自己相似の写像は在庫に無い。**
- **再開条件**:殻の写像の縮小(λ に一様な RG の不動点の安定性)が立ったとき。

## F279(E05、全列を**正値性と直交**(発注の (iv):擬交差の 2 構造はともに正、重なりが小さいことは Q 空間での台の分離;分離の境界の流束を下から押さえる)で出す方式 —— Gauss 構造の**逆超縮小性**(Borell 1982 の逆 Bonami–Beckner)を含む。2026-10-21、w_E05_442_strat_contra、稿 `442_` §4.3、成算 S234)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:(1) 正の単位ベクトルの重なり ε は Bhattacharyya 係数で、全変動 $\ge1-\epsilon$ = 台の分離;境界の流束は Cheeger の量で 2 準位で t に等しい(観察 438-A (1)、F211)。(2) 逆超縮小性(原典 Mossel–O'Donnell–Regev–Steif–Sudakov 2006、arXiv math/0410560 §1.3・Thm 3.4 を本文で確認)は非負の関数の重なりを台の測度で下から押さえるが、巨視的に異なる 2 構造の台の測度は $e^{-c\Delta N}$($\Delta N\ge\Delta\langle H_f\rangle$)で、下界も指数的に小さい;PF の転送の主項は $\lambda T$ で OU 半群でない。
- **共通点(1 行)**:**正値性は t の正しか与えず、台の測度から出る下界は指数的に小さい(F194・F211 と同じ段)。**
- **R9**:流束の下界 = t の下界(標的の量)。
- **再開条件**:F211 の再開条件 (1)。

## F280(E05、全列を**重ね合わせのエネルギーの勘定**(窓の中心の状態 $c\psi_-+s\psi_+$ がビリアル・反磁性・319-A・P158 の不等式に反すること)で出す方式。2026-10-21、w_E05_442_strat_contra、稿 `442_` §2 B5、成算 S234)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由**:線形の恒等式(ビリアル、尺度則 $\lambda\langle T\rangle=\Lambda\partial_\Lambda E_0-E_0$)は混合で閉じる;状態の水準の不等式は $(\langle T\rangle,\langle H_f\rangle)$ の結合数域(2 つの自己共役作用素の結合数域は凸 —— Toeplitz–Hausdorff の型)の境界の言明で、境界の曲率 = $1/\chi_T$(F245);F だけの不等式は 406-U(E05-P210)で凹性に退化。
- **共通点(1 行)**:**エネルギーの勘定は結合数域の凸性の中に住み、境界の平らさ(= 小さい t)を禁じない。**
- **再開条件**:結合数域の境界の曲率の下界(F245 の再開条件)。

## F281(E05、全列を**標的 $h$ への直接の背理法**($f(\lambda_n)\ge c$ と 396-D の両側の良い点から、擬交差での $f$ の内挿で矛盾)で出す方式 —— 断熱の二分(ℓ=1 の励起の隙間 $x\ll t$ は混合に従い、$x\gg t$ は構造ごと;どちらも内挿)の厳密化。2026-10-21、w_E05_442_strat_contra、稿 `442_` §4.2、C0 661 J5、成算 S234)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(全列の真偽ではない;値は真の向き)。
- **理由**:内挿を厳密にするには構造への分解(F219 (a1):2 準位の縮約の質 = t)か良い点からの移送(F243:誤差 $\psi_b-\psi_g=O(1)$)が要る。C0 661 J5(抽象の玩具、値【T88】):瘤は「$x\sim t$ の ℓ=1 の励起が G の O(1) を担い、構造間でトンネルしない」ときだけ(0.29、他は内挿 0.04〜0.06);PF では $x\lesssim t$ の ℓ=1 の低帯は(構造)⊗(軟光子)(F220 (b))で G への寄与は $\sim t^2$、軟光子は断熱的に従う —— 類 C の見込みは動かさない。
- **共通点(1 行)**:**内挿は物理として正しいが、証明は構造を見分ける操作を要し、F219 の共通点に戻る。**
- **R9**:閉じたのは方式。双極子では内挿は自明;梯子(π なし)は f を持たない。
- **再開条件**:F219 の再開条件 (1)(2)、または稿 442 の (S-stab$_G$) の (i)(ii)(励起状態の重さ・ℓ=1 の干渉の上界)が在庫に載ったとき。


## F282(E05、全列(行 E1-H の内側)の命題 442-S(E05-P236)の移り先 (iii) を消すための「ℓ=1 の応答の運動の含量 $\kappa=\langle\varphi,T\varphi\rangle/\lVert\varphi\rVert^2\ge g(\lambda)$」($\varphi=(A_{\lambda'}+\varepsilon)^{-1}Q_z\psi_\lambda$、補題 448-K の補正の符号)を **Cauchy–Schwarz の型**($\langle T^2\rangle\ge\langle T\rangle^2$)で出す方式。2026-10-21、w_E05_448_ws = 書き下しの型、稿 `448_全列_準最小状態の重さ_族WS_2026-10-21.md` §2.2、C0 687、成算 S239)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(κ ≥ g の真偽ではない;値は真の向き)。
- **理由**:成分が可換なら $\sum_i\langle Q_i\psi,TQ_i\psi\rangle/\sum_i\lVert Q_i\psi\rVert^2=\langle T^2\rangle/\langle T\rangle\ge g$ だが、(a) $[Q_i,Q_j]$ = 原点の磁場の項の符号の一般論が無い(圧縮の値では正で κ₀ ≈ 4g);(b) レゾルベントの重み直しで低い x の状態に重みが移る(κ₀ → κ ≈ 2.4〜3 g);(c) 連続体では $H_{\lambda'}$ の低い ℓ=1 状態 ψ′⊗(軟光子) の T は ≈ g(λ′) < g(λ) で、軟い部分の $\lVert\varphi\rVert^2$ は Low の定理の型で $\frac{2\alpha}{3\pi}f^2\log$ に発散する(値)—— **作用素の水準の κ ≥ g は偽**。(c) の損は ε で切れば小さい(値)が、(a)(b) を λ に一様に押さえる型が在庫に無い。
- **共通点(1 行)**:**運動の含量の下界は ℓ=1 の応答のスペクトルの重みの配り方(F219・F220 の ℓ=1 の量)を要し、和則の CS は配り方を見ない。**
- **R9**:双極子(Gauss)では可換で CS が成り κ ≥ g;擬交差の梯子(429-U・438-B)は ℓ=1 の応答を持たず判定しない。標的と同値ではない(補題 448-K の補正の符号の条件)。
- **再開条件**:ℓ=1 の応答のスペクトル測度の重みの配り方(F220 の再開条件 (i))か、磁場の交換子の項の符号を与える反磁性の不等式が在庫に載ったとき。

## F283(E05、全列の命題 442-S の (S-stab$_G$) を「**軽さのエネルギー費用**」(η-準最小状態を基底状態より δ だけ軽くするには $A_{\lambda'}[\psi]\ge\Theta(\delta)\gg wF$ が要る)で出す方式。2026-10-21、w_E05_448_ws、稿 `448_` §3、C0 686、成算 S239)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((S-stab$_G$)・全列の真偽ではない;値は真の向き:433-D の圧縮で $\Theta(\delta)\approx F\delta^2/C^2$、C ≈ 0.75〜1.0)。
- **理由**:費用を出すには ℓ=0 の η 以下の部分空間を「ψ′⊗(軟光子の対)」(観客、重い)と「束縛した別の構造」に分ける HVZ 型の分解が要り、後者が重いことは稿 442 の (i)(軽い侵入者の不在)そのもの。在庫の型「応答の形式の $A'$ に対する相対有界 $K(u)\lesssim A'[u]$」は観客の対で偽($A'[u]\to0$ で $K(u)\approx G\lVert u\rVert^2$)。
- **共通点(1 行)**:**軽さの費用は励起状態の重さの言い換えで、在庫は基底状態の情報しか持たない(稿 442 §5 B7 の移り先と同じ)。**
- **R9**:(i) の衣替え(名指しにしない)。
- **再開条件**:P=0 ファイバーの ℓ=0 の低エネルギーの部分空間の構造(観客 ⊗ 束縛状態の分解)と束縛した励起の応答の下界が立ったとき。

## F284(2026-10-21、w_E05_446_hmc_systematics、書き下しの型)仮説「426 の $h_{\rm eff}(1)$ の局所冪 0.5495 は HMC の有限の窓 T=6・経路の刻み dt の系統で 3/7 の帯から押し出された」—— 値で閉じた

親(G3 第 73 陣)が連結 2026-10-21
- 閉じたもの:**値の読みの仮説**(全列の (R-B)$_w$ の (ii) の類 C の否定側の逃げ道の 1 つ)。方式・命題の真偽は閉じていない。
- 理由:窓は在庫の同じ dt の短い T(392:T=1・0.5、領域が端から 0.25・0.125)で $h_{\rm eff}(1)$ が T=6 と 0.6%(1σ)以内、局所冪 64→128 も 1σ で一致 → $\lvert\delta p_T\rvert\lesssim0.003$。刻みは HMC の積分の誤差が受理で消え、c_δ = 0.25〜4 の C0 で $\varepsilon(\lambda)$ が λ=16 の +0.5〜1.3% から λ=128 の +0.16% ± 0.31% に縮む(E05-P98 2. の 1 ループの Trotter は c_δ² の絶対量)→ 中心 0.002・保守 0.023。合計は保守でも 0.026 < 余裕 0.121 の 1/3。札 SYSTEMATIC_SMALL(稿 `446_` §4、NUM-?(681・682/683))。
- 再開条件:λ=256 で T か c_δ を変えた実測が $h_{\rm eff}(1)$ を 2% 以上動かす(稿 `446_` §4 の最小の確認:λ=256 の c_δ=2、5090 で約 1.3 GPU h)。
- 残るもの(本族の外):λ=256 の 1 本の鎖の統計の誤差の推定の揺れ、局所冪(2 点の差分)と λ→∞ の冪の差。値であって上下界ではない【T88】。

## F285(2026-10-21、w_E05_450_gpu、書き下しの型)方式「2080 Ti で族 A(c_δ=1)の高い λ を K2 または T=6 のまま回す」(W1 の λ=512・W2 の [128,256])—— 費用で閉じた(方式の閉鎖)

親(G3 第 73 陣)が連結 2026-10-21
- 閉じたもの:**方式**(計算の経路)。標的(λ=512 の局所冪、431 の [128,256] の段・準安定)は閉じていない —— 別の装置で包装した(稿 `450_`)。
- 理由:2080 Ti の族 A の λ=512・T=6 は 1 軌道 約 540 s で数百軌道 45 h 超(監査 449 §2b、12 h の C2・24 h の承認を越える);K2 の λ=256・T=6 は 1 軌道 ≈170 s で 431 の設計の量(点あたり約 1000 軌道 × 3 rep)に届かない(449 §2c)。代わりに (W1) 族 B(c_δ=4、N が 1/4)を段 1 の R(λ) で族 A に照合してから λ=512 を読む;(W2)359 の RESPA + F4 を族 A のまま T=64/λ で(N = 64λ、2080 Ti で λ=256 が 1 軌道 0.71 s、smoke の実測)。
- 再開条件:計算機 2 の 5090 が 70 h 空く(族 A の λ=512、承認事項)か、段 1 の札が B_BIASED(族 B が使えない)。
- 値であって上下界ではない【T88】。

## F286(E05 の外・難問 #1 の弱い構成:**結合を切断とともに下げる族**〔各 Λ で $\alpha(\Lambda)\le\alpha_0(\lambda(\Lambda))$〕で、系 435-G(E05-P229)の $h_{\rm ls}=h_{\rm sr}$ と命題 432-D(E05-P224)・A-437-1 の着衣の座標の率を組み合わせ、経路の緊密性(弱い構成)を出す方式。2026-10-21、audit_Replenish73_2 = 監査の型、監査稿 `457_` §3、成算なしの確認)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(値と字面による;#1 の真偽は閉じない)。
- **理由**:(1) 量化子は合う(∀λ ∃α₀(λ)、λ で径数づけた族は在る)が、α₀(λ) の値 $\lambda^{-1}$〜$\lambda^{-2}$(P229【T88】)と 1 ループ・RG 改良の h で族に沿って $h\to1$、$m_0\to m_{\rm ph}$ —— 族は小結合の極限で、#1(固定 α のくりこみ族)の問いでない。(2) 432-D・A-437-1 は L² の率(2 次のモーメントで τ の 1 乗)だけで、緊密性に要る高次のモーメントは非主張。(3) h が発散する族には $\alpha_0(\lambda)\gtrsim1/\ln\lambda$ の下界が要り、それは FP・CFP の多尺度の Λ 一様性 = 紫外の問題。
- **共通点(1 行)**:**固定の切断の小結合の結果を、結合を切断とともに下げて族に運ぶと、族は先に小結合の極限へ逃げ、くりこみの問いが消える —— 残るのは α₀(λ) の下界(紫外の一様性)。**
- **R9**:閉じたのは方式。双極子では族に沿って $h=1+\frac{4\alpha\lambda}{3\pi}$ が有界(くりこみなし);2 構造の擬交差の梯子では族は擬交差に届く前に結合が消える。
- **射程(T60)**:禁じるのは「α を切断とともに下げる族で、固定 λ の小結合の定理(435-F/G・FP・CFP)を使って #1 の弱い形を出す」発注。止めないもの:固定 α の族での $h_{\rm ls}\le Ch_{\rm sr}$ を移送でない道(434-B の CLT + 底の窓の重み)で当てる角度;α₀(λ) の下界そのものの研究(紫外の問題として)。
- **再開条件**:$\alpha_0(\lambda)\ge c/\ln\lambda$ 型の下界(FP・CFP の多尺度の定数の Λ 一様化)が文献か在庫に出たとき;または #1 の問いを「結合も動く族」に読み替える承認(STATEMENT の外、ユーザー判断)。


## F287(E05、全列(行 E1-H の内側)の十分条件「$F'$ の凸性」(命題 404-G・補題 405-G、E05-P208・P209)を**専用の候補表 5 本**で供給する方式 —— V1 $F'$ の Stieltjes / Bernstein の表示を FK・汎関数積分・正値性から、V2 摂動の各次の $F'''$ の符号と再和、V3 3 階の Feynman–Hellmann の恒等式の符号、V4 双極子(θ=0)からのホモトピー、V5 漸近展開から。2026-10-21、w_E05_458_thin_sufficient = 書き下しの型、稿 `458_全列_手薄な十分条件3本_2026-10-21.md` §2・§3・§4、C0 693・695・697、成算 S241)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(凸性・全列の真偽ではない;値は凸の向き)。5 本とも成算 1 割未満(V1・V4 1% 未満、V2・V3・V5 0%)。
- **理由**:(1) **R9**:凸性は抽象の玩具・読みでは標的から従わない(PF の上の強弱は主張しない —— 監査 462 §8) —— 擬交差の下の枝の S 字で破れ、閾は相対幅 $\approx0.3(\Delta\tau/\tau)^{1/2}$(観察 458-C、C0 693 J2;(REG-L) の $\lambda^{-1/7}$ より強い);404-B・442 J2 で全列は真のまま凸性は偽になり得る。(2) **V1**:双極子では厳密に Stieltjes(観察 458-D:ln det、機構は場について 2 次);Stieltjes ⟺(おおよそ)基底の枝の例外点が負の実軸の外に無い —— 429-U(PF・整な正則族・孤立)は持たない;PF では FK で λ が反跳の位相にも入り Gauss でない。反跳の玩具は擬交差なしで差分 6 階まで完全単調・右半平面の箱に例外点なし(C0 695 J1・697、値)だが、表示の機構は無い。(3) **V2**:PF の α² 次は $-\lambda^2\sum c/(a+b\lambda)$ で各項 $F'''\gt0$ だが、凸性が厳密に真の双極子でも $e^{2n}$ 次の $F'''$ は n ≥ 3 で符号が交代(C0 695 J3)—— 凸性は再和からだけ来る;λ→∞ は強結合で一様でない(F187 (K3) の段)。(4) **V3**:3 点関数の符号は 2 準位で変わる(F187 (K1))。(5) **V4**:443-U (b)・443 Q6 —— 径数を育てると擬交差が現れ得る。(6) **V5**:単調密度定理は 1 階まで(F212 (4))、2 階は誤差に入る(406-U)。
- **共通点(1 行)**:**凸性(完全単調性)を出す構造的な表示は在庫では双極子の Gauss 性(ln det)からしか出ておらず、反跳つきの代わりの表示は知られていない(表示が無いことは示していない —— 監査 459 §3.1);一般の構造(正値性・解析性・摂動の各次)は擬交差・例外点を禁じない —— F212・F214・F234 と同じ段。**
- **R9**:閉じたのは方式。双極子では成る(458-D);擬交差の梯子では偽;難しさは「反跳つきで擬交差(例外点)が無いこと」に局在し、消滅していない。
- **射程(T60)**:禁じるのは「$F'$ の凸性・完全単調性・Stieltjes 性を、FK の正値性・λ についての解析性・摂動の各次の符号・双極子からの連続変形・漸近展開で出す」発注。止めないもの:反跳つきの模型で ln det に代わる厳密な表示(例えば場の側の Gauss 化で反跳を位相に残さない表示)の探索。
- **再開条件**:(1) PF の基底エネルギーの λ についての ln det 型(正値の測度の Stieltjes 型)の表示が在庫・文献に載ったとき;(2) F211 の再開条件 (1)(擬交差の隙間の量的な下界)。

## F288(E05、全列の十分条件 **(REG-L)**(E05-P206、命題 403-B)を**専用の候補表 4 本**で供給する方式 —— L1 閾 $\lambda^{-1/7}$ の改良(430-A の双対で閉じた理由を外す)、L2 ℓ=1 の情報(396-D の良い点・補題 442-M)で ℓ=0 の窓を縛る、L3 λ についての $\chi_T$ の Harnack、L4 平均形(自然密度 1)からの格上げ。2026-10-21、w_E05_458_thin_sufficient = 書き下しの型、稿 `458_` §3・worklog §4.4、成算 S241)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((REG-L)・全列の真偽ではない)。4 本とも成算 1 割未満(L1 1% 未満、L2〜L4 0%)。
- **理由**:L1:閾 $\lambda^{-1/7}$ は $\alpha\lambda/M_{\min}^2$ の最悪 = 凍結の帯だけで要り(403-B の証明の $p\lt\frac12$ の場合分けが既にそれ以外を処理;404-A の巨視的な $s_*\asymp\alpha\lambda^{-3/7}$・430-C と同じ内容)、帯の中では 403-C の族で鋭い;凍結の帯の不在($\tilde Q\to0$)は在庫に無い。L2:442 J2(重い構造どうしの鋭い交差で ℓ=1 は滑らか、(REG-L) は偽)—— ℓ=1 の情報は ℓ=0 の擬交差を禁じない。L3:双極子では厳密(458-D (c)、定数 $(\lambda/\mu)^2$)だが、2 準位の峰で比 ≍ 1/s —— (REG-L) の言い換え。L4:415-A(P213)で消費者の余地は閾で尽き、格上げは 443-I の量化子の潰れ。
- **共通点(1 行)**:**(REG-L) は擬交差の相対の隙間 $\gg\lambda^{-1/7}$ の言い換えで、閾の改良は凍結の帯で止まり、他の情報(ℓ=1・平均・Harnack)は擬交差の鋭さ t に触れない —— 393 §3.4 (b)・F211・F223 と同じ段。**
- **R9**:閉じたのは方式。抽象の玩具・読みでは標的から従わない(404-B・442 J2;PF の上の強弱は主張しない —— 監査 462 §8);双極子で成る。
- **射程(T60)**:禁じるのは「403-A の閾を $M$ の下界の改良・ℓ=1 の情報・$\chi_T$ の Harnack・密度 1 からの格上げで緩める」発注。
- **再開条件**:凍結の帯の不在($\tilde Q\to0$ が全ての λ で)の供給、または F211 の再開条件 (1)。

## F289(E05、全列の命題 442-S の (S-stab$_G$)(E05-P236)を**専用の候補表 5 本**で供給する方式 —— S1 LL 型の配位ごとの議論(433-A・433-B の BO 下界)で励起構造の重さ、S2 双極子からのホモトピーで Φ を運ぶ、S3 ψ に依らない普遍の試行で G の下界、S4 スペクトルの局在 + 束縛励起の不在(HVZ 型)、S5 η-超勾配の固定(補題 458-E)+ 運動–質量の不等式 (KM)。2026-10-21、w_E05_458_thin_sufficient = 書き下しの型、稿 `458_` §3・§5、C0 695 J4、成算 S241)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((S-stab$_G$)・全列の真偽ではない;値は 448 C0 686 で否定でない)。5 本とも成算 1 割未満(S5 1〜2%、S4 1%、S2 1% 未満、S1・S3 0〜1%)。
- **理由**:S1:配位ごとの下界はエネルギーの下界 → 曲率 λf の下界 = 軽さの向き;重さは試行の向きで逆;433-C で全模型への移植は自明。S2:Φ の θ 微分に $\lambda\langle P_f\cdots\rangle$ が入り λ に一様でない;中間の θ で侵入者が現れ得る。S3:良い点の性質を使わない試行は各 λ の基底状態自身にも効き、全ての λ の h の下界 = 標的そのもの。S4:連続の模型で $E_0$ の上は連続スペクトル、埋め込まれた励起構造の不在・重さは在庫に無い;η/M = 2w/(1−p) は中間の λ で ≳ 1(λ=256 で ≈ 3)、凍結の帯の良い点では → ∞。S5:補題 458-E(厳密)で侵入者を 2 型に分けると、⟨T⟩ が g から θ 離れた侵入者は良い点の相対距離 $O(w/\theta)$ に $\ln F'$ の擬キンクを要り t が戻る;⟨T⟩ ≈ g の侵入者を禁じる (KM)「軽い η-準最小状態は ⟨T⟩ が g を超える」は玩具で偽(C0 695 J4:τ/g=0.93 で f=0.52 > f₀=0.436;正則化の η をそろえて比べ直しても残る —— A=0.238 で τ/g=0.994・f=0.595 > 基底状態の 0.539、監査 459 §5.2;値【T88】)。
- **共通点(1 行)**:**(S-stab$_G$) は t を外す唯一の型だが、移り先 (i) は励起状態(η 以内の ℓ=0 の部分空間)の重さで、在庫の道具は基底状態の情報(エネルギーの下界・試行)しか運ばない;侵入者を ⟨T⟩ で分けると片方は t に戻る。**
- **R9**:閉じたのは方式。抽象の玩具では標的から従わない(442-R、C0 661 J3:固定 λ・和則なし;PF の上の強弱は主張しない —— 監査 447 P-2〜P-4・監査 462 §8);双極子・π つきの 2 構造の梯子で成る。
- **射程(T60)**:禁じるのは「BO・配位ごとの下界で重さを出す」「普遍の試行で Φ を押さえる」「双極子から Φ を連続変形で運ぶ」「⟨T⟩ と f の状態ごとの不等式を構造(λT + H_f・和則)だけから出して軽い侵入者を禁じる」発注(玩具が否定したのはこの形;PF に固有の入力 —— 赤外の構造・漸近の λ —— を使う不等式は否定されていない、監査 459 §4.2)。止めないもの:ℓ=0 の低エネルギーの部分空間の HVZ 型の分解と束縛励起の応答の下界(448 S239 の破れる条件)。
- **再開条件**:F283 の再開条件、または埋め込まれた励起構造(共鳴)の不在・重さを与える入力が在庫に載ったとき。


## F290(E05、全列(行 E1-H)の類 C の検査を、光子数の上限 N つきの PF・有限モードの玩具(模型の梯子の M2〜M4)の大きい λ で行う方式 —— 擬交差・全列の向き(h→∞)を有限の模型の λ ≳ 4〜16 の値で読む。2026-10-21、w_E05_461_model_ladder = 書き下しの型、稿 `461_全列_模型の梯子_2026-10-21.md` §2.3・§2.4、C0 699〜702、成算 S242)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(全列・(NFT$_{\rm s}$) の真偽ではない)。
- **理由**:(1) 光子数の上限 $T_N=\frac12(P_N\Pi P_N)^2$ は有限次元で、大きい λ で基底状態を $P_N\Pi P_N$ の近い核へ飽和させる —— ⟨T⟩ の急な落ち(差分の κ 5〜7.6、⟨N⟩ が 1→5〜6)が N=6→8 で λ≈6→10〜16 と動き(C0 702)、小さい隙間(699 の 0.024 @ λ=64)は $\lambda\langle T\rangle$ と同じ桁の核の近くの帯の分裂で、擬交差でない。(2) 上限を外しても、1 成分の有限モードの玩具は補題 461-K1 で厳密に脱結合(F 有界・λ⟨T⟩→0;h→1 も厳密 —— 監査 462 の A-462-1、独立確認 confirm_A-462;値は C0 700・701)—— 全列の類似そのものが偽で、全列の向きの検査にならない(F204 の注の値の観察の厳密版)。(3) ベクトルの有限モードは F の飽和を禁じる(461-K2)が、±k で閉じた有限モードの切断は全ての λ で $F\lesssim\sqrt{\alpha\lambda V}$ の双極子の類で凍結の帯($F\gtrsim\lambda^{2/3}$)に入らない(E05-P234)うえ、上限 N で収束するのは λ ≲ 4 だけ(C0 702;D は N=8 で 1.3×10⁵)、障壁 $\Delta N\gtrsim\lambda^{4/7}$(417-A)に届かない。
- **共通点(1 行)**:**有限の模型は大きい λ で上限の人為か反断熱的な脱結合に支配され、擬交差の障壁(光子数の差 ≫ 1)も全列の成立も作れない —— 困難は多モードの極限にだけ在る(F204 の注・412b・597 と同じ所)。**
- **R9**:閉じたのは方式。双極子(M0)では全列の類似は真(h=1+4αλ/3π、在庫の既知の式)、1 成分の反跳の有限模型では偽(461-K1)—— 難しさは多モードの極限に局在し、消滅していない。
- **射程(T60)**:禁じるのは「光子数の上限つき・有限モードの玩具の λ ≳ 4〜16 の値を、全列・擬交差の類 C の証拠に使う」発注。止めないもの:N・モード数で収束した領域の凸性・κ の値;多モードの極限の外挿(モード数 n とともに $F_\infty^{(n)}$ が発散する冪、h の山の位置 λ*(n) の移動)。
- **再開条件**:(1) 光子数の上限なしで収束する多モード(≫ 16)の数値の道具(連続の HMC の段 = 412a・426 の系統)が全列の向きを直接読むとき;(2) 461-K の連続の版(核の非存在の量的な形)が在庫に載ったとき。


## F291(E05、全列の命題 442-S の (S-stab$_G$)(E05-P236)の余分の内容「良い点の η 以内に軽い侵入者が無い」を、**P の構造の和則 $f=1-2\lambda G$・ℓ=1 の応答 π・重さ(f が小さい)だけから出す方式** —— 値の記録(R1、成算なしの確認)。2026-10-21、w_E05_464_sstab_toy = 書き下しの型、稿 `464_` §0・§3・§4、C0 706〜712、成算 S241・S239 への追記)

親(G3 第 73 陣)が連結 2026-10-21

- **閉じたもの**:**方式**((S-stab$_G$)・全列の真偽ではない)。
- **理由(値【T88】)**:準位ごとの電荷を持つ内部準位つきの 1 次元 Fock 玩具 $H(P)=\frac\lambda2(P-Q)^2+H_f+V$、$Q=\bigoplus_s(P_f+e_sA)$(和則・π・重さ・別の ℓ=0 構造の擬交差を全て持つ)で、**一度も基底状態にならない軽い侵入者**(λ ∈ [0.5, 2.5] で基底状態の重み < 0.01、f ≈ 0.6)が良い点 λ′=0.98(f=0.021)の η 以内に居て $\Phi\ge f_\eta(B)=0.71$(w=0.01;Φ の 16 偶状態の下界 0.762〜0.932、w = 0.01〜0.1)(C0 709 v2)。交差する侵入者でも同じ(C0 708 I1:Φ = 0.774〜0.995)。単一種(構造 1 つ)の重い模型では否定でない(全偶空間で Φ − f ≈ 1.8〜2.3√w、C0 711)。
- **得たもの**:観察 464-C(有限次元の固有状態で $1-f_i^\eta\ge8\lambda\tau_i^2/(S_i+2(\Delta_i+\eta)\tau_i)$、$S_i=\frac12\langle[Q,[H_f,Q]]\rangle_i$;初等、self-audited)と補題 458-E (2) の合成で、軽い固有状態の侵入者は傾き τ が小さく、そのそばに g の擬キンク(458 §5.2 の型 (a)、θ ≥ $1-\tau_c/g$)が必然(スカラーの Q の模型で、侵入者自身の $S_i$ について $\lambda'g^2\gg S_i$ のとき;監査 462 §9) —— 玩具で g は相対距離 0.02 で 1.40 → 0.034。
- **共通点(1 行)**:**和則・π・重さは軽い侵入者を禁じない;値の上で禁じているのは g の滑らかさ(t の型)だけで、型 (b) の軽い固有状態は $\kappa_0\gt(1-c)/(1-f)$(基底状態の CS の効率;スカラーの Q の模型の読みで、3 次元の PF には $[Q_z,[T,Q_z]]$ の項のため移らない —— 監査 462 §9.3)で消えるが、型 (a) は t に戻る。**
- **R9**:閉じたのは方式。双極子では侵入者が無く (S-stab$_G$) が成る;π つきの 2 構造の擬交差の梯子(709)では侵入者は型 (a) —— 標的と同値な名指しを立てていない。
- **射程(T60)**:禁じるのは「和則($H(P)$ の形)・π・重さ・ℓ=0 の別構造の存在だけから (S-stab$_G$) の (i) を出す」発注。止めないもの:単一種に固有の入力(基底状態の応答のスペクトル測度の形 $\kappa_0$ と、3 次元の PF で $[Q_z,[T,Q_z]]\ne0$ の項を含めた 464-C の類似 —— 稿 464 §4.3 の「ℓ=0 での $S_{\rm PF}$ の普遍性」はスカラーの Q でだけ成る形式の読み、監査 462 §9.3)を使う型 (b) の消去;型 (a) は t の入力(393 §3.4 (b) の段)。
- **再開条件**:PF の基底状態の $\kappa_0$ の下界と、η-準最小状態(固有状態でない)への 464-C の拡張(余分の項 $\mathrm{Re}\langle Q^2\psi,(H-E_0)\psi\rangle$ の評価)—— 両方がそろっても型 (a)(t)は残る。


## F292(E05、難問 #3 = HP-G3-1 の Q3(有効質量の増大則)を**簡単な模型で調べてフル PF の上界の冪に還元する**方式 —— 候補 9 模型(双極子・剛体電荷の平均場・双極子 + 反跳の摂動・1 ループ・有限モード 1 成分・有限モードのベクトル PF・1 成分 n モード族・走る質量の 1 体閉包・背中合わせ対のチャネル)と還元の 5 段。2026-10-21、w_E05_468_toy_p3 = 書き下しの型、稿 `468_難問3_簡単な模型で有効質量の増大則_2026-10-21.md` §1・§3、成算 S248)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(簡単な模型の論法の還元)。命題(真の冪・上界の冪 3/2・2 より下の上界)の真偽は閉じていない。
- **理由(在庫 + 初等 + 値)**:(1) **模型の 3 類**:反跳を捨てる模型(双極子・剛体電荷の平均場)は冪 1 で問題が自明;多モードを捨てる模型(有限モードの 1 成分・ベクトル・各 n の n モード族)は $h\to1$(E05-P243、NUM-7018)、1 ループは対数で問題が消える;2 体の相関を捨てる模型(走る質量の 1 体閉包)は冪 $g/(1+g)$(補題 468-A)を出すが F14 で閉じた類(HS の $c_0\alpha^2\sqrt\lambda$ を落とす)。3 つを全て保つ最小の模型は対のセクターそのもので、自己無撞着の版は F21 で ill-posed。(2) **還元の 5 段**:通るのは $\Phi_a$ の冪 1(P195)・TRK の各 $k$(冪 2 の出所)・流れの積分(F5 の定理 3)の 3 段で全て在庫;止まるのは「反跳の分母で殻ごとに $m(k)/k$ を稼ぐ」段と「背中合わせ対の総運動量を $\sqrt{2M\lvert k\rvert}$ に局在させる」段で、どちらも大きい反跳運動量でドレスト分散が $\le\lvert q\rvert$(366-A・14_ 補題8)の線形になる所 —— F5(反跳エネルギーから殻重みの減衰は取れない)・F15(線形の下界は係数だけ)・F21・434 U4・F182 の再開条件 (1) と同じ。修正して通る段は無い。(3) 値(C0 753、【T88】):α=1・λ=256 で 1 体閉包 $h$=12.3・局所冪 0.456、1 ループ 5.13・0.17、HMC の $h_{\rm eff}(1)$ 4.85・0.5495 —— 1 体の機構は大きさと冪を同時に合わせない。
- **R9**:閉じたのは方式。R5 を通すのに要る「局所冪 $\le\gamma_0\lt1$(λ に一様)」は標的の局所の強化で名指しにしない;「$\le C\alpha$」の形は F5 で偽。双極子では局所冪 → 1(反跳が無く、PF の反例ではない);2 構造の擬交差の梯子では h の跳びが局所冪の上界を破る。障害は「対のチャネルの非摂動の重み」に局在し消滅していない。
- **再開条件**:(1) F182 の再開条件 (1)(閾値帯の重みの非摂動の抑制 —— F254 (4) の上界の冪 3/2)が出たとき;(2) 反跳・多モード・2 体の相関の 3 つを保ち、かつ対のセクターより真に単純な模型(質量の 4 スロットを 1 つに縮める正当化つき、F21 の転進先「最小結合形の一様な着せ替え」)が見つかったとき。


## F293(E05、難問 #2(HP-G3-1 の Q2):自己エネルギー $E_0$ の冪を、ゲージの着衣(直線の弦 —— 基点 b の Poincaré/Fock–Schwinger ゲージ $U_b=e^{-ie\chi_b(x)}$、軸ゲージ)をかけた積の試行で 5/7 より下げる方式;2/3 の具体の機構の候補「反跳の 1 方向を無料にする」を含む。2026-10-21、w_E05_467_toy_p2 = 書き下しの型、稿 `467_難問2_簡単な模型で自己エネルギーの冪の機構_2026-10-21.md` §4、C0 746、成算 S247)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**($E_0$ の冪の真偽ではない)。
- **理由**:着衣の後の結合は $`A^{(b)}(x)=-\int_0^1s\,(x-b)\times B(b+s(x-b))ds`$(作用素で成る古典の恒等式)。線の玩具(r=1)では恒等的に 0 で冪が ≤1/3 に落ちる(E05-P245〔命題 467-A〕)が、3 次元では磁場の全成分が残り、真空の大きさは $e^2\langle\lvert A^{(b)}\rvert^2\rangle\approx\alpha\ell/9$(ℓ≫1/Λ)対 $e^2\langle\lvert A(0)\rvert^2\rangle=\alpha/\pi$(C0 746:比 1.07 @ℓ=4、139.6 @ℓ=400)—— 積の最適の局在 $\ell\sim(\lambda/\alpha)^{1/7}$ では着衣が圧搾すべき揺らぎを増やす。「1 方向を無料にする」(軸ゲージで n 方向に L ≫ ℓ に拡がる)は、管の中の磁束の累積和の圧搾の費用 $`\sim\sqrt{\alpha\lambda L}\,\ell\ln L`$(勘定、値)が L=ℓ で 3 次元の積の費用と同じ、L>ℓ で超え、2/3 の費用には n 方向の紫外の局在(反跳 ∼λ)が要る。
- **共通点(1 行)**:**交差項で反跳を消す着衣は配位空間の接続が平坦なときだけ効き(r=1)、3 次元では残りが磁場(π の成分の非可換)で、局在の尺度 ℓ≫1/Λ では元の結合より大きい —— 着衣の族は 3 次元の積の勘定(5/7)に戻る。**
- **R9**:閉じたのは方式。双極子(r=0)では着衣は 1 点で自明(段は空);擬交差の梯子には触れない。難しさは「磁場の非可換を越えて交差項が反跳を部分的に消せるか」に留まる(消滅ではない)。
- **射程(T60)**:禁じるのは「直線の弦(Wilson 線)の着衣・Poincaré/軸ゲージの変換をかけた積・準自由の試行で 5/7 を割る」発注。止めないもの:着衣の基点を電子と磁場の配位に相関させる非 Gauss の試行(F227 の再開条件 (1) の族)。
- **再開条件**:磁束の圧搾が管の長さに対し劣線形($\sqrt L$ より遅い)で済む場の状態の構成が示されたとき。
- **成算**:S247(本方式は 1% 未満)。

## F294(E05、難問 #2:自己エネルギーの冪(2/3 か 5/7 か)を、単純化した模型 —— 少数モード、光子数の制限(≤2)、古典の場 + 量子の電子(Pekar 型)、固定した電子(双極子)、積状態・Hartree、偶模型、中心化した準自由状態、1 偏極の有限モード —— の冪の値か厳密な冪で決める方式。2026-10-21、w_E05_467_toy_p2 = 書き下しの型、稿 `467_` §1(表 T1〜T8)、成算 S247)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(簡単な模型で冪を決める型のうち、この 8 型)。$E_0$ の冪の真偽は閉じていない。
- **理由**:T1〜T3 は問題が消える(少数モードは F 有界か ≤1/2〔E05-P234・461-K〕、光子数の制限は圧搾が無く λ の 1 次、古典の場は零点の揺らぎが無く 0);T4 は反跳が無く 1/2(床);T5〜T7 は交差項の期待値が 0 で 5/7(E05-P191・P194、F227 (U1));T8 は Π 可換の戯画(F203)。どれも 2/3 と 5/7 の差(交差項)を保ったまま冪を出さない。保つのは反跳の方向の数 r の玩具(T9)だけで、そこでは r=1 で交差項が冪を下げる(命題 467-A)が、3 次元への還元は磁場で止まる(上の F293)。
- **共通点(1 行)**:**冪の差は交差項と多モードの局在の組み合わせにだけあり、どちらかを落とす単純化は「問題が消える」か「交差項 0 の壁」に落ちる。**
- **R9**:閉じたのは方式。双極子は T4 そのもの;障害は交差項に局在(F227・F258 と同じ)。
- **再開条件**:交差項と 3 次元の多モードの局在を両方保ちつつ厳密に解ける模型(例:r=2 の玩具の真の冪)が見つかったとき。
- **成算**:S247。


## F295(E05 の外・難問 #1 の模型の軸:1 光子の切断(Tamm–Dancoff、反跳つき)を厳密に解ける玩具にして、くりこみ族の存在と族に沿う分散関係の非退化の論法(裸の成分の Schur 補 + 有限階の $A^2$ の Woodbury の足し上げ)をフル PF に移す方式。2026-10-21、w_E05_466_toy_p1 = 書き下しの型、稿 `466_難問1_簡単な模型で構成の難所を特定_2026-10-21.md` §3・§5(S4・S5)、成算 S246)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(PF の族の存在 $\iota_{\rm PF}=0$・非退化の真偽は閉じない)。
- **理由(厳密 + 在庫)**:(1) TD の非退化は裸の成分 Ω の Schur 補が状態を運ぶこと($Z_\Lambda\to1$、命題 466-B (iv))に依る;PF のくりこみ族では (E2) で全ての有限光子数の重みが 0(A-247-1 = E05-P131、E05-P116)、特に $Z\to0$ —— 論法の要が PF では空。(2) TD の $1-2G=\frac1{1+2y}$ は $A^2$ が 1 光子の区画で階数 3 の核で入ることに依る;PF では反跳つきの $A(x)^2$ が多光子の空間で無限階、足し上げが立たない。(3) 字面の切断(ζ=1)は反磁性の応答を半分しか持たず Landau 型の極で族が終端する(466-B (ii)、α=1 で $`\Lambda_c=1.556\,m_{\rm ph}`$、値)—— 切断そのものがゲージの釣り合いを壊す。(4) 修正の試み:Ω の代わりに着衣の参照ベクトルで Feshbach–Schur をとると、補空間の区画の族に一様な隙間が要る = F225 の再開条件 (3);TD は PF の圧縮なので $E_{\rm PF}(P)\le E_{\rm TD}(P)+{\rm const}$ だが、差 $E(P)-E(0)$ の下界の向きは出ない。
- **共通点(1 行)**:**有限の区画への切断は、反磁性の足し上げを有限階にして分散関係の下界を只で与えるが、同時に着衣の雲((E2))を禁じて Z→1 の自明な極限に落とす —— PF の内容(Z→0 での下からの評価)には触れない。**
- **R9**:閉じたのは方式。双極子では 1 光子の切断は $h=\frac{1+\zeta x/2}{1+(\zeta/2-1)x}$ 型で、厳密解(ζ=1 で $1+x$)と釣り合いの値がずれる(切断の産物);擬交差の梯子(抽象の 2 枝)には 1 光子の区画が無く適用外。
- **射程(T60)**:禁じるのは「1 光子(または有限光子数)の切断の Schur 補・Woodbury の足し上げで、PF のくりこみ族の存在・非退化を出す」発注。止めないもの:≤2 光子の切断で釣り合い(ζ=1)と Z の向きを値で見ること(稿 §7 の残タスク (1))。
- **再開条件**:着衣の参照ベクトルについての Feshbach の補空間の族に一様な隙間(F225 の再開条件 (3));または有限光子数の切断で、反磁性の釣り合いを保ったまま $Z\to0$ になる族が見つかったとき。

## F296(E05 の外・難問 #1 の模型の軸:$A^2$ の係数 ζ(ζ>1 で質量のくりこみが有限)や形状因子の冪 s(s<1 で Gross の着衣が Fock)を連続に動かし、解ける側の構成をゲージの値 ζ=1・質量の発散の始まる s=1 へ運ぶ方式(双極子からのホモトピー 443 Q6 の構成版)。2026-10-21、w_E05_466_toy_p1 = 書き下しの型、稿 `466_` §2・§4・§5、成算 S246)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。
- **理由(厳密)**:(1) ζ-双極子(命題 466-A)で、ζ>1 のくりこみ族の極限 $m_0\to m_{\rm ph}\frac{\zeta-1}\zeta$ は ζ↓1 で 0 に潰れ、ζ=1 では族が有限の $\Lambda_c=m_{\rm ph}/\xi$ で終端 —— 族の型(有限のくりこみ → 終端)が ζ=1 で不連続に変わり、ζ>1 の Λ 一様な主張は ζ=1 へ運べない。TD-ζ でも同じ(釣り合い ζ=2 の上下で有界・極)。(2) s-族(§4)で、着衣のノルムと 2 次の質量の補正は同じ積分 $\int k^{2s-3}dk$ で、s↑1 で $\frac1{2(1-s)}$ 型に発散 —— 境目の s=1 は質量くりこみの発散の始まりそのもので、s<1 の構成(質量を動かさない)は参照の拡散係数を動かす s ≥ 1 の段(432-A、F230)に接続しない。(3) PF はちょうど境目の点にいる:ゲージ不変性が ζ=1 を固定し、質量は 2 次で対数($\frac{8\alpha}{3\pi}\ln$、s=1 の型)。
- **共通点(1 行)**:**PF は解ける族の内点でなく、族の型が変わる端点(釣り合いの点・質量の発散の始まり)に在る —— 内側からの連続変形は端点で一様性を失う。**
- **R9**:閉じたのは方式。双極子では ζ=1 の端点で族が終端(在庫の F230 R9 と同じ);擬交差の梯子には ζ・s の径数が無く適用外。
- **射程(T60)**:禁じるのは「ζ・s・形状因子の連続変形で、解ける側の構成(有限のくりこみ・Fock の着衣)を PF の値へ極限で運ぶ」発注。止めないもの:端点そのものでの評価(稿 §5 の S4・S5)。
- **再開条件**:ζ(または s)について一様な、族に沿う分散関係の下界が 1 本立ったとき。


## F297(E05、難問 #2 の模型の梯子:r=2 の玩具(面上の電子)で、線の玩具(E05-P245)の純ゲージの機構 —— 面内の 2 次元の縦の部分をゲージの着衣で消す —— により冪を 2/3 より下げる方式。2026-10-21、w_E05_469 = 書き下しの型、稿 `469_難問2_r2の玩具_2026-10-21.md` §2・§3、C0 747・748)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(r=2 の真の冪の真偽ではない)。
- **理由**:面内の場の重みのうち着衣で消せる縦の部分は 1/4(紫外)〜1/2(大きい尺度の極限)で、C0 747 で 0.250〜0.446、1/2 を超えない(札は BOUNDED:閾 T3「ℓ=100 で ≥0.45」を 0.446 で外した —— 1/2 への近づきが遅いだけで、GAUGE_FULL の 0.9 には遠い)。残る横の部分($B_3$)が反磁性を担い、着衣つきの積の族の局所冪は積と同じ 0.670(C0 748、λ=1e12→1e14)で比 0.764 の定数だけが変わる。下は補題 469-A の床 1/2 で、線の崩れ(≤1/3)は r=2 では起きない。
- **共通点(1 行)**:**純ゲージで消せるのは反跳の方向に沿った縦の部分だけで、反跳の部分空間の中に横波の方向がある(r≥2)と、その方向の場が床と反磁性を担い、着衣は定数しか変えない。**
- **R9**:閉じたのは方式。双極子(r=0)では着衣は自明;擬交差の梯子に触れない。難しさは「横の部分の交差項による追跡」に留まり、3 次元の 2/3 か 5/7 かと同じ型(1 次元下)。
- **再開条件**:横の部分($B_3$)を追跡するもつれの試行で、面内の反磁性の係数を局在の尺度とともに 0 へ下げる族が示されたとき。
- **成算**:S247(本方式は 1% 未満)。


## F298(E05、難問 #2 の模型の梯子:r=2 の玩具(面上の電子)で、3 次元の下界の鎖(282-A・282-B・282-C・298-A〜C・295-C・295-D・290-D、在庫 E05-P151・P152・P156・P158)を字面で運んで下界 $\alpha^{1/3}\lambda^{2/3}$(対数の精度)を出し、r=2 の冪を 2/3 と確定する方式 —— 4 時間の予算の 1 体で。2026-10-21、w_E05_471 = 書き下しの型、稿 `471_難問2_r2の下界2_3_2026-10-21.md` §1・§3・§4、C0 749、成算 S247 の延長)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(この予算・この在庫での字面の運搬)。r=2 の冪の真偽は閉じていない(区間 $[\frac12,\frac23]$:E05-P248 と命題 471-U)。
- **理由**:(1) 3 次元の鎖の基盤 —— 基底状態の存在・一意性(E05-F22)、定義域(E05-F26)、$E(P)\ge E(0)$(LHB 2011)—— の r=2 版が在庫に無く、関数積分の正値性と無質量のファイバーの基底状態の存在を r=2 で書き直す文献の分量(赤外の切断で押さえる段は書けるが、切断ありの存在に $E(P)\ge E(0)$ が要り循環)。(2) (S2)「$\langle a(\varphi)\rangle_0=0$」は J=0 から出ていたが、r=2 の対称性(面内の O(2)・z の反転・時間反転)は子午線の向きで $k_3$ に奇の電場の型の期待値を消さない(観察 471-S;全ての $\varphi$ の形が出ないという意味で、鎖が使う具体の $\varphi$ の不変射影が 0 ならその段は B1 に帰着する —— 監査 470)—— 282-A (iv)・295-C・215-C の段が誤差つきの再走になる(勘定では誤差は 2/3 の尺度で主要項と同じ桁で冪を落とさない)。(3) 面に垂直な向きのコヒーレンスは罰されず、組み立ては対数の損 $(\ln\lambda)^{-1/3}$ つき(補題 471-H、C0 749)—— これは障害でなく形。
- **共通点(1 行)**:**3 次元の鎖は、反跳の 3 方向の対称性(J=0)で線形の場の期待値を消し、文献の基盤の事実に乗っていた —— r=2 では対称性が足りず、基盤も文献に無い。冪を落とす段は見つかっていない。**
- **R9**:閉じたのは方式。双極子(r=0)では鎖は床だけ(段は空);擬交差の梯子には触れない。
- **再開条件**:(a) 面に拘束した電子の PF 型の模型のファイバーの基底状態の存在と $E(P)\ge E(0)$ の文献(または書き下し)が入ったとき;(b) 215-B・298-A/B・282-A・295-C を (S2) の誤差つきで再走したとき(この体の再開で続けられる);(c) 鎖が使う具体の線形の場の期待値について、r=2 の対称性の不変部分空間 $\lbrace\alpha\hat m:\alpha$ は $k_3$ に奇$\rbrace$ への射影が 0 と示されたとき(その段の (S2) は B1 だけに帰着;監査 470)。〔2026-10-21 注(監査 473):(b) は稿 472(E05-P251)で満たされ、(a) は文献の証明の r=2 への読み(472 §1;監査 473 §1 で横波性の 3 箇所と質量つきの (9) を補った)で代替された —— F298 の方式(4 時間・字面の運搬)の閉鎖は字面どおり;r=2 の冪は読みの下で 2/3(E05-P251)〕
- **成算**:S247 の延長(r=2 の冪の確定 2 割)。


## F299(E05、難問 #2 の下界側 K1:配位表示の BO(433-B)+ LL の場の側の罰を速い部分 $A_\gt$ で + 古典の帯域制限の場の中の 1 電子の磁気の下界 (MAG) で、全模型の $E_0\ge c'\alpha^{2/7}\lambda^{5/7}$ を出す方式。2026-10-21、w_E05_474_MAG = 書き下しの型、稿 `474_難問2_K1のMAGの書き下し_2026-10-21.md` §1〜§3、C0 779・780・781、成算 S228 の延長)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(K1)。5/7 の真偽(難問 #2 の標的)は閉じていない。
- **理由**:(1) (MAG) は 3 次元で偽(E05-P? = 命題 474-S):殻に Fourier の台を持つ発散なしの場は、球の上で任意の一様な場に $C^1$ で近づけられ(補題 474-D、超振動;代価は球の外の巨大な振幅)、ゲージで電子の磁気のエネルギーが消える;(2) 同じ配位が正の測度を持つので、433 §5.1 の BO の下界そのものが自明(命題 474-T)—— 433-C の障害(一様な大振幅)は Fourier の分割 $A\to A_\gt$ で消えない(ゲージの障害は位置の局所、分割は運動量の局所);(3) 直す余地:窓に局所の**振幅の**掛け算の罰 $\int wG(A_\gt)$($G$ 連続、$w\ge0$ の台は有界)は一様な大振幅を $\lVert w\rVert_1\inf G$ 程度(窓の体積 $W^3$、λ に依らない)でしか罰せない(監査 475 の A-475-3、厳密);LL の局在と両立する最良が $\min(\lambda/W^2,W^3)\sim\lambda^{3/5}$ という勘定は読み(λ/W² の側は未検査)。〔監査 475 で訂正:旧文「罰せるのは BO が捨てる Born–Huang の項(着衣の代価)だけ」は誤り —— 磁場の Hardy の罰と導関数の罰の設計 K1-B が別に残る(監査 475 §3.3 O-475-1)〕
- **共通点(1 行)**:**場の配位を固定して ess inf を取り、場の側を局所の振幅の罰($\lvert A\rvert^{-2}$ 型・$G(A(y))$ 型)で払う方式は、ゲージで電子に見えない局所に一様な配位(速い部分だけでも超振動で作れる)を窓の体積の大きさでしか罰せず、$\lambda^{5/7}$ に届かない。**〔監査 475 で範囲を縮小:旧文は「場の側の局所の罰」一般について述べていたが、磁場の Hardy の罰と導関数の罰はこの配位を罰する(O-475-1)〕
- **(0) の整合(記録)**:K1 は r=2 では 5/7 を出さない(Lemma 2.3 の定数 $n-2$ が 0、(MAG) の r=2 版は TM の模で偽、局在の冪 $\frac{2+r}{4+r}$)—— 471-U と矛盾せず、3 段とも $\pi_3$ を使う;K1 は J=0 を使わない(O-473-1 の天井の外)。閉鎖の理由は r=2 との整合ではなく 3 次元の (MAG) の偽。
- **ジョブ 433・459 の札の読み直し**:BOUNDED・MAG_PLAUSIBLE は周期箱 6π〜8π・平均振幅を固定した族の値で、(MAG) の量化子(全ての $A$)には情報を持たない(小さな箱に超振動の球は入らない)。
- **R9**:閉じたのは方式。双極子では BO は何も与えない(433 §3 の注)のと同じ機構が、速い場の局所の一様な配位で起きる;擬交差の梯子には触れない。
- **再開条件**:(a) Born–Huang の項(場の運動が電子のゲージの位相の配位依存に掛かる項)を下から評価する道具が入ったとき —— BO の枠の外の方式として別に立てる。〔監査 475 で追記〕(b) 射程の外として止めないもの:BO + ゲージ不変な罰(磁場の Hardy の罰 $\int w\lvert B\rvert^{-2}$ + 導関数の罰 $\int w\lvert\nabla^mA\rvert^2$)+ 導関数を抑えた 3 次元の磁気の下界(433 §5.3 (a) の本体)の設計 K1-B —— 本件の閉鎖(474-S・474-T)はこれに当たらない;成算未作成(R8)。

## F300(E05 の外・難問 #1・#3 の共通の結節 D3 候補 1:F254 の再開条件 (1)「PF の経路測度の拡散の尺度の CLT(特性関数の形)」と、それを #1 の非退化(F180・F225 (1))・#3 の上側の一様版(F182 (1))の共通の入口として文献から在庫に入れる方式。2026-10-21、w_E05_480_PF_CLT = 書き下しの型、稿 `480_難問1と3_PFの経路測度のCLTの文献照合_2026-10-21.md` §0〜§4、成算 S244・S246 の追記)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(文献から入れる道)。PF の CLT・$h_{\rm ls}\le Ch_{\rm sr}$・(iii-2)・Q3 の上側の真偽は閉じない。
- **共通点(1 行)**:**CLT は固定の結合・$p\to0$ の尺度の赤外の量で、#1・#3 の族に一様な評価(紫外の閾値帯・大偏差)と尺度が違う;PF に限っては固定の結合の CLT そのものも、確率カレントの重みを扱う方式が無いため文献に無い。**
- **R9**:閉じたのは方式。双極子では $S_T$ は Gauss で CLT は厳密(段は空);障害は「$x$ 依存の確率カレント × 無質量」に局在し消滅していない。
- **射程(T60)**:禁じるのは「スカラーの polaron/Nelson の CLT(KV・更新過程・Dobrushin)を PF に字面で移す」「CLT を #1 の非退化・#3 の上側の一様版の入口として発注する」形。止めないもの:PF の確率カレントの更新過程の表示そのものの構成(新しい確率論の定理);Hiroshima 2024 の章の照合([要入手])。
- **再開条件**:(1) Hiroshima 2024(DOI 10.1007/978-981-97-0364-7_10)か後続の文献に PF($P=0$、並進不変)の経路測度の CLT が載っていたとき;(2) 符号の定まらない二重確率積分の重みの下での CLT の一般の方式が文献に出たとき。

## F301(2026-10-21、w_E05_477_famB_stage2、書き下しの型)方式「族 B(RESPA + F4、T=6)の刻みの係数 c_δ を 4 → 2(一般に c_δ ≤ 3.2)に下げて、δ_B を縮めつつ λ=512 の門(受理 ≥ 0.6・1 軌道 ≤ 90 s)を 2080 Ti で通す」—— 費用で閉じた(方式の閉鎖)

親(G3 第 73 陣)が連結 2026-10-21

- 閉じたもの:**方式**(計算の設定)。標的(λ=256→512 の $h_{\rm eff}(1)$ の局所冪、全列の類 C の値の 3 段目)は閉じていない —— c_δ = 128/36 の条件つきの包装 `g3_e05_477_famb_s2` に移した(稿 `477_` §2)。
- 理由:c_δ を下げると N = 6λ²/c_δ が増え、1 刻みの費用は N に線形以上(段 1 の実測:N×4 で近接 ×6.6〜7.2・遠方 ×14〜16)、要る ε は c_δ に依らない(λ=128 の段 1 で c_δ=4・1 の ε 0.2195・0.2202)。楽観の下界(450 の smoke の 74.2 s を N に線形)でも c_δ=2 は 1 軌道 148 s、c_δ=3 は 99 s で門の 90 s を越える;段 1 の本番の 199 s からなら 398 s・265 s(C0 (研究ノート: `799_w_E05_477_famB_gate_count.py`))。門と帯 D(|δ_B| + 2σ ≤ 0.04)が楽観の側で両立するのは c_δ ∈ [3.30, 3.85] だけ。
- 再開条件:2080 Ti より 2 倍以上速い GPU(計算機 2 の 5090)が族 B に空く、または 1 軌道の費用を下げる装置の変更(積分器・前処理)。
- 値であって上下界ではない【T88】。


## F302(E05、難問 #2 の下界側 K1-B の字面の版:配位表示の BO(433-B)+ ゲージ不変な罰(磁場の Hardy の罰 $c\int w\lvert B\rvert^{-2}$ + 固定の有限の階数の導関数の罰 $\int w\lvert\nabla A\rvert^2$・$\int w\lvert\nabla B\rvert^2$、一般に $\int w\lvert\nabla^mA\rvert^2$、$m\le M$ で M は λ に依らない)で $E_0\ge c'\alpha^{2/7}\lambda^{5/7}$ を出す方式。2026-10-21、w_E05_479_K1B = 書き下しの型、稿 `479_難問2_K1Bの類Cの判定_2026-10-21.md` §1・§2、C0 809)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(監査 475 §3.3 O-475-1 の 3. の字面の K1-B、および固定の有限の階数 M の導関数の罰を持つ全ての版)。5/7 の真偽(難問 #2 の標的)は閉じていない。λ に依る階数 $M\sim\log(\lambda/\alpha)$ の版 K1-B′ は閉じていない(稿 479 §2.3、札 K1B_NEEDS_INPUT)。
- **理由**:局所の螺旋(Beltrami)場 $A=b\varepsilon(\cos(z/\varepsilon),\sin(z/\varepsilon),0)$($\lvert B\rvert=b$ 一定、$\lvert A\rvert=b\varepsilon$、$\lvert\nabla^mA\rvert=b\varepsilon^{1-m}$)を電子の球の上に置き(補題 474-D の $C^k$ 版で正の測度)、$\varepsilon=b^{1/(M-1)}$ とすると階数 ≤ M の罰は真空の水準、Hardy の罰は $c\ell^3/b^2$、電子の費用は試行 $u=\phi_\ell$(実)で厳密に $\lambda/\ell^2+\lambda\alpha b^2\varepsilon^2$。BO の値は $\le C\lambda^{(5+3s)/(7+5s)}$、$s=1/(M-1)$:字面の版(M=2)で $C\lambda^{2/3}\alpha^{1/6}$。外側の配位の寄与は罰の真空期待値 ≤ 0($H_f\ge V$、$\langle\Omega,H_f\Omega\rangle=0$)と空間平均の集中による(読み;監査 483 の監査人の補題 A-483-1 で正の測度の組み立てを補った —— 外側の寄与の期待値 ≤ 0 の事象と Cameron–Martin の平行移動)。C0 809 で冪 0.6666(M=2)〜0.7068(M=11)、M → ∞ で 0.7143(値【T88】)。〔監査 483:809 の族は導関数の罰を真空の水準に留める部分族;罰を払う螺旋では固定の M で冪 $(5M+1)/(7M+3)$(M=2 で 11/17、C0 827)—— 閉鎖の向きは強まる〕
- **共通点(1 行)**:**有限の階数の局所の導関数の罰は球の上の $C^M$ の制約にすぎず、帯域制限の場の超振動はそれを満たしたまま尺度 $b^{1/(M-1)}$ の螺旋を作れる —— 475 §3.3 の勘定の暗黙の仮定「尺度 1」が罰で固定されない**(A-475-2「速い帯域制限は局所の制約にならない」の別の顔;F299 の振幅の罰の閉鎖と同じ根)。
- **(0) の整合(記録)**:K1-B は r=2 では 5/7 を出さない —— 面の円板の上で $A_\parallel=0$($B_3=0$)の配位を Hardy の罰 $\lvert B\rvert^{-2}$ がすり抜け、r=2 の値は $\lambda^{3/5}$ 以下(E05-P249 と整合)。閉鎖の理由は r=2 との整合ではなく 3 次元の尺度の非固定。
- **R9**:閉じたのは方式。双極子では場が $x$ に依らず $B=0$、Hardy の罰が無制限 —— BO は双極子で何も与えないのと整合;擬交差の梯子には触れない。
- **再開条件**:(a) 階数が λ に依る罰($M\sim\log(\lambda/\alpha)$)の版 K1-B′ —— 本件の閉鎖の外;要る下界は 3 次元の弱い場の Neumann の下界 (WF3)($\lambda_1^N(Q,eA)\ge c e^2\lVert\mathrm{curl}A\rVert^2_{H^{-1}(Q)}$、2 次元の版は Fournais–Helffer 2010 §2.2 (2.21))と M ≈ log λ で一様な補間 (INT)(稿 479 §3)。(b) 無限階の掛け算の罰(整関数の記号)は超振動で欺ける見込み(稿 479 §2.4、読み)—— 再開条件にしない。
- **監査記録**(2026-10-21、audit_S2_479_482 = 監査の型、合同 S2、監査稿 `483_合同監査_K1BとK1Bprimeの類C_479_482_2026-10-21.md`):方式の閉鎖は **PASS with fixes** —— 天井は成り、罰を払う螺旋では固定の M で $(5M+1)/(7M+3)$ とさらに低い(C0 827);外側の配位の正の測度は監査人の補題 A-483-1(**独立確認 `confirm_A-483`〔監査の型、2026-10-21〕で CONFIRMED with fixes**:同時の正の測度・外側の罰の期待値の上界の定性の版は盲検で成立;量の版は、483 の Gauss の評価が異方的な共分散で偽〔確認者が訂正形を与えた〕ことと、内縁の一様な相関の下界〔読み〕を要する。A-483-2〔凹な立方体の和〕は CONFIRMED。確認者の補い 2 点の独立確認 `confirm_A-416_A-483fix`〔監査の型、2026-10-21〕:Gauss の評価の訂正形は CONFIRMED;内縁の相関の下界は読みのまま —— 係数のコンパクト性は不要で各点の $\rho(y)\lt1$ は成り、残る読みは赤外の引き算で定義した $F_0$ の版での一様性 $\sup_y\rho(y)\lt1$ だけ。ゆえに量の版は読み 1 本つき;LL 型の窓 $r_w\lesssim\ell$ では本文の配位で足り A-483-1 に依らない);§2.4 は読みとして PASS。再開条件 (a) の K1-B′ は監査 483 §5 で「立方体ごとの不等式 (PC_M) + 凹な和」に組み直し、残る難所は強い場の域 (v) と場の側の 2 つの罰。

## F303(2026-10-21 12:4x 親が smoke の実測で連結)(2026-10-21、w_E05_477_famB_stage2、書き下しの型)方式「族 B・T=6 の段 2(λ=512)を 2080 Ti で回す(c_δ = 128/36、適応の目標 0.65)」—— 費用 / 偏りで閉じた(方式の閉鎖)

親(G3 第 73 陣)が連結 2026-10-21

- 連結の条件:smoke `g3_e05_477_famb_smoke` の SM_P512 の 1 軌道が 90 s を越えた、または本体 `g3_e05_477_famb_s2` の札が BOUNDED「B512_GATE_FAIL_c3556」・BOUNDED「D_MIDDLE」・COUNTEREXAMPLE「B_BIASED_c3556」。**当たった:smoke の SM_P512 の 1 軌道は中央値 90.81 s・平均 97.87 s(2 軌道、計算機 1 2080 Ti、ε=0.17 固定)で門 90 s を越えた**(SM_P256 は中央値 8.35 s)。
- 閉じたもの:**方式**。標的(λ=256→512 の局所冪)は閉じていない —— 族 A の λ=512 は F285 の再開条件(5090 の 70 h、承認事項)のまま。
- 理由:smoke の SM_P512 の 1 軌道 90.81 s(中央値;門 90 s、事前に固定、緩めない)。族 B・T=6 で門を通す c_δ の窓は [3.30, 3.85](稿 `477_` §1)で、その中央の c_δ = 128/36 が門で外れた —— 窓の端(c_δ → 3.85 は帯 D の余裕 0、c_δ → 3.3 は門の時間の余裕 0)に動かしても両立しない。
- 再開条件:5090 が族 B に空く(1 軌道が約半分)、または 1 軌道の費用を下げる装置の変更。
- 値であって上下界ではない【T88】。


## F304(E05、全列の困難の地図の模型の軸 (V):有限モードの横偏光のベクトルの PF で $G(\lambda)\to0$〔h→1、E05-P243 のベクトル版〕を、(a) 一様な隙間の上界 $G\le\lambda\lVert\Pi^1\psi\rVert^2/{\rm gap}$、(b) 交換子の方法(命題 478-V)+ エネルギーの先験評価、で示す方式)(2026-10-21、w_E05_478_model_axis、書き下しの型、稿 `478_全列_模型の軸の読みの訂正_2026-10-21.md` §3.4)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((a)・(b) の 2 つ)。標的($G\to0$)は閉じていない —— 値では強く成る向き(主項の式 $G\approx2e^{-2r}\sum_jc_j^2(\varepsilon^1_j)^2/\lvert k_j\rvert^2$ が NUM-7018 の h と λ=4096 で相対 1.3×10⁻³・4×10⁻⁴、C0 806)。
- **理由**:(a) 隙間は √λ の桁(値:gap/√λ → 1.20・0.65)で、上界 $\frac23\lambda F'/{\rm gap}$ は値で ≈ 1.02・1.01(λ=4096)—— 0 に行かない;$\Pi^1\psi$ の費用は隙間でなく $\lvert P_f\rvert\ge1$ の部分の反跳 $\lambda\lvert k\rvert^2/2$ で、隙間の上界はそれを見ない。(b) 命題 478-V(厳密、定義域の仮定 (D) つき)は $(\sqrt M-\sqrt R)_+^2\le G\le(\sqrt M+\sqrt R)^2$ を与えるが、M・R → 0 には基底状態の $\ker P_f$ への集中($\lVert P_f\psi\rVert^2=o(\lambda^{-1/2})$)と対の $p_-$ の縮みの先験評価が要る。エネルギーは $\lambda\lVert\Pi\psi\rVert^2\le2F$ と $\langle H_f\rangle\le F$ だけを与え、交差の項 $2A\cdot P_f$ は符号を持たないので $P_f$ と $A$ を別々に抑えない;$H_f$ による $\langle A^2\rangle=O(\sqrt\lambda)$ は要る $O(\lambda^{-1/2})$ に λ だけ足りない。
- **共通点(1 行)**:**基底状態の期待値を、エネルギー($\lvert\Pi\rvert^2$ と $H_f$)だけで抑える方式は、$\Pi=P_f+A$ の 2 つの部分を分けられない —— $\lvert P_f\rvert\ge1$ の部分の反跳の費用 λ を使う Schur の補行列の議論が要る。**
- **再開条件**:スクイーズの枠で $\lvert P_f\rvert\ge\kappa_{\min}$ の部分の上の $H-E\ge c\lambda$ と、$\ker P_f$ との結合 $\frac\lambda2e^{-2r}A^2$($O(\sqrt\lambda)$)の相対有界性の形が見つかる;または $\inf\sigma(H-sP_f^2)\ge E_0-o(\lambda^{-1/2})$(s>0 固定;凹性で $s\langle P_f^2\rangle_\psi\le E_0-\inf\sigma(H-sP_f^2)$)〔監査 481 §4.2 で訂正:原文の $H+t\lambda P_f^2$ の下界は $\langle P_f^2\rangle$ の下界しか与えない;$H-sP_f^2$ は s が O(1) を超えると下に非有界の見込み(雑な試行)、要る評価は標的と同じ強さで R9 の懸念あり〕。
- **R9**:閉じたのは方式。双極子は $P_f$ を含まず問いにならない(461-H で h → ∞ が厳密);擬交差の梯子には触れない。
- 値であって上下界ではない【T88】(C0 806・807 の部分)。


## F305(E05、全列(行 E1-H)の核 K-t の類 C を、λ ≤ 10³〜10⁴ の 2 進区間ごとに凍結の帯の擬交差を**全数で**押さえる計算機援用のジョブ(計画 Ⅲ:厳密 = 区間演算、または値 = 431 の HMC の装置の 1/4 オクターブの走査)で決める方式。2026-10-21、w_E05_488_CAP_Kt、稿 `488_` §1〜§3、成算 S252)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:方式(置き方 —— 予算の内の資源で λ ≥ 10³ に届かない)。命題の真偽・標的は閉じていない。
- **理由**:(i) 厳密の版は F197 の理由そのもの(固定の λ でも $g=F'$ の厳密な両側の囲い込みは無い)。(ii) 値の版:431 の装置の 1 軌道の秒は λ について冪 e = 3.20(C0 860:λ=256 で 53.1 s、CPU 1 スレッド)、λ₀=1024 の 1 窓(5 点 × 2 rep、σ_κ ≈ 0.04)で GPU 32.6 h(426 の 5090 の効率を保つ楽観)・CPU 6480 コア時 —— 閾(12 h・48 コア時)の 2.7 倍・135 倍、10⁴ の窓は 3〜4 桁超過;微視の類(ΔM = O(1))は 270 h(C0 859)。(iii) P205 は例外集合の測度だけを縛り位置を与えず、その上界も $c_2$(P158)の数値が無いため $r=C_U/c_L\le3.4$ のときだけ空でない(C0 858)—— 窓の数え上げで走査を狭められない。
- **共通点(1 行)**:**全数の走査の費用は軌道の秒(λ^{3.2})が支配し、在庫の定理は走査の場所を狭めない(測度だけ)ので、有限の窓の全数は λ ~ 10³ で資源を桁で超える。**
- **射程(T60)**:禁じるのは「λ ≥ 10³ の 2 進区間を 431 の装置で全数走査する」発注(12 h・効率の監査なしの枠で)。止めないもの:[128,1024] の窓の値の走査(GPU 0.3〜18 h、稿 488 §3.3 —— 431 の続きの族)、推定量・核を替えた装置の費用の再見積もり。
- **再開条件**:(1) 1 軌道の費用の冪を下げる核(力の $N^2$ を $N\log N$ にする等)が在庫に載り、本番の機械の smoke で λ=1024 の 1 軌道が 5 s 以下になったとき;(2) $c_2$ の数値が在庫に載り $r\le3$ と分かって、P205 に位置の情報を足す命題が出たとき。
- **R9**:閉じたのは方式。K-t((NFT$_{\rm s}$))の真偽には何も言わない(有限の窓の値は漸近を運ばない:P234・F197)。


## F306(E05、全列(行 E1-H)の核 K-S を**計画 Ⅱ「エネルギーだけの質量の不等式」**で直接出す方式 —— 全ての λ の η-準最小状態で 1 次の慣性の汎関数($\langle N\rangle$・$\langle H_f\rangle$・$\langle P_f^2\rangle$・場の変位・$G_{\rm sr}$ の 1 次の代用 = CS の比 R)が $\Phi(\lambda)\to\infty$ 以上、かつそれが重さ($f_\eta\to0$)を与える;および集中コンパクト性で「軽い成分」がエネルギーを $c\lambda^\beta$ 上げることを在庫の下界の道具で示す。2026-10-21、w_E05_487_mass_inequality = 書き下しの型、稿 `487_全列_計画2_質量の不等式_2026-10-21.md` §0〜§5、C0 852・853、成算 S251)

親(G3 第 73 陣)が連結 2026-10-21

- **閉じたもの**:**方式**(K-S・(S-stab$_G$)・全列の真偽ではない;値は真の向きのまま —— NUM-6919・NUM-7084 と矛盾なし)。類 C の (0) が否定で、書き下しに進んでいない。
- **理由**:(1) **エネルギーが制御する量**:補題 487-V(self-audited、厳密・初等:$H(\lambda)=KH(\lambda/K)-(K-1)H_f$ と在庫の冪 P158・P167)で全ての η-準最小が $\langle H_f\rangle\ge\frac{c^3}{16C^2}\lambda^{4/7}$、$\langle N\rangle\ge\langle H_f\rangle-\eta$ —— (C1) は自動で、(C2) を準最小に限れば全ての λ の K-S と同値(R9:言い換え)。閾を基底状態の値 $M=E-\lambda g$ の近くに置くと、$\langle H_f\rangle=\langle H\rangle-\lambda\tau$ から I2 の質量の不等式は (KM)(F289:玩具で偽)と η/λ の誤差まで同値(観察 487-K)。C0 852:型 (a) の侵入者は $\langle V\rangle$ が基底状態より大きく($0.81\gt0.50$、$f_\eta=0.60$)、型 (b) は等しい(0.51、$f_\eta=0.60$)—— I2 は侵入者を逆向きに読むか区別しない。(2) **G の 1 次の代用 R**:双極子では分離したモードが測度を 1 点に集めて $R\to1$(C0 853:λ=10⁴ で 0.99958)だが、PF では $[Q_i,Q_j]$ = 原点の磁場の 2 重交換子 $\lambda e^2\langle B_\perp^2\rangle\asymp\lambda\tau$ が分母を支配し $R\asymp\tau\sim\lambda^{-2/7}\to0$(値、LL の積状態の勘定)—— 基底状態自身で使えない。(3) **場の変位**は ℓ=0 で横性により恒等的に 0;Pekar の質量の読みはコヒーレントの汎関数が $\asymp\alpha\lambda\gg E_0$(F277 (1))で運べない。(4) **集中コンパクト性**:軽さの費用の冪は E₀ と同じ(F283 の値 $\Theta\approx F\delta^2/C^2$)で、分離には主項の定数の精度が要る;在庫の下界は冪から合わず(2/3 対 5/7)分解能 0;E₀ の尺度に輪郭(極限の対象)が無い;凍結の帯では $\eta/M\to\infty$。
- **共通点(1 行)**:**エネルギーが制御する 1 次の量は $(\langle T\rangle,\langle H_f\rangle)$ だけで侵入者を区別せず((KM) に戻る)、重さの 1 次の代用(CS)は ℓ=1 のスペクトル測度が 1 点に集まる模型(双極子・スカラーの Q)でしか鋭くなく PF の磁場の交換子で壊れる;CC は定数の精度を要し計画 Ⅰ の極限汎関数に戻る。**
- **R9**:閉じたのは方式。双極子では (C1)(C2)・R→1 が全て成る;擬交差の梯子(429-U・438-B・443-U)は ℓ=1 を持たず判定しない;π つきの重い 2 構造(442 J2)では自明に成る;軽い侵入者の玩具(442 J3・464・C0 852)で I2 の (C2) は偽。新しい名指し 0 本。
- **射程(T60)**:禁じるのは「$\langle N\rangle$・$\langle H_f\rangle$・$\langle T\rangle$ の関数で重さを判定する」「CS 型(Schwarz の 1 段)の G の下界で準最小の重さを出す」「在庫の下界の道具(LL・BO・P151・P158)だけで軽い成分のエネルギーの費用を出す集中コンパクト性」の発注。止めないもの:計画 Ⅰ(冪の決着 → 極限汎関数 → 非退化性 → 量的な強圧性);多段のモーメント(Padé)の G の下界で磁場の項を含めたもの(成算 1% 未満と読む、未試行)。
- **再開条件**:(1) 難問 #2 の冪が決まり E₀ の主項の定数(漸近 $E_0=a\lambda^p(1+o(1))$)が在庫に載ったとき;(2) PF の原点の磁場の揺らぎ $\langle B(0)^2\rangle$ が基底状態で $o(\tau)$ に絞られることが示されたとき(I5 が再び立つ);(3) F283 の再開条件。

## F307(E05、全列(行 E1-H)の計画 Ⅰ 段 2:**2/3 の尺度**($E_0\asymp\alpha^{1/3}\lambda^{2/3}$)で 3 次元の PF の強結合の極限汎関数を立て、(β)〔一意な有効の対象〕の候補にする方式。2026-10-21、w_E05_486_limit_functional = 書き下しの型、稿 `486_全列_計画1_強結合の極限汎関数の偵察_2026-10-21.md` §2、worklog §2、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(2/3 の尺度で候補を立てる道)。冪 2/3 か 5/7 かの真偽(難問 #2)は閉じない。
- **理由(読み + 値)**:Γ-limsup の試行が無い —— (i) LL の積の族の最適は 5/7(F258 (K3)、稿 486 の LDA の冪 0.7143);(ii) LL 1999 Thm 1.2(本文照合 (1.9)〜(1.10)):交差項を落とした模型は上下とも $\asymp\alpha^{2/7}\Lambda^{12/7}$ で、2/3 には交差項の相関が主項を変える必要があるが、積の状態のまわりの $p\cdot A$ の 2 次の利得は値で相対 $(\alpha/\lambda)^{2/7}$;(iii) 螺旋の敵対者(NUM-7064 の M=2)は下界の方式の敵対者で、量子化すると波長 $(1,\ell)$ の真空の $\langle A^2\rangle$ がゲージで消えず、絞ると積の LDA(5/7)に戻る;次元の合う局所汎関数 $\frac12\lVert\nabla u\rVert^2+c\int\lvert u\rvert^{4/3}$ は機構を持たない。
- **共通点(1 行)**:**3 次元で場の費用を ℓ に比例させる機構(r=2 の面の局在が与えるもの)は、ゲージで見えない一様な配位か交差項の相関にしか無く、前者は量子の零点の揺らぎで、後者は 2 次で相対 $(\alpha/\lambda)^{2/7}$ に落ちる。**
- **R9**:閉じたのは方式。双極子では局在が場に効かず尺度の極限は自明;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「3 次元の PF で 2/3 の尺度の極限汎関数を在庫の試行の族から立てる」発注。止めないもの:交差項の相関が主項の定数・冪を変えるかの非摂動の検査(難問 #2 の下界側の族);r=2 の玩具の極限汎関数(2/3 で正しい)。
- **再開条件**:3 次元で $O(\lambda^{2/3})$ の試行状態(交差項の相関を持つもの)が構成されたとき、または難問 #2 が 2/3 に決着したとき。
- **成算**:S250。

## F308(E05、全列(行 E1-H)の計画 Ⅰ 段 2(S2-c′):交差項なしの偶の模型 $\frac12(p^2+\alpha A^2)+H_f$ で、LL 1999 の下界の鎖((2.28)・Lemma 2.3・(2.31)〜(2.33))を延長して Φ57(E05-P257)の定数 $e_\infty$ まで(率 o(w) で)運び、定数つきの Γ-liminf を出す方式。2026-10-21、w_E05_492_Gamma_even = 書き下しの型、稿 `492_全列_計画1_偶の模型のΓ収束_2026-10-21.md` §0・§1、C0 881、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(LL の鎖の延長)。偶の模型の基底エネルギーの定数の真偽(Φ57 に一致するか)は閉じない。
- **理由(初等 + 値)**:鎖の下界は、状態ごとに w を選んでも局所の 2 定数を鋭い値に替えても、$e_\infty S(u_*)^{4/7}$ 以下。$S(\varphi)=\sup_{0\le w\le1}\iint\varphi\varphi w/(\sqrt{\int w}\lVert\varphi\rVert_1)$ は位置をまたぐ Schwarz (2.31) の重なりの因子で、対称減少の φ では球の指示関数で達成される(浴槽原理)。$S(u_*)=0.5442$ なので 70.6% 以下(C0 881;対照の一様な球 0.50041 は閉じた形と一致)。字面の定数($K/c_*=\sqrt2/6$:Hardy 型の 1/3 と (2.28) の 1/4)では 30.9%。
- **共通点(1 行)**:**Φ57 の場の項 $\int\sqrt\rho$ は凹で非 2 次だが、LL の鎖は位置をまたぐ Schwarz で並進不変な 2 次形式に置き換える —— 台の中の自己相関の不均一の分だけ、λ に依らない因子を失う;局所の段の修理(Hardy → 振動子)も、同じ点・同じベクトルで組むために平均場の正確さを要する。**
- **R9**:閉じたのは方式。双極子では A(0) が一様で局在が場に効かず、鎖は空;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「LL の (2.31) 型の位置をまたぐ Schwarz を含む下界の鎖で、Φ57 の定数を出す」発注。止めないもの:偶の模型の配位表示の BO(433-B)の場の問題 $\inf\sigma(H_f+E_{\rm el}(A))$ と平均場の比較(ゲージの障害 F299 は偶の模型には無い);冪だけの下界(LL Thm 1.2 で既知)。
- **再開条件**:凹な $E_{\rm el}(A)$ の期待値を準自由(積)の値で下から押さえる道具 —— F115 の再開条件の前半 —— が入ったとき。
- **成算**:S250。


## F309(E05、全列の困難の地図の模型の軸 (V):有限モードの横偏光のベクトルの PF で $G(\lambda)\to0$ を、(c) Feshbach の分け方 $\bar P=1_{\lbrace P_f\ne0\rbrace}$(格子の条件 $\lvert P_f\rvert\ge\kappa\gt0$ の下)と先験の評価で示す方式)(2026-10-21、w_E05_489_model_axis2、書き下しの型、稿 `489_全列_模型の軸の残り2族_2026-10-21.md` §3)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたのは方式**(標的 $G\to0$ は閉じていない;値は強く支持)。F304 の (a)(b) に続く 3 つ目の方式。
- 方式:補足 489-F(厳密)—— 横偏光で $\bar PHP_0=\frac\lambda2\bar PA^2P_0$(1 光子の項 $P_f\cdot A$ は $P_0$ から出ない)、$d=\bar PH\bar P$ が $d-E\gt0$ なら $G=G_F+G_\chi$、$G_F=\lambda\langle\bar\varphi,(d-E)^{-1}\bar\varphi\rangle\le\frac23\sqrt{S_AW/2}/(\bar\delta\sqrt\lambda)$(F304 (a) の $\lVert\Pi^1\psi\rVert^2\le\frac23F/\lambda$ と組む)、$G_\chi=\lambda\langle\chi,F^{-1}\chi\rangle\ge0$(F は Schur の補行列)。
- 止まる所:(F1) $\bar\delta:=(\inf\sigma(d)-E)/\lambda\ge c$(λ に一様)—— $\lvert P_f+A\rvert^2$ は $P_f\ne0$ でも A が打ち消せば小さく、A の下界はエネルギーから $O(\sqrt\lambda)$ の光子数の分しか出ない;(F2)(F3) $G_\chi\to0$ —— $\chi\ni\frac\lambda2P_0A^2\bar P(d-E)^{-1}\bar\varphi$ の A² を $(d-E)$ で相対有界に抑えるにはスクイーズの枠の A の小ささが要り、先験の $\lVert A^2u\rVert\le C\lVert(N+1)u\rVert$・$\langle N\rangle\sim\sqrt\lambda$ では λ の冪が足りない。分解は $G\ge G_F$ の向きしか与えない。〔監査 493a(A-493a-1・A-493a-2、confirm_A-493a で CONFIRMED):$\gamma_F\ge{\rm gap}$ は厳密;対ごとに非退化な模型では $G_\chi=0$ で $G\to0$ は (F1) 単独に帰着(格子の条件と両立する非退化の模型は $k_p$ が 1 次独立な対 3 本以下)—— (F2)(F3) は $\ker P_f$ が対ごとの釣り合いより広い模型(立方 12 モード・対が 4 本以上の周期箱)にだけ残る〕
- 共通点(F304 と):**エネルギーの先験評価では $\lvert P_f+A\rvert^2$ の中の $P_f$ と A を分けられない**。本方式はそれを (F1)(非零の $P_f$ の打ち消し)と $G_\chi$(A² の相対有界性)の 2 か所に局所化した。
- 値(C0 868・869):$G=G_F$ が 6 桁(N = 4・6・8、λ ≤ 4096);$\bar\delta$ = 0.227・0.313・0.384(e=1.5、N=6、λ = 256・1024・4096)と λ とともに増えるが N とともに下がり(N=8 で 0.197・0.360)、札 BOUNDED。
- 試したが閉じなかった補助の道:pull-through(ずれたファイバーの不等式 $\inf\sigma(H(k_j))+\omega_j\gt E$ が (F1) と同じ型);$E(\xi)$ の下界への言い換え(2 次の摂動で G に戻る);2 次形式の下界($\lambda P_f^2$ を落とすと $A\cdot P_f$ が残る)。
- 再開条件:(F1) を格子の条件の下で示す(例:$\bar P$ の上で $P_f$ の値ごとの下界と、A による打ち消しの状態の費用を反スクイーズの $x_-$ の揺らぎで抑える評価)と、スクイーズの枠での A² の $(d-E)$ に対する相対有界性。連続の PF には移らない($\kappa\to0$ で (F1) が壊れる、稿 489 §3.5)。
- R9:双極子では $P_f=0$ で分け方が空(h = 1+λξ、461-H);擬交差の梯子は模型でない;(F1) は G の上界の一部で標的と同値でない —— 新しい名指しは立てない。

## F310(E05、全列(行 E1-H)の計画 Ⅰ 段 2(J-C の裾 (i)):補題 495-J の裾を、(a) 上限なしの $G_{1/2}$ と「支えの外の静かな塊の数 × 塊ごとの大偏差」で $o(\ell^{-2})$ にする方式、(b) 電子を局在させない全空間の BO の下界 $H\ge H_f+E_{\rm el}(A)$ で偶の模型の定数を出す方式。2026-10-21、w_E05_496_tail_i = 書き下しの型、稿 `496_全列_計画1_裾iの多重尺度の評価_2026-10-21.md` §0・§1、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((a)(b) とも)。裾 (i) と偶の模型の定数の真偽は閉じない —— 修理した版(命題 496-T、IMS の箱 + 上限つきの M)は立った。
- **理由(初等)**:(a) 上限なしの条件は、運動の費用で電子が入らない遠くの小さい塊でも破れ、塊 1 つの確率は ℓ に依らない正の定数、点の数は $\gtrsim\ell^3$ —— $o(\ell^{-2})$ にならない(所見 A)。(b) 真空の Gauss の配位では任意に大きい静かな球がどこかに a.s. あり、$E_{\rm el}(A)=0$ a.s.、場を真空にして $E_{\rm BO}\le0$(所見 B)—— BO は静かな場所とともに動く電子の状態の場の運動(Born–Huang)を捨てる。
- **共通点(1 行)**:**確率的な場の中の 1 粒子の下界は、電子の届く範囲(箱)と関係する揺らぎの尺度(上限つきの h)に局在させないと、無関係な遠くの稀な配位が下界を壊す。**
- **R9**:閉じたのは方式。双極子では V が一様で静かな球の機構は空;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「電子を局在させない全空間の BO」「上限なしの $G_\theta$ の裾の評価」の発注。止めないもの:命題 496-T の形(IMS の箱 + 上限つきの M + Lifshitz の裾の型)とその連続版。
- **再開条件**:なし(言明は初等で、直した版が命題 496-T)。
- **成算**:S250。

## F311(E05、全列(行 E1-H)の計画 Ⅰ 段 2(J-C の裾 (i) の連続版):命題 496-T(E05-P261)の Hoeffding(点ごとの独立)を、連続の切断の場で Gauss の Lipschitz の集中(共分散の作用素ノルムの有界性)に置き換えて、指数 $s^3$ のまま連続の模型の裾を出す方式(稿 496 §3 の読み)。2026-10-21、w_E05_497 = 書き下しの型、稿 `497_全列_計画1_裾iの連続の模型_2026-10-21.md` §0・§1、C0 904、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。連続の模型の裾 (i) の真偽は閉じない。
- **理由(値 + 初等の勘定)**:IMS の箱は辺 $M\ell$・$M\to\infty$ が要り、箱の大部分は真空の領域。真空の横波の切断の場の乗数 $\frac1{2\lvert k\rvert}$ は赤外で有界でなく、辺 r の立方体に制限した共分散のノルムは 0.308〜1.268(r = 4〜12、冪 1.28;跡/体積 = $1/(4\pi^2)$ で検算)。真空の小箱で要る大きな偏差($\lvert A\rvert\lesssim\ell^{-1}$)の Lipschitz の指数は $\bar e s^3/(\alpha\ell^2\lVert\Sigma_B\rVert)$ で、$s=b\ell$ のとき ℓ に依らない定数 —— 和集合の評価が通らない。
- **共通点(1 行)**:**格子の玩具の点ごとの独立(Hoeffding)は、鋭い切断の帯域制限の場には無い(Paley–Wiener で有限の到達距離の分解も無い);連続版の裾には、赤外の長い相関に効く別の道具(小球の確率 + 低エネルギーの網、または Feynman–Kac)が要る。**
- **R9**:閉じたのは方式。双極子では V が一様で問題は空;擬交差の梯子に触れない。
- **射程(T60)**:禁じるのは「Lipschitz の集中を真空の小箱を含む IMS の箱の全体に当てて $s^3$ の指数を出す」発注。〔2026-10-21 監査 499 §4・confirm_A-499:止めないものに追加 —— 共分散を $\Sigma=\Sigma_1+\Sigma_2$、$\Sigma_2=\min(\Sigma,\frac1{2k_0})$ と独立に分け、低周波の $A_1$ で条件づけ、Anderson の不等式で条件つきの平均を下から押さえ、残り(作用素ノルム ≤ $\frac1{2k_0}$)にだけ Lipschitz の集中を当てる道(監査人の補題 A-499-2、盲検の独立確認で CONFIRMED;真空の小箱の指数は $k_0\bar eb^3\ell$ に比例して増える);残る段は支えの領域の条件づけの損 q(x) が η 未満であることと (U-MF)・(U-G)。〕止めないもの:小球の確率(Laplace 変換、凸・対称の事象)+ 低エネルギーの網の道(網の次元と小球の指数の競合が未解決);Pastur・Donsker–Varadhan の Feynman–Kac の型;平滑な切断(公理の外)での版。
- **再開条件**:(1) 作用素の正値性の破れを $L^2$ で小さい事象の多項式個の和集合に落とす段(V の高いモードの寄与を V の上限なしで押さえる)が立ったとき;(2) Gauss の確率的ポテンシャルの Lifshitz の裾の Feynman–Kac の評価を Ran Q・gap に相対的に書けたとき。
- **成算**:S250。


## F312(E05、難問 #1 の非退化 (iii-2)・#3 の上側の一様版の共通の入口 —— F182 の再開条件 (1)「$\Phi_c$ の非摂動の上界が λ の 1 次(閾値帯の重みの非摂動の抑制)」を、非摂動の値が線形に抑えられることを足場に追う方式。2026-10-21、w_E05_498 = 書き下しの型、稿 `498_難問1と3_Phicの値の回収_2026-10-21.md` §0・§3、ジョブ `g3_e05_490_phic`、C0 905、成算 S244・S246 の追記)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(値の向き)。命題「$\Phi_c\le C\lambda m$(族に一様)」の真偽は閉じない(値は λ≤128 の 3 点で、漸近の上界ではない【T88】)。
- **理由(値 + C0)**:(1) ジョブ 490(A1 の HMC の保存配位の後処理、α=1・T=6・$dt=1/\Lambda^2$、全 24 課題)で $\Phi_c$ = 1.581 ± 0.060・5.320 ± 0.099・17.42 ± 0.31(λ=32・64・128)、局所冪 1.751 ± 0.061・1.711 ± 0.037、$\Phi_c/\lambda$ = 0.049・0.083・0.136 と単調に増える —— 線形の抑制($p\approx1$)は $p-2\sigma\ge1.63$ で値に無く、σ を 2 倍にしても $p-4\sigma\ge1.50$。(2) C0 905:同じ λ の 1 ループ $\Phi_c^{(2)}$ = 2.407・7.505・22.63(NUM-6721 を λ=10・100 で再現)、局所冪 1.640・1.593 —— 非摂動は 1 ループの下(比 0.66→0.77)だが λ について 1 ループより速く増え、「閾値帯の重みが非摂動で抑えられる」向きの値は無い。(3) 推定量の刻みの対照(2 刻み・Richardson)で $p_{\rm hi}$ は 1.66〜1.75 —— 系統は冪を ±0.05 しか動かさず、線形との差 0.7 に桁で届かない。測度の刻みは未測(留保)。
- **共通点(1 行)**:**閾値帯 $\lvert k-q\rvert\lesssim\sqrt{2m\lvert k\rvert}$ の反跳の重みは非摂動でも 1 ループの形(冪 3/2 以上)で増え、族に一様な紫外の閾値帯の抑制(F182 (1)・F300 (3) の消費者の字面)は値の上に無い —— F182 (5) の 1 ループの読み($h\gtrsim\alpha^2\lambda_0^{3/2}$ が要る)は非摂動の値でも変わらない。**
- **R9**:双極子では $\Phi_c\equiv0$(反跳なし)で段は空;2 構造の擬交差の梯子では閾値帯の重みは固定の λ の量で、族の一様性の問いに触れない。障害は「非摂動の閾値帯の重みが λ とともに 1 ループの速さで増える」ことに局在し、消滅していない。
- **射程(T60)**:禁じるのは「$\Phi_c$ の非摂動の線形の抑制を足場に、族に沿う $\Phi\le Cm_{\rm ph}$ や (iii-2) を出す」形の発注。止めないもの:$\Phi_c$ の上界の冪を 2 から 3/2 側へ下げる試み(E05-P195 の改良、値は冪 2 を飽和しない);非摂動/1 ループの比の飽和の値(λ=256・測度の刻み・小さい α);F254 (1) の 3/2 の読み(本件で否定されない)。
- **再開条件**:(1) 測度の刻み $c_\delta\to0$ か λ=256 の値で、非摂動の局所冪が 1.25 以下に落ちたとき;(2) $\Phi_c$ の非摂動の上界が λ の 1 次で証明されたとき(F182 (1) そのもの —— 値の向きに反するので成算なし)。

## F313(E05、全列(行 E1-H)の計画 Ⅰ 段 2(J-C の裾 (i) の連続版):命題 504-R の経路空間の指数のモーメント $\sup_x\mathbb E^{\rm br}e^{-M_b+\frac12{\rm Tr}f(X_b)}\le e^{t\varepsilon}$ を、(a) 2 次の展開 + Khas'minskii、(b) $\min(a,b)$ の凸結合、(c) 作用素ノルムの飽和 $D_b\le\frac12{\rm Tr}X\lVert X\rVert/(2+\lVert X\rVert)$、(d) ブロック対角の支配で出す方式。2026-10-21、w_E05_504 = 書き下しの型、稿 `504_全列_計画1_裾iの経路の分割の大偏差_2026-10-21.md` §3、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**((a)〜(d))。経路空間の評価そのもの(連続の裾 (i))の真偽は閉じない —— 値(C0 912)は通る向き。
- **理由**:(a) 真空で Khas'minskii の定数が $\lambda\alpha^2I/(8\pi\eta)$ の桁(稿 500);(b) Khas'minskii に θ ~ 1/λ が要り、残る上限の利得 $(1-\eta)C\bar Et$ が正;(c) 長い経路では局所の長い滞在が a.s. どこかで起き $\lVert X_b\rVert=O(1)$ —— 支えの内側で要る比 η に届かない;(d) m 個の窓で m 倍の損。
- **共通点(1 行)**:**$\frac12{\rm Tr}f(X_b)$ は経路の自己重なりのスペクトルの関数で、飽和は大域の固有値で起きる —— 加法的汎関数の道具(Khas'minskii・占有測度の大偏差)にも大域のノルムの評価にも乗らない;要るのは滞在ごとに飽和した寄与を足す窓の分解と、窓の間の結合の補題。**
- **R9**:閉じたのは方式。双極子では $\Sigma_b$ は階数 3 で段は空;擬交差の梯子に触れない。
- **射程(T60)**:禁じるのは (a)〜(d) の形の発注。止めないもの:時間の窓ごとの局所の X と窓の間の Hilbert–Schmidt の結合の分解(稿 504 §5 の族 窓)。
- **再開条件**:窓の間の HS の結合を f の非線形のもとで制御する補題が立ったとき。
- **成算**:S250。

## F314(E05、全列(行 E1-H)の計画 Ⅰ の律速 (L2):稿 445 X1 の (α) の試行の τ を **LS の字面の類 $\tau=t(\ell P_f)$**(場の運動量の固定の関数、Lieb–Seiringer 2020 の $t(P_f/\alpha)$ の型)に取り、極限の対象(Φ57 + 準自由の場)の上で分数を 1 に行かせる方式。2026-10-21、w_E05_501 = 書き下しの型、稿 `501_全列_計画1_L2の類Cと補助の摂動つきのS2c_2026-10-21.md` §2、worklog (研究ノート: `2026-10-21_w_E05_501.md`) §1.1、C0 908a、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(τ を $P_f$ の関数に限る道)。(L2) の真偽・X1 の道は閉じない(雲の重心の類 $\tau=i\hat X$ では分数が恒等式 501-X で $\langle D_z\rangle^2/(\langle\lvert D\rvert^2\rangle+\langle C_f\rangle/\lambda)$ に落ち、細胞模型で 1 に行く値 —— 稿 501 §3・§4;極限の対象の上の欠損 → 0 は定理 509-L(E05-P268、率 $O(\ell^{-2}+(\lambda\ell)^{-1})$、監査 516)で解析的に —— (L2-a) は閉じ、(L2) の律速は (L2-b))。
- **理由(読み + 値)**:極限の対象の上で類 T の分数は静的なポテンシャル $W=\frac c{2u}$ の中の電子の試行 $2\lambda\lvert\langle t\varphi,p_z\varphi\rangle\rvert^2/\langle t\varphi,(h-\mu)t\varphi\rangle$ に落ち、TRK の上限 1 の達成は相対位置の掛け算 $z\varphi$ で $p$ の関数で書けない。固定の非多項式の $t$ は台の外へ漏れて障壁 $\sim\lambda\alpha$(極限の単位で $\Omega_0\to\infty$ 倍)で分母が発散し、多項式は自由境界の正則性($\partial^2u$ の跳び × $W\sim s^{-2}$)で 1 次だけが残る;線形の値 $\mathcal R_{\rm lin}=\frac43\lVert\nabla u\rVert^4/(c\int\lvert u'\rvert^2/u)=0.6075175088$(2 方式一致、調和の対照で 1)—— $f\ge0.39$ の上界しか出ない。
- **共通点(1 行)**:**Φ57 の自由境界(光子の泡の壁)が、正則な(連続・多項式増大の)運動量の関数による試行の稠密性を壊す —— Fröhlich の Pekar(台が全空間)と違い、電子の相対位置は場の配位(泡)を通してしか測れない。**
- **R9**:閉じたのは方式。双極子(ファイバー分解が無い)・擬交差の梯子(場の配位が無い)には触れない。
- **射程(T60)**:禁じるのは「極限の対象の上で、固定の $t$ による $t(\ell P_f)$ だけで (α) の分数を 1 にする」こと —— **t は連続で多項式増大(LS 2020 の型)に限る**(監査 506 §3:極を持つ $t=i\partial_{p_z}\hat u/\hat u$ は $t(p)u=zu$ を与え極限の対象の上で分数 1 に届くが、真の基底状態の上で $\lVert t(\ell P_f)\psi_\lambda\rVert=\infty$ で試行にならない;「特定の u で台を保つ連続の t は多項式だけ」は未証明の完全性の読み)。$A$ の汎関数を含む τ・λ ごとに選ぶ $t_\lambda$ は禁じない。0.6075 は固定の $t$ の族の上限の読みで、上界の証明ではない。
- **何が新しければ再挑戦可か**:Φ57 に代わる極限の対象の台が全空間(自由境界なし)になること(例えば次の補正 $\ell^{-1}$ の表面の汎関数で壁が柔らかくなる域の扱い)—— ただし固定の $t$ では漏れの費用 $\Omega_0$ が残るので、成算は低い。


## F316(E05、全列(行 E1-H)の計画 Ⅰ の律速 (L2) の類 C の判定を、**C0 の規模の相関のある Gauss 場の数値**(2 次元の格子のトーラス、窓つきの重心の欠損の梯子 $r_b$=3〜7)で行う方式。2026-10-21、audit_S2_501 = 監査の型、監査稿 `506_独立監査_L2の類Cと補題501X_2026-10-21.md` §2、worklog (研究ノート: `2026-10-21_audit_S2_501.md`) §5・§6、C0 915・915c)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(C0 の規模の相関のある模型の梯子で極限を判定する方式)。(L2) の真偽は閉じない —— 類の判定は監査人の補題 A-506-1・A-506-2(解析)に移した。
- **理由**:監査人が実行前に固定した判定文 J1(最後の 3 段の傾き ≤ −1)は字面 FAIL(欠損 0.998〜1.000)。原因は前漸近:分母 $\mathcal D=\int wG$ の S/N は全段で 1.1〜2.2(Wick の厳密な分散、C0 915c)、2 次元では SNR ∝ $r_b^{\approx0.75}$ で、極限の判定に要る SNR ≳ 10 は $r_b\sim60$(格子点 $\sim2\times10^5$、密な共分散の C0 の外)。908c の 3 次元の細胞模型でも 欠損 ≈ 4.6/SNR² で、K3 の閾 0.05 は SNR ≈ 10 を要した —— 稿 501 の K3 と同じ型の設計の誤り(梯子を S/N で事前に確かめない)。
- **共通点(1 行)**:**窓つきの重心の欠損は分母の S/N だけで決まる(A-506-1)ので、有限の梯子の閾は S/N の設計値の検査になり、極限の問いに答えない。**
- **R9**:閉じたのは方式。双極子・擬交差の梯子には触れない。
- **何が新しければ再挑戦可か**:判定文の条項を「欠損 × SNR² の安定」(A-506-1 の予言)で書き、起動前に各段の S/N を Wick の分散で確かめる;相関のある 3 次元の模型は定数の質量の泡で FFT の対角化(C1 の規模)—— ただし A-506-2 の独立確認が通れば数値は要らない。


## F318(E05、全列(行 E1-H)の計画 Ⅰ の律速 S2-c:Bach–Hach 2020 の LL の模型の下界の鎖(Weyl 変換 BH1・与えた φ の場の厳密な最小 BH2・X の凹性による局在 BH3)を、積の状態の汎関数の形のまま真の模型の下界に字面で運ぶ方式。2026-10-21、w_E05_510 = 書き下しの型、稿 `510_全列_計画1_S2cの偵察_BachHachの運搬_2026-10-21.md` §1・§2、worklog (研究ノート: `2026-10-21_w_E05_510.md`)、C0 919a〜919c、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(字面の運搬)。S2-c の真偽・BH の機構の真の模型版(配位表示の断熱の下界 + ゲージの射影 + IMS + Lemma VII.1 の Θ' 版 510-R)は閉じない —— 段ごとには運べる(稿 510 §2)。
- **理由(原典の字面 + 初等)**:BH1・BH2 は「与えた電子の状態 φ の上で場だけを最小化する」積の状態の命題で、BH3 は $A\mapsto X(A)$ の凹性を電子の輪郭の混合に使う。真の模型では電子の密度が場の配位ごとに動け(相関)、凹性の向きは $\mathbb E_q\inf_\rho\le\inf_\rho\mathbb E_q$ —— 下界には逆の向き。
- **共通点(1 行)**:**積の状態の下界の鎖は、相関が下げうる分(配位ごとの inf と場の量子の期待値の交換)を一度も測らない —— 真の模型の下界は断熱の下界を経て、その交換(J-G・(U-G))に全ての難しさを集める。**
- **R9**:閉じたのは方式。双極子では断熱の下界が空(ゲージ);擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「BH の Thm IV.4・IV.5・V.1 を真の模型の状態に字面で当てる」発注。止めないもの:配位表示の断熱の下界での段ごとの運搬(稿 510 §2 の表)、J-C・J-G の族。
- **再開条件**:なし(言明は原典の字面と初等の向きの議論)。

## F319(E05、全列(行 E1-H)の計画 Ⅰ の (L2-a) の縁の評価 (H3) を、**障壁の高さに一様な比較(Dirichlet の障害物の極限)**で行う方式。2026-10-21、w_E05_509 = 書き下しの型、稿 `509_全列_計画1_L2aの窓つきの重心の欠損_2026-10-21.md` §4 の観察 509-F、worklog (研究ノート: `2026-10-21_w_E05_509.md`) §0・§1.4)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(高さ一様の障害物の比較)。(H3) そのものは閉じない —— 補題 509-3 が高さを陽に使う変分の試行で示した(self-audited)。
- **理由**:切断 $\lvert k\rvert\le1$ の帯域制限の一粒子空間 $\mathfrak h$ では、$\bar B$ の上で 0 になる元は 0 だけ(Paley–Wiener:整関数の制限)。ゆえに ℓ を固定して高さ $V_0\to\infty$ とすると、増加する閉形式の単調収束で各 t の $(\omega^2+V_0P\mathbf 1_{\bar B}P+t^2)^{-1}\to0$(強)、共分散 $\bar C\to0$、縁の $`\varepsilon(y)\to\mathrm{tr}\,\Sigma_0`$ —— 高さに一様な $\varepsilon\to0$ は偽。付随して閉じた 2 つの小さな方式:(i) 試行 $P^\perp(\eta u)$(縦の成分 $\nabla\Delta^{-1}(\nabla\eta\cdot u)$ が泡の上で $O(\ell^{-1})$ 残り、$V_0\sim\alpha^2\ell^4$ 倍で発散 —— curl の形に替えた);(ii) 共分散の差を障壁について線形化する評価($R_0-R_V\le R_0WR_0$、低い周波数の成分が泡に届き $V_0$ 倍で発散)。
- **共通点(1 行)**:**帯域制限の場は泡の上で消せないので、強い障壁の効果は飽和せず、評価は障壁の高さ(多項式)と試行の漏れ(超多項式)の兼ね合いでしか取れない。**
- **R9**:閉じたのは方式。双極子・擬交差の梯子には触れない。
- **何が新しければ再挑戦可か**:不要(補題 509-3 で (H3) は高さを陽に使って閉じた);高さが ℓ の指数で増える模型では 509-3 の論法も使えない —— Gevrey 級(位数 σ>1)のコンパクト台の η で漏れは $e^{-c\ell^{1/\sigma}}$ まで強まり、高さ $e^{c\ell^a}$($a\lt1/\sigma$)には届くが、真の指数 $e^{c\ell}$ にはコンパクト台の η では届かない(指数の Fourier の減衰はコンパクト台と両立しない —— Paley–Wiener;監査 516 §2.5)。

## F320(E05、全列(行 E1-H)の計画 Ⅰ の S2-c の全模型の類 B (G2)(G3):位相の渦と磁気の裾を、curl の技法(補題 515-V:$\lVert(\nabla+ib)\phi\rVert^2\ge\int(1-2\lvert C\rvert)\lvert\nabla\phi\rvert^2+\int\lvert b\rvert^2\lvert\phi\rvert^2$、$C={\rm curl}^{-1}b$)の点ごと・sup のノルムの評価で処理して、断熱の下界を定数の水準で o(1) の損失に収める方式。2026-10-21、w_E05_515 = 書き下しの型、稿 `515_全列_計画1_S2cの全模型の類B_2026-10-21.md` §2・§3、C0 925b、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。渦・磁気の裾の真偽(極分解の道)は閉じない。
- **理由(閉じた形 + 値)**:(G2) 泡の中の欠損 $2\sqrt\alpha(\mathbb E\lvert C\rvert^2)^{1/2}$ は、泡の尺度より長い波長($1/(M\ell)\le k\le1/\ell$)のモードが泡の中で抑えられないので $2\sqrt\alpha\sqrt{\log M}/\pi$(α=1/137、M=10 で 0.083)に止まる(ℓ=16〜128 で 0.0925→0.0827、冪 −0.05)。(G3) 係数の正には $2\sqrt\alpha\sup_{(M\ell)^3}\lvert C\rvert\lt1$ が要り、真空の Gauss の和集合の上界は ℓ ≥ 32 で 1(自明);α=10⁻⁴ の対照では ≤10⁻²⁷⁸。
- **共通点(1 行)**:**curl の逆は長い波長に $\lvert k\rvert^{-1}$ の重みを置くので、点ごと・sup の評価はゲージで消える長い波長の部分を罰として払い、√α·√log の定数と箱の大きさの log の育ちが残る。**
- **R9**:閉じたのは方式。双極子では C を定数に選べ自明;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「curl の技法を点ごと・箱の sup で全模型の断熱の下界に当てて定数の水準の o(1) を出す」発注。止めないもの:極分解の下界(510 §2・515-G1)での渦の寄与の評価(稿 485 の 485-V の再利用)、長い波長をゲージで除いた後の高い帯域だけへの 515-V。
- **再開条件**:渦の寄与を極分解の下界で押さえる道具(485-V 型の立方体の磁気の不等式)が入ったとき。

## F321(E05、全列(行 E1-H)の計画 Ⅰ の (L2-b):監査 506 の補助の摂動の族 $B\in\lbrace D_z,\lvert D\rvert^2,C_f/\lambda\rbrace$(場の配位だけの汎関数)を、Griffiths の道(A-491-2 の凹性の挟み)で S2-c の補助の摂動として使い、真の基底状態の ⟨B⟩ を極限の値に決める方式。**読みによる閉鎖 —— 監査の型 の確認が要る**。2026-10-21、w_E05_515 = 書き下しの型、稿 `515_` §4、C0 925c(札 BOUNDED —— 細胞模型の較正の外れ)、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(場だけの B での Griffiths の道;読み)。(L2-b) の直接の道(状態の水準の集中)と、偽の欠損が F の桁を払う B の設計は閉じない。
- **理由(読み + 値)**:窓の縁の電子の無いモードをスクイーズする偽の欠損で $D_z$ を O(1) 動かせ、費用 ∝ モード数 ∝ ℓ³ ≪ F ∝ αℓ⁵(比 $\sim1/\Omega_0$);試行 $E(s)\le E(0)+sF(\langle B\rangle_0+\Delta B)+E_{\rm fake}$ で、尺度を外した $e(s)$ は $s_*\sim\lambda^{-2/7}\alpha^{-5/7}$ で折れ、挟みには $s\gg\varepsilon_{\rm up}\sim\lambda^{-4/105}$ が要る —— 両立しない。値:同じ細胞模型の中の $E_{\rm fake}/E_{\rm bubble}$ = 0.099・0.042・0.020(ℓ=32・48・64、冪 ≈ −2.2);$E_{\rm fake}/F$ は冪 −1.38 だが、対照(泡の場のエネルギー/F)が 0.014 以下で模型の絶対の尺度が F に較正されていない(札 BOUNDED)。
- **共通点(1 行)**:**場だけの観測量は場だけの安い変形(電子に触れないスクイーズ)で動く —— 費用がモード数(体積)でしか効かず、F の $\Omega_0$ 倍の桁に届かない。**
- **R9**:双極子では泡が無く B は定義されない;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「電子の枠の場だけの汎関数を、窓の縁が真空の域にある形のまま Griffiths の補助の摂動にする」発注。止めないもの:縁が泡の内側(反スクイーズが電子のポテンシャルに逆らい費用 ∼F)の B の設計、直接の道。
- **再開条件**:偽の欠損の費用が $\gtrsim cF\lvert\Delta B\rvert$ になる B、または F に較正した模型で $E_{\rm fake}/F$ が ℓ で減らないこと。


## F322(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G:平均場の最適の Gauss の状態 $G_{\rm MF}$ の周りの基底状態の変換で $\inf\sigma_\mu(L-U')$ を、$G_{\rm MF}$ の Gauss の対数ソボレフ不等式(大域の定数)と Gibbs の変分(1 つの t)で $-\frac1t\log\mathbb E_\mu e^{tU'}$ と押さえる方式(Federbush 型)。2026-10-21、w_E05_514 = 書き下しの型、稿 `514_全列_計画1_JGの設計と類C_2026-10-21.md` §0・§2、worklog (研究ノート: `2026-10-21_w_E05_514.md`)、C0 924a、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**。J-G の真偽、場の配位の空間の切り落とし + サイトごとの不等式の版(稿 514 §5 候補 3)は閉じない。
- **理由(初等 + 値)**:補題 514-F —— $E_{\rm el}$ の凹性の支える超平面で $U'$ は 1 点の $\lvert q_x\rvert^2$ に沿って傾き $c(\bar\rho-\rho_0)(x)\to c\bar\rho(x)$(満額、電子がその点を避ける)で下から押さえられ、LSI が許す $t\ge2/\Omega_{\min}$ では $\mathbb E_\mu e^{tU'}=\infty$($\Omega_x^2-1\ge\Omega_x$ の点があれば;質量 0 の連続では常に)。C0 924a:$\kappa_F$ = 22.5・45.8・91.0(λ = 1e5・1e6・1e7、閾 1)、小結合の対照 0.111、穴の深さ 0.9996。
- **共通点(1 行)**:**配位ごとの適応の利得 U′ を、場のモードに一様な 1 つの定数(LSI の t・Temple の θ・凹性の向き)で払う方式は、サイトごとの利得の満額の傾き(hot spot)で限界に落ちる —— 払いはモードごとの障壁(電子の穴の費用 $a_x\sim\lambda\bar\rho\gg\Omega_x$)でなされなければならない。**(同じ機構で、場の空間の 495-J(Temple–Feshbach)は θ ≤ Ω_max^{-2}(補題 514-T)に落ち、2 次の項は相対 O(α²) の定数 —— 札は BOUNDED で、本件には含めない。)
- **R9**:閉じたのは方式。双極子では $U'\equiv0$ で hot spot は無い(電子が避ける場所が無い);擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「$G_{\rm MF}$ の大域の LSI 定数と 1 つの t の Gibbs の変分で J-G を出す」発注。止めないもの:U′ の切り落とし + サイト(塊)ごとの t・θ の版、Feynman–Kac の窓、状態の水準の 495-J 型。
- **再開条件**:なし(言明は初等;直した版は候補 3)。
- **成算**:S254。


## F323(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G:場の配位の空間で点ごとに $\lvert q_x\rvert^2$ の閾 s で IMS し、切り落としの内側で Temple(場の空間の 495-J)の θ が λ に依らない O(1) になる(1 点の穴の費用が利得の傾きを抑える)ことに頼る方式。2026-10-21、w_E05_519 = 書き下しの型、稿 `519_全列_計画1_JGの場の空間の496T型_2026-10-21.md` §0・§2、worklog (研究ノート: `2026-10-21_w_E05_519.md`)、C0 929a・929b、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(仮説「1 点の切り落としで内側の θ = O(1)」)。J-G の真偽、θ → 0 でも 2 次の項 Y/θ が o(1) になる道、Gauss の多様体の集団座標の局在の道は閉じない(判定文は θ で書かれ、証明が使う Y/θ を測っていない —— 稿 519 §0 の注)。
- **再判定(2026-10-21、記録 `519a_判定_JGのYtheta_2026-10-21.md`、judge_JG_Ytheta = 監査の型、結果を見ていない体の判定文)**:証明が消費する量 $Y/(\theta_*E_{\rm MF})$ で **JGY_BOUNDED**(λ=1e8 で $[8.2\times10^{-4},0.225]$;必要側の冪 −1.75 で Temple の型は閉じない、Poincaré の端 +0.31 で o(1) は値で支えられない)。補題 519a-ES(self-audited)で $Y/E_{\rm MF}\lesssim\ell^{-2.64}$ —— 未決は内側の θ* の作用素の下界 1 つ($\theta_*\gg\ell^{-2.64}$ で足りる)。本閉鎖((H-loc) の方式)の範囲は変わらない。
- **理由(初等 + 値)**:補題 519-C(U′ の凸性 + 殻の試行)で θ はパターン P ごとの値で上から押さえられ、1 点(θ^val = 0.57)では穴の費用が効くが、半分の泡のパターンでは電子が穴を開けずに**移動**して利得の比が 1 に近づく:θ_min(傾きの形)= 0.0215・0.0085・0.0028(λ = 1e5・1e6・1e7、冪 −3.1)、値の形 0.077・0.045・0.025(冪 −1.68);対照(一様なパターン θ = 1、1 点の 924c の再現)は通る。
- **共通点(1 行)**:**利得 U′ を G_MF の OU に相対な定数で払う方式は、1 点では穴の費用で救えても、集団の方向(電子の移動 = 別の Gauss の状態 $G_{\rho'}$ への変形)では救えない —— その方向は L でなく MF の汎関数で測るべき;稿 514 の命題 514-R で消した (U-G) はここに戻る。**
- **R9**:閉じたのは方式。双極子では U′ ≡ 0 で集団の方向も空;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「点ごとの場の配位の切り落とし + G_MF に相対な一様な θ の Temple」で J-G を出す発注。止めないもの:外側の補題 519-O・命題 519-I(帰着)、Gauss の多様体の集団座標の局在 + 横の方向の Temple、Y/θ の判定の立て直し。
- **再開条件**:内側の Temple の θ の作用素の下界(集団の方向を除いた空間で)を与える道具が入ったとき。
- **成算**:S254。

## F324(2026-10-21、w_E05_521 = 書き下しの型、稿 `521_全列_計画1_UMFの連続版_2026-10-21.md` §5.4)無制約の平均場の最小化子の (U3)(中心が箱の境界から $\gg\log\ell$)を、内側への平行移動の比較で出す方式 —— **閉じたもの:方式**

親(G3 第 73 陣)が連結 2026-10-21
- 中身:Φ57 の最小化子の台はコンパクトなので、極限の対象は箱の中の位置について縮退する(半空間の Dirichlet の下限は距離 $\ge R_0$ で $e_\infty$ に等しい)。最小化子を切断して箱の中心へ平行移動した試行は $\mathcal E$ を超指数的に小さい量しか変えず、等号の側にしか効かない —— 中心の位置の下界を出さない。位置は指数的に小さいエネルギーの差で決まり、有限の ℓ の平均場の最小化子の一意性・非退化性(Φ57 は $L^1$ の項で滑らかでなく、陰関数定理の形にならない)が要る。
- 止めないもの:箱の鏡映で対称な最小化子では対称性で中心が固定され (U3) は成る(命題 521-T);消費者が対称な対を使えれば本方式は不要。
- 注(読み):準最小の全ての Gauss の G((U-G))では、壁の近くに中心がある配位が窓の中に入り、(U3) の形は一様に成らない見込み —— J-G の族で 505-Q の場合 I の壁の近くの版が要る。
- 再開条件:有限の ℓ の(無制約の)平均場の最小化子の、平行移動を除く一意性と量的な安定性(指数の精度)。

## F325(E05、全列(行 E1-H)の計画 Ⅰ の S2-c の全模型の類 B (G3)(i):局所のゲージの射影の損失 $\eta_{\rm loc}-\eta_{\rm glob}=O(1/s)$ を、**鋭い立方体**ごとの 515-G1 の恒等式に Neumann の境界項 $\int_{\partial Q}\rho (n\times C_A)\cdot\nabla_\tau\bar\chi$(または $\int_{\partial Q}(\chi-c)\rho n\cdot A$)をつけて評価する方式。2026-10-21、w_E05_522 = 書き下しの型、稿 `522_全列_計画1_S2cの渦と局所の射影の書き下し_2026-10-21.md` §1(読み)・worklog (研究ノート: `2026-10-21_w_E05_522.md`) §1.5、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたのは方式**:境界項は $\chi\in H^1(Q)$ の接線の微分(または跡)を含み、$\lVert\varphi\nabla\chi\rVert_{L^2(Q)}$ で押さえるには $H^{1/2}$–$H^{-1/2}$ の双対と ρ の立方体の上の比較可能性(Harnack)が要る —— 一般の $\varphi\ge0$(BH の鎖の $\inf_\rho$ の変数)では成らず、跡ノルム(510-R が消費する形)にも乗らない。単純な跡の評価 $\lVert\chi-\bar\chi\rVert^2_{L^2(\partial Q)}\le Cs\lVert\nabla\chi\rVert^2$ では相対の損失が O(1)(帯域の振動を使えない)。
- **置き換え**:滑らかな分割 $\sum j_k^2=1$ で重み $j_k^2\rho$ を台の縁で 0 にし、境界項そのものを無くす(補題 522-G、E05-P? —— 損失は $\frac{C_j}s\lVert\varphi\rVert_{2;1}$)。
- **再開条件**:なし(置き換えで標的は閉じた)。

## F326(E05、同じ行の (G3)(ii):立方体ごとの磁気の Neumann の基底値の床を、Temple の第 2 固有値の下界 $E_1\ge(1-\delta)\pi^2/s'^2-\delta^{-1}\lVert a'_Q\rVert_\infty^2$ と $\lVert a'_Q\rVert_\infty\lesssim s'\lVert b\rVert_\infty$(485-W〔E05-P260〕を辺 $s'$ に移して Morrey)で出す方式。2026-10-21、w_E05_522 = 書き下しの型、稿 522 §3 の補題 522-T の注、成算 S250)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたのは方式**:$\lVert a'_Q\rVert_\infty\lesssim s'\lVert b\rVert_\infty$ は定数の b で鋭く、帯域制限の場でも Morrey の評価からは改善しない —— 条件 $s'^4\alpha\lVert b\rVert^2_\infty\ll1$ で $s'\ll\ell^{1/2}$ に縮み、下側の裾の指数 $\sim s'^3/(\alpha\ell^2)\to0$ で和集合が自明になる。
- **置き換え**:$L^3$・$L^4$ のノルムによる第 2 固有値の下界と分散(補題 522-T)—— 条件 $s'\ll\ell$、指数 $\sim s'^3/\ell^2\to\infty$($2/3\lt\gamma'\lt1$)。
- **再開条件**:なし。


## F327(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G:G_MF の 1 点を基準に、場の空間の 495-J 型の Temple で $\inf\sigma(L-\delta U')\ge-Y/(\kappa\theta^*)$ とし、θ* の作用素の下界(θ* ≫ ℓ^{-2.64}、記録 519a)で J-G を出す方式。2026-10-21、w_E05_527 = 書き下しの型、稿 `527_全列_計画1_JGの集団座標の局在とθstarの下界_2026-10-21.md` §2、worklog (研究ノート: `2026-10-21_w_E05_527.md`)、C0 938a・938b・938c、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(G_MF の上の Temple を全ての方向で 1 つの θ* で払うこと)。J-G の真偽は閉じない —— 並進の方向は Temple の商の分子が 0 で、J-G には害が無い(補題 527-Q)。
- **理由(初等 + 値)**:補題 527-T —— 並進不変な玩具(周期の箱)で $\theta^*\le2m_d\sqrt{\mathrm{Var}_\mu U'}/\mathrm{cost}_d$、$\log m_d=-43\sim-4459$(λ = 1e5〜1e8、d = 1〜3);稿 514 の Dirichlet の箱では値で θ_d = 5e-7〜4e-6(箱の欠損)、要求 5.8e-3(λ=1e8・ε=0.05・κ=1/2)の 1/1000 以下。並進を除いても、有限振幅の偶の移動・圧縮(外殻→芯)で G_MF の L に相対の θ は θ_up と同じ冪 −1.60(C0 938a、札 JT_BOUNDED)。
- **共通点(1 行)**:**G_MF の OU(L)を分母に置く限り、MF の余剰が 0(並進)か E_MF の桁(移動・圧縮)の方向で商が小さくなり、Temple の $Y/\theta$ が発散する —— 集団の方向は θ で割らず、(527-3) の $\mathcal M(\psi)-\mathrm{MF}_{\min}$ で直接払う。**
- **R9**:閉じたのは方式。双極子では泡が無く $\mathrm{cost}_d=0$ で 527-T は空(標的は自明に真);擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「G_MF(または 1 つの固定の Gauss の状態)の上の全空間の Temple の θ* の下界」で J-G を出す発注。止めないもの:並進を止めた片の上の横の Temple、(527-3) の直接の評価(Jensen の隙間を MF の余剰で払う)、Frank–Seiringer 型の多様体の近く/遠くの分割。
- **再開条件**:なし(並進の対称性による;箱の玩具では箱の欠損の桁を超えない)。519-I の切り落とし s = 3 の内側に限った版は値の上で閉じる向き(厳密な誤差の評価は稿 527 §2 で非主張)。
- **成算**:S254。

## F328(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の連続版:ブロックの Hardy の連続の比較の段で、ブロックの中の点の最小 $`m_Q=\mathop{\mathrm{ess\,inf}}_Q\rho`$(または Slepian の固有ベクトルをそのまま部分空間に取る・全空間の多重のベクトル場で Hardy を当てる)を使う方式。2026-10-21、w_E05_532 = 書き下しの型、稿 `532_全列_計画1_JGのブロックのHardy_2026-10-21.md` §2.5)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(3 つの組み立て)。J-G の連続版の真偽と、ブロックの Hardy の道そのもの(命題 532-B は成る)は閉じない。
- **理由(初等)**:(i) 連続の 3 次元では点の容量が 0 —— 電子は各ブロックに半径 r → 0 の窪みを費用 O(r) で掘れ、$m_Q=0$ にでき下界が空;(ii) Slepian の固有ベクトル(固有値 ≥ 1 − δ)はブロックどうしで直交でなく(内積 $\le2\sqrt\delta$)、補題 532-C を同時に当てられない;(iii) $\sum_QV_Q$ の 1 つの場で Hardy を当てると交差項 $V_Q\cdot V_{Q'}$ が隣のブロックの数の定数倍を失い、主項の定数が崩れる。
- **共通点(1 行)**:**格子では自明な「ブロックの座標が直交」と「点の値が最小を決める」の 2 つが、帯域制限の連続の場では同時に成らない —— 最小は分解能 1/Λ で取り、部分空間は直交化した局在の枠で取る必要がある((BH-c1)(BH-c2))。**
- **R9**:閉じたのは方式。双極子では Π が階数 3 でブロックは 1 つ、問題が起きない(標的は自明に真);擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは上の 3 つの組み立てで連続の比較の段を書く発注。止めないもの:分解能 1/Λ の最小 $\tilde m_Q$ と直交化した局在の枠での比較((BH-cont))、格子の切断族での定理 532-L の使用。
- **再開条件**:(BH-c1) の直交で局在した枠が構成され、かつ F330 の再開条件(外の場の調和の費用を残す局所性)が満たされたとき((ii)・(iii) は不要になる)。枠だけでは足りない —— 535-D の崩壊は枠と独立(監査 534 §5)。
- **成算**:S254。


## F330(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の連続版:ブロックの Hardy(稿 532 の命題 532-B・(BH-cont))—— 場の零点を Hardy で配位の関数に移し、箱の外のモードを振動子の零点に落としたうえで、φ と全ての場の座標 q の古典の inf を取る方式(m̃_Q の版、k*ρ の滑らかな最小の版、外の座標を結合から切り離す版、全空間をブロックで覆う版を含む)。2026-10-21、w_E05_535 = 書き下しの型、稿 `535_全列_計画1_JGのブロックのHardyの連続版_2026-10-21.md` §1・§2、worklog (研究ノート: `2026-10-21_w_E05_535.md`) §1.2)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(連続の場でのブロックの Hardy の古典の inf)。J-G の連続版の真偽は閉じない —— 崩れるのは下界の道具で、真の $H_{\rm BO}$ は遠方の巨大な振幅に調和の費用を払う。格子の定理 532-T・532-L は影響なし。
- **理由(初等、補題 535-D)**:帯域制限の場(スカラー・3 成分・横波)の有界な箱への制限は稠密(横波は curl の場を含む)—— Paley–Wiener。各ブロックに正の測度の窪み(費用は容量 → 0)を持つ φ に、箱の中では窪みに集まり外では巨大な場を当てると、Hardy の項 $a_Q/u_Q\to0$ と結合 $c\int\rho\lvert A\rvert^2\to0$ が同時に起き、下界は $\inf_\varphi T$(MF_min の $O(M^{-2})$ 倍)に崩れる。救済 3 本も閉じる:負の 2 次形式の残り(sinc の裾 1/d 対 $c\rho\sim\alpha^2\ell_*^4\gg\Lambda^2$;安定にする大きい余白では余白のモードの真空の損が主項を超える)、真空の引き算の体積の不一致、ブロックあたり O(Λ) の Hardy の損 × 無限個。
- **共通点(1 行)**:**連続の場の箱への制限は稠密なので、外の場の座標を自由にした古典の inf は場を窪みに集めて Hardy と結合を同時に 0 にできる —— 外の場の調和の費用を古典の側に残せない限り、零点を Hardy で配位の関数に移す方式は連続では閉じる。**
- **R9**:閉じたのは方式。双極子(場は A(0) の 3 成分)では稠密性が無く崩れない(標的は自明に真);擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「連続の場で、外のモードの座標を自由にした古典の inf + ブロックの Hardy」で J-G を出す発注。止めないもの:格子の切断族での 532-L の使用、格子から連続への比較、外の場の調和の費用(Schur の補元)を残す量子の版、稿 530 の予備 B。
- **再開条件**:外のモードの条件つきの最小の調和の費用 $\frac12q_{\rm in}\cdot\Sigma q_{\rm in}$ を古典の作用に残し、かつ結合が $q_{\rm in}$ だけで下から押さえられる局所性(Σ と sinc の裾の評価)が示されたとき。
- **訂正**:稿 532 §2.5 の「$\tilde m_Q$ は実質は分解能 1/Λ の最小」は誤り —— 稠密性で $`\mathop{\mathrm{ess\,inf}}_Q\rho`$ に一致する。
- **成算**:S254。

## F331(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の連続版:字面の (β) —— 補題 532-V の Schur の補元 $\frac12q_{\rm in}\cdot\Sigma q_{\rm in}$ だけを古典の作用に残し、外のモードの座標は自由のままブロックの Hardy の古典の inf を取る方式。2026-10-21、w_E05_537 = 書き下しの型、稿 `537_全列_計画1_JGのSchur補元の量子版_2026-10-21.md` §1、worklog (研究ノート: `2026-10-21_w_E05_537.md`) §0.1)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(Σ だけを残す (β))。重みつきの版 (β′)(可積分な θ の勾配の費用を残す)は閉じない(稿 537 §1・§2)。
- **理由(初等、所見 537-Q)**:箱の中の格子点の座標を 0 にすると Σ の項は 0;外の sinc の張る空間の箱への制限は稠密(標本化定理 + Paley–Wiener)—— 535-D の崩壊の配位がそのまま作れる。Σ の局所性(C0 947a C1:冪 −2.00)には依らない。
- **共通点(1 行)**:**崩壊を止めるには箱の中の座標の費用ではなく、外の座標が箱の中に作る場の形の費用(全空間で正の重みの勾配)が要る —— 外の座標を自由にしたまま中の座標にだけ費用を置く方式は、535-D の稠密性で崩れる。**
- **R9**:閉じたのは方式。双極子では稠密性が無い;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「Σ だけを残した古典の inf」の発注。止めないもの:(β′)、(SL′) の評価、格子の 532-L。
- **再開条件**:なし(稠密性による)。
- **成算**:S254。


## F332(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の連続版:命題 537-R(稿 537 §2 (c))の窪みの吸収を「隣のブロックの min $\mu_Q=\min_{Q'\sim Q}\bar m_{Q'}$」と補題 537-LC($\sup_Q\lvert B\rvert^2\le K_3\int_{Q^+}\lvert B\rvert^2+\cdots$)で行う組み立て —— **方式の穴**(w_E05_539 = 書き下しの型、2026-10-21、稿 `539_全列_計画1_JGのSLprimeとSlepianの跡_2026-10-21.md` §3.1・§4 R9)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:方式(J-G の主項の真偽ではない —— 定理 539-R が別の組み立てで成る)。
- **理由(初等)**:537-LC の局所の項 $\int_{Q^+}\lvert B\rvert^2$ は隣のブロックの場 $u_{Q'}$ を含み、その吸収には $\sum_{Q\sim Q'}\mu_Q\lesssim\mu_{Q'}/(\varepsilon_HK_3)$ が要るが、$\mu_Q\le\bar m_{Q'}$ からは $\mu_{Q'}$(Q′ の別の隣の min)と比べられない —— 低密度のブロック(泡の縁)の 2 つ隣で $u_{Q'}$ の係数が負になり、u の inf が −∞。電子の箱の壁の隣では $Q^+$ が箱の外(結合なし)を含む。
- **置き換え**:補題 539-H(窪みの点の場を、同じブロックの窪みでない部分の平均と再生核による勾配の上限で押さえる;隣の項なし)と、ブロックごとの窪みの予算 $\varepsilon_Q\propto1/(c\bar m_Q)$。
- **射程(T60)**:禁じるのは「隣の min・537-LC の $\int_{Q^+}$」で窪みを吸収する組み立ての発注。止めないもの:539-H の組み立て、537-V・537-Q。


## F333(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の全模型版 (JG-2):系 522-A の字面の $R_Z$(類 (i) の $\frac{11}D\int\rho_0\alpha\tilde A^2$ を含む)の期待値を o(F) にする方式 —— **方式の閉鎖**(w_E05_541 = 書き下しの型、2026-10-21、稿 `541_全列_計画1_JGの全模型版の付加項_2026-10-21.md` §0・§1.3 候補 2、worklog (研究ノート: `2026-10-21_w_E05_541.md`) §0.1・§2)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:方式(標的・命題の真偽ではない)。
- **理由**:C0 951a(起動前に固定した K1b、522 の 3 次元の玩具、α = 0.1・ℓ = 6・9・12):$r_1=\alpha\int\rho_0\tilde A^2/e$ は 0.269 → 0.553(比 2.05 > 1.5)、$T=\frac{11}{D}r_1+r_Z$($D=(\log\ell)^2$)は 0.923 → 0.986 —— 損の上界が e の桁で、育つ向き。第 1 項は零点が無くても残る緩め(sup の膨らみ $r_1/r_{\rm plain}\approx8\sim10$)。零点そのものは物理の α でも α = 0.1 でも 0(K1a PASS)。Feynman–Hellmann で $R_Z$ を 2 次形式で押さえる道(稿 532 §3 の読み)は sup を $L^2$ に落とす段で $s^3$ を失う(稿 541 §1.3)。
- **置き換え**:補題 541-Z♯(緩めなしの $R_Z^\sharp$、零点の無い配位で 0);さらに命題 541-M(n 倍の位相 + Neumann のブロック)で $R_Z$ の消費そのものが不要 —— 残りは名指し (JG-F)(字面は偽 —— F334;置き換え (JG-F‴\*)、監査 543)。
- **射程**:窓 ℓ ≤ 12、α = 0.1 は抑制の域の代理(物理の α ではない)。522-A の不等式(配位ごと、E05-P275)は正しいまま。
- **再開条件**:なし(置き換えで標的の道が変わった)。


## F334(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の全模型版:稿 541 §4.1 の名指し (JG-F)(1 立方体の Neumann の磁気の基底値の配位ごとの床 $E_0^N(Q;n\sqrt\alpha B_q)\ge n^2(1-\eta)\alpha\min\lbrace u'_Q,u_b\rbrace/\lvert Q\rvert$、全ての q)—— **命題の偽**(w_E05_542 = 書き下しの型、2026-10-21、稿 `542_全列_計画1_JGFの磁気の床_2026-10-21.md` §1・§2、worklog (研究ノート: `2026-10-21_w_E05_542.md`) §0〜§2)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:命題の真偽(字面の (JG-F) は偽)。定理 541-G は仮定が偽の帰着になる;541-n・541-M・541-D・541-C′ は正しいまま。
- **理由**:命題 542-X(帯域制限の場の Q への射影の稠密性 542-D で Q の中の小さな球に集まる場を作り、電子は容量 ~r の費用で避ける —— n・η・$u_b$ によらない)。C0 952a(起動前に固定した C1・C2):s = 10・L = 16・24 の格子で、集まった場(r = 1)は Y = 0.01〜0.04 で R = 0.80〜0.38、同じ Y の白い場は R ≥ 0.989;反例の Ω = 299〜16563。
- **射程**:$u'_Q$(Q の中の情報)だけの関数の 1 立方体の床は立たない;Q を含む有界な台の窓の局所のエネルギーで条件づけた床も立たない(監査 543 の A-543-2、F302 と同じ機構)。消費者の周期の箱の模型でも L が大きければ偽(A-543-1)。539 §3.1 の多項式の裾の窓で勾配のエネルギーで条件づけた形 (JG-F‴\*)(監査 543 §2)は閉じていない(C0 952b:欠損は局所の余分とともに単調、余分 ≤ 12 で R ≥ 0.95;952c:余分は磁気の結合に見える)。
- **再開条件**:なし(名指しを (JG-F‴) に置き換えた)。

## F335(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の全模型版 (JG-F‴\*) の弱い場の側:補題 544-C の入力 (MB_Q″) $\sup_QV\le(K_*/s)^3M$($V=\lvert a'\rvert^2$、射影した場)を、1 立方体の格子の C0 の類 C で「$K_*$ は h → 0 で有界・辺と角で定数倍だけ」と支えてから書き下す方式 —— **方式の閉鎖(類 C の否定 2 回)**(親、2026-10-22、稿 `546_`(札 COUNTEREXAMPLE)・記録 `547_判定_JGFのMBQ2_2026-10-22.md`(札 MBQ2_FAIL、結果を見ていない 監査の型 の判定文))

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:方式(sup と質量の比を点ごとの格子の値で支える道)。命題 (MB_Q″) の真偽は閉じていない —— 547 の D1(集まりの尺度に対する育ち $p_P\le1$)は PASS の側、外れたのは D0(h → 0 の極限)の 1 セル(面・向き x・r = 0.5)と D2 の幾何の因子の 1.57 倍。
- **読み(札に使わない)**:両回とも著者・判定者は外れを判定文の置き方(r/h = 2 の前漸近の段、質量の重み)に帰したが、記憶の規則どおり否定として受ける。共通点:**sup の形の量は境界(面・辺・角)の点ごとの正則性に敏感で、格子の C0 では分解能と境界の前漸近を分けられない**。
- **再挑戦の条件**:(a) 境界の点ごとの量を使わない入力(偶の鏡映で周期の箱に移して境界を内点にする形、または $L^p$ の逆 Hölder の形)に組み替えた 544-C の版が書けたとき;(b) 多面体の Neumann の正則性(Dauge・Grisvard)の原典で辺・角の $\sup$ の有界が定理で得られたとき。


## F336(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の全模型版:(JG-F‴\*) の (iii) 大きな場の床を、(a) 難問 #2 K1-B′ の強い場の補題 485-V(E05-P260)をそのまま当てて出す方式、(b) 大きな場の配位を場の自分のエネルギー(A-543-3 の $\frac{\theta_0}{2C_w}\int\mathrm w_Q\lvert\nabla B\rvert^2$)で払う方式 —— **方式**(w_E05_545 = 書き下しの型、2026-10-22、稿 `545_全列_計画1_JGFの大きな場の床_2026-10-22.md` §1.1・§1.3、worklog (研究ノート: `2026-10-22_w_E05_545.md`) §0.1)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:方式 (a)(b)。(iii) そのものは閉じていない —— 定理 545-CF(双対の試験場 + 穴の容量)で (MB_Q) の下に閉じた(E05-P? 545-CF・545-G)。
- **理由**:(a) 485-V の床は $\mu\lVert b\rVert^2_{L^2}\ge c_A\delta_0^4$・$\mu\ge c_B/(1+\lVert b\rVert_\infty)$ で、場の振幅とともに 0 へ落ちる —— K1-B′ はそれを場の罰 $c_2\int\lvert B\rvert^2$ と AM–GM で払った(485 §1.1 の (v′))が、JG の消費者には同じ罰が無い。(b) 485-W の Poincaré 部分で払いは $\ge\frac{\theta_0\pi^2}{4C_ws^2}u'_Q$、要求は $\frac{(1-\eta)\lambda\alpha}{2s^3}u_b$ —— $s\ge2C_w(1-\eta)\lambda\alpha/(\theta_0\pi^2)$ が要り、A-543-3 の $\Lambda_F$ の桁($\lambda\alpha\gg s$)と両立しない(値ではなく初等の比較;$\lambda\alpha$ の桁は監査 543 §3.1 の率)。
- **射程(T60)**:禁じるのは「場の強さで減る立方体の床(485-V の型)を、場の罰なしの消費者に当てる」発注と「(iii) の配位を局所の場のエネルギーで払う」発注。止めないもの:振幅に一様な床(545-CF)、場の罰を持つ消費者(K1-B′ は閉じたまま)。
- **再開条件**:なし((iii) は 545-CF で別の道に移った)。


## F337(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の J-G-st(監査 506 §4.3 (L2-b) の真の基底状態の水準の集中)を、**エネルギーの情報だけ**(BO の下界 J-G に「軌道からの距離の 2 乗」の余りを残した強い形・495-J 型の基底の重み s の下界・準最小の状態の変分 + 状態 → 密度の連続)で出す方式。2026-10-22、w_E05_551 = 書き下しの型、稿 `551_全列_計画1_JGstの状態の集中_2026-10-22.md` §1・§2、worklog (研究ノート: `2026-10-22_w_E05_551.md`)、C0 961a・961b、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(読み + 玩具の値)。J-G-st の真偽は閉じない。
- **理由**:3 候補とも「$\langle H_{\rm BO}\rangle_\gamma\le\mathrm{MF}_{\min}$ ⇒ 消費者の距離が小さい」の含意を使う。$G_{\rm MF}$ 自身が $\mathrm{MF}_{\min}-g$ にあり(514-R (iii))余裕は少なくとも g、J-G の証明済みの形では εE_MF(ε = O(ℓ^{−1/12}√log ℓ))。消費者($1-\mathcal R=V/((1+m)^2+V)$、V は窓の縁 —— 真空の域 —— の G の揺らぎの泡の対比 $\mathcal D\sim\kappa\ell^3$ に対する比)を 0.1 壊す最も安い局所の状態の費用は、稿 514 の玩具で g の Q = 3.77・4.94・8.41 倍(冪 +1.22、札 ST_BOUNDED)、$E_{\rm MF}$ の 0.047・0.032・0.029 倍(冪 −0.73 —— ε の冪 −1/12 より速く 0、証明済みの J-G では含意は大きな ℓ で必ず落ちる);連続では縁の殻の尺度 ℓ の古典の横波が費用 ~ℓ で消費者を O(1) 動かす(値)—— 要る精度は相対 o(ℓ^{−4})。強い形 $c\delta^2\gt$ 余裕と競争者の $c\,d_{\rm bad}^2\le$ 余裕 + exc から、余裕 ≫ exc なら δ は $d_{\rm bad}$ の桁を割れない(稿 551 §2.2)。
- **共通点(1 行)**:**場だけの汎関数(窓の縁の揺らぎ)を O(1) 動かす費用が、エネルギーの情報の精度より桁で小さい** —— F321(Griffiths の道、偽の欠損 ~ℓ³ ≪ F)と同じ障害で、エネルギーの微分でもエネルギーの余りでも当たる。
- **射程(T60)**:禁じるのは「BO・MF の水準のエネルギーの下界と MF_min の上界だけで、真の基底状態の窓の汎関数の積率を決める」発注(泡の平均の形 —— 密度 —— の集中は禁じない)。止めないもの:(d) 基底状態の方程式(pull-through / ファイバーの反跳の項 $\frac\lambda2(\cdot)^2$ が電子に相対的に固定した場の構造に課す費用 —— BO はこれを捨てる)を使う道;(e) $E_{\rm true}$ の上界を o(exc) の精度にする非断熱の評価(成算 1 割未満)。
- **再開条件**:J-G の相対の精度が o(ℓ^{−4})(連続)になり、かつ $E_{\rm true}$ の上界が同じ精度で $E_{\rm BO}$ に付く —— または消費者の窓の汎関数を低い k と縁の真空の励起に感じない形に再設計し、その費用が余裕を超えることを示す。


## F338(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の J-G-st:(f) 窓の縁を泡の内側に置いて (L2-b) をエネルギーだけで出す方式と、(d1) 素朴な pull-through(作用素のノルムで縁のモードの占有を押さえる)方式。2026-10-22、w_E05_552 = 書き下しの型、稿 `552_全列_計画1_JGstのpullthrough_2026-10-22.md` §1・§2、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(2 つ)。J-G-st の真偽は閉じない。
- **理由**:(f) A-506-1 の $D_j=-(\delta_{jz}+E_j/\mathcal D)$ で、コンパクトな台の窓の縁を泡の芯($G\approx-\kappa$ 一定)に置くと $E_z/\mathcal D\to-1$、$D_z\to0$;境に置くと泡の勾配が $E_j$ に残る;自己中心の窓も根の非退化に $\lvert E_z\rvert\lt\mathcal D$ が要る —— 縁を真空の域に置くのは構造(読み、初等)。(d1) ファイバーの pull-through は $a_kH(P)=[\frac\lambda2(X+k+\sqrt\alpha g_k)^2+H_f-\omega_k]a_k$ で右辺に $a_k$ が残り閉じない(反跳 $\lambda k\cdot X\gg\omega_k$);全空間の形は閉じるがノルムの評価は殻の 1 モードあたり ≲ αλE₀ ≫ 1 —— 局在の情報はレゾルベントの位相にあり、ノルムで捨てる。
- **射程(T60)**:禁じるのは「窓の縁を泡の芯に置く消費者の再設計」と「pull-through の作用素ノルムだけで縁の真空からのずれを押さえる」発注。止めないもの:Euclid の形(経路ごとの Gauss、稿 552 補題 552-G・552-B)で (PT-e)・(PT-m) を示す道。


## F339(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の J-G-st:消費者 (L2) を**片側化**し、その向きを平均場の積の試行状態の**変分の上界だけ**(真の基底状態の情報なし)で出す方式(親の設計メモの候補 C1)。2026-10-22、audit_design_JGst = 監査の型、監査 `553_設計監査_JGst_2026-10-22.md` §1.3〜§1.5、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(読み、初等)。J-G-st・全列の真偽は閉じない。
- **理由**:(1) 計画 Ⅰ の量 $f_{\rm sr}=E''(0)/\lambda$($f_{\rm ls}$ も p → 0 の差分商)は最小点の曲率で、上界は p = 0 で $E(0)$ に接する試行からしか出ない;MF の試行は $g_{\rm true}=\mathrm{MF}_{\min}-E(0)\ge0$ の隙間で曲率の情報を失う(Brooks 2024 (1.11)〜(1.12) の注意と同型)。ゆえに試行は真の ψ の上に組む(501-X・LS (2.1)・Brooks (1.15))。(2) 片側は R の側では正しい($\mathcal R\le1$ は自動)が、要るのは真の ψ の非負の量 W の上界で、凹性の挟みでは W を報酬にした $E(-s)$ の下界 —— F321 の折れの側そのもの;作用素不等式 $W\le c(H-E_{\rm low})+\delta$ と $E\le\mathrm{MF}_{\min}$ の型は稿 551 (a)(F337)。
- **共通点(1 行)**:**片側化は「どちらの不等式が自動か」を変えるだけで、要る側(真の状態の量の上界)に安い競争者が効く限り F321・F337 の障害は同じ所に残る。**
- **R9**:双極子では計画 Ⅰ の消費者が定義されない;擬交差の梯子には触れない。
- **射程(T60)**:禁じるのは「(L2) の片側化だけで J-G-st を不要にする」発注。止めないもの:消費者の観測量の尺度を変えて安い競争者を消す設計(監査 553 の C6)。
- **再開条件**:曲率を接しない試行から押さえる大域の不等式(例:$E(p)\le E(0)+p^2/2m_{\rm eff}$ 型の逆向きの比較で MF の試行と組めるもの)が PF で供給されたとき。

## F340(E05、同じ J-G-st を、真の基底状態の代わりに**準最小の状態の族の上の上限**または**低温の Gibbs 状態**で (L2-b) を出す方式(親の設計メモの候補 C4)。2026-10-22、audit_design_JGst = 監査の型、監査 `553_` §2、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(読み)。
- **理由**:エネルギーの窓 ≫ ℓ の準最小の族は稿 551 の競争者(縁の古典の波・加熱、費用 ~ℓ)を含み、消費者の欠損の上限は O(1) —— 上限で書いた条件は**偽**の向き;窓を o(ℓ) にすると F337 の精度の要求に戻る。低温の Gibbs 状態は Euclid の有限時間の経路の測度で、稿 552 の (PT-e)(PT-m) と同じ道に合流する。501-X は真の固有ベクトルを要り(近似固有ベクトルの誤差 $\lVert\hat X^2\rVert\lVert(H-E)\phi\rVert$)、状態の族への置き換えは消費者の字面に合わない。
- **射程(T60)**:禁じるのは「状態の族の上限で消費者を書き換える」発注。止めないもの:Euclid の経路の道(C2・C3)と C6。
- **再開条件**:消費者の観測量を、縁の安い変形に感じない形にしたとき(そのときは族の上限でも O(1) にならない —— C6 の型)。

## F341(E05、同じ J-G-st を、**光子の位置の表示の頑健な重心**(Brooks 2024 の正則化した中央値 $m_q(\chi*\rho)$ を光子の経験測度で)を 501-X の型の擬似ブーストにし、その集中をエネルギーで出す方式(監査 553 の候補 C5)。2026-10-22、audit_design_JGst = 監査の型、監査 `553_` §2、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(エネルギーの道;読み + 値)。
- **理由**:粒子の表示では真空は粒子 0 で縁の揺らぎが消え、$B(\rho_z)=B(\rho)+z$ で $D\equiv e_z$ が厳密 —— ただし光子数は赤外で安い:波長 L の軟光子を泡の光子数 N(~F)の 2 倍置く費用は ~2N/L + λN/L² → 0 で中央値を動かせ、エネルギーの精度 εF の内に入る;真の状態の軟光子の少なさを pull-through で示す道は、波長 ℓ〜L の光子で反跳が効き稿 552 §2 の αλE₀ の損に戻る。F190 (a) の「PF には局在した雲が無い」は Φ57(E05-P257)以前の読みで、絞りの泡は粒子の表示で局在する —— 閉鎖の理由はこれに差し替える。
- **射程(T60)**:禁じるのは「光子数で重みづけた頑健な重心をエネルギーだけで集中させる」発注。止めないもの:エネルギーで重みづけた(可換な族にできる)頑健な重心、C6。
- **再開条件**:赤外の光子を重みで消した可換な観測量の族(例:ウェーブレットの占有数をエネルギーの尺度で重みづけたもの)で並進共変性の誤差が制御できたとき。

## F342(E05、同じ J-G-st の磁気の模型の名指し (PT-m) を、**反磁性の不等式**(偶の模型・場の無い模型との比較)で押さえる方式(親の設計メモの候補 C3 の推論 1)。2026-10-22、audit_design_JGst = 監査の型、監査 `553_` §4、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(読み、初等)。(PT-m) の真偽は閉じない。
- **理由**:(1) 反磁性の不等式 $\lvert(F,e^{-tH}G)\rvert\le(\lvert F\rvert,e^{-tH_0}\lvert G\rvert)$(Hiroshima 1997 の型)は正規化前の半群の比較で、基底状態の期待値に正規化すると比 $e^{2t(E-E_{\rm dec})}$ が発散する(自己エネルギーを失う)。(2) 場を積分した経路の測度は正(Betz–Hiroshima 2009 (1.4)〜(1.5))で、偶の正定値の汎関数には虚のずれが $\cosh\ge1$ で**下界**を与える —— 縁の上界には向きが逆。
- **射程(T60)**:禁じるのは「反磁性・正定値性で (PT-m) の縁の上界を出す」発注。止めないもの:名指しを (PT-m′)(正の経路の測度の下の縁の Euclid の場 $b(y)$ の指数モーメント)に言い直した道。
- **再開条件**:正規化した期待値どうしの比較不等式(磁気 ≤ 偶)が PF で供給されたとき。


## F343(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の J-G-st を、記録 553 の補題 553-W(縁の 2 次のモーメントを縁の体積の Cauchy–Schwarz で 1 次のモーメントに落とす消費の形)と局所の計量つきの J-G (J1) で閉じる方式。2026-10-22、w_E05_554 = 書き下しの型、稿 `554_` §1・§2.2 注 (2)、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21

- **閉じたもの**:**方式**(初等の勘定)。J-G-st の真偽は閉じない(稿 554 の 554-W′ で別の消費の形に置き換えた)。
- **理由**:553-W の第 1 項は $K^3\varepsilon_{\rm J1}/(c\kappa_0^2)$ で、窓の尺度 K を育てるなら $\varepsilon_{\rm J1}\ll K^{-3}$ が要る。(J1) を J-G の鎖から運ぶには殻を IMS の箱(辺 $M\ell$、$M\to\infty$ は消費者の IMS の誤差に要る —— A-540-1)の外に置く包絡が要り、球の帯域の鋭い切断の裾で内の座標の場が殻に漏れて $\varepsilon_{\rm J1}\gtrsim(M/K_c)^{1/2}\ge K^{-1/2}$(補題 554-S の冪)—— 両立しない。
- **射程(T60)**:禁じるのは「縁の汎関数の 2 次のモーメントを縁の体積で 1 次のモーメントに落とす消費者」と、M → ∞ の J-G から (J1) を運ぶ組み合わせ。止めないもの:K を止める読み(M も止めると IMS の誤差が残る)、自己中心の窓(554-W′:悪い事象の確率だけを要り Markov で 1 次のモーメントから出る)。
- **再開条件**:殻の電場のエネルギーの 2 次のモーメント $\langle(\int_R{:}\lvert E\rvert^2{:})^2\rangle$ の上界が供給されたとき、または J-G が M を止めた箱で o(1) の精度を持つとき。


## F344(E05、全列(行 E1-H)の計画 Ⅰ の芯 J-G の J-G-st の磁気の模型の名指し (J2-m) を、**Coulomb ゲージの閾の観測量 $h_\theta(\theta\lvert A\rvert^2)$ のまま**、エネルギーの情報(箱の水準の低いエネルギーの全ての状態での押し縮め —— 稿 554-J2e (ii)(iii) の型 —— ・ファイバーの変分・J-G の余り)だけで出す方式。2026-10-22、audit_S2_JGst = 監査の型、監査 `555_合同監査_JGstの偶の分_2026-10-22.md` §4.2、成算 S254)

親(G3 第 73 陣)が連結 2026-10-21
- **閉じたもの**:**方式**(読み、値の競争者)。(J2-m) の真偽・磁気の J-G-st は閉じない(値では真の向き:真の基底状態は T′ で $\langle a\rangle=0$、長波の真空の揺らぎは $\theta\lvert A_{\gt\ell}\rvert^2\sim c_\theta\alpha$)。
- **理由**:電子の箱の周りに尺度 R(≫ Mℓ)・振幅 $a_0$($\theta a_0^2=L_a\gg L$)の静的な横波の古典の場を Weyl のずらしで足し、電子にゲージ $e^{-i\sqrt\alpha a_0\hat\varepsilon\cdot(x-x_0)}$ を掛ける競争者は、泡の中で $\theta\lvert A+a\rvert^2\gg L$ にして芯の閾の質量を真空の値に落とす(消費者の Γ を壊す)一方、費用は電子の残り $\frac{\lambda\alpha}2a_0^2(M\ell/R)^2\asymp\mathrm{MF}(L_a/c_\theta)(M\ell/R)^2$ と場 $\frac12\int\lvert\mathrm{curl}(a)\rvert^2\sim L_aR/(c_\theta\alpha\ell^2)$ —— $R\gg M\ell\varepsilon^{-1/2}$ で J-G の余裕 εF より小さい(ファイバーでは場の運動量の補償 $\gtrsim\sqrt\alpha a_0\sim\ell^{-1}$、やはり安い)。ゆえに「箱の $\langle H\rangle\le2\mathrm{MF}$ の全ての状態で芯が押し縮む」の磁気版は偽。偶では同じ競争者が結合 $ca_0^2\asymp\mathrm{MF}L_a/c_\theta$ を払う(正値性 $c\lvert A(x)\rvert^2\le H$)ので効かない。
- **共通点(1 行)**:**ゲージで消せる成分を観測量が見る限り、磁気のエネルギーはそれを罰さず、F321・F337 の「場だけの汎関数を安く動かす競争者」がゲージの自由を通って戻る。**
- **R9**:双極子では泡が無く (J2-m) は偽で、方式の閉鎖と独立;擬交差の梯子は場の配位が無く書けない。閉じたのは方式で、標的(全列)と同値でない。
- **再開条件**:観測量をゲージ共変にする((J2-m′):ブロックの射影 $u'_{Q(y)}$ か curl A の閾 —— 監査 555 §4.3)か、エネルギー以外の真の基底状態の情報(T′ 以上の長波の揺らぎの評価)を使う。

## F345(2026-10-22、w_E05_563、稿 `563_難問2_自己エネルギーの主要項の漸近_2026-10-22.md` §0.1)難問 #2 の締めの字面「$E_0/(F[1]\alpha^{2/7}\Lambda^{12/7})\to1$」—— 閉じたのは**命題の字面(定数)**

親(G3 第 73 陣)が連結 2026-10-21
- **何が偽か**:公理表(= Lieb–Loss 1999)の規格化では極限は $(6\pi^2)^{-4/7}\approx0.0971$(Bach–Hach の規格化 $\alpha_{\rm BH}=\alpha/2$ でも $(\sqrt2/(6\pi^2))^{4/7}\approx0.1184$)で 1 ではない(系 563-C)。原因:Bach–Hach Thm I.1 の主張文の定数をそのまま写したこと(BH の A の規格化が LL の $\sqrt2$ 倍、BH の $\beta(\alpha,\Lambda)$ が Weyl の係数の $(2\pi)^{3/2}$ 倍、主張文の $F_1$ が証明の $F[\beta(\alpha,\Lambda)]$ と不一致)。
- **正しい形**:$E_0=(1+o(1))F[1](6\pi^2)^{-4/7}\alpha^{2/7}\Lambda^{12/7}$、$E_0/E_{\rm LL}\to1$(系 563-C、self-audited)。
- **再開条件**:なし(命題の字面の訂正;正しい形は系 563-C が供給)。


## F346(2026-10-22、w_E05_569、稿 `569_難問1_族E3_族の存続の0側の類C_2026-10-22.md` §2、成算 S-E05-R1)難問 #1 の道 (a)「J-G の泡の外の自己相似の有効模型(1 ループの RG の写像の不動点)」—— 閉じたのは**方式**

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:写像 $h_{n+1}=1+\frac{8\alpha}{3\pi}\ln(1+\frac{\lambda_n}2)$、$\lambda_{n+1}=\lambda_n/\ell(\lambda_n)$(と有効質量を入れた $\lambda_n/(\ell_nh_{n+1})$)、$\ell=0.889(\alpha\lambda)^{1/7}$(NUM-7302 の α=1 の泡の尺度)の不動点を、J-G の域 λ ≥ 1e7(NUM-7303)で探した(C0 977b)。
- **理由**:形式の不動点($\ell=1$ または $\ell h=1$)は λ* = 0.58〜312(α = 1〜1/137)で J-G の域の 5 桁以上下 —— 域の中の写像は $\log\lambda\mapsto\frac67\log\lambda$ の縮小で、紫外の不動点(自己相似の有効模型)は無い(NOFP)。ℓ の α の冪を替えても不変。写像が与える $h_{\rm tot}$ の副多項式の成長(ι=0 の向き)は、入力の 1 ループの形 A の局所冪(α=1・λ=256 で 0.17)が実測(NUM-7563:0.55)の 1/3 であることの写しで、証拠にならない。
- **閉じたもの**:方式(有効模型の自己相似で (T3)(T6) を立てる道)。ι の値・(T3)(T6) の真偽は閉じない。
- **R9**:双極子には泡が無く ℓ が定義されない(適用外);擬交差の梯子は場の自由度が無く適用外。標的 (T0) と同値でない。
- **再開条件**:泡の外の有効模型の結合(1 ループの形 A に替わる、J-G の域での $h$ の一段の値)が在庫に入り、それで写像が域の中に不動点を持つこと。

## F347(2026-10-22、w_E05_569、稿 `569_難問1_族E3_族の存続の0側の類C_2026-10-22.md` §3、成算 S-E05-R1)難問 #1 の道 (d)「Euclid の経路の測度の UV 極限(GHL 型の対角の引き算)」の標的 (T1) の Euclid 版 —— 閉じたのは**標的の字面**(1 ループの値)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:$P=0$ ファイバーの真空の振幅 $\langle\Omega,e^{-T(H-E_{\rm sub})}\Omega\rangle$ = Euclid の $\mathbb E[e^{-\frac{e^2}2(S_T-\mathrm{sub})}]$ を 2 次のキュムラント(order $e^4$ で厳密、反跳つき)で、(D) 1 次の対角 $E_{\rm diag}=\frac{e^2}2\langle A^2\rangle$ を引く版、(R) 基底エネルギー(2 次まで)を引く版、T = 1・0.1、λ = 4〜64・1e3(C0 977c)。
- **理由**:(D) は残りの 2 次の自己エネルギー $T\lvert E^{(2)}\rvert\sim\alpha^2\lambda^2$ で ∞(局所冪 2.6 → 2.2);(R) は対の重み $e^{-\lVert\psi_2\rVert^2}$、$\lVert\psi_2\rVert^2\sim\alpha^2\lambda^{1/2}$(F179 (2) の型)で 0(λ=1e3 で 5.9e-4)。**どの引き算でも有限の非自明な極限が無い** —— GHL(Nelson)では対角が対数の自己エネルギーを取り切るが、PF では 2 次の $\lambda^2$ の自己エネルギーと背中合わせの対の重みが残る。
- **閉じたもの**:標的の字面(Euclid の真空の振幅の有限な極限としての (T1))。1 ループの値で、非摂動の極限は主張しない(非摂動の向き:$w_0e^{T(E_{\rm diag}-E_0)}$ の下界で $\log w_0=o(\lambda^2)$ なら ∞)。
- **R9**:双極子では反跳が無く 2 次の自己エネルギーと対の重みは同じ冪かそれ以上で、同じく有限でない(閉鎖と整合);擬交差の梯子は適用外。
- **再開条件**:引き算に 2 次以上の自己エネルギーの作用素の項(定数でない)を入れた Euclid の構成の型が文献か在庫に入ること(Eckmann 1970 の「質量くりこみが作用素」の型の PF 版)。


## F348(2026-10-22、w_E05_568、稿 `568_難問1_族E1_泡の慣性の類C_2026-10-22.md` §3.1・§4、成算 S-E05-R1)難問 #1 の道 (e) の入力「場のエネルギーから泡の慣性を出す」(564 §3 の推論 1「コヒーレントな雲で $M=\frac23E_f$」、族 E-2 の (e1)〈$\langle H_f\rangle_{\psi_0}\ge c\,\mathrm{MF}_{\min}$ ⇒ $h/\lambda\gtrsim\lambda^{5/7}$〉)—— 閉じたのは**方式**(道 (e) の向きと標的 (T0) は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:J-G の玩具(稿 514 §1、α=1)の MF の泡の移動解の慣性を積の Gauss の状態の TDVP(= Inglis の cranking、1 振動子で相対 4.5e-11 で一致)で $M_{\rm LP}=1/\lambda+\sum_x\lvert\nabla\sigma_x\rvert^2$($\sigma_x=(2\Omega_x)^{-1/2}$)とし、λ = 1e5〜1e9 で $\mathrm{MF}_{\min}$・場のエネルギー $E_f$ と並べた(C0 976a・976a2)。
- **理由**:$E_f/\mathrm{MF}_{\min}$ = 0.608 → 0.575 で一定(場のエネルギーは全体の一定割合 —— (e1) の MF の版は成る)のに、$M_{\rm sq}/\mathrm{MF}_{\min}$ の局所冪は −0.38・−0.40・−0.41・−0.42(→ −3/7)。PF の積状態の泡は squeezed vacuum(実の $\varphi$ では $p\cdot A$ の 1 次の源が 0 でコヒーレントな変位が無い)で、エネルギーは各点の零点の振動数の和(体積)、慣性は共分散の空間の勾配(壁の面積 $\ell^2$)—— 両者は別の量で、コヒーレントな雲の恒等式 $M=\frac23E_f$ は成り立たない。ゆえに (e1) を証明しても $h$ の冪の率は 564 §3 の天井 (ii)($E_f^2/E_0\sim\lambda^{6/7}$)の型を越えない。
- **閉じたもの**:方式(場のエネルギーの下界を慣性の下界に読み替える段)。値の水準で、真の基底状態の慣性については主張しない。道 (e) の向きは残る:同じ玩具で $h/\lambda\approx M_{\rm LP}\sim\lambda^{0.30}$(C-e1 = N1E1_GO)。差し替えの入力は (e1′)「場の共分散の泡の壁の勾配 $\gtrsim\ell^2$」(稿 568 §4)。
- **R9**:双極子では場が電子の位置に依らず $\nabla\sigma\equiv0$ —— 泡も慣性のこの機構も無い(適用外、閉鎖と矛盾しない);2 構造の擬交差の梯子は場の自由度が無く適用外。

## F349(2026-10-22、w_E05_570 = 書き下しの型、稿 `570_hlsの上界_JG域のBrooks型_2026-10-22.md` §1〜§4、成算 S-E05-R2、C0 978a)$h_{\rm ls}$ の上界(難問 #3 の上側・#1 の (T0) の ι = 0 の側)を、大きい λ で $E(p)-E_0\ge\frac{p^2}{2M}(1-o(1))$($M\approx M_{\rm LP}$)として Fröhlich の強結合の型(Brooks 2024・Brooks–Seiringer 2024 Part II)で J-G の域の PF に移す方式(親の設計メモ 2026-10-22 07 時の候補 1 (B))—— 閉じたのは**方式**(標的 $h_{\rm ls}\le(1+o(1))M_{\rm LP}/m$ の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:原典の本文(arXiv 2211.03353v1・2409.08835v1)で証明の入力を 4 項に分けて PF の在庫と照合し(稿 §1.3)、要る精度 $p^2/(2M_{\rm LP})$ と J-G の誤差 $\varepsilon\,\mathrm{MF}_{\min}$ の比を稿 568 の玩具の値で λ = 1e5〜1e9 に並べた(C0 978a、札 WALL)。
- **理由**:(1) 向き:標的は $m_{\rm eff}$ の上界の向きで、Fröhlich でこれを出したのは Brooks 2024(擬ブーストの試行 = 下界の向き)でなく B–S II の系 1.2 —— (A) $\lvert P\rvert\sim\alpha$ での絶対の下界を誤差 $\alpha^{-(2+w)}$(2 次の補正の先)で、(B) Polzer 2023 の $E(P)\le E(0)+P^2/(2M_{\rm eff})$ で P → 0 へ運ぶ。B–S II の定理 1.1 単独は誤差が $P^2$ に比例せず P → 0 に届かない。(2) (A) の精度:玩具で要る相対精度は ≈ $1/N_*$(泡の中の 1 モードの量子 $\Omega_{\max}$ / 全体、$\lambda^{-3/7}$ の桁;× $N_*$ = 1.04 → 1.73)。J-G は相対 $\sqrt{\log\log\lambda/\log\lambda}$、その機構(多数のモードの大数の法則)の最良でも $N_*^{-1/2}$;比 ρ は最も甘い p(泡の速さ = 光速)でも 1.7e-3 → 4.9e-5 で λ とともに下がる。(3) (B):F169((M1)(M2) が逆)・F254 (R2) —— PF に |P|² の凹性の道具が無い。(4) 乗数(Legendre)の段は PF で Fröhlich より易しい(観察 570-A:$\lvert v\rvert\lt1$ で $\inf\sigma(H-v\cdot\mathbf P)\gt-\infty$、(D)〈$E_0-g(v)\le\frac M2v^2(1+o(1))$〉⟹ 標的)が、(D) は無質量の連続体の底の 2 次の摂動の非摂動の上界で、F254 (U4)・観察 434-B と同じ赤外の問い。F141 の障害(相互作用が平方の中)は主要項では J-G が払ったが、(A) の精度の紫外の替えでは再び立つ。
- **閉じたもの**:方式(B–S II・Brooks の型を J-G の精度のまま PF に移すこと)。標的・(D)・(N1)(N2) の真偽は閉じていない。
- **R9**:双極子では (N1)(N2)・標的とも真(2 次の模型)で閉鎖と矛盾しない;2 構造の擬交差の梯子では (N2)(2 本の放物線の min は $P^2$ について凹)は真で標的は外れうる —— 再開条件は標的と同値でない。
- **射程(T60)**:禁じるのは「J-G の主要項の精度(相対 o(1) のエネルギーの言明)と試行状態・擬ブーストだけで $h_{\rm ls}$ の上界(有効質量の上界)を出す」形の発注。止めないもの:(N1) PF の 2 次の展開そのもの;(D) の赤外の評価(候補 2 (I) の型);Brooks 2024 の擬ブーストを $h$ の**下界**の向き(族 E-2 の (e2))に使うこと。
- **再開条件**:(N1)PF の基底エネルギー(と $g(v)$ または $E(P)$)の 2 次の展開が絶対誤差 $o(\Omega_{\max})$(相対 $o(1/N_*)$)で在庫に出たとき、**かつ** (N2)PF の放物線の上の包絡 $E(P)\le E_0+P^2/(2M_{\rm eff})$(|P|² の凹性、F254 の再開条件 (3))か (D) の赤外の評価(F254 の再開条件 (2) の型)が出たとき。


## F350(2026-10-22、w_E05_568b、稿 `568_難問1_族E1_泡の慣性の類C_2026-10-22.md` §7.1、成算 S-E05-R1)難問 #1 の (T0) の ι>0 側に、光子数で重みをつけた擬ブースト(光子だけの運動量の一様なずらし、生成子 $D=N$、P118 の $D_\theta$ の型)の Rayleigh 商で $h$ の冪の率の下界を出す —— 閉じたのは**方式**(道 (e) と標的 (T0) は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:稿 514 §1 の玩具(α = 1)の MF の squeezed の泡で、光子だけの擬ブーストの最良の値 $h_{\rm rec}=1+\langle N\rangle^2/\mathrm{Var}N$(場のエネルギーの変化を落とした楽観の値)を λ = 1e5〜1e9 で、泡と電子を一緒に動かす慣性 $h_{\rm LP}=\lambda M_{\rm LP}$(Dirichlet・周期の箱の両方)と並べた(C0 976c・976d・976e)。
- **理由**:$h_{\rm rec}$ の局所冪 0.506 → 0.442(→ 3/7)。PF の積の状態の泡では光子が対で生まれ $\mathrm{Var}N\sim\sum_xs_x^2$(超 Poisson)なので、$\langle N\rangle^2/\mathrm{Var}N$ は $\langle N\rangle\sim\lambda^{5/7}$ にすら届かず $\lambda^{3/7}$ —— ι>0 に要る $h\ge c\lambda$ に冪で届かない。一方、泡の汎関数を生成子にした試行は $h\sim\lambda^{9/7}$(冪 1.30)に届く。
- **閉じたもの**:方式(光子数の重心型の生成子で ι>0 を出す段)。値の水準で、真の ψ0 については主張しない。比較はどちらも $h$ の下界の試行なので、真の $h$ が反跳型に上から押さえられる(道 (f))ことは示さない。監査 567 §3.3 の訂正(P = 0 ファイバーではどの試行も場だけの擬ブーストで、違いは生成子)と整合。
- **R9**:双極子では泡が無く、線形の h は 1 光子の電磁質量の機構 —— 光子数の重心の試行の値は双極子では別の量で、閉鎖と矛盾しない;2 構造の擬交差の梯子は場の自由度が無く適用外。

## F351(2026-10-22、w_E05_570b = 書き下しの型(w_E05_570 の再開)、稿 `570_hlsの上界_JG域のBrooks型_2026-10-22.md` §7、成算 S-E05-R2 の追記、C0 978b)$h_{\rm ls}$ の上界を、親の設計メモ 2026-10-22 07 時の候補 2 (I)「赤外の着衣の重なり(泡の外の軟らかい光子のコヒーレントな雲の差、速さ $v\sim p/M$)」で、観察 570-A の (D)〈$E_0-g(v)\le\frac M2v^2(1+o(1))$〉の形で出す方式 —— 閉じたのは**方式**(候補 2 を単独で上界の道にすること);赤外の段そのもの・標的の真偽は閉じていない

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:(D) を観察 434-B・F254 (U4)・観察 570-A と並べ、小さい α の文献(BCFS 2007 Thm 2.1、Chen 2008 Thm 3.1、CFP 2009 Thm III.1)を本文で照合;1 ループの重い粒子の雲の差の重み $e^{-N}$、$N=\frac{\alpha}{4\pi^2}v^2A(v)\ln\frac{\mu}{\eta p^2}$ を 976a の玩具の M・$R_*$ で λ = 1e5〜1e9 に並べた(C0 978b、値の札 GO)。
- **理由**:(1) 小さい α・固定の紫外の切断では標的は既知(Chen 2008 (3.2)・(3.3):$\partial_{\lvert p\rvert}E\ge(1-c_0\alpha)\lvert p\rvert$、σ に一様)、機構は CFP (III.15)(基底状態 = 速さ $\nabla E$ の軟らかい雲 $W_\sigma(\nabla E)$ × 正則な Φ)。(2) 値:重みは各 λ で p → 0 で 1 に行き(p/M = 1e-4 で 0.999999)、着衣の速さでの係数は λ とともに下がる(局所冪 −0.6)—— 赤外は律速でない。(3) 大きい α では多尺度の解析の**入力**(IR の切断 $\mu\sim1/R_*$ の上のファイバーの隙間・光速未満〈CFP (I4) の型〉・$\nabla E^\mu$ の正則性・曲率の両側)が無く、質量の上界側 $M_\mu\le(1+o(1))M_{\rm LP}$ は標的の μ 版 —— F349 の壁(強結合の 2 次の精度)が μ の上に残る。(4) 係数は着衣の速さ $\nabla E=p/(mh)$ で決まり、裸の速さでは $\lambda^2$ で爆発(対照):λ に一様な赤外の評価は $h\gtrsim\lambda$(ι の側)を入力に要する —— 循環。
- **閉じたもの**:方式(候補 2 で強結合の中身を迂回すること)。赤外の段(μ → 0、入力を仮定)は止めない。
- **R9**:双極子では μ の上の質量殻・赤外の段・標的とも真(434-B の R9 と同じ);2 構造の擬交差の梯子では赤外の段は真だが μ の上の基底の枝の質量が $M_{\rm LP}$ と違いうる —— 再開条件は標的と同値でない。
- **射程(T60)**:禁じるのは「赤外の着衣の重なり・底の窓の重み・軟らかい光子の多尺度だけで、大きい λ の $h_{\rm ls}$ の上界(強結合の質量)を出す」形の発注。止めないもの:段 IR(重い粒子 + 波長 > $R_*$ の光子の Chen–CFP の型、入力を仮定した条件付きの書き下し);段 S の (S1)(隙間、光子の質量の正則化で自明の部分)。
- **再開条件**:IR の切断 $\mu\sim1/R_*$ の上のファイバーの、強結合での曲率の下界(= 質量の上界)$\partial^2_{\lvert P\rvert}E^\mu\ge(1-o(1))/M_{\rm LP}$ と光速未満 $\lvert\nabla E^\mu\rvert\le C\lt1$ が在庫に出たとき(F349 の再開条件 (N1) の μ 版と、族 E-2 の ι > 0 の側)。

## F352(2026-10-22、w_E05_571 = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §1・§4.2 (b)、成算 S-E05-R1、C0 979a)難問 #1 の (E4) の ι > 0 の側に要る $f_{\rm sr}\le C/\lambda$(= 率 $\ell^{-7}$)を、計画 Ⅰ の鎖(562-B の型:557-W (d)(e) の $P(\Gamma^c)$ を 557-J2m の Markov + 554-J1 の IMS + MF の水準の J-G〈541-G・548-G・A-549-2〉で抑える)のパラメタの取り方の替えで出す方式(監査 567 §5 の族 E-2′ (a))—— 閉じたのは**方式**(標的 $f_{\rm sr}\le C/\lambda$、ι > 0 の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:562-B の上界の 6 項の各々について、在庫の窓(562 §2.3 の前提)の最良と、項を作る不等式の型の床を出した(稿 §1 の表)。
- **理由**:どの項も $\ell^{-7}$ に届かない。(1) 律速:$\varepsilon_{\rm JG}$(MF の水準の相対精度、在庫の窓で $s\le\ell^{1/10}$ ゆえ $\eta_s\ge\ell^{-1/20}$)が 557-J2m の Markov の増幅 $1/(c_\theta\kappa_0)\sim\eta^{-8}$ を通って率 $\sim\varepsilon^{1/9}$;$\ell^{-7}$ には $\varepsilon_{\rm J1}\le\ell^{-63}$ が要る。(2) 構造の床:IMS $M^{-2}\ge\ell^{-4/3}$($\mu\lt2/3$)、殻(557-H)と $\langle C_f\rangle/\lambda$(557-W (c))の積 $\ell^{8\kappa_c-8}\kappa_0^{-3}$ で少なくとも一方 $\ge\ell^{-4}$、殻の項 $(M/K_c)^{1/2}\ge\ell^{-1/3}$。(3) Markov を通す限り、良い集合の下界の相対精度 $1/\lambda$(場の量子 1 個より細かい絶対精度)が要る。
- **共通点(1 行)**:**エネルギーの 1 次の積率(Markov)で悪い配位の確率を抑える型は、MF の水準の相対精度を率に写すので、率 1/λ には相対精度 1/λ の下界を要する —— 消費者の形(自己中心の共変な推定子、571-A)は正しく、壁は確率の評価の型に在る。**
- **R9**:閉じたのは方式。難しさは「共変性の破れる配位の確率 $P(\Gamma_\Delta^c)\le C/\lambda$」(名指し 571-N)へ移った —— 消滅ではない。双極子(泡なし)には当たらず、2 構造の擬交差の近くでは 571-N が偽になりうる(空でない)。
- **射程(T60)**:禁じるのは「557-ST/562-B の鎖のパラメタの取り方・閾の関数の替えだけで率 $\ell^{-7}$(または $f_{\rm sr}\le C\lambda^{-\gamma}$、γ > 4/21)を出す」発注。止めないもの:Markov を指数の局在(Agmon の型、確率の**上界**;F223 の射程の外)に替える道 (b′)、揺らぎの水準の J-G (c)。
- **再開条件**:(1) 配位の集合に局在した J-G の作用素の下界(悪い集合で $H-E\ge(\delta-\varepsilon)\mathrm{MF}$)が在庫に載ったとき((b′) の入力);(2) MF の水準を越える相対精度 $o(\lambda^{-1})$ のエネルギーの下界が載ったとき。

## F353(2026-10-22、w_E05_572 = 書き下しの型、稿 `572_hlsの上界_質量殻を仮定した条件付き定理_2026-10-22.md` §1.2・§2、成算 S-E05-R2)$h_{\rm ls}$ の上界の段 IR を、IR の切断 μ を泡の尺度 $1/R_*$ に置いて(稿 570 §7.3 の設計)、波長 > $R_*$ の光子を重い合成粒子への摂動として Chen 2008・CFP 2009 の多尺度で扱う方式 —— 閉じたのは**方式**(μ の取り方);段 IR そのもの・(MS$_\mu$)・標的の真偽は閉じていない

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:最初の Feshbach の段の 2 次の量を、和則の恒等式(補題 572-S)と Feynman–Hellmann で評価した(補題 572-F)。
- **理由**:軟らかい光子は裸の電流 $e(Q-P_f-eA)/m$ に結合し、その簡約レゾルベントの応答は恒等式 $\langle V\psi,RV\psi\rangle=\frac m2(1-m\,\partial^2E)$ で着衣で改善されない($M\gg m$ で $\frac m2$)。帯 $[\sigma',\mu)$ の 2 次の量は $\alpha(\mu\lvert\nabla E\rvert^2+\mu^2/m)$、隙間 ρμ との比は $\alpha\mu/m$ を含む —— 摂動の小ささは $\mu\lesssim m/\alpha$ でしか立たない。$1/R_*$ は格子単位で $\lambda^{-1/7}$、$m/\alpha=1/(\alpha\lambda)$、比 $\alpha\lambda^{6/7}\gg1$。978b(NUM-7586)の着衣の速さの係数は軟らかい雲の光子数(対数の項)で、この裸の質量の項を含まない。
- **閉じたもの**:方式(μ ~ $1/R_*$ で段 IR を摂動にすること)。μ = $c_*m/\alpha$ に下げた設計(稿 572 の (MS$_\mu$))は開いている;そのとき段 S は泡の尺度から $m/\alpha$ までの全ての光子を含む。
- **R9**:双極子では裸の電流の応答は $\frac m2(1-m/m_{\rm eff})$ で同じく飽和し、閉鎖と整合;2 構造の梯子は場の自由度が無く適用外。
- **射程(T60)**:禁じるのは「泡の尺度の IR の切断の上の質量殻から、裸の質量の 2 次を着衣の質量に置き換えて段 IR を摂動で回す」形の発注。止めないもの:μ = $c_*m/\alpha$ の (MS$_\mu$) の下の段 IR(稿 572 の (CR))。
- **再開条件**:裸の電流の応答のうち隙間 σ の窓の部分 $\langle V\psi,1_{[0,\sigma]}(K-E)\,(K-E)^{-1}V\psi\rangle$ が $m\cdot o(1)$ で抑えられる入力(高いエネルギーの内部の励起が窓に重みを持たないこと)が出たとき —— そのとき比は $\alpha\mu/M$ の型に改善しうる。

## F354(2026-10-22、w_E05_571b = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §7、成算 S-E05-R1、C0 979b・情報 979c)名指し 571-N(共変性の破れる配位の確率 ≤ C/(λW²ℓ²))の類 C を、窓の半径を ℓ の固定倍($R_W=2\ell$、縁 $(W-\frac12)\ell=1.5\ell$)に取った整合フィルタの推定子で Gauss の玩具の値として当てる方式 —— 閉じたのは**方式**(窓の取り方;571-N と標的の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:Gauss の積の状態(976d の MF)で、雑音の偽の泡の Chernoff の和と、電子の広がりで泡の中心が窓の縁に来る確率 $P_{\rm el}$ を λ = 1e5〜1e9 に並べた(判定文は worklog §6 に起動前に固定)。
- **理由**:判定量の局所冪 −0.26・−0.11(NOGO の帯 ≥ −0.3)。遅いのは $P_{\rm el}$ だけで、泡の半径 $R_*$ が 1.49ℓ → 1.63ℓ と ℓ より速く育ち、窓の縁 1.5ℓ が泡の内側に落ちる(電子の密度の泡の内側の部分を「窓の外」と数える)。雑音の項は $\log P$ = −140 → −16332 で超冪。
- **共通点(1 行)**:**窓を ℓ(976d の尺度 $4.6(\lambda/10^5)^{1/7}$)の固定倍に取ると、泡の実の半径 $R_*\propto\ell^{1+}$ の前漸近の育ちで縁が泡に飲まれ、悪い事象の確率が λ に一様に O(10⁻³) で止まる —— 窓は泡の実の半径の倍で取らねばならない。**
- **R9**:閉じたのは窓の取り方。571-N の向きは情報の値(979c、判定の後)で、縁を $2\ell$ 以遠・$1.25R_*$ 以遠に置くと局所冪 −1.8〜−4.4 で加速し、Markov の型の遅さではない —— 難しさは「窓の縁を泡の外に置く取り方での再判定」と、真の(相関のある)状態での裾へ移る。
- **射程(T60)**:禁じるのは「窓の半径を ℓ の固定倍(縁 ≤ 1.5ℓ)に取った推定子で 571-N を判定・証明する」発注。止めないもの:窓を $R_*$ の倍(W ≥ 1.25)か $W=\ell^\kappa$ で取った判定文での再判定(結果を見ていない体が判定文を書く)、真の玩具での値。
- **再開条件**:窓の縁を MF の泡の半径 $R_*$ の 1.25 倍以上に置いた判定文が、979c の結果を見ていない体によって起動前に固定されたとき。

## F355(2026-10-22、w_E05_573 = 書き下しの型、稿 `573_hlsの上界_CRの照合_2026-10-22.md` §1・§3、成算 S-E05-R2、C0 980a)定理 572-T の仮定 (CR)(Chen 2008 の赤外の RG を重い合成粒子の参照に移すこと)を、(MS$_\mu$) の (S1)(S3) だけを入力に、元のファイバー(尺度 −1)から Chen の多円板・Prop. 9.6 を写して閉じる方式 —— 閉じたのは**方式**((CR)・標的の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:Chen の RG の 11 段を (a) 尺度の替え /(b) 着衣への置き換え /(c) 移らない に分類し(稿 §1)、(c) の段の要る評価を自然な値と (S1)(S3) からの一般の評価で玩具の値に当てた(C0 980a)。
- **理由**:(1) 尺度 −1 から回すと Prop. 9.6 の (9.81)〜(9.84) は裸の $\partial^2_{\lvert p\rvert}H=1/m$ を使い、誤差 $O(\eta^2)$ が $1/m$ に掛かって曲率 $1/M_\mu$ を覆う —— 尺度 0 から回す必要がある(移せる、(b))。(2) 最初の段の 2 点 —— (S4) 基底の帯の軟らかい応答 $\chi_r(q)$ の q-正則性、(S5) 内部の励起の帯の上の軟らかい結合 —— は (S1)(S3) からの一般の評価で桁で外れる(比 6.8e14〜1.1e27、1.3e5〜3.6e8):源は内部の裸の速さ $\sqrt{E/m}$(格子単位で $\lambda^{6/7}$)で、和則は基底状態の上の 2 次の量しか抑えない(E05-P300 の 572-S)。自然な値(和則・f-和則の型)は閾の内(3.8e-4、2e-2)。
- **閉じたもの**:方式((S1)(S3) だけで最初の段を組むこと、尺度 −1 から Prop. 9.6 を写すこと)。(S4)(S5) を (MS$_\mu$) に足した版の (CR) は開いている。
- **R9**:双極子(内部構造なし)では (S4) 自明・(S5) 空で閉鎖と整合;434-B の病理は (S4)(S5) と両立 —— 再開条件は標的と同値でない。
- **射程(T60)**:禁じるのは「隙間と曲率の下界だけを入力に、合成粒子の内部の励起を通る軟らかい結合を一般の作用素の評価で抑える」形の発注。止めないもの:(S4)(S5) を段 S の仮定に入れた (CR) の組み立て;Chen §8.4・§9.2 の α の追跡(照合)。
- **再開条件**:(S4)(S5) のどちらかを (S1)(S3) と和則から導く道具(内部の励起の状態ごとの f-和則の一様な版、または基底の帯の応答の q-正則性の非摂動の評価)が出たとき。

## F356(2026-10-22、w_E05_571c = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §8.0、成算 S-E05-R1、C0 979e)名指し 571-N の電子の側(泡が電子から窓の半分以上離れる事象)を、557-J2m (iii) の作用素の形 $H(0)\ge(1-\varepsilon')\mathrm{MF}_{\min}+\mathrm{MF}_{\min}\hat B$(余裕 $\mathrm{MF}_{\min}$)と Agmon の恒等式で抑える方式 —— 閉じたのは**方式**(571-N の電子の側は命題 571-F で別の余裕で閉じた)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:Agmon の率を余裕 m から格子の電子の分散 $\cosh k=1+m/\lambda$ で出し、窓の縁 $5R_*$ での上界 $e^{-2k(r_W/2-R_*)}$ を玩具の λ = 1e5〜1e9 に並べた(判定文は worklog §10 に固定)。
- **理由**:余裕 $\mathrm{MF}_{\min}\sim\lambda/\ell^2$ では率 $k\sim\ell^{-1}$(0.64 → 0.18)で、距離 $\sim R_*\propto\ell$ と打ち消し、上界は $e^{-13}$ → $e^{-15}$(局所冪 −0.19・−0.13)で λ に一様な定数に止まる。Agmon の計量の λ の項($\lambda\lvert D_f\rvert^2$、電子の軽さ)に対して、J-G のエネルギーの余裕は $\ell^2$ だけ小さい。
- **共通点(1 行)**:**電子の相対位置の Agmon は余裕 ÷ λ の平方根の率で、余裕が MF の水準なら泡の尺度の距離で O(1) しか稼げない —— 余裕は電子の居る所の局所のポテンシャル(557-P、$\kappa g\sim\lambda\alpha$)から取らねばならない。**
- **R9**:閉じたのは余裕の取り方。標的・571-N の真偽は閉じていない。
- **射程(T60)**:禁じるのは「J-G のエネルギーの余裕($\mathrm{MF}_{\min}$ の定数倍)だけで電子の相対位置の確率の裾を、窓の半径 $O(\ell)$ で超冪に出す」発注。止めないもの:557-P の配位ごとの下界を余裕に使う道(命題 571-F)、窓を $\ell\log\lambda$ 以上に広げる取り方。
- **再開条件**:なし(571-F が上位の方式)。

## F357(2026-10-22、w_E05_573b = 書き下しの型、稿 `573_hlsの上界_CRの照合_2026-10-22.md` §8.2、成算 S-E05-R2)合成粒子の最初の Feshbach の段を、速度ゲージのまま(結合 $-\frac emA_\lt\cdot V$)作用素ノルムで組む方式 —— 仮定を (S1)(S3)(S4) と速度ゲージの形式の評価 (S5) に限る場合;閉じたのは**方式**(最初の段・(CR)・標的の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:ファイバーごとの自由部分 $H_0=K^\mu_{p-P_f^\lt}+H_f^\lt$(下界は補題 573-H で立つ)に対し、$W=-\frac e{2m}\lbrace A_\lt,V\rbrace+\frac{e^2}{2m}A_\lt^2$ の相対の評価(BCFS (11.25)・(11.31)〜(11.32) の型)を当てた。
- **理由**:(a) 一般の評価は $\lVert V\Phi\rVert^2\le2m\langle K\rangle$ の $E^\mu$ の項で相対 $\sqrt\alpha(2E/m)^{1/2}$(980a:1.3e5〜3.6e8)。(b) (S5) を $\lvert V/m\rvert\le D(K-E)$ の形にしても、ファイバーのずれ $-k\cdot V/m$ と、内部の励起 × 多光子の積 $H_f^{1/2}(K-E)^{1/2}$ の項が残り、相対の大きさは $D\sqrt\alpha\mu^{1/2}\sup\sqrt{\min(x,h)}$ で有界でない。(c) 帯で縮めた曲率に $\frac2{m^2}(\tilde\chi_0-\tilde\chi_h)\le h/(m\rho\mu)$ の裸の大きさの項が残り、$1/M_\mu$ を桁で越える。源は 1 つ:速度ゲージの内部の行列要素が $(E_i-E_j)\times$ 双極子で、エネルギー差の因子が大きい。
- **閉じたもの**:方式(速度ゲージ + (S5) での最初の段)。長さゲージの分解 (LG)(稿 §8.3)の下では組める(補題 573-F、self-audited)。
- **R9**:双極子模型では d = 0 で速度ゲージと長さゲージが一致し、閉鎖と整合;2 構造の梯子は擬交差の接続で (LG) の D が爆発 —— 再開条件は標的と同値でない。
- **射程(T60)**:禁じるのは「合成粒子の内部の励起を通る軟らかい結合を、速度ゲージのまま形式の評価で抑えて Feshbach の対を立てる」形の発注。止めないもの:(LG) の下の組み立て、(LG) の真偽の偵察。
- **再開条件**:LLP のファイバーで $V_q/m$ の内部の行列要素を $(E_i-E_j)\times$(有界な量)の形でなく抑える別の道具(例:内部の励起の帯ごとの一様な f-和則と、多光子の積の項を消す正値性)が出たとき。

## F358(2026-10-22、w_E05_571d = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §9.1、成算 S-E05-R1、C0 979f)名指し 571-N2(場の側:窓の縁に非真空的な集合が在る確率 ≤ C/(λr_W²))を、**粗視化の尺度 b を ℓ に依らず固定**(b = 4)した非真空的な集合で当てる方式 —— 閉じたのは**方式**(571-N2 は b ∝ ℓ で N2_GO)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:玩具の Gauss の積の状態で、窓 $5R_*$ の縁の殻に辺 b の非真空的な立方体が在る確率を λ = 1e5〜1e9 に並べた(判定文は worklog §13 に固定)。
- **理由**:1 つの立方体の偽の窪みの確率 $p_b$ = 7.1e-10 は λ に依らず、殻の立方体の数が $R_*^2$ で育つので、確率は上界・下界とも局所冪 +0.30 で**育つ**(目標は −1.30)。
- **共通点(1 行)**:**粗視化の尺度を固定すると、真空の 1 立方体の大偏差の確率が λ に一様で、窓の面積の育ちが勝つ —— 尺度は ℓ とともに育てねばならない(b ∝ ℓ で $3b^3$ 自由度の大偏差が超冪)。**
- **R9**:閉じたのは粗視化の尺度の取り方。571-N2 の真偽は閉じていない(b = ℓ/2 で GO)。
- **射程(T60)**:禁じるのは「ℓ に依らない粗視化の尺度で 571-N2 を判定・証明する」発注。止めないもの:b ∝ ℓ(または $b\sim\varepsilon_{\rm JG}^{1/3}\ell$)の推定子。
- **再開条件**:なし(b ∝ ℓ が上位の方式)。

## F359(2026-10-22、w_E05_573c = 書き下しの型、稿 `573_hlsの上界_CRの照合_2026-10-22.md` §14.6・§15、成算 S-E05-R2)合成粒子の最初の Feshbach の段の出力に、Chen 2008・BCFS 2007 の**厳密な**軟らかい光子の和則 SR[σ](Chen (7.86)、BCFS (11.14)〜(11.16))を立て、Chen の多円板 $\mathcal U^{\rm sym}$ に字面どおり入れる方式 —— 閉じたのは**方式**((ASR)・572-T′・標的の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:長さゲージの $UH^\sigma(p)U^*$ を帯の射影 $\chi=\Pi_{p-P_f}\otimes\chi_1[H_f^\lt]$ で Feshbach に縮め、和則の各段を照合した(補題 573-SR)。
- **理由**:BCFS §8 の冒頭の注のとおり、和則の保存が「純粋に代数」なのは切断の作用素が $P_f$ に依らないとき。合成粒子の帯の射影は $P_f$ に依り、(i) BCFS (8.4)(8.5) の $P_f$-微分が $\partial_q\Pi$ の項(光子の挿入で表されない)を生む —— 相対 $2\mu D_\mu$;(ii) 2 段目の極限はスペクトルのパラメタ z に依り z = E でだけ一致 —— 相対 $2\mu D_\mu^2M_\mu$。1 段目は軟らかい光子の無い部分で厳密(Feynman–Hellmann)。ゲージ共変な射影 $\Pi_{p-P_f-eA}$ は成分の非可換で定義できず、$P_f$ に依らない切断では内部の隙間を使えない。
- **閉じたもの**:方式(厳密な和則)。近似の和則の下の版 (ASR)(稿 §15)は開いている。
- **R9**:双極子模型(内部構造なし)では帯の射影が不要で違反 0 —— 閉鎖と整合;違反は (LG) の D に比例し、標的(質量)に触れない。
- **射程(T60)**:禁じるのは「$P_f$ に依る帯の射影を含む最初の段の出力に、厳密な和則を前提とする Chen・BCFS の定理を字面どおり当てる」形。止めないもの:(ASR) の証明(BCFS §8 の代数に違反の核の評価を重ねる)。
- **再開条件**:ゲージ共変な帯の射影(零モードの移動と運動量の移動が一致する射影)を作る道具か、近似の和則の下の Chen の縮小の定理が文献か在庫に出たとき。

## F360(2026-10-22、w_E05_571e = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §9.3・§10、成算 S-E05-R1、C0 979g)消費者の E5($\langle C_f\rangle\le C$)と場の側 571-N2 を、**θ の閾の重みだけの 1 層の推定子**(557 の $\hat h$ の重心)で、ℓ に依らない c_θ のまま両立させる方式 —— 閉じたのは**方式**(2 層の推定子で両立 —— E5_GO)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:玩具の Gauss の積の状態で、1 層の推定子の $\langle C_f\rangle$ を c_θ = 1・ℓ^{-1/2}・ℓ^{-1} で λ = 1e5〜1e9 に並べた(判定文は worklog §16 に固定)。
- **理由**:c_θ = 1 で $\langle C_f\rangle$ = 0.34 → 2.85(局所冪 +0.19・+0.17)と育つ;O(1) には c_θ を ℓ の負の冪(玩具で $\lesssim\ell^{-0.75}$)に下げねばならず、証明の側の場の余裕 $c_\theta\gtrsim8\varepsilon_{\rm JG}$ と合わせると J-G の精度の床 $\varepsilon_{\rm JG}\lesssim\ell^{-0.75}$ 程度に戻る(§9.3)。
- **共通点(1 行)**:**同じ閾の汎関数に「C_f を小さく(閾を緩く)」と「偽の窪みの余裕を大きく(閾を鋭く)」の逆向きの要求を課すと、両立は J-G の精度に戻る —— 重みと破れの判定を別の層に分ければ外れる。**
- **R9**:閉じたのは推定子の 1 層の作り方。E5・571-N2・標的の真偽は閉じていない。
- **射程(T60)**:禁じるのは「θ の閾の重みの重心(1 層)で、c_θ を ℓ に依らず止めたまま $\langle C_f\rangle\le C$ を示す」発注。止めないもの:2 層の推定子(壁の勾配の核の重み + θ の閾の判定)、c_θ を ℓ の冪で下げた 1 層(J-G の精度の要求と引き換え)。
- **再開条件**:なし(2 層が上位の方式)。

## F361(2026-10-22、w_E05_573d = 書き下しの型、稿 `573_hlsの上界_CRの照合_2026-10-22.md` 第 4 部 §17・§18、成算 S-E05-R2、C0 980b)近似の和則の下の Chen の RG (ASR) を、和則の違反の核の**段ごとの norm の漸化式**($\lVert\hat\Delta_1\rVert\le(1+C\eta/\rho)\lVert\Delta_1\rVert+C\rho\lVert\Delta_{\ge2}\rVert$ の型)で閉じる方式 —— 閉じたのは**方式**((ASR) は補題 573-A で別の形に閉じた、self-audited)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:BCFS §8 の代数で違反の運搬を書き、Chen §8.4 の norm の評価を違反の核に当てた;1 ループの段の写像で違反の倍率を測った(C0 980b)。
- **理由**:粗い norm の評価では 1 段目の違反の倍率が $1+C\eta/\rho$ で、周辺の領域の段数 $N(\sigma_0)\sim\log(1/\sigma_0)$ にわたって $\sigma_0^{-C\eta/(\rho\log(1/\rho))}$ に増え、σ₀ に一様でない。1 ループの値では増大は $1+O(\lambda_ng^2)$(Ward の恒等式の相殺で周辺の項が消える)で和が収束 —— 段ごとの評価は相殺を見ない。
- **閉じたもの**:方式(段ごとの漸化式)。尺度 0 への集約(Chen Lemma 9.1・BCFS Lemma 15.2・15.5 の型)で違反を直接表す形(補題 573-A)は開いて閉じた(self-audited)。
- **R9**:双極子模型(違反 0)では漸化式も集約も自明;方式の閉鎖は標的に触れない。
- **射程(T60)**:禁じるのは「周辺の違反を段ごとの norm の漸化式で σ₀ に一様に抑える」形。止めないもの:集約の形の評価、1 ループの値。
- **再開条件**:なし(集約の形で閉じた)。

## F362(2026-10-22、w_E05_571f = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §11.4、成算 S-E05-R1、C0 979h)消費者の E5 に要る壁の勾配の量の下界 $`G=\sum\partial k\,m_c(u')\gtrsim M_{\rm sq}`$(良い集合の上)を、**エネルギーの比較(J-G の下界 + Markov、または Agmon)**で出す方式 —— 閉じたのは**方式**(G の下界・E5 の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:玩具(976d の MF)で、σ の輪郭を半径方向にぼかして G を半分にしたときの場の Gauss のエネルギーの増え ΔE を $\mathrm{MF}_{\min}$ と比べた(判定文は worklog §18)。
- **理由**:$\Delta E/\mathrm{MF}_{\min}$ = 0.090 → 0.0080(λ = 1e5〜1e9、局所冪 −0.30・−0.38)—— 壁の形は MF の小さく縮む割合しか担わず、J-G の余裕 $\varepsilon_{\rm JG}\mathrm{MF}_{\min}$(在庫の窓で $\varepsilon\ge\ell^{-1/20}$、構造の床 $\ell^{-1/2}$)より桁で小さい。Markov の上界は 1 を越え、Agmon の余裕は負。
- **共通点(1 行)**:**壁の形(面積の桁の量)をエネルギーで捉えるには、MF に対する相対の精度 $\sim\lambda^{-0.3}$ が要る —— 全体のエネルギーの J-G の精度では見えない;局所の(手術による)比較で J-G を通らずに言う道が残る。**
- **R9**:閉じたのは方式(エネルギーの全体の比較)。
- **射程(T60)**:禁じるのは「J-G の下界(MF の精度)とエネルギーの比較だけで、壁の勾配の量 G の下界やその確率を出す」発注。止めないもの:局所の変分(外の殻の場を真空に替える手術と継ぎ目の評価)、決定的な等周(帯の核)と外の殻の真空性の組。
- **再開条件**:J-G の精度 $\varepsilon_{\rm JG}\ll\lambda^{-0.4}$ のエネルギーの下界が在庫に載ったとき。

## F363(2026-10-22、w_E05_571g = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §12.3、成算 S-E05-R1、C0 979i)名指し 571-N3 の道 3(局所の手術)を、**殻の両面で切る手術**と、面の近くの ψ の局所のエネルギーの在庫の評価(554-J1 の $\langle\int_R{:}\lvert E\rvert^2{:}\rangle\le\varepsilon_{\rm J1}\mathrm{MF}+\dots$ を面の位置で平均)で閉じる方式 —— 閉じたのは**方式**(1 枚の面と微分不等式の道は開いている)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:真の状態の継ぎ目の費用を、面の近くの局所のエネルギーで上から押さえ、面の位置を帯(幅 w)で平均する算術。
- **理由**:帯の局所のエネルギーは在庫で $\lesssim\varepsilon_{\rm J1}\mathrm{MF}_{\min}\sim\varepsilon\ell^5$、平均の面の費用は $\varepsilon\ell^5/w\sim\varepsilon\ell^4$($w\sim\ell$)で、殻の利得(面積 × 厚さ $\sim\ell^2\cdot\ell$)を ε ℓ の因子で越える —— J-G の精度が面の費用に入り直す。〔玩具の Gauss の値(C0 979i)では継ぎ目の費用は面積あたり 0.018 と小さいが、それは ψ が面の近くで真空的であることを前提にした値。〕
- **共通点(1 行)**:**面の費用を全体のエネルギーの在庫の評価で押さえると J-G の精度が戻る —— 面を 1 枚にし、面の近くのエネルギーを利得の側に吸収する微分不等式(外のエネルギーの減衰)で閉じる。**
- **R9**:閉じたのは継ぎ目の費用の評価の型。571-N3・E5 の真偽は閉じていない。
- **射程(T60)**:禁じるのは「両面の手術と 554-J1 の型の局所のエネルギーの評価だけで外の殻の真空性を出す」発注。止めないもの:1 枚の面の手術と面の半径についての微分不等式(稿 §12.3 の U1〜U7)。
- **再開条件**:なし(U1〜U7 が上位の方式)。

## F364(2026-10-22、w_E05_571i = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §14.1、成算 S-E05-R1)名指し 571-N3(G の門の失敗の重み $\langle C_f(X_\theta)1\lbrace\Gamma_G^c\rbrace\rangle\le C$)を、外の殻の強く窪んだブロックの割合の **Markov の裾**(Hardy 557-H、補題 571-U6′)と等周(帯の核)で出す方式 —— 閉じたのは**方式**(指数の裾の Agmon の道は開いている)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:窪みの閾 $`c\,u'_{\rm vac}`$ について、G の門の下界 $G_0\sim c$、帯の核の主の項 $C_f\lesssim c^{-2}/r_{\rm in}$、Markov の $P(\Gamma_G^c)\lesssim c$、1 層の $C_f(X_\theta)\sim\ell^{1.2}$(玩具、c_θ = 1)の指数の帳簿。
- **理由**:主の項が O(1) には $c\gtrsim\ell^{-1/2}$、失敗の重みが O(1) には $c\lesssim\ell^{-1.2}$ —— 窓が空。c_θ を下げて 1 層の冪を下げると §9.3 の J-G の精度の床に戻る。
- **共通点(1 行)**:**裾を窪みの閾に比例する Markov で取ると、門の下界の閾と同じ c を両側から引き合い窓が空になる —— 裾は指数(Agmon)で取らねばならない。**
- **R9**:閉じたのは裾の型。571-N3 の真偽は閉じていない。
- **射程(T60)**:禁じるのは「1 次の積率の型(Markov・Chebyshev)の裾だけで G の門の失敗の重みを抑える」発注。止めないもの:手術の作用素の不等式(571-S0)を配位の下界にした Agmon(稿 §14.5)。
- **再開条件**:1 層の $C_f(X_\theta)$ の育ちが $\ell^{1/2}$ 未満に下がる推定子(J-G の精度の床に戻らずに)が見つかったとき。

## F365(2026-10-22、w_E05_571j = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §15、成算 S-E05-R1、C0 979l・979l2)名指し 571-S の第 2 の条項(手術の作用素の不等式 571-S0 の電子の項 El)を、**外のモードの電子の箱への漏れの作用素のノルムが距離 D で減衰すること**($\lambda\alpha\lVert1_{\Lambda_e}P_{W_{\rm ext}}\rVert^2\le Ce^{-cD}$ または冪)で抑える方式 —— 閉じたのは**方式**(El の期待値の大きさ $\lambda\alpha/D^2$ の型と、571-S の交換子の条項は開いている)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:格子の横波の自由場で漏れの作用素のノルムを D に並べ(979l、N⊥ = 12 で指数)、横の格子の大きさを替えて確かめた(979l2)。
- **理由**:漏れは各横の運動量 $k_\perp$ で $e^{-2k_\perp D}$(横波の射影の縦の部分の核)で、N⊥ = 12・24・48 で D = 50 の値が 1.9e-23・1.4e-12・4.0e-7 と横の格子の最小 $2\pi/N_\perp$ に支配される —— 無限の平面では $k_\perp\lesssim1/D$ のモードの漏れが O(1) で、作用素のノルムは D で減衰しない。
- **共通点(1 行)**:**横波の射影の縦の部分は面に沿う長波で面を越えて広がる —— 作用素のノルムの局在は無い;在るのは面積あたりの HS($\sim D^{-2}$)と、真空の期待値の水準の $\langle A_{\rm e}^2\rangle\sim D^{-2}$ だけ。**
- **R9**:閉じたのは El の評価の型。571-S・571-N3 の真偽は閉じていない。
- **射程(T60)**:禁じるのは「漏れの作用素のノルムの D での減衰」を前提にする El の評価。止めないもの:$\mathrm{El}\le\eta T_{\rm el}+\frac{\lambda\alpha}\eta A_{\rm e}(0)^2+c$ と $A_{\rm e}(0)$ の大偏差の評価、窓 $K\ell\log\lambda$。
- **再開条件**:なし(上の止めない道が上位)。

## F366(2026-10-22、w_E05_576 = 書き下しの型、稿 `577_hlsの上界_最初の段の書き直し_2026-10-22.md` §2、監査 575 §2、成算 S-E05-R2)$h_{\rm ls}$ の上界の条件付き定理の最初の段を、長さゲージの分解 (LG) だけ(切らない生成子 $X=-\frac e2\lbrace A_\lt,d\rbrace$)で、U の全ての次数と反跳を (LG) の d・Γ の大きさで抑えて閉じる方式(稿 573 第 2 部 573-F (ii)・573-W)—— 閉じたのは**方式**(最初の段・572-T‴・標的の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:573-W で M+N ≥ 2 の核を $(\mathrm{ad}_d)^nK$ の入れ子で書き、$\lVert\bar R^{1/2}[d,[K,d]]\bar R^{1/2}\rVert\le4D^2$ と $\sqrt\alpha\mu^{1/2}D$ の冪級数で抑えた。
- **理由**(合同 S2 575 の判定を著者の側で確認):消した 1 次の裸の速さ $[K,d]=-i(V/m-\Gamma)$ が、(G1) U の 2 次では TRK の組 $B=\delta/m-[d,[K,d]]$(作用素ノルムが要る;(LG) に無い)、(G2) 反跳では磁気双極子型 $\mathcal M_k$(相対 $c_Lv_{\rm bare}=\gamma_V$)、(G3) 3 次以上では軟らかい場の n 次の多項式(切らないと $H_0$ に形式有界でない)の形で戻る。$4D^2$ の評価は「d が K の形式の領域を O(D) で保つ」ことを暗に使い、A-575-1(f-和則)がそれを否定する。
- **閉じたもの**:方式((LG) だけ、切らない生成子)。(LG-2) を足し生成子を $H_f^\lt\lesssim K_g\alpha v_{\rm bare}^2\mu$ で切る設計(補題 577-F)は開いて閉じた(self-audited)。
- **R9**:双極子模型(d = 0)では切っても切らなくても同じで閉鎖と整合;原子型($d=x$)では B = 0 で (G1)(G3) が消える —— 障害は内部の励起の TRK の和 1/m に固有。
- **射程(T60)**:禁じるのは「長さゲージの生成子を切らずに、d・Γ の大きさだけで U の全ての次数と反跳を抑える」形。止めないもの:577-F の設計の写しの照合。
- **再開条件**:なし(577-F で置き換えた)。

## F367(2026-10-22、w_E05_571k = 書き下しの型、稿 `571_難問1_族E2p_計画1の消費者の冪の率_2026-10-22.md` §16、判定文 = 記録 `576_判定文_571SのEl_2026-10-22.md`、成算 S-E05-R1、C0 979m)名指し 571-S の第 2 条項(El)を、571 §14.5 の設計のまま(外の領域 = 電子の箱から距離 ≥ D の全て)作用素の形式の水準で吸収する方式(記録 576 §1.2 の割り方:$\mathrm{El}\le2\eta T_{\rm el}+\frac{3\lambda\alpha}{4\eta}A_{\rm e}^2+\dots$、$A_{\rm e}^2\le4L_2(H_{\rm ee}-E_0)+2L_1$)—— 閉じたのは**方式**(571-N3・標的の真偽は閉じていない)

親(G3 第 73 陣)が連結 2026-10-21
- **何を試したか**:記録 576 §4・§5 の判定文(結果を見ていない 監査の型 が固定)を字面どおりに、格子の横波の自由場(質量 0、両側の平板、横と法線を同時に倍)で当てた。
- **理由**:吸収の係数 $L_2^*$(外の部分空間の箱の点の ω⁻² の重み)が N の倍ごとに 1.53〜1.61 倍・1.26〜1.30 倍と育ち(D = 4・8・16・32)、赤外の発散の印(規則 2)—— 札 El_NOGO_IR。定数 $L_1^*$ は収束の向きだが距離の局所冪 2.1 で、消費者の要る 5 に遠い。読み:TM の漏れ $e^{-2k_\perp D}$ と $\Omega_{\rm ee}\sim k_\perp$ で $L_2\sim\int d^2k_\perp e^{-2k_\perp D}/k_\perp^2$ が 2 次元の赤外で対数に発散。 〔訂正注記 2026-10-22 w_E05_591(稿 `591_` §6・§9、NUM-7633・断片 w_E05_591b.NUM):979m の核 `per_kperp` の縮約 `conj(Q[rows])@W` は $W^Tc$ で誤り、正しくは $W^\dagger c$。正しい値は $L_1^*$・$L_2^*$ ともおよそ半分(例 D = 8、N = 32D:$L_1^*$ 6.00e-5、$L_2^*$ 6.41e-4)で、$L_2^*$ の倍の比 32D/16D は 1.385・1.419、16D/8D は 2.07〜2.17 —— 赤外の発散の印は保たれ、札 El_NOGO_IR と結論は変わらない。〕
- **共通点(1 行)**:**外の領域を電子から距離 D の全空間に取ると、面に沿う長波の横波($k_\perp\lesssim1/D$)が外の部分空間に入り、電子の運動量との結合(慣性の物理)を ω⁻² の重みで持ち込む —— El は Hardy の余裕に吸収できない。**
- **R9**:閉じたのは El の吸収の型(外の領域の取り方と組で)。手術の作用素の不等式 571-S0 そのもの、571-N3・標的の真偽は閉じていない。〔注 2026-10-22 audit_S2_590_592(監査 `596_` §4 (b)、F375):値は格子の点の評価(裾なし)の模型;公理表の連続の鋭い切断では帯域の縁の裾 $\cos(\pi r)/r^2$ が $L_s$ に赤外に育たない $D^{-1}$ を足し、$L_1$ の冪は 2.1 → ≈ 1 —— 札 El_NOGO_IR(長波の赤外の育ちは連続にも在る物理)と閉じたものは不変、閉鎖の向きは強まる。〕
- **射程(T60)**:禁じるのは「§14.5 の外の領域(電子から距離 ≥ D の全て)のまま、El を作用素の形式の水準で吸収する」発注。止めないもの:記録 576 §5.3 の組み替え(外の領域を有界な殻に取る・長さゲージで長波を先に外す・D を ℓ より速く育てる)、大偏差の水準(真の状態の $A_{\rm e}(0)$ の裾の補題)。
- **再開条件**:外の領域の取り方を替えた設計で、$L_2^*$ が N の倍で 10% 以内に収まる判定文が別に固定されたとき。

## F368(2026-10-22、w_E05_592 = 書き下しの型、稿 `592_難問1_ιの正の側_G-SH_G-BO_G-BR_2026-10-22.md` §1、判定文 = worklog (研究ノート: `2026-10-22_w_E05_592.md`) §1(C0 の前に固定)、成算 S-E05-R1、C0 992a)El の吸収の冪を、571 §14.5 の外の領域を有界な殻 $[D,R_{\rm out}]$ に替えて上げる方式(稿 590 §2.2 の G-SH)—— 閉じたのは**方式**(札 BOUNDED(暫定)、El の赤外は切れるが冪が上がらない)
- **何を試したか**:記録 576 §2.4 の量 $L_1^*$・$L_2^*$ を、両側の平板・質量 0 で外を殻 $\lbrace D/2+D\le\lvert z\rvert\le D/2+\rho D\rbrace$(ρ = 2)に替えて、N = 8D・16D・32D、D = 4・8・16 で。対照:射影なし(K1)と半空間(979m を相対 0 で再現)。
- **理由**:赤外は殻で切れる(N の倍で $L_1$ 1.0013・$L_2$ 1.0021;半空間は 1.26〜1.30)が、距離の局所冪は $p_1$ = 2.48 → 2.37・$p_2$ = 1.75 → 1.52(尺度の不変性の 2・1 へ減速)で、$\gamma_{\rm req}$ = 2.55(漸近 2.875)〔訂正注記 2026-10-22 audit_S2_590_592(監査 `596_` §2、C0 996a):992a は 979m の縮約の誤り $W^Tc$ を流用していた;正しい $W^\dagger c$ で IR の比 ≤ 1.0031・1.0046、$p_1$ = 2.30・2.03、$p_2$ = 1.55・1.21、$\gamma_{\rm req}$ = 2.73 —— 札 BOUNDED・閉じたもの・共通点は不変。連続の鋭い切断の模型では帯域の縁の裾で冪 ≈ 1(閉鎖の向きは強まる)。〕—— 要る距離 $D\sim\ell^{2.5\sim2.9}$ は 571 の鎖の窓 $D\le K\ell\log\lambda$ の外。継ぎ目の真空の分は面 1 枚・面積あたり 0.0268 で有限(N・D に依らない)。
- **共通点(1 行)**:**El の障害は赤外の対数でなく尺度の不変性の冪(長さが D だけなら $L_1\propto D^{-2}$・$L_2\propto D^{-1}$)で、外の領域の取り方では冪が変わらない —— 冪を変えるのはゲージ(一様な部分・勾配の部分の消去)だけ。**
- **R9**:閉じたのは El の吸収の型(外の領域の取り方と組)。571-S0・571-N3・標的の真偽は閉じていない。
- **射程(T60)**:禁じるのは「外の領域の形(殻・半空間・距離)だけを替えて El の吸収の冪を上げる」発注。止めないもの:殻を G-LG(長さゲージ)・592-B3(BO の上の手術)と組んで IR の対数を外す補助;窓 $\ell^{\gamma}$ を許す鎖の構成(G-LG の (i) と共通)。
- **再開条件**:571 の鎖(571-N2・E5・G の門)が窓 $r_W\ge\ell^{2.9}$ で成ると示されたとき(そのとき G-SH は G-LG の代替の 1 つとして BOUNDED → 再判定)。

## F369(2026-10-22、w_E05_592 = 書き下しの型、稿 `592_` §2.1〜§2.2、成算 S-E05-R1)稿 590 §2.2 の行 4(G-BO):「Born–Oppenheimer の配位ごとの下界で、571-F(電子の側の超冪)を手術なしで再導出する」—— 閉じたのは**標的**(既に成っている)
- **理由**:命題 571-F(E05-P302)は 571-D を 571-E の $V=\kappa\hat g$ で当てたもので、571-E (a) = 557-P(E05-P294)は「配位ごとの下界を q ごとの電子に当て」る BO の型(433-B、E05-P225)—— **571-F はもともと手術を使っていない**。外の殻の窪みには BO は効かない:補題 592-B2 で El は消えるが内の場のエネルギー(泡の費用、MF の O(1) の割合)を捨て、取り戻すには精度 $m_H/\mathrm{MF}\sim\ell^{-1.5}$(J-G の精度の床より細かい)が要る。
- **共通点(1 行)**:**BO は電子の側の余裕 λα を配位の掛け算で与えるが、場だけの費用(殻の窪み・泡の費用)を局在した掛け算に直す段には触れない —— それは手術(または J-G の精度)の仕事。**
- **R9**:閉じたのは標的の字面(新しい内容が無い)。BO の上の手術(補題 592-B3、El をゲージ不変な掛け算に替える)は別の角度として生きている(稿 §2.5、BOUNDED の値)。
- **射程(T60)**:禁じるのは「BO の下界だけで (D-i) を作り、外の殻の窪みを払う」発注。止めないもの:592-B3 を G-LG の LG-1(長さゲージの段)・G-LD の LD-1 の代替に使う道。
- **再開条件**:なし(標的が空)。

## F370(2026-10-22、w_E05_592 = 書き下しの型、稿 `592_` §3、成算 S-E05-R1)稿 590 §2.2 の行 6(G-BR):F341 の再開条件「赤外の光子を重みで消した可換な観測量の族」で、Brooks の正則化した中央値を窓なしの推定子にし $v=0$ を厳密に得る方式 —— 閉じたのは**方式**
- **理由**:571-C・501-X の消費者は A と可換な(場の配位の)推定子を要る。この意味の可換な族で一様な長波を消すものは在庫の $g(y;A)$(557 の $u'_Q$、571-E・571-F)で、F341 の再開条件の字面はこれで満たされる。しかし真空の下で非真空的な集合 $\lbrace g\le t\rbrace$ は正の密度を持ち(観察 592-R)、全空間の分位点は定義されない —— 窓が要り、$v\gt0$ で集中 571-N(= 571-F + 571-N2)に戻る。非可換な族(光子数・占有数、真空は静か)は $[\hat X,A(0)]\ne0$ が λ 倍の交差を作り、F341 の閉鎖の理由(軟らかい光子)に戻る。
- **共通点(1 行)**:**窓なしの並進共変な推定子は、可換な族では真空の揺らぎの正の密度で、非可換な族では λ 倍の交差で作れない —— どちらも集中の補題(571-N2 か光子の集中)に戻る。**
- **R9**:閉じたのは方式。571-N・標的の真偽は閉じていない。
- **射程(T60)**:禁じるのは「Brooks の中央値の型の窓なしの推定子で $v=0$ を厳密に得る」発注。止めないもの:窓つきの $g$ の推定子(族 E-2′-b′、571-N2)。
- **再開条件**:F341 の再開条件は「可換」を A との可換に読めば満たされた(在庫の $g$)。G-BR として再開するのは、真空の非真空的な集合の密度が 0 になる閾(全空間で有限の質量)を持つ配位の汎関数が見つかったとき —— Gauss の真空では不可能(592-R)なので、実質的に再開しない。

- **F370 への追記**(2026-10-22、w_E05_623_brooks、稿 `623_…` §3.1・§5)
- 前半(可換な族 = Q 空間の推定子で v = 0)は**補題 623-E(E05-P?、self-audited)で厳密**:Q 空間の並進はエルゴード的で、厳密に共変な可測な推定子は Fock の全てのベクトルの測度で零集合の上にしか無く、非定数の並進不変な局在も無い(系 623-E′:Q 空間の局在は λ 倍の反跳の項を必ず払う)。後半(非可換な族の λ 倍の交差)は玩具の値で向きが当、定数は小さい:全ての光子の位置の平均の対の位相のずれの費用 $K_A\approx0.043\ell$(C0 a623a、λ = 1e5〜1e9 で 0.22〜0.57、1 を越えるのは λ ≈ 1e11、a623b)。費用を O(1) に保つ低密度の帯の選びは悪い集合の強圧性を $\ell^{-2.8\sim-3.2}$ に落とす(a623b、判定の後の情報)—— 壁の精度の難しさは強圧性の側に戻る。

## F371(2026-10-22、w_E05_590b = 書き下しの型、稿 `590_難問1_ιの正の側_El後の設計のやり直し_2026-10-22.md` §3〜§5、判定文 = worklog (研究ノート: `2026-10-22_w_E05_590.md`) §2(590b)、成算 S-E05-R1、C0 990a)候補 G-LG(箱の模型の手術に長さゲージ $U=e^{i\sqrt\alpha x\cdot A_{\rm e}(0)}$ を当て、外の殻を $D=\ell^{\gamma}$、$\gamma\approx2.25$ に出して El を吸収する設計)—— 閉じたのは**方式**(G-LG の殻 × 帯が泡に接する G の門の組;量は格子の模型で通る。2026-10-22 audit_S2_590_592 で「標的」から訂正 —— G の門の核を替えた形は F373 で別に閉じた)
- **値(C0 990a、値【T88】)**:長さゲージの後の El の重み $L_s^{\rm rem}$(差 $g_x-g_0$ の ω⁻ˢ の重み)は平板の外(F367 と同じ 2 次元の赤外)で赤外に有限(N の倍の比 ≤ 1.005)、距離の局所冪 $p_1$ = 3.78・3.89、$p_2$ = 2.89・2.94、$\gamma_{\rm req}$ = 2.22(μ → 0)〜2.38(μ = 1/3)—— 量 (ii) は通る;対照(ゲージなし)は El_NOGO_IR を再現。〔訂正注記 2026-10-22 audit_S2_590_592(監査 `596_` §1.5・§2):990a は 979m の縮約の誤りを含み、990a2(NUM-7644)で $\gamma_{\rm req}$ = 2.22〜2.43(札不変)。「量 (ii) は通る」は格子の点の評価(裾なし)の値 —— 公理表の連続の鋭い切断では帯域の縁の裾 $\cos(\pi r)/r^2$ が長さゲージで消えず $L_s^{\rm rem}\sim D^{-1}$、576 (B6) で量の段から閉じる(閉鎖の向きは強まる)。〕
- **閉じた理由(字面と冪の勘定)**:571 §14.5 の Agmon が制御すべき殻は G の門(571 §11.4 道 2・§14.1、571-H)の核の帯で、芯(泡)との対比を作るために泡の壁に接する($r_{\rm in}\sim R_*\sim\ell$)。帯を $D=\ell^{\gamma}$ に退けると対比が $(R_*/r_{\rm in})^3$ に薄まり E5 の $\langle C_f\rangle\le C$ が $r_{\rm in}\lesssim\ell^{6/5}$ を要る —— $\gamma_{\max}\le1.2\lt\gamma_{\rm req}$。殻 $[D,2D]$ は消費者の要る領域を覆わない。
- **共通点(1 行)**:**El を払える距離(D ≫ ℓ)と、消費者(G の門)が制御を要る領域(泡に接する帯)が離れている —— 手術の外は電子の慣性を担う泡の場を含まねばならない。**
- **R9**:閉じたのは G-LG の標的の置き方(殻を遠くに出す)。長さゲージそのもの(稿 590 §3.1:El の一様な部分は λ の外に出て、残りは赤外で有限)・571-N3・標的の真偽は閉じていない。
- **射程(T60)**:禁じるのは「殻を $D\gg\ell$ に出して El を払い、G の門(泡に接する帯)の失敗をその殻で制御する」発注。止めないもの:G の門を替える設計(稿 590 §5.2 の筒の核 —— ただし値で閉、次の項)、手術を使わない消費者。
- **再開条件**:消費者の側で、制御の要る領域が泡から $\ell^{2.25}$ 以上離れた G の門(または E5 を通る別の推定子)が書けたとき。

## F372(2026-10-22、w_E05_590b = 書き下しの型、稿 `590_…` §4 末尾・§6 R4、値)571 §14.5 の箱の模型の手術の Agmon(571-S0 + 571-U6′ + 571-E の IMS)の幾何と IMS の両立 —— 閉じたのは**方式**(値の冪の勘定;El と独立)
- **勘定**:(D-ii) の余裕は F の立ち上がりの上で Hardy だけ(記録 576 (B2)):$m_H\sim\rho_{\rm m}r_{\rm in}^3/c$。571-E (b) の $c_0\ni C_{\rm IMS}\lambda/n_e^2$($\lambda=\alpha\ell^7$)と、殻 ⊂ 外(電子の箱から距離 ≥ D)の $n_e\lesssim r_{\rm in}$ で $r_{\rm in}\gtrsim(c\alpha\ell^7/\rho_{\rm m})^{1/5}\sim\ell^{7/5}c^{1/5}$;G の門の対比(前項)で $r_{\rm in}\lesssim\ell^{6/5}c^{2/5}$ —— $c\le1$ で空(隔たり $\ell^{1/5}$)。El = 0 としても成る。〔射程の訂正 2026-10-22 audit_S2_590_592(監査 `596_` §1):「El と独立」は G の門の核が泡に接する帯(双極子の帯・max 核)のときだけ。筒の核 G-TK では El = 0 なら IMS と E5 の窓 $D\in(\ell^{5/3}c^{1/3},\ell^2c^2]$(c ≳ ℓ^{-1/5})が開き、G-TK を閉じたのは El(F373・F375)—— 本行は手術の族の標的の閉鎖ではない。集団座標の IMS(監査 §1.4)も本行の射程の外(再開条件の「IMS を使わずにファイバーへ運ぶ道」の 1 つ)。〕
- **読み**:576 §3.1 の「$n_e=M\ell$ は D($\le r_{\rm in}\sim\ell$)と同じか大きい」は、辺 $M\ell$ の箱が帯を内に含み外に帯が残らない点を見ていない。E_box − E は IMS の損を打ち消さない(重い複合体の重心の閉じ込めは $\sim1/(Mn_e^2)$、IMS の損は裸の電子の $\lambda/n_e^2$)。
- **R9**:閉じたのは箱の模型で手術して IMS でファイバーへ戻す組み立て(571 §14.5 段 1)。571-S0 の作用素の不等式そのもの・571-N3 の真偽は閉じていない。候補表(稿 590 §2.2)の行 1・3・7 と、箱の模型の手術を使う限り行 2 に効く。
- **射程(T60)**:禁じるのは「Hardy の余裕だけで、箱の模型の IMS の損 $\lambda/n_e^2$ を払う」発注。止めないもの:泡に相対の手術(分解が配位に依る —— 費用は未検)、電子の側の余裕($\kappa\hat g\sim\lambda\alpha$)で払う組み立て。
- **確認**:値の勘定で、監査の型 の確認が要る。
- **再開条件**:IMS を使わずに手術をファイバーへ運ぶ道(または余裕が $\lambda/\ell^2$ の桁の配位の下界)が書けたとき。〔注 2026-10-22 audit_S2_597(監査 `596_` §8):集団座標の IMS(補題 597-B)+ 欠損つきの Agmon(597-A)で、λ の損は共変性の破れの集合 $\Gamma_R$ と η の遷移にだけ残り期待値で払える —— 電子の箱は $\sim\ell$ でよく、本行の障害は外れる(値 C0 997a の M と補題の水準)。残る難所は $P(\Gamma_R)$ の集中(571-N2 の型)と El の窓(稿 597 §4)。〕

## F373(2026-10-22、w_E05_590b = 書き下しの型、稿 `590_…` §5.2、値)新しい角度 G-TK(G の門の核を芯と遠い蓋の間に張る「筒の核」で、近い領域 $[R_*,D]$ を G から外し、Agmon と手術を蓋だけに当てる)—— 閉じたのは**方式**(値の冪の勘定)
- **勘定**:E5:$K_2\approx\pi D/R_*^2$ で 571-H の主の項 $\lesssim D/(R_*^2c^2)$ ⟹ $D\lesssim\ell^2$。El(外 = 蓋、長さゲージあり):$L_2^{\rm rem}\sim a^2R_*^4D^{-7}$、余裕 $m_H\sim\rho_{\rm m}R_*^2D/c$、IMS で $a\sim n_e\gtrsim(\lambda c/m_H)^{1/2}$;(B6) は $D^9\gtrsim\alpha^4\ell^{19}$ ⟹ $\gamma\ge19/9$ —— E5 の 2 を $\ell^{1/9}$ 越える。
- **R9**:閉じたのは筒の核と蓋の手術の組。G の門の他の形・手術を使わない消費者は閉じていない。
- **再開条件**:蓋の外の $L_2^{\rm rem}$ の D の冪が 7 より速いこと(有界な外の格子の類 C)か、筒の核の $\langle C_f\rangle$ が $K_2$ の決定的な上界より D で遅く育つこと(玩具)が示されたとき。

## F374(2026-10-22、w_E05_591b = 書き下しの型、稿 `591_難問1_ιの正の側_G-LD_外の場の裾_2026-10-22.md` §9、成算 S-E05-R1)候補 2 G-LD(El を大偏差の水準で V に残す)を、571 §14.5 の箱の模型の手術の Agmon のまま、殻 $[D,2D]$・$D=\ell^\gamma$(γ > 1.36)で使う方式
- **何を試したか**:稿 591 の段の列 L0〜L7(補題 591-T = E05-P314・591-K で裾と並進の微分を払う)を、稿 590 §4(590b)の鎖の照合の表に当てた。
- **理由(字面と冪の勘定、値)**:G-LD が替えるのは El だけで、590b の 2 つの障害はどちらも El に依らない。(1) G の門の帯は泡の壁に接する要があり、$r_{\rm in}\lesssim\ell^{6/5}$(γ_max ≤ 1.2)—— G-LD の段 0 の閾 γ > 1.36(と 591-K の $n_e,R\ll D$ の閾 γ > 1.3)はこれを越える。(2) IMS の損 $\lambda/n_e^2\le m_H/8$ から $r_{\rm in}\gtrsim\ell^{7/5}$ で、(1) と両立しない —— G-LD の L2(IMS とファイバーへの運び)と 591-K の ε の段は同じ IMS の条件を含む。
- **閉じたのは**:方式(G-LD × 殻 [D,2D] の幾何の組;G-LD の量 —— 真の状態の外の場の裾 —— は通る;Agmon が制御すべき領域が泡に接し、外を D ≫ ℓ に置けない。2026-10-22 audit_S2_590_592 で「標的」から訂正 —— G-TK の幾何との組は F375 で別に閉じた)。
- **射程**:591-T・591-K(E05-P314)は無傷(一般の補題)。閉じないもの:G の門の核を筒の核 G-TK(590 §5.2)に替えた幾何での G-LD(稿 591 §9.3 の値で、外の場の結合の核の鋭い切断の裾の扱いに依って開くか閉じるかが分かれる)。
- **再開条件**:G の門の帯を泡から離せる核(G-TK の型)で、殻の外の場の分散と λ 倍の並進の微分の連鎖が E5 の上限 $D\lesssim\ell^2$ の内で払えること(稿 591 §9.3)。

## F375(2026-10-22、w_E05_591c = 書き下しの型、稿 `591_難問1_ιの正の側_G-LD_外の場の裾_2026-10-22.md` §10、判定文 worklog `2026-10-22_w_E05_591.md` §7、成算 S-E05-R1、C0 991h)G-TK(筒の核、590 §5.2)の El の段を G-LD(591-T・591-K = E05-P314)で払う方式 —— 札 BOUNDED(字面)、値は閉じる向き
- **何を試したか**:連続の鋭い切断(|k| ≤ π)の平板で、外の部分空間の箱の点の分散と微分 1 つの比を、k⊥ ごとの 1 次元の鎖(帯域の射影を厳密に)で測った;対照は同じコードの格子の型(991d を相対 2e-15 で再現)。
- **理由(値)**:$\sigma_0^2\propto D^{-0.98}$、微分の比 → π²(局所冪 +0.015)—— 結合の核の裾 cos(πr)/r² の型で、蓋の幾何では $\sigma_0^2\sim\ell^2D^{-3}$、591-K の連鎖が育たず閉じる段の $R^3$ の損で γ > 2.42 が要り、G-TK の E5 の上限 γ ≤ 2 を越える。収束の条項($L_z$・動径の求積の相対差 3%・1%)が字面で外れたので札は BOUNDED;判定の後の情報(991i)では主の段の差は約 5% で、冪の判定の閾から遠い。
- **閉じたのは**:方式(値;札は BOUNDED —— 確定には収束の閾を満たす段での同じ判定文の C0 が要る)。
- **射程**:E05-P314(591-T・591-K)は無傷。格子の型の結合(点の評価が局所)の模型では窓 γ ∈ (1.5, 2] が開く読み(稿 §9.2 (i))—— E05 の公理表の模型(鋭い切断)には当たらない。
- **再開条件**:手術の分解 $W_{\rm ext}$ を、帯域の縁(|k| ≈ π)のモードの外への寄与を箱の点で消す形に選べること(未検 → 2026-10-22 稿 597・C0 997a:$W_{\rm ext}:=1_{[1/2,1]}(S_\delta BS_\delta)$ で平板の $\sigma_0^2$ の局所冪 0.98 → 1.93(値、$L_z$ の収束 14〜23%);Hardy の取り直し(597 §4 の C3)は未;監査 596 §8.6)、または結合の核の裾を払う別の閉じる段(Plancherel–Pólya の $R^3$ の損の無いもの)。

## F376(2026-10-22、w_E05_590c = 書き下しの型、稿 `590_難問1_ιの正の側_El後の設計のやり直し_2026-10-22.md` §8 の行 3、成算 S-E05-R1)難問 #1 の (E4) の ι > 0 の側の集中(571-N の (C-v)・(C-m))を、電子の側の余裕 $\kappa\hat g\sim\lambda\alpha$(571-E (b) の V)で直接払う方式 —— 閉じたのは**方式**(字面)
- **理由**:571-E (b) の V は電子の居る所の場の水準 $\hat g(A)=g(0;A)$ だけの関数。消費者を害する事象(G の門の壁の崩れ、窓の縁の第 2 の窪み)では電子は泡の中に居て $\hat g$ は泡の中の値のまま —— 余裕 0。壁の配位への感度は BO の面 $e_{\rm el}(A)$ を通してだけで、それは稿 590 §8 の行 1(G-BOF)の量。
- **R9**:閉じたのは余裕の取り方。571-F(電子の周りが真空的な事象、既にこの形)は無傷。
- **射程(T60)**:禁じるのは「$\kappa\hat g$ の余裕で壁・窓の縁の事象を払う」発注。止めないもの:BO の面の余裕(G-BOF)。
- **再開条件**:なし(字面の所在の不一致)。

## F377(2026-10-22、w_E05_590c = 書き下しの型、稿 `590_…` §8 の行 2、成算 S-E05-R1、値)補題 592-B3(E05-P315、BO の上の手術)を、箱を使わずファイバーの電子に相対な外の領域で当てる方式(IMS を避ける形)—— 閉じたのは**方式**(値の冪の勘定)
- **理由**:IMS は消えるが、$\mathrm{El}_{\rm BO}\lesssim C_W\delta^{-1}r_{\rm loc}(A_{\rm e})^2$ で、消費者の要る外(泡に接する帯、$r_{\rm in}\sim R_*$)と電子の局在の半径 $\sim R_*/2$(NUM-7574)が同じ桁 —— $r_{\rm loc}^2\sim a^2D^{-4}\sim\ell^{-2}$、$\lambda\alpha\ell^{-2}\sim\mathrm{MF}$ で、壁を崩す費用 $\Delta E_{\rm rel}\sim10^{-4}\mathrm{MF}$(C0 990b)に対し桁で大きい。さらに全空間の BO は F310 (b) で閉じている。
- **共通点(1 行)**:**泡に接する場は MF の場の裾(電子の自己エネルギーの担い手)で、自由な真空で替えると MF の桁を失う。**
- **R9**:閉じたのは手術の型。592-B3 の不等式そのものは無傷。
- **射程(T60)**:禁じるのは「泡に接する帯を外にする手術(BO の上でも)」の発注。

## F378(2026-10-22、w_E05_590c = 書き下しの型、稿 `590_…` §8 の行 4・5、成算 S-E05-R1)補題 591-T(E05-P314、真の状態の外の場の Gauss の裾)を手術なしで集中(571-N)に使う方式と、その共役(電場 Π の上側の裾で偽の窪みを押さえる)—— 閉じたのは**方式**(字面と向き)
- **理由**:P314 が押さえるのは $s\ge0$ の指数の積率、すなわち A の型の場が**大きい**側の裾。消費者を害する事象は全て窪み(スクイーズ、u′ が**小さい**)の側(稿 590 §7.2 (iii))—— 向きが逆。共役の Π の側は、泡の中で真の状態の Π が真空より太い(スクイーズの共役)ので大域の Gauss の支配は偽;領域に局在した支配は G-BOF と同じ精度の問題。
- **R9**:閉じたのは裾の向きの使い方。P314 そのもの(El の大偏差の側、G-LD)は無傷。
- **射程(T60)**:禁じるのは「上側の裾の補題で窪みの事象を押さえる」発注。
- **再開条件**:窪みの側(下側の裾 $\langle e^{-sW}\rangle$)の、真の状態での真空との比較の不等式が立ったとき(エネルギーで払う側の量なので、Gauss の支配の機構では出ない見込み)。

## F379(2026-10-22、w_E05_598 = 書き下しの型、稿 `598_難問1_ιの正の側_手術G-TK滑の値_2026-10-22.md` §1、成算 S-E05-R1、C0 997b)蓋の幾何の外の場の点の分散を「蓋の格子点の上の有限の局在の基底」で測る数値の方式
- **閉じたもの**:**方式**(数値の方式。G-TK の蓋の幾何の El の重み $\sigma_0^2(D)$ を、蓋の格子点 $y$ の帯域の制限されたデルタ $S_\delta P_T\delta_y$ の張る有限の空間で外の部分空間を近似して測る方法)。El の窓・G-TK・ι > 0 の真偽は閉じていない。
- **理由**:鋭い切断(δ = 0)の対照が予言 $R_c^2D\cdot D^{-4}$(局所冪 3)を再現しない —— 第 1 版(一般化固有値 $\lVert S\varphi\rVert^2\ge\frac12\lVert\varphi\rVert^2$)で局所冪 3.24・2.73・2.23(D = 4〜32)、第 2 版($1_{[1/2,1]}(SBS)$ の Rayleigh–Ritz、$1_{\mathcal E}$ を格子の和で近似)で 1.74・2.41・5.60。第 1 版は外の領域への局在($B\ge\frac12$)を課さず、第 2 版は有限の基底と格子の和の近似が帯域の縁の振動の裾を扱えない(読み)。同じ量の $L^2$ の上界(997e、動径の積分だけ)は 2.73・2.88・2.95・2.99 で予言 3 に収束する —— 失敗は基底の作り方にある。
- **共通点(1 行)**:有限の点の上の帯域の制限された基底では、外の領域への局在と帯域の縁の裾の両方を同時に正しく扱えない。
- **射程(T60)**:禁じるのは「蓋の有限の点の基底の Rayleigh–Ritz で El の重みの D の冪を判定する」発注。止めないもの:円筒の座標の連続の計算(軸の対称で角運動量ごとに分け、動径と z の帯域の基底を使う);$L^2$ の上界 $2\lVert1_{\mathcal E}SP_T\delta\rVert^2$ による冪の評価(ω⁻¹ の赤外の重みは別に要る)。
- **再開条件**:円筒の座標の連続の基底で、鋭い切断の対照(冪 3)が再現できたとき。
- **R9**:数値の方式の閉鎖で、標的とも名指しとも同値でない。

## F380(2026-10-22、w_E05_598b = 書き下しの型、稿 `598_難問1_ιの正の側_手術G-TK滑の値_2026-10-22.md` 第 2 部、成算 S-E05-R1、C0 997h)G-TK の G の門の核の形を替えて(蓋を D まで広げる「ラッパの蓋」など)外の領域の Hardy の余裕を増やし、El の窓を広げる方式
- **閉じたもの**:**方式**(G の門の核の形の替えで Hardy の余裕を増やす組み立て)。El の窓・筒の蓋の G-TK・ι > 0 の真偽は閉じていない。
- **理由**:補題 598-W(self-audited):G は m の z 方向の段差だけを見るので、泡を貫く線の上の泡の外(管)を強く窪ませた配位は、核の形に依らず $G=(\tau-m_{\rm in})\Phi_{\rm wall}$ で門を落とす。ゆえに門の失敗の集合の上の Hardy の余裕は管の体積 $\lesssim\pi R_*^2L_k$ で上から押さえられ、広がりの体積は効かない。C0 997h:柱だけの窪みで $\bar b$ が −0.264・−0.258・−0.252 倍(ラッパと筒で同じ;窪んだのはラッパの台の 13.8%・7.0%・4.0%)、広がりだけの窪みで不変(相対 1e-12)。稿 598 第 1 部 §4 の「ラッパの蓋で $m_H\propto D^3$、窓の幅 +0.06〜+0.32」は無効。
- **共通点(1 行)**:一様な窪みは鉛直の線ごとの望遠鏡で G から消えるので、G の門が要る窪みは泡の壁の段差を運ぶ線(断面 $\pi R_*^2$)の上だけに限られる。
- **射程(T60)**:禁じるのは「G の門の核の形(広がり・太さ)を替えて El の窓を広げる」発注。止めないもの:筒の蓋の勘定の定数(C3 の Hardy の取り直し、C5 の ω⁻¹ の冪)で際を動かす値の計算;G の門以外の消費者(窓の段差でなく別の汎関数で失敗の集合を定める形)。
- **再開条件**:G の門の量を、z の段差でなく体積に比例する量(例えば外の殻の全体の平均)で失敗を判定する消費者に替え、571-H の C_f の評価と E5 が保てたとき。
- **R9**:核と配位の決定的な言明に基づく方式の閉鎖で、標的とも名指しとも同値でない。

## F381(2026-10-22、w_E05_603 = 書き下しの型、稿 `603_難問1_ιの正の側_筒の蓋のT4_2026-10-22.md` §1・§2、成算 S-E05-R1、C0 997o)T4 の Hardy の取り直しで、Hardy の定数を「外の成分の量 $u'^{\rm ext}_Q$ への換算」と「被覆の固有値の最小の方向を捨てた有効の次元(h ≈ ¼)」で見積もる読み(稿 602 §5 の入力 (a)(b)、稿 598 §2 の「有効 ≈ 0.25」)
- **閉じたもの**:**方式**(Hardy の係数の見積もりの読み)。T4 そのもの・El の窓・ι > 0 の真偽は閉じていない(T4 は補題 603-T4 で閉の向き)。
- **理由**:557-H の定数は $\mathrm{tr}G'-2\lVert G'\rVert$(次元の数え)で決まり、2 次形式の最も弱い方向にも ω⁻¹ の重みの共分散の比にも依らない。外の運動量だけで Hardy を取ると、観測量は全ての成分の $u'_Q$ のままで(内の配位を止めると外の座標のずらした 2 次形式;補題 603-T4 (i))、(a) の換算は要らない。定数は外の部分空間の局所の次元の密度 $\kappa_{\rm e}$ で、C0 997o で $h_{\rm eff}=\kappa_{\rm e}^2$ = 0.373〜0.378(D = 4〜32、バルク $(k_*/\pi)^6$ = 0.374)—— 「¼」は誤り(控えめ)。C3 の 0.727 は共分散の比で別の量(997o で 0.721 を再現)。
- **共通点(1 行)**:Hardy の定数を「分散の大きさ」で見積もったが、Hardy の発散の議論が数えるのは次元(跡と最大の固有値)だけ。
- **射程(T60)**:禁じるのは El の窓の勘定に h = 0.25・0.316((1−δ)⁴)を Hardy の係数として入れること。止めないもの:c(窪みの閾)の定数の勘定(稿 603 §4)、$e_*$ の値。
- **再開条件**:なし(読みの訂正)。
- **R9**:場の 2 次形式の決定的な言明に基づく読みの閉鎖で、標的とも名指しとも同値でない。

## F382(2026-10-22、w_E05_604 = 書き下しの型、稿 `604_難問1_ιの正の側_筒の蓋のT7とcの勘定_2026-10-22.md` §1・§2、成算 S-E05-R1、C0 997p)筒の蓋の G-TK の El の窓を、到達できる λ(≤ 1e9)で、芯の核の取り方(602 §3「芯の核を泡の壁の内に縮める」、$\beta_0\to0$)で正にする方式
- **閉じたもの**:**方式**(到達できる λ での窓の値の見通し)。漸近の窓(幅 +0.436)・ι > 0 の真偽・T4(E05-P320)は閉じていない。
- **理由**:E5 の c(門の閾 $c_G=G_0/(Wm_{\rm vac})$)と El の c(窪みの閾 $c_{\rm dep}$)は別の量で、602-T3 が $\theta_*=\beta_0+G_0/W$、$f=1-\theta_*/\tau$ でつなぐ。603-T4C の正味の余裕が正であるには $c_{\rm rel}\lt0.64f$ で τ ≲ 0.2、すると $G_0/W\lt\tau$ で $c_G\lesssim0.15$、E5 の上限 $D\lesssim\ell^2c_G^2$ が縮む。C0 997p:λ = 1e9 の幅の最良は −1.39($\beta_0=0$)、$\beta_0$ = 0.12 で −4.4、≥ 0.15 で正味の余裕なし。式の外の O(1) の定数で救うには約 50 倍が要る。
- **共通点(1 行)**:Hardy の正味の余裕は深い窪み(閾 ≲ 真空の 2 割)でしか正にならず、602-T3 の線形の門ではその閾が門の閾 $G_0$ を同じ小ささに縛る —— 余裕と E5 が同じ τ を逆向きに引く。
- **射程(T60)**:禁じるのは「到達できる λ の数値で窓が正」を手術の族の成算の根拠にすること。止めないもの:漸近の命題の組み立て;$G_0$ を τ から切り離す別の門(非線形の門、または E5 を別の項で払う)。
- **再開条件**:602-T3 の型の包含で $G_0/W$ を τ と独立に取れる門の量(例えば窪みの深さの非線形の関数を核で重ねた G)が見つかり、571-H の C_f の評価が保てたとき。
- **R9**:定数の算術による方式の閉鎖で、標的とも名指しとも同値でない。

## F383(2026-10-22、w_E05_604 = 書き下しの型、稿 `604_…` §3、C0 997q)T7(571-N2 の弱い版、$P(\Gamma_R)\lesssim\ell^{-4.2}$)の場の側を、閾 $g_0$ = 0.1 の粗視化(b = ℓ/2)の非真空の事象と、603-T4C の一様の重みの余裕・571-G の F の費用の Agmon で払う設計
- 〔2026-10-22 訂正:札「NOGO」の読みは F384 で置き換え —— 閾 $g_0$ = 0.1 の選びの人工物。値の記録は残す〕
- **閉じたもの**:**方式**(閾 $g_0$ = 0.1 の設計の、到達できる λ での指数の予算)。T7 の真偽・閾を下げた設計は閉じていない。
- **理由**:正味の余裕は $g\le0.124$ でだけ正で、指数の予算は要る水準 $4.2\ln\ell$ の 0.059 倍(1e9、b = ℓ/2;b = ℓ でも 0.47)。交差は λ ≈ 1.5e12。
- **共通点(1 行)**:Agmon の指数は深い窪みの区間($g\lesssim0.05$)で稼がれ、事象の閾が浅いと区間が空に近い。
- **射程(T60)**:止めないもの:$g_0\to$ 泡の内の水準の設計(情報で $g_0=0$ なら 5.9 倍、交差 λ ≈ 8.6e6)。
- **再開条件**:推定子の $\tilde\chi(g)$ の台を、泡の検出の頑健さを保ったまま $g\le g_0$($g_0\lesssim0.05$)に絞れると示せたとき —— 判定文は結果を見ていない体で固定する。
- **R9**:予算の算術による方式の閉鎖で、標的と同値でない。

## F384(2026-10-22、kc_E05_608 = 書き下しの型、稿 `608_類C_T7のK交点_2026-10-22.md`、判定文 記録 `606_判定文_T7のg0_2026-10-22.md` §2、C0 997s)**F383 の訂正**:F383 の NOGO は閾 $g_0$ の選びの人工物(方式の設定)
- 何を閉じたか:**閉鎖の取り消し(方式の設定の誤り)**。F383 が「T7 の場の側は予算で殺される」とした札は、閾 $g_0$ = 0.1 が φ の正味の余裕の稼ぎ場(小さい g の側、$\varphi\sim1/g$)を切り捨てた設定に依っていた(606 §2.4)。
- 根拠:606 §2 で起動前に固定した判定文(下端 $g_0=Ku_{\rm vac}\ell^{-2}$、K は検出の頑健さで決まる範囲)を 997s に当てて **GO**:決め手のセル r(λ = 1e9, b = ℓ/2, K = 9) = 2.23(境の帯の外)、$K_\times(10^9,\ell/2)$ = 18.5 ≥ 9;N のセル r(1e9, ℓ, K = 1) = 37.3。C0 対照(997q の再現、相対差 0)・C-num(格子の倍で 5e-5)は成る。値は [T88]。
- 限定:GO は場の作用素だけの予算(997q の量:電子の λ の項 597-B・継ぎ目・El を含まない)で T7 の第 1 歩が殺されないことだけを言う。**命題 T7 の真偽は開いたまま**;F383 の本文のうち $g_0$ = 0.1 での値の記録はそのまま残し、「NOGO」の札の読みだけをこの行で置き換える。
- 再開条件:T7 の書き下しでは、電子の λ の項(597-B)・継ぎ目・El の予算を $F_{\max}$ に差し引いた形で同じ判定(K ≤ 9、b = ℓ/2)を当て直す。

## F385(2026-10-22、w_E05_609 = 書き下しの型、稿 `609_難問1_ιの正の側_状態の集中T7T8_2026-10-22.md`、判定文 worklog (研究ノート: `2026-10-22_w_E05_609.md`) §1(C0 の前に固定)、成算 S-E05-R1、C0 997t)T7(571-N2 の弱い版、$P(\Gamma_R)\lesssim\ell^{-4.2}$)を、997s の場だけの Agmon の予算(F384 の GO)から電子に相対な窓の λ の項・597-B の IMS の損・継ぎ目・El を差し引いて取る方式
- **閉じたもの**:**方式の設定**(ファイバーの f を電子に相対な窓で作る単一ブロックの深さの経路の Agmon を、窓の定数 $K_w$ = 1($r_W=\ell\ln\lambda$)と 606 の $F_{\rm req}=4.2\ln\ell$(571-D の因子 2 なし —— 要る F を 2 倍に見積もる)の組で)。楽観の端の比は λ に依らず $K_w$ に線形(0.49・1.02・1.55 @ $K_w$ = 1・2・3、λ = 1e9)、因子 2 を入れると $K_w$ = 1 で 0.98 —— F383 と同じ設定の型(監査 610 §6.1)。機構(窓の長さに比例する Agmon、571 §9.2)と命題 T7 の真偽は閉じていない。
- **根拠**:札 NOGO(字面)。λ = 1e9 の楽観の端(K = 1、b = ℓ、$r_W=\ell\ln\lambda$、λ の率だけを引き、経路は線形計画で最適)で $r=F/(4.2\ln\ell)$ = 0.491;悲観の端(K = 9、b = ℓ/2、$r_W=7.5\ell$、差し引き全部)で 3.9e-4。C0(997s の再現)・C-num とも成。
- **共通点(1 行)**:軽い電子(質量 1/λ)に相対に局在した f の Agmon の率は $\sqrt{2M/\lambda}\sim\ell^{-1}$ に縛られ、指数は窓の長さにしか比例しない(571 §9 の難所 (1)・597 R9 の循環と同じ根)。
- **射程(T60)**:止めないもの —— 窓 $\ge2\ell\ln\lambda$(要る窓 $K_w^\times$ = 1.96 @1e9、λ でほぼ一定:楽観の端はそこで届く);$F_{\rm req}$ に 571-D の因子 2 を入れる読み(楽観の端 r ≈ 0.98、境の帯の中)。確度は中。
- **再開条件**:$K_w$・$n_b$・d の構造の上限(E5 の D と窓の縁の関係、min の汎関数の配位の IMS の分割の費用、電子の箱 $n_b+4d$ と蓋の距離)を記号の勘定で特定した後、その範囲の端で結果を見ていない体が判定文を書くとき(上限を特定しない固定は空の閾 —— 監査 610 §6.3)。悲観の端の 597-B の損は λ に依らない比(λ = 1e9 で 15.5、$\propto C_\chi/n_b^2$)で、$n_b\gtrsim4\ell$ で払える見込み(値、監査 610 §6.2)。
- **R9**:予算の算術による方式の閉鎖で、標的と同値でない。

## F386(E05、難問 #1 (E4) ι > 0 の G-BOF の段 S4′(PF)を、**大域の 2 次の比較(局在なし)または座標ごとの積の IMS** で出す方式。2026-10-22、w_E05_601b = 書き下しの型、稿 `601_難問1_ιの正の側_G-BOFのS4prime_2026-10-22.md` 第 2 部 §8・§9、worklog (研究ノート: `2026-10-22_w_E05_601.md`) 第 2 部、C0 a601c・a601d)
- **閉じたもの**:**方式**(値と初等の比較)。S4′(PF)の真偽は閉じない —— 真の ε は玩具で 2 次の型で桁で小さく(稿 §3・NUM-7693)、命題の向きは真の見込みのまま。
- **理由**:補題 601-L′(線形の座標を局在なし)の誤差は $\frac12\mathrm{Tr}((K^+-K^-)\mathrm{Cov}(\ell))=\eta\,\mathrm{Bog}_{\rm para}$(η は常磁性の Hessian の**大域の**相対の幅)。PF の余裕に要るのは η ≲ $\Delta E^*/\mathrm{Bog}_{\rm para}$ ≈ 4.5e-3(玩具 1e8)・1.8e-3(1e9)だが、全ての ℓ の上の幅は(大きい ℓ で電子の状態が替わるので)O(1)。座標ごとの積の IMS は費用 $J\pi^2/(8w^2)$ が場のモードの数に比例し、2 乗の座標の方向は下からの 2 次の比較が q の 4 次で下に有界でない(IMS が要る;一様な形の 601-L は玩具の尺度で 20〜40 倍足りない、稿 §4)。有限の確かめ(a601d)で、大域の幅の 1 次の上界は真の ε より 3 桁緩い。
- **共通点(1 行)**:**誤差を Hessian の大域の量(幅、または座標ごとの局在の費用)で払う型は、真の ε(Hessian の局所の変化の 2 次)より桁で粗く、PF の余裕(MF の $10^{-4}$)に入らない。**
- **射程(T60)**:禁じるのは「局在なしの大域の 2 次の比較」と「場のモードごとの積の IMS」(モードごとに幅 $w_j$ を最適にしても、費用と曲率の釣り合いは $\sum_j\sqrt{K_j}$ の √ の型で外延的 —— これも含む)で S4′(PF)の ε を余裕の内に押さえる発注。大域の $K^+$ は電子の箱の基底の一様な隙間なしでは有限でもない(監査 612 §1.2・§3)。止めないもの:電子の応答の集団の自由度(有限個)に落としてから局在する型(BS の局在の段に当たる)、Gauss の周りの摂動の作用素の不等式(Feshbach・Schur の補行列の型)を下に有界でない 4 次の残りの上で使えるようにする道具。
- **再開条件**:常磁性の Hessian の大域の幅を、泡のセルの上で余裕/$\mathrm{Bog}_{\rm para}$ 以下に押さえる構造(例:電子の隙間の一様な下界で ℓ の範囲を Gauss の裾で切れる形)が見つかったとき。

## F387(2026-10-22、w_E05_599 = 書き下しの型、稿 `599_難問1_ιの正の側_G-BOFのHFB型の参照_2026-10-22.md` §4.1、判定文 worklog (研究ノート: `2026-10-22_w_E05_599.md`) §6(C0 の前に固定;§4.1 の量は判定の後の情報)、成算 S-E05-R1、C0 999Pf・999Pg)G-BOF の参照を、縦の場の成分を持つ玩具(976d の場・模型 P)の**対角で等方の Gauss の共分散**($E_{\rm GBO}$ または 2 次の F の、点ごとに独立な s の族の最小)で立てる方式
- **閉じたもの**:**方式**(参照の族の取り方)。玩具の場は点ごとに 3 成分の独立な振動子で、格子の純ゲージの方向(縦、$q_j(x)=\chi(x+e_j)-\chi(x)$)を含む;ゲージ不変な正確な Peierls の電子はこの方向を感じない($A_S$ の固有値で 1 に張りつくもの 1370 本 = 泡の内部のサイトの数)。対角で等方の Γ は縦の成分まで泡の中でスクイーズして場のエネルギーを払うので、非対角(Bogoliubov)の Gauss で $E_{\rm GBO}$ が余裕の 22 倍(1e5:−1629 ± 8 対 余裕 75.2;場の項 −752・電子の項 −877)下がる —— 対角の参照は G-BOF の余裕の尺度より桁で大きい自由度を見落とす。
- **根拠**:値【T88】(1e5、泡の中の結合 5229 本で $\Gamma_S=\frac12A_S^{-1/2}$、外は対角、共通の正規乱数 32 本の MC);2 次の展開の値は −721(展開は効かない)。δ の差(ref と half)は余裕の 0.24 ± 0.16 で未決。
- **共通点(1 行)**:対角で等方の族は、玩具の場の縦(純ゲージ)の成分を電子に見えないまま泡の中でスクイーズし(場の項だけの損)、かつ物理(横)の部分の非対角の相関(電子の項の得 −877・−3806、PF にも在る型)を表せない —— 対角の参照は両方を見落とす(監査 600 §2.2 の限定の具体の形と、族の狭さ;監査 612 §5.1)。
- **射程(T60)**:止めないもの —— 横(発散 0)の場の玩具での対角・非対角の参照(監査 600 §5.2 の 3 手目);PF(Coulomb ゲージ、縦の成分なし)での $E_{\rm GBO}$ の参照そのもの;第 1 部の玩具の F の自己無撞着な最小の値(縦を区別しない玩具の中の量として)。止めるもの —— 縦の成分を持つ玩具の対角の参照の壁の量(G・余裕)を PF の S3〜S6 の値として読むこと。確度は中(全次数は 1e5 と 1e6(泡の芯だけ、余裕の 33 倍)の 2 段;比は λ で増える)。
- **再開条件**:玩具の場を横に制限する(または縦の成分を電子の結合から外し場のエネルギーからも除く)設定で、対角と非対角の参照の差が余裕の 10% 以内に収まると示されたとき。
- **R9**:参照の族の取り方の閉鎖で、標的(ι > 0)の真偽に触れない。

## F388(2026-10-22、w_E05_611 = 書き下しの型、稿 `611_難問1_ιの正の側_状態の集中_定数の上限とT7T8_2026-10-22.md` §1.2、成算 S-E05-R1、値 997u)T7 の Agmon の余裕を、窓の中のどこかの深いブロックから拾う 2 つの組み方 —— (B1) 603-Z の重み M を窓の全てのブロックに一様に置く凸結合、(B2-rel) 電子に相対な枠で最小点の位置を分ける IMS
- **閉じたもの**:**方式**(2 つの組み方)。命題 T7 の真偽は閉じない(代わりの組み方 = 電子の局在 + 補題 611-P の場だけの分割、稿 §1.2・§2.2)。
- **根拠**:(B1)603-T4C の掛け算の下界は全てのブロックの和で、深くないブロックは正味で負(真空の水準で Hardy/零点の比 $h_v$ = 0.641)—— 零点の基線 $c_{\rm ZP}\cdot\frac{4\pi}3r_W^3$ が窓の体積で効き、$K_w\le(3\mu/(4\pi c_{\rm ZP}))^{1/3}/(\ell\ln\lambda)$;1e9 の楽観の端で基線/余裕 = 880(上限 ≈ 0.10)。(B2-rel)分割の関数が並進で動き λ の項 $\lambda C_\chi/(2n_p^2)$ を $\mathcal Z$ の全体に置き、胞の基線と合わせて最適で $\propto\lambda^{3/5}$(1e9 で余裕の約 8 倍、値)。
- **共通点(1 行)**:「各 Y で $H\ge\mathcal V_Y$」から「$H\ge\max_Y\mathcal V_Y$」へ移る費用を、窓の体積(B1)か電子の質量の率(B2-rel)で払っていた —— 場だけの関数で選べば(電子を箱に置いた後)どちらも要らない。
- **射程(T60)**:止めないもの —— 電子の座標の IMS の後の絶対の枠の場だけの softmax(補題 611-P;費用 $\frac{\beta^2}8C_g$、窓は $\ln^2N$)。B1 の上限は漸近 $\ell^{2/3}/\ln\lambda$ で育つ(定数の上限ではない)が、到達できる λ で効く。B2-rel の費用 $\propto\lambda^{3/5}$ は余裕 $\mu\propto\lambda^{5/7}$ に対し比 $\propto\lambda^{-4/35}$ で縮む —— B2-rel の閉鎖は到達できる λ の値の閉鎖で、漸近の方式の閉鎖ではない(監査 613 §1.2 (e))。
- **再開条件**:なし(代わりの組み方で置き換え済み)。
- **R9**:作用素の下界の組み方の閉鎖で、標的と同値でない。

## F389(E05、難問 #1 (E4) ι > 0 の G-BOF の S4′(PF)の道 (B) を、**Hessian の軟化の方向(電子が 2 次で感じる方向)を集団の座標に取って局在する**形で出す方式。2026-10-22、w_E05_601c = 書き下しの型、稿 `601_難問1_ιの正の側_G-BOFのS4prime_2026-10-22.md` 第 3 部 §13・§14、worklog (研究ノート: `2026-10-22_w_E05_601.md`) 第 3 部、C0 a601f)
- **閉じたもの**:**方式**(値)。道 (B) そのものと S4′(PF)の真偽は閉じない —— 道 (B) は「非調和の方向」を集団の座標に取る形(系 601-B、名指し (BO-rank))で続く。
- **理由**:976d の Hartree の MF の Hessian で、電子が 10% 以上軟らかくする方向の数は 371(1e5)・≥ 397(1e6)と数百で、λ とともに増える(泡の体積の型、外延的);それを集団の座標に取ると IMS の費用 $\sum_{y\in c}\pi^2/(8w^2)$ が座標の数に比例し、601-L・601-L′ の失敗(F386)と同じ型に戻る。しかも軟化は 2 次の量で Gauss の族に厳密に吸収される(系 601-B の $W_0$)—— 局在する必要がそもそも無い方向だった。
- **共通点(1 行)**:**2 次で書ける応答(軟化)を局在の対象に数えると、座標の数が外延的になり、局在の費用が余裕を越える —— 局在すべきは非調和の方向だけ。**
- **射程(T60)**:禁じるのは「Hessian の軟化の方向(固有値の閾で選んだ方向)を集団の座標として IMS で局在する」発注。止めないもの:非調和の階数で選ぶ形((BO-rank))、強圧性で 𝒟 の外を払う構成。
- **再開条件**:なし(方式の誤りの同定;道 (B) は (BO-rank) の形で続く)。

## F390(2026-10-22、audit_S2_611 = 監査の型、監査稿 `613_合同監査_611の状態の集中_2026-10-22.md` §2.1・§2.2)T7 の Agmon を、**窓の外縁で打ち切った min(または格子の点の soft-min)の汎関数** $\tilde G=\min_{\lvert Y\rvert\le r_W}[g_b(Y)+\Psi(\lvert Y\rvert)]$ と、**斜面をずらさない輪郭**(要求 $\lambda k^2/(G-s)$)で書く設定(稿 609 §1.1・稿 611 §2.2 の命題 611-T7 の字面)
- **閉じたもの**:**方式の設定**(f の汎関数の作り方と輪郭)。命題 T7 の真偽と「窓の長さに比例する Agmon」の機構は閉じない —— 修理版(積分の soft-min・外の堀・θ のずらし)は監査人の補題 613-A(self-audited、独立確認待ち)。
- **根拠**:(1) 外縁 $\lvert Y\rvert=r_W$ の上の深いブロックが最小点の配位(縁の事象の内部)で、Danskin の型で $D_f=F'\nabla g_b(Y^*)$、$\lvert D_f\rvert\sim F'\sqrt3/b$ —— 571-D の条件で $F'\lesssim b\sqrt{\mu/\lambda}=O(1)$、指数は $O(g_0)\sim\ell^{-2}$ に落ちる。(2) 格子の点の soft-min の並進の微分は $\langle\nabla_Yg_b\rangle_p$($\sim1/b$)で、斜面の傾き h で押さえられない(積分の soft-min なら部分積分で $-\langle\nabla\Psi\rangle_p$)。(3) 611-P の選び分けの代償で余裕は $\mu(g+\theta_\delta g_0)$(g → 0 で有限)になり、ずらさない輪郭の要求 $\lambda k^2/(G-s)$ は斜面の上の非常に深いブロックで発散 —— 仮定 $`\inf_g g\,\mu_{\rm net}(g)\gt0`$ は決して成らない。
- **共通点(1 行)**:**Agmon の f の並進の微分を「斜面の傾き」だけで押さえる計算は、領域の縁(打ち切り)と格子(離散の選び)と余裕の下端(選び分けの代償)の 3 か所で破れる —— どれも f の作り方の人工物。**
- **射程(T60)**:止めないもの —— 積分の soft-min(温度 β′ → ∞ は費用なし)、Ψ を窓の外で同じ斜面で再び立ち上げる外の堀(候補の範囲 $r_W+L_*$、対数の定数)、斜面の θ のずらし($c_9$ = 0.882 → 0.751・0.647・0.493 @ θ = ¼・½・1)。609 の LP の値(F385 の札)は外縁を見ない楽観の側の値で、向きは NOGO を強める側 —— 札は変わらない。
- **再開条件**:なし(修理版で置き換え;613-A の独立確認が FAIL なら再検討)。
- **R9**:Agmon の汎関数の作り方の閉鎖で、標的とも T7 とも同値でない。

## F391(2026-10-22、kc_E05_616 = 書き下しの型、稿 `616_類C_T7の(H-μ′)と(Cap)_2026-10-22.md` §3〜§6、判定文 記録 615 §1〜§4、C0 997v)T7 の場の側を**補題 613-A(E05-P326:遠いブロックの手術 + 611-P の場だけの分割 + 粗視化のブロックの Agmon)で取る方式**を、到達できる λ(≤ 1e9)と 615 の設計の格子(7776 × K × b)で当てる
- **閉じたもの(R3)**:**方式**(到達できる有限の λ で)。命題 T7 の真偽・λ → ∞ は閉じない。
- **札**:NOGO-μ(最終、λ = 1e9;暫定 1e8 も)。決め手 $c_N$ =(1e9、楽観、$b_{\max}$ = ℓ)で $h^*=-0.477\lt-0.05$(93312 設計の全てで (H-μ′) が外れる);$c_G$ =(1e9、悲観、ℓ/2)は $h^*=-\infty$。対照 C0-s/t/u/J・C-num は全て PASS。全 12 セル(λ = 1e7〜1e9)で $h\gt0$ の設計は 0 本。
- **機構**:(H-μ′) の inf は $0\lt g\le ag_s$ の全域で、上端 $g=ag_s$ で決まる —— φ が 1/g より速く落ち($\mu(5g_s)/\mu(g_s)$ = 0.138 < η の格子の下端の和 0.15)、$\theta_\delta$ を下げると $S'_{\rm part}\propto\theta_\delta^{-2}$ が育つ。悲観の端は φ の台の上端 0.124 < $(a+2\theta_\delta)g_s$ で μ = 0 の点が入る。
- **共通点(1 行)**:**613-A の (H-μ′) は斜面の頂上 $ag_s$(a ≥ 3)まで余裕の正を要り、有限の λ では φ の 1/g より速い減衰と分割の費用が頂上の余裕を食う。**
- **射程(T60)**:止めないもの —— λ の格子の外(情報、数えない):楽観・ℓ の $h^*$ は 1e10 で +0.022、1e11 で +0.28(G の型、$K_w^{\rm req}$ = 20.6)、悲観・ℓ/2 は 1e14 で G の型(冪の当てはめと φ の表の適用範囲は未確認)。613 §5 の「漸近では自動」と同じ向き。
- **再開条件**:(a) 斜面の頂上を $ag_s$ より下げる版(1 < a < 3、または頂上での余裕の要求を緩める 613-A の改訂)が立ったとき、または (b) 到達の λ を 1e11 以上に上げる根拠(格子・φ の表の延長)が立ったとき —— 615 の判定文を新しい格子で立て直して当てる(結果を見ていない体で)。
- **R9**:613-A の方式の有限の λ での閉鎖で、標的とも T7 とも同値でない。
- **親の注(2026-10-22)**:ι = inf_λ h/λ > 0 に要るのは λ ≥ λ₁(λ₁ は任意の有限)での主張だけ(λ ≤ λ₁ は h ≥ 1 で h/λ ≥ 1/λ₁)。本行の閉鎖は到達できる λ(≤ 1e9)と 615 の格子の範囲に限り、**ι > 0 の証明の道を閉じない**(情報:λ ≥ 1e11 で G の型、$K_w^{\rm req}$ = 20.6)。

## F392(2026-10-22、w_E05_622_shell = 書き下しの型、稿 `622_難問1_ιの正の側_殻の漸化式_2026-10-22.md` §2・§3、成算 S-E05-R1 の族 D6、C0 622a)難問 #1 (E4) ι>0 の族 D6「力ずくの殻の漸化式:殻 $[\Lambda,\Lambda(1+\delta)]$ ごとの $h$ の増分を作用素の不等式で下から押さえ、ODE $dg/d\ln\lambda=\Phi(g)-g$($g=h/\lambda$)の比較で障壁 $g\ge g_c\gt0$ を出す」—— 閉じたのは**方式**

親(G3 第 74 陣)が連結 2026-10-22
- **何を試したか**:(a) 1 ループ・反跳つきの増分 $\Phi_1(g)=\frac{8\alpha}{3\pi}\frac g{1+2g}$(F10 命題 3、HS02 Thm 1 式 (3.4))と、泡の慣性を殻が見る質量 M で書いた版 $\Phi_b(g)=K_B\alpha^{2/7}g^{-5/7}$($K_B=\frac{12}7\frac4{21}c_{\rm JG}$、P298・564 §3 の推論)の流れの零点(C0 622a);(b) 障壁の補題 622-B(Dini の比較);(c) 消費者 $1/h=1-\frac23Q$ の殻ごとの増分 $Q'-Q\ge\frac32\delta/h$((3.1))を、殻の Feshbach 分解(E05-P94 補題 136-A)と作用素の評価(P94 補題 136-C、P93 の天井)で出す道。
- **理由**:(a) 1 ループ版は $a=\frac{8\alpha}{3\pi}\le1$(α ≤ 3π/8)で NOFP、$h\sim\lambda^a$;泡の版は障壁が出るが形式の不動点は泡の域の外(PINNED_AT_CROSSOVER、値)。(b) (C-cont) の下で (D-shell) ⟺ ι>0 —— 標的と同値な言い換え。(c) 殻の利得と損はそれぞれ αδ の桁で、要る精度 $\delta/h$ との比は $\alpha h\to\infty$ —— 別々の評価は相殺を見ない;作用素の水準ではさらに誤差が $\gtrsim\alpha\lambda\delta$(読み:P94 補題 136-C の通貨は |q| ≥ κ₀Λ のファイバーの評価、P93 の天井 $(2+\kappa)\Lambda$ で反跳の分母 $\Lambda^2/2$ に届かない;監査 624 §6)、比 $\alpha\lambda h\ge\alpha g_c\lambda^2\to\infty$ で殻の幅に依らない。機構は F10 命題 1・2(主要項の相殺を別々の評価は見ない)と同じ。泡の版の殻の不等式は、自己相似(F10 の R5′-1;対チャネルは M に依らない —— F10 命題 4 —— で偽の向き)と各尺度の泡の慣性(道 (e) の微分形)を要し、後者の静的な版だけで $h\ge c\lambda$ 以上(玩具の値で $\lambda^{9/7}$;$M=\frac23E_f$ からの $\lambda^{12/7}$ は F348 で外れた式 —— 監査 624 §6)が出るので、D6 は (e) より強い入力を要する。
- **閉じたもの**:方式(殻ごとの作用素・ノルムの不等式の積み上げ + ODE の比較)。ι の値・真偽、道 (e) は閉じない。
- **R9**:双極子($h=1+c_d\lambda$)では $g_c\le c_d$ で (D-shell) の前件が空 —— 整合;擬交差の梯子は場の自由度が無く適用外。(D-shell) は標的と同値なので名指しにしない。
- **射程(T60)**:禁じるのは「段ごとの評価が相殺を見ない型」の積み上げ(ノルム・作用素の不等式・Cauchy–Schwarz)。止めないもの:Ward の恒等式・電荷の非くりこみで主要項の相殺を段ごとに厳密に表す型(F10 の R5′-2、補題 573-A の集約の型)、道 (e) の静的な慣性の下界、値の水準の RG。
- **再開条件**:殻ごとの $Q$ の増分を、利得と損の相殺を恒等式で表した形(誤差が $o(\delta/h)$)で書ける道具が在庫に入ること。

## F393(2026-10-22、w_E05_621_lit = 書き下しの型、稿 `621_難問1_ιの正の側_文献の掘り起こし_2026-10-22.md` §1〜§2、判定文 worklog (研究ノート: `2026-10-22_w_E05_621_lit.md`) §0)難問 #1 (E4) の ι>0 の側(全ての大きい λ で $h\ge c\lambda$)を、**既存の文献の定理か、ポーラロンの有効質量の冪の下界の方法の移送**で取る方式(族 D5:Lieb–Loss 2002・1999、Hainzl–Seiringer 2002、Hiroshima–Ito 2005、Hiroshima–Spohn 2005、Bach–Hach 2020/2022、Chen 2003・2008、Dybalski–Spohn 2020、Betz–Polzer 2022、Brooks 2024、Sellke 2024、Frank–Seiringer 2019;在庫の Spohn 1987・BMSV 2023・Lieb–Seiringer 2014/2019・Bach–Ballesteros–Mlinarzik 2026;新規取得の Feynman 1955・Lieb–Thomas 1997・Frank–Lieb–Seiringer 2012・Ricaud 2016)
- **閉じたもの(R3)**:**方式**(文献に既存の定理が無く、移せる方法も無い)。ι の真偽・道 (e) は閉じない。
- **札**:D5-A = ABSENT(α 固定・全ての大きい λ で $h\ge c\lambda^\gamma$、γ > 0 の定理は PARTIAL も含めて無い;PF の非摂動の下界は HS05 Cor 3.2 の $h\ge1$ だけ);D5-B = NOGO-方式。
- **理由(原典の字面)**:(1) PF の質量くりこみの文献は摂動の係数(HS05 Thm 4.1・HI05 Thm 2.9)、固定の Λ・小さい α(HS02 Thm 1・Chen08)、エネルギーだけ(LL99 Thm 1.1・BH22・BBM26)で、HS05 p.5 は「大きい λ の技法は無い」、LL02 p.3 は曲率の質量の終端を "We cannot prove this"。(2) 方法ごとに PF で破れる段:Jensen(Spohn 87 (3.2)、本人が「有用な評価が無い」)は J のスペクトル測度の集中;Gauss 混合・点過程(BP22・BMSV)は PF の重み $e^{-\alpha Q/2}$ の正の Gauss 混合の表示(F190 (a));Gauss 支配(Sellke Rem 1.2)は基準の測度の Gauss 性(F99);束縛・外場の定義(LL02・Chen03・LS14)は要る量が $E(P)$ の上界そのもので循環;エネルギーの漸近は曲率に要る相対 $\lambda^{-19/7}$ の精度に冪で届かない。(3) Brooks 2024 の擬ブースト(E(0) の精度不要)は在庫の道 (e) と同型で、PF の入力(泡の率つきの集中・磁気の MF 汎関数の Hessian の非退化)を文献は供給しない。
- **共通点(1 行)**:**ポーラロンで質量の冪の下界を出した方法は全て、Fröhlich の重みの符号の構造(正の Gauss 混合・準凹性)か、Pekar の最小点の一意性・非退化と基底状態の集中という PF には未だ無い入力に依る;PF の文献は摂動・固定の Λ・エネルギーの水準に留まる。**
- **射程(T60)**:禁じるのは「照合した文献の定理・方法を ι>0 の側にそのまま当てる」発注。止めないもの:Brooks の擬ブーストの PF への 1 対 1 の写し(族 D7、w_E05_623)と道 (e) の入力 (B1′)(B2′) の証明;Spohn の本(CUP 2004)の量子部の照合。
- **再開条件**:(a) PF の $p\ne0$ の準自由の変分(Bach–Ballesteros–Mlinarzik の続報)か、磁気の Pekar 型(ベクトルの MF)汎関数の最小点の非退化の文献が出たとき、(b) PF の断熱の極限(裸の質量 → 0、切断固定)の着衣の質量を扱う文献が見つかったとき。
- **R9**:閉じたのは方式。双極子では $h=1+b_0\lambda$ が厳密(van Kampen、LL02 p.3)で文献の「くりこみ不能」の分類(HS05 (1.16))に入る —— 本行は双極子の結論を変えない;2 構造の擬交差の梯子には触れない。

## F394(E05、難問 #1 (E4) ι>0 の族 D3:経路の測度の拡散定数の上界を Gauss 支配・Gauss 混合(Sellke 2024・Betz–Polzer 2022・BMSV 2023・Mukherjee–Varadhan 2020・Spohn 1987)の PF への移植で出し、$h\ge c\lambda$(λ ≥ λ₁)を得る方式。2026-10-22、w_E05_619_path = 書き下しの型、稿 `619_難問1_ιの正の側_経路の測度とGauss支配_2026-10-22.md` §2〜§4、C0 999p・999q・999r)
- **閉じたもの**:**方式**(D3 の 2 つの型)。ι の真偽・(QC_κ) の真偽は閉じない。
- **理由**:(1) 混合の型(BP22・BMSV・MV20):Fröhlich の重み $\exp(+\alpha\iint g\,v)$ の正の点過程の展開が段 1;PF の重みは $\exp(-\frac{e^2}4Q)$(罰)で交代級数、場の表示は位相 —— 段 1 で不成立(F190 (a) と一致)。Spohn 87 の不等式は $m^*$ の上界で向きが逆、$m^*=1/D$ は PF で CLT が無い(F300)。(2) Sellke の型:支配の**向き**は破れない(C0 999p:全ての対称凸 K で $\nu(K)/\mu(K)\ge1.18$;999q・999r:連続の k 球で準凸性の必要条件〔半直線の単調性・中点〕は通る)が、**強さ**が足りない —— 観察 619-A($W(0,\tau)-W(y,\tau)\succeq0$:罰は変位で弱まり、Sellke の Prop 2.4 の「引力の減少から Gauss の閉じ込め」の類似は符号が逆)により比較の閉じ込めは双極子の域 $\lvert k\rvert R\le\delta$ からだけ、その自己無撞着 $h\ge1+c_d\alpha\delta^2h/C$ は小さい α で有界(値【T88】;線形の暴走は α ≳ 10〜10² だけ)。
  (3) 出力の形:消費者が要るのは T に一様な特性関数の下界 ⟹ $h_{\rm ls}$ の下界(監査 624 §2.1 の第 3 形;「拡散定数の上界 ⟺ 有効質量の下界」は同値でない)。GD の出力は対称凸の集合・関数の比較で、特性関数の下界の形でない($\cos$ は準凸でない)。Fröhlich で $m_{\rm eff}$ に届くのは混合の表示による CLT があるからで、PF にはない(F300)。連鎖の各段で log の損が入る(天井 λ/polylog λ、値)。
- **共通点(1 行)**:**Gauss の比較が使える強さは、経路ごとに位相が揃うモード(双極子の域)の強さで、その上限 $k_0\sim h$ が h 自身で決まるので自己無撞着は小さい α で有界 —— λ に線形な部分は位相の外れたモードの経路ごとの 2 次の下界 (QC_κ) にしか無い(F99 の枝 1〜4 の合流)。**
- **R9**:閉じたのは方式。双極子では Q は増分の非負 2 次形式で全段が自明に立ち h ∝ λ —— 障害は位相(変位依存)に局在;擬交差の梯子は経路の測度を持たず対象外。
- **射程(T60)**:禁じるのは「Fröhlich の混合・点過程の表示を PF に移す」「双極子の域のモードだけの Gauss 支配で λ に線形を出す」発注。止めないもの:(QC_κ)(窓の閉じ込め集合の上で $\mathbf 1_K e^{-\frac{e^2}4Q+\kappa\lvert\Delta b\rvert^2}$ が準凸の積、$\kappa\ge c\Lambda/R$)の真偽の判定;それが成れば自己無撞着で $h\gtrsim c^2\alpha^2\lambda/C$(値)。
- **再開条件**:(1) (QC_κ) の証明か、増分に依る 2 次形式 × 変位の核の型の重みに対する準凸性の一般の判定法が文献に出たとき;(2) PF の重みの正の Gauss 混合の表示(位相を使わないもの)が見つかったとき。

## F395(2026-10-22、w_E05_617_asym = 書き下しの型、稿 `617_難問1_ιの正の側_G-TKの道の漸近の組み立て_2026-10-22.md` §1 の 5.・§3 617-E (iv)、成算 S-E05-R1 の D1)筒の蓋の G-TK の道の E5(消費者の $\langle C_f\rangle\le C$)を、**571-H の第 2 項の主の項 $K_2$ だけで勘定し、生の G-TK の核($\sqrt{R^2-\rho^2}$ の側面)と門 $\lbrace G\ge G_0,\kappa_N\le\frac14\rbrace$ のまま漸近で組む方式**
- **閉じたもの(R3)**:**方式**(核と門の設計の 1 つ)。G-TK の道・命題 ι>0 は閉じない。
- **理由**:571-H の第 2 項 $\frac{CU_c\lvert Q\rvert}{b^2}(K_2+\frac{a^2}{b^2}K_2'+\frac{a^4}{b^4}K_2'')$ で、門の κ_N ≤ 1/4 は $\lvert a/b\rvert=\lvert F\rvert/G$ を押さえない(H が小さい配位)。生の核は側面 ρ → R で微分が発散し $K_2'$ は対数、$K_2''$ は格子の刻みの負冪で育つ。$\lvert a/b\rvert\sim D$ を許すと $(a/b)^2K_2'\asymp D^3R^{-4}\log$ を O(1) に保つのに γ ≤ 4/3($D=\ell^\gamma$)が要り、El の窓の下限 γ > 11/7(607-N)と両立しない。
- **共通点(1 行)**:**E5 の勘定を主の項だけで行い、Newton の歩の大きさ $\lvert F\rvert/G$ の項を門が押さえていなかった。**
- **再開条件**:核を尺度 εR で $C^\infty$ に均し、門に第 3 条件 $\lvert F\rvert/G\le R$ を足す(稿 617 §1 の 5.)—— そのとき 3 項とも $D/R^2$ の型で (E5) 1 つに収まる。第 3 条件の失敗は T8 の事象に入れる。
- **R9**:核と門の設計の閉鎖で、標的とも T8 とも同値でない。
- **射程**:605 §3.1 の E5 の勘定(主の項)と El の窓の冪の結論は変わらない;変わるのは門の設計と T8 の事象の広さ。

## F396(2026-10-22、w_E05_618_loclb = 書き下しの型、稿 `618_難問1_ιの正の側_局在した下界の族_2026-10-22.md` §4.2、成算 S-E05-R1 の族 D2)T8(近い筒の片側の揃った弱い窪み)を、手術(571-S0)の後の外の自由な部分 $H_{\rm ee}$ の相対エントロピー(Gauss の対数 Sobolev で $\le2\langle N_{\rm ee}\rangle$)とエントロピーの不等式 $\nu(S)\le(H(\nu\vert\mu)+\log2)/\log(1/\mu(S))$ で、真空の大偏差 $e^{-c\ell^2}$ を真の状態に移して取る方式
- **閉じたもの**:方式(射程)。T8 の事象の台(近い筒 $\lvert z\rvert\in[R,D]$)は手術の距離 D の内側で、外の自由な部分空間に入らない —— 道具が当たらない。命題 T8 の真偽は閉じていない。
- **理由**:エントロピーの道は自由な調和の系(真空の Gauss が基準)の周辺分布にしか効かず、内の部分は泡と電子を含む。
- **残るもの**:外の場の事象(D より外)の道具としては使える見込み(値、未書き下し)。T8 は費用/MF ∼ $\lambda^{-3/7}$ の壁型(稿 §1.5)で族 D7 へ移管。
- **再開条件**:T8 の事象を手術の外へ移す G-TK の核の変更(近い筒を D の外へ)が見つかったとき。

## F397(2026-10-22、w_E05_620_toy = 書き下しの型、稿 `620_難問1_ιの正の側_簡単な模型の練習_2026-10-22.md` §5.1〜§5.3、成算 S-E05-R1 の D4)難問 #1 (E4) の ι>0 の側を、**比較の不等式**(可解な模型・反跳を持たない部分模型・反跳の係数 η の族との比較)と、**c 数の変位の試行(補題 275-A = E05-P147)に ψ0 の圧搾を入れる型**で出す方式 —— 閉じたのは**方式**(ι>0 の真偽・泡の慣性の型 501-X は閉じていない)
- **何を試したか**:候補 K1(反跳を持たない部分模型との比較、補題 620-A)、K2(η の族、観察 620-B)、K3(275-A + (SQZ))、K5(可解な模型との作用素の不等式)を、判定文を先に固定して当てた(C0-A・C0-C、worklog (研究ノート: `2026-10-22_w_E05_620_toy.md`))。
- **理由**:(1) K1:PF の全てのモードは反跳を持ち S = ∅、$h\ge1$ しか出ない。(2) K2:$h_\eta(\lambda,\alpha)=h_{\rm PF}(\eta^2\lambda,\alpha/\eta^2)$ で η の族は PF の $\alpha\lambda$ 一定の曲線;η の単調性が在っても上界の向き。(3) K5:作用素の不等式 $H(P)\ge K(P)$ は $E(P)$ の下界しか与えず、h の下界に要る $E(P)-E(0)\le P^2/(2c\lambda)$(E(P) の上界)の向きに効かない。(4) K3:275-A の分母の反跳の項 $\Phi(k_jf)$ は ∂E 型で、補題 620-C(Robertson)によりその圧搾は共役の ∂A 型 $\Phi(ik_jf)$ の反圧搾を要する;J-G の泡は A² の項で場を $\Omega_p/\Lambda\sim\alpha^{5/7}\lambda^{2/7}\gg1$(値)で硬くし A 型を圧搾する —— 泡の中の f では分母が真空より大きく、$h_W$ は 1 ループの対数以下の向き(冪 0、値)。
- **共通点(1 行)**:**比較・変位の型は運動量を「A の配位のずれ」で運ばせ、その運動量の変化が E 型の揺らぎ(k² の重み)を払う —— 反跳を持つ PF ではこの費用を消す構造が無く、泡は逆にそれを増やす。**
- **閉じたもの(R3)**:方式。止めないもの:場の配位の同変な汎関数で E を変位させる型(501-X、E05-P263)—— 反跳の費用が恒等的に 0 で、慣性は圧搾の壁が担う(稿 §5.4、値で $h_{\rm LP}\sim\ell\lambda$〜$\ell^2\lambda$)。
- **再開条件**:ψ0 が ∂A 型の直交位相を泡の中で反圧搾していることを示す入力(J-G の平均場の向きと逆)が出たとき(K3);E(P) の上界を与える等式で結ばれた可解な族が PF に見つかったとき(K5)。
- **R9**:双極子では反跳の項が無く 275-A は等号で ι>0 —— 閉鎖と矛盾しない;2 構造の擬交差の梯子は場が無く適用外。
- **照合(監査の型)**:F137 の再開条件の字面「$B_\perp$ または ∂A の圧搾の情報」は、$\tilde f$ が実・偶なら 620-C と逆の向き —— 稿 275 の規約で確かめる。

## F398(2026-10-22、w_E05_625_IRfirst = 書き下しの型、稿 `625_難問1_ιの正の側_IRの切断を先に入れて外す_2026-10-22.md` §1・§2、判定文 C0-625 = worklog (研究ノート: `2026-10-22_w_E05_625_IRfirst.md`) §2、成算 S-E05-R1 の族 D8、C0 990a)難問 #1 (E4) の ι > 0 を、IR の切断(光子の質量 μ)を先に入れた模型で示し、Chen の IR の RG の鎖(572-T‴ = E05-P309、P300〜P305)を**下界の向き**に読んで μ → 0 で外す方式(監査 624 §3 行 7・§5.1 の族 D8)—— 閉じたのは**方式**(ι の真偽・μ についての質量の単調性は閉じていない)

- **何を試したか**:起動前に固定した判定文の条項 A(鎖の入力の用途を 572 §1.1・§2.2、573 §8.1・§16、577 §1.2・§5 の字面で照合)と、条項 B(検算:泡の尺度 $\mu_b=\kappa/R_*$〈κ ∈ {1/4, 1, 4}〉と移しの段の窓の比、980c の 976a の行で λ = 1e5〜1e9)。
- **理由**:(1) **窓の不両立**(検算、F353 の再確認):障害(F341 の中央値・F367 の El の赤外の対数)は μ ~ 泡の尺度で自動に消えるが、その μ で移しの段の小ささは $\alpha\mu_b/m$ = 3.6e4〜1.4e9 倍・$\gamma_V(\mu_b)$ = 1.6e4〜7.3e8 で摂動でない(局所冪 0.84〜0.87 ≈ 6/7、κ に依らない)。移しが立つ μ ≲ $c_*m/\alpha$ の模型は帯 $m/\alpha\lesssim\lvert k\rvert\lesssim1/R_*$ の光子を全て持ち、障害は消えない。(2) **曲率の両側**(条項 A、決め手):下界の向きの結論 $h_{\rm ls}(\lambda,0)\ge(1-C\epsilon)h_\mu$ には尺度 μ の曲率の上界($h_\mu\gtrsim\lambda$ = 標的の μ 版)が要り、RG を回すには (S3) $\nabla^2E^\mu\ge M_\mu^{-1}$ と (S4) の $M_\mu$ の尺度の正則性(572-F の $\langle VRV\rangle\le\frac m2$、多円板の参照、各段の自由部分の下界の $(\partial^2E^\sigma)_-$)が要る —— #3 の上側・F349 の壁の μ 版。凹性 $\partial^2\le1/m$ は逆向きしか与えず、$\partial^2E^\mu\ge-C/m$ も在庫に無い。F351 (3) の停止条件。
- **共通点(1 行)**:**IR の切断を泡の尺度に置けば赤外の障害は消えるが移しが摂動でなくなり、移しが摂動で立つ尺度($\lesssim m/\alpha$)まで下げれば模型は元の難しさをほぼ全て持ち、しかも移しの鎖は曲率の両側を入力に要る —— 難しさは「尺度 μ の質量の両側の評価」へ移るだけで減らない。**
- **R9**:双極子では μ の上の質量・移し・標的とも真(閉鎖と整合);2 構造の擬交差の梯子では、μ の上で枝の質量が $M_{\rm LP}$ でも μ 未満で枝が入れ替わりうる —— 片側の移しは偽になりうる(空でない)。
- **射程(T60)**:禁じるのは「光子の質量(IR の切断)μ を入れた模型で ι>0 を示し、Chen–BCFS–CFP 型の多尺度の鎖(572-T‴ の型)を下界の向きに読んで μ → 0 で外す」発注 —— μ の取り方(泡の尺度・$m/\alpha$・その間)に依らない。止めないもの:多尺度の鎖を使わない片側の比較(μ についての質量の単調性 $h(\lambda,0)\ge h(\lambda,\mu)$ の型)、IR の切断つき模型を集中の段の**練習**に使うこと(移しを主張しない)。
- **再開条件**:(1) 尺度 μ ≲ $m/\alpha$ の曲率の下界 (S3)(S4)(F349 の再開条件 (N1) の μ 版、F351 の再開条件)が在庫に載ったとき;または (2) PF のファイバーで μ についての質量の単調性(または $h(\lambda,0)\ge c\,h(\lambda,\mu)$ の非摂動の比較)が出たとき。

## F399(2026-10-22、w_E05_623_brooks = 書き下しの型、稿 `623_難問1_ιの正の側_Brooks2024の段の移植_2026-10-22.md` §4、成算 S-E05-R1 の枝 D7)難問 #1 (E4) ι>0 の側の MF の水準の下界の冪の率を、**Lieb–Thomas 1997 の段 IV(コヒーレント状態の下の記号、誤差 = 有効なモードの数)**で出す方式(監査 624 の角度 2)—— 閉じたのは**方式**(初等の勘定;値)
- **理由**:PF の古典(コヒーレント)の汎関数の最小は A = 0(F141 (b))で、MF の泡のエネルギーは「泡のモード ~ $\ell^3$ 個 × 零点の硬さ $\Omega\sim\ell^2$」の和(MF ~ $\ell^5$)。下の記号の誤差は 1 モードあたり ω の単位で 1(固定のスクイーズ r の分解でも $\cosh2r\sim\Omega$)で、電子の箱 L の IMS $\lambda/L^2$ と合わせて $\min_L(\ell^7L^{-2}+L^3\ell^2)\sim\ell^5$ —— 誤差が MF の桁で精度 0。Fröhlich で効くのは主項が古典の振幅(コヒーレント)で誤差がモードの数 × 1 だからで、PF の泡は ⟨A⟩ = 0 のスクイーズ(568・F348)。
- **共通点(1 行)**:**PF の泡のエネルギーは零点の和で、モードごとの O(Ω) の誤差を許す道具(下の記号・コヒーレント状態)は全て精度 0 —— 誤差を Gauss で厳密に扱える 2 次の部分の外に置く型(系 601-B)だけが残る。**
- **R9**:双極子(泡なし)では MF の泡が無く適用外;擬交差の梯子は場の自由度が無く適用外。閉じたのは方式で、S4′・(BO-rank)・ι の真偽ではない。
- **射程(T60)**:禁じるのは「コヒーレント状態(固定のスクイーズを含む)の下の記号で PF の MF の水準の冪の率を出す」発注。止めないもの:LT の段 II(在庫 S1)、段 III の PF 版(系 601-B・(BO-rank) の型の集団の座標)、非調和の総量で押さえる型(稿 623 §6 の読み)。
- **再開条件**:PF の泡の主項を古典の振幅で書ける表示(例:スクイーズを古典の変数にする Gauss の位相空間の分解で、下の記号の誤差がモードあたり o(Ω) のもの)が見つかったとき。

## F400(2026-10-22、w_E05_623b = 書き下しの型(w_E05_623_brooks の再開)、稿 `623_難問1_ιの正の側_Brooks2024の段の移植_2026-10-22.md` §9、判定文 worklog (研究ノート: `2026-10-22_w_E05_623_brooks.md`) §B1(C0 の前に固定)、成算 S-E05-R1 の枝 D7、C0 a623e)難問 #1 (E4) ι>0 の T8・(BO-rank)・S4′ の芯(壁型の事象を見分ける精度)を、**BO の面の非調和の部分の総量が壁の余裕より小さいこと**で局在せずに押さえる方式 —— 閉じたのは**方式**(値 + 初等の勘定)
- **何を試したか**:a623a の MF の玩具(α = 1、c = λ/2、ω ≡ 1)に常磁性の結合と相関を入れ、電子の励起を物理の切断(運動量 ≤ π)で取って、反磁性の 4 次 $A_2$、常磁性の非調和の尺度 $A_{4p}=B_pn_1$、混合 $A_{3m}$ の和 $A_{\rm tot}$ / MF を λ = 1e5〜1e9 で並べた。
- **理由**:$A_{\rm tot}$ = 1.26e-2・6.2e-3・3.2e-3・1.68e-3・8.9e-4、ln ℓ の局所冪 −2.43・−2.14・−2.02・−1.97(K0:切断を 0.5・2 倍で比 0.56・1.86、冪の差 ≤ 0.05)—— 要る精度 $\ell^{-3}$(620 §8、NUM-7720 の $\lambda^{-0.42}$)より 1 冪遅い(札 NOGO、最終)。機構:非調和の分は泡の体積の格子点ごとに O(1)(絶対で ~ℓ³)、壁の慣性の精度は外の縁の面積 × 厚さ λ⁰(~ℓ²)—— 体積 対 面積。常磁性は 2 次では実の状態で反磁性との交差が消え q の 2 次(W₀)に入り、非調和には $n_1\sim\ell^{-2}$ を通して入る。
- **副産物の訂正**:稿 623 §6 の「$A_2\sim\ell^{-3.2}$」(反磁性だけ)は連続の格子の電子の紫外を拾った切断の人工物 —— 物理の切断で $\ell^{-2.0}$(稿 623 の訂正注記)。
- **共通点(1 行)**:**非 Gauss の部分を全体(体積)で数える型は、壁(面積)の余裕に 1 冪足りない —— 局在して壁の近くだけを数える型(S4′・(BO-L) の本体)に戻る。**
- **R9**:双極子(泡なし)では余裕が 0 で消費者の前提が立たず空虚;擬交差の梯子では非調和(交差の方向の折れ目)が余裕を越え偽になりうる —— 閉じたのは方式で、S4′・(BO-rank)・ι の真偽ではない。
- **射程(T60)**:禁じるのは「BO の面の非調和の総量(大域、局在なし)を S4′ の誤差の上界にして壁型の事象の余裕と比べる」発注。止めないもの:壁の近くに局在した非 Gauss の分の評価(S4′ の局在の型)、非 Gauss の得 ε の 2 次の型(4 次の揺らぎの 2 乗 / 隙間)の見積もり。
- **再開条件**:非 Gauss の得の上界が、総量でなく壁の近くの面積に比例する形で(局在せずに)書ける恒等式・対称性が見つかったとき。

## F401(2026-10-22、w_E05_618c = 書き下しの型、稿 `618_難問1_ιの正の側_局在した下界の族_2026-10-22.md` 第 3 部 §13・§14、判定文 worklog §10、C0 a618c)T3′-b の芯の中心のずれ(因子 M)を、**平の重心の第 1 層 $X_\theta$ のまま第 2 層だけを局所の窓(半径 ∼ 2R_*)の重心にする**設計で消す方式
- **閉じたもの**:方式。第 1 層の誤差 $vM/(1+v)$ が局所の窓の半径を越えると第 2 層は泡を捕まえ直せない(玩具 a618c:v = 0.2・M ≥ 30 で誤差 5〜50R);ゆえに $v\lesssim1/M$ がやはり要る。
- **閉じないもの**:T3′-b。第 1 層を最頻値(局所の窪みの質量の soft-argmax)にすると M は消える(補題 618-C、命題 618-T3b)。
- **再開条件**:なし(最頻値の版で置き換え済み)。

## F402(2026-10-22、w_E05_627_seam = 書き下しの型、稿 `627_難問1_ιの正の側_継ぎ目571-Sの漸近_2026-10-22.md` §1・§2、判定文 worklog (研究ノート: `2026-10-22_w_E05_627_seam.md`) §1、成算 S-E05-R1 の族 D9、C0 997x (a))617-T の名指し (N-S) の字面 —— 571-S0 の分解で面の位置を厚さ O(1) の殻で平均し、継ぎ目を**定数の右辺** $C_\delta\lvert\Sigma\rvert\log(2+R_{\rm IR})$ に押さえる形 —— は偽:閉じたのは**命題の真偽**(字面の形)
- **何を試したか**:617 §4 の (N-S)「$H_{\rm box}-E_{\rm box}\ge(1-\delta)(H_{\rm ee}-E_0(H_{\rm ee}))-\mathrm{El}-C_\delta\lvert\Sigma\rvert\log(2+R_{\rm IR})$」を、α = 0(El = 0)と Weyl のずらし(コヒーレントな状態)で検査。
- **理由**:命題 627-F —— α = 0 の (N-S) は $\rho:=\sup_qq_{\rm e}\Omega^2_{\rm ee}q_{\rm e}/q\Omega^2q\le1/(1-\delta)$ と同値(左辺 − 右辺 = 2 次のハミルトニアン $H_f-(1-\delta)H_{\rm ee}$ が下に有界 ⟺ そのポテンシャルが半正定値)。面を横切る尺度 L の長波は外の成分に段差を作り $\rho\gtrsim L$;格子の鋭いスペクトルの切断で ρ = 1.97・3.32・6.07・11.62(L = 16〜128、局所冪 0.93、札 NS_LITERAL_FALSE)。平らな面では α > 0 でも(悪い向きを電子から面に沿って遠ざけ El の $a^2$ の係数 → 0)全ての λ で偽。面の位置の平均は段差の振幅を小さくしないので助けない。
- **共通点(1 行)**:**継ぎ目の余り $T_\Sigma$ は内の場の振幅(段差)を測る配位の量で、真空では面積 × 定数だが配位ごとには有界でない —— 定数に吸収する形は偽;配位の項のまま確率(591-T の Gauss の裾)で払う。**
- **R9**:閉じたのは (N-S) の字面の形。正しい形(補題 627-A:$H_{\rm ie}\ge-\delta(H_{\rm ee}-E_0)-\delta^{-1}T_\Sigma$、最適)と、617 段 4 での確率の払い(系 627-C)で型 I は保たれ、残りは名指し (N-S′)(真空の跡の面積 × polylog の上界)。ι>0・617-T の道は閉じていない。
- **射程(T60)**:禁じるのは「継ぎ目を全ての状態で定数(面積 × log)に押さえる作用素の不等式」を名指し・仮定として立てる発注(面の位置の平均つきでも)。止めないもの:配位の項 $T_\Sigma$ を残して 597-A′/627-C で払う形、真空の跡の評価 (N-S′)。
- **再開条件**:なし(627-A が上位の形)。

## F403(2026-10-22、audit_S2_617_618_620 = 監査の型、監査稿 `626_合同監査_集中攻撃の617と618と620_2026-10-22.md` §1.1、成算 S-E05-R1 の D1)門の上の消費者の $C_f$ を、**θ の層の重心 $X_\theta$ を中心とする 2 次の展開の根への Newton の n 歩**(稿 571 §11.1・補題 571-H = E05-P306)で潰し、勾配の因子 $\lvert\Pi_n\rvert\le(2\kappa_N)^{2^n-1}$ で $C_f(X_\theta)$ の先験の多項式の上界を打ち消す方式(定理 617-T 段 3 第 1 項の字面)
- **閉じたもの**:**方式**(2 次の展開の Newton の勾配の評価)。E5 そのもの・定理 617-T の組み立て・門の事象は閉じていない —— 修理版(核を毎歩置き直す Newton と Kantorovich の門)は監査人の補題 626-H(self-audited、独立確認待ち)。
- **根拠**:$\nabla X_n=[1-b\Delta_a-c\Delta_b+F'''\Delta_c]\nabla X_\theta+\dots$ で、前半(固定した 2 次式の Newton の始点微分)は 2 次で縮むが、展開の係数 $c=H(X_\theta)$ の $X_\theta$ への依存から来る $F'''\Delta_c$ は $-F'''\delta^{*2}/(2q'(\delta^*))$ に収まり n で縮まない。門は $\lvert a/b\rvert$ を R の桁まで許し、均した核で $F'''\sim G/R^2$ ゆえ係数は ℓ に依らない定数 —— $C_f(X_\theta)$ の多項式の上界を打ち消せない。数値(3 次の F、R = 10):a/b = 0.5 で $\Pi_n$ = 5.0e-2・1.45e-3・1.39e-3(n = 1・2・≥3)、主張の上界 1.0e-1・1.0e-3・1.0e-7;a/b = 2 で 3.28e-2 に飽和。陰関数の式で同じ値(1.388e-3)。
- **共通点(1 行)**:**場の汎関数を「配位に依る点」に置いた量の場の微分で、置き場所を通る連鎖律の項を落とす** —— 本監査の段 4 の Agmon の f の $C_f$(626 §1.6)と同じ型の落とし。
- **射程(T60)**:止めないもの —— 核を毎歩置き直す Newton($\partial_X\Phi=FH/G^2$ は 2 階まで)、Kantorovich の門 $\lvert a\rvert(\lvert c\rvert+4\frac{\lvert a\rvert}bU_cK_3)/b^2\le\frac18$。玩具の値(979h:典型の配位で $\lvert\delta X\rvert\lvert H/G\rvert\le0.06$)は反例と矛盾しない(典型では $F'''$ の項が小さい)。
- **再開条件**:なし(626-H で置き換え;626-H の独立確認が FAIL なら再検討)。
- **R9**:決定的な補題の評価の閉鎖で、標的とも名指しとも同値でない。

## F404(2026-10-22、w_E05_618d = 書き下しの型、稿 `618_難問1_ιの正の側_局在した下界の族_2026-10-22.md` 第 4 部 §21・§22、判定文 worklog §15(値の前に固定、解析の類 C)、成算 S-E05-R1 の族 D2)難問 #1 (E4) ι>0 の T8((N-8):G-TK の門の F の側の失敗)を、**門・推定子の設計の変更で体積型の事象に作り直す**方式 —— 3 案:(a) 門の第 2・第 3 条件を窪みの体積の統計(分位点)で定める;(b) 根の関数 F を θ の水準の平らな頂の指示 d で作る(T8 を Φ57・618-S′ の対称差で罰せる形に読み替える);(b′) Newton をやめて平らな頂の 1 層の重心にする
- **閉じたもの**:方式(札 NOGO、K1・K2 とも成)。
- **理由**:(K2)G-TK の核は $k=-\int^za$ で、G の正の部分を距離 D の蓋に置くと筒の全長で $\lvert k\rvert=W/(2\pi R^2)$;片側の窪み δm は根を $`\delta X\approx\delta m\,L/(2(\bar m_{\rm cap}-\bar m_{\rm core}))`$ 動かし、W に依らない(てこの長さの恒等式)—— 門の失敗は δm ≳ R/D の弱く広い窪み、費用 $\ell^{4-\gamma}$ ≪ MF;筒を短くすると El の窓 T9(γ > 11/7)と両立しない。(a) は F を替えないので根のずれが残り、F を分位点にすると 626-H (ii) の C_f の評価が壊れる。(K1)平らな頂の帯の水準 $\ell^{-\kappa}$ について、E5(C_f = O(1))は κ ≤ 4/3(MF の連続の輪郭;620 §8 の値の薄い壁でも κ ≤ 1.75)、近い所の余分の窪みを MF の定数割合の費用で罰する(体積型)には κ ≥ 2 —— 窓が空。
- **共通点(1 行)**:**滑らかな根の関数(小さい C_f)と、窪みの判定の θ の尺度(体積型)は ℓ の約 1 冪で両立しない;間の水準の近い殻 $[R,D_s]$ の窪みは MF の精度で見えず、手術は El の窓の内側に届かない。**
- **残るもの**:T8 (N-8) は名指しのまま —— 芯は「電子の手術が届かない近い殻の、MF より細かい局所の下界」(611 §3.3・F400 と同じ所)。要求が多項式 $`1/(\ell\,{\rm polylog})`$ に下がっても(監査 626)、MF の水準の Markov は $\varepsilon_{\rm JG}\ell^2$ で役に立たない。
- **R9**:双極子では門の事象が空虚;擬交差の梯子では片側に広がる構造で偽になりうる —— 閉じたのは方式で、T8 の真偽ではない。
- **射程(T60)**:禁じるのは「G-TK の核のまま門・推定子の重みの水準を替えて T8 を体積型にする」発注。止めないもの:近い殻の局所の下界そのもの(El の窓より内側の手術、または電子に相対な局所の Hardy の作用素の形)。

## F405(2026-10-22、w_E05_627b = 書き下しの型、稿 `627_難問1_ιの正の側_継ぎ目571-Sの漸近_2026-10-22.md` 第 2 部 §8.2・§8.5、成算 S-E05-R1 の族 D9)617 段 4(T5、筒の蓋)の継ぎ目の余り $\delta^{-1}T_\Sigma$ を、**体積の評価(補題 627-V)または面積 × R の評価(627-T′ の粗い版、$\lVert1_E\Omega^{-1}P_T1_E\rVert\lesssim R$)**で $m_H/8$ の下に払う方式 —— 閉じたのは**方式**
- **何を試したか**:$\langle T_\Sigma\rangle_{\rm vac}\le\lVert\Omega\rVert\dim W_{\rm ext}\le\frac{2\pi^2}3\mathrm{vol}(\mathcal E)$、および $\langle P_{\rm ext}c_p,\Omega^{-1}P_{\rm ext}c_p\rangle\le t^{-2}\lVert c_p\rVert^2\lVert1_E\Omega^{-1}P_T1_E\rVert$ を 597-A′/627-C の $b_\Sigma^2$ に入れる。
- **理由**:蓋の外の領域の体積 ≍ $R^2D$、面積 × R ≍ $R^2D$ で、Hardy の余裕 $m_H\asymp(1-\delta)\Psi'DR^2$ と同じ冪 —— 条件は $\frac{32\pi^2}3\le\delta(1-\delta)\Psi'$ という定数の比較になり漸近で勝たない(Ψ′ は段 0 の定数)。
- **共通点(1 行)**:**継ぎ目の余りを体積で押さえる評価は、余裕が体積に比例する段(T5)では定数の綱引きになる —— 体積の小さい割合(o(体積) = 面積 × o(R))の評価が要る —— 面積 × polylog は十分条件で必要ではない(監査 655 §1.1:617-T′ 段 4 の条件は $\langle T_\Sigma\rangle\le\varepsilon_0\mathrm{vol}$、ε₀ は段 0 の定数)。余裕が体積より冪で大きい段(T7:μ ≍ ℓ⁵ ≫ b³)では体積で足りる。**
- **R9**:閉じたのは方式。(N-S′) の真偽は開いたまま(値 997z は CAP_POLYLOG で支持)。T7 の継ぎ目は同じ評価で閉じた(稿 §8.4)。
- **射程(T60)**:禁じるのは「T5 の継ぎ目を体積の評価・面積 × 蓋の径の評価で払う」発注。止めないもの:有界な面での $P_{\rm ext}c_p$ の $\Omega^{-1}$ の重みの局所の評価、格子の curl* の分解(稿 §8.6)。
- **再開条件**:Ψ′ の下界が紫外の定数 $32\pi^2/3$ を越える在庫が載ったとき(見込みは薄い)。

## F406(2026-10-22、w_E05_629_shortlever = 書き下しの型、稿 `629_難問1_ιの正の側_T8のてこを短くする_2026-10-22.md` §2・§3、判定文 worklog (研究ノート: `2026-10-22_w_E05_629_shortlever.md`) §1(C0 の前に固定)、C0 a629a、成算 S-E05-R1 の族 D10)難問 #1 (E4) ι>0 の T8(G-TK の門の F の側)を、**筒の長さ D を R の定数倍に縮めて(てこを短くして)空・体積型にし、同時に El の窓 T9 を D ∼ R で開く**方式 —— 3 案:(a) El を Gauss の裾でなく別の型で払う、(b) 蓋・芯の幾何を替えて 607-N の $R^3D^{-5}$ の R の冪を下げる、(c) $m_H$ を最大に取る(芯の水準と門の閾を下げる)
- **閉じたもの(R3)**:**方式**(札 NOGO)。T8・T9・命題 ι>0 の真偽は閉じない。
- **理由**:(i) D = cR では門の幅 $c_3R\asymp DU_c/c_G$ で T8 の筒の事象は決定的に空になり、571-H の第 2・第 3 項 $D^3R^{-4}c_G^{-4}$・$D^5R^{-6}c_G^{-6}$ は $c_G\ge\ell^{-1/6}$ で O(1)(成)。(ii) しかし 597-A′ は $\kappa_Wb_W^2\le m_H/4$・$b_W^2\ge2{\rm tr}\Gamma$ を要り、1 次の積率の条件 $\lambda E_{\rm box}{\rm tr}\Gamma\lesssim m_H^2$ は裾の型に依らない;607-N の ${\rm tr}\Gamma\lesssim R'^3D^{-5}$ と $m_H\asymp DR'^2/\theta_*$、$\theta_*\ge c_G\ge(D/R'^2)^{1/2}$(E5)で $7\gamma\ge12-\rho-2g$ 対 $\gamma\le2\rho-2g$ —— γ = 1 で 3 案とも不可、不足は最小 $\ell^3=\lambda^{3/7}$。蓋の正の重みは核の線ごとの釣り合いで芯の影の円柱に限られ、広い蓋は効かない。(iii) El と「T8 を空にする門」の両立 $\frac{11-2g}7\lt\gamma\le\frac{4-4g}3$ は g ≥ 0 で空(g = 0 が F395 の 4/3 対 11/7)。
- **共通点(1 行)**:**てこを短くすると手術が切る分極の雲の結合 El が $\alpha\mathrm{MF}(R/D)^5$ の桁に育ち、それを払う MF の桁の余裕(θ の水準の窪み)は E5 を ℓ の冪で壊す —— F404 の K1 の二律背反が El の窓に移っただけ。**
- **残るもの**:T8 (N-8)・T9 は名指し・段のまま。窓を動かすには、El を Cauchy–Schwarz の $1/\delta=E_{\rm box}/m_H$ なしで払う道具(断熱・ゲージの型)と、571-H の Newton の型の外の推定子(門の幅に比例する $K_2'$・$K_2''$ の項を持たないもの)の両方が要る;前者だけでは 571-H の第 2 項までで冪 0 の 1 点 $D=\ell^{4/3}$、第 3 項まで入れると空(C0 の情報)。
- **R9**:双極子では泡が無く門の事象が空虚;擬交差の梯子では蓋の水準が構造ごとに替わり El の勘定の前提(蓋が真空の水準)が崩れうる —— 閉じたのは方式で、T8・T9・標的と同値でない。
- **射程(T60)**:禁じるのは「G-TK × 571-S0 × 597-A′ × 571-H(E5)の型のまま D・芯の半径・門の閾・裾の型を替えて T8 と El の窓を両立させる」発注。止めないもの:El の断熱・ゲージの型の作用素の評価(単独では窓を開かない)、Newton を使わない推定子の族の作り直し、T8 の近い殻の局所の下界(F404 の残るもの)。
- **再開条件**:(1) El を $\lambda\alpha{\rm tr}\Gamma$ の桁(Cauchy–Schwarz の損なし)で払う作用素の不等式と、第 2・第 3 項のない並進に共変な推定子の両方が在庫に入ったとき;(2) 真の状態の外の場の分散の**上界**が真空の値より R の冪で小さいことが示されたとき。

## F407(2026-10-22、w_E05_627c = 書き下しの型、稿 `627_難問1_ιの正の側_継ぎ目571-Sの漸近_2026-10-22.md` 第 3 部 §9.2、成算 S-E05-R1 の族 D9)T5(617 段 4、筒の蓋)の (N-S′) を、補題 627-H の τ を **Heinz の補間 τ ≤ √ρ と Hardy の型の ρ の評価**で押さえて閉じる方式 —— 閉じたのは**方式**
- **何を試したか**:τ ≤ √ρ と、ρ ≤ $4t^{-2}\lVert\Omega^2\rVert C_H(\mathrm{diam}E+1)^2$(体積の Hardy)、断面の Hardy(余次元 2 の線への Hardy は log で失敗)による ρ ≲ R² log(D/R)。
- **理由**:体積の Hardy は τ ≲ D で $\lvert\Sigma\rvert D\gg m_H\asymp DR^2$;断面の Hardy でも τ ≲ R√log(D/R) で $\langle T_\Sigma\rangle\lesssim\lvert\Sigma\rvert R\sqrt{\log}$ が $m_H$ に √log で負ける。値では ρ は線形(RHO_LINEAR)、τ は log(TAU_LOG)で、補間は τ の log の型を捉えない。
- **共通点(1 行)**:**τ を ρ(curl の重み)や $L^2$ の比較から補間で得る道は、$1_E$ の $H^{1/2}$ での log だけの非有界性を √(線形) に潰してしまう —— τ を直接($\Omega^{1/2}$ の重みで)評価する道が要る。**
- **R9**:閉じたのは方式。(N-τ)・(N-S′) の真偽は開いたまま(値は面積・log の側)。
- **射程(T60)**:禁じるのは「τ を補間と Hardy・体積の評価で押さえて T5 を払う」発注。止めないもの:τ の直接の評価(平板の k⊥ のブロックの 1 次元の問題 → 有界な面への局所化)。
- **再開条件**:ρ ≲ R^{2−ε}(断面の尺度で冪の余裕)の評価が在庫に載ったとき。

## F408(2026-10-22、w_E05_627c = 書き下しの型、稿 同上 §9.4、補題 627-N)連続の鋭い切断の模型で、**層への厳密な局在を持つ直交分解**(格子の 627-L の型:$`\mathrm{curl}\,W_{\rm ext}`$ が I の内部で 0、$`\mathrm{curl}\,W_{\rm in}`$ が E の内部で 0)を設計して継ぎ目の局在を回復する方式 —— 閉じたのは**方式**(命題として不可能)
- **理由**:帯域の場は整関数に延び、開集合で 0 なら恒等的に 0(Paley–Wiener + 一致の定理)。
- **共通点(1 行)**:**帯域の模型では局在は近似(Schwartz の裾)でしかありえない;継ぎ目の連続の評価は裾の定量化が芯。**
- **R9**:閉じたのは方式。近い局在の分解(607-N の滑らかな X)での (N-S′) は開いたまま;帯域の縁で切ること自体は値で体積の継ぎ目を生まない(997za、S_AREA)。
- **射程(T60)**:禁じるのは連続の模型で「E に台を持つ部分空間」を前提にする設計。止めないもの:格子の模型での curl* の分解(稿 §8.6)、連続の近い局在の評価。
- **再開条件**:なし(命題として不可能)。

## F409(2026-10-22、w_E05_631_T8sym = 書き下しの型、稿 `631_難問1_ιの正の側_T8の対称性と2次の積率_2026-10-22.md` §1〜§3、判定文 worklog (研究ノート: `2026-10-22_w_E05_631_T8sym.md`) §1(値・解析の前に固定)、C0 a631a、成算 S-E05-R1 の族 D11)難問 #1 (E4) ι>0 の T8((N-8′):G-TK の門の F の側の失敗)を、**回転の対称性(片側の窪みの平均は根を動かさない)+ 2 次の積率(Chebyshev)+ 場の相関の自由場の型の減衰**で、MF の精度を経由せずに払う方式
- **閉じたもの**:**方式**(札 NOGO:(a) 対称性 PASS、(b) 冪の勘定 NOGO)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。
- **理由**:(a) E05-F22 と推定子の立方体の回転群 O の共変性(動く立方体のブロック、原点中心の窓、両側の蓋の奇の核)で $\tau_{X^{(2)}}A$ の法則は O 不変、$\mathbb E\vec F(X^{(2)})=0$ —— 成る。(b) Chebyshev に要るのは $\mathrm{Var}F\lesssim(c_3RG_0)^2/(\ell{\rm polylog})$。全分散の法則 $\mathrm{Var}F\ge\mathrm{Var}(\mathbb E[F\mid\mathcal B])$(𝓑 = 泡の配位)で、方式の成功には泡の片側の形のずれ δ(θ より浅い近い殻の窪みの偏りを含む)の $\langle\delta^2\rangle\lesssim R^2/\ell$ が要る —— 618 §23・監査 626 §7 の要求と同じ(J-G の相対の精度 $\ell^{-1}$)。在庫の分散の上界(E05-P39・P32・591-T)は全て「真の場は真空より狭い」向きで、窪みも共通の揺らぎも押さえない。場の 2 次の汎関数では P39 の表示(虚の平均の Gauss の混合)から $\mathrm{Var}_\psi(\sum k_yQ_y)=\sum kk'[2C^2-4C\mathbb E_\mu cc']+\mathrm{Var}_\mu(\sum k_yc_y^2)$ —— 前の 2 項(真空の型)の上界は $D/R^4$・$D/R^3$ で親の勘定どおり γ < 2 で $1/\ell$ 以下(C0 a631a で冪 −2.29、予測 −2.2)、第 3 項(経路 = 泡の形の揺らぎによる共通の揺らぎ)は分離の距離で減衰せず払えない。
- **共通点(1 行)**:**対称性は共通の揺らぎ(泡を介した相関)の平均を消すが分散を消さない;積率の方法はどれも(R2:Jensen で全ての p)泡の片側の形の積率を要り、F404 の芯「近い殻の MF より細かい局所の評価」に戻る。**
- **残るもの**:T8 (N-8′) は名指しのまま。対称性と真空の部分は MF の精度なしに払える(本稿 §1・§2.3)ので、要るものは「泡の片側の形の 2 次の積率 $\lesssim R^2/\ell$」の 1 点に絞れた。
- **R9**:双極子では門の事象が空虚(共通の揺らぎも無い);擬交差の梯子では泡の形が構造の間を飛び共通の揺らぎが O(1) —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「推定子から見た場の対称性 + 自由場の型の塊の相関の減衰で、片側の窪みの確率を Chebyshev(または高い積率・Markov)で払う」発注。止めないもの:経路の測度 μ の上の絞りの和 $\sum k_yc_y^2$ の分散を経路の汎関数の集中で押さえる道(§2.3 の第 3 項、場の側は真空で済む)、泡の集団座標の有効な調和の揺らぎの評価。
- **再開条件**:泡の片側の形(θ より浅い水準を含む)の 2 次の積率 $\lesssim R^2/\ell$、または経路の測度の上の $\mathrm{Var}_\mu(\sum_{\rm cyl}c_y^2)\lesssim R^6/\ell$ が在庫に入ったとき(そのとき本方式の残りは §2.3 の前の 2 項で払える)。

## F410(2026-10-22、w_E05_617d = 書き下しの型、稿 `617_難問1_ιの正の側_G-TKの道の漸近の組み立て_2026-10-22.md` 第 5 部 §17・§18、判定文 worklog (研究ノート: `2026-10-22_w_E05_617_asym.md`) 第 5 部、成算 S-E05-R1 の族 D1)T8 (N-8′) を**事象ごと消す**ために、Newton(3 方向の G-TK の核の根)を外して最頻値の推定子 $X^{(2)}$ だけで消費者を満たす方式、および第 2 層を (a) 空間で滑らかにした $X^{(2)}$、(b) θ の水準の局所の重心、(c) 浅い水準 $g_w\asymp\ell^{-\kappa}$ の局所の重心、(d) 第 1 層も浅い水準、に替える方式
- **閉じたもの(R3)**:**方式**(T8 を消す設計の 5 案)。命題 T8・ι>0 は閉じない。
- **札**:NEWTON_NEEDED(解析の類 C)。
- **理由**:消費者のうち Newton の精度が要るのは 571-A/501-X の ⟨C_f⟩ ≤ C(E5)だけ;θ の水準の推定子は指示の遷移の帯が芯の内部に入り $C_f\sim\ell$(618 §21 K1、979g の $\ell^{1.2}$、617-M′ の上界)—— (a)(b) は帯を動かさず $\ell$ のまま;(c)(d) は $C_f$ を O(1) に下げるが、第 1 層を通る項または窓の中の帯の体積を通して「近い殻の浅い窪み」の事象の確率 $\lesssim\ell^{-1}$ を要し、これは費用 / MF ∼ $\ell^{\kappa-2}$ で体積型でない(618 §21 Q2)—— T8 と同じ型への付け替え。
- **共通点(1 行)**:**⟨C_f⟩ = O(1) には推定子の感度を泡の壁に集める層が要り(571-B の等号の条件)、その層の失敗はどう設計しても壁の位置・形の揺らぎ(近い殻・費用 ≪ MF)の事象になる。**
- **再開条件**:近い殻 $[R,D_s]$ の、泡の形の外れに比例する掛け算の局所の下界(618 §22・611 §3.3 の欠けた道具)が立ったとき、または消費者を 501-X の擬ブースト以外(E05-P7 の $h_{\rm ls}$ を ψ0 に基づかない試行で)に替える道が立ったとき。
- **R9**:方式の閉鎖で、標的とも T8 とも同値でない。
- **副産物**:Newton なしの版で定理 617-W($h\ge c\lambda^{6/7}(\ln\lambda)^{-k}$、類 B の名指しなし)。
- **射程の注(2026-10-22 監査稿 661 §2.4・§3.4)**:共通点の「どう設計しても」は、環の揺らぎを確率で押さえる局所の窓(2 層・Newton の基底)の建付けに限る。1 層・大域の窓の重心は環の窪みを窓の因子 $(\rho/\ell)^5$ に決定的に吸い、芯は到達距離の条件 $5(r(\kappa)-1)\lt1-\kappa$ と窓の縁の Agmon が λ を払うかの分岐 (R-λ0) に移る(F422・F425・E05-P353 の勘定と同じ)。

## F411(2026-10-22、w_E05_627d = 書き下しの型、稿 `627_難問1_ιの正の側_継ぎ目571-Sの漸近_2026-10-22.md` 第 4 部 §10.6、成算 S-E05-R1 の族 D9)有界な面の NP の部分 $\nu=\lVert\Omega^{1/2}\Pi_{V_{\rm NP}}\Omega^{-1/2}\rVert$ を、境界の局所ベクトルの横波への射影の Gram($\Gamma$、$\Gamma_A$、$\Gamma_{A^{-1}}$)の**作用素ノルムの積**で押さえる方式 —— 閉じたのは**方式**
- **何を試したか**:$\nu\le\lVert\Gamma^{-1/2}\Gamma_A\Gamma^{-1/2}\rVert^{1/2}\lVert\Gamma^{-1/2}\Gamma_{A^{-1}}\Gamma^{-1/2}\rVert^{1/2}$。
- **理由**:平板の Fourier の見積もりで $\Gamma\sim\lvert\xi\rvert$、$\Gamma_A\sim\lvert\xi\rvert^2\log$、$\Gamma_{A^{-1}}\sim1$(面の波数 ξ ∈ [1/R, 1])—— 2 つの比はそれぞれ ≲ log と ≲ R で、積は R log(周波数の食い違い);実際の ν は周波数ごとの積 $\sqrt{\lvert\xi\rvert^2\log\cdot1}/\lvert\xi\rvert$ = √log(平板で厳密、627-T_K)。
- **共通点(1 行)**:**NP の部分は面の周波数ごとに A の重みを合わせて初めて polylog —— 周波数を分けない作用素ノルムの評価は面の径の冪を失う。**
- **R9**:閉じたのは方式。(N-ν)・(N-S′) の真偽は開いたまま(値は POLYLOG)。
- **射程(T60)**:禁じるのは「Gram の作用素ノルムの積で ν を押さえる」発注。止めないもの:周波数を合わせる評価(箱の鏡映で周期の Fourier の掛け算へ写す、曲がった面の局所の Fourier)。
- **再開条件**:なし(周波数を合わせる道が上位)。

## F412(2026-10-22、w_E05_632_JGrate = 書き下しの型、稿 `632_難問1_ιの正の側_J-Gの収束の率の多項式化_2026-10-22.md` §1〜§4、判定文 worklog (研究ノート: `2026-10-22_w_E05_632_JGrate.md`) §判定文(C0 の前に固定)、C0 a632a、成算 S-E05-R1 の族 D12)難問 #1 (E4) ι>0 の T8((N-8′):G-TK の門の F の側の失敗)を、**J-G(MF)の下界の相対の精度を $\ell^{-1}$(polylog の損は可)に上げ、形の剛性 × Markov で泡の片側の形の揺らぎ $\langle\delta^2\rangle\lesssim R^2/\ell$ を出す**方式 —— 4 案:(i) ブロックの辺を ℓ の冪に(在庫の式のまま・549 の鋭い $K_V$・$K_V$ を polylog・Slepian を理想の $1/s$)、(ii) 局所の Lieb–Thomas、(iii) Frank–Seiringer 型の 2 次の補正、(iv) 集団のモードの 2 次の展開
- **閉じたもの(R3)**:**方式**(札 NOGO:J1 PASS・J2 NOGO・J3 FLAT_O1)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。
- **理由**:(i) 在庫の誤差の式 $\varepsilon_{\rm JG}\lesssim\nu^{-2}+\eta_F+s^{-1}+\sqrt{\log s/s}+M^3/(\alpha\ell^2)+\nu^2M^3s^2(31.4s+7\log_2\ell)^{18}/(\eta_F\ell^2)$(A-549-2 = E05-P291、560 §4)のパラメタを ℓ の冪で選ぶ LP の最良は $\ell^{-2/43}$(618 §10.2 の $\ell^{-0.05}$ と一致;天井は Hardy の剰余の $s^{20}$);鋭い $K_V$ で 2/17、$K_V$ を polylog で 2/7、理想の Slepian で 2/5、ν・$\eta_F$ の項を仮に消しても 2/3 —— ブロックの境界の損 $1/s$ と、強度を分解する粗視化の損 $(s/\ell)^2$ が同時に $\ell^{-1}$ 以下にならない($s\gtrsim\ell$ 対 $s\lesssim\ell^{1/2}$)。(ii) コヒーレント状態の下界は PF の古典場の汎関数の最小 A = 0 で空(F141 (b))。(iii)(iv) 泡の形は場の 2 次の観測量(強度)で古典場の点が無く、2 次の展開が要るのは電子を介した共通の揺らぎ(631 §2.3 の第 3 項)だけ —— J-G のエネルギーの精度を経由しない別の族。剛性は MF の O(1) 倍で平ら(976b:$e_*/\mu_0$ = 1.21〜1.29、ℓ = 5〜19)、要る精度 $\asymp1/\ell$ は緩まない。情報:鋭い帯域の Szegő の第 2 項は面積の項(1 次元で $R^0$、a632a・a632b)—— LDA の水準の下界は理想でも隙間 $c_S\mathrm{MF}/\ell$ を残し、要求の桁に定数でちょうど乗る(polylog の余白なし)。
- **共通点(1 行)**:**エネルギーの精度 × Markov で形の揺らぎを払う型は、下界の隙間に形と無関係な誤差(ブロックの境界・粗視化・LDA の面積の項)を全て抱え、そのどれもが相対 $\ell^{-1}$ の桁かそれより大きい —— 形の揺らぎの真の値($\ell^{-6}$ の桁、断熱の比 $\ell^{-3}$ の 2 乗)の余裕は、エネルギーの側でなく揺らぎを直接測る側にある。**
- **残るもの**:T8 (N-8′) は名指しのまま。要るものは 631 の残りと同じ「泡の片側の形の 2 次の積率 $\lesssim R^2/\ell$」—— 経路の測度 μ の上の $\mathrm{Var}_\mu(\sum_{\rm cyl}c_y^2)\lesssim R^6/\ell$ を、電子の隙間 $\asymp\alpha\ell^5$ と場の振動数 $\asymp\alpha\ell^2$ の比 $\ell^{-3}$(断熱)による時間の脱相関で押さえる道。
- **R9**:双極子(泡なし)では J-G の MF は自明で T8 の事象が空虚(方式は空虚に成る);擬交差の梯子では MF の最小点が 2 つで剛性が 0 に近い方向が生じ要る精度はさらに厳しい —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「J-G(BO + ブロックの強度で場の配位を分ける型)の相対の精度を上げ、形の剛性 × Markov(またはエネルギーの隙間を使う積率の評価)で T8 の形の揺らぎを払う」発注(ブロックの辺・ν・$\eta_F$・$K_V$・Slepian の改良の組み合わせを含む)。止めないもの:非局所の MF そのもの(粗視化なし)と比べる下界の型の偵察(Szegő の第 2 項まで含む精度、J-G の型の外)、経路の測度の上の分散を断熱の比で押さえる道(631 の残タスク)、J-G の率の改善を他の段(562-P の率など)に使うこと。
- **再開条件**:泡全体を粗視化なしに扱う(電子の $\inf_\varphi$ と場の $\inf\sigma$ の入れ替えを局所化なしで行う)下界が在庫に入り、その誤差が相対 $o(1/(\ell\,{\rm polylog}))$ のとき;または Szegő の面積の項の係数 $c_S$ を下界の側に含めた 2 項の J-G が立ったとき。

## F413(2026-10-22、audit_S2_617T2_618 = 監査の型、監査稿 `630_合同監査_617T修理版と618のT3primeb_2026-10-22.md` §1.2・§8.1、成算 S-E05-R1 の D1)3 方向の G-TK の核の Newton(稿 617 第 4 部 §10.1)を、**1 次元の 626-H の門を軸ごとに写した門**(Hessian の対角 $\kappa_N^{(i)}$ と純の 3 階 $K_3^{(i)}=\int\lvert\partial_i^3k^{(i)}\rvert$ だけ)で Kantorovich の量 ≤ 1/8 に押さえる方式
- **閉じたもの**:**方式**(門の量の選び方)。3 方向の Newton・定理 617-T′・(N-8′) の型は閉じていない —— 正しい門は監査人の補題 630-H3(self-audited、独立確認待ち)。
- **根拠**:3 方向の Newton の歩は横にも $\lvert s\rvert\le2\lvert\vec F\rvert/b$ 進み、Kantorovich に要るのは球の上の Hessian 全体。長い筒の核(断面の半径 R、長さ D、振幅 $R^{-2}$)では横の 2 階の先験 $U_c\int\lvert\partial_\perp^2k\rvert\asymp U_cD/R^2$、横の 3 階 $U_c\int\lvert\nabla^3k\rvert\asymp U_cD/R^3$ —— 門の第 3 条件 $\lvert\vec F\rvert/b\le c_3R$($c_3$ は ℓ に依らない)の下で Kantorovich の量は $\asymp c_3U_cD/(G_0R)\asymp\ell^{\gamma-1}\to\infty$。軸の対角の量は横の曲率(m が筒の横で非対称な配位で非零)を見ない。
- **共通点(1 行)**:**1 次元の評価を成分ごとに写して、多次元の反復が横に動く分の微分(非対角・横の高階)を落とす** —— F403(展開の中心を通る連鎖律の落とし)・628 §1.4(横の座標の依存の欠け)と同じ型。
- **射程(T60)**:止めないもの —— Hessian 全体を門に入れ $c_3^2:=G_0/(128R^2U_cK_3)$、$K_3:=\int\lvert\nabla^3\vec k\rvert_{\rm HS}$($c_3\propto(R/D)^{1/2}$)とする門、または球の上の Hessian の sup を門にする版(630-H3 の注 (c))。
- **再開条件**:なし(630-H3 で置き換え;630-H3 の独立確認が FAIL なら再検討)。
- **R9**:決定的な補題の門の選び方の閉鎖で、標的とも名指しとも同値でない。

## F414(2026-10-22、audit_S2_617T2_618 = 監査の型、監査稿 `630_合同監査_617T修理版と618のT3primeb_2026-10-22.md` §2.6 穴 2・§8.3、成算 S-E05-R1 の D2)T3′-b の芯の事象 $\lbrace\beta(X)\gt\beta_0\rbrace$($\beta$ は $U_c$ で飽和した $m_c(u')$ の芯の平均)を、**τ で飽和した $g_\tau$ の辺 b の立方体の平均 $g_b$ の窪みの指示 d = $\tilde\chi(g_b)$ の芯の中の割合**で下から捉える方式(稿 618 §17 の包含 $S\subset\lbrace d\lt1\text{ の割合}\ge p_0\rbrace$)
- **閉じたもの**:**方式**(事象の包含の作り方)。618-T3b の結論・T3′-b の閉鎖は閉じていない —— 𝒮 := β($X^{(2)}$) を直接使う監査人の補題 630-S(self-audited)で置き換え。
- **根拠**:真空のブロックは $g_\tau$ に高々 τ しか足さないので、芯に真空のブロックが一様に割合 $f_v\le g_s/(2\tau)=1/(2\rho a_T)$ で散った配位では芯の全ての点で $g_b\le g_s/2$(d = 1)、一方 $m_c$ は $U_c$ まで上がるので β ≈ $f_vU_c$ —— $\beta_0/U_c\lt f_v\le1/(2\rho a_T)$ の配位は S に入るが d < 1 の点が無い(β₀ は小さい定数、$\rho a_T\gt4$ —— 窓は一般に空でない)。
- **共通点(1 行)**:**飽和の水準の違う 2 つの観測量(τ で飽和した平均と $U_c$ で飽和した平均)を、閾の上で同じ事象と読む** —— 626 §4.5 の飽和の係数 $L(g)$ の非一様と同じ根。
- **射程(T60)**:止めないもの —— 𝒮 を 602-T3 の芯の水準そのものに取り、良い配位の上界を 618-S′ の $D^+$(格子のブロックの $u'\le u_s$)から直接出す形(630-S)。$\rho a_T\gt U_c/(2\beta_0)$ と ρ を大きく取る設計でも包含は回復するが、ρ と β₀ の順序の条件が増える。
- **再開条件**:なし。
- **R9**:事象の包含の作り方の閉鎖で、標的とも名指しとも同値でない。

## F415(2026-10-22、w_E05_627e = 書き下しの型、稿 `627_難問1_ιの正の側_継ぎ目571-Sの漸近_2026-10-22.md` 第 5 部 §11.1、判定文 worklog (研究ノート: `2026-10-22_w_E05_627e.md`) §1、成算 S-E05-R1 の族 D9、C0 997ze)連続の鋭い帯域の模型で、(N-S′) を **(N-τ)(τ = ‖Ω^{1/2}P_ext Ω^{-1/2}‖² の polylog の上界)経由**で示す方式 —— 閉じたのは**方式**(連続の t = ½ では (N-τ) は値で偽)
- **何を試したか**:格子の 627-H(跡 ≤ ½‖Ω‖|P_Σ|(1+τ))の道を連続へ。連続の平板の k⊥ のブロックで τ を厳密な Fourier の表示で測った。
- **理由**:TE の τ は log² の型だが、**TM の τ は 1/k⊥ の冪**(1.55 → 33.4、N = 16〜512、局所冪 ≈ 1、札 CONT_TAU_POWER)—— TM の束縛(NP 型)のモードが X の連続スペクトルの中の ½ に埋まった共鳴を、しきい値 t = ½ が切る。加えて連続には 627-L(層への局在)が無く、τ から跡への道そのものが無い。
- **共通点(1 行)**:**連続では帯域が X に連続スペクトル (0,1) を与え、NP のモードがそこに埋まる —— 格子の「掛け算の $1_E$ + 有限次元の NP」の分解(627-S)が連続に移らない;跡はブロックごとに直接評価する(TE は 627-E で閉)。**
- **R9**:閉じたのは方式。(N-S′) の真偽は開いたまま —— 真空の跡そのものは連続の平板で面積の型(CONT_AREA:0.0705 → 0.1068、N⊥ = 8〜64、比 1.06)。
- **射程(T60)**:禁じるのは「連続の T5 を τ の polylog で閉じる」発注。止めないもの:ブロックごとの跡の直接の評価(TM の Friedrichs の模型)、しきい値 t₀ ≠ ½ の設計(t₀ = 0.75 で τ_TM は polylog —— 値)。
- **再開条件**:しきい値を ½ から離す設計が採られたとき(そのとき τ の道は値で生きる —— ただし連続の 627-L の代わりは別に要る)。

## F416(2026-10-22、w_E05_631b = 書き下しの型(w_E05_631_T8sym の再開)、稿 `631_難問1_ιの正の側_T8の対称性と2次の積率_2026-10-22.md` 第 2 部 §7・§8、判定文 worklog (研究ノート: `2026-10-22_w_E05_631b_T8time.md`) §1(値の前に固定)、C0 a631b、成算 S-E05-R1 の族 D11)難問 #1 (E4) ι>0 の T8 の残り(F409 の第 3 項 = 真の場の 4 次のキュムラント κ₄ の筒の和、補題 631-K)を、**断熱の比 $\ell^{-3}$(場 $\alpha\ell^2$ / 電子の隙間 $\alpha\ell^5$)による経路の測度の時間の脱相関**で $\lesssim R^6/\ell$ に押さえる方式(族 D12 = 稿 632 の提案)
- **閉じたもの**:**方式**(札 NOGO:U1 PASS、U2 NOGO)。T8・(N-8′)・命題 ι>0 の真偽、形の揺らぎの値は閉じない。
- **理由**:窓の和 $c_y$(窓 $\tau_f$ ≲ ℓ)の κ₄ は、速い部分(電子、$\sim\tau_e/\tau_f$)と遅い部分(BO の遅い変数 = 場の形、$\sim\min(1,\tau_s/\tau_f)$)の和で、遅い部分は $\tau_e$ に依らない(混合の Gauss の厳密な式;C0 a631b で τ_e を 3 桁動かして変化 ≤ 0.1%、遅い部分 × τ_f/τ_s = 1.44〜1.60 で一定)。断熱の比は速い部分だけを縮め(632 の $\ell^{-6}$ はこれ)、遅い部分には $\tau_s\lesssim\tau_f/\ell$ —— 真の H(0)(隙間なし)の形の観測量の低いエネルギーのスペクトルの重みの上界、エネルギーの分解能で MF に対し相対 $\ell^{-3}$ 以下 —— が要る。静的に言い直すと BO の場の問題の基底状態の非 Gauss 性(S4′/(BO-rank)、F400、P321 の非主張)。在庫(P315・P321・P323・P325・597-B)は全て静的で、時間の相関・スペクトルの重みの道具は無い。
- **共通点(1 行)**:**断熱の分離は電子を速く脱相関させるが、形の揺らぎは BO の遅い変数そのもので、その脱相関には遅い部分の動力学(MF より細かいエネルギーの分解能)が要る —— F404・F409 の芯「近い殻の MF より細かい評価」の時間の版。**
- **残るもの**:T8 (N-8′) は名指しのまま。要求は補題 631-K で、固定の中心の代理について「真の場の κ₄ の筒の和 $\lesssim R^6/\ell$」と書ける(推定子の中心を入れた形は未確定 —— 監査 634 §1.3)(630-H3 の門では $R^7/(D\ell)$、形の換算で相対 $\ell^{-\gamma}$)。
- **R9**:双極子では泡が無く κ₄ の遅い部分も無い(空虚に成る);擬交差の梯子では遅い変数が構造の間を飛び κ₄ が O(1) —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「電子の時間尺度(断熱の比)の脱相関・BO の分離だけで、場の形の揺らぎの 2 次の積率・κ₄ を払う」発注。止めないもの:形の観測量の低いエネルギーのスペクトルの重みの直接の評価(壁の外の絞られない場との結合を分けて)、BO の場の問題の非 Gauss 性の局在した評価(S4′ の局在の型)。
- **再開条件**:真の H(0) の形の観測量について低いエネルギーのスペクトルの重みの上界、または BO の場の問題の基底状態の非 Gauss 性の局在した上界が在庫に入ったとき。

## F417(2026-10-22、w_E05_599c = 書き下しの型、稿 `599_難問1_ιの正の側_G-BOFのHFB型の参照_2026-10-22.md` 第 3 部 §11〜§13、判定文 worklog (研究ノート: `2026-10-22_w_E05_599.md`) §11・§17(C0 の前に固定)、成算 S-E05-R1、C0 999Tb・999Td・999Tsc)G-BOF の壁の余裕を、横の玩具 T の非対角の Gauss の参照で**電子の参照を模型 P の対角の点に固定したまま**(自己無撞着にせず)測る方式
- **閉じたもの**:**方式**(参照の作り方)。電子の跳びを固定した参照 H では余裕 $\Delta_T$ = 41.6・43.4(1e5・1e6)で Hartree-P の 0.44・0.17 倍(§11 の字面の札 T_SHRINK、暫定)だが、電子を前の Γ の横の分散から取り直す自己無撞着の反復で参照のエネルギーは 121・842 下がり、余裕は 78.2・221.4(0.82・0.85 倍)に動く(§17 の札 T_KEPT_SC、暫定)—— 非自己無撞着の参照の余裕は、参照の取り方の産物で桁で動く。
- **根拠**:値【T88】;1e5 は反復 8 で収束(写像の比 0.52、Aitken 78.17 対 78.23)、1e6 は反復 3・4・5 の外挿 221.4 対 反復 8 の 212.5(K-AIT 通る)。
- **共通点(1 行)**:2 次の HFB の形の参照を、Gauss の状態に整合しない電子の参照(縦を含む模型の対角の点)の上で立てると、電子の跳びの繰り込み(横の分散だけが効く)が食い違い、壁の両端の差が参照の誤差に埋もれる。
- **射程(T60)**:止めるもの —— 非自己無撞着の参照で壁の余裕・対比の λ 依存を読むこと(§11 の札 T_SHRINK を G-BOF の余裕の消滅と読むこと)。止めないもの —— 自己無撞着な参照(§17)、分散のある横の場(ω = |k|)、全次数で Γ を最小化する参照。確度は中(1e5・1e6 の 2 段;1e7 はジョブ未投入)。
- **再開条件**:自己無撞着でない参照と自己無撞着な参照の余裕の差が、ある段で余裕の 10% 以内になると示されたとき。
- **R9**:参照の作り方の閉鎖で、標的(ι > 0)の真偽に触れない。

## F418(2026-10-22、audit_design_T8_634 = 監査の型、監査稿 `634_設計の監査_T8の芯_2026-10-22.md` §3.2、判定文 worklog (研究ノート: `2026-10-22_audit_design_T8_634.md`) J3(値の前に固定)、C0 a634a、成算 S-E05-R1)難問 #1 (E4) ι>0 の T8 (N-8′) を**事象ごと迂回する**ために、617-W(Newton なし)の推定子の窪みの指示を浅い水準 $g_w\asymp\ell^{-\kappa}$(κ < 2、2 層とも)に替えて E5(⟨C_f⟩ = O(1))を満たし、失敗の事象(近い殻の浅い窪み、費用 / MF ∼ $\ell^{\kappa-2}$)を **J-G の率の改善 × Agmon の可視性**(Markov でなく、局所の下界の誤差 $\varepsilon_{\rm JG}\ll\ell^{\kappa-2}$ だけを要る形)で払う方式 —— T8・(N-S′)・G-TK の手術を全て要らなくする道
- **閉じたもの(R3)**:**方式**(値の窓の閉鎖)。T8・(N-8′)・ι>0 の真偽、漸近の $\kappa_{\rm E5}$ の値は閉じない。
- **理由**:窓 $2-\rho\lt\kappa\le\kappa_{\rm E5}$(ρ = J-G の相対の率の冪、$\kappa_{\rm E5}$ = ⟨C_f⟩ = O(1) となる最深の水準)。F412 でブロックの J-G の率は構造上 ρ ≤ 2/3(境界 1/s × 粗視化 $(s/\ell)^2$)ゆえ $\kappa_{\rm E5}\gt4/3$ が要る。618 K1 の連続の輪郭の解析は $\kappa_{\rm E5}=4/3$(境界ちょうど)、C0 a634a の値は $\kappa_{\rm eff}$ = 1.75 で局所冪 1.21・1.13、1.44 で 0.45・0.66(上向き)、1.13 で −1.06・−0.46 —— $\kappa_{\rm E5}\in(1.13,1.44)$、618 K1 の薄い壁の読み 1.75 は支持されない。窓は空か測度 0(境界でも polylog の損で $h\gtrsim\lambda/{\rm polylog}$ どまり)。
- **共通点(1 行)**:**推定子の感度を薄くするほど(浅い水準)失敗の事象は浅く広くなり、それを見るのに要る局所の下界の精度は、ブロックの J-G の構造の天井を越える —— F404 の K1 の二律背反は Agmon に替えても残る。**
- **副産物(閉じていない)**:窓が空でも、水準を $2-\rho(1-\delta)$ に取れば 617-W は $h\gtrsim\lambda^{1-a(2-\rho)/7}$(a(κ) は浅い水準の 617-M′ の型の上界の冪)に強まる見込み(在庫の ρ = 2/43 で冪の利得は $10^{-2}$ の桁、値)—— 監査 634 §5 の族 C。
- **R9**:双極子では泡が無く推定子の前提が立たない(空虚);擬交差の梯子では壁の輪郭が構造ごとに替わり $\kappa_{\rm E5}$ が定まらない —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「ブロックの J-G(率の天井 2/3)の下で、指示の水準を浅くして T8 を Agmon で迂回する」発注。止めないもの:ブロックを使わない下界(監査 634 の族 D)で ρ > 2/3 を得る道;漸近の壁の輪郭が連続の MF より鋭いこと($\kappa_{\rm E5}\gt4/3$)の証明;族 C の率の内挿。
- **再開条件**:(1) 相対の率 ρ > 2 − $\kappa_{\rm E5}$ の局所の下界(非ブロック)が在庫に入ったとき;(2) 漸近の $\kappa_{\rm E5}\gt4/3$ が示されたとき(そのとき ρ ∈ (2 − $\kappa_{\rm E5}$, 2/3] で窓が開く)。

## F419(2026-10-22、audit_S2_617W = 監査の型、監査稿 `635_合同監査_617Wとその在庫_2026-10-22.md` §3.5、成算 S-E05-R1 の族 D9)継ぎ目の余りの真空の跡を、**$P_{\rm ext}$ と Ω の可換を暗に使う跡の等式** $`\mathbb E\lVert\mathrm{curl}\,q_{\rm e}\rVert^2=\frac12\mathrm{tr}(P_{\rm ext}\Omega P_{\rm ext})`$ で $\lVert\Omega\rVert\dim W_{\rm ext}$(体積)に押さえる方式(補題 627-V の証明、E05-P337)—— 閉じたのは**方式(証明の段)**
- **何を試したか**:627-A (c) の $`T_\Sigma\le\lVert Qg\rVert^2+\lVert\mathrm{curl}\,q_{\rm e}\rVert^2`$ の第 2 項の真空の期待値を $\frac12\mathrm{tr}(P_{\rm ext}\Omega P_{\rm ext})\le\frac12\lVert\Omega\rVert\dim W_{\rm ext}$ とする。
- **理由**:$q_{\rm e}=P_{\rm ext}q$ の共分散は $P_{\rm ext}\Gamma_0P_{\rm ext}$ ゆえ正しくは $\frac12\mathrm{tr}(P_{\rm ext}\Omega^2P_{\rm ext}\Omega^{-1})$;$W_{\rm ext}$ は $1_{\mathcal E}$ のスペクトルの部分空間で Ω と可換でない(2×2 の反例 Ω = diag(1, 4)・P = (1,1)/√2 の射影で 5.31 対 2.5;格子 N = 8・10 で真値は 4〜11% 大きい、値)。赤外の重み $\Omega^{-1}$ が入り、確かに言えるのは $`\lVert P_{\rm ext}\Omega^{-1}P_{\rm ext}\rVert\le\frac8\pi\mathrm{diam}\,\mathcal E`$(t = ½)を掛けた体積 × 径(監査人の補題 635-V)。
- **共通点(1 行)**:**$P_{\rm ext}$(空間の局在の射影)と Ω の関数の跡は、可換を仮定すると赤外の重みを落とす —— 局在した部分空間の上の $\Omega^{-1}$ は領域の径で育つ(F405・627-H の τ と同じ量)。**
- **R9**:閉じたのは証明の段。627-V の主張文の真偽は未確定(格子の値では成る)。T7 の継ぎ目は 635-V(率 $\delta^{-1}\ell^{-1}\ln\lambda$)で名指しなしのまま閉じる;T5 は F405 のまま。
- **射程(T60)**:禁じるのは「$P_{\rm ext}\Omega^aP_{\rm ext}$ の跡を可換として扱って継ぎ目・El の真空の跡を体積だけで押さえる」段。止めないもの:635-V の体積 × 径、627-H の τ による評価、格子の 627-L の層の局在。
- **再開条件**:$\lVert P_{\rm ext}\Omega^{-1}P_{\rm ext}\rVert$ を径に依らず押さえる在庫(連続の帯域で $W_{\rm ext}$ の元の赤外の重みが有界)が載ったとき。

## F420(2026-10-22、w_E05_640_famD = 書き下しの型、稿 `640_難問1_ιの正の側_非局所のBogoliubov精度の偵察_2026-10-22.md` §1・§2、判定文 worklog (研究ノート: `2026-10-22_w_E05_640_famD.md`) §判定文(C0・解析の前に固定)、C0 a640a、成算 S-E05-R1 の族 T8-D)難問 #1 (E4) ι>0 の T8((N-8′))を、F412 の再開条件の 2 本 —— (i) **Szegő の面積の項を下界の側に含めた 2 項の J-G**、(ii) **粗視化なしの下界**(電子の $\inf_\varphi$ と場の $\inf\sigma$ の入れ替えを局所化なしで)—— を**在庫の道具で**立て、MF の下界の相対の精度を $o(1/(\ell\,\mathrm{polylog}))$ にして剛性 × Markov で形の揺らぎを払う方式(偵察)
- **閉じたもの(R3)**:**方式**(札:J1 NOGO・J2 IN・J3 NOGO、C0 a640a AREA)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。
- **理由**:(i) 632 §2.1 の J-G の誤差の式の等号の項は在庫 2/43 から仮説の上限 2/3 まで ν⁻²・$\eta_F$・Slepian・Hardy の剰余・ブロックの境界 $1/s$・粗視化 $(s/\ell)^2$ で、LDA の床 $c_S/\ell$(C0 a640a:3 次元・横波で ≈ 0.63/ℓ、面積の項)はどの段でも律速でない —— 面積の項を下界に含めても上限 $\ell^{-2/3}$ は動かない(箱の尺度の Landau–Widom の第 2 項を含めるのは理想の Slepian の 2/5 の中)。(ii) 入口 $H\ge H_f+e_{\rm el}(A)$ は E05-P315(v-b)に在り、値では隙間は相対 ~ℓ⁻² で余裕があるが、入れ替えは:形の空間の IMS は壁(ρ → 0)で先験の評価 $\langle\int\rho A^2\rangle\le E_0/C_W$ が効かず T8/E5 の量(C_f の型)に戻る;押し縮めた Gauss の族 $U_\rho$ のまわりの 2 次の下界は在庫に無く(F386・F389)、Fröhlich の型(Frank–Seiringer・Brooks–Seiringer)は古典場の点を要る(F141 (b)・F399);2 項の Szegő は固定の面の漸近の公式(Sobolev 2010、抄録で照合)で ρ に一様な不等式でない。
- **共通点(1 行)**:**面積の項は J-G の律速でなく、粗視化なしの下界では要る精度が全て MF の多様体の近い域の 2 次の下界に局在する —— エネルギーの側から T8 に当たる道は「押し縮めた Gauss の族のまわりの Bogoliubov の型の下界」1 本に絞られ、その道具が無い。**
- **R9**:双極子(泡なし)では MF の多様体は真空で方式は空虚に成る;擬交差の梯子では多様体が 2 成分で、近い域の下界が成っても形の揺らぎの上界は偽になりうる —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「Szegő の面積の項(または箱の Landau–Widom の第 2 項)を J-G のブロックの型の下界に足して F412 の上限を越えようとする」発注と、「粗視化なしの BO の下界の入れ替えを、形の空間の IMS(壁を見る座標)・コヒーレントの下の記号・2 項の Szegő の漸近で行う」発注。止めないもの:MF の多様体の近い域(泡の内部の低い q の強度の集団の座標 O(1) 個 + 並進)の 2 次の下界を、ρ に依る押し縮めの枠のまわりの作用素の不等式として立てる道(634 の族 A と合流;第 1 手は有限モードの玩具の類 C);遠い域の大域の J-G の形ごとの版の照合(557-P の配位ごとの下界から)。
- **再開条件**:押し縮めた Gauss の族のまわりの 2 次の下界(電子の応答の負の 4 次を Bogoliubov のエネルギーで押さえる不等式、誤差 $O(\ell^{-2}\mathrm{polylog})$ MF)が在庫に入ったとき;または 2 項の Szegő の型の**不等式**(ρ に一様な剰余 $o(\ell^{-1})$)が文献に見つかり、かつ粗視化なしの入れ替えが別の道で立ったとき。

## F421(2026-10-22、w_E05_637_famA = 書き下しの型、稿 `637_難問1_ιの正の側_T8族A_外の縁に局在したS4primeと再中心化_2026-10-22.md` §2・§4、判定文 worklog (研究ノート: `2026-10-22_w_E05_637_famA.md`) J1 (b)(値の前に固定)、C0 a637a・a637b、成算 S-E05-R1 の族 T8-A)難問 #1 (E4) ι>0 の T8((N-8′):G-TK の門の F の側の失敗)を、**BO の面の非 Gauss を壁の外の縁に局在して外の縁の慣性の余裕と比べる(局在した S4′)**方式と、**固定の内の領域の Euclid の履歴に条件付けた外の場の Gauss 性(Schur の床)で外の窪みを払う**方式(監査 634 §3 の候補 1)
- **閉じたもの**:**方式**(2 つ)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。
- **理由(局在した S4′)**:a623a/a623e の MF の玩具(α = 1、c = λ/2、ω ≡ 1、κ = 1)で、外の縁 $E_1=[R_{50},\infty)$ に局在した非 Gauss の尺度 $A_{{\rm tot},E_1}$ と慣性 $M_{E_1}=\int_{E_1}4\pi r^2\sigma'^2$ の比 Q = 2.45・2.10・1.97・1.92・1.90・1.91・1.875(λ = 1e5〜1e11)、ln ℓ の局所冪は最上の 2 区間で +0.02・−0.06 —— 冪 0 で定数 ≈ 1.9、GO の閾 1/4 の約 7.5 倍(札 NOGO;域 $E_2$・$E_3$、切断 κ = 0.5・2 でも Q ≥ 1)。機構:非 Gauss の密度は泡の内で平ら(0.113/点、体積)で縁にも同じ桁で掛かり、慣性の密度は縁だけ(最大 0.036/点);外の縁の厚さ(λ⁰)が分子・分母で同じなので比は定数。
- **理由(Schur の床)**:密度が内の履歴だけに依れば外の場は条件付きで $N(Lx,S)$、Anderson で窪みの下の裾は Schur の Gauss 以下(観察 637-F、初等)—— ただし床は**固定の**領域の外だけを押さえ、泡の位置の揺らぎ(電子の枠で ~R)を覆う領域を要するので壁を O(R) の精度でしか止めない;再中心化した領域では Markov が崩れ、局所集合の強い Markov でも外の窪みを内の形の揺らぎに帰着するだけ;PF(P39)では虚の平均が窪みを起こしやすくする向きで、床には外のブロックの ρ の小ささ(El の型の尾)が要る。
- **共通点(1 行)**:**非 Gauss・窪みを空間で局在して数えても、外の縁の厚さは分子と分母で同じなので冪は勝てず(定数で負け)、外を条件付きの Gauss で押さえても難しさは内の形の揺らぎ(再中心化した壁の位置)に戻る —— 監査 634 §2.1 の共通点(泡の形の集団の揺らぎそのものを押さえる道具がない)の内側。**
- **残るもの**:T8 (N-8′) は名指しのまま;要求の確定形は補題 637-R(sup の門なら主の条項は $\langle\lvert\Delta\rvert^2\rangle\lesssim c_3^2R^2/\ell$)。
- **R9**:双極子では泡が無く分子・分母とも空虚;2 構造の擬交差の梯子では非 Gauss とずれ Δ が O(1)・O(R) になりうる —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「BO の面の非 Gauss の尺度(a623e の型、局所密度の項を含む)を外の縁に局在して慣性の余裕と比べる」発注と「固定の領域の条件付きの Gauss の床で壁型の事象を払う」発注。止めないもの:局所密度の補正(LDA)を汎関数に吸収した後の非局所の残りと余裕の比較(値では余裕の 0.10 倍、稿 §3 —— 新しい角度「LDA で着せた S4′」)、形のモードの差のエネルギー(族 B)。
- **再開条件**:非 Gauss の得のうち局所密度の関数でない部分だけを誤差に残す下界(着せた汎関数に対する Gauss の最適性)の道具が在庫に入ったとき。

## F422(2026-10-22、w_E05_639_famC = 書き下しの型、稿 `639_難問1_ιの正の側_617Wの率の内挿_2026-10-22.md` §3(命題 639-N)、判定文 worklog (研究ノート: `2026-10-22_w_E05_639_famC.md`) J2(値の前に固定)、C0 a639a、成算 S-E05-R1 の族 T8-C)難問 #1 (E4) の 617-W の率を上げるために、推定子の窪みの指示を浅い水準 $g_w\asymp\ell^{-\kappa}$(κ < 2)に替え、水準 w の失敗の事象(窓の縁・遠い浅い塊)を **T7 型の局所の手術**(613-A の機構、El は 597-A′ + 607-N)で払う方式(設計 W1)
- **閉じたもの(R3)**:**方式**(冪の算術)。617-W・639-W・T8・ι>0 の真偽は閉じない。
- **理由**:手術の余裕は $\mu(g_w)\propto b^3/g_w$(θ の水準の $\ell^{\kappa-2}$ 倍)、El は $\lambda b^3D^{-5}$ ゆえ届く距離は $D_s(w)\gtrsim\ell^{(7-\kappa)/5}=\ell^{1+(2-\kappa)/5}$。窓をそこまで広げると 617-M′ の型の決定的な上界の窓の因子 $(\rho/\ell)^5=\ell^{2-\kappa}$ が水準の利得 $2-\kappa$ をちょうど食い、$a_{\rm W1}(\kappa)=\kappa-1+5\max(0,\frac{7-\kappa}5-1)\equiv1$(全ての κ)—— 617-W の冪 6/7 から動かない。
- **共通点(1 行)**:**El の冪(電子の場への寄与の距離の減衰 $D^{-5}$)と、決定的な上界の窓の冪 5(体積 3 + てこ 2)が等しいので、手術で見る限り浅い水準の利得は窓の膨らみで相殺される —— 617 §18 (c) ② の冪の形。**
- **R9**:双極子では泡が無く空虚;擬交差の梯子では 618-S′ の一意の球が崩れ設計の前提が立たない —— 標的と同値でない。
- **射程(T60)**:禁じるのは「在庫の El の上界($p=5$)と 617-M′ の型の決定的な上界の組で、水準 w の事象を手術で払って 617-W の率を上げる」発注。止めないもの:J-G の可視性で払う設計(639-W、利得 e/7)、El の冪 p > 5 の評価、典型の値(帯の体積)を使う道(T8 の芯)。
- **再開条件**:El の評価 $\sigma^2\lesssim D^{-p}$ が p > 5 で在庫に入ったとき(a の利得 $(2-\kappa)-5\max(0,(7-\kappa)/p-1)$)。

- **注(2026-10-22 親)**:再開条件「El の冪 p > 5」は系 639-E(稿 639 第 2 部、self-audited)で満たされた —— コンパクトな立方体で p = 6(607-N の (a)(c) から;D⁻⁵ は筒の評価 (d) の流用)。W1 は命題 639-N′・定理 639-T で再開(S2 待ち)。

## F423(2026-10-22、w_E05_638_famB = 書き下しの型、稿 `638_難問1_ιの正の側_T8族B_形のモードの差のエネルギー_2026-10-22.md` §1・§4.3・§4.4、判定文 worklog (研究ノート: `2026-10-22_w_E05_638_famB.md`) §判定文(C0 の前に固定)、C0 a638a、成算 S-E05-R1 の族 T8-B)難問 #1 (E4) ι>0 の T8 (N-8′) を、**形のモードの差のエネルギーの下界**(W に共役な流れ $U_t$ でセクターを動かし、$\langle U_t^*HU_t-H\rangle$ の下界で $E_0$・J-G の局所化の絶対の誤差を相殺させ、Feynman–Hellmann の 1 次の項を Q に双対な W とセクターで吸う)で払い、他の形のモードとの 3 次の結合を**在庫の J-G の粗い強制性**で吸う方式
- **閉じたもの(R3)**:**方式**(類 C 札 BOUNDED;在庫の率では比が 1 を桁で越えて育つ)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。族 B の枠組み(補題 638-D・597-B′・命題 638-C・638-P)は残る。
- **理由**:差の形で $t^0$ の誤差は相殺するが、$t\langle B\rangle$ の 3 次の結合 $\frac t2T(g,a,a)$ を吸う粗い強制性の絶対の誤差が $\eta_B=\lVert T(g)\rVert_Q\varepsilon_{\rm JG}{\rm MF}$ で残り、$\eta_B\lesssim Kt_*$ には $\varepsilon_{\rm JG}\lesssim\varepsilon_{\rm need}=Kt_*/(\lVert T(g)\rVert_Q{\rm MF})$ が要る。976d の玩具(λ = 1e5〜1e9)で $\varepsilon_{\rm need}$ = 0.049→0.034、局所冪 0.06・0.10・0.45・0.48(尺度の勘定 $\ell^{-1/2}$;K ∝ ℓ^{3.1}、‖T‖_Q ∝ ℓ^{-0.96}、MF ∝ ℓ^{5.0})。在庫の率 $\ell^{-2/43}$ で比 $\varepsilon_{\rm JG}/\varepsilon_{\rm need}$ = 19〜26(冪 0.43 で育つ)。F412 の LP の理想の Slepian 2/5 も 1/2 に届かず、1/2 を越えるのは ν・$\eta_F$ の項が消える仮想の場合(構造の天井 2/3)だけ。
- **共通点(1 行)**:**差の形は誤差を t の 1 冪だけ有利にする(要る相対の精度 $\ell^{-1}\to\ell^{-1/2}$)が、他の遅い形のモードの粗い強制性をエネルギーの精度で供給する限り、J-G のブロックの型の率では届かない —— 難しさは「全ての遅い形のモードを同時に押さえる」側に残る。**
- **残るもの**:名指し (N-8B)(稿 §4.2:差の形の近い条項;値の勘定では粗い強制性の相対の精度 $o(\ell^{-1/2})$ と B の MF の線形化)。流れの仮定 (F) の欠損つきの版(§5 R1)。
- **R9**:双極子(泡なし)では W・Q が空で方式は空虚に成る;擬交差の梯子では $K_{\min}\to0$ で $\varepsilon_{\rm need}\to0$、方式はさらに厳しい —— 閉じたのは方式で、標的と同値でない。
- **射程(T60)**:禁じるのは「差の形の下界の 3 次の結合を、ブロックの J-G(在庫の P291、または F412 の (i) の改良の範囲)の粗い強制性で吸う」発注。止めないもの:非局所の MF(+ 局所密度の項、637 の族 A′)の下界で相対 $o(\ell^{-1/2})$ の強制性を出す道(族 D の型 —— Szegő の面積の項の床 $\ell^{-1}$ は要求に $\ell^{1/2}$ の余白で入る)、全ての遅いモードをセクターで縛る多モードの版、輸送の族の外も緩めた全 MF の Hessian での再測。
- **再開条件**:粗い強制性(状態の形の内容 a について $\langle H-E_0\rangle\ge cQ(a)-\varepsilon{\rm MF}$)が $\varepsilon=o(\ell^{-1/2}/{\rm polylog})$ で在庫に入ったとき。

## F424(2026-10-22、w_E05_653_borank = 書き下しの型、稿 `653_難問1_ιの正の側_G-BOFの(BO-rank)_2026-10-22.md` §2・§3、判定文 worklog (研究ノート: `2026-10-22_w_E05_653_borank.md`)「判定文」(C0 の前に固定)、成算 S-E05-R1 の族 B-r、C0 a653a)難問 #1 (E4) ι>0 の道 (B) G-BOF の律速 (BO-rank) を、**外の縁に局在した形で、集団の座標ごとの局在(補題 601-L・601-L′・系 601-B の IMS + 曲率の型)で書く**方式 —— 閉じたのは**方式**(値 + 初等の勘定);(BO-rank) の字面(λ に依らない有限個の座標)は値で偽の向き
- **何を試したか**:976d の Hartree の MF の点(反磁性、α = 1、対角の参照の Gauss)で、BO の面の Hessian $-\chi$($\chi=2c^2\Phi G'\Phi$)から (Q3) 非 Gauss の項の有効階数 $r=(\mathrm{Tr}\tilde K)^2/\mathrm{Tr}\tilde K^2$、(Q2) 2 次の非 Gauss の得 $\bar\varepsilon_2$ / 余裕、(Q4) 座標ごとの 601-L の型の費用 $\sum_y\pi\sqrt{3\chi_{yy}s_y}$ / 余裕 を λ = 1e5〜1e8 で(Hutchinson、門は全段で通る;1e9 は 5 分の規則で未測)。
- **理由**:札 TOOL_NOGO(q₄ = 71・89・137・220、ℓ の局所冪 +1.43)—— 座標あたりの費用は 1〜18 ω で、座標あたりの余裕(0.14〜0.19 ω)の 5〜100 倍;費用の大部分は泡の内部と壁の座標で、外の縁に局在しても減らない。札 RANK_AREA(r = 748・1757・3737・7804、冪 2.59・2.29・2.24)—— 集団の座標の数は面積の型で育ち、λ に依らない有限個でない(623 の「無限の階数」と同じ向き)。真の向きは閉じない:札 EDGE_SMALL(ε₂ / 余裕 = 0.150・0.120・0.117・0.115、冪 −0.05;ε₂ は ρ の小さい側に寄る)。
- **共通点(1 行)**:**凹の BO の面を Q(2 乗の座標)について下から押すには局在(弦・IMS)が要り、その費用は座標あたり曲率の √ の型(1 次)で、真の非 Gauss の得(座標あたり 2 次、≈ 0.02 ω)より桁で大きい —— 座標の数を外の縁(面積)に減らしても、面積 × O(1) の費用が面積 × 0.18 の余裕を越える。**
- **射程(T60)**:禁じるのは「(BO-rank) の集団の座標(外の縁に局在したものを含む)を座標ごとの IMS・弦・大域の幅で処理して S4′(PF)の ε を余裕の内に押さえる」発注。止めないもの:面積の個数の座標の 4 次の摂動に対する **2 次の型の作用素の下界**(640 §2.3 の近い域の 2 次の下界・F386 の再開条件と同じ欠け)、ε₂ の値の精密化(軟化した参照・常磁性・摂動を超えた値)。
- **再開条件**:座標あたりの局在の費用が曲率の 2 次(または座標あたり ≤ 0.1 × 余裕の面密度)になる下界の道具(例:Feshbach・Schur の補行列を下に有界でない 4 次の残りの上で使う構成)が在庫に載ったとき。
- **R9**:双極子(泡なし)では余裕 0 で空虚;2 構造の擬交差では電子の隙間が閉じて χ が発散し ε₂ も余裕を越えうる —— 閉じたのは方式で、S4′・ι の真偽ではない。

## F425(2026-10-22、w_E05_639b_famC2 = 書き下しの型、稿 `639_難問1_ιの正の側_617Wの率の内挿_2026-10-22.md` 第 2 部 §9.1(命題 639-N′)、C0 a639c、成算 S-E05-R1 の族 T8-C)617-W の第 2 層を浅い水準 κ にし、窓の縁の事象を**在庫の T7 の立方体の辺 b ≍ ℓ のまま**(618-G の $b=c_*\ell$)水準 w の手術で払って ι>0(⟨C_f⟩ = O(1))を得る方式
- **閉じたもの(R3)**:**方式**(冪の算術)。ι>0・(T7_w)・定理 639-T の真偽は閉じない。
- **理由**:El を系 639-E(p = 6)で払っても、b ≍ ℓ では $D_s(w)\asymp\ell^{(8-\kappa)/6}$、補題 639-M の第 1 項の冪は $a=(\kappa+4)/6\ge2/3$(κ > 0)—— ⟨C_f⟩ は ℓ の正の冪で育つ。617-W の冪は $1-(\kappa+4)/42$(κ → 0 で 19/21)まで上がる候補にとどまる。
- **共通点(1 行)**:**El の領域の体積 $b^4$ が手術の届く距離を押し上げ、窓の体積 ρ⁵ が浅い水準の利得を食う —— a < 0 には手術の領域を $\ell^{(1-\kappa)/5}$ 以下に縮める要がある(定理 639-T の設計)。**
- **R9**:双極子では泡が無く空虚;擬交差の梯子では 618-S′ が崩れる —— 標的と同値でない。
- **射程(T60)**:禁じるのは「手術の立方体を ℓ の桁のまま W1 で ι>0 を狙う」発注。止めないもの:小さい立方体(定理 639-T、名指し (T7_w))、β = 1 の版での 617-W の冪の改善。
- **再開条件**:El の評価が立方体の体積に対して $b^{q}D^{-6}$ で q < 4 になる(赤外の重み $N_{\mathcal E}$ を b より小さく押さえる)とき。
- **注(F422 の再開条件)**:F422 の再開条件「El の冪 p > 5」は系 639-E(607-N の立方体の系、p = 6)で満たされた —— W1 は小さい立方体で開く(定理 639-T)。

## F426(2026-10-22、w_E05_647_HS = 書き下しの型、稿 `647_難問1_ιの正の側_T8のHelffer-Sjöstrand表示_2026-10-22.md` §2〜§5、判定文 worklog (研究ノート: `2026-10-22_w_E05_647_HS.md`) §1・§1b(値の前に固定)、C0 a647a・a647b・a647c、成算 S-E05-R1 の族 T-E)難問 #1 (E4) ι>0 の T8((N-8′))を、**Q 空間の基底状態の変換と Helffer–Sjöstrand の共分散表示**($\mathrm{Var}_\mu O=\frac12\langle\nabla O,(L_\mu\otimes1+\mathrm{Hess}W)^{-1}\nabla O\rangle_\mu$、μ = |ψ|² = e^{-2W})と **Brascamp–Lieb の型の上界**(近い域の局所の凸性 + 非凸の部分は 617-Q の型の大偏差)で、再中心化した壁の位置の 2 次の積率 $\lesssim R^2\ell^{-\gamma}$ を出す方式
- **閉じたもの(R3)**:**方式**(類 C:a647a BOUNDED(判定文どおり)、補題の確認 a647b NOGO、情報 a647c)。T8・(N-8′)・命題 ι>0 の真偽は閉じない;真の μ の形の向きの凸性も主張しない。
- **理由**:(1) 恒等式は立つ(補題 647-D:実の掛け算の Dirichlet 形式、ファイバーの反跳の項は並進不変な観測量で 0;補題 647-K:PF の ψ は複素で $H-E\cong L_\mu-iv\cdot\nabla$ —— 作用素の同値は実の ψ のときだけ、ゆえに $L^{(1)}$ の下界は H のスペクトルから来ず、点ごとの Hess(−log|ψ|²) からだけ来る;その源の Brascamp–Lieb 1976 Thm 6.1 は実の $-\frac12\Delta+V$ で V 凸を要り、PF の複素の ψ にも BO の $V=\frac12\omega^2q^2+e_{\rm el}(A)$(凸 2 次形式の下側の包絡)にも当たらない)。(2) 補題 647-N(厳密):泡の形を潜在の変数とする Gauss の尺度の混合で $\mathrm{Hess}(-\log\mu)=\mathbb E_{\rm post}\Sigma_S^{-1}-\mathrm{Cov}_{\rm post}(\Sigma_S^{-1}q)$;自然な計量の最小の相対曲率は(Laplace)$(\tau-I_F)/(\tau+I_F)$ —— 形の向きの凸性 ⟺ 形の事前の分散 ≲ 場のデータの Fisher の分解能 $1/I_F$。(3) 値:泡の玩具(976d、e = 5〜9)で $I_F$ = 177 → 4907、T8 の要る分散 $R_s^2/\ell$ は $1/I_F$ の $\rho_C$ = 531 → 48028 倍(局所冪 3.6 → 3.3)、その水準の混合は全標本で非凸(κ* ≈ −1)—— 非凸の重みは 1 で、費用の無い典型の性質ゆえ大偏差で払えない。(4) 凸性を入力にしない版(潜在の分散の分解・曲線座標の Bakry–Émery・intertwining)は「形の潜在の法則の凸性の剛性」= Var(δ)⁻¹ を入力に要り、T8 の量に戻る。(5) 半古典の零点の分散は $\sigma_{\rm sc}^2I_F$ = 1.59 → 1.19(a647c)で凸の閾の境目 —— 道が要る「零点の精度」は T8 より $\rho_C$ 倍強く、半古典でも真偽が決まらない。
- **共通点(1 行)**:**点ごとの凸性(Brascamp–Lieb)は、形の潜在の変数の法則が場のデータの Fisher の分解能より狭いときだけ働き、それは T8 より $\ell^{3.3}$ 倍強い零点の精度の主張 —— 形の集団の揺らぎを押さえる道具なしに凸性の代用品で払う型(F175・F322 と同じ型:代用品が芯の向きで落ちる)。**
- **R9**:双極子では形の潜在が無く μ は Gauss(凸)—— 方式は空虚に成る;擬交差の梯子では潜在が 2 峰で非凸は強まり T8 の型の命題は偽になりうる —— 閉じたのは方式で、標的と同値でない。
- **射程(T60)**:禁じるのは「Q 空間の |ψ|² の点ごとの対数凹性・Bakry–Émery の曲率・局所の Brascamp–Lieb(近い域の凸性 + 大偏差)・log-Sobolev で T8 の形の揺らぎを出す」発注と、「HS の表示を凸性なしで(潜在の分散の分解・曲線座標・重みつき)当てて T8 を出す」発注。止めないもの:エネルギーの側の近い域の 2 次の下界(族 T-J、凸性を要らない作用素の不等式)、スペクトルの重み(族 T-G、647-D のファイバーの Dirichlet 形式はその f-sum の入力)、形の潜在の法則の集中を別の機構で示す道。
- **再開条件**:形の集団の座標の法則の集中(強い対数凹性の剛性 ≳ $I_F$、または Var(δ) ≲ $R^2\ell^{-\gamma}$ そのもの)が別の道で在庫に入ったとき(その時は HS は不要);または複素の基底状態の |ψ|² の点ごとの対数凹性を、凸でないポテンシャルについて与える定理が文献に現れたとき。

## F427(2026-10-22、w_E05_651_feshbach = 書き下しの型、稿 `651_難問1_ιの正の側_T8のFeshbachによる形の有効模型_2026-10-22.md` §3〜§5、判定文 worklog (研究ノート: `2026-10-22_w_E05_651_feshbach.md`) §1・§4(C0 の前に固定)、C0 a651a・a651b、成算 S-E05-R1 の族 T-I)難問 #1 (E4) ι>0 の T8((N-8′))を、**Feshbach–Schur の写像で形の集団座標(片側の壁の位置)へ断熱消去し、有効の形の問題 $Ks^2$ の基底状態から再中心化した 2 次の積率を出す**方式 —— (a) 形だけの射影 P、(b) 柔らかい光子を P に残し補空間を一様な隙間(603-T4C の Hardy の余裕・電子の隙間)で押さえる P
- **閉じたもの(R3)**:**方式**(札:a651a NOGO・a651b GO〈律速でない〉、補題 651-Z)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。
- **理由**:(a) 補題 651-Z(self-audited):P = 0 のファイバーで $[E,E+\epsilon)\subset\sigma(H(0))$(E05-F23 と E(P) の連続性、1 光子の Weyl の列〔要確認〕)なら、補空間の隙間 $g\ge2\omega_s$ と「形の振動子(準位の間隔 $\omega_s$)+ ノルム $\lt\omega_s/2$ の摂動」の有効の作用素は両立しない(等スペクトル性の片側)—— Ran P は柔らかい光子を運ぶ。(b) 形の座標の結合 $\frac12\partial_s\Omega^2A^2$ は泡の深さ全体の対(振動数は 2π から $2\Omega_{\rm in}\sim\ell^2$ まで連続)に広がり、補空間の resolvent を一様な隙間 $g_0=2\pi$ で押さえると 2 次の剛性の補正を Q 倍に過大評価:C0 a651a(1 次元の Gauss の玩具)で Q = 2.1・4.9・14.9・50.9(ℓ = 4〜32、局所冪 1.62・1.77、LDA の予言 $\Omega_{\rm in}/g_0\sim\ell^2$);正規化の版で $2QE_2/\lvert K_f\rvert\approx670$(ℓ = 32)—— 有効の剛性の下界は符号ごと崩れる。在庫の供給(603-T4C、電子の隙間、P315、597-B)は全て一様な隙間の型。B-r(653)の残タスク (a)「セルの中の誤差を曲率の 2 次で払う」部分は C0 a651b で律速でない(Y = 11.6 → 0.26、局所冪 −1.6)。形の慣性の 22→56% は形より遅い対が担う(断熱の分離が無い)。
- **共通点(1 行)**:**形の座標は泡の深さ全体の連続の対の振動数に結合し、形より速い補空間を切り出せない —— 断熱消去の誤差は補空間の resolvent の一様な上界に集まって $\Omega_{\rm in}/g_0\sim\ell^2$ を失い、払うには MF の多様体の近くの 1 量子の分解能の下界(640 の欠けの細かい版)が要る。**
- **R9**:双極子では泡と形の座標が無い(空虚に成る);擬交差の梯子では P に 2 構造の多様体が要り剛性が 0 に近い —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「形の集団座標(少数)への Feshbach–Schur・断熱消去で、補空間を一様な隙間(外の光子の尺度の Hardy・電子の隙間)の resolvent の上界で押さえて有効の形の剛性を出す」発注と、「形だけの射影で有効の振動子を得る」発注。止めないもの:補空間の上の局所の Bogoliubov の作用素 $U_\rho d\Gamma(\Omega_\rho)U_\rho^*$ に対する定数倍の強圧性(640 の欠けの細かい版、族 T-J と合流);IMS のセルによる局在(a651b で安い)。
- **再開条件**:押し縮めた Gauss の族の補空間の上で $\bar P(H-E)\bar P\ge c\,\bar PU_\rho d\Gamma(\Omega_\rho)U_\rho^*\bar P$(c は ℓ に依らない)が在庫に入ったとき。

## F428(2026-10-22、w_E05_644_glue = 書き下しの型、稿 `644_難問1_ιの正の側_T5の貼り合わせ_2026-10-22.md` §2・§5.1、判定文 worklog (研究ノート: `2026-10-22_w_E05_644_glue.md`) §1(C0 の前に固定)、C0 a644a、成算 S-E05-R1 の族 S-c)難問 #1 (E4) ι>0 の T5 の (N-S′) を、**「t₀ が X の隙間にある ⟹ $1_{[t_0,1]}(X)=f(X)$(f 滑らか)⟹ Helffer–Sjöstrand の関数計算と 1 の分割で $f(X)-\sum_j\chi_jf(X_j)\chi_j$ の跡のノルムを面積 × polylog に」**の字面の枠組みで閉じる —— 閉じたのは**命題の真偽**(前提の隙間が無い)
- **何を試したか**:設計メモ((研究ノート: `2026-10-22_親_名指し2本のブルドーザー攻撃の設計.md`))§4 の行 S-c の推論 1・2 を検算し、帯域の模型の $X=P_T\Pi1_E\Pi P_T$ の t₀ のまわりのスペクトルを、平板の厳密(627-Hκ)・原典(Sobolev 2010、Widom の予想の証明)・C0(スカラー、立方体、s = 8〜20)で調べた。
- **理由**:(i) 平らな半空間の TE のブロックで X は $m(D_t)$ に同値、スペクトルは [0,1] で絶対連続(命題 644-N (a));(ii) 有界な $C^1$ の E(スカラー)で窓 $(\lambda_1,\lambda_2)\subset(0,1)$ の固有値の数は Per(E) × log の型で育つ(Sobolev Thm 2.4・Rem 2.7);(iii) C0 a644a:窓 [0.8, 0.9] に 60・117・190・304 個、窓の密度は面から $d^{-0.70}$(DECAY_SLOW)。隙間が無いので $P\ne f(X)$、Combes–Thomas の局在が無く、幾何の resolvent の恒等式の誤差 $X-X_j=Q(1_E-1_{E_j})Q$ の跡のノルムは体積の型;$\chi_j$ は帯域の空間を保たない(627-N)。
- **共通点(1 行)**:**帯域で圧縮した X は、空間の跳び ∂E と運動量の跳び(帯域の縁)の積の上に Widom の連続スペクトルを持ち、(0,1) に隙間が無い —— 隙間を前提にする関数計算の局在の道具は、帯域の模型の X には当たらない(隙間を持つのは帯域なしの $X_\infty$ だけ)。**
- **R9**:閉じたのは枠組みの前提(命題の真偽:隙間の不在)。(N-S′) の真偽は閉じない —— 紫外の塊は同じ稿の定理 644-UV で面積(隙間なしで)。
- **射程(T60)**:禁じるのは「帯域の模型の X の t₀ に隙間を仮定して $1_{[t_0,1]}(X)$ を滑らかな関数の計算に置き換える」段と、「位置の 1 の分割の resolvent の恒等式で帯域の X のスペクトルの射影を局所化する」段。止めないもの:帯域なしの $X_\infty$(隙間あり)の関数計算、644-K の型の隙間なしの分解、V で重みをつけた窓の跡(644-T)。
- **再開条件**:帯域なしの $X_\infty$ の射影と帯域の X の射影の赤外の成分の差を、窓のモードの赤外の尾として押さえる評価が在庫に入ったとき(稿 644 §5.3 の設計の種)。

## F429(2026-10-22、w_E05_644_glue = 書き下しの型、稿 `644_難問1_ιの正の側_T5の貼り合わせ_2026-10-22.md` §5.2、情報 a644b、成算 S-E05-R1 の族 S-c)T5 の (N-S′) の有界な面を、**位置の 1 の分割(尺度 r ≪ R の小片)で平板・稜・曲率の局所の模型の評価の和に帰着させる**方式 —— 閉じたのは**方式**
- **何を試したか**:継ぎ目の量 $\mathcal T=\lVert\Omega^{-1}P_{\rm ext}VP_{\rm in}\Omega^{-1/2}\rVert_{\rm HS}^2$ を左右の $1_{\Omega\ge\mu}$・$1_{\Omega\lt\mu}$ で 4 つの塊に分け(HS で直交、等号)、紫外の塊を 644-K・644-C・644-T で押さえ(定理 644-UV、面積・log なし、局所の模型なし)、赤外の塊を局所の模型で見る道を検討した。
- **理由**:平板の在庫(627-E・636-T)の面積あたりの $\log(\Lambda N_\perp)$ は全て赤外の階層($\lvert k\rvert\lesssim k_\perp$ の殻ごとに O(1))にあり(644-UV で紫外に log は無い)、殻 $\lvert k\rvert\lesssim1/r$ のモードは大きさ r の小片の局所の模型では表せない;多尺度の分割には $P_{\rm ext}$ の赤外の成分の尺度ごとの局在が要り、それは (N-τ)・F419 の型の難しさ。重みの取り出し(作用素ノルム)は $\lVert1_{\Omega\lt\mu}\Omega^{-1}P\rVert$ の径の型(635-V と同じ)。値:𝒯 の 78% が赤外の塊(a644b)。
- **共通点(1 行)**:**位置の局所化は紫外にしか効かず、紫外は局所化なしで閉じる;(N-S′) の残りは赤外の塊(射影 $P_{\rm ext}$ の低い運動量の成分の局在)だけで、それは局所の模型の和ではない。**
- **R9**:閉じたのは方式。(N-S′) の赤外の塊の真偽は開いたまま(値は面積 × log の型)。
- **射程(T60)**:禁じるのは「局所の模型(平板・楔・曲がった面)の評価の和で (N-S′) の有界な面を閉じる」発注で、赤外の塊の扱いを書かないもの。止めないもの:族 S-a・S-b の局所の結果(赤外の塊の入力として);帯域なしの $X_\infty$ の隙間を使う赤外の解析。
- **再開条件**:$P_{\rm ext}$ の赤外の成分の尺度ごとの局在(または $X_\infty$ の射影との差の評価)が在庫に入ったとき。

## F430(2026-10-22、w_E05_643_curv = 書き下しの型、稿 `643_難問1_ιの正の側_T5の曲率と大域モード_2026-10-22.md` §1・§4・§6、判定文 worklog (研究ノート: `2026-10-22_w_E05_643_curv.md`) §1、成算 S-E05-R1 の族 S-b、C0 a643a)T5 の (N-S′) の有界な面で、**しきい値 t₀ を X(帯域つき)の全ての固有値から 1/polylog 離して選び、射影の安定性で曲率の補正を払う**方式 —— 閉じたのは**方式**
- **何を試したか**:無限の円柱 E = {r < R} を (n, k) のブロックに分け(補題 643-B)、各ブロックの X の [0.8, 0.9] の固有値を数えた(ΛR = 4〜48)。
- **理由**:[0.8, 0.9] の固有値はブロックあたり ≈ 0.5 個(0.29・0.46・0.53・0.52・0.53)で、ブロックの数は面積 × Λ² —— 全体で面積 × Λ² 個の固有値が窓を埋め、隙間の平均は ~0.2/(面積 × Λ²)(値)。族 S-e(稿 646、蓋つきの筒)でも 0.6〜0.8 が面積に比例して詰まる(親の知らせ)。各ブロックは帯域の円板への集中の作用素(Slepian 型)で、陽な対角化も無い —— 射影 $1_{[t_0,1]}$ の X の差についての安定性が使えない。
- **共通点(1 行)**:**有界な面では帯域が X に面積 × Λ² 個の plunge の固有値を与え、t₀ は必ず密なスペクトルの中にある —— 平板(627-E・636-T)は陽な対角化でこれを避けた;有界な面では隙間でなく、t₀ の平均(補題 643-M)で避ける。**
- **R9**:閉じたのは方式。(N-S′) の真偽は開いたまま —— 円柱の面積あたりの跡は平板の値に相対 O(1/(ΛR)) の負の補正で近づき(BOUNDED、増分の比 0.51・0.48)、n = 0 の大域モードの共鳴は R の冪で育たない(値)。
- **射程(T60)**:禁じるのは「t₀ を帯域つきの X の全ての固有値から離して選ぶ」ことを前提にする発注。止めないもの:帯域なしの界面の値(n = 0、kR < 1.2)から離す規則(命題 643-G、≳ R/ℓ)、t₀ の平均(643-M)、緩和 U(627-E (1))の評価(値で面積の型、U/T ≈ 1.7〜2.0)。
- **再開条件**:滑らかな境界・帯域の縁で X の窓の固有値の数が polylog に落ちる模型が採られたとき(現行の鋭い帯域では起きない)。

## F431(2026-10-22、w_E05_645_smooth = 書き下しの型、稿 `645_難問1_ιの正の側_T5の滑らかな窓への設計変更_2026-10-22.md` §1〜§6、判定文 worklog (研究ノート: `2026-10-22_w_E05_645_smooth.md`) §1(C0 の前に固定)、C0 a645a、情報 a645b、成算 S-E05-R1 の族 S-d)難問 #1 (E4) ι>0 の名指し (N-S′)(T5、617 段 4 の蓋の継ぎ目)を、**窓を滑らかにする設計変更**($W_{\rm ext}=1_{[t_0,1]}(X_\chi)$、$X_\chi=S\Pi\chi\Pi S$、χ は幅 w の滑らかな窓)で、縁・共鳴・大域モードごと消す方式
- **閉じたもの(R3)**:**方式**(厳密な補題 645-D・645-P + 類 C a645a:J1 DENSE、J2 NA、J3 W_FLAT;字面の総合は BOUNDED)。(N-S′) の真偽・命題 ι>0 は閉じない。
- **理由**:(1) 設計変更そのものは許される —— 手術(571-S0・627-A・635-S・613-A 段 1)は $V_T$ の任意の直交分解で成り、消費者(603-T4 (ii)・603-T4C・626-W の $P_{\rm ext}\ge p(X)$、607-N の $P_{\rm ext}=Xf(X)$)は $X_\chi$ でも同じ字面(命題 645-C)。(2) しかし縁・大域モードは尺度 ≫ w の構造で、滑らかな窓は層の重み $\lVert1_{L_w}\Pi Sv\rVert$ しか動かさない(補題 645-P:rank の版;筒の側面の t₀ = 0.85 のモードで層の割合 1.070 w/R、ずれ $\le(1.07w/R)^{1/2}$;縁の Weyl の列も尺度 [w, R] で残る)。(3) 窓の層の UV の横波が χ の全ての値に固有値を置き、t₀ の隙間を壊す(補題 645-D:$\mathrm{dist}(s,\sigma(X_\chi))\le(3.73(wk_*)^{-1/2}+3\sqrt T)/(1-1.87(wk_*)^{-1/2}-\sqrt T)$;a645a で [0.80, 0.90] の固有値の数 / 面積 = 0・1.98・3.01(w = 0・4・8、N⊥ = 32))—— 族 S-c の Helffer–Sjöstrand の前提が失われる。(4) 継ぎ目の跡は変わらない(t(8)/t(0) = 1.003、値)。(5) 平板で閉じた部分(627-L・627-T・627-E・636-T)は鋭い $1_E$ の構造を使い、作り直しになる。
- **共通点(1 行)**:**尺度 ≫ w の IR の構造(縁・曲率・大域モード)を、尺度 ≲ w の局所の操作(窓を均す)で消そうとした —— 難しさは尺度の上にあり、均しは UV の連続スペクトルを足すだけ。**
- **射影でない 1 の分割(DG の $\check\Gamma(j)$)**:閉じていない(別の問いに移る)。継ぎ目の真空の部分は局所(面積 × $\Lambda^2/(96w)$ の見込み、IR の log・縁・大域モードなし)になるが、$\check\Gamma$ がユニタリーでないので 571-S0 の試行状態 $\varphi\otimes\Omega_{\rm ee}$ の比較が物理の状態でできず、相互作用する基底状態の、蓋の層の光子の数が入る;欠損の π の部分は θ-実でない;603-T4C を重みつきの振動子 $d\Gamma(j_\infty\omega j_\infty)$ へ書き直す要(稿 §5、成算の候補 S-d′)。
- **R9**:645-C・645-D・645-P は自由場の作用素の言明で、双極子にも 2 構造の擬交差の梯子にも同じに成る —— 閉じたのは方式で、標的と同値でない。
- **射程(T60)**:禁じるのは「窓 χ を滑らかにして $1_{[t_0,1]}(X_\chi)$ で (N-S′) の縁・共鳴・大域モードを消す」発注(w ≪ R の全ての w)。止めないもの:領域 E の形を尺度 ~R で丸める設計(族 S-a・S-b の範囲、稿 §6 の注)、DG の局在の道(S-d′)。
- **再開条件**:滑らかな窓の $X_\chi$ について、t₀ の隙間を要らない (N-S′) の評価(連続スペクトルの中のスペクトルの射影の跡の安定性)が別の族で得られたとき —— そのときも 645-P により縁・大域モードは残る。

## F432(2026-10-22、w_E05_642_edge = 書き下しの型、稿 `642_難問1_ιの正の側_T5の稜の局所化_2026-10-22.md` §3(補題 642-K・系 642-K′)・§5、判定文 worklog (研究ノート: `2026-10-22_w_E05_642_edge.md`)「類 C 判定文」(値の前に固定)、C0 a642a、成算 S-E05-R1 の族 S-a)難問 #1 (E4) ι>0 の T5 の (N-S′) の**稜(縁)**を、**「楔の NP の本質的スペクトル [¼,¾](Perfekt 2018)の外の t₀ ⟹ 稜の近くで $1_{[t_0,1]}(X)=f(X)$(f 滑らか)⟹ 局在」**で長さ × polylog に押さえる方式 —— 閉じたのは**方式**(前提の命題の真偽:帯域の楔の X に隙間は無い)
- **何を試したか**:発注文の任務 2 と設計メモ §4 の行 S-a の推論 1 を、帯域の楔の作用素のスペクトルで検算(補題 642-K、強収束の初等の証明);類 C a642a(連続の鋭い帯域、kz ごとの断面の周期の箱、柱 − 板、t₀ = 0.6・0.75・0.85)。
- **理由**:帯域の楔の $X_{E_W}$ は σ = σ_ess = [0,1](面に沿った平行移動で半空間の [0,1] を含む);どの連続関数 f でも $\lVert f(X)-1_{[t_0,1]}(X)\rVert\ge\frac12$;有界な蓋では (0,1) の任意の区間の固有値が面の大きさとともに無限に増え、隙間の幅は 0 に縮む。[¼,¾] は帯域なしの極限の作用素(636-NP の ½ − K*)の本質的スペクトルで、帯域の X の言明ではない。値でも t₀ = 0.6(区間の中)で稜は有界 —— 局在の機構は隙間ではない。
- **共通点(1 行)**:F428(族 S-c)と同じ —— **帯域で圧縮した X は (0,1) に隙間を持たない;隙間を前提にする関数計算の局在は、稜の局所の模型にも当たらない**。
- **R9**:閉じたのは方式の前提。(N-S′) の稜の部分の真偽は閉じない —— 類 C は GO(稜の kz ごとの寄与は有界・負、紫外・赤外の塊とも;a642a・a642e)、消費者の o(体積)(655-C)の下では稜は余次元 2 として局所の密度の有界性に吸収される(稿 §5)。
- **射程(T60)**:禁じるのは「帯域の楔・縁の X の t₀ に隙間を仮定して稜の近くの射影を滑らかな関数の計算に置き換える」段と、「帯域なしの Mellin の記号を主の項にして帯域を摂動に入れる」段(帯域の縁が連続スペクトルの源なので)。止めないもの:帯域なしの $X_\infty$ の関数計算(隙間あり)、kz ごとの断面の数値、644-UV の型の隙間なしの評価、o(体積) の局所の密度の評価(S4)。
- **再開条件**:F428 と同じ(帯域なしの射影と帯域の射影の赤外の差の評価が在庫に入ったとき)。

## F433(2026-10-22、w_E05_649_spec = 書き下しの型、稿 `649_難問1_ιの正の側_T8のスペクトルの重み_2026-10-22.md` §1〜§5、判定文 worklog (研究ノート: `2026-10-22_w_E05_649_spec.md`) §1(C0 の前に固定)、C0 a649a、成算 S-E05-R1 の族 T-G)難問 #1 (E4) ι>0 の T8((N-8′):G-TK の門の F の側の失敗)を、**形の観測量 Õψ のスペクトルの重みを外の自由な光子の成分(pull-through)と泡の内の励起(f-sum / 内の隙間 $\omega_s$)に分ける**方式(634 候補 4)と、その変種 **Feynman の比 f/Var で内の隙間を避ける**方式(任務 3、634 候補 8 の形)で払う
- **閉じたもの(R3)**:**方式**(札:類 C a649a NOGO)。T8・(N-8′)・命題 ι>0 の真偽は閉じない。
- **理由**:(1) 高い側は厳密に払える —— 補題 649-F(647-D の系):再中心化した O で $`\int E\,d\mu_O=\frac12\langle C_f(O)\rangle`$、$\mathrm{Var}O\le\mu_O([0,\varepsilon))+\langle C_f\rangle/(2\varepsilon)$;617-W の $`\langle C_f\rangle\lesssim\ell\,`$polylog で切りは $\varepsilon\gtrsim\ell^{\gamma-1}$polylog、残る要求は $\mu_O([0,\varepsilon))\lesssim\ell^{2-\gamma}/$polylog。(2) C0 a649a(1 次元の MF の泡 + 凍った Bogoliubov + 静的な χ の準ボソンの RPA、$\Omega_p\propto R^2$、隙間 $\propto R^3$):電子を介した共通の揺らぎ ΔV の切り $R^{0.8}$ より下の割合は shell 1.000・1.000、wall 1.045・1.021(R_w = 31・47)、2 光子の上端 4 より下でも 0.8〜1.3;凍った分散も 99〜100% が下;f/Var ≈ 2 で R に依らず($\Omega_p$ = 42 → 474)—— 形の重みは壁の層の柔らかいモード(局所の振動数が電子の裾に沿い厚さ O(1) で ω から $\Omega_p$ まで連続)に住み、低い側の要求は T8 と値で同じ強さ(a647c の $\sigma^2I_F=O(1)$ と同じ向き)。(3) pull-through の外の光子の数の減衰($r^{-6}$)は $r\gg R$ の量で、壁の層(Fock の真空からのずれ O(1)、形の揺らぎは $\tilde O$ が作る 2 光子の状態)に届かない;Mourre は特定のベクトルの低い側の重みを与えない(F182 (3))。(4) Feynman の比 f/Var は最低の励起の上界で向きが逆;Var の上界の形 $\mathrm{Var}\le(\frac14\langle C_f\rangle\chi_O)^{1/2}$ は静的な感受率 $\chi_O\lesssim\ell^{3-2\gamma}$ = 傾けた基底のエネルギー $\inf\sigma(H+tO)$ の t² の精度の下界を要し、絶対の下界(J-G、t に依らない誤差)では届かず差の形の下界(族 B、638)に戻る。
- **共通点(1 行)**:**形の観測量の重みは光子の尺度(壁の層の柔らかい端)に住み、内の励起と外の光子の間にスペクトルの隙間が無い —— スペクトルで分けても T8 の量はそのまま低い側に残り、正しい向きの比の形は静的な感受率(差の下界)に戻る。**
- **R9**:双極子(泡なし)では O の重みは真空の 2 光子で方式は空虚に成る;擬交差の梯子では形が構造の間を飛び低い側の重みが O(1) で方式は偽になりうる —— 閉じたのは方式で、T8・標的と同値でない。内の隙間 $\omega_s$ の名指しは T8 を払わない(形の重みが $\omega_s$ に乗らない)ので立てない。
- **射程(T60)**:禁じるのは「形の観測量(再中心化した G-TK の F・壁の位置・近い殻の強度)のスペクトルの重みを、内の隙間・pull-through の外の光子の数・Mourre・f-sum と Var の比で分けて T8 を払う」発注。止めないもの:f-sum の高い側の払い(補題 649-F)を他の消費者に使うこと;静的な感受率 $\chi_O$ を差の形の下界で押さえる道(族 B に合流)。
- **再開条件**:形の観測量の低いエネルギー(光子の尺度)の重みが真空の型(Gauss の部分 $T\le C$)で押さえられることを示す入力 —— 例えば壁の層のモードについての局所の比較(真の ψ の壁の層の 2 点・4 点の関数が真空より狭い向きの不等式で、κ₄ を含むもの)が在庫に入ったとき;または 3 次元・横波の玩具で形の重みが $\Omega_p$ の尺度へ移ると値で示されたとき。

## F434(2026-10-22、w_E05_650_path = 書き下しの型、稿 `650_難問1_ιの正の側_T8の経路の側で中心と形を分ける_2026-10-22.md` §2〜§4、判定文 worklog (研究ノート: `2026-10-22_w_E05_650_path.md`)「判定文」(C0 の前に固定)、C0 a650a(INVALID)・a650b(GO_COND)、成算 S-E05-R1 の族 T-H)難問 #1 (E4) ι>0 の T8((N-8′))を、**P39 の Gauss + iρ の表示で経路の側へ移し、泡の中心(電子の泡の中の位置、観察 634-O)を経路の中心で除き、残りの形の揺らぎを電子の閉じ込め(571-F)と経路の側の正値の評価で払う**方式
- **閉じたもの**:**方式**。T8・(N-8′)・ι>0 の真偽、形の揺らぎの値、PGM の真偽は閉じない。
- **理由**:(1) P39 の表示は確率の表示でなく複素のずれ Φ = G + iρ で、経路ごとの場の実部は真空の G(経路と独立)—— 泡の位置・形は分散の打ち消しとしてだけ経路に載る。(2) 経路の中心 c(b) は場の可測な量でなく(補題 650-R で再中心化した ρ は経路の量)、消費者 571-A/501-X の τ = iX̂ は場の掛け算を要る;T8 の量(推定子のずれ Δ、637-R)は場の非多項式の汎関数。(3) その移しは補題 650-F の $E_\psi h=E_wH^h_C(\rho)$ だけで、命題 650-N により、絞られた典型の集合の補集合の稀な事象では経路の被積分の絶対値の平均が O(1)(1 モードの厳密な値で $E\lvert H\rvert/P_\psi$ = 370〜2.5e4)—— 経路の分割・571-F の型の裾・Chebyshev の和では $1/\ell$ に届かない。(4) 固定の中心の多項式の枝は厳密に移る($\kappa_4^\psi=\kappa_4^w(\rho)$)が 634-O で値で偽(C0 a650b の J0:$M_2\approx0.05$、ℓ に依らない)。
- **値(C0 a650b、PGM を仮定した玩具)**:経路の中心での再中心化は 634-O の項を消し(速い部分だけで冪 −5.0)、残りは形の分散の入力の 0.4〜0.5 倍(p = 3)・0.3 倍(p = 1)—— PGM が成れば T8 は経路の側の $\langle\delta^2\rangle_w\lesssim R^2/\ell$ に帰着し、半古典の値 $\ell^{-3}$ で余裕(条件付き)。
- **共通点(1 行)**:**泡を場の分散の絞りとして持つ PF では、P39 の経路の表示は泡を打ち消しとしてしか運ばない —— 場の推定子で定まる稀な事象を経路の側の正値の道具で押さえる型は O(1) を払う(F394 の「位相・正の混合の表示が無い」と同じ芯の、T8 の版)。**
- **R9**:双極子では泡が無く $k_{\rm eff}\approx0$ で 650-N の前提が外れ、経路の評価は打ち消しなしに効く;2 構造の擬交差の梯子では経路の表示が無い —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「P39(または Hiroshima の汎関数積分)の表示で T8・推定子の事象を経路の側へ移し、経路の中心・電子の閉じ込め・経路の分割の正値の評価で払う」発注。止めないもの:打ち消しを保つ経路の側の解析(振動積分の評価)、多項式の固定の中心の量の移し(631-K)、PGM そのものの探索。
- **再開条件**:PGM(場の法則が経路の遅い変数 Z の上の実の Gauss の混合 $\int N(0,C-S_Z)dw(Z)$、または同等の正の混合の表示)が成ったとき —— F394 の再開条件 (2)・F169 の再開条件 (1) と同じ型。

## F435(2026-10-22、w_E05_652_nearquad = 書き下しの型、稿 `652_難問1_ιの正の側_T8の近い域の2次の下界_2026-10-22.md` §3・§6、判定文 worklog (研究ノート: `2026-10-22_w_E05_652_nearquad.md`) §1(C0 の前に固定)、C0 a652a、成算 S-E05-R1 の族 T-J)難問 #1 (E4) ι>0 の T8((N-8′))の近い域の 2 次の下界を、(a) **固定の尺度の立方体の箱(集団座標なし、大域の θ)+ 作用素ノルムで地点ごとに分けた高い q**、(b) **古典の配位の下界**(運動を全て箱の Hardy $\frac12\lvert p_B\rvert^2\ge(N-2)^2/(8\lvert q_B\rvert^2)$ に落として $H\ge V_{\rm eff}(A)$)、(c) **状態の水準の Gauss の大偏差**(近い域の下界から ψ と Bogoliubov の Gauss のノルムの近さを出し、窪みの確率を Gauss の大偏差で払う、640 §2.3 の後段)で出す方式
- **閉じたもの**:**方式**(冪の勘定と値)。(N-8′)・T8・近い域の下界そのものの真偽は閉じない —— C0 a652a は誤差の下限(BO の利得)が相対 ℓ^{-1.9}〜ℓ⁻² で GO。
- **理由**:(a) 誤差は $\max(b^2\ell^{-2},b^{-3})$(高い q の作用素ノルムの膨らみ $2\pi b^2$ × 2 次の利得、補題 652-H の大域の θ の損 箱あたり θΩ)で最良 $\ell^{-6/5}$ —— 630-H3 の門の要求 $\ell^{-\gamma}$(γ > 11/7、617 T9)に冪で届かない(sup の門の要求 $\ell^{-1}$ には届く —— 閉じるのは 630-H3 の門の上だけ)。(b) $\inf V_{\rm eff}$ は箱の強度を電子の避ける 1 地点に集める配位で MF より相対 O(1)(または ≥ ℓ⁻¹)下がる —— Hardy の型の掛け算は等方な箱の総強度しか罰さず、地点ごとの不確定性(押し縮めの零点は量子)を拾わない;地点ごとの Hardy は零点の運動の 1/9。(c) 誤差の絶対値 / 形の量子(泡の中心の Ω)= 7.1 → 29.2(C0、冪 ≈ 1)—— ノルムの近さ $\lVert\psi-\Gamma\rVert^2\lesssim\varepsilon_{\rm abs}/\omega_s$ が 1 を越える。
- **共通点(1 行)**:**押し縮めの零点のエネルギーは運動の部分にあり、乗法の罰金(Chebyshev に入る形)に落とせるのは等方な箱の総強度(超動径)だけ —— 損は箱あたり θΩ で、要る精度 ℓ^{−γ} には電子の集団の応答を集団座標に分けて θ を下げることと、壁の殻で等方な箱を作ることが要る。**
- **射程(T60)**:禁じるのは (a) 集団座標なしの固定の尺度の箱で 630-H3 の門の (N-8′) を払う発注、(b) 運動を全て配位の関数に落とす下界、(c) 近い域の下界を状態の水準の大偏差に移す発注。止めないもの:補題 652-H の箱 + 上位 L 本の集団座標の IMS + 地点ごとの高い q の組み立て(冪の窓:sup の門なら余裕 1/5、630-H3 の門なら γ ∈ (11/7, 30/19));壁の殻の非等方な箱の 2 次の下界;PF の非局所の ω での箱の分解;1 量子の強圧性 (NQ-b) は要らない(T8 に要るのは加法の誤差 + 乗法の罰金 (NQ-a))。
- **再開条件**:なし((a)(b)(c) は方式の同定;続きは稿 §5.4 の 2 点)。
- **R9**:双極子では W の 2 次が 0 で下界は空虚に成る;擬交差の梯子では MF の多様体が 2 成分で、形の剛性は谷の間の跳びを罰さず T8 の上界は偽になりうる —— 標的と同値でない。

## F436(2026-10-22、w_E05_639c_famC3 = 書き下しの型、稿 `639_難問1_ιの正の側_617Wの率の内挿_2026-10-22.md` 第 3 部 §14、判定文 worklog (研究ノート: `2026-10-22_w_E05_639_famC.md`) 第 3 部 L2(読む前に固定)、成算 S-E05-R1 の族 T8-C)617-W の第 2 層を浅い水準 κ にし、窓の縁の水準 w の事象を **613-A(E05-P326)をそのまま水準 $g_w$・立方体の辺 $b_w$ で当てて**払う方式(定理 639-T の名指し (T7_w) を 613-A の形で供給する道)
- **閉じたもの(R3)**:**方式**(冪の算術、613-A の字面)。定理 639-T の論理・(T7_w) の真偽・ι>0 は閉じない。
- **理由**:613-A の $\mu'_{\rm net}$ の電子の座標の IMS の損 $\lambda C_\chi/(2n^2)$ と、主張の指数 $2c_akL_*/\sqrt g$($k\propto\sqrt{\mu'_1/\lambda}$)の斜面の長さは、ともに距離 $\sqrt{\lambda/\mu_w}=\ell^{(7-\kappa-3\beta)/2}$($\mu_w\asymp b_w^3\ell^\kappa$、$b_w=\ell^\beta$)を要る;El(系 639-E)は $\ell^{(7-\kappa+\beta)/6}$。窓の冪 δ の最小は β = (7−κ)/5 で (7−κ)/5、補題 639-M の冪は $a=\kappa-1+5(\delta-1)\ge1$ —— 全ての κ・β で 617-W の冪 6/7 から動かない。
- **共通点(1 行)**:**電子に相対な配位空間の Agmon は並進の運動の係数 λ と余裕の比の長さ $\sqrt{\lambda/\mu}$ を払い、余裕を浅い水準・小さい立方体で減らすほど窓が伸びて、窓の体積の 5 冪が利得を食う(F422 の El の相殺と同じ形が、El の冪 6 の下で IMS と斜面に移って起きる)。**
- **R9**:双極子では泡が無く空虚;擬交差の梯子では 618-S′ が崩れる —— 標的と同値でない。
- **射程(T60)**:禁じるのは「613-A の字面(電子に相対な斜面・電子の座標の一様な IMS)で水準 w の手術を当てて 617-W の冪を上げる、または ι>0 を得る」発注。命題 639-N′(E05-P353)の冪の式と、F425 の理由の「$a=(\kappa+4)/6$」は El だけを数えた不完全な式(613-A の道の真の冪は ≥ 1)。止めないもの:場に相対な並進の共変な Agmon の関数 + 597-B の集団座標の局在で (T7_w) を書く道 (T7_w′)(稿 §17)。
- **再開条件**:配位空間の Agmon で、電子の局在の損と斜面の λ の損を遷移の稀な集合の欠損に移す下界(597-B の片ごとの手術の下界)が書けたとき。

## F437(2026-10-22、verify_617W_adversary = 監査の型、記録 `658_多重検証V3_617Wへの反対の側からの攻撃_2026-10-22.md` §1〜§3、多重検証 V3)定理 617-W(E05-P340、$h_{\rm ls}\ge c_\alpha\lambda^{6/7}(\ln\lambda)^{-k}$)を、**γ < 6/7 の物理の筋書き**(Σ1 RG で足し上げた対数 $\gamma=8\alpha/3\pi$・閉包 $2a/(1+2a)$;Σ2 HS05 の 2 次 $c_0\alpha^2\sqrt\lambda$;Σ3 反跳で律された雲 $N_{\rm eff}\lesssim\lambda^{5/7}$;Σ4 泡は在るが失敗の裾が多項式)で反駁する方式

- **閉じたもの(R3)**:**方式**(筋書きによる反駁)。617-W の真偽は在庫の下で閉じない(在庫の読み 3 つは V1・V2 の範囲)。
- **理由**:観察 658-F(漏斗):消費者 501-X/571-A は変分、617-M′ は配位ごとの Schur の上界で、どの筋書きでも偽にならない;$h\le C\lambda^\gamma$(γ < 6/7)は $P_\psi(\mathcal G^c)\ge c\ell^{7(1-\gamma)-D}$ を強い、617-Q・613-A・613-B・$\Gamma'_R$ の「任意の冪の確率」の連言と矛盾する。Σ1・Σ2 は泡なしを要し、Markov の水準で既に J-G の下界(E05-P283〜P291・P298)+ 618-S と矛盾;Σ3・Σ4 は Agmon の裾(余裕 $tF\asymp\ell^5$ 対 経路の長さ $\gtrsim\ell^{1/2}$ で指数 $\gtrsim\ell^3$)と矛盾し、裾を多項式にする柔らかい方向は見当たらない。値:NUM-7672 の局所冪 0.829 ± 0.011 は Σ1(α=1 で 0.459)・Σ2(0.5)・Σ3(0.714)を到達できる λ で既に越える(前漸近、判定に数えない)。
- **共通点(1 行)**:**617-W を否定する筋書きは、変分の消費者と配位ごとの $C_f$ の上界を迂回できず、基底状態の泡の失敗の確率が ℓ の固定の冪より重いことを要する —— 物理の機構(BO の自己捕獲の大偏差)はそれを ℓ の超冪で否む。**
- **射程(T60)**:止めないもの —— J-G の鎖そのものの外部の水準の検証;617-W の在庫の 3 つの読み((H-μ′) の漸近の φ の展開と値の写像が下界であること、630-P の (P0) が重みつきの状態 $e^f\psi$ に当たること、有限モードの補題の全空間への読み)の照合;ι の値。
- **再開条件**:(a) 3 つの読みのどれかが外れたと V1・V2 か以後の監査で判明したとき(そのときは名指しに戻して筋書き Σ4 を再評価);(b) J-G の鎖(LL99 の未解決の問いの解決)に穴が見つかったとき(Σ1・Σ2 が生き返る)。
- **R9**:617-W の検証の方式の閉鎖で、標的(ι)とも 617-W とも同値でない。

## F438(2026-10-22、w_E05_648_optcorr = 書き下しの型、稿 `648_難問1_ιの正の側_E5の最適の補正子の数値_2026-10-22.md` §3・§5、判定文 worklog (研究ノート: `2026-10-22_w_E05_648_optcorr.md`) §3(J2、値の前に固定)、C0 a648b、成算 S-E05-R1 の族 T-F)難問 #1 (E4) ι>0 の E5(⟨C_f⟩ ≤ C)を満たす推定子として、**θ の水準の指示を水準について対数で平均した推定子**(co-area の型)、または **Bayes の事後平均 $\mathbb E[a\mid q]$** を T8 の族の推定子に採る方式
- **閉じたもの(R3)**:**方式**(値)。E5 の真偽・T8 (N-8′)・ι>0 は閉じない。
- **理由**:どちらも押し縮めた深い所(q が小さく、場の勾配の Dirichlet の費用が大きい所)に重みを置く。帯域制限の位置の混合の玩具で、水準の平均の ⟨C_f⟩ は上の 2 段で ℓ の冪 0.92・1.20 で育つ;事後平均(Laplace で MLE、核は Fisher の得点 $\partial\sigma^{-2}$)は絶対値は減るが最適(571-B の等号の核 $K=\log\sigma$ の大域の argmax)との比が 1.32 → 3.23(ℓ¹ の桁)で開く —— 推論「事後平均は Fisher 情報の最小化だから最適」は向きが誤り(分散の最小 ≠ Dirichlet のエネルギーの最小)。札 J2 は対照の外れで INCONCLUSIVE —— 閉鎖は札の外の値の読み(NUM-7822、a648b)。
- **残るもの**:最適の向きは $V=-\log\sigma_{\rm eff}$ の M 推定子(稿 648 §5 の 3.)。その ⟨C_f⟩ の制御に要るのは大域の argmax の跳びと壁の 2 次形式 $H_{zz}$ の下の裾で、後者は T8 と同じ型。

## F439(2026-10-22、w_E05_648_optcorr = 書き下しの型、稿 648 §2、C0 a648a(smoke)、判定文 worklog §1(J))**罠(数値の装置)**:泡の位置の連続の並進を、各点独立の白い格子の場に FFT の位相で当てた玩具で E5 の最適の補正子を測る方式
- **閉じたもの(R3)**:**方式**(装置の人工物)。
- **理由**:帯域の端の Umklapp で部分和の公式 $\sum V u\,Du=-\frac12\sum(DV)u^2$ が破れ、$\partial_a^2Q$ に副格子の並進の非局所の項が入り、M 推定子の ⟨C_f⟩ が 571-B の下界 $1/M_{\rm sq}$ を 25 倍下回る(機械的には E5_OK —— 偽)。直し:場を $2k_c\le\pi$ に帯域制限する(a648b)。G3 の格子の玩具で連続の並進を使う全ての数値に当たる。

## F440(2026-10-22、w_E05_644b_glue2 = 書き下しの型、稿 `644_難問1_ιの正の側_T5の貼り合わせ_2026-10-22.md` 第 2 部 §11、成算 S-E05-R1 の族 G-b)617 の滑らかな帯域の縁 S(607-N)の分解で、**t₀ を 1 点に固定したまま補題 644-K の窓の項 $\lVert V\rVert\mathrm{tr}(1_{W_\delta}(X)V)$ で無重みの漏れ $\lVert PVP^\perp\rVert^2$ を押さえる**方式 —— 閉じたのは**方式**
- **何を試したか**:644-K の窓の項を $1_W\le X(1-X)/c_W$ と 644-T の型で押さえる。
- **理由**:滑らかな S では E の奥の $S(k)^2=t_0$ の殻の平面波が X の窓の固有ベクトルになり、$\mathrm{tr}(1_W(X)V)$ と $\mathrm{tr}(X(1-X)V)$ に体積の項が残る(鋭い帯域の 644-T の $(1-Q)QV^{1/2}1_E=0$ が $(1-QS^2)$ で壊れる)。実の漏れは奥で小さい(P は殻の上で k の関数に近く V と交換)が、窓の対の対角を数える 644-K の粗さで体積になる。
- **共通点(1 行)**:**1 点の t₀ の鋭い切断は、連続スペクトルの殻の上で対の重みを 1 にする —— 窓の平均(644-A)で重みが δ/Δ になり、体積の項は小さい因子を受ける。**
- **R9**:閉じたのは方式。o(体積) の版の (N-S′) は同じ稿の系 644-O2(t₀ の窓の平均)で閉(候補)。
- **射程(T60)**:禁じるのは「滑らかな S の分解で 1 点の t₀ の 644-K の窓の項を体積より良く押さえる」発注。止めないもの:t₀ の窓の平均、鋭い帯域の 644-K・644-T。
- **再開条件**:t₀ の平均が 617 段 4 の消費者の字面で許されないと合同 S2 が判定したとき(その場合は 1 点の t₀ で窓の殻の対の非対角の評価が要る)。

## F441(2026-10-22、w_E05_652b_nearquad2 = 書き下しの型(w_E05_652_nearquad の再開)、稿 `652_難問1_ιの正の側_T8の近い域の2次の下界_2026-10-22.md` 第 2 部 §9〜§11、判定文 worklog (研究ノート: `2026-10-22_w_E05_652_nearquad.md`) §7(値の前に固定)、C0 a652b・a652c・a652d、成算 S-E05-R1 の族 T-J)難問 #1 (E4) ι>0 の T8((N-8′))の近い域の 2 次の下界 (NQ-a) を、**630-H3 の門の要求 ℓ^{−γ}(γ > 11/7)の下で**、補題 652-H′ の箱(残りの結合 θ = κ)+ θ > κ の強度の模様を集団座標に(IMS と胞の中の線形化)+ 地点ごとの高い q(作用素ノルム)で出す方式、および「集団座標は低い q の O(1)〜polylog 本」の読み(640 §2.3・652 第 1 部 §5、F435 の射程の「止めないもの」の窓 (11/7, 30/19))
- **閉じたもの**:**方式**(630-H3 の門の上で、冪の勘定と値)と**読み**(集団座標の本数)。sup の門の上の同じ組み立て・(N-8′)・T8 の真偽は閉じない。
- **理由**:損は $4G_2/\sqrt\kappa+\kappa R_{\rm total}+(\text{膨らみ})G_2$ で、集団座標の分の和は $\mathrm{Tr}(K\mathrm{Cov})=2G_2$ で押さえ座標の数に依らない;最良 $G_2^{2/3}R_{\rm total}^{1/3}$、P3 の制約 $A\le\ell^{2-\gamma'}$ の下で $R_{\rm total}\sim\ell^{(\gamma'-3)/2}$ —— $\le\ell^{-\gamma'}$ ⟺ γ′ ≤ 11/7、T9 は γ > 11/7 を要り窓は空。値(a652d):損 × ℓ^{11/7} = 1.56・1.43・1.42・1.47・1.56(ℓ = 5.7〜21.3、横ばい)、損 × ℓ = 0.575 → 0.272(減少)。読み:a652b で θ ≥ 0.01〜0.3 の模様の数は ℓ^{2.0〜2.4}(壁の面積)、数え上げの傾き −0.77〜−0.91(予言 −3/2 でない)、θ(L) は固定の L で ℓ とともに増える —— 柔らかい模様は壁に局在(剛性 2Ω³/3 ∝ ρ^{3/2} が応答 ∝ ρ より速く落ちる)。
- **共通点(1 行)**:**箱の作りの損は全て残りの結合 θ 倍で効くが、壁が ~ℓ² 本の柔らかい模様を持つので θ を下げる代価は $G_2/\sqrt\kappa$ —— 釣り合いの冪 $G_2^{2/3}R^{1/3}$ は 630-H3 の門の要求にちょうど届かず、sup の門には届く。**
- **射程(T60)**:禁じるのは、630-H3 の門の (N-8′) をこの組み立て(または集団座標の本数で払う勘定)で払う発注。止めないもの:sup の門(637-R・637-G)の上の同じ組み立て(値で余裕:損 × ℓ → 0);非局所の ω の Schur の分割(a652c:面積あたり O(1)、IR で壊れない);形の余裕 1 − θ₂(当てはめで正の極限 ≈ 0.15)。
- **再開条件**:$R_{\rm total}$ を $\ell^{(\gamma'-3)/2}$ より速く下げる箱の作り(壁の法線の方向の非等方を θ 倍より小さく払う)、または $G_2$ の集団の部分を $G_2^{2/3}$ より良く払う道具が見つかったとき。
- **R9**:双極子では W が 0 で空虚;擬交差の梯子では柔らかい模様が 2 つの谷を繋ぎ θ ≥ 1 になりうる —— 標的と同値でない。
- **射程の注記(2026-10-22、w_E05_652c_nearquad3、稿 652 第 3 部 §18)**:この閉鎖(630-H3 の門の上で窓が空、冪の境 γ′ ≤ 11/7)は T9(El の窓、γ > 11/7)が要る設計に限る。補題 663-G・系 663-C(El のゲージ除去で T9 が消え D ≍ ℓ ln λ に取れる)の下では要求は γ′ = 1(polylog つき)で、652-H′ + 652-C の組み立ては冪で余裕 4/7(立方体の箱でも 1/5)—— 閉鎖は当たらない。

## F442(2026-10-22、strategy_review_C2 = 書き下しの型、稿 `662_全体戦略の見直しC_簡単な模型の側から_2026-10-22.md` 第 2 部 §6、判定文 worklog (研究ノート: `2026-10-22_strategy_review_C.md`) 第 2 部(C0 の前に固定)、C0 a662d、成算 S-E05-R1 の枝 SR-C)難問 #1 (E4) ι>0 の T8 (N-8′) を、**推定子を泡の並進の軌道への変調の座標(Hessian / Fisher の計量の射影)に替えれば、片側の窪み(F404 の失敗の事象)は推定子を 1 次で動かさず、T8 は推定子の人工物として消える**とする読み(稿 662 §4.1 (ii)・§4.2)
- **閉じたもの**:**読み**(「1 次で動かさない」の部分)。(N-mod)・(N-8′)・ι>0 の真偽は閉じない。
- **理由**:片側の窪みは並進の接ベクトルに成分を持ち(l = 1 の成分)、どの共変な推定子も動く。979g の玩具で $X_{\rm mod}$ の窪みの感度は $X^{(2)}$ の 0.24〜0.60 倍(λ = 1e9〜1e5)、局所冪 +0.34〜0.49(テンプレート −log σ でも +0.08〜0.24)—— 0 にならない。消えるのは「てこの増幅」($X^{(2)}$ の感度の ℓ¹ の育ち)と E5 の $C_f$ の育ち(冪 +1.6〜2 → −1.4〜−2.1)だけ。
- **共通点(1 行)**:**推定子の取り替えで消えるのは推定子の感度の増幅で、窪みそのものが担う並進の成分と、壁の 2 次形式 $H_{zz}$ の下の裾(真の状態の形の揺らぎ)は残る —— 648 §5 の移り先と同じ。**
- **R9**:双極子では泡が無く空虚;擬交差の梯子では軌道が 2 つで推定子の射影が定まらない —— 閉じたのは読みで、標的と同値でない。
- **射程(T60)**:禁じるのは「推定子を変調の座標に替えるだけで T8 が消える」とする発注。止めないもの:変調の座標(とくに −log σ の重み)の下での $H_{zz}$ の下の裾の評価、(N-mod) の下の条件付きの定理。
- **再開条件**:片側の窪みの並進の成分を推定子の定義で吸収する(窪みを「泡の位置」の一部として数える)消費者の側の読み替えが 571-A の字面で許されると示されたとき。

## F443(2026-10-22、w_E05_648b_optcorr2 = 書き下しの型、稿 `648_難問1_ιの正の側_E5の最適の補正子の数値_2026-10-22.md` 第 2 部 §8、成算 S-E05-R1 の族 T-F)難問 #1 (E4) ι>0 の T8 (N-8′) を、617-T′ の推定子(X^(2) + 3 方向の Newton + 門)を**大域の argmax の M 推定子**(根の関数の核のポテンシャル V との相関 Q の、窓つきの柔らかい argmax;1 層・門なし)に替えて消す方式
- **閉じたもの(R3)**:**方式**(難しさの保存;字面の比較と次元の勘定)。(N-8′) の真偽・ι>0 は閉じない。
- **理由**:M 版は (N-8′) の主の条項(637-R:X^(2) と根のずれの 2 次の積率 ⟨|Δ|²⟩ ≲ c₃²R²/ℓ)と Kantorovich の条項 (g2)(g3) を要らなくするが、柔らかい argmax の跳びの Dirichlet の費用 $\frac\beta6\mathbb E[\lvert\Delta a\rvert^2\lvert\nabla_q\Delta Q\rvert^2]\rho_{\Delta Q}(0)$ が残り、近く縮退した 2 重の谷の密度の要求になる(入れ子にならない —— 比較不能)。分離 d ≳ $R\ell^{-1/43}$ の谷は MF の量的な安定性と J-G で Agmon に乗る見込みだが、近い部分(壁が 2 枚の「段々」、余分のエネルギー相対 $\sim\ell^{-1}$)は在庫の J-G($\ell^{-2/43}$)にも構造の天井($\ell^{-2/3}$、F412)にも見えない —— 617-Q の型では払えない。(B1) 曲率の小さい谷は 617-T′ の $A_1$ と同じ型(段 4 で払う見込み)。
- **残るもの**:名指しを (N-8M)〈近く縮退した 2 重の谷の密度〉に替える利点は、要るのが典型の揺らぎの大きさでなく稀な非凸の地形の密度であること(玩具 a648g では泡の谷の中の 2 つ目の谷は 1 度も出ない)。立てるかは設計の監査の判断(R9:2 構造の擬交差の梯子では偽になりうる)。条件:根の関数の核が勾配であること(未確認)、M 版の 617-M′ の類比(未証明)。

## F444(2026-10-22、w_E05_663_gauge = 書き下しの型、稿 `663_難問1_ιの正の側_Elのゲージ除去と短いてこ_2026-10-22.md` §4、判定文 worklog (研究ノート: `2026-10-22_w_E05_663_gauge.md`)「判定文」(C0 a663a・a663b の前に固定)、成算 S-E05-R1 の族 G-a)難問 #1 (E4) ι>0 の名指し (N-8′)(T8)を、**El のゲージ除去(補題 663-G)で El の窓を消し、てこを短く(D ≍ R polylog)して T8 の筒の事象を決定的に空にする**方式(監査 655 §2.1 の T1・§3 C6)
- **閉じたもの(R3)**:**方式**。El のゲージ除去そのもの(663-G、self-audited)・(N-8′)・T8・ι>0 の真偽は閉じない。
- **理由**:(1) F406 (i) の「決定的に空」は旧の門の**第 3 の条件だけ**の言明(629 §2.1 が κ_N の門は勘定の外と明記)。(2) 命題 663-K:630-H3 の門(Hessian 全体・$c_3^2=G_0/(128R^2U_cK_3)$、$K_3\asymp D/R^3$)では、片側の蓋を深さ $\delta\gt(R/D)^{3/2}(8c_K)^{-1/2}$ だけ下げた配位で κ > 1/32 —— 浅い窪み(θ の水準より上)なので 𝒢・$X^{(2)}$ に掛からない;対角の差の条件は D に依らず δ > 0.29(χ = 1 の門 b/8 の HS;要素ごとの b/16 では 0.18 —— 合同 S2 670 の直し、旧「δ ≈ 3/8」)で外れる。決定的に空にできるのは $D\ll R$(蓋が芯より近い)だけで、蓋は泡の外(余裕 $m_H$ の前提)ゆえ設計として不可能。(3) 系 663-C の残る条件 $n_b+2d\le D/2$($d\propto\ell\ln\lambda$)が $D\ge C\ell\ln\lambda\gg R$ を強い、失敗の深さ $\delta_\ast\asymp(\ln\lambda)^{-3/2}\to0$。
- **共通点(1 行)**:**El は手術の分割の産物(Coulomb ゲージの Schwarz が勾配の場を電子の慣性に結んでいた)で、ゲージで消える;しかし T8 の事象は門(推定子の Newton の基底)の側の性質で、てこの長さを替えても片側の浅い窪みの事象として残る —— T8 を消すのは El ではなく、泡の片側の形の揺らぎを押さえる道具だけ。**
- **残るもの**:(N-8′) は名指しのまま。系 663-C で D ≍ ℓ ln λ が許されるので、(N-8′) の主の条項の Chebyshev の要求は $`\langle\lvert\Delta\rvert^2\rangle\lesssim R^2/(\ell\,{\rm polylog})`$(長いてこ $R^2\ell^{-\gamma}$ の $\ell^{\gamma-1}$ 倍弱い;F409 の再開条件の水準)。近い殻の手術(C2)は El の窓が消えた代わりに、浅い集団の圧縮を罰する掛け算の余裕(LSI の型は $\omega_{\min}\sim1/R$ を失う)と $W_{\rm in}$ の成分が障害(稿 §5)。
- **R9**:双極子では泡が無く門の事象が空虚;擬交差の梯子では片側の形が構造の間を飛ぶ —— 閉じたのは方式で、T8・標的と同値でない。
- **射程(T60)**:禁じるのは「てこの長さ(D・芯・蓋の幾何)を替えて 630-H3 の型の Newton の門の失敗を決定的に空にする」発注。止めないもの:663-G による El の除去(段 4・段 1 で使ってよい)、短いてこの (N-8′)$_s$ の芯(片側の形の 2 次の積率 $R^2/\ell$)、門を持たない推定子、紫外に局在した浅い圧縮の掛け算の余裕(C2)。
- **再開条件**:並進に共変で $C_f=O(1)$ の推定子で、門(Newton の基底)の失敗の集合を持たないもの(F406 の再開条件 (1) の後半)が在庫に入ったとき —— 前半(El)は 663-G が監査を通れば充足〔2026-10-22 合同 S2 670:663-G は PASS with fixes(S0)—— 前半は充足、後半(門の失敗の集合を持たない推定子)は未充足〕。

## F445(2026-10-22、w_E05_664_qck;E05、難問 #1 (E4) ι>0 の族 G-c:経路の測度の第 3 形 (QC_κ)(窓の閉じ込め集合 K の上で $\mathbf 1_Ke^{-\frac{e^2}4Q+\kappa\lvert\Delta b\rvert^2}$ が対称準凹の有限積の一様極限、$\kappa\ge c\Lambda/R$)の真偽の判定と、それを経由する Sellke 型の Gauss 支配の自己無撞着で $h\ge c\lambda$ を出す方式。2026-10-22、w_E05_664_qck = 書き下しの型、稿 `664_難問1_ιの正の側_(QC_κ)の類C_2026-10-22.md` §1〜§3、C0 a664a〜a664f)
- **閉じたもの**:**命題 (QC_κ) の真偽(値の水準)**と、それを経由する方式(F394 の射程の「止めないもの」を確定)。ι の真偽は閉じない。
- **理由**:(1) 必要条件は半直線の単調性 (N2)(対称準凹の積の各因子が半直線で非増加;中点・2 点の対数凹は積の必要条件でない)。(2) 観察 664-A(厳密、バーストの極限):$\partial_tQ(tb)=\frac{\Lambda^2t}{2\pi^2}S_b(t\Lambda)$、$S_b(\rho)$ = 半径 ρ の球面の上の $\lvert P_\perp\hat\jmath_b\rvert^2$ の平均 —— κ なしの単調性は構造的に成るが、(N2) ⟺ $\tilde c\le\min_{\rho\le\Lambda}\Lambda R\,S_b(\rho)/(4\pi^2\lvert\Delta b\rvert^2)$。(3) 帯域の分解能より細かい 2 重のジグザグ(線の間隔 < 2π/Λ)で滑らかな Gauss の管の電流を真似る経路は、p-変分(p = 2.5・3)の球 $K_R$ の内で殻の量が端点の扇まで落ち、臨界 $\tilde c_{\rm crit}$ = 0.046・0.0335・0.00426・0.00069(ΛR = 4・16・64・256;線分 2 段で不変)、窓に広げた時間の核つきで 0.0403・0.00908(16・64;多重尺度の部分窓の比 M ≈ 1.4)。直線は 1/(4π) ≈ 0.08。(4) 観察 664-B:自己無撞着の固定点は $x\tilde c(x)=C/(2\pi\alpha)$($x=\Lambda R$)—— 測った $x\tilde c\le0.64$(4 点)は α = 1/137 の要求 ~10² に 2 桁届かず、γ(16→64) = 1.49(時間の核つき 1.07)で弱めた形も双極子の強さ(F394 の GD に安全な部分)止まり。
- **共通点(1 行)**:**PF の自己コストは経路の電流の Fourier の横の成分の重みつき二乗で、整った経路は帯域より細かい往復で滑らかな電流を真似て高い殻の量を消せる —— 経路ごとの準凹性・単調性の下界は乱れた(典型の)経路でなく整った経路で破れる(F99 の球内の往復と同じ根を p-変分の球の内へ持ち込んだ形)。**
- **R9**:閉じたのは命題 (QC_κ)(値)と方式。双極子では Q が増分の 2 次形式で (N2) は自明に成る(双極子の h ∝ λ と整合);擬交差の梯子は経路の測度を持たず対象外。標的(ι>0)とは同値でない。
- **射程(T60)**:禁じるのは「(QC_κ)(c 一様、または $\tilde c\sim(\Lambda R)^{-\gamma}$ の弱めた形)を経路ごとの準凹性で示して Sellke の連鎖で λ に線形を出す」発注(K = p-変分の球・多重尺度の窓の球)。止めないもの:(a) 速さを縛る K(Hölder の球)での (N2)(未検査;a664f の経路は Brown の尺度の部分窓の比 1.4 で定数の球に入る見込み);(b) 準凹性を経ずに GCI の積分の不等式を出す道(正の Gauss 混合の表示 —— F394 の再開条件 (2) = 稿 650 の PGM と同じ型、名指しにしない)。
- **再開条件**:(1) PF の重みの正の Gauss 混合の表示(位相を使わないもの)が見つかったとき(F394 の (2) と同じ);(2) 「整った」経路を Wiener の台の上の版で除ける K の取り方(台の外の半直線を使わない比較の定理)が文献に出たとき。
- **F394 への注記の案**:射程の「止めないもの:(QC_κ) の真偽の判定」は本項で値の水準で閉(稿 664)。

## F446(2026-10-22、rejudge_Rlambda0 = 監査の型、稿 `667_再判定_Rlambda0_2026-10-22.md` §4(観察 667-U1)、判定文 worklog (研究ノート: `2026-10-22_rejudge_Rlambda0.md`) §1(値の前に固定、条項 U1)、C0 (研究ノート: `a667_rejudge_Rlambda0.py`))(R-λ0) の下界で、遠い窪みの選び分け(611-P、E05-P324)の候補を**泡の中心 $X_c$ に相対に**取る方式(639 第 4 部 §22 の骨子の 3.「候補 = $X_c$ に相対な辺 $C_bs$ の立方体」)
- **閉じたもの(R3)**:**方式**(冪の算術、611-P の字面)。(R-λ0)・(T7_w′) の真偽、ι>0 は閉じない。
- **理由**:$g_k=g_b(X_c+y_k)$ の場の微分に $\nabla_Yg_b\cdot\partial_AX_c$ が入り、$C_{g_k}\gtrsim\lvert\nabla_Yg_b\rvert^2C_f(X_c)$。選び分けの鋭さ $\beta_{\rm sm}\asymp\ln N/(\theta g_w)$ と、飽和した水準の位置の感度 $\lvert\nabla_Yg_b\rvert\le3\tau_w/b$($\tau_w=c_\tau g_w$)の積は水準に依らず $\ln N/b$ —— 費用 $\beta_{\rm sm}^2C_{g_k}/8$ の余裕 $\mu_w\asymp b^3\ell^\kappa$ に対する比は $\ell^{1-\kappa}/b^5$ polylog($C_f(X_c)\asymp\ell$ polylog、617-M′)。≤ 1/8 には β ≥ (1−κ)/5 が要り、$a=(\kappa-1+5\beta)/6\ge0$ ちょうど。飽和なしでは β ≥ (1+κ)/5、a ≥ κ/3。最小点の近くの p の集中を入れても対数だけ(667 §8 R1)。値:a667 で全ての κ・段で比 ≫ 1(到達できる 1e9 でも 126〜743)。
- **共通点(1 行)**:**泡に相対な位置で窪みを選ぶ鋭さ(∝ 1/水準)と位置の感度(∝ 水準/辺)の積が泡の中心の場の感度 ℓ を運び、余裕との釣り合いが El の窓の境 β = (1−κ)/5 にちょうど落ちる —— F422・F436 と同じ型の 3 度目の相殺(a = 0 の境)。**
- **R9**:双極子では泡が無く $X_c$ が立たない(空虚);擬交差の梯子では 618-S′ が崩れる —— 標的と同値でない。
- **射程(T60)**:禁じるのは「(R-λ0) の下界の選び分けの候補を $X_c$ に相対に取る」発注。止めないもの:597-B の片 $\varphi_j$ の中で泡の絶対の位置を $\chi_j$ で局在させ、候補を絶対の格子の点に取る設計(667 §4 の (abs);連鎖なし、冪 $a=(\kappa-1)/6$ が生きる)。
- **再開条件**:位置の感度を水準と切り離す選び分け(例:$\lvert\nabla_Yg\rvert$ が水準より速く小さい輪郭の汎関数)を在庫の形で書けたとき。

## F447(2026-10-22、w_E05_652d_nearquad4 = 書き下しの型(w_E05_652_nearquad の再開)、稿 `652_難問1_ιの正の側_T8の近い域の2次の下界_2026-10-22.md` 第 4 部 §22・§24、判定文 worklog (研究ノート: `2026-10-22_w_E05_652_nearquad.md`) §13・§15(値の前に固定)、C0 a652f・a652f2・a652g、成算 S-E05-R1 の族 T-J)難問 #1 (E4) ι>0 の (N-8′) の近い域の 2 次の下界 (NQ-a) を、補題 652-C(E05-P369)の近い域を**全ての集団座標(θ_k ≥ 0.1、多重度込み 223〜3636 本)の箱**で取り、かつ W の 2 次の上界を補題 652-T の**一様な β** で取る方式
- **閉じたもの**:**方式**(近い域の取り方と一様な β)。(NQ-a)・(N-8′) の真偽は閉じない —— 典型の配位では両条件とも余裕の内。
- **理由**:(a) 箱の近い域の胞で全ての集団座標が 2σ に符号を揃えると、仮定 (A) の量 ε₂ = 2.55・3.64・5.36・7.69・11.2(λ = 1e5〜1e9、壁の外の地点)が 1 を越え ℓ で育つ —— 2 次の代理 $\frac12u\cdot Ku$ の線形化が不安定になる(真の W は大きい揃った偏差で頭打ちで、代理だけが壊れる)。符号がばらばらの典型の値は 0.20〜0.22。(b) 一様な β は典型で 0.39 に横ばい(J8)、膨らみ $(1-\beta)^{-1}$ = 1.63 は形の余裕(1 − θ₂ → 0.15、許容 1.18)を越える;形の方向だけの膨らみは典型 3%・敵対的(2×2×2 の箱に強度を集める)30%(J8′)。
- **共通点(1 行)**:**近い域の条件を「各座標・各地点の窓」で書くと、壁の ~ℓ² 個の地点・座標の符号や強度を揃えた敵対的な配位が近い域に残り、2 次の代理(W の上界・集団座標の線形化)が壊れる —— 揃った配位を払えるのは場の地点ごとの不確定性(運動)だけで、その費用は ~0.2 ℓ^{-1}(要求と同じ冪、到達の値の雑な勘定)。**
- **射程(T60)**:禁じるのは、近い域を集団座標の箱・一様な β で取って (NQ-a) を出す発注。止めないもの:壁の地点ごとの窓 Z(x) の IMS(費用の係数の測定が次の手)、形の方向ごとの W の上界(典型で 3%)、場の地点ごとの不確定性で揃った配位を払う補題。
- **再開条件**:壁の地点ごとの窓の IMS の費用が要求 ℓ^{-1}/polylog より冪で小さい(係数でなく冪)と示されたとき、または揃った配位の確率を場の運動で直接(IMS なしに)払う不等式が見つかったとき。
- **R9**:双極子では W が 0 で空虚;擬交差の梯子では揃った配位が 2 つの谷を繋ぐ —— 標的と同値でない。

## F448(2026-10-22、w_E05_652e_nearquad5 = 書き下しの型(w_E05_652_nearquad の再開)、稿 `652_難問1_ιの正の側_T8の近い域の2次の下界_2026-10-22.md` 第 5 部 §26・§27、判定文 worklog (研究ノート: `2026-10-22_w_E05_652_nearquad.md`) §18(値の前に固定)、C0 a652h、成算 S-E05-R1 の族 T-J)難問 #1 (E4) ι>0 の (N-8′) の近い域の 2 次の下界 (NQ-a) で、壁の敵対的な配位を**地点ごとの窓 $\lvert Z(x)\rvert\le k_w\sigma_Z(x)$ の IMS**で近い域から外し、残りを補題 652-C(E05-P369)の Taylor の評価で払う方式
- **閉じたもの**:**方式**(652-C の Taylor の評価を壁の窓の幅の胞まで使うこと)。(NQ-a)・(N-8′) の真偽は閉じない;窓の IMS の費用そのものは要求に勝つ。
- **理由**:窓の IMS の費用 R_Z は R_Z ℓ = 1.08 → 0.44(λ = 1e5〜1e9、局所冪 −1.37〜−2.15)で要求 ℓ^{-1} より冪で小さい —— 第 4 部の「~0.2 ℓ^{-1}」は過大の勘定で訂正。しかし全ての窓の地点(N_win = 2.5e3 → 6.5e4)で同時に窓の内に入るには $k_w=\sqrt{2\ln N_{\rm win}}$ = 3.96 → 4.71 が要り、652-C の仮定 (A) の量 compat = 2k_w max σ_Z/Ω² + ρ_A = 0.82〜0.85(c ≈ 6.7)—— 3 次の剰余 $E_3=\varepsilon c^2\tilde R$ は ~1e8 で MF(1.7e7、λ = 1e9)を越え、剛性で吸収できない(値の雑な勘定)。k_w は √ln ℓ で育ち、max σ_Z/Ω² の減りは減速(→ 0.075 の見込み)—— 外挿で λ ~ 1e24 で compat が 1 を越える。
- **共通点(1 行)**:**壁の地点の数 ~ℓ² の全てを同時に窓に入れる union の代価 √(2 ln N) が、2 次の代理の安定の余裕(定数)を対数で食う —— 窓の外に出る少数の地点を 2 次の代理から外して 1 地点ごとに厳密に払う「局所の例外」が要る。**
- **射程(T60)**:禁じるのは、652-C を全ての窓の地点の共通の窓の近い域で使う発注。止めないもの:局所の例外の補題(窓を固定の k_w ~ 3 に、外に出た地点を 1 地点の厳密な評価で;費用の見込み相対 ~ℓ^{-2.8}、値)、窓の IMS(費用は勝つ)。
- **再開条件**:局所の例外の集合を外した後の compat が ≤ 0.3 に収まる(類 C)と示されたとき。
- **R9**:双極子では W が 0 で空虚;擬交差の梯子では窓の外の地点が谷の間の跳びに対応しうる —— 標的と同値でない。
- **注記(2026-10-22、w_E05_652f_nearquad6、稿 652 第 6 部 §29)**:窓を k_w = 3 に固定し外の地点を局所の例外として払う形(この F の「止めないもの」)の類 C a652i は BOUNDED(GO の向き):例外を外した後の compat = 0.58、合計の費用 / 要求 = 6.33 → 0.82(λ = 1e5〜1e9、減少)、例外の数は ℓ^{2.15} で union の √ln の代価は消える。閉じたのは「共通の窓」の方式だけで、局所の例外の道は開いている。

## F449(2026-10-22、audit_S2_639Tprime = 監査の型、合同 S2 `668_合同監査_639Tprimeと639ABとRlambda0_2026-10-22.md` §1.3・§4、C0 (研究ノート: `a668_audit_S2_639Tprime_etaEbox.py`))難問 #1 (E4) ι>0 の枝 (ii):補題 639-AB(597-B の片 × 611-P の絶対の候補 × 片ごとの手術)の段 3 の手術を**在庫の 635-S(E05-P347)で浅い水準 $g_w\asymp\ell^{-\kappa}$(0 < κ < 1)・小さい立方体**に当て、系 639-T′(E05-P370)の ⟨C_f⟩ = o(1) と ι>0 を出す方式
- **閉じたもの(R3)**:**方式**(635-S の Cauchy–Schwarz で El を場の 2 次 + 定数に割る手術を、余裕が電子の運動の尺度より冪で小さい浅い水準に当てる道)。ι>0・(N-8′)・T8・663-G の真偽は閉じない。
- **理由**:635-S の主張は $H_{\rm box}-E_{\rm box}\ge(H_{\rm ee}-E_0)+H_{\rm ie}-\frac{\lambda\alpha}2(\eta_S^{-1}-1)\lvert A_{\rm e}(x)\rvert^2-\eta_SE_{\rm box}-c_A$ で、$E_{\rm box}\ge E\asymp F\asymp\ell^5$。浅い水準・辺 $b=\ell^\beta$ の立方体の余裕 $\mu_w\asymp b^3\ell^\kappa$ で $\eta_SE_{\rm box}$ を払うには $\eta_S\lesssim b^3\ell^{\kappa-5}$;El の係数 $\lambda/\eta_S$ と 639-E の $\sigma_0^2\lesssim b^4D^{-6}$ で $D_{\rm El}\asymp\ell^{2-(\kappa+\beta)/3}$、639-M の第 1 項 $\ell^{\kappa-6}\rho^5$ の冪は $a=4-\frac{2\kappa+5\beta}3\ge1$(0 < κ ≤ 2・0 ≤ β ≤ 1;等号は κ = 2・β = 1 の θ の角 = 617-W)。立方体を μ_w ≥ ℓ⁵ まで大きくしても a ≥ 11/9 − κ/9 ≥ 1。稿 639 第 5 部・記録 667 の冪 (κ−1)/6 は $\eta_SE_{\rm box}$ を落とした($\kappa_W\asymp\lambda$)算術。値:C0 a668 の格子の全てのセルで閉じた形と一致、最小 1。
- **共通点(1 行)**:**El の交差項 $`\lambda\sqrt\alpha\,\pi\cdot A_{\rm e}`$ は外の場に線形で、Cauchy–Schwarz で電子の運動の割合 η に結ぶと実効の冪は $`\sqrt{E_{\rm box}\lambda\alpha}\,\sigma_0\propto D^{-3}`$ —— 浅い水準の小さい余裕 $\mu_w\ll E\asymp\ell^5$ はこの釣り合いで窓 $\ell^{2-\kappa/3}$ を強い、窓の体積が水準の利得を食う(F422・F436・F446 と別の型の 4 度目の相殺:鋭さ × 位置の感度でなく、余裕の小ささ × 電子の運動の尺度)。**
- **R9**:相殺の機構(電子の運動の割合を盗む Cauchy–Schwarz)は双極子でも擬交差の梯子でも同じ形で、標的の真偽と独立 —— 閉じたのは方式。
- **射程(T60)**:禁じるのは「635-S(または El を電子の運動の一定の割合で払う同型の手術)を、余裕が $E\asymp\ell^5$ より冪で小さい浅い水準・小さい立方体に当てて 617-W の冪 1 を下回る」発注。止めないもの:補題 639-AB の段 1・2・4〜7 の組み立て(絶対の候補・597-B の片・単一の水準の f —— 合同 S2 668 で当)、El の距離を $\ell^{2-(\kappa+\beta)/3}$ に直した弱い形の 639-AB(遠い浅い窪みの確率の言明として)、663-G のゲージ除去の手術に替える道。
- **再開条件**:El の交差項を電子の運動の一定の割合で払わない手術の不等式が在庫に入ったとき —— 例:663-G(E05-P368)が η が ℓ の負冪の域で 監査の型 の監査を通る、または電子の束縛の間隙を使う 2 次の評価(TRK の和則で位移 $\lambda\alpha\sigma_0^2$)が作用素の形で書けたとき。前者なら El の窓が消え、冪は κ − 1(値、記録 668 §1.4)。

## F450(2026-10-22、w_E05_652g_nearquad7 = 書き下しの型(w_E05_652_nearquad の再開)、稿 `652_難問1_ιの正の側_T8の近い域の2次の下界_2026-10-22.md` 第 7 部 §33・§34、判定文 worklog (研究ノート: `2026-10-22_w_E05_652_nearquad.md`) §25(値の前に固定)、C0 a652j、成算 S-E05-R1 の族 T-J)難問 #1 (E4) ι>0 の (N-8′) の近い域の 2 次の下界 (NQ-a) で、**線形化する集団座標を θ ≥ 0.6 の少数の形の座標に絞り、他を球で頭打ちにして、地点ごとの窓なしで**仮定 (A) と 3 次の剰余を保つ方式
- **閉じたもの**:**方式**(値)。(NQ-a)・(N-8′) の真偽は閉じない。
- **理由**:θ(L) が ℓ とともに育つので、固定の閾 θ ≥ 0.6 の座標は 5・6・6・13・22 本(λ = 1e5〜1e9)に増え、符号を揃えた 3σ の最悪の胞の compat は 0.56・0.53・0.42・0.66・0.84、3 次の剰余の上界 / MF は 1e9 で 0.79(費用 / 要求 16.8)—— 到達の λ でも保たない。
- **共通点(1 行)**:**線形化する座標の数は θ の育ちで ℓ とともに増え、窓なしの最悪の胞では仮定 (A) の余裕が消える —— 線形化の群を小さく保つには ℓ に依る閾が要り、その外は球で払えるが、L の群の中の符号を揃えた胞は地点ごとの窓か例外(確率の bootstrap が欠け)でしか払えない。**
- **射程(T60)**:禁じるのは、固定の θ の閾で線形化の群を絞り窓なしで (A) を保とうとする発注。止めないもの:補題 652-E の球(線形化しない群の費用は桁で小さい)、窓つきの低い群(J11 で T ℓ = 0.79 で減少)、例外の確率の bootstrap の類 C。
- **再開条件**:L の群の大きさを ℓ に依らず有界に保つ選び方(例:L ≤ L₀ の固定の角運動量)で、最悪の胞の compat が 0.6 以下に保たれると示されたとき。
- **R9**:双極子では W が 0 で空虚;擬交差の梯子では揃った胞が谷の間の跳びに対応しうる —— 標的と同値でない。

## F451(2026-10-22、w_E05_652h_nearquad8 = 書き下しの型(w_E05_652_nearquad の再開)、稿 `652_難問1_ιの正の側_T8の近い域の2次の下界_2026-10-22.md` 第 8 部 §37・§38、判定文 worklog (研究ノート: `2026-10-22_w_E05_652_nearquad.md`) §27(値の前に固定)、C0 a652k、成算 S-E05-R1 の族 T-J)難問 #1 (E4) ι>0 の (N-8′) の近い域の 2 次の下界 (NQ-a) の局所の例外の補題で、**例外の確率を、場の H の一部で作る地点ごとの罰金 $\kappa_x(Z(x)-Z_0)^2$(例外が自分を罰する bootstrap)で払う方式**
- **閉じたもの**:**方式**(値)。(NQ-a)・(N-8′) の真偽は閉じない。
- **理由**:例外の上で 652-X の払い $c_x=\frac32(\Omega_x-1)$ を罰金で覆うには $\kappa_x=c_x/(8\sigma_Z^2)$、それを Z(x) の台($N_{\rm eff}$ = 260〜1750 地点)の剛性の割合で作ると、各地点の需要(割合の和)が $D_{\max}$ = 221・215・216・208・195(λ = 1e5〜1e9)—— 供給 1 の約 200 倍。損 $\sum c_x/8$ は要求の 3〜20% で小さいが、割り振りが成り立たない。
- **共通点(1 行)**:**Z(x) は数百の地点の弱い集団の変数で、典型の尺度(3σ)の揺らぎの費用は 1 本の量子の桁、しかも同じ地点の剛性を数百の Z(x) が分け合う —— エネルギーの方法では ψ の局所の Gauss 性(典型の尺度)を出せない。**
- **射程(T60)**:禁じるのは、局所の例外の確率をエネルギーの bootstrap(地点ごとの Z の罰金)で払う発注。止めないもの:状態の水準の道具(局所の対数 Sobolev・Bakry–Émery の型で ψ の局所の Gauss 性を出す —— PF の ψ が複素である障害つき、647)。
- **再開条件**:ψ の局所の集団の変数の分布が典型の尺度で Gauss に近いことを出す状態の水準の道具が在庫に入ったとき。
- **難しさの保存**:第 4〜8 部で、2 次の代理の安定の余裕 → 窓の union の √ln → 例外の費用 → 例外の確率 → 状態の水準の局所の Gauss 性(F435 (c) の典型の尺度版)と移った。
- **R9**:双極子では W が 0 で空虚;擬交差の梯子では局所の Gauss 性そのものが偽になりうる —— 標的と同値でない。
