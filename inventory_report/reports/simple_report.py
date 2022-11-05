from collections import Counter


class SimpleReport:

    def generate(items):
        oldFab = min(i['data_de_fabricacao'] for i in items)
        minVal = min(i['data_de_validade'] for i in items)
        compCount = Counter(i['nome_da_empresa'] for i in items)

        return (
            f'Data de fabricação mais antiga: {oldFab}\n'
            f'Data de validade mais próxima: {minVal}\n'
            f'Empresa com mais produtos: {compCount.most_common(1)[0][0]}'
        )
