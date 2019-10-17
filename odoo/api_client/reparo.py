ESTAGIOS_EXCLUIDOS=['cancel', 'condenado', 'done', 'devolvido', 'montar_devolver', 'descartado']

def get_reparo(odoo, models, reparo):
    reparo = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair',
        'search_read',
        [
            [
                ['id', '=', reparo],
            ],

        ],
        {
            'fields': ['id', 'name', 'product_id', 'state', 'responsavel', 'partner_id']
        }
    )

    if reparo:
        return formatar_reparos(reparo)[0]
    else:
        return None


def get_reparos(odoo, models, parceiro, estagios_excluidos=ESTAGIOS_EXCLUIDOS):
    reparos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair',
        'search_read',
        [
            [
                ['partner_id', '=', parceiro],
                ['state', 'not in', estagios_excluidos]
            ],

        ],
        {
            'fields': ['id', 'name', 'product_id', 'state', 'responsavel', 'partner_id']
        }
    )

    return formatar_reparos(reparos)


def get_ultimos_reparos(odoo, models, parceiro, estagios_excluidos=ESTAGIOS_EXCLUIDOS):
    reparos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair',
        'search_read',
        [
            [
                ['partner_id', '=', parceiro],
                ['state', 'not in', estagios_excluidos]
            ],
        ],
        {
            'fields': ['id', 'name', 'product_id', 'state', 'responsavel', 'partner_id'],
            'order': 'id desc'
        }
    )

    return formatar_reparos(reparos)


def get_reparos_tecnico(odoo, models, tecnico, estagios_excluidos=ESTAGIOS_EXCLUIDOS):
    reparos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair',
        'search_read',
        [
            [
                ['responsavel', '=', tecnico],
                ['state', 'not in', estagios_excluidos]
            ],
        ],
        {
            'fields': ['id', 'name', 'product_id', 'state', 'responsavel', 'partner_id'],
            'order': 'id desc'
        }
    )

    return formatar_reparos(reparos)


def criar_reparo(odoo, models, parceiro, produto, descricao):
    reparo = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair',
        'create',
        [{
            'product_id': produto,
            'partner_id': parceiro,
            'product_qty': 1.0,
            'product_uom': 1,
            'internal_notes': descricao,
            'invoice_method': 'after_repair',
            'state': 'novo',
            'location_id': 9,
            'location_dest_id': 9,
            'responsavel': 1
        }]
    )

    return reparo or None


def alterar_estagio_reparo(odoo, models, reparo, estagio):
    reparo = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair',
        'write',
        [
            [reparo],
            {
                'state': estagio
            }
        ]
    )

    return reparo or None


def formatar_reparos(reparos):
    return reparos