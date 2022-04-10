from hydralit import HydraApp
import streamlit as st
#from streamlit.scriptrunner import get_script_run_ctx
from streamlit.scriptrunner.script_run_context import get_script_run_ctx
from streamlit.scriptrunner import get_script_run_ctx
from PIL import Image
from stats import Stats
from home import Home
from tokens.toks import Token
from wallets.wallets import Wallet
from collection import Collection
from duplicate import Duplicate
from Discuss import Discuss
#ckey_eb29565e970e4b46930dca374df

st.set_page_config(
    page_title="ETH Global hack",
    layout="wide"
)

#title_image = Image.open("/home/dills/Music/ethglobal/images/CryptoMode-Polygon-DeFi.jpg")
new_title = '<p style="font-family:Bodoni; text-align: center; color:#FEB440; font-size: 60px;">NFT DATA HOUSE</p>'
st.markdown(new_title, unsafe_allow_html=True)


if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!

    app = HydraApp(title='ETH Global hack')
    
    #add all your application classes here
    app.add_app("Home", app=Home(),is_home=True)
    app.add_app("Collection", app = Collection())
    app.add_app("Token", app=Token())
    app.add_app("Wallet", app=Wallet())
    app.add_app("Duplicate & Forgery", app=Duplicate())
    app.add_app("Stats", app=Stats())
    app.add_app("Discuss", app=Discuss())
    
    

    #run the whole lot
    app.run()