import sys
sys.path.insert(0, r'src')
from updateZipFiles import updateZipFolder
from companiesList import companiesList
from getDataCompanie import getCompanieData

# atualiza a base de dados
updateZipFolder()

# cria a lista com todas as empresas
companiesList()

# salva a base de dados do demonstrativo por empresa
getCompanieData()