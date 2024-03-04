from .indicadores_abstrata import IndicadoresFinanceirosAbs
import fundamentus

class Fundamentus(IndicadoresFinanceirosAbs):

    def recuperar_lista_acoes_por_setor(self, setor_id):
        return fundamentus.list_papel_setor(setor_id)

    def recuperar_indicadores_por_papel(self, papel):
        dados_empresa = fundamentus.get_papel(papel)
        indicadores = {
            "nome_empresa": dados_empresa["Empresa"].values[0],
            "papel": dados_empresa["Papel"].values[0],
            "valor_da_firma":  float(dados_empresa["Valor_da_firma"].values[0]),
            "ebit": float(dados_empresa["EBIT_12m"].values[0]),
            "patrimonio_liquido": float(dados_empresa["Patrim_Liq"].values[0]),
            "divida_liquida": float(dados_empresa["Div_Liquida"].values[0]),
            "disponibilidades": float(dados_empresa["Disponibilidades"].values[0])
        }

        return indicadores
