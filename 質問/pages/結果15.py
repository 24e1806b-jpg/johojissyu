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
st.title('MW4250 tradition')
st.image('4250.webp')
st.write('')
st.write('F管5ロータリー')
st.write('割と新しいF管．ドイツの伝統的な音色は残しつつ，現代の技術で吹きやすくなっている．')