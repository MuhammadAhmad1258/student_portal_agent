# coordinator.py — Root agent, routes all queries to sub-agents
from google.adk.agents import LlmAgent

from agents.comparison_agent import comparison_agent
from agents.merit_agent import merit_agent
from agents.eligibility_agent import eligibility_agent
from agents.deadline_agent import deadline_agent
from agents.profile_agent import profile_agent
from agents.search_agent import search_agent
coordinator_agent = LlmAgent(
    name="coordinator",
    model="gemini-2.5-flash",
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
    sub_agents=[deadline_agent,comparison_agent,eligibility_agent,merit_agent,profile_agent,search_agent],  # Import and add sub-agents here
)
