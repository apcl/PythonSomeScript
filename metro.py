edadFirst = int(input('A que edad comenzaste a circular en metro?: '))
edadLast = int(input('Hasta que edad pretendes seguir haciendolo?: '))
timeMetro = int(input('Cuantos minutos circulas en metro a diario?: '))

anios = edadLast - edadFirst
total = anios * (12 * (4 * (timeMetro * 5)))
dias = (total/60)/24


print('aproximadamente circularás ' + str(total) + ' minutos en metro.')
print('que equivale a ' + str(dias) + ' días.')
