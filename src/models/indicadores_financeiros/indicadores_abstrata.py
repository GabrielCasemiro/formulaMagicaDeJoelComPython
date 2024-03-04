from abc import ABC, abstractmethod

class IndicadoresFinanceirosAbs(ABC):

    @abstractmethod
    def recuperar_lista_acoes_por_setor(self, setor_id):
        pass

    @abstractmethod
    def recuperar_indicadores_por_papel(self, papel):
        pass 
