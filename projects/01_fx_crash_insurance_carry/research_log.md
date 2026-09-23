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
