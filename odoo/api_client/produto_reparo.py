def criar_produto_reparo(odoo, models, produto, nome, unidade_medida, preco_unitario, quantidade, reparo):
    produto_reparo = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'mrp.repair.line',
        'create',
        [{
            'product_id': produto,
            'produto_uom_qty': quantidade,
            'type': 'add',
            'repair_id': reparo,
            'name': nome,
            'price_unit': preco_unitario,
            'product_uom': unidade_medida,
            'location_id': 14,
            'location_dest_id': 9
        }]
    )

    return produto_reparo or None