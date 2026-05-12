##
## EPITECH PROJECT, 2026
## info_utilisateur
## File description:
## info_utilisateur
##

import pandas as pd # panda for open a csv and extract the data for file and data manipulation
import matplotlib.pyplot as pl # matplotlib to create visualisation via graphs
import pydeck as pdk
import streamlit as st
import numpy as np
import re
from src.tools import *


def render(df):
	st.write("## Page U")
	df_departure_station = df.dropna(subset=['Departure station'])
	stations = np.concatenate([["Toute direction"], df_departure_station['Departure station'].unique()])
	col1, col2 = st.columns(2)
	departure_station = col1.selectbox("Gare de dapart:",stations,)
	arrival_station = col2.selectbox("Gare d'arriver:",stations,)
	graph_departure_arrival_station(df, departure_station, arrival_station, 2022)