import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import investpy

df= investpy.get_index_historical_data(index="XRPUSD", country="XRP Amerikan Doları", from_date="20/01/2020", to_date="28/09/2020")
print(df)