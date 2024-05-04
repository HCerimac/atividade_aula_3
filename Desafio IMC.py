

peso_em_quilogramas = int(input('Insira seu peso aqui:'))
altura_em_metros = float(input('Insira sua altura aqui:'))
resposta = peso_em_quilogramas//altura_em_metros**2
print('Seu IMC é:',resposta,)
print('A tabela do IMC é a seguinte:')
print('resultados menores que 16 — magreza grave')
print('resultados entre 16 e 16,9 — magreza moderada')
print('resultados entre 17 e 18,5 — magreza leve')
print('resultados entre 18,6 e 24,9 — peso ideal')
print('resultados entre 25 e 29,9 — sobrepeso')
print('resultados entre 30 e 34,9 — obesidade grau ')
print('resultados entre 35 e 39,9 — obesidade grau II ou severa')
print('resultados maiores do que 40 — obesidade grau III ou mórbida')