# profile_tools.py — Tools for saving/retrieving student profile

_profile_store = {}  # In-memory store (replace with persistent memory later)

def save_profile(name: str, city: str, field: str,
                 matric_obtained: float, matric_total: float,
                 fsc_obtained: float, fsc_total: float) -> str:
    """Save the student profile and marks to memory."""
    _profile_store["profile"] = {
        "name": name, "city": city, "field": field,
        "matric_obtained": matric_obtained, "matric_total": matric_total,
        "fsc_obtained": fsc_obtained, "fsc_total": fsc_total,
    }
    return f"Profile saved for {name}."

def get_profile() -> dict:
    """Retrieve the saved student profile."""
    return _profile_store.get("profile", {})

def update_marks(matric_obtained: float, matric_total: float,
                 fsc_obtained: float, fsc_total: float) -> str:
    """Update only the marks in the student profile."""
    if "profile" not in _profile_store:
        return "No profile found. Please save profile first."
    _profile_store["profile"].update({
        "matric_obtained": matric_obtained, "matric_total": matric_total,
        "fsc_obtained": fsc_obtained, "fsc_total": fsc_total,
    })
    return "Marks updated successfully."
