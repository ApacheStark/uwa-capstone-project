def get_admission(x):
    if x['disposition'] in ['ADMITTED', 'TRANSFER']:
        return 1
    else:
        return 0
        
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



def work_hours(x):
    if x >= 8 and x <= 18:
        return 1 
    else:
        return 0
    
    
def length_of_stay(x, binary=False):
    if binary:
        print('Binary infers a likelhood of leaving within the next 24 hours')
        if x == 0:
            return 1
        else: 
            return 0
    else: 
        print('Going with ordered caterogical, ensure to encode using pandas.Categorical(ordered=True)')
        if x == 0:
            return 'Within the Day'
        elif x <= 7:
            return 'Within the Week'
        elif x <= 28:
            return 'Within the Month'
        else:
            return 'Beyond a Month'
        
        
def rescale_pain(x):
    try:
        x = int(x)
        if x > 100:
            return 10
        elif x > 10:
            return x/10
        elif x < 0:
            return 0
        else:
            return x
    except:
        return None
 
# assumes temp is accidentally scaled 10x when x > 200
def rescale_temp(x):
    if x > 200:
        return x/10
    else:
        return x