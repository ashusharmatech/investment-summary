import pandas as pd

from Constants import LIMIT_ROWS


def covertToDataframe(data, columns):
    df = pd.json_normalize(data)
    df = df[columns]
    return df

def sort(df, sort_details):
    if(sort_details['column'] is not None):
        df[sort_details['column']] = df[sort_details['column']].astype(float)
        df = df.sort_values(sort_details['column'],  ascending=sort_details['order'])
    return df


def finalizeDataframe(df, rename_colmns):
    df = df.head(LIMIT_ROWS)
    df = df.rename(columns=rename_colmns)
    df.rename_axis(None)
    df.reset_index()
    return df


def convert(data, columns, rename_colmns, sort_details):
    df = covertToDataframe(data, columns)
    df = sort(df, sort_details)
    df = finalizeDataframe(df, rename_colmns)
    return df
