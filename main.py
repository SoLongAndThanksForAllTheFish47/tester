#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:41:06 2026

@author: raphaelelser

Diesese Programm berechnet den Betrag der Impedanz einer R,L,C Serienschaltung.
"""

from utils import induktiverBlindwiderstand
from utils import kapzitiverBlindwiderstand
from utils import sqrter


def main():
    """Hauptprogramm"""

    print("_Dieses Programm berechnet die Impedanz einer R,L,C Serienschaltung_")

    frequenz = float(input("Frequenz in Hz: "))
    induktivitaet = float(input("Induktivität in Henry: "))
    kapazitaet = float(input("Kapazität in Farad: "))
    resistanz = float(input("Resistanz in Ohm: "))

    # Impedanz berechen
    reaktanz = abs(
        induktiverBlindwiderstand(frequenz, induktivitaet)
        - kapzitiverBlindwiderstand(frequenz, kapazitaet)
    )
    impedanz = sqrter(resistanz, reaktanz)
    # Ergebnisse ausgeben
    print("Die Impedanz beträgt:", impedanz, "Ohm")


if __name__ == "__main__":
    main()
