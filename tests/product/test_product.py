from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        'shampoo',
        'natura',
        '01/01/23',
        '01/12/23',
        'NA00123045',
        'Armazenar longe do sol')
    assert new_product.id == 1
    assert new_product.nome_do_produto == 'shampoo'
    assert new_product.nome_da_empresa == 'natura'
    assert new_product.data_de_fabricacao == '01/01/23'
    assert new_product.data_de_validade == '01/12/23'
    assert new_product.numero_de_serie == 'NA00123045'
    assert new_product.instrucoes_de_armazenamento == 'Armazenar longe do sol'