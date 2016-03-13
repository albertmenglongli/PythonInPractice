def getRates(refresh = False):
    if refresh is True:
        getRates.rates={}
    if getRates.rates:
        return getRates.rates
    getRates.rates['US'] = 6
    getRates.rates['EU'] = 10
    return getRates.rates

getRates.rates = {}

results = getRates()
print(results)
results = getRates()
print(results)
