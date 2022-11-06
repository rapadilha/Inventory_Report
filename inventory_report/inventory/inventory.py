import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        list = []
        with open(path, encoding='utf-8') as file:
            data = csv.DictReader(file)
            for row in data:
                list.append(row)
        if type == 'simples':
            return SimpleReport.generate(list)
        elif type == 'completo':
            return CompleteReport.generate(list)
