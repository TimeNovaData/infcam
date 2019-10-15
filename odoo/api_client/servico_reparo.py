def criar_servico_reparo(odoo, models, produto, nome, unidade_medida, preco_unitario, quantidade, reparo):
    servico_reparo = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair.fee',
        'create',
        [{
            'product_id': produto,
            'produto_uom_qty': quantidade,
            'repair_id': reparo,
            'name': nome,
            'price_unit': preco_unitario,
            'product_uom': unidade_medida,
        }]
    )

    return servico_reparo or None