from prllrequests import PrllRequests

set = PrllRequests(
    url='https://data.cdc.gov/resource/bugr-bbfr.json',
    max_rows=300000,
    chunksize=5000,
    method='thread'
)

df = set.get_request()
print(df)