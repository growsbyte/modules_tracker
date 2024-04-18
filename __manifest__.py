# -*- coding: utf-8 -*-
{
    'name': "Modules Trackers",
    'summary': """
        ModulesTracker is your essential Odoo module for tracking and store development modules """,
    'description': """
        ModulesTracker is your essential Odoo module for tracking and store development modules and optimizing workflows. 
        Monitor activity, analyze performance, and generate insightful reports to streamline your projects effortlessly.
    """,
    'author': "GrowsByte",
    'company': "GrowsByte",
    'website': "https://www.growsbyte.com/",
    'license': 'OPL-1',
    'category': 'Tools',
    'version': '1.1',
    'depends': ['base', 'hr'],
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'data/odoo_versions.xml',
        'views/views.xml',
        'views/odoo_versions.xml',
        'views/reporting.xml',
        'views/configuration.xml',
        'views/modules_dependents.xml',
        'views/python_packages_dependents.xml',
        'views/statistics.xml',
        'views/menues.xml',
    ],
    'css': ['static/src/css/custom.css'],
}
