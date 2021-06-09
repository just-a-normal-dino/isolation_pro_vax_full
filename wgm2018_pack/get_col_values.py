from datas import wgm_bool

def get_col_values(keys, df=wgm_bool):
    cols = list()

    if type(keys) == type("abc"):
        keys = [keys]

    for key in keys:
        col = df[key].values
        cols.append(col)

    if len(cols) == 1:
        cols = cols[0]

    return cols