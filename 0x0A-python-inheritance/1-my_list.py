#!/usr/bin/python3
"""Class MyList
"""


class MyList(list):
    def print_sorted(self):
        """Uses bubble sort to return a sorted list

        Args:
            self (list): unsorted list

        Returns:
            lst: (list): sorted list
        """
        # copy self to lst
        lst = self[:]
        # eliminate the null terminator
        i = len(lst) - 1
        # begin bubble sort algorithm
        # while length of lst is >= 1,
        while i >= 1:
            # set j = 0
            j = 0
            # while j < i,
            while j < i:
                # if 'number' > 'next number' in list,
                if lst[j] > lst[j + 1]:
                    # store 'number' in temp variable
                    temp = lst[j]
                    # move 'next number' to "number's" place
                    lst[j] = lst[j + 1]
                    # move 'number' in temp to "next number's" place
                    lst[j + 1] = temp
                # increment 'j' by 1
                j += 1
            # decrease 'i' by 1
            i -= 1
        print(lst)
