import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        list = []
        with open(path, encoding='utf-8') as file:
            if path.endswith('csv'):
                data = csv.DictReader(file)
            elif path.endswith('json'):
                data = json.load(file)
            else:
                data = xmltodict.parse(file.read())["dataset"]["record"]
            for row in data:
                list.append(row)
        if type == 'simples':
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)
