import unittest

class FizzBuzz:
    def __init__(self):
        self.result = ""

    def affiche(self):
        for i in range(1, 101):
            if i % 15 == 0:
                self.result += "FrisBee"
            elif i % 3 == 0:
                self.result += "Fizz"
            elif i % 5 == 0:
                self.result += "Buzz"
            else:
                self.result += str(i)
        return self.result

    def verifier(self):
        if self.result:
            return self.result[:3], self.result[-3:]
        else:
            raise ValueError("Veuillez d'abord exécuter la méthode affiche().")

class TestFizzBuzz(unittest.TestCase):
    #def setUp(self):
        #self.instance=FizzBuzz()

    def test_affiche(self):
        fb = FizzBuzz()
        result = fb.affiche()
        self.assertTrue(result.startswith("12Fizz"))
        self.assertTrue(result.endswith("98FizzBuzz"))

    def test_verifier(self):
        fb = FizzBuzz()
        fb.affiche()
        debut, fin = fb.verifier()
        self.assertEqual(debut, "12F")
        self.assertEqual(fin, "uzz")



if __name__ == "__main__":
    unittest.main()