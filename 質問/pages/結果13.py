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
st.title('Hisburner HBS-290S')
st.image('HBS-290.jpg')
st.write('')
st.write('C管5ロータリー　値段はよくわからん')
st.write('中古でしか見ない．製造終了したのかな．製造時期によって仕様が異なる．')