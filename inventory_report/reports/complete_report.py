from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(items):
        simpleReport = SimpleReport.generate(items)
        completeReport = 'Produtos estocados por empresa:\n'
        companyNames = [c['nome_da_empresa'] for c in items]
        for company in Counter(companyNames).most_common():
            name = company[0]
            quant = company[1]
            report = f'- {name}: {quant}\n'
            completeReport += report
        return f'{simpleReport}\n{completeReport}'
