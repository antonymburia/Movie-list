import unittest
from models import movie
'''
we import both Unittest and movie modules

'''
Movie = movie.Movie

'''We get the movie class
'''

class MovieTest(unittest.TestCase):
  '''
  
  Test class to test movie class behavior
  '''
  def setUp(self):
    '''
    set up method to run before test
    '''
    self.new_movie = Movie(1234,'python is crazy', 'A new python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

  def test_instance(self):
    '''
    test case that uses isinstance function to check if 
    the self.movie is an instance of the class
    
    '''
    self.assertTrue(isinstance(self.new_movie,Movie))

if __name__== '__main__':
  unittest.main()

