# 06. Mostre a tabela gerada pelo algoritmo de programação dinâmica para resolver a seguinte
#instancia do problema do SUBSET-SUM: S = {2, 4, 7, 8, 9, 10, 15, 19, 21} e t = 35

# 07. Implemente uma solução de programação dinâmica para o SUBSET-SUM.

def subsetsum(s, t):

    v = []
    for i in range( len(s)+1 ):
        v.append( [0] * (t+1) )

    # instancia primeira posicao da linha inferior com True
    v[len(s)][0] = True

    # instancia demais posicoes da linha inferior como False
    for j in range(1,t+1):
        v[len(s)][j] = False

    for i in range( len(s)-1, -1, -1 ):
        v[i][0] = True #primeira coluna sempre verdadeira
        for j in range( 1, s[i] ):
            v[i][j] = v[i+1][j]
        for j in range( s[i], t+1 ):
            v[i][j] = v[i+1][j] or v[i+1][ j - s[i]]
    
    return v[0][t]



print("# # Programação Dinâmica para SubSet-Sum")

s = [2, 4, 7, 8, 9, 10, 15, 19, 21]
t = 35
exist = subsetsum(s,t)

print(f"sendo s = {s} e t = {t}")
print(f"Existe uma solução" if exist else "Não existe uma solução")

# 08. Calcule a complexidade do algoritmo.
# R: A complexidade de tempo do algoritmo subset-sum utilizando programação dinâmica
# é O(n.t), sendo n o número de elementos do conjunto e t o valor total esperado.
# A complexidade é polinomial ao valor de t, e exponencial ao número de dígitos de t
# pois considerando que para um t=10 (2 dígitos) são calculadas 10 linhas, para um t=100
# (3 dígitos) são calculadas 100 linhas - o que indica que é um problema pseudopolinomial.


# 09. Defina o que é um problema pseudo-polinomial.
# Explique porque essa solução, que usa programação dinâmica,
# não resolve o problema 3-CNF-SAT em tempo polinomial provando que P = NP.

# R: Um algoritmo é executado em tempo pseudopolinomial se o seu tempo de execução é polinomial no valor numérico da entrada,
# mas é exponencial no comprimento da entrada (o número de bits necessários para representá-lo).
# O problema 3-CNF-SAT pode ser reduzido em tempo polinomial para SubSet-Sum, porém
# a solução para SubSet-Sum é calculada em tempo exponencial (problema NP-completo),
# assim, consequentemente 3-CNF-SAT também é resolvido em tempo exponencial, o que não prova que P = NP,
# pois nenhum dos problemas é resolvido em tempo polinomial, apenas sua redução.
# O valor de t cresce exponenciamente ao número de variáveis e cláusulas presentes na fórmula booleana.