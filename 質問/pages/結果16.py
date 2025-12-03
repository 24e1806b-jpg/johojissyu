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
st.title('Miraphone 86A')
st.image('86A.jpg')
st.write('')
st.write('Bb管4ロータリー　だいたい220万くらい')
st.write('学校の楽器でヤマハ意外だとだいたいこれ．でも最近見ない．いい音するよ')