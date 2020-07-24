# Script to sort a list of items and determine it's item data-type.
# NOTE: The output of this script is meant to display on the CONSOLE.
import time


# Error and exception handling
class Error(Exception):
    """ Base class for other exceptions"""
    pass


class EmptyListError(Error):
    """Raised when the buffer captures nothing, i.e when no value is entered"""
    pass


class InvalidCharacterError(Error):
    """Raised when the user uses wrong delimiter """
    pass


# The merge sorting using the principle of 'DIVIDE AND CONQUER ALGORITHM'
# Merge sorting the list
if __name__ == '__main__':
    def sort_values(list):
        if len(list) > 1:
            mid = len(list) // 2
            leftList = list[:mid]
            rightList = list[mid:]

            # using recursion to break the array more
            sort_values(leftList)
            sort_values(rightList)

            i = 0  # left side counter
            j = 0  # right side counter
            k = 0  # merge counter

            # TODO: while both side has values merge the array
            while (i < len(leftList) and j < len(rightList)):
                if (leftList[i] < rightList[j]):
                    list[k] = leftList[i]
                    i += 1
                else:
                    list[k] = rightList[j]
                    j += 1
                k += 1

            # Addin values if the left side still has value
            while (i < len(leftList)):
                list[k] = leftList[i]
                i += 1
                k += 1
            # Adding values if the right side still has value
            while (j < len(rightList)):
                list[k] = rightList[j]
                j += 1
                k += 1

    # Converting and categorising each data entry

    def split(list):
        str_list = []
        int_list = []
        float_list = []
        invalid_input = []
        invalid_test = 0
        i, j, k = 0, 0, 0
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for item in list:
            if (item[0:1] in alphabets):
                str_list.append(str(item))
                i += 1
            elif ((item[0:1] in numbers) and ('.' not in item[0:])):
                try:
                    int_list.append(int(item))
                    j += 1
                except (ValueError):
                    invalid_input.append(item)
                    invalid_test += 1
            elif ('.' in item[0:]):
                try:
                    float_list.append(float(item))
                    k += 1
                except (ValueError):
                    invalid_input.append(item)
                    invalid_test += 1
        print('    ')
        print('Sorted: {}, {}, {}....'.format(str_list, int_list, float_list))
        print('Sorted "{} STRING" , "{} INTEGER", "{} FLOAT".... items'.format(i, j, k))
        print('')
        print('You had {} invalid inpust, {}'.format(
            invalid_test, invalid_input))

    # Collecting input and validating each input

    def collect_values():
        data = []
        list = []
        try:
            data.append(
                input('Please enter values separated by comma: ').split(','))
        except (EmptyListError, InvalidCharacterError):
            print('Please check the input prompt to take the proper steps!')

        for value in data:
            for items in value:
                list.append(items)
        sort_values(list)  # Calling the sort function to sort the list
        print('Merge sorting started.....')
        time.sleep(3)
        print('')
        print('Item splitting and conversion started.....')
        time.sleep(2)
        # Calling the covert function to covert each value in the list to it's
        split(list)
        # respective 'DATA-TYPE'
        print('')
        print('DONE!')

    collect_values()
else:
    print("Script can't be referenced yet!")
