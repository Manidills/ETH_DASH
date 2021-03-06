

<!-- PROJECT LOGO -->

<br />
<div align="center">
    <img src="https://www.logo.wine/a/logo/Ethereum/Ethereum-Logo.wine.svg" alt="Logo" width="80" height="80">
  <h3 align="center">NFT Data House</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Usage">Application Insights</a></li>
    <li><a href="#API">API's </a></li>
    <li><a href="#ProjectLink">Project Link</a></li>
    <li><a href="#Acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The main goal of our project is to encourage individuals to invest in the proper NFTs based on our data because many people find it difficult or harder to choose the right NFTs for their wallet. 

### Features
* NFT Wallet growth prediction
* NFT Volume growth prediction
* NFT Forgery detection
* NFT Duplicate detection
* TOP Trending collection
* Token and Wallet Analysis
* Token Estimated Prize

Website link : [NFT Data House](https://share.streamlit.io/manidills/eth_dash/main.py)


<img src="https://user-images.githubusercontent.com/91189264/162620252-6f391809-3d3f-4f7b-8a9f-d39a07849ab6.png" alt="Logo" width="1300" height="550">


<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

The frameworks/libraries explicitly used in this project are

* [Python](python.org)
* [keras](https://keras.io/)
* [pillow](https://pillow.readthedocs.io/en/stable/)
* [sklit_learn](https://scikit-learn.org/stable/)
* [streamlit](https://streamlit.io/)
* [streamlit-aggrid](https://pypi.org/project/streamlit-aggrid/)
* [requests](https://docs.python-requests.org/en/latest/)


<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

Follow these steps to install certain packages which is to be installed in this project also make your own 
API key from covalent to get access for data.

### Home page data is not complete ethereum data, we can take it as approx 

1. Get a free API Key from [covalent](https://www.covalenthq.com/)
2. Clone the repo
3. streamlit run main.py

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* altair==4.2.0
* hydralit==1.0.11
* keras==2.8.0
* numpy==1.22.1
* pandas==1.4.0
* pillow==9.0.1
* requests==2.22.0
* scikit_learn==1.0.2
* streamlit==1.4.0
* streamlit-aggrid


## Usage

The chain ethereum is covered in this application with general information and predictions.
Volume exchanges per day, unique wallets per day, collection-wise unique wallets and volume, and 
so on are all included in the forecast. This will provide a clear statistic to NFT traders and buyers. 
As a result, they will be able to invest according to market conditions. This also provides a graphical view of 
how the chain works over time and how the market fluctuates.


* The home page represents the total volume and wallet prediction across the chain ethereum by line chart??and includes a few key metrices 
like Total volume, Average daily volume, and Average weekly volume. Time series forecasting model was built here to predict the number(LSTM).

* The collection page depicts????the overall volume and wallet prediction across all collections in the chain ethereum by line chart; for example, 
we've provided a few key metrics and predictions of volume and wallet over the period of time??for BAYC. The metrices includes??total volume, average daily volume, and average weekly volume.

* The Token page displays a list of unique tokens, tokens that are frequently traded, tokens that are sold in large quantities, and so on. 
We've also included the current owner of the token id, as well as the characteristics of the Top 4 most sold tokens by volume throughout each collection.

* The wallet page displays a list of unique wallets, as well as the top seller by volume, tokens top seller by volume, and total transactions, 
among other information. We've also compiled a list of the top 100 wallet-to-wallet transactions in the chain ethereum.

* Duplicate and forgery page shows the near duplicate token minted in the same nft collections or other.

* Discussion page stores the idea of the people in IPFS storage.

* The state page includes all of the collectios across the chain??ethereum, along with the market cap, transaction count, and floor price,etc.

<img src="https://user-images.githubusercontent.com/91189264/162620334-da01e95f-cb9f-461c-a1e1-1fb1f9945d5b.png" alt="Logo" width="1300" height="550">

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## API

We have used API's from covalent for listing transcation details, collection details,etc.


* COVALENTHQ API

https://api.covalenthq.com/v1/1/tokens/0xe4605d46fd0b3f8329d936a8b258d69276cba264/nft_metadata/123/?key=ckey_docs

https://api.covalenthq.com/v1/:chain_id/nft_market/?&key=

https://api.covalenthq.com/v1/:chain_id/nft_market/collection/:collection_address/?&key=

https://api.covalenthq.com/v1/:chain_id/tokens/:contract_address/nft_transactions/:token_id/?&key=


## ProjectLink


Project Link: (https://github.com/Manidills/ETH_DASH)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

Would like to give credit to below teams for providing the API's

* [Covalent](https://www.covalenthq.com/)
* [IPFS](https://ipfs.io/)

<p align="right">(<a href="#top">back to top</a>)</p>





