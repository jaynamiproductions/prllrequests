import pandas as pd
import requests
import concurrent.futures

class PrllRequests:
    def __init__(self, url, max_rows, limit):
        self.url = url
        self.max_rows = max_rows
        self.limit = limit
    
    def get_request(self):
        offsets = list(range(0,self.max_rows, self.limit)) 
        stable = [self.limit, self.url]
        params = [[x] + stable for x in offsets]

        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(Helper.prll_requests, param) for param in params]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result is not None:
                    results.append(result)

        final_df = pd.concat(results, ignore_index=True)
        return final_df

class Helper:
    def prll_requests(param):
        final = []
        api = param[2] + f'?$limit={param[1]}&$offset={param[0]}&$order=:id'
        resp = requests.get(api).json()
        if len(resp) == 0:
            return
        df = pd.DataFrame(resp)
        final.append(df)
        return pd.concat(final)
