#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:24:57 2021

@author: ricardo
"""


from os.path import dirname, abspath
import os
print(dirname(abspath(__file__)))
print(dirname(__file__))
print(abspath(__file__))
diretorio_local = dirname(__file__)
lista_diretorios = [x for x in os.walk(diretorio_local)]


class Minuscularizador:
    """Pega o caminho de um diretório ou arquivo e renomeia para minúsculo.


    Descrição detalhada da classe


    Atributos
    """

    def __init__(self, diretorio) -> None:
        """
        Inicializa a classe Minuscularizador com o nome do diretório.

        Argumentos:
            diretorio
        Returns
        -------
        None.

        """
        self.diretorio = self.__valida_diretorio(diretorio)

    @staticmethod
    def __valida_diretorio(diretorio_para_validar: str) -> str:
        if os.path.isdir(diretorio_para_validar):
            return diretorio_para_validar
        else:
            raise ValueError("Não foi informado um diretório válido.")


if __name__ == '__main__':
    Minuscularizador('/run/media/ricardo/samsung1tb/google_drive/projetos/renomeador/')
