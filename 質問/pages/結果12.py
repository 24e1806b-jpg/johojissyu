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
st.title('ヤマハ YCB-621')
st.image('YCB-621.avif')
st.write('')
st.write('C管4ピストン　だいたい100万')
st.write('ちっちゃいC管．友達も使ってたが，大きいものに買い替えた．')