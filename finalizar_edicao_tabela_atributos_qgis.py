#  TODOS OS CAMINHOS E DADOS EDITADOS NESTE CÓDIGO SÃO APENAS EXEMPLOS
#  USAR SEUS DADOS PARA OBTER RESULTADO ESPERADO


# Importar os módulos necessários
from qgis.core import QgsVectorLayer, QgsFeatureRequest

# Caminho para o arquivo shapefile
caminho = r'C:\Users\EXEMPLO\Desktop\BR_Municipios_2022\BR_Municipios_2022.shp'

# Nome do campo a ser verificado
nome_campo = 'NM_MUN'

# Carregar a camada
camada = QgsVectorLayer(caminho, 'BR_Municipios_2022', 'ogr')

# Verificar se a camada foi carregada corretamente
if not camada.isValid():
    print("Erro ao carregar a camada!")
else:
    # Selecionar as features com valores NULL na coluna 'NM_MUN'
    exp = QgsExpression('"{}" IS NULL'.format(nome_campo))
    selecionar = [f.id() for f in camada.getFeatures(QgsFeatureRequest(exp))]
    camada.selectByIds(selecionar)

    # Remover as features selecionadas
    camada.dataProvider().deleteFeatures(selecionar)

    # Finalizar edição e salvar as alterações
    camada.commitChanges()
    print("Linhas com valores NULL excluídas e edição finalizada com sucesso!")

# Recarregar a camada no QGIS para ver as alterações
QgsProject.instance().addMapLayer(camada)
