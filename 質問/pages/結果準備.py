import streamlit as st

st.title('あなたにぴったりの楽器を' \
'持ってきますね...')
st.title('')


score = st.session_state.get("score", 0)

if st.button("結果を見る"):
   if score == 1111:
    st.switch_page('pages/結果1.py')
   elif score == 1115:
    st.switch_page('pages/結果2.py')
   elif score == 1151:
    st.switch_page('pages/結果3.py')
   elif score == 1511:
    st.switch_page('pages/結果4.py')
   elif score == 5111:
    st.switch_page('pages/結果5.py')
   elif score == 1155:
    st.switch_page('pages/結果6.py')
   elif score == 1551:
    st.switch_page('pages/結果7.py')
   elif score == 5511:
    st.switch_page('pages/結果8.py')
   elif score == 1515:
    st.switch_page('pages/結果9.py')
   elif score == 5151:
    st.switch_page('pages/結果10.py')
   elif score == 5115:
    st.switch_page('pages/結果11.py')
   elif score == 1555:
    st.switch_page('pages/結果12.py')
   elif score == 5155:
    st.switch_page('pages/結果13.py')
   elif score == 5515:
    st.switch_page('pages/結果14.py')
   elif score == 5551:
    st.switch_page('pages/結果15.py')
   else:
    st.switch_page('pages/結果16.py')   
