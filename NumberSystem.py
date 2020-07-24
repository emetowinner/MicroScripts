import time

class NumberSystem():

    def __init__(self):

        self.hex_value_pairs = {'A': 10, 'B': 11,
                                'C': 12, 'D': 13, 'E': 14, 'F': 15}
        self.value_digits = []
        self.base_10_value = []

    def converter(self, value, fro, to):

        if to == 10:
            self.value = str(value)

            for digit_str in self.value:
                if digit_str.upper() in self.hex_value_pairs.keys():
                    self.value_digits.append(
                        self.hex_value_pairs[digit_str.upper()])
                else:
                    self.value_digits.append(int(digit_str))
            counter = len(self.value_digits)-1
            for digit_int in self.value_digits:
                self.base_10_value.append(digit_int*(fro**counter))
                counter -= 1

            print(
                f'Converted {value} from base {fro} to {to} which is: {sum(self.base_10_value)}')

        elif to != 10:
            NumberSystem.others(self, value, fro, to)

        return sum(self.base_10_value)

    def others(self, value, fro, to):
        print(f'First convert {value} from base {fro} to {10}')
        base = NumberSystem.converter(self, value, fro, 10)
        checker = 0
        base_digits = []
        base_value = ''
        print(f'Converting {value} from base {fro} to {to}......')
        while base:
            breaker = str(base - to)
            if '-' in breaker:
                base_digits.append(base)
                break

            base_digits.append(base % to)
            base = base//to
        for char in base_digits:
            for key, pair in self.hex_value_pairs.items():
                if str(char) == str(pair):
                    print('Hexadecimal value has been encountered!')
                    time.sleep(1)
                    print('*'*5)
                    time.sleep(1)
                    print('*'*5)
                    print("Done pairing hexadecimal value to it's equivalent")
                    base_value = base_value + key
                    break
                else:
                    pass
            if char not in self.hex_value_pairs.values():
                base_value = base_value + str(char)
        time.sleep(3)
        print(f'Done converting {value} from base {fro} to {to}!')
        print('  ')
        if base_value.isnumeric():
            base_value = base_value[::-1]
            print(
                f'Converted {value} from base {fro} to {to} which is: {base_value}')
        else:
            base_value = base_value[::-1]
            print(
                f'Converted {value} from base {fro} to {to} which is: {base_value}')

convert = NumberSystem()
convert.converter('66d', 16, 8)