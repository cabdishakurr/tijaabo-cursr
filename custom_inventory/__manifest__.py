{
    'name': 'Custom Inventory Low Stock',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Shows products with low stock (less than 10 units)',
    'depends': ['stock'],
    'data': [
        'views/product_views.xml',
    ],
    'installable': True,
    'auto_install': False,
} 