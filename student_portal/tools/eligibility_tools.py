# eligibility_tools.py — Eligibility checking tools
from data.universities import UNIVERSITIES

def get_eligible_universities(aggregate: float, field: str) -> str:
    """Return universities the student is likely eligible for based on aggregate."""
    results = []
    for uni, info in UNIVERSITIES.items():
        closing = info.get("closing_merit", {}).get(field, None)
        if closing is None:
            continue
        if aggregate >= closing + 2:
            status = "✅ Likely"
        elif aggregate >= closing - 2:
            status = "⚠️ Borderline"
        else:
            status = "❌ Unlikely"
        results.append(f"{uni}: {status} (Closing merit ~{closing}%)")
    return "
".join(results) if results else "No data available for this field."

def get_realistic_chances(aggregate: float, university: str) -> str:
    """Get admission chances for a specific university."""
    uni_data = UNIVERSITIES.get(university.upper())
    if not uni_data:
        return f"University '{university}' not found in database."
    closing = uni_data.get("closing_merit", {})
    lines = [f"Chances at {university} (your aggregate: {aggregate}%):"]
    for program, merit in closing.items():
        diff = aggregate - merit
        if diff >= 2:
            status = "✅ Good chance"
        elif diff >= -2:
            status = "⚠️ Borderline"
        else:
            status = "❌ Below closing merit"
        lines.append(f"  {program}: {status} (closing ~{merit}%)")
    return "
".join(lines)
