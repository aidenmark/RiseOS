import os

# This file is the centralized home for the settings for RiseOS

# -----------------------------------------------------------------------------
# Weather - OpenWeather
# -----------------------------------------------------------------------------
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
UNITS = "imperial"
WEATHER_CITY = os.getenv("WEATHER_CITY")
WEATHER_STATE = os.getenv("WEATHER_STATE")

# -----------------------------------------------------------------------------
# Tech Pulse - Hacker News API
# -----------------------------------------------------------------------------
# "top" is what is currently rising on the front page. The alternatives are
# "best", which is high scoring over a longer window, and "new", which is
# unfiltered chronological.
NEWS_STORY_FEED = "top"
NEWS_STORY_COUNT = 3

# -----------------------------------------------------------------------------
# Market Snapshot - Alpha Vantage API
# -----------------------------------------------------------------------------
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
STOCK_TICKERS = ["AAPL", "DIS", "GOOGL", "MAR", "NVDA"]

# -----------------------------------------------------------------------------
# New Music - MusicBrainz API
# -----------------------------------------------------------------------------
MUSIC_GENRES = ["r&b", "reggae", "afrobeats"]
MUSIC_TRACKS_PER_GENRE = 1

# 30 days keeps a release feeling new while still giving most mornings a result.
MUSIC_LOOKBACK_DAYS = 30

# -----------------------------------------------------------------------------
# Sports Events - TheSportsDB API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Wellness - Local Configuration
# -----------------------------------------------------------------------------
DAILY_STEP_GOAL = 10000
DAILY_HYDRATION_GOAL = 64
