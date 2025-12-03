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

st.title('質問2')
st.title('')
score_map = {"はい": 10, "いいえ": 50}

ans = st.selectbox("周りと差をつけたい？", ["はい", "いいえ"])

if st.button("次へ"):
    st.session_state.score += score_map[ans]
    st.switch_page("pages/質問3.py")