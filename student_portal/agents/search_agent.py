# search_agent.py — Live Google Search for dynamic info
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

search_agent = LlmAgent(
    name="search_agent",
    model="gemini-2.5-flash",
    description="Searches the web for live admission news and updates.",
    instruction="""
    Search for current, time-sensitive admission information:
    deadline extensions, HEC policy changes, new scholarships,
    university announcements. Only search admission-related topics.
    """,
    tools=[google_search],
)
