# 🎓 Pakistani University Admission Portal — AI Agent

> **Note:** This project is actively under development. What you see here is the foundation — more features, improvements, and a better UI are on the way.

---

## What is this?

A multi-agent AI system built with **Google ADK (Agent Development Kit)** that acts as a personal university admission assistant for Pakistani students.

Instead of juggling 5 different university websites, a student can simply ask questions in plain language and get instant, personalized answers about admissions, merit calculations, deadlines, and more.

---

## Why I built this

Pakistani students face a genuinely painful problem every admission season:
- Every university has a different aggregate formula
- Deadlines are scattered across different websites
- There's no single place to compare options based on your own marks

This project is my attempt to solve that with AI.

---

## Features (Current)

- 🧮 **Merit Calculator** — Calculates your aggregate for NUST, FAST, UET, COMSATS, and Air University using their exact formulas
- ✅ **Eligibility Check** — Tells you which universities you're realistically likely to get into based on your marks
- 📅 **Deadline Tracker** — Application deadlines and entry test dates in one place
- 🔍 **Live Search** — Fetches real-time admission news via Google Search (deadline extensions, HEC updates, scholarships)
- ⚖️ **University Comparison** — Side-by-side comparison of fee structures, locations, programs, and merit
- 🛡️ **Guardrails** — Stays focused on admissions only, politely declines off-topic queries
- 💾 **Per-Student Memory** — Each student gets their own isolated portal with persistent profile

---

## Agent Architecture

```
coordinator_agent          ← Root agent, routes all queries
├── profile_agent          ← Saves student marks & preferences  
├── merit_agent            ← Calculates aggregate per university
├── eligibility_agent      ← "Where can I get in?"
├── deadline_agent         ← Dates, deadlines, days remaining
├── comparison_agent       ← Side-by-side university comparison
└── search_agent           ← Live Google Search for dynamic info
```

---

## Universities Covered (v1)

| University | Entry Test | Weightage |
|---|---|---|
| NUST | NET (200) | Matric 10% · FSc 15% · Test 75% |
| FAST | NU Test / NAT | Matric 10% · FSc 40% · Test 50% |
| UET Lahore | ECAT (400) | Matric 25% · FSc 45% · Test 30% |
| COMSATS | NTS-NAT | Matric 10% · FSc 40% · Test 50% |
| Air University | AU-CBT | Matric 15% · FSc 35% · Test 50% |

---

## Tech Stack

- **Framework:** Google ADK (Agent Development Kit)
- **Language:** Python
- **Models:** Gemini (via Google AI Studio)
- **Architecture:** Multi-agent system with persistent memory and guardrails
- **Structure:** Fully modular — tools, agents, data, and runner are all separate

---

## Project Structure

```
student_portal/
├── agents/          # One file per agent
├── tools/           # One file per tool set
├── data/            # Static university data & formulas
├── runner/          # Session management & helper function
├── memory/          # Persistent memory config
└── main.py          # Entry point
```

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/MuhammadAhmad1258/student-portal.git
cd student-portal/student_portal

# 2. Install dependencies
pip install google-adk python-dotenv

# 3. Add your API key
echo "GOOGLE_API_KEY=your_key_here" > .env
echo "GOOGLE_GENAI_USE_VERTEXAI=0" >> .env

# 4. Run
python main.py
```

---

## What's Coming Next

This is just the beginning. Planned improvements include:

- [ ] Web UI (no more terminal)
- [ ] More universities (IBA, Aga Khan, and others)
- [ ] MDCAT support for medical students
- [ ] Scholarship finder agent
- [ ] WhatsApp bot integration
- [ ] Model upgrade for better responses

---

## About

Built by **Muhammad Ahmad** — an 18-year-old ICS student from Lahore, self-learning AI development outside of formal schooling.

This project is part of my journey into AI agent development using Google ADK. Feedback and contributions are welcome.

---

*If this helped you or you found it interesting, consider giving it a ⭐ on GitHub.*
