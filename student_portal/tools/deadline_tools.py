# deadline_tools.py — Deadline and date tools
from data.universities import UNIVERSITIES
from datetime import datetime

def get_application_deadline(university: str) -> str:
    """Get the application deadline for a university."""
    uni_data = UNIVERSITIES.get(university.upper())
    if not uni_data:
        return f"University '{university}' not found."
    deadline = uni_data.get("application_deadline", "Not available")
    return f"{university} application deadline: {deadline}"

def get_entry_test_date(university: str) -> str:
    """Get the entry test date for a university."""
    uni_data = UNIVERSITIES.get(university.upper())
    if not uni_data:
        return f"University '{university}' not found."
    test_date = uni_data.get("entry_test_date", "Not available")
    return f"{university} entry test date: {test_date}"

def get_days_remaining(university: str) -> str:
    """Get how many days are left until the application deadline."""
    uni_data = UNIVERSITIES.get(university.upper())
    if not uni_data:
        return f"University '{university}' not found."
    deadline_str = uni_data.get("application_deadline", None)
    if not deadline_str:
        return "Deadline not available."
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        days_left = (deadline - datetime.now()).days
        if days_left < 0:
            return f"{university} deadline has passed."
        return f"{days_left} days remaining for {university} application."
    except ValueError:
        return f"Deadline format error for {university}."
