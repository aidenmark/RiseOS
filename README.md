# RiseOS

RiseOS is a modular, Python-based personal morning operating system. It collects information from configured external data sources, monitors and logs system events, exposes briefing data through a Representational State Transfer (REST) Application Programming Interface (API), and generates a formatted daily morning brief on an automated schedule.

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
- Secure configuration management

---

## System Overview

RiseOS contains four primary systems:

- **Event Monitor**: tracks selected system activity such as central processing unit (CPU) usage, memory usage, and disk thresholds
- **Event Logger**: writes system and application events to a SQLite database with a timestamp, source, event type, severity, and description
- **REST API Layer**: a Flask application that exposes briefing and event data through queryable endpoints
- **Daily Briefing Generator**: aggregates enabled data sources and the overnight event log into a formatted morning brief

File-system monitoring is deferred until useful monitoring boundaries and privacy rules are defined.

---

## Morning Brief

The initial RiseOS morning brief is planned to include:

| Section | Source | Status |
|---|---|---|
| Date and daily intention | Local configuration | In development |
| Weather | OpenWeatherMap API | In development |
| Tech Pulse | Hacker News API | Planned |
| Market Snapshot | Alpha Vantage API | In development |
| Music | MusicBrainz API | Planned |
| Sports events | TheSportsDB API | Planned |
| Wellness goals | Local configuration | In development |
| Overnight event summary | SQLite event log | Planned |

The planned Music section will use user-selected genres to discover recent releases without requiring a music-streaming account.

Users will eventually be able to enable, disable, and configure briefing sections according to their preferences.

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| API Layer | Flask |
| Database | SQLite |
| Scheduling | APScheduler |
| Hypertext Transfer Protocol (HTTP) client | Requests |
| Testing | Pytest |
| Version control | Git and GitHub |

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

The structure may evolve as implementation validates the application’s internal boundaries.

---

## Planned API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/brief` | Returns the complete morning brief as JavaScript Object Notation (JSON) |
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

RiseOS reads credentials and user-specific configuration values from environment variables.

The current configuration expects these environment variables when their corresponding integrations are enabled:

```text
OPENWEATHER_API_KEY
WEATHER_CITY
WEATHER_STATE
ALPHA_VANTAGE_API_KEY
```

For local development, set the variables in the active shell before running RiseOS. Do not place real API credentials in `config.py`, commit them to Git, or include them in public examples.

Hacker News, MusicBrainz, and TheSportsDB do not currently require user authentication for the planned integrations.

Support for loading a local `.env` file has not yet been implemented.

---

## Development Status

RiseOS is under active development and is working toward Version 1.0.0.

### Completed

- GitHub repository created
- Initial project documentation created
- Project folder structure scaffolded
- Python virtual environment configured
- Initial dependencies installed
- `requirements.txt` generated
- Initial configuration values added
- Initial API-key loading from environment variables added
- MusicBrainz selected as the planned music metadata provider

### In Progress

- Completing the application configuration
- Defining configuration validation behavior
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
