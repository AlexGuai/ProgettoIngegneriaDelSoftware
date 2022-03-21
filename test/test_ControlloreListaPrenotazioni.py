from unittest import TestCase

from prenotazione.model.Prenotazione import Prenotazione
from listaprenotazioni.controllore.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni


class TestControlloreListaPrenotazioni(TestCase):
    def setUp(self):
        self.lista = ListaPrenotazioni()
        self.controller = ControlloreListaPrenotazioni()

    def test_aggiungi_prenotazione(self):
        self.test_prenotaz = Prenotazione("mariorossi", "Mario Rossi", "Seconda Corsia", "12/12/2022")
        self.lista.aggiungi_prenotazione(self.test_prenotaz)
        self.assertIsNotNone(self.test_prenotaz)

    def test_lista_vuota(self):
        self.test_prenotaz1 = Prenotazione("mariorossi", "Mario Rossi", "Seconda Corsia", "12/12/2022")
        self.controller.aggiungi_prenotazione(self.test_prenotaz1)
        self.assertNotEmpty(self.controller)

    def test_elimina_prenotazione(self):
        self.test_prenotaz2 = Prenotazione("mariorossi", "Mario Rossi", "Seconda Corsia", "12/12/2022")
        print(
            "Prenotazione per " + self.test_prenotaz2.cliente + " in " + self.test_prenotaz2.servizio + " del " + self.test_prenotaz2.data + " è stata cancellata")
        self.controller.aggiungi_prenotazione(self.test_prenotaz2)
        self.controller.elimina_prenotazione_by_id(self.test_prenotaz2)
        self.assertEmpty(self.lista.get_lista_prenotazioni())

    def assertNotEmpty(self, obj):
        self.assertTrue(obj)

    def assertEmpty(self, obj):
        self.assertFalse(obj)
