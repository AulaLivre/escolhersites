#Meus sites favoritos:
import webbrowser as wb
import random as rd

print('-------------------------')
print('  MEUS SITES FAVORITOS  |')
print('-------------------------')

def randomica():
	ran = rd.randint(1, 5) 
	if ran == 1:
		wb.open('https://www.google.com/')
	elif ran == 2:
		wb.open('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')
	elif ran == 3:
		wb.open('https://www.youtube.com/')
	elif ran == 4:
		wb.open('https://www.chess.com/pt-BR')
	elif ran == 5:
		wb.open('https://www.foxnews.com/')
		
def main():
	while True:	
		print('GOGLE[1], WIKIPEDIA[2], YOUTUBE[3], CHESS.COM[4], FOX NEWS[5], RANDOMIZAR[6], EXIT[7].')
		x = int(input('>>>'))
		#Condições:
		if x == 1:
			wb.open('https://www.google.com/')
		elif x == 2:
			wb.open('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')
		elif x == 3:
			wb.open('https://www.youtube.com/')
		elif x == 4:
			wb.open('https://www.chess.com/pt-BR')
		elif x == 5:
			wb.open('https://www.foxnews.com/')
		elif x == 6:
			randomica()
		elif x == 7:
			input('Aperte enter para sair.')
			break
		else:
			print('Opção não aceita, por favor digite uma opção válida.')
		print()		
main()

