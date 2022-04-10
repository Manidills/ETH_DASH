from hydralit import HydraHeadApp
import streamlit as st
from PIL import Image
from hydralit import HydraHeadApp
from metric import polygon_metric
from predict import predict

class Home(HydraHeadApp):
    def run(self):
        # img = Image.open("images/eth.png")
        # st.image(img,  caption=None, width=1000, use_column_width=600, clamp=False, channels="RGB", output_format="auto")

        st.markdown('#') 

        total_volume,daily_avg,weekly_avg = polygon_metric('./data/ETH_volume.csv')

        col1, col2, col3 = st.columns((3,3,3))
        col1.metric(label = "Total Volume", value = '$' + str(total_volume) )
        col2.metric(label = "Average Daily Volume", value = '$'+ str(daily_avg) )
        col3.metric(label = "Average Weekly Volume", value = '$' + str(weekly_avg))

        st.markdown('#') 
        st.markdown("<h4 style='text-align: center; color: white;'>ETH NFT GROWTH PREDICTIONS </h4>", unsafe_allow_html=True)

        file_path_ = './data/ETH_volume.csv'
        split_percent_ = 0.95
        predict_model_ =  './data/ETH_volume.h5'
        volume_chart = predict(file_path_,split_percent_,predict_model_)

        st.altair_chart(volume_chart)  

        st.info("ETH Volume prediction")
        st.write("""
         Above chart shows the Growth of NFTs volume on ETH over the period and prediction using our AI MODEL
        """)



        st.markdown('#')
        st.markdown("<h4 style='text-align: center; color: white;'>ETH WALLETS GROWTH PREDICTIONS </h4>", unsafe_allow_html=True)  
        file_path = './data/ETH_wallet.csv'
        split_percent = 0.90
        predict_model =  './data/ETH_wallet.h5'
        wallet_chart = predict(file_path,split_percent,predict_model)
        
        st.altair_chart(wallet_chart)  
        

        st.info("ETH Wallet prediction")
        st.write("""
        Above chart shows the Growth of user wallets on ETH over the period and prediction using our AI MODEL
        """)

