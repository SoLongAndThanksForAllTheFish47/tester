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
    if (kapazitaet > 0) and (frequenz > 0):
            creaktanz = 1 / (2 * Pi * abs(frequenz) * abs(kapazitaet))
            return creaktanz 
    
    else: return 0
    