from hydralit import HydraHeadApp
import streamlit as st
from PIL import Image
from hydralit import HydraHeadApp
from metric import polygon_metric,chicken_metric
from predict import predict

class Collection(HydraHeadApp):

    def run(self):
        values = ["Bored Ape Yacht Club"]
        default_ix = values.index("Bored Ape Yacht Club")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)

        # img = Image.open("./images/chicken.JPG")
        # st.image(img,  caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

        st.markdown('#') 

        total_volume,daily_avg,weekly_avg = chicken_metric('./data/Bored_volume.csv')

        col1, col2, col3 = st.columns((3,3,3))
        col1.metric(label = "Total Volume", value = '$' + str(total_volume) )
        col2.metric(label = "Average Daily Volume", value = '$' + str(daily_avg) )
        col3.metric(label = "Average Weekly Volume", value = '$' + str(weekly_avg))

        st.markdown('#') 

        file_path_ = './data/Bored_volume.csv'
        split_percent_ = 0.70
        predict_model_ =  './data/Bored_volume.h5'
        volume_chart = predict(file_path_,split_percent_,predict_model_)
        st.markdown("<h4 style='text-align: center; color: white;'>BAYC Volume Prediction </h4>", unsafe_allow_html=True)
        st.altair_chart(volume_chart)

        st.info("BAYC Volume prediction")
        st.write("""
        BAYC Volume predictions over the period of time.
        """)

        
        st.markdown('#') 
        file_path = './data/Bored_wallet.csv'
        split_percent = 0.70
        predict_model =  './data/Bored_wallet.h5'
        wallet_chart = predict(file_path,split_percent,predict_model)

        st.markdown("<h4 style='text-align: center; color: white;'>BAYC Wallet Prediction </h4>", unsafe_allow_html=True)
        st.altair_chart(wallet_chart)  
        
        st.info("BAYC Wallet prediction")
        st.write("""
        BAYC Wallet predictions over the period of time.
        """)

