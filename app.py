# Emerald Dashboard - Main Application Entry Point
from dash import Dash
import os

from config import EXTERNAL_SCRIPTS, DEBUG, PORT
from layout import create_layout

# Import callbacks to register them with the app
import callbacks  # noqa: F401

# Load custom index template with inline loader
with open(os.path.join(os.path.dirname(__file__), 'assets', 'index_template.html'), 'r') as f:
    index_string = f.read()

# Create the Dash application
app = Dash(
    __name__,
    external_scripts=EXTERNAL_SCRIPTS,
    use_pages=True,
    pages_folder='pages',
    index_string=index_string,
    suppress_callback_exceptions=True
)

# Set the layout
app.layout = create_layout()

# Run the server
if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
