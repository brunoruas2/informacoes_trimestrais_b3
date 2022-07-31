import sys
import requests
import urllib.request as urlRequest

# progress bar
# https://twitter.com/clcoding/status/1549819582390894592

def progressBar(count, total, suffix=''):
    barLenght = 60
    filledLength = int(round(barLenght * count / float(total)))
    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filledLength + '-' * (barLenght - filledLength)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    sys.stdout.flush()

def updateZipFolder():
    # getting the zip files
    url = requests.get('https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/').text
    url = url.split('.zip\">')

    files = []
    for item in url:
        if item[0:3] == 'itr':
            files.append(item.split('</a>')[0])

    # downloading the files into respository src\zip
    print('Downloading Files\n')

    for url in files:
        progressBar(files.index(url)*2,len(url)-1)
        urlRequest.urlretrieve('https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/{}'.format(url),'src\zip\{}'.format(url))

    print('\n\nFiles Updated')