def get_adesoes(odoo, models, contratos, ids=None):
    if ids:
        adesoes = models.execute_kw(
            odoo.db, odoo.uid, odoo.password,
            'adesao',
            'search_read',
            [
                [
                    ['contrato', 'in', contratos],
                    ['id', 'in', ids]
                ],

            ],
            {
                'fields': [
                    'id',
                    'name',
                    'plano',
                    'data_ultimo_faturamento',
                    'ativo',
                    'inativacao_contrato',
                    'logradouro',
                    'numero',
                    'bairro',
                    'complemento',
                    'cep',
                    'estado',
                    'cidade',
                    'ponto_referencia',
                    'latitude',
                    'longitude'
                ]
            }
        )
    else:
        adesoes = models.execute_kw(
            odoo.db, odoo.uid, odoo.password,
            'adesao',
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
                    'plano',
                    'data_ultimo_faturamento',
                    'ativo',
                    'inativacao_contrato',
                    'logradouro',
                    'numero',
                    'bairro',
                    'complemento',
                    'cep',
                    'estado',
                    'cidade',
                    'ponto_referencia',
                    'latitude',
                    'longitude'
                ]
            }
        )

    return formatar_adesoes(adesoes)


def formatar_adesoes(adesoes):
    from datetime import datetime

    for adesao in adesoes:
        if adesao['data_ultimo_faturamento']:
            adesao['data_ultimo_faturamento'] = datetime.strptime(adesao['data_ultimo_faturamento'], '%Y-%m-%d')
        else:
            adesao['data_ultimo_faturamento'] = ""

        adesao['logradouro'] = adesao['logradouro'] or '-'
        adesao['numero'] = adesao['numero'] or '-'
        adesao['complemento'] = adesao['complemento'] or '-'
        adesao['bairro'] = adesao['bairro'] or '-'
        adesao['cep'] = adesao['cep'] or '-'
        adesao['ponto_referencia'] = adesao['ponto_referencia'] or '-'
        adesao['latitude'] = adesao['latitude'] or '-'
        adesao['longitude'] = adesao['longitude'] or '-'

    return adesoes