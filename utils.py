#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:42:37 2026

@author: raphaelelser
"""

import math


def induktiverBlindwiderstand(frequenz, induktivitaet):
    """Induktiven Blindwiderstand berechen"""
    Pi = math.pi
    lreaktanz = 2 * Pi * abs(frequenz) * abs(induktivitaet)
    return lreaktanz


def kapzitiverBlindwiderstand(frequenz, kapazitaet):
    """Kapazitiven Blindwiderstand berechen"""
    Pi = math.pi
    if (frequenz > 0) and (kapazitaet > 0):
        creaktanz = 1 / (2 * Pi * abs(frequenz) * abs(kapazitaet))
        return creaktanz 
    else:
        return float("inf")


def sqrter(resistanz, reaktanz):
    """Betrag berechnen"""
    impedanz = math.sqrt(resistanz * resistanz + reaktanz * reaktanz)
    return impedanz
