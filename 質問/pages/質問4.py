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

st.title('質問4')
st.title('')
score_map = {"はい": 1000, "いいえ": 5000}

ans = st.selectbox("やっぱり安い方がいい？", ["はい", "いいえ"])

if st.button("次へ"):
    st.session_state.score += score_map[ans]
    st.switch_page("pages/結果準備.py")