import pandas as pd

url = 'http://10.175.94.58:8085/project_requirement/demand_list/'

df = pd.read_html(url)
print(df)