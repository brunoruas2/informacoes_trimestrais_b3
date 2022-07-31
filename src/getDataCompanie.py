import os
import zipfile as zip
import pandas as pd

def getCompanieData():
    PATH = 'src\zip'

    cvmCode = input('\n\nPor favor, diga o código CVM da empresa. Se você tiver uma dúvida sobre o código, pode procurar no site:\nhttps://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm\n\nCódigo CVM: ')

    wichTypeFile = input('\n\nQual tipo de demonstrativo você quer coletar?\n\n1 - Consolidado\n2 - Individualizado\n\nTipo de Demonstrativo: ')

    wichFile = input('\n\nQual demonstrativo você quer baixar?\n\n1 - Balanço Patrimonial Ativo (BPA)\n2 - Balanço Patrimonial Passivo (BPP)\n3 - Demonstração de Fluxo de Caixa - Método Direto (DFC-MD)\n4 - Demonstração de Fluxo de Caixa - Método Indireto (DFC - MI)\n5 - Demonstração das Mutanções do Patrimônio Líquido (DMPL)\n6 - Demonstração de Resultado Abrangente (DRA)\n7 - Demonstração de Resultado (DRE)\n8 - Demonstração de Valor Adicionado (DVA)\n\nDemonstrativo: ')

    files = os.listdir(PATH)

    companieData = pd.DataFrame()
    for file in files:
        zf = zip.ZipFile(PATH + '\\' + file)
        nameFile = zf.namelist()
        nameFile.pop(0)
        
        individual = []
        consolidado = []
        
        [consolidado.append(x) if nameFile.index(x)%2 == 0 else individual.append(x) for x in nameFile]
        
        if wichTypeFile == '1':
            nameFile = individual[int(wichFile)-1]
        else:
            nameFile = consolidado[int(wichFile)-1]
        
        demonstrative = pd.read_csv(zf.open(nameFile),encoding='ISO-8859-1',sep=';')
        demonstrative = demonstrative[demonstrative['CD_CVM'] == int(cvmCode)]
        companieData = pd.concat([companieData,demonstrative])

    companieData.to_excel('data\\{}.xlsx'.format(nameFile[15:-9]),index=False)
    print('\n\nArquivo criado na pasta "data".\n\n')