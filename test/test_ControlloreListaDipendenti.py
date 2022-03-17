from unittest import TestCase

from listadipendenti.controllore.ControlloreListaDipendenti import ControlloreListaDipendenti
from dipendente.model.Dipendente import Dipendente
from listadipendenti.model.ListaDipendenti import ListaDipendenti

class TestControlloreListaDipendenti(TestCase):
    def setUp(self):
        self.lista = ListaDipendenti()

    def test_aggiungi_dipendente(self):
        self.test_dip = Dipendente("Marisonia", "Ferrandino", "19/08/1999", "San Giovanni Rotondo", "s1093762@stidenti.univpm.it", "1234567890", "segretaria")
        self.lista.aggiungi_dipendente(self.test_dip)
        self.assertIsNotNone(self.test_dip, "Non esiste")

    def test_controlla_dipendente(self):
        self.test_dip1 = Dipendente("Marisonia", "Ferrandino", "19/08/1999", "San Giovanni Rotondo",
                                   "s1093762@stidenti.univpm.it", "1234567890", "segretaria")
        self.test_dip2 = Dipendente("Marisonia", "Ferrandino", "19/08/1999", "San Giovanni Rotondo",
                                   "s1093762@stidenti.univpm.it", "1234567890", "segretaria")
        self.assertNotEqual(self.test_dip1, self.test_dip2, "Dipendente già esistente")

    def test_lista_vuota(self):
        self.test_dip3 = Dipendente("Marisonia", "Ferrandino", "19/08/1999", "San Giovanni Rotondo",
                                    "s1093762@stidenti.univpm.it", "1234567890", "segretaria")
        self.lista.aggiungi_dipendente(self.test_dip3)
        self.assertNotEmpty(self.lista)

    def test_elimina_dipendente(self):
        self.test_dip4 = Dipendente("Marisonia", "Ferrandino", "19/08/1999", "San Giovanni Rotondo",
                                   "s1093762@stidenti.univpm.it", "1234567890", "segretaria")
        self.lista.aggiungi_dipendente(self.test_dip4)
        self.lista.rimuovi_dipendente("Marisonia")
        self.assertEmpty(self.lista.get_lista_dipendenti())

    def assertNotEmpty(self, obj):
        self.assertTrue(obj)

    def assertEmpty(self, obj):
        self.assertFalse(obj)

