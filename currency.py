from forex_python.converter import CurrencyRates, CurrencyCodes


class Currency():

    def __init__(self, res):
        self.currency1 = res['convert-from'].upper()
        self.currency2 = res['convert-to'].upper()
        self.amount = res['amount']
        self.res = res
        self.c_rates = CurrencyRates()
        self.c_codes = CurrencyCodes()
        self.list = [self.currency1, self.currency2, self.amount]

    def get_conversion(self):
        '''Converts base currency to new currency, rounds 2 decimal places, adds correct symbol'''
        currency_code = self.c_codes.get_symbol(self.currency2)
        converted_currency = '{:,}'.format(round(self.c_rates.convert(self.currency1, self.currency2, float(self.amount)), 2))
        return f'{currency_code} {converted_currency}'

    def check_valid_currencies(self, code):
        '''Accepts a currency code and checks it against a list of valid codes'''
        rates = self.c_rates.get_rates('USD')
        code_list = [item for item in rates.keys()]
        code_list.append('USD')

        if self.res[code].upper() not in code_list:
            return False
        return True

    def check_valid_amount(self, amount):
        '''Accepts an amount to convert and checks that it is a number, and it is greater than 0'''
        try:
            if float(self.res[amount]) > 0:
                return True
            elif float(self.res[amount]) <= 0:    
                return False
        except:
            return False

    def validate_input(self):
        ''''''
        if not self.check_valid_currencies('convert-from'):
            self.list.remove(self.currency1)

        if not self.check_valid_currencies('convert-to'):
            self.list.remove(self.currency2)

        if not self.check_valid_amount('amount'):
            self.list.remove(self.amount)

        return self.list

        

