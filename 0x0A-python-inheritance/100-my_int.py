#!/usr/bin/python3
"""MyInt rebel class.
"""


class MyInt(int):
    """MyInt rebel class that inherits from int its attributes and
    methods but inverts '==' and '!='
    """
    def __eq__(self, __value: object) -> bool:
        """__eq__ will be inverted to return __ne__"""
        return super().__ne__(__value)
    
    def __ne__(self, __value: object) -> bool:
        """__ne__ will be inverted to return __eq__"""
        return super().__eq__(__value)
