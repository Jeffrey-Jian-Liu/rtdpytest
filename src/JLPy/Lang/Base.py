"""
JLPy.Lang.Base Module.

Description: Python Language Base Module for all other modules
Author     : JLPy
Version    : 2023.04.25.01
"""


class BaseClass:
    """
    .. autoclass::
    
    Lang Base Class.
    """

    def __init__(self):
        """Init Fxn"""
        self.name = None

    def print(self):
        """Print Fxn"""
        self.name = 'Main Class'
        print('This is ' + self.name)


if __name__ == '__main__':
    mc = BaseClass()
    mc.print()
