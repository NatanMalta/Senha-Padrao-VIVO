# Senha Pradrão VIVO-####

Esse script python monta a senha padrão Wifi de rotedores distribuido pela vivo. 

Use o airodump-ng com o seguinte comando:

airodump-ng -w <nome do arquivo> --output-format csv wlan0mon

Inicie o script:
python3 vivo.py
E depois informe o arquivo .csv gerado pelo airodump-ng
