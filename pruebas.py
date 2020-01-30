import unittest
from Pension import Persona


class pensionTest(unittest.TestCase):
    def testVaron60anos750cotizaciones(self):
        self.persona = Persona("1/1/1960",'M',750,0)
        self.assertTrue(self.persona._EsPensionado())


if __name__ == '__main__':
    unittest.main()    