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
st.title('ヤマハ YFB621')
st.image('YFB-621.avif')
st.write('')
st.write('F管4ピストン1ロータリー　だいたい120万')
st.write('ちっちゃい楽器．でもファンは多い良い楽器．') 