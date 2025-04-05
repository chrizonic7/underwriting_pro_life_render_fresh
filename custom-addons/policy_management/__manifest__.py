{
    'name': 'Policy Management',
    'version': '1.0',
    'summary': 'Life and Group Insurance Policy Management',
    'category': 'Insurance',
    'author': 'ERPBridge Technologies',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/policy_views.xml',
        'data/admin_user.xml',
        'data/features_description.xml',
        'data/sample_financial_data.xml',
        'views/finance_dashboard.xml',
    ],
    'installable': True,
    'application': True,
}