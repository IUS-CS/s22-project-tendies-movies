import os
import re
from MovieClass import MovieClass
from imdb import Cinemagoer
import unittest


movie = MovieClass()
movie.import_top250()
movie.randomize()

def findMovie(i):
    if i in movie.genres():
        return 0
    else:
        movie.randomize()
        return findMovie(i)

class TestFindMovie(unittest.TestCase):

    def testActionSuccess(self):
        findMovie('Action')
        error = "Action is not found in movie genres."
        self.assertIn('Action',movie.genres(), error)

    def testAdventureSuccess(self):
        findMovie('Adventure')
        error = "Adventure is not found in movie genres."
        self.assertIn('Adventure',movie.genres(), error)
    
    def testAnimationSuccess(self):
        findMovie('Animation')
        error = "Animation is not found in movie genres."
        self.assertIn('Animation',movie.genres(), error)

    def testBiographySuccess(self):
        findMovie('Biography')
        error = "Biography is not found in movie genres."
        self.assertIn('Biography',movie.genres(), error)

    def testComedySuccess(self):
        findMovie('Comedy')
        error = "Comedy is not found in movie genres."
        self.assertIn('Comedy',movie.genres(), error)

    def testCrimeSuccess(self):
        findMovie('Crime')
        error = "Crime is not found in movie genres."
        self.assertIn('Crime',movie.genres(), error)

    def testDramaSuccess(self):
        findMovie('Drama')
        error = "Drama is not found in movie genres."
        self.assertIn('Drama',movie.genres(), error)

    def testFamilySuccess(self):
        findMovie('Family')
        error = "Family is not found in movie genres."
        self.assertIn('Family',movie.genres(), error)

    def testFantasySuccess(self):
        findMovie('Fantasy')
        error = "Fantasy is not found in movie genres."
        self.assertIn('Fantasy',movie.genres(), error)

    def testNoirSuccess(self):
        findMovie('Film-Noir')
        error = "Film-Noir is not found in movie genres."
        self.assertIn('Film-Noir',movie.genres(), error)

    def testHistorySuccess(self):
        findMovie('History')
        error = "History is not found in movie genres."
        self.assertIn('History',movie.genres(), error)

    def testHorrorSuccess(self):
        findMovie('Horror')
        error = "Horror is not found in movie genres."
        self.assertIn('Horror',movie.genres(), error)

    def testMysterySuccess(self):
        findMovie('Mystery')
        error = "Mystery is not found in movie genres."
        self.assertIn('Mystery',movie.genres(), error)

    def testRomanceSuccess(self):
        findMovie('Romance')
        error = "Romance is not found in movie genres."
        self.assertIn('Romance',movie.genres(), error)

    def testScifiSuccess(self):
        findMovie('Sci-Fi')
        error = "Sci-Fi is not found in movie genres."
        self.assertIn('Sci-Fi',movie.genres(), error)

    def testThirllerSuccess(self):
        findMovie('Thriller')
        error = "Thriller is not found in movie genres."
        self.assertIn('Thriller',movie.genres(), error)

    def testWarSuccess(self):
        findMovie('War')
        error = "War is not found in movie genres."
        self.assertIn('War',movie.genres(), error)

    def testWesternSuccess(self):
        findMovie('Western')
        error = "Western is not found in movie genres."
        self.assertIn('Western',movie.genres(), error)

if __name__ == '__main__':
    unittest.main()