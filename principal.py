#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:24:57 2021

@author: ricardo
"""


from os.path import dirname
import os
from typing import List
diretorio_local = dirname(__file__)
lista_diretorios = [x for x in os.walk(diretorio_local)]


class Renomeador:
    """Pega o caminho de um diretório ou arquivo e renomeia para minúsculo.


    Descrição detalhada da classe


    Atributos
    """

    def __init__(self, diretorio_absoluto: str, caracteres_removiveis: str, caracteres_novos: str = '') -> None:
        """
        Inicializa a classe Renomeador com o nome do diretório.

        Argumentos:
            diretorio
        Returns
        -------
        None.

        """
        self.__diretorio_raiz = self.__valida_diretorio(diretorio_absoluto)
        self.__caracteres_removiveis = caracteres_removiveis
        self.__caracteres_novos = caracteres_novos

    @staticmethod
    def __valida_diretorio(diretorio_para_validar: str) -> str:
        if os.path.isdir(diretorio_para_validar):
            return diretorio_para_validar
        else:
            raise ValueError("Não foi informado um diretório válido.")

    @property
    def get_diretorio_raiz(self) -> str:
        return self.__diretorio_raiz

    @staticmethod
    def armazena_diretorios(arquivos_diretorios) -> List[str]:
        return [
            x for x in os.listdir(arquivos_diretorios) if not (
                x.startswith('.') or x.endswith(('.md', '.py', '.sh', '.cfg', '.ci'))
            )
        ]

    def lista_arquivos_renomeia(self, diretorio_pai: str) -> List[str]:
        todos_arquivos = []
        for entrada in self.armazena_diretorios(diretorio_pai):
            caminho_completo = os.path.join(diretorio_pai, entrada)
            if os.path.isdir(caminho_completo):
                self.renomeia_arquivo(diretorio_pai, entrada)
                todos_arquivos.append(self.lista_arquivos_renomeia(caminho_completo))
            else:
                self.renomeia_arquivo(diretorio_pai, entrada)
                todos_arquivos.append(caminho_completo)
        return todos_arquivos

    def renomeia_arquivo(self, diretorio_pai, nome_antigo: str) -> None:
        if len(self.get_caracteres_removiveis.strip()) == 0:
            return None
        else:
            for caracter in self.get_caracteres_removiveis():
                os.rename(
                    os.join(diretorio_pai, nome_antigo),
                    os.join(diretorio_pai, nome_antigo.replace(caracter, self.get_caracteres_novos))
                )

    @property
    def get_caracteres_removiveis(self):
        return self.__caracteres_removiveis

    @property
    def get_caracteres_novos(self):
        return self.__caracteres_novos


if __name__ == '__main__':
    # pass
    # Minuscularizador('/run/media/ricardo/samsung1tb/google_drive/projetos/renomeador/')
    # ? Precisa verificar qual SO ou estabelecer função que funcione independente do SO
    todos_arquivos = Renomeador(r"F:/google_drive/projetos/renomeador/", '&()').lista_arquivos_renomeia(
        r"F:/google_drive/projetos/renomeador/")
    # print(todos_arquivos)
