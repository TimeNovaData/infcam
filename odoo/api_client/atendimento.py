def get_atendimentos(odoo, models, contratos):
    atendimentos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'atendimento',
        'search_read',
        [
            [
                ['contrato', 'in', contratos]
            ],

        ],
        {
            'fields': [
                'id',
                'name',
                'reclamacao',
                'manifestacao_atendimento',
                'grupo_atendimento',
                'tipo_atendimento',
                'status_atendimento',
                'create_date'
            ],
            'order': 'id desc'
        }
    )

    return formatar_atendimentos(atendimentos)


def get_ultimos_atendimentos(odoo, models, contratos):
    atendimentos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'atendimento',
        'search_read',
        [
            [
                ['contrato', 'in', contratos]
            ],

        ],
        {
            'limit': 5,
            'fields': [
                'id',
                'name',
                'manifestacao_atendimento',
                'grupo_atendimento',
                'tipo_atendimento',
                'status_atendimento',
                'create_date'
            ],
            'order': 'id desc'
        }
    )

    return formatar_atendimentos(atendimentos)


def formatar_atendimentos(atendimentos):
    from datetime import datetime

    for atendimento in atendimentos:
        atendimento['create_date'] = datetime.strptime(atendimento['create_date'], '%Y-%m-%d %H:%M:%S')

    return atendimentos