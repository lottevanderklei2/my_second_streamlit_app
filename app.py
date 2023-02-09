import streamlit as st
import pandas as pd
import random
from io import StringIO

import streamlit as st

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
#     st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)

playlist = pd.DataFrame(dataframe)    
aantal_kaarten = 2
seed_num = 2407

def kaart_generator(playlist, seed_num):
#     df = pd.read_csv(playlist, header = None)
    random.seed(seed_num)
    nums = list(range(1, 51)) 
    random.shuffle(nums)
    playlist['random'] = nums
    new_df = playlist.sort_values("random")
    data = list(zip(new_df['title_and_artist'][0:5], 
        new_df['title_and_artist'][5:10],
        new_df['title_and_artist'][10:15],
        new_df['title_and_artist'][15:20],
        new_df['title_and_artist'][20:25]))
    df2 = pd.DataFrame(data)
    df2[2][2] = "BINGO"
    return df2

def bingo_kaarten_generator(playlist, aantal_kaarten, seed_num):
    kaarten_list = []
    for i in range(0, aantal_kaarten):
        kaarten_list.append(kaart_generator(playlist, seed_num + i))
    return kaarten_list

st.dataframe(bingo_kaarten_generator(playlist, aantal_kaarten, seed_num)[0])

