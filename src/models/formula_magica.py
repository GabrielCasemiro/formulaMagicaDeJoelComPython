class FormulaMagica:
    def __init__(self):
        self.__empresas = []
    
    def adicionar_empresa(self, empresa):
        self.__empresas.append(empresa)
        return

    def __recuperar_lista(self, tipo_lista):
        dict_retorno = {}
        for empresa in self.__empresas:
            if tipo_lista == "retorno_sobre_capital":
                valor = empresa.calcular_retorno_sobre_capital()
            else:
                valor = empresa.calcular_rendimento_lucros()

            dict_retorno[empresa.papel] =  valor

        return [x[0] for x in sorted(dict_retorno.items(), key=lambda x:x[1], reverse=True)]

    def recuperar_ranqueamento_empresas(self) -> list:
        dict_formula_magica = {}
        lista_retorno_sobre_capital = self.__recuperar_lista(tipo_lista="retorno_sobre_capital")
        lista_rendimento_lucros = self.__recuperar_lista(tipo_lista="rendimento_lucros")

        print("Lista retorno sobre capital", lista_retorno_sobre_capital)
        print("Lista de rendimento dos lucros", lista_rendimento_lucros)

        for empresa in self.__empresas:
            pontuacao_formula_magica = lista_retorno_sobre_capital.index(empresa.papel) + lista_rendimento_lucros.index(empresa.papel)
            dict_formula_magica[empresa.papel] = pontuacao_formula_magica

        return sorted(dict_formula_magica.items(), key=lambda x:x[1])