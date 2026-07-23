# RiseOS

A Python-based personal morning operating system. RiseOS pulls data from six
external sources, monitors and logs system events overnight, exposes everything
through a REST API layer, and delivers a clean formatted morning brief every day
on an automated schedule.

Built with modularity at its core. New data sources and personal modules can be
added without restructuring anything that already exists.

# What It Does

RiseOS runs four core systems in parallel:

- **Event Monitor** — tracks CPU spikes, memory usage, disk thresholds, and
  file system changes throughout the day and overnight
- **Logger** — writes every event to a SQLite database with timestamp, source,
  event type, severity, and description
- **REST API Layer** — a Flask application that exposes the event log and
  briefing data as queryable endpoints
- **Daily Briefing Generator** — aggregates all six data sources plus the
  overnight event log and outputs a formatted morning brief every morning on
  schedule

# Morning Brief

Each daily brief includes:

| Section | Source |
|---|---|
| Date and daily intention | Local config |
| Weather | OpenWeatherMap API |
| Tech news | Hacker News API |
| Stocks | Alpha Vantage API |
| New music releases | Spotify API (OAuth) |
| Sports events | TheSportsDB API |
| Wellness goals | Local config |
| Overnight event summary | SQLite event log |

# Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| API Layer | Flask |
| Database | SQLite |
| Scheduling | APScheduler |
| HTTP Calls | Requests |
| Testing | Pytest |
| Version Control | Git / GitHub |

# Project Structure

riseos/
├── main.py
├── config.py
├── database/
│   └── db.py
├── monitors/
│   ├── weather.py
│   ├── news.py
│   ├── stocks.py
│   ├── music.py
│   ├── sports.py
│   └── system.py
├── logger/
│   └── event_logger.py
├── api/
│   └── routes.py
├── briefing/
│   └── generator.py
├── scheduler/
│   └── jobs.py
└── tests/
└── test_monitors.py

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /brief | Returns full morning brief as JSON |
| GET | /events | Returns all logged events |
| GET | /events?severity=high | Filter events by severity |
| GET | /summary | Returns aggregated event stats |
| POST | /events | Manual event injection for testing |

# Installation

```bash
git clone https://github.com/YOUR_USERNAME/riseos.git
cd riseos
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configuration

Copy config.py and add your API keys and personal settings before running.
Required keys:

	•	OpenWeatherMap API key
	•	Alpha Vantage API key
	•	Spotify developer credentials (OAuth)

TheSportsDB and Hacker News require no authentication.

Status

Active development. Currently in Week 1 of a six-week build

Two notes before you paste: replace `YOUR_USERNAME` with your actual GitHub username, and the inner code block with the folder tree will need the triple backticks removed and re-added manually if GitHub's editor mangles them on paste. Everything else drops in clean.
