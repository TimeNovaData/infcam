def get_contratos(odoo, models, parceiro, status=['open', 'pending'], ids=None, tipo_contrato=[1, 2, 3, 4]):
    if ids:
        contratos = models.execute_kw(
            odoo.db, odoo.uid, odoo.password,
            'account.analytic.account',
            'search_read',
            [
                [
                    ['partner_id', '=', parceiro],
                    ['tipo_contrato', 'in', tipo_contrato],
                    ['state', 'in', status],
                    ['id', 'in', ids]
                ],

            ],
            {
                'fields': [
                    'id',
                    'name',
                    'tipo_contrato',
                    'condicao_pagamento',
                    'adesao',
                    'atendimento',
                    'fatura',
                    'state'
                ]
            }
        )
    else:
        contratos = models.execute_kw(
            odoo.db, odoo.uid, odoo.password,
            'account.analytic.account',
            'search_read',
            [
                [
                    ['partner_id', '=', parceiro],
                    ['tipo_contrato', 'in', tipo_contrato],
                    ['state', 'in', status]
                ],

            ],
            {
                'fields': [
                    'id',
                    'name',
                    'tipo_contrato',
                    'condicao_pagamento',
                    'adesao',
                    'atendimento',
                    'fatura',
                    'state'
                ]
            }
        )

    return formatar_contratos(odoo, models, contratos)


def get_id_contratos(odoo, models, parceiro, tipo_contrato=[1, 2, 3, 4]):
    contratos = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'account.analytic.account',
        'search',
        [
            [
                ['partner_id', '=', parceiro],
                ['tipo_contrato', 'in', tipo_contrato],
                ['state', 'in', ['open', 'pending']]
            ],

        ]
    )

    return contratos


def formatar_contratos(odoo, models, contratos):
    for contrato in contratos:
        contrato['condicao_pagamento'] = contrato['condicao_pagamento'][1].split()[2]
        contrato['fatura'] = [fatura for fatura in contrato['fatura'] if fatura_is_open(odoo, models, fatura)]

        if contrato['state'] == 'open':
            contrato['state'] = 'Aberto'
        elif contrato['state'] == 'pending':
            contrato['state'] = 'A Renovar'

    return contratos


def fatura_is_open(odoo, models, id_fatura):
    fatura = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'account.invoice',
        'read',
        [id_fatura],
        {
            'fields': ['id', 'state']
        }
    )

    return fatura['state'] == 'open'
