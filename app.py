import streamlit as st

st.title("Final Decision... 🙄")

# تعريف متغيرات الحجم في ذاكرة الجلسة
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20  # الحجم الابتدائي لـ Yes
if 'no_size' not in st.session_state:
    st.session_state.no_size = 15   # الحجم الابتدائي لـ No

# سحر الـ CSS للتحكم في الزرين بدقة
st.markdown(f"""
    <style>
    /* تنسيق زر Yes (الزر الأول في الصفحة) */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        padding: {st.session_state.yes_size // 2}px !important;
        background-color: #28a745 !important;
        color: white !important;
        width: auto !important;
        transition: 0.2s;
    }}
    
    /* تنسيق زر No (الزر الثاني في الصفحة) */
    div.stButton > button:last-child {{
        font-size: {st.session_state.no_size}px !important;
        padding: {max(2, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        width: auto !important;
        opacity: {max(0.3, st.session_state.no_size / 15)}; /* يبهت لونه كلما صغر */
    }}
    </style>
""", unsafe_allow_html=True)

st.subheader("Do you agree that I am a genius programmer?")

# إنشاء أعمدة لوضع الأزرار بجانب بعضها
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("Correct answer! I'm proud of you. 🏆")

with col2:
    if st.button("no"):
        # تكبير نعم وتصغير لا
        st.session_state.yes_size += 40
        if st.session_state.no_size > 5: # منع الزر من الاختفاء تماماً
            st.session_state.no_size -= 2
        st.rerun()
