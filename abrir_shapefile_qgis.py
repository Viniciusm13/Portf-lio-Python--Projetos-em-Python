#  TODOS OS CAMINHOS E DADOS EDITADOS NESTE CÓDIGO SÃO APENAS EXEMPLOS
#  USAR SEUS DADOS PARA OBTER RESULTADO ESPERADO


from abrir_shapefile_qgis.core import QgsVectorLayer

caminho = r'C:\Users\EXEMPLO\Desktop\BR_Municipios_2022\BR_Municipios_2022.shp'   # Caminho para o arquivo shapefile

camada = QgsVectorLayer(caminho, "BR_Municipios_2022", "ogr")  # Criar uma instância da camada vetorial

# Verificar se a camada foi carregada com sucesso
if not camada.isValid():
    print("Erro ao carregar a camada!")
else:
    # Adicionar a camada ao projeto do QGIS
    QgsProject.instance().addMapLayer(camada)