# -*- coding: utf-8 -*-

{
    'name': 'POS Report Sale Person',
    'category': 'sale',
    'version': '0.1',
    'summary': 'This module provides POS Report Sale Person',
    'author': 'anonym',
    'description': '''This module provides Extra Report(Receivable & Payable report and PoS report).''',
    'depends': [
        'base', 
        'sale', 
        'account', 
        'pos_cashback', 
        'point_of_sale'
        ],
    'data': [
        'views/pos_view.xml',
        'report/pos_temp.xml',
        'report/pos_report.xml',
        # 'views/menu.xml',
        # 'views/qaqc_coa.xml',
    ],
    'qweb': [
        # 'static/src/xml/cashback_templates.xml',
    ],
    'demo': [
        # 'demo/sale_agent_demo.xml',
    ],
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'installable': True,
    'application': False,
}
