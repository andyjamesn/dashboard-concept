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
            {
                'title': 'Overview',
                'id': 'nav-go-portfolio',
                'href': '/portfolio',
                'description': 'Aggregate CSP flexibility and season status'
            },
        ]
    },
    {
        'title': 'CSP\'s',
        'icon': 'Building2',
        'isActive': True,
        'items': [
            {
                'title': 'Overview',
                'id': 'nav-go-csp-overview',
                'href': '/csps/overview',
                'description': 'List of contracted CSPs with performance metrics'
            },
            {
                'title': 'CoreWeave',
                'id': 'nav-go-csp-coreweave',
                'href': '/csps/coreweave',
                'description': 'CoreWeave facility power visualisation'
            },
            {
                'title': 'Applied Digital',
                'id': 'nav-go-csp-applied-digital',
                'href': '/csps/applied-digital',
                'description': 'Applied Digital facility power visualisation'
            },
        ]
    },
    {
        'title': 'Events',
        'icon': 'Zap',
        'isActive': True,
        'items': [
            {
                'title': 'Dispatch',
                'id': 'nav-go-dispatch',
                'href': '/events/dispatch',
                'description': 'Event configuration and dispatch console'
            },
            {
                'title': 'Live Monitor',
                'id': 'nav-go-live-monitor',
                'href': '/events/live',
                'description': 'Real-time view during active DR events'
            },
            {
                'title': 'Verification',
                'id': 'nav-go-verification',
                'href': '/events/verification',
                'description': 'Post-event M&V and settlement'
            },
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'TrendingUp',
        'isActive': True,
        'items': [
            {
                'title': 'Grid Demand',
                'id': 'nav-go-forecast',
                'href': '/forecast',
                'description': 'Grid demand forecasting'
            },
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {
                'title': 'General',
                'id': 'nav-go-settings-general',
                'href': '/settings/general',
                'description': 'General application settings'
            },
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
            {
                'title': 'Overview',
                'id': 'nav-csp-capacity-overview',
                'href': '/capacity/overview',
                'description': 'Grid obligations vs customer flexibility'
            },
        ]
    },
    {
        'title': 'Customers',
        'icon': 'Users',
        'isActive': True,
        'items': [
            {
                'title': 'Overview',
                'id': 'nav-csp-customer-overview',
                'href': '/customers/overview',
                'description': 'All flex-tier customers with compliance status'
            },
        ]
    },
    {
        'title': 'Events',
        'icon': 'Zap',
        'isActive': True,
        'items': [
            {
                'title': 'Timeline',
                'id': 'nav-csp-timeline',
                'href': '/events/timeline',
                'description': 'Upcoming, active, and past DR events'
            },
            {
                'title': 'Orchestrator',
                'id': 'nav-csp-orchestrator',
                'href': '/events/orchestrator',
                'description': 'Planned and executed orchestration actions'
            },
            {
                'title': 'Intervention',
                'id': 'nav-csp-intervention',
                'href': '/events/intervention',
                'description': 'Controls for non-compliant customers'
            },
        ]
    },
    {
        'title': 'Simulator',
        'icon': 'FlaskConical',
        'isActive': True,
        'items': [
            {
                'title': 'Scenarios',
                'id': 'nav-csp-simulator',
                'href': '/simulator',
                'description': 'Test curtailment scenarios'
            },
        ]
    },
    {
        'title': 'Settlement',
        'icon': 'Receipt',
        'isActive': True,
        'items': [
            {
                'title': 'Reports',
                'id': 'nav-csp-settlement',
                'href': '/settlement',
                'description': 'Post-event financial reconciliation'
            },
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'TrendingUp',
        'isActive': True,
        'items': [
            {
                'title': 'Grid Demand',
                'id': 'nav-csp-forecast',
                'href': '/forecast',
                'description': 'Grid demand forecasting'
            },
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {
                'title': 'General',
                'id': 'nav-csp-settings-general',
                'href': '/settings/general',
                'description': 'General application settings'
            },
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
            {
                'title': 'Overview',
                'id': 'nav-cu-flexibility',
                'href': '/flexibility',
                'description': 'Flexibility posture and commitment status'
            },
        ]
    },
    {
        'title': 'Cluster',
        'icon': 'Server',
        'isActive': True,
        'items': [
            {
                'title': 'Overview',
                'id': 'nav-cu-cluster-overview',
                'href': '/cluster/overview',
                'description': 'Real-time cluster monitoring and job stats'
            },
            {
                'title': 'Workloads',
                'id': 'nav-cu-workloads',
                'href': '/cluster/workloads',
                'description': 'Workload inventory and classification'
            },
            {
                'title': 'Metrics',
                'id': 'nav-cu-metrics',
                'href': '/cluster/metrics',
                'description': 'Per-job training and system metrics'
            },
        ]
    },
    {
        'title': 'Events',
        'icon': 'Zap',
        'isActive': True,
        'items': [
            {
                'title': 'Preparedness',
                'id': 'nav-cu-preparedness',
                'href': '/events/preparedness',
                'description': 'Upcoming event impact forecasting'
            },
            {
                'title': 'Live View',
                'id': 'nav-cu-live-view',
                'href': '/events/live',
                'description': 'Real-time monitoring during DR events'
            },
            {
                'title': 'Reports',
                'id': 'nav-cu-reports',
                'href': '/events/reports',
                'description': 'Post-event compliance evidence'
            },
        ]
    },
    {
        'title': 'Analysis',
        'icon': 'LineChart',
        'isActive': True,
        'items': [
            {
                'title': 'DR Events',
                'id': 'nav-cu-analysis',
                'href': '/analysis',
                'description': 'Historical DR event analysis'
            },
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'TrendingUp',
        'isActive': True,
        'items': [
            {
                'title': 'Grid Demand',
                'id': 'nav-cu-forecast',
                'href': '/forecast',
                'description': 'Grid demand forecasting'
            },
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {
                'title': 'General',
                'id': 'nav-cu-settings-general',
                'href': '/settings/general',
                'description': 'General application settings'
            },
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
            {
                'title': 'Analysis',
                'id': 'nav-int-analysis',
                'href': '/analysis',
                'description': 'Historical DR event analysis'
            },
            {
                'title': 'Forecast',
                'id': 'nav-int-forecast',
                'href': '/forecast',
                'description': 'Grid demand forecasting'
            },
            {
                'title': 'Event Config',
                'id': 'nav-int-event-config',
                'href': '/tools/event-config',
                'description': 'Configure DR event shapes for demos'
            },
        ]
    },
    {
        'title': 'Development',
        'icon': 'Code',
        'isActive': True,
        'items': [
            {
                'title': 'System Health',
                'id': 'nav-int-system-health',
                'href': '/dev/health',
                'description': 'System health monitoring'
            },
            {
                'title': 'Raw Metrics',
                'id': 'nav-int-raw-metrics',
                'href': '/dev/metrics',
                'description': 'Raw metrics dashboard'
            },
            {
                'title': 'API Status',
                'id': 'nav-int-api-status',
                'href': '/dev/api',
                'description': 'API status monitoring'
            },
            {
                'title': 'Logs',
                'id': 'nav-int-logs',
                'href': '/dev/logs',
                'description': 'System logs viewer'
            },
        ]
    },
    {
        'title': 'Documentation',
        'icon': 'BookOpen',
        'isActive': True,
        'items': [
            {
                'title': 'Introduction',
                'id': 'nav-int-docs-intro',
                'href': '/docs/intro',
                'description': 'Introduction to Emerald Dashboard'
            },
            {
                'title': 'Get Started',
                'id': 'nav-int-docs-getstarted',
                'href': '/docs/get-started',
                'description': 'Getting started guide'
            },
            {
                'title': 'Tutorials',
                'id': 'nav-int-docs-tutorials',
                'href': '/docs/tutorials',
                'description': 'Step-by-step tutorials'
            },
            {
                'title': 'Changelog',
                'id': 'nav-int-docs-changelog',
                'href': '/docs/changelog',
                'description': 'Release notes and updates'
            },
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'isActive': True,
        'items': [
            {
                'title': 'General',
                'id': 'nav-int-settings-general',
                'href': '/settings/general',
                'description': 'General application settings'
            },
            {
                'title': 'Team',
                'id': 'nav-int-settings-team',
                'href': '/settings/team',
                'description': 'Team management'
            }
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


def get_page_info(href: str) -> dict:
    """Get page info (title, description, icon) for a given href."""
    for nav in PERSONA_NAVIGATION.values():
        for section in nav:
            for item in section.get('items', []):
                if item.get('href') == href:
                    return {
                        'title': item['title'],
                        'description': item.get('description', ''),
                        'section': section['title'],
                        'icon': section.get('icon', 'File')
                    }
    return None


# Legacy - for backwards compatibility during transition
NAV_MAIN = NAV_COMPUTE_USER
