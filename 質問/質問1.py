import streamlit as st

#左のサイドバーを隠す呪文ね

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


st.title ('質問１')
st.title('')

score_map = {"はい": 1, "いいえ": 5}
if "score" not in st.session_state:
    st.session_state.score = 0

ans = st.selectbox("目立ちたいタイプ？", ["はい", "いいえ"])

if st.button("次へ"):
    st.session_state.score += score_map[ans]
    st.switch_page("pages/質問2.py")

