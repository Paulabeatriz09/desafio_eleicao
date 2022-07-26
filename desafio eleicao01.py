
candidato_x=0
candidato_y=0
candidato_z=0
branco=0
enc='não'


while (enc=='não'):

    voto = int(input("Digite 889 para votar no candidato X, 847 para o candidato y, 515 para o candidato Z, ou digite 0 para votar branco:"));

    if(type(voto)==int):
        if(voto==889):
            candidato_x +=1
        if(voto==847):
            candidato_y +=1
        if(voto==515):
            candidato_z +=1
        if(voto==0):
            branco +=1
        else:
            branco +=1
    else:
        print("digite um número válido:")
        continue

    enc=str(input("Caso deseje finalizar escreva -sim-, ou -não- para continuar?"))
    if(enc=='sim'):
        break

if(candidato_x>candidato_y and candidato_x>candidato_z):
    print("o candidato X foi o vencedor")

elif(candidato_y>candidato_x and candidato_y>candidato_z):
     print("o candidato Y foi o vencedor")

elif(candidato_z>candidato_x and candidato_z>candidato_y):
     print("o candidato Z foi o vencedor")

elif(branco>candidato_x and branco>candidato_y and branco>candidato_z):
     print("O maior número de votos foi nulo ou branco, votação não válida")


print("O candidato X teve", candidato_x, "votos.")
print("O candidato Y teve", candidato_y, "votos.")
print("O candidato Z teve", candidato_z, "votos.")
print("Brancos ou nulos foram", branco, "votos.")
