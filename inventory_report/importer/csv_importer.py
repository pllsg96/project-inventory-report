from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        with open(file_path, 'r') as csv_file:
            csv_reader = list(csv.DictReader(csv_file))
        return csv_reader