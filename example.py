from main import PrllRequests

set = PrllRequests(
    url='https://data.cdc.gov/resource/bugr-bbfr.json',
    max_rows=300000,
    limit=5000,
)

df = set.get_request()
print(df)