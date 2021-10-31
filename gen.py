import math
import random
import sys

tests = 1
for i in range(tests):
	if len(sys.argv) == 4:
		n,m,k = map(int, sys.argv[1:])
	else:
		n = random.randrange(3, 100) # animales
		m = random.randrange(2, 60) # partes incl aper
		k = random.randrange(1, n) # escenas por parte

	print('{}\n{}\n{}'.format(n, m , k))

	nombres, grandezas = [], []
	banco = list(range(1, n+1))
	for a in range(n):
		# gen nombres
		nombre = ''
		while(nombres.count(nombre) > 0 or nombre == ''):
			nombre = ''
			for l in range(math.ceil(math.log(n, 26))):
				nombre += random.choice('qwertyuiopasdfghjklzxcvbnm')
				nombre += random.choice('aeiou')
		nombres.append(nombre)
		grandezas.append(banco.pop(random.randrange(len(banco))))

	print(''.join([i+', ' for i in nombres]).strip(', '))
	print(''.join([str(i)+', ' for i in grandezas]).strip(', '))

	partes = [[[] for e in range(k)] for i in range(m-1)]
	for p in partes:
		for e in p:
			banco = nombres.copy()
			e.append(banco.pop(random.randrange(len(banco))))
			e.append(banco.pop(random.randrange(len(banco))))
			e.append(banco.pop(random.randrange(len(banco))))

	apertura = [e for p in partes for e in p]
	random.shuffle(apertura)
	print(''.join(['{'+''.join([a+', ' for a in e]).strip(', ')+'}'+', ' for e in apertura]).strip(', '))
	for p in partes:
		print(''.join(['{'+''.join([a+', ' for a in e]).strip(', ')+'}'+', ' for e in p]).strip(', '))

