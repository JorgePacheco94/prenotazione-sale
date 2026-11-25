"""Test per i difetti segnalati dalla segreteria."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 20))
        self.oggi = date(2026, 11, 2)
        self.martedi = date(2026, 11, 3)

    def test_prenotazioni_continue(self):
        prima = Prenotazione("A2", self.martedi, "09:00", "10:00", "Mario Rossi", 10)
        seconda = Prenotazione(
            "A2", self.martedi, "10:00", "11:00", "Luigi Bianchi", 10
        )
        self.agenda.prenota(prima, oggi=self.oggi)
        identificativo = self.agenda.prenota(seconda, oggi=self.oggi)

        self.assertIsNotNone(identificativo)
        self.assertEqual(len(self.agenda.prenotazioni), 2)

    def test_prenotazione_con_capienza_esatta(self):
        sala = Sala("R1", "Sala riunioni", 10)
        self.agenda.aggiungi_sala(sala)

        prenotazione = Prenotazione(
            "R1", self.martedi, "09:00", "10:00", "Mario Rossi", 10
        )

        identificativo = self.agenda.prenota(prenotazione, oggi=self.oggi)

        self.assertIsNotNone(identificativo)


if __name__ == "__main__":
    unittest.main()
