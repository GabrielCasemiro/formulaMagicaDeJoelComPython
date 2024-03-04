from models.empresa import Empresa
from models.formula_magica import FormulaMagica
from models.indicadores_financeiros.fundamentus import Fundamentus as PlataformaIndicadores


indicadores_financeiros = PlataformaIndicadores()
formula_magica = FormulaMagica()

setores = [21] # papel e madeira

for setor_id in setores:
    for empresa_papel in indicadores_financeiros.recuperar_lista_acoes_por_setor(setor_id=setor_id):
        dados_empresa = indicadores_financeiros.recuperar_indicadores_por_papel(empresa_papel)
        empresa_obj = Empresa(**dados_empresa)
        print("Papel", empresa_obj.papel)
        print("Retorno sobre capital", empresa_obj.calcular_retorno_sobre_capital())
        print("Rendimento sobre os lucros", empresa_obj.calcular_rendimento_lucros())
        formula_magica.adicionar_empresa(empresa_obj)

formula_magica_lista = formula_magica.recuperar_ranqueamento_empresas()
print("Fórmula mágica", formula_magica_lista)