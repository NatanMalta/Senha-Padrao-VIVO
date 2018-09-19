import csv

arquivoCsv = open('vivo-01.csv', 'r')

try:
    reader = csv.reader(arquivoCsv)

    for linha in reader:
        
        if not linha:
            pass
        else:
            
            if linha[0] == 'Station MAC':
                break
            else:
                dicio = { 'BSSID':linha[0],'ESSID':linha[13] }

                if dicio['BSSID'] == 'BSSID':
                    pass
                else:

                    if 'VIVO-' in dicio['ESSID']:
                        print(dicio['ESSID'], dicio['BSSID'][3:].replace(':',''))
                    
                
            
finally:
    arquivoCsv.close()
