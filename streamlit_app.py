import streamlit as set 
import random 
st.title ("おみくじアプリ")
if st.button("おみくじをひく"):
    results={"大吉","中吉","小吉","吉","凶",大凶"}
    results=random.choice(results)
    st.write(f"結果:{result}")



