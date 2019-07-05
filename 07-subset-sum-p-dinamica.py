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

print(f"Sendo s = {s} e t = {t}")
print(f"Existe uma solução" if exist else "Não existe uma solução")