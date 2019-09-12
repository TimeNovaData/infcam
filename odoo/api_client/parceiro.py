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
                'name',
                'legal_name',
                'is_company',
                'cnpj_cpf',
                'phone',
                'mobile',
                'email',
                'street',
                'number',
                'street2',
                'zip',
                'district',
                'l10n_br_city_id',
                'state_id'
            ]
        }
    )

    if parceiro:
        return formatar_parceiro(parceiro[0])
    else:
        return None


def get_id_parceiro(odoo, models, cnpj_cpf):
    parceiro = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'res.partner',
        'search_read',
        [
            [
                ['cnpj_cpf', '=', cnpj_cpf]
            ],
        ],
        {
            'fields': [
                'id',
                'name',
                'legal_name',
                'is_company',
                'cnpj_cpf',
                'phone',
                'mobile',
                'email',
                'street',
                'number',
                'street2',
                'zip',
                'district',
                'l10n_br_city_id',
                'state_id'
            ]
        }
    )

    if parceiro:
        return formatar_parceiro(parceiro[0])
    else:
        return None


def formatar_parceiro(parceiro):
    parceiro['phone'] = parceiro['phone'] or '-'
    parceiro['mobile'] = parceiro['mobile'] or '-'
    parceiro['street'] = parceiro['street'] or '-'
    parceiro['number'] = parceiro['number'] or '-'
    parceiro['street2'] = parceiro['street2'] or '-'
    parceiro['district'] = parceiro['district'] or '-'
    parceiro['zip'] = parceiro['zip'] or '-'

    return parceiro