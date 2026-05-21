# -*- coding: utf-8 -*-

{
    'name': 'Union Energy Website',
    'summary': 'Union Energy Website',
    'category': 'Union Energy',
    'author': 'BatamTech',
    'sequence': 10,
    'version': '1.1',
    'description': "This module allows to publish the Union Energy website.",
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/faq_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': ['website'],
    'assets': {
        'web.assets_frontend': [
            'union_energy_web/static/src/css/*',
            'union_energy_web/static/src/js/*',
        ],
    },
}
