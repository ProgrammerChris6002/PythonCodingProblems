def compound_interest (principal, rate, time) :
    comp_int = ((principal) * ((1 + rate) / 100) * (time))

    return comp_int


principal = int (input ('Enter amount borrowed: '))
rate = float (input ('Enter interest rate: '))
time = float (input ('Enter time duration/interval: '))

print (compound_interest (principal, rate, time))