{
    'name': 'RealEstate Management ', # name in ui app for user AND (real_state) TECHNICAL NAME IS THE APP NAME
    'version': '17.0.1.0',# version of odoo + version of app
    'summary': 'Manage RealEstate Properties,Offers,Agents', # show in module info
    'description': 'A comprehensive system to manage real estate properties, offers, and agents.', # show in module info
    'author': 'Abdulrahman Elsharef', # who create this module
    'website': 'https://yourwebsite.com', # site link for this module
    'category': 'Real Estate', # category of this app
    'depends': ['base', 'mail'], # other app or module that my app depends when i install my app
    'data': [ #  data file like (security , views , reports , wizards)
        'security/security.xml', #for gruop and categouty defind and access
        'security/ir.model.access.csv',
        'data/property_sequence.xml',
        'data/property_server_actions.xml',
        'data/property_automated_actions.xml',
        #SHOW SEQUENS AND automated and server actions
        'views/property_views.xml',
        'views/property_extended_views.xml',
        'views/commercial_property_views.xml',
        'views/property_history.xml',
        'views/property_wizard.xml',
        'views/offer_views.xml',
        'views/agent_views.xml',
        'views/tag_views.xml',
        'views/real_state_menu.xml',
        'reports/property_report.xml',
        'reports/property_report_template.xml',

    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'real_estate/static/src/css/property_view.css',
    #     ],
    # },
    'installable': True, # can install
    'application': True, # kind  of module
    'license': 'LGPL-3', # odoo license for this app 
    'icon': 'real_state\static\description\icon.png',  # Add this line for icon

}