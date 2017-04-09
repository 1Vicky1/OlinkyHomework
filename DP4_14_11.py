pocet_radku=int(input('Zadej pocet radku: '))
for radek in range(pocet_radku):
    for sloupec in range(radek+1):
        print('X', end=' ')
    print('')
