# comparison_tools.py — University comparison tools
from data.universities import UNIVERSITIES

def compare_universities(uni1: str, uni2: str) -> str:
    """Compare two universities side by side."""
    u1 = UNIVERSITIES.get(uni1.upper())
    u2 = UNIVERSITIES.get(uni2.upper())
    if not u1:
        return f"'{uni1}' not found in database."
    if not u2:
        return f"'{uni2}' not found in database."

    fields = ["location", "semester_fee", "entry_test", "hostel_available", "sector"]
    lines = [f"{'Feature':<20} {uni1:<20} {uni2:<20}"]
    lines.append("-" * 60)
    for f in fields:
        lines.append(f"{f:<20} {str(u1.get(f, 'N/A')):<20} {str(u2.get(f, 'N/A')):<20}")
    return "\n".join(lines)

def get_fee_structure(university: str) -> str:
    """Get fee structure for a university."""
    uni_data = UNIVERSITIES.get(university.upper())
    if not uni_data:
        return f"University '{university}' not found."
    fee = uni_data.get("semester_fee", "Not available")
    hostel = uni_data.get("hostel_fee", "Not available")
    return (
        f"{university} Fee Structure:\n"
        f"  Semester Fee : {fee}\n"
        f"  Hostel Fee   : {hostel}"
    )