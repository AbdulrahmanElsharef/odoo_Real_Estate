{
  'name': 'RealEstate Management ',  # Name displayed in the UI for users (and technical name)
  'version': '17.0.1.0',           # Version of Odoo + version of your app
  'summary': 'Manage RealEstate Properties,Offers,Agents',  # Brief description shown in module info
  'description': 'A comprehensive system to manage real estate properties, offers, and agents.',  # Detailed description shown in module info
  'author': 'Abdulrahman Elsharef',  # Author of the module
  'website': 'https://yourwebsite.com',  # Website link for your module
  'category': 'Real Estate',  # Category for your app in Odoo
  'depends': ['base', 'mail'],  # Dependencies on other Odoo apps or modules
  'data': [  # List of data files associated with your module
    'security/security.xml',  # Security definitions (groups, access rules)
    'security/ir.model.access.csv',  # Additional access control configurations
    'data/property_sequence.xml',  # Data related to property reference sequence
    'data/property_server_actions.xml',  # Data related to property server actions
    'data/property_url_actions.xml',  # Data related to property server actions
    'data/property_automated_actions.xml',  # Data related to property automated actions (Cron Jobs)
    'views/property_views.xml',  # Views for the main property model
    'views/property_extended_views.xml',  # Views for any extended property models
    'views/commercial_property_views.xml',  # Views for the commercial property model
    'views/property_history.xml',  # Views for property history
    'views/property_wizard.xml',  # Views for property wizards (forms)
    'views/offer_views.xml',  # Views for offer models
    'views/agent_views.xml',  # Views for agent models
    'views/tag_views.xml',  # Views for tag models (likely for property tagging)
    'views/real_state_menu.xml',  # Views for the real estate menu
    'reports/property_report.xml',  # Report definitions for properties
    'reports/property_report_template.xml',  # Report templates for properties
  ],
  # 'assets': {  # Uncomment if you have web assets (CSS, JavaScript)
  #   'web.assets_backend': [
  #     'real_estate/static/src/css/property_view.css',  # Example CSS file
  #   ],
  # },
  'installable': True,  # Indicates the module can be installed
  'application': True,  # Indicates this is a full Odoo application
  'license': 'LGPL-3',  # License for your module (LGPL-3 in this case)
  'icon': 'real_state\static\description\icon.png',  # Path to the module icon
}