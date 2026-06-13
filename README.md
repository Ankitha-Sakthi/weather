# Weather Alert Automation

A Python automation project that fetches live weather data using the OpenWeatherMap API and sends email alerts when the temperature exceeds a defined threshold.

## Features

* Fetches real-time weather data for Kollam
* Checks current temperature automatically
* Sends email alerts using Gmail SMTP
* Uses environment variables for security
* Supports GitHub Actions automation
* Beginner-friendly Python project

## Technologies Used

* Python
* Requests
* OpenWeatherMap API
* SMTP (Gmail)
* GitHub Actions

## Project Structure

```text
weather-alert/
│
├── weather.py
├── requirements.txt
├── README.md
│
└── .github/
    └── workflows/
        └── weather.yml
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create the following secrets:

* API_KEY
* EMAIL
* APP_PASSWORD

## Running Locally

```bash
python weather.py
```

## Author

Ankitha

Built as part of the ZERO2DEV Python Automation Bootcamp.
