# -*- coding: utf-8 -*-
{
    'name': "Recibo cliente/proveedor modificado",

    'summary': """
        Se agregar una tabla con las facturas relacionadas en los recibos de pago
        y una tabla con los detalles de cheques(en caso de tener el módulo account_check)""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Brenda - Exemax",
    'website': "http://www.exemax.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/account_payment_group_custom.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}