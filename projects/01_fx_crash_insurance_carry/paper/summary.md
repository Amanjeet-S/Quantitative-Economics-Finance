# Crash insurance and the G10 carry premium: research summary

Amanjeet Singh, draft of 25 September 2026. Paper: [paper.pdf](paper.pdf) ([paper.tex](paper.tex)).

## Question

Does the price of crash insurance in G10 FX option smiles account for the carry premium and its change between the zero-rate regime (May 2013 to December 2021) and the hiking regime (from January 2022)? I fixed the design and its interpretation rules on 23 September 2026, before any estimate.

## Data

I obtained the data from LSEG Workspace under my university's student licence, which covers only me and does not permit redistribution. Composite dealer quotes for nine currencies against the dollar are sampled at New York month-ends from May 2013 to August 2026 (160 month-ends, 159 return months); Fenics quotes from January 2007 (72 usable month-ends) are secondary; VIX futures are from Cboe. Only aggregate results are published; rerunning the work needs the reader's own LSEG Workspace licence.

## Method

SABR smiles (β = 1; Hagan et al., 2002) are calibrated to at-the-money, 25Δ risk-reversal and 25Δ market-strangle quotes (Reiswich and Wystup, 2012). Each leg of a three-long, three-short forward-discount portfolio (Lustig, Roussanov and Verdelhan, 2011) is protected by a one-month 10Δ option, as in Burnside et al. (2011). E1 compares φ, the skew premium of protection per unit of forward discount, across regimes; E2 tests whether it predicts carry returns; E3 decomposes the realised hedge cost; E4 uses the other butterfly reading; E5 measures exposure to a VIX roll-down (Caballero and Doyle, 2012) and FX volatility (Menkhoff et al., 2012).

## Answer

Partial support only, under the pre-registered rules.

- The point estimate of φ falls from 0.809 to 0.454, but the difference (−0.355; Newey–West s.e. 0.204; bootstrap interval [−0.814, 0.014]) includes zero, so none is claimed. In a supplementary (post hoc) split, the skew cost is 11.24 and 11.19 bp per month while the forward-discount spread rises by 8.44 bp. Realised carry returns are higher after 2022 (37.0 against 7.4 bp per month), but the difference is not significant (post hoc).
- φ predicts carry returns in sample (bias-corrected one-sided p = 0.021) but not out of sample (Clark–West 1.639 against 1.645).
- The mean realised hedge cost is close to the ex-ante skew premium (−11.2 bp per month). The hedge-cost ratio θ_UB, 0.53 against a diffusive null of about 0.10, has an unbounded confidence set because the unhedged mean (17.7 bp, t = 1.47) is insignificant, and is not read as a crash share.
- Unhedged carry loads on the VIX roll-down (0.049, t = 7.41); the hedge lowers the loading by about a fifth.
- Only a ten-currency ranking makes the regime difference significant under both inferences, and there too the fall comes from the forward-discount spread.

The evidence points to a rise in the forward-discount spread rather than a change in the price of crash insurance.

## What the paper adds

- A decomposition of the realised cost of G10 crash insurance over 2013–2026, with a regime comparison of its ex-ante skew component, extending the option-hedged carry evidence of Jurek (2014).
- A pre-registered test of whether the skew price explains the change in the carry premium; secondarily, the butterfly reading, whose two versions Bossens et al. (2010) show can differ markedly for skewed smiles, moves φ by under 4 per cent.
- Theory: the currency-premium decomposition of Backus, Foresi and Telmer (2001), in the entropy form of Backus, Chernov and Zin (2014), restated with the covered-interest-parity basis as a wedge (as Lustig and Verdelhan, 2019, do with a general wedge); bounds on option-implied moments from truncated quotes under a stated tail condition, which are my own and extend the truncation bounds of Jiang and Tian (2005); and an exact form and error bound, my own, for the diffusive null whose leading-order form is due to Farhi et al. (2015).

## Limitations

A short hiking regime (roughly 8 effective observations per regime, post hoc), nine currencies, weak identification of θ_UB, realised terms that depend on the crashes that occurred, tail assumptions, composite quotes, end-of-day spot instead of the 10:00 New York cut, New York holidays only, an unconfirmed three-month USD OIS description, unchecked quote revisions and sensitivity to the training start. Requiring both intervals to exclude zero is my reading of the E1 rule.

## Documents

Reports: [E1, E4](../reports/e1.md), [E2, E3, E5](../reports/stage4.md), [robustness](../reports/robustness.md); [design](../research_design.md); [proofs](../theory/notes.tex); [sources](../references.md).
