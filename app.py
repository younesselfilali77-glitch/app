import streamlit as st
import random

st.title("Final Love Trap 😈")

st.write("Do you love me?")

# إنشاء عمودين للأزرار
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes"):
        st.balloons()
        st.success("I knew it! ❤️")

with col2:
    # استخدام Session State لتغيير مكان الزر
    if "button_pos" not in st.session_state:
        st.session_state.button_pos = 0

    # هذه هي الخدعة: الزر سيختفي ويظهر في مكان مختلف عند الضغط عليه
    # أو يمكنك ببساطة جعل الزر لا يفعل شيئاً سوى إظهار رسالة سخرية
    if st.button("No"):
        st.session_state.button_pos += 1
        st.error("Too slow! Try again 😂")
        st.snow()

# إضافة لمسة "الهروب" باستخدام CSS (اختياري ومتقدم)
st.markdown("""
    <style>
    div.stButton > button:last-child:hover {
        /* يمكنك إضافة كود هنا لجعل الزر يتحرك عند مرور الماوس عليه */
    }
    </style>
    """, unsafe_allow_html=True)
