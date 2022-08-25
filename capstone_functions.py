def get_admission(x):
    if x['disposition'] == 'HOME':
        return 0
    else:
        return 1
        
def get_expired(x):
    if x['disposition'] == 'EXPIRED':
        return 1
    else:
        return 0
        
def look_n_load(path, describe=False):
    import pandas as pd
    df = pd.read_csv(path)
    print('\nShape:', df.shape)
    print('\nColumns:', list(df.columns))
    if describe:
        print('\n',df.describe())
    print('\nMissing proportions:\n', df.isna().sum()/len(df))
    print('\nData:\n', df.head())
    return df