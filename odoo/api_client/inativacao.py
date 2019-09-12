def get_ultimas_inativacoes(odoo, models, adesoes):
    inativacoes = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'inativacao_contrato',
        'search_read',
        [
            [
                ['adesao', 'in', adesoes]
            ],

        ],
        {
            'limit': 5,
            'fields': ['id', 'name', 'data_inicial', 'dias_inativacao', 'data_final', 'executado', 'finalizado'],
            'order': 'id desc'
        }
    )

    return formatar_inativacoes(inativacoes)


def formatar_inativacoes(inativacoes):
    from datetime import datetime

    for inativacao in inativacoes:
        inativacao['data_inicial'] = datetime.strptime(inativacao['data_inicial'], '%Y-%m-%d')
        inativacao['data_final'] = datetime.strptime(inativacao['data_final'], '%Y-%m-%d')

        inativacao['executado'] = 'Sim' if inativacao['executado'] else 'Não'
        inativacao['finalizado'] = 'Sim' if inativacao['finalizado'] else 'Não'

    return inativacoes