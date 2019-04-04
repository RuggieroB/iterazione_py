'''

# iterazione_py

# Programmi di Laboratorio di Programmazione (Linguaggio "Pyton" ("py")). Alunno: Bucchianico Enrico Ruggiero, 4^Finf.


- Programma "pigreco.c": Programma che calcola il valore di π mediante la formula: π=4-4/3+4/5-4/7+4/9-4/11+4/n+...
			  Il numero di termini da utilizzare nella serie è inserito dall'utente.

'''

pi=0

segno=1
num_termini=-1

while num_termini<0:
	num_termini=input("Inserire il numero di termini da utilizzare:\t")
	num_termini=int(num_termini)

for i in range(num_termini):
	pi+=segno*4.0/(2.0*i+1)
	segno=-segno

print("pi=\t",pi)
