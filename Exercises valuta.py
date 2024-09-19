USD_to_GBP = 0.76
USD_to_EUR = 0.90
USD_to_JPY = 143.49
USD_to_INR = 83.66
USD_to_DKK=6.70

GBP_sign = '\u00A3'
EUR_sign = '\u20AC'
JPY_sign = '\u00A5'
INR_sign = '\u20B9'
DKK_sign = 'kr'

dollars = 1000
pounds = dollars*USD_to_GBP
euros = dollars*USD_to_EUR
yen = dollars*USD_to_JPY
rupees = dollars*USD_to_INR
dkk = dollars*USD_to_DKK

print('Today, $' + str(dollars))
print('convertd to ' + GBP_sign + str(pounds))
print('convertd to' + EUR_sign + str(euros))
print('convertd to' + JPY_sign + str(yen))
print('convertd to' + INR_sign + str(rupees))
print('convertd to' + DKK_sign + str(dkk))
