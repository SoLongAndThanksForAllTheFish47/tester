#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:22:44 2026

@author: raphaelelser
"""
from utils import induktiverBlindwiderstand
from utils import kapzitiverBlindwiderstand


def test_induktiverBlindwiderstand():
    """Test induktiverBlindwiderstand"""
    assert induktiverBlindwiderstand(0, 0) == 0


def test_kapzitiverBlindwiderstand():
    """Test kapzitiverBlindwiderstand"""
    assert kapzitiverBlindwiderstand(0, 0) == float('inf')
