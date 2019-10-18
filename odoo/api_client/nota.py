def criar_nota(odoo, models, reparo, texto):
    nota = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mail.message',
        'create',
        [{
            'message_type': 'comment',
            'body': texto,
            'model': 'mrp.repair',
            'res_id': reparo,
            'subtype_id': 2,
        }]
    )

    return nota or None