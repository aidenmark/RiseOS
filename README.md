# RiseOS

RiseOS is a modular, Python-based personal morning operating system. It collects information from configured external data sources, monitors and logs system events, exposes briefing data through a REST API, and generates a formatted daily morning brief on an automated schedule.

The project is designed so that new data sources and personal modules can be added without restructuring the existing application.

---

## Project Goals

RiseOS is being developed as both a functional personal productivity tool and a software engineering portfolio project.

The project demonstrates:

- REST API development
- Third-party API integration
- Modular application architecture
- Structured event logging
- SQLite data persistence
- Automated task scheduling
- Error handling
- Automated testing

---

## System Overview

RiseOS contains four primary systems:

- **Event Monitor**: tracks system activity such as CPU usage, memory usage, disk thresholds, and file-system changes
- **Event Logger**: writes system and application events to a SQLite database with a timestamp, source, event type, severity, and description
- **REST API Layer**: a Flask application that exposes briefing and event data through queryable endpoints
- **Daily Briefing Generator**: aggregates enabled data sources and the overnight event log into a formatted morning brief

---

## Morning Brief

The initial RiseOS morning brief is planned to include:

| Section | Source | Status |
|---|---|---|
| Date and daily intention | Local configuration | In development |
| Weather | OpenWeatherMap API | In development |
| Tech news | Hacker News API | Planned |
| Stocks | Alpha Vantage API | In development |
| Wellness goals | Local configuration | In development |
| Overnight event summary | SQLite event log | Planned |
| Sports events | TheSportsDB API | Planned |
| New music releases | Music provider API | Deferred |

Users will eventually be able to enable, disable, and configure modules according to their own preferences.

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| API Layer | Flask |
| Database | SQLite |
| Scheduling | APScheduler |
| HTTP Client | Requests |
| Testing | Pytest |
| Version Control | Git and GitHub |

---

## Project Structure

```text
riseos/
  main.py
  config.py
  database/
    db.py
  monitors/
    weather.py
    news.py
    stocks.py
    music.py
    sports.py
    system.py
  logger/
    event_logger.py
  api/
    routes.py
  briefing/
    generator.py
  scheduler/
    jobs.py
  tests/
    test_monitors.py
```

The structure may evolve as the application grows.

---

## Planned API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/brief` | Returns the complete morning brief as JSON |
| GET | `/events` | Returns logged events |
| GET | `/events?severity=high` | Filters events by severity |
| GET | `/summary` | Returns aggregated event statistics |
| POST | `/events` | Creates a manual event for testing |

These endpoints are planned and may change during development.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aidenmark/riseos.git
cd riseos
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

RiseOS uses environment variables for credentials and sensitive configuration values.

Create a local `.env` file based on the provided `.env.example` file:

```bash
cp .env.example .env
```

Add the required API credentials to `.env`:

```text
OPENWEATHER_API_KEY=
ALPHA_VANTAGE_API_KEY=
```

Do not commit the `.env` file or any API credentials to version control.

Hacker News and TheSportsDB do not currently require authentication for the planned integrations.

Music integration is deferred until a provider is selected.

---

## Development Status

RiseOS is under active development.

### Completed

- GitHub repository created
- Initial README created
- Project folder structure scaffolded
- Python virtual environment configured
- Initial dependencies installed
- `requirements.txt` generated
- Initial configuration values added

### In Progress

- Completing application configuration
- Adding secure environment-variable handling
- Building the SQLite database layer
- Building the structured event logger

### Planned

- System monitoring
- External API integrations
- Morning briefing generation
- Flask REST API endpoints
- Automated scheduling
- Pytest coverage
- Continuous integration
- Additional configurable modules
