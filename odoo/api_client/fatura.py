def get_fatura(odoo, models, fatura):
    fatura = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'account.invoice',
        'search_read',
        [
            [
                ['id', '=', fatura],
            ],

        ],
        {
            'fields': ['id', 'period_id', 'date_due', 'amount_total', 'state', 'status_banco', 'partner_id']
        }
    )

    if fatura:
        return formatar_faturas(fatura)[0]
    else:
        return None


def get_faturas(odoo, models, contratos, situacao=['open', 'paid']):
    faturas = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'account.invoice',
        'search_read',
        [
            [
                ['contrato', 'in', contratos],
                ['state', 'in', situacao]
            ],

        ],
        {
            'fields': ['id', 'period_id', 'date_due', 'amount_total', 'state', 'status_banco', 'partner_id']
        }
    )

    return formatar_faturas(faturas)


def get_ultimas_faturas(odoo, models, contratos):
    faturas = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'account.invoice',
        'search_read',
        [
            [
                ['contrato', 'in', contratos],
                ['state', 'in', ['open', 'paid']]
            ],

        ],
        {
            'limit': 5,
            'fields': ['id', 'period_id', 'date_due', 'amount_total', 'state', 'status_banco'],
            'order': 'id desc'
        }
    )

    return formatar_faturas(faturas)


def registrar_pagamento(odoo, models, fatura):
    pagamento = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'account.invoice',
        'registrar_pagamento',
        [fatura]
    )

    return pagamento


def formatar_faturas(faturas):
    from datetime import datetime

    for fatura in faturas:
        if fatura['state'] == 'open':
            fatura['state'] = 'Aberta'
        elif fatura['state'] == 'paid':
            fatura['state'] = 'Paga'

        fatura['date_due'] = datetime.strptime(fatura['date_due'], '%Y-%m-%d')
        fatura['nosso_numero'] = '2922611' + str(fatura['id']).rjust(10, '0')

    return faturas