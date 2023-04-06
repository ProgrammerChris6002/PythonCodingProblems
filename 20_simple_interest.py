def simple_interest (principal, rate, time) :
    simp_int = (((principal) * (rate) * (time)) / 100)

    return simp_int


principal = int (input ('Enter how much borrowed: '))
rate = float (input ('Enter interest rate: '))
time = float (input ('Enter time interval: '))

print (simple_interest (principal, rate, time))