# add index column
import pandas as pd
path='mrt.csv'
mrt=pd.read_csv('mrt.csv',header=0)
mrt=mrt.rename_axis('index').reset_index()
store=pd.DataFrame(mrt)
store.to_csv(path,encoding='utf-8')
