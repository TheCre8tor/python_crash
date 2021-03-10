# The zip function zip multiful data structure together

provider = ['mtn', 'airtel', 'glo', 'globalcomms', 'visa']
recharge_card = [50, 150, 450, 70, 40]
time = ('5:00', '3:30', '2:20', '6:00', '1:10')

zipper = list(zip(provider, recharge_card, time))
print(zipper)
 