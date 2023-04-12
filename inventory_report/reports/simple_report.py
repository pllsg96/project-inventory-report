from datetime import date


class SimpleReport:
    @staticmethod
    def generate(data: list) -> list:
        fab_antiga = SimpleReport.fabricacao_antiga(data)
        val_proxima = SimpleReport.validade_proxima(data)
        emp_mais_prod = SimpleReport.contador_empresa(data)
        return (
            f"Data de fabricação mais antiga: {fab_antiga}\n"
            f"Data de validade mais próxima: {val_proxima}\n"
            f"Empresa com mais produtos: {emp_mais_prod}"
        )

    def fabricacao_antiga(data: list) -> list:
        data_de_fabricacao = date.max
        for i in data:
            fabricacao = date.fromisoformat(i["data_de_fabricacao"])
            if date.fromisoformat(i["data_de_validade"]) >= date.today():
                if fabricacao < data_de_fabricacao:
                    data_de_fabricacao = fabricacao
        return data_de_fabricacao

    def validade_proxima(data: list) -> list:
        data_de_validade = date.max
        for i in data:
            validade = date.fromisoformat(i["data_de_validade"])
            if date.fromisoformat(i["data_de_validade"]) >= date.today():
                if data_de_validade > validade:
                    data_de_validade = validade
        return data_de_validade
    
    def contador_empresa(data: list) -> str:
        all_empresas = {}
        for i in data:
            if (i['nome_da_empresa'] in all_empresas):
                all_empresas[i['nome_da_empresa']] += 1
            else:
                all_empresas[i['nome_da_empresa']] = 1
                
        return max(all_empresas, key=all_empresas.get)