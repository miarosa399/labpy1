print ('Program untuk menentukan bilangan terbesar dan terkecil')

def pengulangan():
    print ('Masukan 3 bilangan yang diinginkan!')
    a = int(input('Masukan bilangan 1 = '))
    b = int(input('Masukan bilangan 2 = '))
    c = int(input('Masukan bilangan 3 = '))

    if a>b and a>c:
        if b>c:
            print (a, 'Terbesar',
                   c, 'Terkecil')
        else:
            print (a, 'Terbesar',
                   b, 'Terkecil')
    elif b>a and b>c:
        if a>c:
            print (b, 'Terbesar',
                   c, 'Terkecil')
        else:
            print (b, 'Terbesar',
                   a, 'Terkecil')
    else:
        if a>b:
            print (c, 'Terbesar',
                   b, 'Terkecil')
        else:
            print (c, 'Terbesar',
                   a, 'Terkecil')

    print('')
    print('Terimakasih telah menggunakan program ini.')

pengulangan()

