# -*- coding: utf-8 -*-
{
    'name': "PayRoll",

    'summary': "This module will compute base on attendance system of employee",

    'description': """
Long description of module's purpose
    """,

    'author': "Aung Min Soe",
    'website': "https://www.sunacademy.com",
    'category': 'Application',
    'version': '17.0.0.1',
    'depends': ['base','mail','hr'],

    'data': [
        'security/ir.model.access.csv',
        'views/payroll_menu.xml',
        'views/salary_period_menu_view.xml',
        
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}

