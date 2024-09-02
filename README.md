# prllrequests
Parallelize web API requests with ThreadPoolExecutor

How to use (see example.py):
- Clone the repo
- In your data analytics environment (preferably notebooks for DataFrame viewing), import the PrllRequests class from main.py
- Create a PrllRequests object and set the following paramters: (
    - REST API URL: only tested with data.cdc.gov/SODA APIs
    - Maximum rows: Approximate size of dataset, rounded up. Check API documentation to see dataset size. For example, if the dataset contains 292k rows, set the maximum rows as 300k. If dataset size is unknown, make an educated guess or set a high/safe number like 10,000,000.
    - Limit: Number of rows returned per API request)
- Call the get_request() method on the PrllRequests. This will return a Pandas dataframe.
