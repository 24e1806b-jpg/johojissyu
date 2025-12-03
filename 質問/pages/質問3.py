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

st.title('質問3')
st.title('')
score_map = {"はい": 100, "いいえ": 500}

ans = st.selectbox("楽器は大きければ大きい方がかっこいい？", ["はい", "いいえ"])

if st.button("次へ"):
    st.session_state.score += score_map[ans]
    st.switch_page("pages/質問4.py")