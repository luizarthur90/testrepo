família = ["Luiz", "Aline", "Pituco", "Pandora", "Holly"]
#            0        1        2         3          4
#           -5       -4       -3        -2         -1

#print(família[0]) - retorna um índice
#print(familía[-1]) - retorna um índice de traz pra frente
#print(família[2:]) - retorna a partir do índice 2
#print(família[2:4]) - retorna a partir do indeico até o 4, excluindo o 4

#print(família)
## família[2] = "Picutuco"
#print(família)

#família.extend(["Luiz Gonzaga", "Eliane", "Isabella"]) - Adiciona os valores no final da lista. 
#família.insert(2, "Ana Luiza") - Insere o valor no índice. 
#família.pop() - Remove o último valor da lista. 
#família.remove("Holly") - Remove o valor parâmetro da lista.
#família.clear() - Remove todos os valores da lista.                
#print(família.index("Picutuco"))  - Retorna o índice do valor parâmetro da lista.

#print(família.count("Luiz Gonzaga"))

#idade_família = [33,34,1,2,3]
#idade_família.sort()
#print(idade_família)

#família.sort()
#print(família)

#idade_família.reverse()
#print(idade_família)

#família.reverse()
#print(família)

## CÓPIA POR REFERÊNCIA ##

#família2 = família
#print(família2)
#família.remove("Luiz")
#print(família2)      

## CÓPIA SEM REFERÊNCIA ##

família2 = família.copy()
família.remove("Luiz")
print(família)
print(família2)

## TUPLES ##

## coordenadas = (-49, -36)
## coordenadas.pop()
## print(coordenadas)

