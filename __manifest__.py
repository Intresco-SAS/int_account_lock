# -*- coding: utf-8 -*-
{
    'name': "int_account_lock",

    'summary': """
        Extension for account lock module to add a new user group to the fiscal lock date.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Intresco SAS",
    'website': "https://www.intresco.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/res_groups.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
