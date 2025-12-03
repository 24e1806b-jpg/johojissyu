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
st.title('B&S BS795-2')
st.image('BS795-2.webp')
st.write('')
st.write('C管4ピストン1ロータリー　だいたい160万')
st.write('コスパのよい楽器．吹いたことあるけどめっちゃよかった．')