def get_parceiro(odoo, models, parceiro):
    parceiro = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'res.partner',
        'search_read',
        [
            [
                ['id', '=', parceiro]
            ],
        ],
        {
            'fields': [
                'id',
                'company_type',
                'name',
                'vat',
                'mobile',
                'email',
                'street',
                'street2',
                'zip',
                'city',
                'state_id'
            ]
        }
    )

    if parceiro:
        return formatar_parceiro(parceiro[0])
    else:
        return None


def get_id_parceiro(odoo, models, email):
    parceiro = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'res.partner',
        'search_read',
        [
            [
                ['email', '=', email]
            ],
        ],
        {
            'fields': [
                'id',
                'company_type',
                'name',
                'vat',
                'mobile',
                'email',
                'street',
                'street2',
                'zip',
                'city',
                'state_id'
            ]
        }
    )

    if parceiro:
        return formatar_parceiro(parceiro[0])
    else:
        return None


def criar_parceiro(odoo, models, nome, pessoa_fisica_juridica, cpf_cnpj, celular, email):
    parceiro = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'res.partner',
        'create',
        [{
            'company_type': pessoa_fisica_juridica=='True',
            'name': nome,
            'vat': cpf_cnpj,
            'mobile': celular,
            'email': email,
        }]
    )

    return parceiro or None


def formatar_parceiro(parceiro):
    parceiro['vat'] = parceiro['vat'] or '-'
    parceiro['mobile'] = parceiro['mobile'] or '-'
    parceiro['email'] = parceiro['email'] or '-'
    parceiro['street'] = parceiro['street'] or '-'
    parceiro['street2'] = parceiro['street2'] or '-'
    parceiro['zip'] = parceiro['zip'] or '-'
    parceiro['city'] = parceiro['city'] or '-'

    return parceiro
