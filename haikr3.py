import random
import re
# encoding: utf-8

# Ler um novo arquivo de frases
with open('frasestest.txt', 'r') as frases:
	count = 1
	output = open('novasfrases.txt', 'w')
	for line in frases:
		if count == 1:
			print "Original"
			print line
			print "\n"
			count +=1
		elif count == 2:
			words = re.findall(r"[\w']+|[.,!?;]", line)
			print "Modelo"
			print line
			count = 1
			for index, word in enumerate(words):
				if word == "XXX":
					nword = str(raw_input("qual palavra deve substituir XXX? "))
					words[index] = nword
			print "Resultado"
			#  cria o cancioneiro de poemas
			print ' '.join(words)
			output.write(' '.join(words))
    		output.write(".\n")
output.close()
	




