#  TODOS OS CAMINHOS E DADOS EDITADOS NESTE CÓDIGO SÃO APENAS EXEMPLOS
#  USAR SEUS DADOS PARA OBTER RESULTADO ESPERADO


# Importar os módulos necessários

from qgis.core import QgsVectorLayer, QgsField, QgsExpression, QgsFeature

# Caminho para o arquivo shapefile
caminho = r'C:\Users\EXEMPLO\Desktop\BR_Municipios_2022\BR_Municipios_2022.shp'

# Nome do campo a ser atualizado
nome_campo = 'NM_MUN'

# Lista de municípios desejados
municipios_desejados = ['Buritis', 'Arinos', 'Abadiânia', 'Água Fria De Goiás', 'Águas Lindas De Goiás',
                        'Alto Paraíso De Goiás', 'Alvorada Do Norte', 'Barro Alto', 'Cocalzinho De Goiás',
                        'Corumbá De Goiás', 'Flores De Goiás', 'Formosa', 'Goianésia', 'Luziânia', 'Mimoso De Goiás',
                        'Niquelândia', 'Novo Gama', 'Padre Bernardo', 'Santo Antônio Do Descoberto',
                        'São João D''Aliança', 'Simolândia', 'Vila Propício', 'Alexânia', 'Cabeceiras', 'Cavalcante',
                        'Cidade Ocidental', 'Cristalina', 'Pirenópolis', 'Planaltina', 'Valparaíso De Goiás',
                        'Vila Boa', 'Brasília', 'Unaí', 'Cabeceira Grande']

# Carregar a camada
camada = QgsVectorLayer(caminho, 'BR_Municipios_2022', 'ogr')

# Verificar se a camada foi carregada corretamente
if not camada.isValid():
    print("Erro ao carregar a camada!")
else:
    # Iniciar edição
    camada.startEditing()

    # Obter índice do campo 'NM_MUN'
    indice_campo = camada.fields().indexFromName(nome_campo)

    # Atualizar valores
    for feature in camada.getFeatures():
        valor_atual = feature[nome_campo]
        novo_valor = valor_atual if valor_atual in municipios_desejados else None
        camada.changeAttributeValue(feature.id(), indice_campo, novo_valor)

    # Finalizar edição e salvar as alterações
    camada.commitChanges()
    print("Alterações salvas com sucesso!")

# Recarregar a camada no QGIS para ver as alterações
QgsProject.instance().addMapLayer(camada)