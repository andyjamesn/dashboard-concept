# Navigation configuration for different personas
# Icons use Lucide icon names - see https://lucide.dev/icons

# Current placeholder navigation (will be replaced with persona-specific nav)
NAV_MAIN = [
    {
        'title': 'Cluster',
        'icon': 'Server',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-overview', 'href': '/cluster/overview'},
            {'title': 'Starred', 'id': 'nav-starred'},
            {'title': 'Settings', 'id': 'nav-settings'},
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'CloudLightning',
        'isActive': True,
        'items': [
            {'title': 'Genesis', 'id': 'nav-genesis'},
            {'title': 'Explorer', 'id': 'nav-explorer'},
            {'title': 'Quantum', 'id': 'nav-quantum'},
        ]
    },
    {
        'title': 'Documentation',
        'icon': 'BookOpen',
        'items': [
            {'title': 'Introduction', 'id': 'nav-intro'},
            {'title': 'Get Started', 'id': 'nav-getstarted'},
            {'title': 'Tutorials', 'id': 'nav-tutorials'},
            {'title': 'Changelog', 'id': 'nav-changelog'},
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'items': [
            {'title': 'General', 'id': 'nav-general', 'href': '/settings/general'},
            {'title': 'Team', 'id': 'nav-team'},
            {'title': 'Billing', 'id': 'nav-billing'},
            {'title': 'Limits', 'id': 'nav-limits'},
        ]
    },
]

# Projects shown in sidebar
PROJECTS = [
    {'name': 'Design Engineering', 'icon': 'Frame', 'id': 'proj-design'},
    {'name': 'Sales & Marketing', 'icon': 'PieChart', 'id': 'proj-sales'},
]

# Persona definitions for the persona switcher
# Colors match PRD: Grid Operator (red), CSP (orange), Compute User (green), Internal (purple)
PERSONAS = [
    {
        'id': 'persona-grid-operator',
        'name': 'Grid Operator',
        'description': 'Grid stability & DR management',
        'icon': 'Radio',
        'color': 'bg-red-500',
        'shortcut': '⌘1',
    },
    {
        'id': 'persona-csp-operator',
        'name': 'CSP Operator',
        'description': 'Tenant flexibility & commitments',
        'icon': 'Building2',
        'color': 'bg-orange-500',
        'shortcut': '⌘2',
    },
    {
        'id': 'persona-compute-user',
        'name': 'Compute User',
        'description': 'AI/ML workloads & jobs',
        'icon': 'Cpu',
        'color': 'bg-green-500',
        'shortcut': '⌘3',
    },
    {
        'id': 'persona-internal',
        'name': 'Emerald Internal',
        'description': 'Full access & dev tools',
        'icon': 'Shield',
        'color': 'bg-purple-500',
        'shortcut': '⌘4',
    },
]

# Default persona (shown on load)
DEFAULT_PERSONA = PERSONAS[2]  # Compute User
