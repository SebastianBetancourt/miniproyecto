# miniproyecto
Theoric and experimental analysis on a variation of a sorting algorithm, 
determining complexity and input dependency

# Planteamiento
Para ordenar los animales dentro de una escena, el script utiliza un
algoritmo de ordenamiento *naive* que aprovechando el tamaño fijo de la
escena compara la grandeza del primer animal con la del segundo, y la
del más pequeño con la del tercero, y de acuerdo al resultado puede
necesitar comparar el tercero con el primero para concluir cual es el
orden de los tres animales. Como se realizan a lo mucho 3 comparaciones,
ordenar los animales en una escena requiere $3\in O(1)$ pasos.

![Table of complexities per task](graphs/disse.png?raw=true "Complexity per tast")

# Experimento
Estas pruebas fueron ejecutadas en Python 3.7.7 (default, Mar 10 2020,
15:43:33) \[Clang 11.0.0 (clang-1100.0.33.17)\] en Windows 10 con un
Intel Core i7-7700HQ a 2.8ghz y 16gb de RAM.

En PowerShell el comando
`Measure-Command {python gen.py 5000 10 10 | python proy.py merge}` mide
el tiempo de ejecución de generación y solución un problema con
$n=5000$, $m=10$ y $n=10$, con MergeSort, por ejemplo. La metología
consisitió en variar estos tres parámetros con los tres algoritmos y
registrar el tiempo de ejecución. Como las condiciones para $n$, $m$ y
$k$ propuestas en el enunciado no permiten ver con claridad cambios
notables en el tiempo de ejecución, jugamos con valores mucho más
grandes.

Para replicar el experimento y revisar el script, refiérase al documento
`leeme.pdf` que contiene instrucciones detalladas de uso.

## Resultados
Los datos brutos fueron registrados en la hoja de Excel `datos.xlsx` que
se encuentra adjunta. Cuando se varió $k$ y $m$, los tiempos de cómputo
crecieron inúsitadamente, por lo que se tuvieron que suspender las
pruebas para $k > 3000$ y $m > 3000$. Por curiosidad, dejamos correr una
prueba con $k=10000,\, m=n=10$, y el tiempo de ejecución fue de 2425983
ms (más de 40 min). También hicimos una prueba con $m=10000, \, k=n=10$
y se demoró 2783891 ms (más de 45 min).

A continuación se muestran las gráficas comparando el rendimiento de los
algoritmos variando $n$, $m$ y $k$.

![Execution time](graphs/graph1.png?raw=true "execution time")

![Execution time](graphs/graph2.png?raw=true "execution time")

## Conclusiones

Las graficas apoyan la hipótesis descrita en el análisis teórico: El
tiempo de ejecución depende de $m$ y $k$ más que de $n$. En las pruebas
variando $n$ para valores $n < mk$, el tiempo realmente se mantiene
constante, es solo para valores grandes de $n$ que el tiempo empieza a
depender de $n$. Usamos CountingSort para ordenar las grandezas en
`aprcns`, Y este es el que más afectado se ve por el crecimiento de $n$
(pues su cota depende directamente), mientras que los otros
ordenamientos solo dependen de $m$ y $k$ que siempre son iguales a $10$.
El problema yace en la decisión de usar *siempre* CountingSort para
ordenar , que termina demorándo más que los otros pasos. Por eso en $n$
vs. tiempo de ejecución las tres variantes del script se comportan
igual.

Hay una diferencia clara en las graficas que varian $n$ con respecto a
las que varían con $k$ y $m$. En las últimas sí se nota una diferencia
de acuerdo a algoritmo seleccionado. Aunque no describen tan claramente
como quisieramos las funciones representativas $y=x$ o $y=x\log x$, sí
hay una clara diferencia y una tendencia a seguir los valores descritos
por estas funciones. Un buen ejercicio sería realizar una ajuste y mirar
la efectividad con alguna prueba estadística como Kolmogórov-Smirnov.

Para dar una respuesta directa a la pregunta "¿Cuál es la compejidad del
algoritmo?\", los resultados apoyan que con `insert` es $O((mk)^2)$, con
`merge` es $O(mk\log(mk))$, y con `count` es $O(mk)$. Ahora, para
cumplir con los requerimientos del enunciado, sabemos que $m < 60$ y que
$k <n$, entonces $Sort(mk) = Sort(60n) = Sort(n)$. Por lo tanto la
complejidad también `insert` es $O(n^2)$, con `merge` es $O(n\log n)$, y
con `count` es $O(n)$. Sin embargo creemos $Sort(mk)$ es una cota más
justa.
