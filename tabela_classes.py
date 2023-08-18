import math

def dados_brutos():
    dados = [ 45, 41, 42, 41, 42, 43, 44, 41 ,50, 46, 50, 46, 60, 54, 52,58, 57, 58,60, 51]
    op = "S"
    """
    while op == "S":
        dados.append(float(input("Digite a observação:")))
        op = input("Continuar inserindo?(s/n)").upper()
    """
    dados.sort()
    return dados

def amplitude_total(lista):
    h_total = max(lista) - min(lista)
    
    return h_total

def regra_sturges(lista):
    k = 1 + 3.3*math.log10(len(lista))

    return round(k)

def amplitude_classe(h_total , k):
    h = h_total/k
    
    return round(h)
    
def montar_classes(lista, h, k):
    classes = []
    aux = min(lista)
    
    for i in range(k):
        classes.append([])
        classes[i].append(aux)
        classes[i].append(aux+h)
        aux = aux+h
    
    return classes
        
        
def frequencia_absoluta(dados, classes):
    absoluta = []
    count = 0
    
    for i in range(len(classes)):
        for j in range(len(dados)):
            if dados[j] >= classes[i][0] and dados[j] < classes[i][1]:
                count += 1
        absoluta.append(count)        
        count = 0
    
    return absoluta
    
def calcular_ponto_medio(classes):
    ponto_medio = []
    
    for i in range(len(classes)):
        ponto_medio.append((classes[i][0]+classes[i][1])/2)
    
    return ponto_medio
    
def calcular_xifi (absoluta, ponto_medio):
    xifi = []
    
    for i in range(len(absoluta)):
        xifi.append(absoluta[i]*ponto_medio[i])
    
    return xifi
        
def frequencia_acumulda(absoluta):
    acumulada = [absoluta[0]]
    
    for i in range(1,len(absoluta)):
        acumulada.append(absoluta[i]+acumulada[i-1])
    
    return acumulada

def frequencia_relativa(absoluta, lista):
    relativa = []
    
    for i in range(len(absoluta)):
        relativa.append((absoluta[i]/len(lista))*100)
    
    return relativa
    
def main():
    dados = dados_brutos()
    print("DADOS:\n",dados)
    amp_total = amplitude_total(dados)
    print("AMPLITUDE TOTAL:\n", amp_total)
    sturges = regra_sturges(dados)
    print("REGRA DE STURGES:\n", sturges)
    amp_classe = amplitude_classe(amp_total, sturges)
    print("AMPLITUDE DE CLASSE:\n", amp_classe)
    classes = montar_classes(dados, amp_classe, sturges)
    print("CLASSES:\n", classes)
    ponto_medio = calcular_ponto_medio(classes)
    print("PONTO MEDIO:\n", ponto_medio)
    absoluta = frequencia_absoluta(dados, classes)
    print("FREQUENCIA ABSOLUTA: \n", absoluta)
    acumulada = frequencia_acumulda(absoluta)
    print("FREQUENCIA ACUMULADA: \n", acumulada)
    relativa = frequencia_relativa(absoluta, dados)
    print("FREQUENCIA RELATIVA: \n", relativa)
    xifi = calcular_xifi (absoluta, ponto_medio)
    print("Xi.Fi:\n", xifi)
    
    
    
main()


"""
i   Classe    fi   Xi   Xi.fi   fa   fri
1   41|--45   7    43   301     7    35%
2   45|--49   3    47   141     10   15%
3   49|--53   4    51   204     14   20%
4   53|--57   1    55   55      15   05%
5   57|--61   5    59   295     20   25%
TOTAL         20        996          100%
"""
      
    
