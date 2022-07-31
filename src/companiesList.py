import os
import zipfile as zip
import pandas as pd

PATH = 'src\zip'

def companiesList():
    files = os.listdir(PATH)

    companiesList = pd.DataFrame()
    for file in files:
        zf = zip.ZipFile(PATH + '\\' + file)
        nameFile = zf.namelist()[0]
        companiesYear = pd.read_csv(zf.open(nameFile),encoding='ISO-8859-1',sep=';')
        companiesYear = companiesYear[['CNPJ_CIA','DENOM_CIA','CD_CVM']].drop_duplicates()
        companiesList = pd.concat([companiesList,companiesYear])

    companiesList = companiesList.drop_duplicates()
    companiesList.to_excel('data\\companiesList.xlsx',index=False)
    print('\n\nLista de companhias atualizada. Verifique o arquivo "companiesList.xlsx".')
