def get_localidade(odoo, models, localidade):
    localidade = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'localidade',
        'search_read',
        [
            [
                ['id', '=', localidade]
            ],
        ],
        {
            'fields': [
                'id',
                'name',
                'contrato'
            ]
        }
    )

    return localidade or None
