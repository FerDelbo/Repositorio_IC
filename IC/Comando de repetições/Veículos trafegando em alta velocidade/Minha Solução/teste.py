def Veiculos_trafegando_em_alta_velocidade(vetor):
    velocidade_maxima = vetor[0]
    infracoes = 0
    for i in range(1, len(vetor)):
        if vetor[i] > (velocidade_maxima *0.20) and vetor[i] < (velocidade_maxima * 0.50):
            print(f"{i}\n")
            infracoes+1
    print(f"{infracoes}\n")

velocidade = []
Veiculos_trafegando_em_alta_velocidade(velocidade)
#caso de teste que possivelmente não foram tratados
# vetor de velocidades nulo entrda :[0, 0, 0, 0, 0, 0] saida: 0 
# vetor de velocidades vazio entrada: [] saida: erro na parte de pegar a primira posicao do vetor
#vetor de velocidades [60, 11.9, 12, 12.1, 29.1, 30, 30.1,]