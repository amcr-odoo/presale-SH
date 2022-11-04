# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Presale",
    'version': '15.0.1.0.0',
    'author': 'Odoo PS',
    'summary': 'Presale application',
    'description':"""
         Presale order on a product
    """,
    'category': 'Customization',
    'depends': [
        'product',
    ],
    'data': [
        'security/presale_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/mail_template.xml',
        'data/ir_cron.xml',
        'views/presale_order_line_views.xml',
        'views/presale_order_views.xml',
        'views/presale_menus.xml'
    ],
    'application': True,
    'license': 'LGPL-3',
}
