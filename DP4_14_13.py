pocet_radku=int(input('Zadej pocet radku: '))
pocet_sloupcu=int(input('Zadej pocet sloupcu: '))
for radek in range(pocet_radku):
    if radek==0 or radek==pocet_radku-1:
        for sloupec in range(pocet_sloupcu):
            print('X', end=' ')
        print('')
    else:
        print('X', end=' ')
        for mezery in range(pocet_sloupcu-2):
            print(' ', end=' ')
        print('X')
