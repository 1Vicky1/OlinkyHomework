for radek in range(5):
    if radek==0 or radek==4:
        for sloupec in range(6):
            print('X', end=' ')
        print('')
    else:
        print('X', end=' ')
        for mezery in range(4):
            print(' ', end=' ')
        print('X')
