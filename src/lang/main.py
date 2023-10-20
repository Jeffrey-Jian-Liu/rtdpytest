"""
Python Language Test Main Module.

Description: Python Language Test
Author     : Jeffrey Liu
Version    : 2023.04.25.01
"""


class Main:
    """Main Class"""

    def __init__(self):
        """Init Fxn"""
        self.name = None

    def print(self):
        """Print Fxn"""
        self.name = 'Main Class'
        print('This is ' + self.name)


if __name__ == '__main__':
    mc = Main()
    mc.print()
