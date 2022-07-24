from base64 import encode
import os
import zipfile as zip
import pandas as pd
from pynvim import encoding

PATH = 'src\zip'

files = os.listdir('src\zip')

companiesList = pd.DataFrame()
for file in files:
    zf = zip.ZipFile(PATH + '\\' + file)
    nameFile = zf.namelist()[0]
    companiesYear = pd.read_csv(zf.open(nameFile),encoding='ISO-8859-1',sep=';')
    companiesYear = companiesYear[['CNPJ_CIA','DENOM_CIA','CD_CVM']]
    companiesList = companiesList.append(companiesYear)

companiesList = companiesList.drop_duplicates