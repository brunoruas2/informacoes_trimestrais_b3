import sys
sys.path.insert(0, r'src')
from updateZipFiles import updateZipFolder
from companiesList import companiesList
from getDataCompanie import getCompanieData

keepAlive = True
while keepAlive == True:
    command = input("\n\nO que você quer fazer?\n\n1 - Update na base de dados\n2 - Update na lista de empresas\n3 - Coletar um demonstrativo\n\nComando: ")
    
    if command == '1':
        # atualiza a base de dados
        updateZipFolder()
    elif command == '2':
        # cria a lista com todas as empresas
        companiesList()
    elif command == '3':
        # salva a base de dados do demonstrativo por empresa
        getCompanieData()
    
    exitTest = input('\n\nDeseja executar outro comando?\n\n1 - Sim\n2 - Não (sair)\n\nComando: ')
    if exitTest == '2':
        keepAlive = False