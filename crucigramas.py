#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csps
import time


class Crucigrama(csps.ProblemaCSP):

    def __init__(self, verticales, horizontales, n=10, m=10):

        self.verticales = verticales
        self.horizontales = horizontales

        self.n = n
        self.m = m

        self.X = set()

        # Variables horizontales
        for i in range(len(horizontales)):
            self.X.add(f"H{i}")

        # Variables verticales
        for i in range(len(verticales)):
            self.X.add(f"V{i}")

        # Dominios
        self.D = {}

        # Vecinos
        self.N = {}

        for x in self.X:
            self.N[x] = self.X.difference({x})

    def restriccion_binaria(self, xi, vi, xj, vj):
        pass