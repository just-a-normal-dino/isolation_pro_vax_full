import numpy as np

def clean_df(df_in):
    threshold = 8
    for quest in df_in.columns:
        serie = df_in[quest]
        try:
            serie[serie == ' '] = np.nan
            serie[serie == ''] = np.nan
        except:
            pass
        serie = serie.astype(float)
        serie[serie > threshold] = np.nan
        df_in[quest] = serie

    # drop the nan
    df_in = df_in.dropna(axis=0)

    return df_in