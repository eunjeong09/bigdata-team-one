# 대피소 지도위에 표시
import folium
import os
import webbrowser
import requests
import json
import pandas as pd
import numpy as np

df_p = pd.read_csv('./junghwa/shelter_location.csv', index_col=False)
print(df_p)
print()
print(df_p.info())
print()