import unittest

class TestModelResponse(unittest.TestCase):

  def test_home(self):
    import model as m

    self.assertEqual("Hello World", m.home())
  

if __name__ == '__main__':
  unittest.main()