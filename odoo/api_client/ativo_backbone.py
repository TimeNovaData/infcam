def get_ativos_backbone(odoo, models, contratos):
    ativos_backbones = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'ativo_backbone',
        'search_read',
        [
            [
                ['contrato', 'in', contratos],
            ],

        ],
        {
            'fields': ['id', 'name']
        }
    )

    return ativos_backbones