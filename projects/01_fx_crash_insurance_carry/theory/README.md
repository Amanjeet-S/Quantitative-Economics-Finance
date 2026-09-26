# Theory

Results used in the [research design](../research_design.md). Every result marked P or P\* is proved in `notes.tex` (compiled as `notes.pdf`); R9 is cited with its conditions.

**Labels:**

- **P:** proved in notes.tex; the part I claim as my own is stated in the result's sources, and the related literature is cited there.
- **P\*:** a known result; notes.tex writes out the published or standard proof for completeness.
- **C:** cited, with hypotheses stated.

## R1 (P\*). Domestic and foreign risk-neutral measures

**Setting.**
- (Ω, 𝔽, (𝔽_t), Q^d) satisfies the usual conditions.
- B^d and B^f are strictly positive money-market accounts with B^d_0 = B^f_0 = 1.
- S is strictly positive and càdlàg.
- Z_t = S_t B^f_t / (S_0 B^d_t) is a true Q^d-martingale.
- Define dQ^f/dQ^d = Z_T.

**Claims.**
- (a) Q^f ~ Q^d.
- (b) E^{Q^f}[X | 𝔽_t] = E^{Q^d}[Z_T X | 𝔽_t] / Z_t, for X ≥ 0 or X ∈ L¹(Q^f).
- (c) Foreign prices discounted by B^f are Q^f-martingales exactly when their domestic values discounted by B^d are Q^d-martingales.
- (d) Under Garman–Kohlhagen, E^{Q^d} S_T = F and E^{Q^f}(1/S_T) = 1/F. This is Siegel's paradox resolved.

**Remark.** If Z is only a strict local martingale, then E Z_T < 1 and Z_T does not define an equivalent measure. Carr, Fisher and Ruf (2014) construct the foreign measure as a Föllmer measure that is not equivalent to Q^d, and restore the domestic-foreign symmetry with a modified pricing operator.

**Source.** Geman, El Karoui and Rochet (1995).

## R2 (P\*). Arbitrage-free call prices

**Statement.** c(K) = E(X − K)⁺ for some X ≥ 0 with E X = F if and only if:
- c is convex,
- c(0) = F,
- c′₊(0) ≥ −1, and
- c(K) → 0 as K → ∞.

**Consequences.**
- The law of X is unique, with distribution function G = 1 + c′₊ and P(X = 0) = 1 + c′₊(0).
- With c(K) = F − K for K < 0, the law equals c″ in D′(ℝ).

**Tests used.**
- On a grid: slopes in [−1, 0] and nondecreasing.
- On total variance w(k): g(k) ≥ 0 (Gatheral and Jacquier, 2014).

**Sources.** Breeden and Litzenberger (1978); the characterisation and its proof through the right derivative and Fubini's theorem are in Föllmer and Schied (2004, Lemma 7.23).

## R3 (P\*). Spanning

**Hypotheses.**
- f′ is locally absolutely continuous on (0, ∞).
- Q(X > 0) = 1.
- ∫₀^F |f″|P dK + ∫_F^∞ |f″|C dK < ∞.

**Statement.** E f(X) = f(F) + ∫₀^F f″(K)P(K) dK + ∫_F^∞ f″(K)C(K) dK.

**Proof.** Taylor's theorem with integral remainder, then Fubini.

**Sources.** Carr and Madan (1998) for the formula; the proof is the standard Taylor-remainder argument, written out with explicit integrability hypotheses; Bakshi, Kapadia and Madan (2003) for the moment contracts.

## R4 (P). Partial identification from truncated quotes

**Sources.** Jiang and Tian (2005, Proposition 2 and Appendix) bound the truncation error of model-free implied variance beyond the quoted strikes; Lee (2004) links finite moments to the wings of implied variance. The power-type tail condition, the bounds for general and sign-changing weights and the resulting variance and skewness intervals are my own.

**Tail bound.**
- If Q(S_T ≤ K)/K^γ is nondecreasing on (0, K_min], then P(K) ≤ P(K_min)(K/K_min)^{γ+1} there.
- If K^η Q(S_T > K) is nonincreasing on [K_max, ∞) with η > 1, then C(K) ≤ C(K_max)(K/K_max)^{1−η} there.
- Hence, for example, ∫₀^{K_min} P K⁻² dK ≤ P(K_min)/(γ K_min).

**Further bounds.** The same inequalities bound the tails of any weight, including the moment contracts adapted from Bakshi, Kapadia and Madan (2003); sign-changing weights are split into positive and negative parts.

**Output.** Variance and skewness are reported as intervals over stated tail exponents, truncating at the 10Δ strikes.

**Quadrature.** F is a node, because the integrand has a kink there. Trapezium error is O(h²) and Simpson error O(h⁴) on each side.

**Implementation.** `src/qef/fx/moments.py` (with R1 for USD-base pairs); results in `reports/stage4.md`.

## R5. Delta-to-strike inversion

**(a) Closed form.** For pips spot delta: K = F exp(σ²τ/2 − φσ√τ Φ⁻¹(|Δ|/D_b)).

**(b) (P\*) Premium-adjusted call delta** h(K) = (K/F) D_b Φ(d₋):
- h → 0 at both ends.
- h′ has the sign of Φ(d₋) − φ(d₋)/(σ√τ).
- Since φ/Φ is strictly decreasing, h is strictly increasing then strictly decreasing, with a unique maximiser K*.
- Each attainable Δ has exactly two strikes; the convention takes the root in [K*, ∞).

