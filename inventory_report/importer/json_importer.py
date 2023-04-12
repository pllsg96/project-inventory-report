from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith('.json'):
            raise ValueError('Arquivo inválido')
        with open(file_path, 'r') as json_file:
            json_reader = json.load(json_file)
        return json_reader
