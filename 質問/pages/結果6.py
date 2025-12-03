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
st.title('ヤマハ YBB-623S')
st.image('YBB-623S.avif')
st.write('')
st.write('Bb管4ピストン　だいたい130万')
st.write('私が使ってる楽器．購入したときは115万だったのに値上がりした．')
st.write('新しい楽器で生産数も少ないため，現在は非常にレア．')