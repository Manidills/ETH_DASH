import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import time

#add an import to Hydralit
from hydralit import HydraHeadApp
from ipfs import *

#create a wrapper class

class Discuss(HydraHeadApp):
    

#wrap all your code in this method and you should be done
    def run(self):
        values = ["Bored Ape Yacht Club"]
        default_ix = values.index("Bored Ape Yacht Club")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)


        st.markdown("##")
        placeholder = st.empty()

        

        input = placeholder.text_input('Your words', key=1)
        click_clear = st.button('clear text input', key=3)
        if click_clear:
            input = placeholder.text_input('Your words', value='', key=2)
        hash = add_ipfs(input)
        ipfs_data = get_ipfs(hash)
        ipfs_data = ''.join(filter(str.isprintable, ipfs_data))
        details = {
            "data": [ipfs_data]
        }
  
        # creating a Dataframe object 
        df = pd.read_csv('ipfs_data.csv')
        df = df.append(details, ignore_index = True)
        df.to_csv('ipfs_data.csv', index=False)

        for i in df['data']:
            st.info(i)
        

        if st.button('clear df'):
            df = df[0:0] 
            df.to_csv('ipfs_data.csv', index=False)

       
        
        
        
        

        
        
            

        