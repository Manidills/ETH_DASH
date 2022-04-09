import streamlit as st
import numpy as np
import pandas as pd
from .metrics import wal
from .search import search
#add an import to Hydralit
from hydralit import HydraHeadApp



#create a wrapper class

class Wallet(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        values = ["Bored Ape Yacht Club"]
        default_ix = values.index("Bored Ape Yacht Club")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)
        st.markdown("####")
        metric = wal()
        check = search()
        
       

        

        

