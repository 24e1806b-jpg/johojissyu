import streamlit as st

#左のサイドバーを隠す呪文

st.set_page_config(initial_sidebar_state="collapsed")
hide_nav = """
    <style>
    [data-testid="stSidebarNav"] { 
        display: none; 
    }
    </style>
"""
st.markdown(hide_nav, unsafe_allow_html=True)
#ーーーーーーーーーーーーーーーーーーーーー

st.title('あなたにぴったりなのはこれ！！')
st.write('')
st.title('EASTMAN EBC836S')
st.image('836.webp')
st.write('')
st.write('C管4ピストン1ロータリー　だいたい180万くらい')
st.write('プロや音大生でも使ってる人が多いよ')