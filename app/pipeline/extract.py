"""Esse é o módulo de extração de dados."""

import glob  # biblioteca para listar arquivos
import os  # para manipular arquivos e pastas
from typing import List

import pandas as pd

path = "data/input"


def extract_from_excel(path: str) -> list[pd.DataFrame]:
    """
    Fazendo uma função para ler os arquivos de uma pasta data/input e retornar uma lista de dataframes.

    agrs: input path (str): caminho da pasta com os arquivos.

    return: lista de dataframes.


    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
