'''

# iterazione_py

# Programmi di Laboratorio di Programmazione (Linguaggio "Pyton" ("py")). Alunno: Bucchianico Enrico Ruggiero, 4^Finf.


- Programma "tabelline.py": Programma che stampa la Tavola Pitagorica da "0" a "12".

'''

print("TAVOLA PITAGORICA DA \"0\" A \"12\"\n\n")

for v in range(0, 12+1):
	for o in range (0, 12+1):
		print('%10d'%(v*o,),end='')
	print(' ')