# Stage 4: portfolio returns, E2 and E3

Stage 4 of the [research design](../research_design.md), except E5, which needs individual VIX futures contracts. Aggregate results only; month-level series stay in `data/private/results/`.

## Reproduction

```bash
.venv/bin/python scripts/estimate_stage4.py
```

## Returns

- **Legs.** Legs are those of the E1 series: market reading, 3L/3S in the primary sample and 2L/2S in the extended sample. The portfolio sorts on the forward discount, in the manner of Lustig, Roussanov and Verdelhan (2011), who sort currencies into six portfolios on f − s at each month-end and take the highest minus the lowest. With nine currencies the analogue is the top three minus the bottom three.
- **Excess returns.** Arithmetic, per USD of forward notional. They are evaluated at the spot quote on the option expiry date, which is the spot rate for value on the forward's delivery date (`src/qef/fx/crash.py`).
- **Hedged returns.** Each leg adds its protective option's payoff less its premium carried to delivery. Hedges are at 10Δ (primary), 25Δ and ATM.
- **Spot quotes.** Spot is the daily mid; six leg-months use the previous available quote.

## E2: predictability of the unhedged carry return

The regression is HML^U_{t+1} = a + b x_t, with x_t = φ_t (primary) or the oriented 10Δ risk reversal (quoted; protective-option volatility minus opposite-option volatility, averaged over legs).

- **In sample.** Newey–West errors (automatic bandwidth), and a residual bootstrap under the null of no predictability (9,999 draws).
  - The bootstrap draws the pairs (û_k, v̂_{k+1}) independently. û are residuals of the unrestricted regression; v̂ are AR(1) residuals of the predictor.
  - The bootstrap bias is checked against the first-order approximation of Stambaugh (1999, eq. 18), −(σ_uv/σ_v²)(1 + 3ρ)/T.
- **Out of sample.** Expanding window. The first forecast, made at end-December 2016, is for January 2017; training starts with the extended sample. The test is the MSPE-adjusted statistic of Clark and West (2007) against the historical mean. It is one-sided, with the least-squares standard error recommended for one-step forecasts; Newey–West is reported alongside.

| Predictor | b | HAC t | Bootstrap bias (analytic) | Bias-corrected b | One-sided p (b > 0) | OOS R² | Clark–West t (p) | Clark–West t, NW (p) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| φ | 0.0062 | 5.96 | 0.00049 (0.00049) | 0.0057 | 0.021 | 3.7% | 1.640 (0.0505) | 1.50 (0.067) |
| Oriented 10Δ RR | 0.397 | 4.13 | 0.0159 (0.0147) | 0.381 | 0.005 | −5.5% | −1.11 (0.87) | −1.19 (0.88) |

There are 117 out-of-sample forecasts. The correlation between the two predictors is 0.56. The predictors are persistent, with AR(1) coefficients of 0.86 for φ and 0.52 for the risk reversal. Their innovations are negatively correlated with returns (−0.39 and −0.53).

**Interpretation under the pre-registered rules.**

- **In sample.** A higher skew price per unit of carry predicts higher carry returns in the following month, after the small-sample bias correction (one-sided p = 0.021). The sign is the one a crash-compensation reading implies.
- **Out of sample.** The Clark–West statistic of 1.640 falls just short of the 5% one-sided critical value of 1.645, so predictability is not established.
- **The risk reversal alone** predicts in sample but not out of sample.
- **The regime-shift question.** The claim that crash-insurance pricing explains the regime shift requires the E1 difference, a bias-corrected b > 0 and an out-of-sample rejection. Only the second holds, so the evidence is reported as partial support.

## E3: decomposition of the hedge cost

Terms are in basis points of notional per month (primary sample, 160 months, 10Δ hedge), with Newey–West standard errors.

- **Term (i)** is the realised payoff minus the Garman–Kohlhagen value at forecast realised volatility σ̂P. σ̂P is the realised volatility over the previous 21 business days.
- **Term (ii)** is the volatility-level term: minus the flat-ATM premium less that value.
- **Term (iii)** is the skew term: minus the smile premium less the flat-ATM premium.
- The three terms add up to HML^H − HML^U.

| Quantity | Mean | s.e. |
| --- | --- | --- |
| HML^U (unhedged) | 17.6 | 12.0 |
| HML^H, 10Δ | 8.2 | 11.8 |
| HML^H, 25Δ | 8.7 | 11.2 |
| HML^H, ATM | 9.6 | 8.9 |
| (i) payoff less σ̂P value | 0.4 | 3.8 |
| (ii) volatility level | 1.4 | 1.3 |
| (iii) skew | −11.2 | 0.65 |

- **Hedge-cost ratio.** θ_UB = 1 − mean(HML^H)/mean(HML^U) is 0.54 at 10Δ, 0.50 at 25Δ and 0.46 at ATM. The diffusive null of result R6 is θ₀ ≈ 0.10 at 10Δ: the average forward delta of the hedges.
- **Confidence set.** The test-inversion 95% set for θ_UB is unbounded, because the mean unhedged carry return is not significantly different from zero in this sample (t = 1.47). As the design anticipated, the ratio is weakly identified, so no point value is claimed.
- **What the decomposition shows.** The realised cost of 10Δ crash insurance over 2013–2026 consists almost entirely of the skew term. It is precisely estimated and equals the ex-ante skew price of E1. The payoff and volatility-level terms are small and not distinguishable from zero.

**Extended sample.** Fenics quotes, 2007–2013, 72 months. The unhedged mean is 8.4 bp (s.e. 62.7). Term (i) is 16.7 bp (s.e. 10.2), reflecting option payoffs in 2008, and the skew term is −22.3 bp (s.e. 3.0).
