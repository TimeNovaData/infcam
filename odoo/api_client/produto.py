def get_produto(odoo, models, produto):
    produtos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'product.product',
        'search_read',
        [
            [
                ['id', '=', produto],
            ],

        ],
        {
            'fields': ['id', 'name', 'list_price', 'uom_id']
        }
    )

    if produtos:
        return produtos[0]
    else:
        return None

def get_produtos(odoo, models, tipo=['service', 'product', 'consu']):
    produtos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'product.product',
        'search_read',
        [
            [
                ['type', 'in', tipo],
            ],

        ],
        {
            'fields': ['id', 'name'],
            'order': 'name asc'
        },
    )

    return produtos