#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:22:44 2026

@author: raphaelelser
"""

from utils import induktiverBlindwiderstand
from utils import kapzitiverBlindwiderstand
from utils import sqrter
import math


def test_induktiverBlindwiderstand():
    """Test induktiverBlindwiderstand"""
    assert induktiverBlindwiderstand(0, 0) == 0


def test_induktiverBlindwiderstandZwei():
    """Test induktiverBlindwiderstand"""
    Pi = math.pi
    assert induktiverBlindwiderstand(1, 1) == 2 * Pi


def test_kapzitiverBlindwiderstand():
    """Test kapzitiverBlindwiderstand"""
    assert kapzitiverBlindwiderstand(0, 0) == float("inf")


def test_kapzitiverBlindwiderstandZwei():
    """Test kapzitiverBlindwiderstand"""
    Pi = math.pi
    assert kapzitiverBlindwiderstand(1, 1) == 1 / (2 * Pi)


def test_sqrter():
    """Test sqrter"""
    assert sqrter(3, 4) == 5
