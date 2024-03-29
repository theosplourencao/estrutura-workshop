import pandas as pd

from app.pipeline.transform import contact_data_frames

df_1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df_2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})


def testar_a_concatenacao_da_lista_de_dataframe():
    data_frame_list = [df_1, df_2]

    df = contact_data_frames(data_frame_list)

    assert df.shape == (4, 2)
