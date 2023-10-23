"""
Base module for Python language testing.

This module is the base module for all other objects @ JLPy.Lang namespace.
::

   Author  : JLPy
   Version : 2023.10.23.02

.. note::
   This is the note.
"""


class BaseClass:
  """
  Base Class for all other object.
  
  This is the base Class for all other objects @ JLPy.Lang namespace.
  
  Properties:
  -----------
  
  Methods:
  --------
  """
  
  def __init__(self):
    """Init Fxn."""
    ...
  
  def test(self):
    """
    Test fxn.
    
    Test the Sphinx docstring.
    
    """
    ...
  
  def print(self):
    """
    Print class name method.
    
    This function is the Print the debug info for the class.
    """
    obj = type(self)
    print(f'This is an instance of the {obj.__name__} class.')


if __name__ == '__main__':
  mc = BaseClass()
  mc.print()
