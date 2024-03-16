"""Biblioteca para concatenar os dataframes."""

from typing import List

import pandas as pd


def contact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Transform your dataframe list into one unique dataframe.

    _summary_

    Args:
        data_frame_list (List[pd.DataFrame]): _description_

    Returns:
        pd.DataFrame: _description_
    """
    return pd.concat(data_frame_list, ignore_index=True)
