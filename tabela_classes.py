import math
import random

def amostragem_aleatoria():
    lista = []
    tam = int(input("Digite o tamanho da amostragem:"))
    for i in range(0,tam):
            lista.append(random.randint(0, 100))
    lista.sort()
    print("AMOSTRA:",lista,"\n")
    
    return lista


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
    if max(lista) >= aux:
        classes.append([])
        classes[len(classes)-1].append(aux)
        classes[len(classes)-1].append(aux+h)
        
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
    
def imprimir_tabela(classes, absoluta, ponto_medio, xifi, acumulada, relativa):
    soma_xifi = 0
    soma_fri = 0
    
    formato_cabecalho = '{:<5} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}'
    print("\n\n")
    print("-"*80)
    print(formato_cabecalho.format('i', 'CLASSE', 'Fi', 'Xi','Xi.Fi', 'Fa', 'FRi'))
    print("-"*80)
    for i in range(len(classes)):
        formato = '{:<5} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10.2f}%'
        print(formato.format(i+1, (str(classes[i][0])+"|--"+str(classes[i][1])), absoluta[i], ponto_medio[i], xifi[i],acumulada[i],relativa[i]))
        soma_xifi += xifi[i]
        soma_fri += relativa[i]
    print("-"*80)    
    print(formato.format("TOTAL","",acumulada[-1],"",soma_xifi,"",soma_fri))
    print("-"*80)
    
    
def main():
    
    dados = amostragem_aleatoria()
    #print("DADOS:\n",dados)
    amp_total = amplitude_total(dados)
    print("AMPLITUDE TOTAL:",amp_total,"\n")
    sturges = regra_sturges(dados)
    print("REGRA DE STURGES:",sturges,"\n")
    amp_classe = amplitude_classe(amp_total, sturges)
    print("AMPLITUDE DE CLASSE:",amp_classe,"\n")
    classes = montar_classes(dados, amp_classe, sturges)
    print("CLASSES:",classes,"\n")
    ponto_medio = calcular_ponto_medio(classes)
    print("PONTO MEDIO:", ponto_medio,"\n")
    absoluta = frequencia_absoluta(dados, classes)
    print("FREQUENCIA ABSOLUTA:", absoluta,"\n")
    acumulada = frequencia_acumulda(absoluta)
    print("FREQUENCIA ACUMULADA:", acumulada,"\n")
    relativa = frequencia_relativa(absoluta, dados)
    print("FREQUENCIA RELATIVA:", relativa,"\n")
    xifi = calcular_xifi (absoluta, ponto_medio)
    print("Xi.Fi:", xifi,"\n")
    imprimir_tabela(classes, absoluta, ponto_medio, xifi, acumulada, relativa)
    
    
    
main()
