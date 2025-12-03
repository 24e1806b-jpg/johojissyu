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
st.title('Besson BE9822-2')
st.image('BE982-2.jpg')
st.write('')
st.write('Eb管4ピストン　だいたい180万')
st.write('割と新しいEb管．Eb管ならベッソンで間違いない．')