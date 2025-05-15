{
    'name': 'Audit Trail',
    'version': '1.0.0',
    'summary': 'Tracks changes in records',
    'description': """
        This module provides an audit trail for tracking changes in records.
    """,
    'author': 'Murshid',
    'website': 'https://www.yourwebsite.com',
    'category': 'Specific Category',
    'license': 'LGPL-3',
    'depends': [
        'base', 'custom_leads','logic_payments_17', 'logic_base_17','refund_17', 'seminar_17','reports','fee_collection_17','hr' # List of module dependencies

        # Add other module dependencies here
    ],
    'data': [
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'views/audit_trail.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
