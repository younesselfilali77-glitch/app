import streamlit as st

st.title("Question for you... 🙄")

# حفظ حجم زر Yes في ذاكرة الجلسة
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20 

# كود CSS للتحكم في الأزرار
# الزر الأول (Yes) يتغير حجمه بناءً على المتغير
# الزر الثاني (No) يبقى صغيراً دائماً
st.markdown(f"""
    <style>
    /* تنسيق زر Yes */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        padding: {st.session_state.yes_size // 2}px !important;
        background-color: #28a745 !important;
        color: white !important;
        transition: 0.3s;
    }}
    
    /* تنسيق زر No ليبقى صغيراً جداً */
    div.stButton > button:last-child {{
        font-size: 10px !important;
        padding: 2px 5px !important;
        background-color: #dc3545 !important;
        color: white !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.subheader("Do you love programming now?")

col1, col2 = st.columns([2, 1])

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("I knew you'd say that! 🚀")

with col2:
    if st.button("no"):
        # عند الضغط على No، يزيد حجم Yes فقط
        st.session_state.yes_size += 30
        st.rerun()
