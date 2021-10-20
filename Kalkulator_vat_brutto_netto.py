stawka_vat = int(input('23' '\n'
                       '22' '\n'
                       '8'  '\n'
                       '5' '\n'
                       '7' '\n'
                       '3' '\n'
                       'Podaj stawke vat: '
                       ))

typ_kwoty = int(input('1 - netto na brutto' '\n'
                      '2 - brutto na netto' '\n'
                       'Podaj typ kwoty: '
                      ))


kwota = float(input('Podaj kwote:  '))


if stawka_vat == 3 or stawka_vat == 5 or stawka_vat == 7 or \
        stawka_vat == 8 or stawka_vat == 22 or stawka_vat == 23:
    if typ_kwoty == 1:
        brutto = kwota * (1 + stawka_vat / 100)
        print('brutto:  ' + str(brutto))
    else:
        netto = kwota / (1 + stawka_vat / 100)
        print('netto: ' + str(netto))
else:
    print('Stawka vat jest niepoprawna')







