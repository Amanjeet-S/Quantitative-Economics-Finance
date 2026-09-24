# Research log

## 2026-09-23

- **Design version 1.0 fixed.** No returns, hedge costs or option-implied statistics had been computed.
- **Butterfly reading.** A three-parameter smile reproduces either butterfly reading exactly, so the reading is set by provider documentation, then by the interdealer convention. The 10Δ fit is supporting evidence only.
- **Primary hedge moneyness is 10Δ.** At one month, 25Δ strikes lie about 2% out of the money.
- **Payoff spot.** WM fixings are not licensed. Option payoffs use end-of-day spot, with a sensitivity check.
- **Independent cross-check.** QuantLib replaces the MATLAB implementation first considered, because it is open source and reproducible without a licence.
- **Pricing and smile engine implemented:**
  - Garman–Kohlhagen pricing in four delta conventions.
  - Delta inversion, including the premium-adjusted branch rule.
  - SABR calibration under both butterfly readings.
  - Static-arbitrage checks.
  - Tests: parity, delta-neutral straddle, inversion round trips, and synthetic SABR recovery under both readings and both delta types.
- **QuantLib cross-check** (QuantLib 1.43, independent C++ implementation). Premiums, deltas in the spot, forward and premium-adjusted conventions, delta-to-strike inversion, delta-neutral ATM strikes and Hagan SABR volatilities agree to between 1e-9 and 1e-13 on the test grid (`tests/test_quantlib_crosscheck.py`).

## 2026-09-23 (data audit)

- **Acquired and audited.** The LSEG panel was acquired: spot, forward points, ATM volatility, 25Δ and 10Δ risk reversals and butterflies at 1M and 3M for the composite and Fenics contributors, one-month rates and VIX futures. Audit checks 1 to 5, 8 and 9 were run. Counts and dates are in the private audit.
- **Conventions confirmed.** Every volatility instrument, including NOK and SEK, is quoted against USD, so no triangulation is needed. Provider scaling factors confirm the configured pip factors. Risk reversals are call minus put on the quoted pair, and the 10Δ quotes follow the same convention.
- **Clarification: extended sample.** The rule requires the calibration set only (ATM, 25Δ risk reversal, 25Δ butterfly) plus forward points. 10Δ quotes are used for the fit test where available. This was recorded before any estimate was computed.
- **Extended-sample quality.** Fenics quotes before 2010 update infrequently, and butterflies in particular are often unchanged for weeks. Extended-sample results are therefore secondary evidence. The stale-butterfly robustness run applies to them, and the long ATM sample is used alongside them for 2008.
- **USD deposit rate added.** `USD1MD=` was added to the catalogue so that the forward-point check compares deposit rates with deposit rates. OIS RICs do not exist for EUR and SEK. (Corrected on 24 September: USD discounting uses Fed Funds OIS as designed; the other currencies use deposit rates. See the entry of that date.)
- **Remaining for Stage 1** at that point: checks 6 and 7, a second retrieval to check for quote revisions, and the snapshot time of daily history.

## 2026-09-24

