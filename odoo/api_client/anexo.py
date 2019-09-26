def criar_anexo(odoo, models, nome, arquivo, mimetype, model, id_relativo):
    anexo = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'ir.attachment',
        'create',
        [{
            'res_model': model,
            'name': nome,
            'res_id': id_relativo,
            'res_name': nome,
            'type': 'binary',
            'datas': arquivo,
            'datas_fname': nome,
            'mimetype': mimetype
        }]
    )

    return anexo or None