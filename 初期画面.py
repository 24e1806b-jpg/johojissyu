import streamlit as st

st.title('鈴木楽器店へようこそ')



st.subheader('あなたにぴったりの楽器を提案できます')



st.title('-')










questions = ["どんな楽器がほしいですか？"]

# 状態管理
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

placeholder = st.empty()  # プレースホルダーを作る

if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]

    with placeholder.container():
        answer = st.text_input(q, key=f"q{st.session_state.current_q}")
        if st.button("送信"):
            if answer.strip():
                st.session_state.answers[q] = answer
                st.session_state.current_q += 1
                placeholder.empty()  # 入力バーを消す
                st.rerun()  # ← ここを変更
else:
    st.write('いいですね！')
    