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
st.title('Meister Walter Nirschl MWN8S')
st.image('nirs.jpg_large')
st.write('')
st.write('C管4ピストン1ロータリー　だいたい500万くらい')
st.write('みんなが羨む憧れの楽器．ミニバンが変えそうな値段．もちろん音もすごく良い')