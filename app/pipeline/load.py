from pandas import pandas as pd
import os

def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    
    """Save your generated dataframe into your output path"""
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo Salvo com Sucesso"