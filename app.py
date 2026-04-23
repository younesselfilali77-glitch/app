import streamlit as st

st.title("Question for you... 🙄")

# تعريف متغير في "Session State" لحفظ حجم الزر حتى لا يضيع عند إعادة التحميل
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20  # الحجم الأصلي بالبيكسل

# كود CSS لتغيير حجم الزر ديناميكياً
st.markdown(f"""
    <style>
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size * 2}px !important;
        width: {st.session_state.yes_size * 4}px !important;
        background-color: #28a745 !important;
        color: white !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.write("Do you think I'm the best programmer?")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Yes"):
        st.balloons()
        st.success("I knew it! 😎")

with col2:
    if st.button("No"):
        # زيادة حجم زر Yes في كل مرة يُضغط فيها No
        st.session_state.yes_size += 20
        st.rerun() # إعادة تشغيل التطبيق لتطبيق الحجم الجديد
