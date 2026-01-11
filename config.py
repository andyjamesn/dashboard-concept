# Application configuration

# Set to False for production (uses pre-built CSS only)
DEBUG = True

# In dev mode, add Tailwind CDN for instant class updates without rebuilding
# In production, only the pre-built CSS from emerald_ui_components is used
EXTERNAL_SCRIPTS = (
    ["https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"] if DEBUG else []
)

# Server settings
PORT = 8052
