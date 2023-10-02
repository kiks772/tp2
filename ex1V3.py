import unittest

class FizzBuzz:
    def __init__(self):
        self.result = ""

    def affiche(self, n1, n2):  # Ajout des paramètres n1 et n2
        for i in range(n1, n2 + 1):  # Modification pour boucler de n1 à n2
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
        result = fb.affiche(1, 100)
        self.assertTrue(result.startswith("12Fizz"))
        self.assertTrue(result.endswith("98FizzBuzz"))

    def test_verifier(self):
        fb = FizzBuzz()
        fb.affiche(1, 100)
        debut, fin = fb.verifier()
        self.assertEqual(debut, "12F")
        self.assertEqual(fin, "uzz")

    def test_affiche_with_5_10(self):  # Nouveau test pour n1 = 5, n2 = 10
        fb = FizzBuzz()
        result = fb.affiche(5, 10)
        self.assertEqual(result, "BuzzFizz78FizzBuzz")

    def test_affiche_with_10_16(self):  # Nouveau test pour n1 = 10, n2 = 16
        fb = FizzBuzz()
        result = fb.affiche(10, 16)
        self.assertEqual(result, "Buzz11Fizz1314FrisBee16")


if __name__ == "__main__":
    unittest.main()