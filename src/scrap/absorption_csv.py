import pandas as pd
import os

def absorption(route, merged):
    saramin = route[0]
    worknet = route[1]
    

    df1 = pd.read_csv(worknet, encoding='CP949')
    df2 = pd.read_csv(saramin, encoding='CP949')

    merged_df = pd.concat([df1, df2])
    merged_df.to_csv(merged, index=False, encoding='CP949')
     