# Emerald Dashboard Concept

A demo/concept dashboard application built with [Plotly Dash](https://dash.plotly.com/) and [Emerald UI Components](https://github.com/ai-emerald/emerald-ui-components).

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Run

```bash
python app.py
# Visit http://127.0.0.1:8050
```

## Project Structure

```
dashboard-concept/
├── app.py              # Main Dash application
├── pages/              # Multi-page routes
│   ├── overview.py
│   └── settings.py
├── assets/             # Static assets (images, favicon)
└── requirements.txt    # Python dependencies
```

## Updating Emerald UI Components

To get the latest version of the component library:

```bash
pip install --upgrade git+https://github.com/ai-emerald/emerald-ui-components.git
```
