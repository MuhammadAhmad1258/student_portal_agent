"""
Student Admission Portal — Project Setup Script
Run this ONCE to create the full modular folder structure.

Usage:
    python setup_project.py
"""

import os

# ── Folder structure ────────────────────────────────────────────
FOLDERS = [
    "student_portal",
    "student_portal/agents",
    "student_portal/tools",
    "student_portal/data",
    "student_portal/runner",
    "student_portal/memory",
]

# ── Files to create with starter content ───────────────────────
FILES = {

    # Root
    "student_portal/main.py": '''\
import asyncio
from runner.session import create_session_and_runner
from runner.helper import call_agent_async

async def main():
    await create_session_and_runner()
    print("Student Portal ready! Type your query.")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            break
        await call_agent_async(query)

if __name__ == "__main__":
    asyncio.run(main())
''',

    "student_portal/.env": '''\
GOOGLE_API_KEY=your_gemini_api_key_here
''',

    # Agents
    "student_portal/agents/__init__.py": "",

    "student_portal/agents/coordinator.py": '''\
# coordinator.py — Root agent, routes all queries to sub-agents
from google.adk.agents import LlmAgent

coordinator_agent = LlmAgent(
    name="coordinator",
    model="gemini-2.0-flash",
    description="Main coordinator for the Student Admission Portal.",
    instruction="""
    You are the main agent for a Pakistani university admission portal.
    Route the user query to the correct sub-agent:
    - Profile questions → profile_agent
    - Merit/aggregate calculation → merit_agent
    - Eligibility (where can I get in) → eligibility_agent
    - Deadlines and dates → deadline_agent
    - University comparison → comparison_agent
    - Live/current info → search_agent
    Only handle admissions-related queries. Politely decline anything else.
    """,
    sub_agents=[],  # Import and add sub-agents here
)
''',

    "student_portal/agents/profile_agent.py": '''\
# profile_agent.py — Handles student profile and marks
from google.adk.agents import LlmAgent
from tools.profile_tools import save_profile, get_profile, update_marks

profile_agent = LlmAgent(
    name="profile_agent",
    model="gemini-2.0-flash",
    description="Saves and retrieves student profile and marks.",
    instruction="""
    Help the student set up or update their profile.
    Collect: name, city, matric marks, FSc marks, field of interest.
    Use the available tools to save and retrieve this information.
    """,
    tools=[save_profile, get_profile, update_marks],
)
''',

    "student_portal/agents/merit_agent.py": '''\
# merit_agent.py — Calculates aggregate for each university
from google.adk.agents import LlmAgent
from tools.merit_tools import (
    calculate_nust_aggregate,
    calculate_fast_aggregate,
    calculate_uet_aggregate,
    calculate_comsats_aggregate,
    calculate_air_aggregate,
)

merit_agent = LlmAgent(
    name="merit_agent",
    model="gemini-2.0-flash",
    description="Calculates admission aggregate for Pakistani universities.",
    instruction="""
    Calculate the student's aggregate for requested universities.
    Always show a breakdown of how each component contributes.
    Supported: NUST, FAST, UET, COMSATS, Air University.
    """,
    tools=[
        calculate_nust_aggregate,
        calculate_fast_aggregate,
        calculate_uet_aggregate,
        calculate_comsats_aggregate,
        calculate_air_aggregate,
    ],
)
''',

    "student_portal/agents/eligibility_agent.py": '''\
# eligibility_agent.py — Tells student where they can get in
from google.adk.agents import LlmAgent
from tools.eligibility_tools import get_eligible_universities, get_realistic_chances

eligibility_agent = LlmAgent(
    name="eligibility_agent",
    model="gemini-2.0-flash",
    description="Tells student which universities they are eligible for.",
    instruction="""
    Based on student's aggregate scores, tell them which universities
    they are likely, possibly, or unlikely to get into.
    Compare against last year's closing merits from data/.
    """,
    tools=[get_eligible_universities, get_realistic_chances],
)
''',

    "student_portal/agents/deadline_agent.py": '''\
# deadline_agent.py — Handles dates, deadlines, test schedules
from google.adk.agents import LlmAgent
from tools.deadline_tools import (
    get_application_deadline,
    get_entry_test_date,
    get_days_remaining,
)

deadline_agent = LlmAgent(
    name="deadline_agent",
    model="gemini-2.0-flash",
    description="Provides deadlines and entry test dates for universities.",
    instruction="""
    Answer questions about application deadlines, entry test dates,
    and days remaining. Always mention if data may be outdated and
    suggest checking the official university website.
    """,
    tools=[get_application_deadline, get_entry_test_date, get_days_remaining],
)
''',

    "student_portal/agents/comparison_agent.py": '''\
# comparison_agent.py — Side by side university comparison
from google.adk.agents import LlmAgent
from tools.comparison_tools import compare_universities, get_fee_structure

comparison_agent = LlmAgent(
    name="comparison_agent",
    model="gemini-2.0-flash",
    description="Compares two universities side by side.",
    instruction="""
    Compare universities on: fee structure, location, programs,
    closing merit, hostel availability, and general reputation.
    Be balanced and factual.
    """,
    tools=[compare_universities, get_fee_structure],
)
''',

    "student_portal/agents/search_agent.py": '''\
# search_agent.py — Live Google Search for dynamic info
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

search_agent = LlmAgent(
    name="search_agent",
    model="gemini-2.0-flash",
    description="Searches the web for live admission news and updates.",
    instruction="""
    Search for current, time-sensitive admission information:
    deadline extensions, HEC policy changes, new scholarships,
    university announcements. Only search admission-related topics.
    """,
    tools=[google_search],
)
''',

    # Tools
    "student_portal/tools/__init__.py": "",

    "student_portal/tools/profile_tools.py": '''\
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
''',

    "student_portal/tools/merit_tools.py": '''\
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
''',

    "student_portal/tools/eligibility_tools.py": '''\
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
    return "\n".join(results) if results else "No data available for this field."

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
    return "\n".join(lines)
''',

    "student_portal/tools/deadline_tools.py": '''\
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
''',

    "student_portal/tools/comparison_tools.py": '''\
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
        lines.append(f"{f:<20} {str(u1.get(f,'N/A')):<20} {str(u2.get(f,'N/A')):<20}")
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
''',

    # Data
    "student_portal/data/__init__.py": "",

    "student_portal/data/formulas.py": '''\
# formulas.py — Aggregate weightages for each university (verified 2025)
# Keys: matric, fsc, test (all as decimals, must sum to 1.0)

FORMULAS = {
    "NUST":    {"matric": 0.10, "fsc": 0.15, "test": 0.75},  # NET out of 200
    "FAST":    {"matric": 0.10, "fsc": 0.40, "test": 0.50},  # NU Test / NAT
    "UET":     {"matric": 0.25, "fsc": 0.45, "test": 0.30},  # ECAT out of 400
    "COMSATS": {"matric": 0.10, "fsc": 0.40, "test": 0.50},  # NTS-NAT
    "AIR":     {"matric": 0.15, "fsc": 0.35, "test": 0.50},  # AU-CBT
}
''',

    "student_portal/data/universities.py": '''\
# universities.py — Static info for all 5 universities
# Update deadlines/dates each admission cycle

UNIVERSITIES = {
    "NUST": {
        "full_name": "National University of Sciences and Technology",
        "location": "Islamabad",
        "sector": "Public",
        "entry_test": "NET (out of 200)",
        "semester_fee": "PKR 150,000 – 250,000",
        "hostel_available": True,
        "hostel_fee": "PKR 30,000 – 50,000 / semester",
        "application_deadline": "2025-06-24",
        "entry_test_date": "2025-07-15",
        "closing_merit": {
            "CS": 82.0,
            "Electrical Engineering": 79.0,
            "Mechanical Engineering": 76.0,
        },
    },
    "FAST": {
        "full_name": "FAST National University of Computer and Emerging Sciences",
        "location": "Lahore / Islamabad / Karachi / Peshawar / Chiniot",
        "sector": "Private",
        "entry_test": "NU Test / NAT",
        "semester_fee": "PKR 120,000 – 180,000",
        "hostel_available": True,
        "hostel_fee": "PKR 25,000 – 40,000 / semester",
        "application_deadline": "2025-07-01",
        "entry_test_date": "2025-07-20",
        "closing_merit": {
            "CS": 78.0,
            "Software Engineering": 75.0,
            "Business": 70.0,
        },
    },
    "UET": {
        "full_name": "University of Engineering and Technology Lahore",
        "location": "Lahore",
        "sector": "Public",
        "entry_test": "ECAT (out of 400)",
        "semester_fee": "PKR 40,000 – 80,000",
        "hostel_available": True,
        "hostel_fee": "PKR 15,000 – 25,000 / semester",
        "application_deadline": "2025-06-28",
        "entry_test_date": "2025-07-13",
        "closing_merit": {
            "CS": 75.0,
            "Electrical Engineering": 73.0,
            "Civil Engineering": 70.0,
        },
    },
    "COMSATS": {
        "full_name": "COMSATS University Islamabad",
        "location": "Islamabad / Lahore / Wah / Attock / Vehari / Sahiwal / Abbottabad",
        "sector": "Public",
        "entry_test": "NTS-NAT",
        "semester_fee": "PKR 50,000 – 100,000",
        "hostel_available": True,
        "hostel_fee": "PKR 20,000 – 35,000 / semester",
        "application_deadline": "2025-07-10",
        "entry_test_date": "2025-07-27",
        "closing_merit": {
            "CS": 77.0,
            "Software Engineering": 75.0,
            "Electrical Engineering": 73.0,
        },
    },
    "AIR": {
        "full_name": "Air University Islamabad",
        "location": "Islamabad",
        "sector": "Public (PAF)",
        "entry_test": "AU-CBT",
        "semester_fee": "PKR 60,000 – 120,000",
        "hostel_available": True,
        "hostel_fee": "PKR 20,000 – 30,000 / semester",
        "application_deadline": "2025-07-05",
        "entry_test_date": "2025-07-22",
        "closing_merit": {
            "CS": 74.0,
            "Software Engineering": 72.0,
            "Electrical Engineering": 70.0,
        },
    },
}
''',

    # Runner
    "student_portal/runner/__init__.py": "",

    "student_portal/runner/session.py": '''\
# session.py — Session and runner setup
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agents.coordinator import coordinator_agent

APP_NAME   = "student_portal"
USER_ID    = "student_1"
SESSION_ID = "session_1"

session_service = InMemorySessionService()
runner = None  # Initialized in create_session_and_runner()

async def create_session_and_runner():
    global runner
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )
    runner = Runner(
        agent=coordinator_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
''',

    "student_portal/runner/helper.py": '''\
# helper.py — call_agent_async helper function
from google.genai import types
from runner.session import runner, USER_ID, SESSION_ID

async def call_agent_async(query: str):
    """Wrap query, run agent, extract and return final response."""
    content = types.Content(role="user", parts=[types.Part(text=query)])
    events = runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content,
    )
    async for event in events:
        if event.is_final_response():
            response = event.content.parts[0].text
            print(f"Agent: {response}")
            return response
''',

    # Memory
    "student_portal/memory/__init__.py": "",

    "student_portal/memory/store.py": '''\
# store.py — Persistent memory configuration
# Currently using InMemorySessionService for dev.
# For production, replace with VertexAiSessionService or DatabaseSessionService.

# Placeholder — memory config will go here as project grows.
''',
}

# ── Script execution ────────────────────────────────────────────
def create_structure():
    print("Setting up Student Portal project...\n")

    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        print(f"  Created folder: {folder}/")

    for filepath, content in FILES.items():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created file  : {filepath}")

    print("\nDone! Your project structure is ready.")
    print("Next steps:")
    print("  1. cd student_portal")
    print("  2. Add your GOOGLE_API_KEY in .env")
    print("  3. pip install google-adk")
    print("  4. python main.py")

if __name__ == "__main__":
    create_structure()