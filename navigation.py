# Navigation configuration for different personas
# Icons use Lucide icon names - see https://lucide.dev/icons
# Based on PRD navigation architecture

# =============================================================================
# PERSONA DEFINITIONS
# =============================================================================

PERSONAS = [
    {
        'id': 'persona-grid-operator',
        'key': 'grid_operator',
        'name': 'Grid Operator',
        'description': 'Grid stability & DR management',
        'icon': 'Radio',
        'color': 'bg-red-500',
        'shortcut': '⌘1',
    },
    {
        'id': 'persona-csp-operator',
        'key': 'csp_operator',
        'name': 'CSP Operator',
        'description': 'Tenant flexibility & commitments',
        'icon': 'Building2',
        'color': 'bg-orange-500',
        'shortcut': '⌘2',
    },
    {
        'id': 'persona-compute-user',
        'key': 'compute_user',
        'name': 'Compute User',
        'description': 'AI/ML workloads & jobs',
        'icon': 'Cpu',
        'color': 'bg-green-500',
        'shortcut': '⌘3',
    },
    {
        'id': 'persona-internal',
        'key': 'internal',
        'name': 'Emerald Internal',
        'description': 'Full access & dev tools',
        'icon': 'Shield',
        'color': 'bg-purple-500',
        'shortcut': '⌘4',
    },
]

# Default persona (shown on load)
DEFAULT_PERSONA = PERSONAS[2]  # Compute User

# =============================================================================
# GRID OPERATOR NAVIGATION (GO-*)
# =============================================================================

NAV_GRID_OPERATOR = [
    {
        'title': 'Network',
        'icon': 'LayoutDashboard',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-go-portfolio', 'href': '/portfolio'},
        ]
    },
    {
        'title': 'CSP\'s',
        'icon': 'Building2',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-go-csp-overview', 'href': '/csps/overview'},
            {'title': 'CoreWeave', 'id': 'nav-go-csp-coreweave', 'href': '/csps/coreweave'},
            {'title': 'Applied Digital', 'id': 'nav-go-csp-applied-digital', 'href': '/csps/applied-digital'},
        ]
    },
    {
        'title': 'Events',
        'icon': 'Zap',
        'isActive': True,
        'items': [
            {'title': 'Dispatch', 'id': 'nav-go-dispatch', 'href': '/events/dispatch'},
            {'title': 'Live Monitor', 'id': 'nav-go-live-monitor', 'href': '/events/live'},
            {'title': 'Verification', 'id': 'nav-go-verification', 'href': '/events/verification'},
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'TrendingUp',
        'isActive': True,
        'items': [
            {'title': 'Grid Demand', 'id': 'nav-go-forecast', 'href': '/forecast'},
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {'title': 'General', 'id': 'nav-go-settings-general', 'href': '/settings/general'},
        ]
    },
]

# =============================================================================
# CSP / DC OPERATOR NAVIGATION (CSP-*)
# =============================================================================

NAV_CSP_OPERATOR = [
    {
        'title': 'Capacity',
        'icon': 'LayoutDashboard',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-csp-capacity-overview', 'href': '/capacity/overview'},
        ]
    },
    {
        'title': 'Customers',
        'icon': 'Users',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-csp-customer-overview', 'href': '/customers/overview'},
        ]
    },
    {
        'title': 'Events',
        'icon': 'Zap',
        'isActive': True,
        'items': [
            {'title': 'Timeline', 'id': 'nav-csp-timeline', 'href': '/events/timeline'},
            {'title': 'Orchestrator', 'id': 'nav-csp-orchestrator', 'href': '/events/orchestrator'},
            {'title': 'Intervention', 'id': 'nav-csp-intervention', 'href': '/events/intervention'},
        ]
    },
    {
        'title': 'Simulator',
        'icon': 'FlaskConical',
        'isActive': True,
        'items': [
            {'title': 'Scenarios', 'id': 'nav-csp-simulator', 'href': '/simulator'},
        ]
    },
    {
        'title': 'Settlement',
        'icon': 'Receipt',
        'isActive': True,
        'items': [
            {'title': 'Reports', 'id': 'nav-csp-settlement', 'href': '/settlement'},
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'TrendingUp',
        'isActive': True,
        'items': [
            {'title': 'Grid Demand', 'id': 'nav-csp-forecast', 'href': '/forecast'},
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {'title': 'General', 'id': 'nav-csp-settings-general', 'href': '/settings/general'},
        ]
    },
]

