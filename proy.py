# This is very unreadable. It became intententional by the end

import sys

def ordenarEscena(e):
	global escenaMasGrande, escenaMasPequena, promedio, aprcns
	if gT(e) > gT(escenaMasGrande):
		escenaMasGrande = e
	if gT(e) < gT(escenaMasPequena):
		escenaMasPequena = e
	promedio = promedio + gT(e)/(2.0*(m-1)*k) 
	aprcns[e[0]] = aprcns[e[0]]+1
	aprcns[e[1]] = aprcns[e[1]]+1
	aprcns[e[2]] = aprcns[e[2]]+1
	if(anms[e[0]] < anms[e[1]]):
		if(anms[e[0]] < anms[e[2]]):
			if(anms[e[1]] < anms[e[2]]):
				r = [0,1,2]
			else:
				r = [0,2,1]
		else:
			r = [2,0,1]
	else:
		if(anms[e[0]] < anms[e[2]]):
			r = [1,0,2]
		else:
			if(anms[e[1]] < anms[e[2]]):
				r = [1,2,0]
			else:
				r = [2,1,0]
	return [e[r[0]], e[r[1]], e[r[2]]]

def countingSort(l, f, cota): # l: lista a ordenar, f: función que mapea l a los naturales, cota: maximo de codominio de f
	count = [0 for i in range(cota+1)]
	for e in l:
		count[f(e)] += 1
	for i in range(1, cota+1):
		count[i] += count[i-1]
	r = [0 for e in range(len(l))]
	for e in reversed(l):
		r[count[f(e)]-1] = e
		count[f(e)] -= 1
	return r

def mergeSort(l, f, cota): # l: lista a ordenar, f: función que mapea l a los naturales, cota: sin usar, solo para igualar args de countingSort
	if len(l) > 1: 
		m = len(l) // 2
		i = mergeSort(l[:m], f, cota) 
		d = mergeSort(l[m:], f, cota) 
		r = []
		while len(i) > 0 and len(d) > 0: 
			r.append((i if f(i[0]) <= f(d[0]) else d).pop(0))
		return r+i+d
	else:
		return l

def insertionSort(l, f, cota): # l: lista a ordenar, f: función que mapea l a los naturales, cota: sin usar, solo para igualar args de countingSort
	r = []
	for e in reversed(l):
		i = 0
		while i<len(r) and f(r[i]) < f(e):
			i = i + 1
		r.insert(i, e)
	return r 

def gT(e): # grandeza total
		return anms[e[0]]+anms[e[1]]+anms[e[2]]

def ordenarParte(p):
	def gI(e): # masima grandeza individual
		p = 0 if(anms[e[0]] > anms[e[1]]) else 1
		return anms[e[p if anms[e[p]] > anms[e[2]] else 2]]

	return sort(sort(p, gI, n), gT, 3*n - 3)

def ordenarTodoMenosApertura(parts):
	def gTP(p): # grandeza total de parte
		return sum(map(gT, p), 0)
	return sort(parts, gTP, (3*n - 3)*k)
	
def imprimirMan():
	print('Uso: '+sys.argv[0]+' <algortimo>\n     '+sys.argv[0]+' <algoritmo> <archivo_entrada>\n    Donde <algorimo> := count | merge | insert')
	sys.exit(2)	

if(len(sys.argv) == 2):
	file = sys.stdin
elif(len(sys.argv) == 3):
	file = open(sys.argv[2], 'r')
else:
	imprimirMan()

sort = {'count' : countingSort,
		'merge' : mergeSort,
		'insert' : insertionSort}.get(sys.argv[1])


n = int(file.readline()); # animales y maxima grandeza
m = int(file.readline()); # Partes incl apertura
k = int(file.readline()); # escenas por parte
nombres = str.split(file.readline(), ',');
grandezas = str.split(file.readline(), ',');
ape = [[a.strip('{}, ') for a in str.split(e.strip(), ', ')] for e in str.split(file.readline(), '}, {')]
parts = [[[a.strip('{}, ') for a in str.split(e.strip(), ', ')] for e in str.split(file.readline(), '}, {')] for i in range(m-1)]
anms = dict(zip([n.strip() for n in nombres], [int(g) for g in grandezas]))
aprcns = dict(zip([n.strip() for n in nombres], [0 for g in grandezas]))
escenaMasGrande = ape[0]
escenaMasPequena = ape[0]
promedio = 0

apertura = (ordenarParte([ordenarEscena(e) for e in ape]))
partes = ordenarTodoMenosApertura([ordenarParte([ordenarEscena(e) for e in p]) for p in parts])
srtdAprcns = countingSort(list(aprcns.items()), lambda t : t[1],2*(m-1)*k)

i, masApariciones = -1, []
while(srtdAprcns[i][1] == srtdAprcns[-1][1]):
	masApariciones.append(srtdAprcns[i][0])
	i=i-1
i, menosApariciones = 0, []
while(srtdAprcns[i][1] == srtdAprcns[0][1]):
	menosApariciones.append(srtdAprcns[i][0])
	i = i+1

def ppE(e):
	return '{} {} {}'.format(*e) 

print('{:10}{}'.format('Apertura:',ppE(apertura[0])))
for e in apertura[1:]:
	print('{:10}{}'.format('',ppE(e)))

for i in range(len(partes)):
	print('\nParte {:4}{}'.format(str(i+1)+':', ppE(partes[i][0])))
	for e in partes[i][1:]:
		print('{:10}{}'.format('',ppE(e)))

print('\nAnimales con mayor participación ({} escenas):'.format(srtdAprcns[-1][1]))
print(''.join([i+', ' for i in masApariciones]).strip(', '))

print('\nAnimales con menor participación ({} escenas):'.format(srtdAprcns[0][1]))
print(''.join([i+', ' for i in menosApariciones]).strip(', '))

print('\nEscena de menor grandeza:')
print(ppE(escenaMasPequena))

print('\nEscena de mayor grandeza:')
print(ppE(escenaMasGrande))

print('\nPromedio de grandeza de todo el espectáculo:')
print(promedio)
