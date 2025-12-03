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
st.title('B&S MRP-C')
st.image('pt-6.jpg')
st.write('')
st.write('C管5ロータリー　だいたい250万')
st.write('Bb管のような音がするC管．見た目がカッコいい．')