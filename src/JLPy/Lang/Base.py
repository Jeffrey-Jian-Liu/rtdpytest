"""
JLPy.Lang.Base Module.

Description: Python Language Base Module for all other modules
Author     : JLPy
Version    : 2023.04.25.01
"""


class BaseClass:
  """
  Lang Base Class.
  """
  
  def __init__(self):
    """Init Fxn."""
    self.name = None
  
  def test(self):
    """
    Test fxn.
    
    Test the Sphinx docstring.
    :return:
    """
    ...
  
  def print(self):
    """
    Print Fxn.
    
    Print the debug info for the class.
    """
    self.name = 'Main Class'
    print('This is ' + self.name)


if __name__ == '__main__':
  mc = BaseClass()
  mc.print()
