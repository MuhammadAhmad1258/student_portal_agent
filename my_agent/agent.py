from google.adk.agents import Agent

def get_weather(city: str) -> str:
    
    return f"{city} mein aaj 32 degree hai aur dhoop hai."
import datetime
import pytz
from google.adk.tools import google_search
def get_city_time(city: str) -> str:
    """Returns the current time for a given city."""
    
    city_timezones = {
        "karachi": "Asia/Karachi",
        "lahore": "Asia/Karachi",
        "islamabad": "Asia/Karachi",
        "dubai": "Asia/Dubai",
        "london": "Europe/London",
        "new york": "America/New_York",
        "tokyo": "Asia/Tokyo",
        "paris": "Europe/Paris",
    }
    
    timezone = city_timezones.get(city.lower())
    
    if not timezone:
        return f"{city} ka timezone mujhe nahi pata."
    
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    return f"{city} mein abhi {now.strftime('%I:%M %p')} baj rahe hain."
def fitness_recorder(name,age:str):
    """Returns the fitness requirments to user using google search"""
    
root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You have to answer user questions,we have access to 2 tools but i am also giving you access to google_search.ok,but make sure data is true',
    tools=[get_weather,get_city_time,google_search]
)#this was my agent
