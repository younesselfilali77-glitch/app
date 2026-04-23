import streamlit as st

st.set_page_config(page_title="Final Decision", page_icon="🙄")

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 1. تهيئة أحجام الأزرار في ذاكرة الجلسة (Session State)
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20  # حجم البداية لـ YES
if 'no_size' not in st.session_state:
    st.session_state.no_size = 16   # حجم البداية لـ no

# 2. كود CSS للتحكم في الأحجام بناءً على ضغطات المستخدم
st.markdown(f"""
    <style>
    /* تنسيق زر YES - ينمو باستمرار */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        height: auto !important;
        width: auto !important;
        min-width: {st.session_state.yes_size * 2}px;
        padding: {st.session_state.yes_size // 2}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px;
        transition: all 0.2s ease-in-out;
    }}
    
    /* تنسيق زر no - يتقلص ويختفي */
    div.stButton > button:last-child {{
        font-size: {max(2, st.session_state.no_size)}px !important;
        padding: {max(1, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        opacity: {max(0.1, st.session_state.no_size / 16)};
        transition: all 0.2s ease-in-out;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. إنشاء الأزرار
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("I LOVE YOU TOO! ❤️🥳")

with col2:
    # عند الضغط هنا، نعدل الأحجام ونعيد تحميل الصفحة
    if st.button("no"):
        st.session_state.yes_size += 50  # زيادة كبيرة لـ YES
        if st.session_state.no_size > 4:
            st.session_state.no_size -= 3   # تصغير زر no
        st.rerun()
