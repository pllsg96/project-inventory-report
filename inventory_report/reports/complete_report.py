from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(data):
        empresas = {}
        for i in data:
            if i['nome_da_empresa'] in empresas:
                empresas[i['nome_da_empresa']] += 1
            else:
                empresas[i['nome_da_empresa']] = 1
        continuacao_relatorio = '\nProdutos estocados por empresa:\n'
        
        for chave, valor in empresas.items():
            continuacao_relatorio += f'- {chave}: {valor}\n'
        
        return SimpleReport.generate(data) + continuacao_relatorio
