# -*- coding: utf-8 -*-
{
    'name': "smart_margin",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets':{'web.assets_backend':[
        'smart_margin/static/src/js/smart_margin.js',
        'smart_margin/static/src/js/margin_popup.js',
        'smart_margin/static/src/xml/smart_margin.xml',
        'smart_margin/static/src/xml/margin_pop.xml',
    ]}
}

