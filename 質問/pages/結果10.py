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
st.title('Melton Meinl Weston MW97/2')
st.image('MW97_2.jpg')
st.write('')
st.write('Bb管4ロータリー　だいたい300万')
st.write('割と新しい楽器．Bb管のダークな音に加えて吹きやすさを併せ持つ')