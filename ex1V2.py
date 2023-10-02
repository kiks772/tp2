import unittest

class FizzBuzz:
    def __init__(self):
        self.result = ""

    def affiche(self, n):  # Ajout du paramètre n
        for i in range(1, n + 1):  # Modification pour boucler jusqu'à n
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
    def test_affiche(self):
        fb = FizzBuzz()
        result = fb.affiche(100)
        self.assertTrue(result.startswith("12Fizz"))
        self.assertTrue(result.endswith("98FizzBuzz"))

    def test_verifier(self):
        fb = FizzBuzz()
        fb.affiche(100)
        debut, fin = fb.verifier()
        self.assertEqual(debut, "12F")
        self.assertEqual(fin, "uzz")

    def test_affiche_with_15(self):  # Nouveau test pour n = 15
        fb = FizzBuzz()
        result = fb.affiche(15)
        self.assertEqual(result, "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")

if __name__ == "__main__":
    unittest.main()