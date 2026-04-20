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
