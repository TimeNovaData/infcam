def get_conexao_cliente(odoo, models, adesao):
    conexao_cliente = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'conexao_cliente',
        'search_read',
        [
            [
                ['adesao', '=', adesao]
            ],

        ],
        {
            'fields': [
                'id',
                'login',
                'senha'
            ]
        }
    )

    return conexao_cliente
