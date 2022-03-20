import pandas as pd
import streamlit as st
import requests
import plotly
import plotly.express as px
import json
import time

data = {
    'Name':
        [
         'Yaniv',
         'Avishay',
         'Yasha',
         'Sam',
         'Tim',
         'Asif'
         ],
    'address':
        [
         "0x3e35698c962BCFfBab99594aff3fa136db78b300",
         "0xEe3dBd4d25000C599bBF3B4497D12c733e7A0cB4",
         "0x52B9C25c4d16a2efe83c89bcfC6fE259B05658A5",
         "0xba2ef5189B762bd4C9E7f0b50fBBaB65193935e8",
         "0x48E92AaDd3b92Aa875fe08BF27fe44080eEC749a",
         "0x6bA98440b46d12b46d3393b21319c38AaC12249a"
         ]
}
df = pd.DataFrame(data)

points = []
for address in df['address']:
    bal_custom = requests.get(
        f"https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress=0x23a32ba2b63051950e8421c18fb300870993d9a9&address={address}&tag=latest&apikey=FSQ6MKYTF5335UAIX3IQZP8XYUX394AU8Q").json()
    bal = float(bal_custom['result']) / 10 ** 18
    list.append(points, bal)
    time.sleep(5)

df['points'] = points
# print(df)

df = df.sort_values(by=['points'], ascending=False)

LeaderBoard = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "Name",
    y = "points",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
st.plotly_chart(LeaderBoard)

df['rank'] = df['points'].rank(ascending = False)
st.write(df)
