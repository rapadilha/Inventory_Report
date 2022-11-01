from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Almoço',
        'Dom Supremo',
        '01-11-2022',
        '01-11-2022',
        5495,
        'Colocar na geladeira'
        )
    assert product.id == 1
    assert product.data_de_validade == '01-11-2022'
    assert product.data_de_fabricacao == '01-11-2022'
    assert product.nome_da_empresa == 'Dom Supremo'
    assert product.nome_do_produto == 'Almoço'
    assert product.numero_de_serie == 5495
    assert product.instrucoes_de_armazenamento == 'Colocar na geladeira'
