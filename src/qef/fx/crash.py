"""Carry legs, protective options and the skew price of crash insurance (estimand E1).

Positions are in USD of forward notional. A leg long currency j loses when j
depreciates against USD; its protective option is a put on j, which is a put
on the quoted pair for EURUSD-type pairs and a call on the pair (a USD call)
for USD-base pairs. A short leg is protected by the opposite option.

Option notional matches the leg: 1/F units of base currency for EURUSD-type
pairs and one USD for USD-base pairs. In both cases the premium, carried to
delivery and expressed in USD per USD of forward notional, equals the
undiscounted premium on the quoted pair divided by the pair forward F.
"""

from __future__ import annotations

import numpy as np

from .conventions import G10
from .gk import CALL, PUT, forward_premium, strike_from_delta_smile


def forward_discount(S, F, usd_base: bool):
    """fd = log(X/F_X) with X in USD per unit of the non-USD currency."""
    return np.log(F / S) if usd_base else np.log(S / F)


def protective_option(currency: str, long_leg: bool) -> int:
    """Option type on the quoted pair (CALL or PUT) that pays when the leg loses."""
    usd_base = G10[currency].usd_base
    if long_leg:
        return CALL if usd_base else PUT
    return PUT if usd_base else CALL


def leg_skew_cost(vol_of_strike, F, tau, df_base, currency, sigma_atm, long_leg, delta=0.10):
    """Strike and premia (USD per USD of forward notional, at delivery) of a leg's protective option.

    The strike is the smile delta strike in the pair's convention. Returns
    (K, V_smile, V_flat), where V_flat prices the same strike at the ATM volatility.
    """
    conv = G10[currency].delta
    phi = protective_option(currency, long_leg)
    K = strike_from_delta_smile(phi * delta, F, tau, phi, conv, vol_of_strike, df_base)
    v_smile = float(forward_premium(F, K, float(vol_of_strike(K)), tau, phi)) / F
    v_flat = float(forward_premium(F, K, sigma_atm, tau, phi)) / F
    return K, v_smile, v_flat


def rank_legs(fd: dict, n_legs: int):
    """Currencies with the n highest (long) and n lowest (short) forward discounts."""
    order = sorted(fd, key=fd.get)
    return order[-n_legs:], order[:n_legs]
