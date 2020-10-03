# -*- coding: utf-8 -*-
{
    'name': "odoo_boilerplate",

    'summary': """
        TL Templates's Odoo Module Boilerplate
    """,

    'description': """
        Odoo plugin boilerplate with some features
    """,
    'author': "Tl Templates",
    'website': "https://tltemplates.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base', 'product', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views_res_config_settings.xml',
        'views/views_sequence.xml',
        'views/views_product_resource.xml',
        'views/views_inherit.xml',
        'views/views_menu.xml',
        'views/views_wizard.xml',
        'views/report_product_resource.xml',
    ],
    "auto_install": False,
    "installable": True,
}