# =============================================================================
# COMPUTE USER NAVIGATION (CU-*)
# =============================================================================

NAV_COMPUTE_USER = [
    {
        'title': 'Flexibility',
        'icon': 'LayoutDashboard',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-cu-flexibility', 'href': '/flexibility'},
        ]
    },
    {
        'title': 'Cluster',
        'icon': 'Server',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-cu-cluster-overview', 'href': '/cluster/overview'},
            {'title': 'Workloads', 'id': 'nav-cu-workloads', 'href': '/cluster/workloads'},
            {'title': 'Metrics', 'id': 'nav-cu-metrics', 'href': '/cluster/metrics'},
        ]
    },
    {
        'title': 'Events',
        'icon': 'Zap',
        'isActive': True,
        'items': [
            {'title': 'Preparedness', 'id': 'nav-cu-preparedness', 'href': '/events/preparedness'},
            {'title': 'Live View', 'id': 'nav-cu-live-view', 'href': '/events/live'},
            {'title': 'Reports', 'id': 'nav-cu-reports', 'href': '/events/reports'},
        ]
    },
    {
        'title': 'Analysis',
        'icon': 'LineChart',
        'isActive': True,
        'items': [
            {'title': 'DR Events', 'id': 'nav-cu-analysis', 'href': '/analysis'},
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'TrendingUp',
        'isActive': True,
        'items': [
            {'title': 'Grid Demand', 'id': 'nav-cu-forecast', 'href': '/forecast'},
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {'title': 'General', 'id': 'nav-cu-settings-general', 'href': '/settings/general'},
        ]
    },
]

# =============================================================================
# EMERALD INTERNAL NAVIGATION
# =============================================================================

NAV_INTERNAL = [
    {
        'title': 'Shared Tools',
        'icon': 'Wrench',
        'isActive': True,
        'items': [
            {'title': 'Analysis', 'id': 'nav-int-analysis', 'href': '/analysis'},
            {'title': 'Forecast', 'id': 'nav-int-forecast', 'href': '/forecast'},
            {'title': 'Event Config', 'id': 'nav-int-event-config', 'href': '/tools/event-config'},
        ]
    },
    {
        'title': 'Development',
        'icon': 'Code',
        'isActive': True,
        'items': [
            {'title': 'System Health', 'id': 'nav-int-system-health', 'href': '/dev/health'},
            {'title': 'Raw Metrics', 'id': 'nav-int-raw-metrics', 'href': '/dev/metrics'},
            {'title': 'API Status', 'id': 'nav-int-api-status', 'href': '/dev/api'},
            {'title': 'Logs', 'id': 'nav-int-logs', 'href': '/dev/logs'},
        ]
    },
    {
        'title': 'Documentation',
        'icon': 'BookOpen',
        'isActive': True,
        'items': [
            {'title': 'Introduction', 'id': 'nav-int-docs-intro', 'href': '/docs/intro'},
            {'title': 'Get Started', 'id': 'nav-int-docs-getstarted', 'href': '/docs/get-started'},
            {'title': 'Tutorials', 'id': 'nav-int-docs-tutorials', 'href': '/docs/tutorials'},
            {'title': 'Changelog', 'id': 'nav-int-docs-changelog', 'href': '/docs/changelog'},
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {'title': 'General', 'id': 'nav-int-settings-general', 'href': '/settings/general'},
            {'title': 'Team', 'id': 'nav-int-settings-team', 'href': '/settings/team'},
            {'title': 'Billing', 'id': 'nav-int-settings-billing', 'href': '/settings/billing'},
            {'title': 'Limits', 'id': 'nav-int-settings-limits', 'href': '/settings/limits'},
        ]
    },
]

# =============================================================================
# NAVIGATION LOOKUP
# =============================================================================

# Map persona keys to their navigation config
PERSONA_NAVIGATION = {
    'grid_operator': NAV_GRID_OPERATOR,
    'csp_operator': NAV_CSP_OPERATOR,
    'compute_user': NAV_COMPUTE_USER,
    'internal': NAV_INTERNAL,
}


def get_navigation_for_persona(persona_key: str) -> list:
    """Get the navigation config for a given persona key."""
    return PERSONA_NAVIGATION.get(persona_key, NAV_COMPUTE_USER)


# Legacy - for backwards compatibility during transition
NAV_MAIN = NAV_COMPUTE_USER
