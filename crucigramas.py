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

        # Horizontales
        for i, palabra in enumerate(horizontales):

            dominio = set()

            for fila in range(n):
                for col in range(m - len(palabra) + 1):
                    dominio.add((fila, col))

            self.D[f"H{i}"] = dominio

        # Verticales
        for i, palabra in enumerate(verticales):

            dominio = set()

            for fila in range(n - len(palabra) + 1):
                for col in range(m):
                    dominio.add((fila, col))

            self.D[f"V{i}"] = dominio