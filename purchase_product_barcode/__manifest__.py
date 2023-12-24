# -*- coding: utf-8 -*-
{
    'name': "Purchase Product Barcode",

    'summary': """
        This module will help you to use product barcode and barcode scanner in purchase module.
    """,

    'description': """
        This module will help you to use product barcode and barcode scanner in purchase module.
    """,

    'author': "Agung Sepruloh",
    'website': "https://github.com/agungsepruloh",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'base_product_barcode'],

    # always loaded
    'data': [
        'views/purchase_order_line.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'images': ['static/description/banner.png'],
    'application': True,
}
