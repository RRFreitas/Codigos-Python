def getMascara(ip):
    if(int(ip[0]) < 128):
        return 'A'
    if(int(ip[0]) < 192):
        return 'B'
    else:
        return 'C'

def isValid(ip):
    bytesIp = ip.split('.')

    if(not len(bytesIp) == 4):
        return False

    for byte in bytesIp:
        try:
            if(int(byte) < 0 or int(byte) > 255):
                return False
        except Exception:
            return False

    return True

ips = open("ips.txt", 'r')
relatorio = open("relatorio.txt", 'w')

ipsvalidos = []
mascaras = []
ipsinvalidos = []

for ip in ips.readlines():
    if(isValid(ip)):
        ipsvalidos.append(ip)
        mascaras.append(getMascara(ip))
    else:
        ipsinvalidos.append(ip)

ips.close()

texto = []
texto.append("[Enderecos validos:]\n")
for i in range(0, len(ipsvalidos) - 1):
    texto.append(str(ipsvalidos[i] + " - " + mascaras[i] + "\n"))
texto.append("\n")
texto.append("[Enderecos invalidos:]\n")
for i in range(0, len(ipsinvalidos) - 1):
    texto.append(ipsinvalidos[i])

relatorio.writelines(texto)
relatorio.close()