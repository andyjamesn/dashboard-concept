# Emerald Dashboard - Main Application Entry Point
from dash import Dash

from config import EXTERNAL_SCRIPTS, DEBUG, PORT
from layout import create_layout

# Import callbacks to register them with the app
import callbacks  # noqa: F401

# Create the Dash application
app = Dash(
    __name__,
    external_scripts=EXTERNAL_SCRIPTS,
    use_pages=True,
    pages_folder='pages'
)

# Set the layout
app.layout = create_layout()

# Run the server
if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
