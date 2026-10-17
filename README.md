# Playwright Python Framework

A lightweight Playwright + pytest automation framework scaffold for browser-based testing.

## Features

- Playwright browser automation
- pytest-based test runner
- Page Object Model structure
- Smoke test example against Example Domain

## Prerequisites

- Python 3.9+
- A browser engine installed via Playwright

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run tests

```bash
pytest
```

## Project structure

```text
.
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── home_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_example.py
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
└──
```
