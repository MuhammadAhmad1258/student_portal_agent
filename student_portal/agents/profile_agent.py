# profile_agent.py — Handles student profile and marks
from google.adk.agents import LlmAgent
from tools.profile_tools import save_profile, get_profile, update_marks

profile_agent = LlmAgent(
    name="profile_agent",
    model="gemini-2.5-flash",
    description="Saves and retrieves student profile and marks.",
    instruction="""
    Help the student set up or update their profile.
    Collect: name, city, matric marks, FSc marks, field of interest.
    Use the available tools to save and retrieve this information.
    """,
    tools=[save_profile, get_profile, update_marks],
)
