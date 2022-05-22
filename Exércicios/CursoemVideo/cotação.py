from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


cotação_bovespa = web.DataReader('^BVSP', data_source='yahoo', star= "01/01/2020", end= "01/01/2021")
print(cotação_bovespa)