**(c) (P)** For pips delta Δ_φ(K) = φ D Φ(φ d₊(K, σ(K))): if |∂σ/∂k| √τ |d₋| < 1 on an interval (k = ln(K/F)), Δ_φ is strictly decreasing there, so the smile delta-to-strike map is injective. The condition holds over ±4 ATM standard deviations at every calibrated month-end; premium-adjusted deltas are checked numerically.

**Sources.** Reiswich and Wystup (2012) give the delta definitions, the non-monotonicity of the premium-adjusted call delta and the right-branch convention. Jäckel (2020, Section 2, eq. (20)) gives the single maximum through the inverse Mills ratio and the choice of the larger root, which is the argument written out for (b). Reiswich (2010, Section 3.8) shows that a smile delta can fail to be monotone; the sufficient condition in (c) is my own.

**Implementation.** `src/qef/fx/gk.py`.

## R6 (P). Diffusive null of the hedge cost

**Setting.** Garman–Kohlhagen with equal P and Q volatility and no jumps; the P-drift of log S exceeds the Q-drift by λ.

**Statement.**
- E^P(K − S_T)⁺ − E^Q(K − S_T)⁺ = −FλτΦ(−d₁) + o(λτ).
- Hence θ₀ = Φ(−d₁) + O(λτ).

**Source.** The leading-order form is stated by Farhi et al. (2015, Section 5.1, eqs. (8)–(9)). Jurek (2014) notes that an unlevered hedge gives up part of the diffusive premium. The exact mean-value form and the error bound are proved in notes.tex.

**Proof.** Mean value theorem, with ∂_G p(G) = −Φ(−d₊(G)) for the undiscounted put.

## R7 (P\*). Entropy decomposition

**Hypotheses.**
- M, M* > 0 in L²(𝔽_{t+1}).
- E_t|log M| < ∞ and E_t|log M*| < ∞.
- E_t M = e^{−r_t} and E_t M* = e^{−r*_t}.
- M S_{t+1}/S_t ∈ L².

**Lemma.** If one-period markets are complete in L², then M* = M S_{t+1}/S_t.

**Claims.**
- (i) E_t[Δs + r* − r] = L_t(M) − L_t(M*), and E_t[s_{t+1} − f_t] = L_t(M) − L_t(M*) − x_t.
- (ii) If the cumulant generating function of m has a Maclaurin series with radius of convergence greater than 1, then L_t(M) = Σ_{j≥2} κ_j/j!.

**Entropy bound** (Bansal and Lehmann, 1997; Alvarez and Jermann, 2005; as stated in Backus, Chernov and Zin, 2014). E L_t(M) ≥ E[log R − log R_f] for funded returns R > 0.

**Sources.** Backus, Foresi and Telmer (2001, Proposition 1 and eqs. (9)–(13)) give the decomposition of the currency premium into the difference of the two kernels' log-expectation minus expectation-of-log terms and its cumulant expansion; Backus, Chernov and Zin (2014) for conditional entropy and the bound; Lustig and Verdelhan (2019) for the decomposition with a wedge; Jiang, Krishnamurthy and Lustig (2021) for the convenience yield inferred from the Treasury basis; Brandt, Cochrane and Santa-Clara (2006). Writing the covered-interest-parity basis into the identity is an elementary step of my own.

## R8 (P). Local well-posedness of the smile calibration

**The system.** Three equations in (α, ρ, ν) at fixed β:
- the ATM delta-neutral-straddle volatility;
- the 25Δ risk reversal at the smile's own 25Δ strikes;
- equality of the market-strangle premium under the smile and under the flat volatility σ_ATM + BF.

**Statement.** If the Hagan volatility is smooth (a lemma for β = 1), the strike fixed points are non-degenerate (R5(c)) and the Jacobian is non-singular at a solution, the solution is locally unique and C¹ in the quotes (implicit function theorem, applied first to the strikes and then to the system).

**Sources.** The implicit-function-theorem argument follows Reiswich (2010, Theorems 2 and 3, Appendices A and B), who uses it for the volatility-strike function and for the market-strangle calibration of a simplified parabolic smile. Its application to the three SABR equations, the smoothness lemma for β = 1 and conditions (i) to (iv) are my own.

**Implementation.** `src/qef/fx/smile.py`, in the variables (ln α, atanh ρ, ln ν).

## R9 (C). Inference

**Central limit theorem** (Ibragimov, 1962, Theorem 1.7).
- Strict stationarity.
- E|X|^{2+δ} < ∞.
- Σ α(n)^{δ/(2+δ)} < ∞.
- A positive long-run variance.

**Stationary bootstrap.** Politis and Romano (1994); the moment and mixing conditions are those of Theorem 2 in their technical-report version (Politis and Romano, 1991). Weaker conditions: Gonçalves and de Jong (2003).

**The ratio θ.** Confidence procedures that are bounded with probability one have zero worst-case coverage (Gleser and Hwang, 1987; Dufour, 1997), so test inversion is used.

## Supporting derivation: the Garman–Kohlhagen PDE

- (P\*) The Garman–Kohlhagen price solves the PDE with terminal condition (S − K)⁺ (direct verification; Garman and Kohlhagen, 1983; Shreve, 2004).
- It is the unique C^{1,2} solution of polynomial growth that is continuous up to T (Feynman–Kac with localisation).
- No boundary condition at S = 0 is needed, because the exchange rate never reaches zero.
