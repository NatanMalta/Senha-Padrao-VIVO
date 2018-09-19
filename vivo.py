import csv

with  open(str(input('Arquivo .csv Airodump-ng: '))) as arquivoCsv:

    print('\n    Rede     Senha')

    try:
        reader = csv.reader(arquivoCsv)

        for linha in reader:

            if not linha: # Verifica se a lista está vazia
                pass
            else:

                if linha[0] == 'Station MAC': # Sai do for porque é onde acaba as redes wireless do arquivo .csv
                    break
                else:
                    dicio = { 'BSSID':linha[0],'ESSID':linha[13] } # Dicionário que contem o nome e MAC da rede wirilless

                    if dicio['BSSID'] == 'BSSID': # Ignora a primeira linha do arquivo .csv
                        pass
                    else:
                        if 'VIVO-' in dicio['ESSID']: # Apenas mostra as redes VIVO-
                            senha = dicio['BSSID'][3:-5].replace(':', '')+dicio['ESSID'][6:]

                            print(dicio['ESSID'], senha)

    finally:
        print('\n')
        arquivoCsv.close()
