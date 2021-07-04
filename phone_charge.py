mins = int (input('enter the minutes used: '))
texts = int (input('enter the number of texts sent: '))
def min_phonebill(mins, rate): #The function should take mins and texts as arguments, here your funct
  if mins > 20:
        extra_mins = mins - 20
        extra_rate = rate * 3
        total_paymin =  (extra_mins * extra_rate) 
        print(total_paymin)       
  else:
       total_pay = mins * rate
       return total_paymin
def text_phonebill(txts, rate2):
  if txts > 20:
        extra_txts = txts - 20
        extra_rate2 = rate2 * 2
        total_pay =  (extra_txts * extra_rate2)        
  else:
       total_pay = txts * rate
       return total_paytxts
print(50 + total_paymin + total_paytxts)