- **Snapshot time.** Daily history was matched against intraday bars over windows in January, March and August to September 2026. The composite daily value corresponds to about 21:18 UTC in both summer and winter, that is, a fixed UTC time rather than a New York local close. The Fenics daily value corresponds to about 17:16 London time. Option payoffs and month-end alignment use these times; the sensitivity check in the design (same-day and previous-day close) is unchanged.
- **Check 6 (conventions).** The instrument metadata name only the quote type and the delta. LSEG's surface-construction documentation gives defaults for its own surfaces (spot delta, premium-adjusted) but does not define the contributed quotes. Delta and premium conventions therefore follow market convention (Clark, 2011; Reiswich and Wystup, 2010), as configured.
- **Check 7 (butterfly reading).** Provider documentation is silent. Under the pre-registered order of evidence, the market-strangle reading is primary. The supporting diagnostic points the other way: across the primary sample, smiles calibrated under the smile-strangle reading predict the held-out 10Δ butterflies better in most month-ends and every currency, with small absolute differences. This is recorded as evidence against the primary reading. E4, which recomputes E1 and the skew term of E3 under the smile-strangle reading, is therefore reported alongside the primary results, not as a footnote.
- **Stage 2 (panel calibration).** Every month-end smile in the primary sample was calibrated under both readings: all converged, with residuals below 1e-13 and all smiles free of static arbitrage within ±4 and ±10 ATM standard deviations. Counts and diagnostics are in the private results. Stage 2's completion criterion is met.
- **Bug fixed during calibration.** The market-strangle butterfly bracket in `quotes_from_smile` could test a negative strangle volatility for low-volatility pairs, which sent the premium-adjusted delta maximiser into an unbounded loop. Volatility is now validated, bracket expansions are bounded and the butterfly bracket keeps σ_ATM + BF positive. Regression tests were added. The delta-to-strike search now brackets locally before scanning and evaluates the smile on the whole grid at once.
- **Remaining for Stage 1:** a second retrieval to check for quote revisions.
- **Citations verified.** Every cited source was checked for its bibliographic details (Crossref, OpenAlex, JSTOR, Project Euclid, publisher pages). Each specific claim attributed to a source was checked against the text, and [references.md](references.md) records what each source is used for and which version was read. Corrections made:
  - The entropy bound is attributed jointly to Bansal and Lehmann (1997) and Alvarez and Jermann (2005), as stated in Backus, Chernov and Zin (2014).
  - The remark on strict-local-martingale exchange rates now states that the foreign measure exists but is not equivalent (Carr, Fisher and Ruf, 2014).
  - Brandt, Cochrane and Santa-Clara (2006) are cited for a risk-sharing index, not a correlation.
  - Delta conventions are cited to Reiswich and Wystup (2012), whose working-paper version was read, and Clark (2011) only as reported there.
  - Brunnermeier, Nagel and Pedersen is dated 2008 (NBER Macroeconomics Annual 2008).
  - The bootstrap conditions are cited to the technical-report version of Politis and Romano.
- **Deviation (before any inference was run): HAC bandwidth.** The design stated a Newey–West lag of ⌊4(T/100)^{2/9}⌋ and attributed it to Newey and West (1994). In that paper this quantity is the pilot truncation of an automatic procedure whose bandwidth is ⌊γ̂ T^{1/3}⌋; using the pilot value directly as the lag is a software convention. The design now uses the full automatic procedure. No standard error had been computed under the earlier rule.

## 2026-09-24 (Stage 3)

- **Stage 3 run.** E1, E4, the 25Δ comparison, the extended sample and the splice test were estimated as specified (`scripts/estimate_e1.py`; method record in [reports/e1.md](reports/e1.md)). The results are held in `data/private/results/` until the licence terms for publishing LSEG-derived findings are confirmed. The ATM comparison named in the design is identically zero by construction, so it is not reported.
- **Independent review before the results were recorded.** A separate review of the estimand and inference code found no error affecting the primary estimates. An independent QuantLib rebuild of every leg agreed to machine precision, and the standard errors matched the R package sandwich exactly. It found five departures, all corrected before the final run; each had a negligible effect on the primary estimates:
  - The extended sample now requires the calibration set only, as logged on 23 September.
  - Option dates are built on the New York calendar, and volatility time is trade to expiry.
  - Provider days-to-maturity is used where reported, and computed spot-to-delivery days otherwise, instead of a 30-day fallback.
  - Currencies, not whole months, are excluded when inputs are missing; non-converged smiles are used and counted.
  - The splice test compares skew costs leg by leg, including the pre-2013 overlap, instead of rows that held by construction.
- **Deviation: discount rates.** The design allows OIS "where available" for non-USD currencies. The implementation uses one-month deposit rates for every non-USD currency, for consistency across currencies. Rates enter E1 only through the base-currency discount factor in spot delta. The review bounded the effect on that factor at about 0.1 per cent, which is negligible for the strikes.
- **Supplementary analyses (post hoc).** Added after the first E1 results, because the series is highly persistent and its zero-rate distribution has a heavy right tail from months with very small forward discounts. With so few effective observations, the automatic Newey–West bandwidth is capped well below what the persistence would require, so the pre-registered intervals are likely too narrow. The additions, listed in [reports/e1.md](reports/e1.md), are reported alongside the pre-registered estimand and do not replace it.
- **Next:** Stage 4 (portfolio returns, E2, E3 and E5).
