from main import PrllRequests

def transform1(df):
    df['web_address'] = df['web_address'].apply(lambda x: x.get('url') if isinstance(x, dict) else None)
    return df
def transform2(df): 
    df['pre_screen'] = df['pre_screen'].apply(lambda x: x.get('url') if isinstance(x, dict) else None)
    return df

set = PrllRequests(
    url='https://data.cdc.gov/resource/bugr-bbfr.json',
    max_rows=300000,
    limit=5000,
    transformations=[transform1, transform2]
)

df = set.get_request()
print(df)