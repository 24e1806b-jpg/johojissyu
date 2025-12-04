import streamlit as st



st.title('奏叔父楽器店へようこそ')
st.subheader('あなたにぴったりの楽器を提案できます')

st.image('Gemini_楽器屋さん.png')

questions = ['どんな楽器がほしいですか？詳しく教えてください']



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
        
        col1, col2 = st.columns([8, 1])
        with col2:
          if st.button('送信'):
            if answer.strip():
                st.session_state.answers[q] = answer
                st.session_state.current_q += 1
                placeholder.empty()  # 入力バーを消す
                st.rerun()  # ← ここを変更
else:
    st.write('なるほど。ではいくつか質問するので、自分の理想に近いものを選択してください！' \
    '良い楽器を紹介しますよ！')

    col1, col2 = st.columns([9, 2])
    with col2:
      st.link_button('質問1へ', 'johojissyu/質問/質問1.py')
      
