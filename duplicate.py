from hydralit import HydraHeadApp
import streamlit as st
from PIL import Image
import requests
import json
from hydralit import HydraHeadApp
from metric import polygon_metric
from predict import predict
from load import load_meta, meta_load, load

class Duplicate(HydraHeadApp):
    def run(self):
        values = ["Bored Ape Yacht Club"]
        default_ix = values.index("Bored Ape Yacht Club")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)
        input = st.text_input("Enter Token Id ",)
        if input:
            url = "https://api.nftport.xyz/v0/duplicates/tokens"
            payload = {
                "chain": 'ethereum',
                "contract_address": '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d',
                "token_id": str(input),
                "page_number": 1,
                "page_size": 5,
                "threshold": 0.95
            }

            headers = {
                'Content-Type': "application/json",
                'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
                }

            response = requests.request("POST", url, data=json.dumps(payload), headers=headers, json=True)

            data = response.json()
            #print(data)
            if data['response'] == 'OK':
                data = data['similar_nfts']
                req = []
                for i in range(len(data)):
                    if  ((len(data[i]['token_id']) < 6) and ( data[i]['token_id'] != str(input) )):
                        req.append(data[i])
                if not req:
                    top_2 = None
                req = [k for j, k in enumerate(req) if k not in req[j + 1:]]
                top_2 = [{"image" : i['cached_file_url'], 'token_id': i['token_id'], 'metadata': i['metadata']} for i in req ]
                top_2 = top_2[:2]
            else:
                st.warning("something went wrong")

            co1, co2 = st.columns((3,3))
            metadata= meta_load(str(input))

            with co1:
                st.image(metadata['cached_file_url'],width=400,)
            with co2:
                name = metadata['file_url']
                token_id = metadata['token_id']
                att = metadata['metadata']['attributes']
                minted = metadata['mint_date']
                st.text(f'Token_id = {token_id}')
                st.text(f'Minted_date = {minted}')
                st.text(f'Metadata_url = {name}')
                st.info(f'Attributes = {att}')
            
            st.markdown("####")
            st.warning("Near Duplicates")
            col1,col2 = st.columns((3,3))
            if not top_2:
                st.info("Not Found")
            else:
                with col1:
                    
                    st.image(top_2[0]['image'],width=400,)
                    st.info(f"Token Id = {top_2[0]['token_id']}")
                    st.success(f"Metadata = {top_2[0]['metadata']}")
                    st.write(f"check out this [link](https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/{top_2[0]['token_id']})")

                with col2:
                   
                    st.image(top_2[1]['image'],width=400)
                    st.info(f"Token Id = {top_2[1]['token_id']}")
                    st.success(f"Metadata = {top_2[1]['metadata']}")
                    st.write(f"check out this [link](https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/{top_2[1]['token_id']})")
            
            st.warning("Forgery Transaction Details")
            try:
                df = load()
                df = df[df['token_id'] == int(input)]
                df_forgery = df[(df['is_washtrade'] == 'Washtrade')]
                df_forgery = df_forgery[['token_id', 'seller', 'buyer', 'timestamp', 'sale_price_eth','is_washtrade','accuracy','transaction_hash']]
                st.dataframe(df_forgery)
            except:
                st.info("No Forgery Found")