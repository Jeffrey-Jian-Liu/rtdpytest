"""Fxn Module"""

"""
Description: Python Function Test Module
Author     : JLPy
Version    : 2023.08.11.01
"""


class Fxn:
  """
  Function Test Class.
  """
  
  def __init__(self):
    """Init Fxn"""
    self.name = None
  
  def print(self) :
    """Print Fxn"""
    self.name = 'Fxn Class'
    print('This is ' + self.name)
  
  @staticmethod
  def first(**kwargs):
    def outer(fl2):
      def inner():
        if kwargs['ist']:
          print('Test!')
        if kwargs['isp']:
          print('Print!')
        fl2()
      
      return inner
    
    return outer
  
  @staticmethod
  def second(fl1):
    def inner():
      print('second')
      fl1()
    
    return inner
  
  @staticmethod
  @first(ist=False, isp=True)
  @second
  def third():
    print('hello')


if __name__ == '__main__':
  fxn = Fxn()
  fxn.third()
