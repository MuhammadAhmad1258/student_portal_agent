# formulas.py — Aggregate weightages for each university (verified 2025)
# Keys: matric, fsc, test (all as decimals, must sum to 1.0)

FORMULAS = {
    "NUST":    {"matric": 0.10, "fsc": 0.15, "test": 0.75},  # NET out of 200
    "FAST":    {"matric": 0.10, "fsc": 0.40, "test": 0.50},  # NU Test / NAT
    "UET":     {"matric": 0.25, "fsc": 0.45, "test": 0.30},  # ECAT out of 400
    "COMSATS": {"matric": 0.10, "fsc": 0.40, "test": 0.50},  # NTS-NAT
    "AIR":     {"matric": 0.15, "fsc": 0.35, "test": 0.50},  # AU-CBT
}
