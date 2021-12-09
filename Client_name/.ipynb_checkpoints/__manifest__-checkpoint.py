# -*- coding: utf-8 -*-
{
    'name': "Client_name",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "iNBest",
    'website': "inbest.enterprises",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','my_module'],

    # always loaded
    'data': ['static/src/xml/client_name.xml'],
    # only loaded in demonstration mode
    'demo': [],
    'qweb':['static/src/xml/client_name.xml']
}
