i = 0
j = 0
arq = open('matrix.txt','r+')
data = arq.read()
matriz = data.split("\n")
matriz.remove("")
for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		if(matriz[i][j] == "1"):
			print(True)
		else:
			print(False)

