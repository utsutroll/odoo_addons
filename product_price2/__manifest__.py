# -*- coding: utf-8 -*-
{
    'name': "Product Price 2",

    'summary': """
        Agregar un nuevo campo para precio 2 en el formulario del producto""",

    'description': """
        Agregar un nuevo campo para precio 2 en el formulario del producto
    """,

    'author': "Euclides Ollarves",
    'website': "https://www.instagram.com/Euclides_Ollarves",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml'
    ],

}