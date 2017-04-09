pocet_radku=int(input('Zadej pocet radku/pocet cisel pro ktere chces vypsat nasobilku: '))
pocet_sloupcu=int(input('Zadej pocet sloupcu/delku nasobilky: '))
for cinitel_radky in range(pocet_radku):
    for cinitel_sloupce in range(pocet_sloupcu):
        print(cinitel_radky*cinitel_sloupce, end=' ')
    print('')
