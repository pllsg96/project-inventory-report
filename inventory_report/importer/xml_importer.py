from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(file_path, 'r') as xml_file:
            xml_data = xml_file.read()
            xml_reader = xmltodict.parse(xml_data)['dataset']['record']
        return xml_reader