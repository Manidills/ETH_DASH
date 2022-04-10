import streamlit as st
import numpy as np
import pandas as pd
from load import load, load_meta, meta_load
import requests, json


def search():
    input = st.text_input("Enter Token ID ",)

    if input:
        df = load()
        try:
            data = df[df['token_id'] == int(input)]
            
            metadata = meta_load(str(input))
            st.markdown('####')
            col1, col2 = st.columns((4,3))
            #print(metadata)
            with col1:
                
                data['timestamp'] = data['timestamp'].astype('datetime64')
                data['timestamp'] = data['timestamp'].dt.date 
                data= data.set_index('timestamp')
                print(data)

               
                st.info('Token Details')
                data['time'] = data.index
                data = data.sort_values(by="time")
                last_sold = data[data['is_sold'] == True]
                last_sold = last_sold['sale_price_usd'].iloc[-1]
                token = metadata['token_id']
                max_date = data['time'].max()
                avg_price = '$'+str(data['sale_price_usd'].mean())
                max_price = '$'+str(data['sale_price_usd'].max())
                mint_date = metadata['mint_date']
                url = metadata['file_url'] 
                att = metadata['metadata']['attributes']
                forgery = data.isin(["Washtrade"]).any().any()
                st.text(f'Token_id = {token}')
                st.text(f'Last transaction date = {max_date}')
                st.text(f'Last price sold = {last_sold}')
                st.text(f'Max price sold = {max_price}')
                st.text(f'Minted_date = {mint_date}')
                st.text(f'url = {url}')
                st.write(f'Attributes = {att}')
                st.warning(f'Forged = {forgery}')
                st.success(f'Avg / Suggested price = {avg_price}')
            with col2:
                st.image(metadata['cached_file_url'],width=500)
            st.markdown('####')
            st.info('Transaction details')
            data.drop(['method','is_washtrade', 'accuracy'], axis=1, inplace=True)
            st.dataframe(data)
            st.markdown('####')
            st.info('Price chart')
            
            line = data[data.columns[~data.isnull().all()]]
            st.line_chart(line['sale_price_usd'])
                    
                
                    
        except:
            st.warning("Info not found in DB")
    else:
        df = load()
        net = df.groupby(['token_id']).agg({'sale_price_usd': 'sum'}).reset_index() 
        net = net.nlargest(10,'sale_price_usd')
        net = net['token_id'].to_list()
        
        st.markdown("##")
        st.warning("Top 4 Most sold Token by volume")


        col1, col2= st.columns((3,3))
        with col1:
            try:
                meta = meta_load(net[0])
                token = meta['token_id']
                mint_date = meta['mint_date']
                url = meta['file_url'] 
                att = meta['metadata']['attributes']
                st.image(meta['cached_file_url'],width=400)
                st.text(f'Token_id = {token}')
                st.text(f'Minted_date = {mint_date}')
                st.text(f'URL = {url}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")
        
        with col2:
            try:
                meta = meta_load(net[1])
                token = meta['token_id']
                mint_date = meta['mint_date']
                url = meta['file_url'] 
                att = meta['metadata']['attributes']
                st.image(meta['cached_file_url'],width=400)
                st.text(f'Token_id = {token}')
                st.text(f'Minted_date = {mint_date}')
                st.text(f'URL = {url}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")

        

        with col1:
            try:
                meta = meta_load(net[2])
                token = meta['token_id']
                mint_date = meta['mint_date']
                url = meta['file_url'] 
                att = meta['metadata']['attributes']
                st.image(meta['cached_file_url'],width=400)
                st.text(f'Token_id = {token}')
                st.text(f'Minted_date = {mint_date}')
                st.text(f'URL = {url}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")
        
        with col2:
            try:
                meta = meta_load(net[3])
                token = meta['token_id']
                mint_date = meta['mint_date']
                url = meta['file_url'] 
                att = meta['metadata']['attributes']
                st.image(meta['cached_file_url'],width=400)
                st.text(f'Token_id = {token}')
                st.text(f'Minted_date = {mint_date}')
                st.text(f'URL = {url}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")
        
        


