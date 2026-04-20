# merit_tools.py — Aggregate calculators for each university
from data.formulas import FORMULAS

def _calculate(matric_obt, matric_tot, fsc_obt, fsc_tot,
               test_obt, test_tot, weights: dict) -> float:
    """Generic aggregate calculator."""
    matric_pct = (matric_obt / matric_tot) * 100
    fsc_pct    = (fsc_obt / fsc_tot) * 100
    test_pct   = (test_obt / test_tot) * 100
    return round(
        (matric_pct * weights["matric"]) +
        (fsc_pct    * weights["fsc"]) +
        (test_pct   * weights["test"]), 2
    )

def calculate_nust_aggregate(matric_obt: float, matric_tot: float,
                              fsc_obt: float, fsc_tot: float,
                              net_score: float) -> str:
    """Calculate NUST aggregate. NET is out of 200."""
    agg = _calculate(matric_obt, matric_tot, fsc_obt, fsc_tot,
                     net_score, 200, FORMULAS["NUST"])
    return f"NUST Aggregate: {agg}%"

def calculate_fast_aggregate(matric_obt: float, matric_tot: float,
                              fsc_obt: float, fsc_tot: float,
                              test_pct: float) -> str:
    """Calculate FAST aggregate. Pass test score as percentage (0-100)."""
    agg = _calculate(matric_obt, matric_tot, fsc_obt, fsc_tot,
                     test_pct, 100, FORMULAS["FAST"])
    return f"FAST Aggregate: {agg}%"

def calculate_uet_aggregate(matric_obt: float, matric_tot: float,
                             fsc_obt: float, fsc_tot: float,
                             ecat_score: float) -> str:
    """Calculate UET aggregate. ECAT is out of 400."""
    agg = _calculate(matric_obt, matric_tot, fsc_obt, fsc_tot,
                     ecat_score, 400, FORMULAS["UET"])
    return f"UET Aggregate: {agg}%"

def calculate_comsats_aggregate(matric_obt: float, matric_tot: float,
                                 fsc_obt: float, fsc_tot: float,
                                 nts_pct: float) -> str:
    """Calculate COMSATS aggregate. Pass NTS score as percentage (0-100)."""
    agg = _calculate(matric_obt, matric_tot, fsc_obt, fsc_tot,
                     nts_pct, 100, FORMULAS["COMSATS"])
    return f"COMSATS Aggregate: {agg}%"

def calculate_air_aggregate(matric_obt: float, matric_tot: float,
                             fsc_obt: float, fsc_tot: float,
                             aucbt_pct: float) -> str:
    """Calculate Air University aggregate. Pass AU-CBT score as percentage."""
    agg = _calculate(matric_obt, matric_tot, fsc_obt, fsc_tot,
                     aucbt_pct, 100, FORMULAS["AIR"])
    return f"Air University Aggregate: {agg}%"
