import streamlit as st
import numpy as np
import pandas as pd
import requests, json


       
@st.cache(allow_output_mutation=True)
def load():
    df = pd.read_csv('./data/Bored.csv')
    return df

@st.cache(allow_output_mutation=True)
def load_meta(x):
    url = f"https://api.covalenthq.com/v1/1/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/nft_metadata/{x}/?key=ckey_eb29565e970e4b46930dca374df"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data1 = response.json()
        data1 = data1['data']['items']
        basic_data = data1[0]['nft_data']
        metadata = basic_data[0]['external_data']
        return metadata, basic_data
    else:
        return 'error', 'error'

def meta_load(x):
    url = f"https://api.nftport.xyz/v0/nfts/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/{x}"

    querystring = {"chain":"ethereum"}

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    meta = response['nft']
    return meta
        

def nfts(x):
        #account = '0x3842ac0946f1fcaaa56842e9b354731276746fa5'

        url = f"https://api.nftport.xyz/v0/accounts/{str(x)}"

        querystring = {"chain":"ethereum"}

        headers = {
            'Content-Type': "application/json",
            'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()
        data = data['nfts']

        chicken = []

        for i in data:
            if i['contract_address'] == '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d':
                chicken.append(i)

        return chicken