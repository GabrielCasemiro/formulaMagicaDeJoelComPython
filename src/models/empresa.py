class Empresa:
    def __init__(self, papel, nome_empresa, ebit, patrimonio_liquido, divida_liquida, valor_da_firma, disponibilidades):
        self.papel = papel
        self.nome_empresa = nome_empresa
        self.ebit = ebit
        self.patrimonio_liquido = patrimonio_liquido
        self.divida_liquida = divida_liquida
        self.valor_da_firma = valor_da_firma
        self.disponibilidades = disponibilidades
    

    def calcular_rendimento_lucros(self):
        return self.ebit / (self.valor_da_firma - self.disponibilidades)
    
    def calcular_retorno_sobre_capital(self):
        return self.ebit / (self.patrimonio_liquido + self.divida_liquida)
