import streamlit as st

st.set_page_config(page_title="The Trap", page_icon="😈")

# 1. إعداد الذاكرة للأحجام (Session State)
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20  # حجم البداية لـ YES
if 'no_size' not in st.session_state:
    st.session_state.no_size = 18   # حجم البداية لـ No

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS للتحكم الديناميكي بالأحجام
st.markdown(f"""
    <style>
    /* تنسيق زر YES - يكبر طولاً وعرضاً بشكل متناسق */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        width: {st.session_state.yes_size * 4}px !important; 
        height: {st.session_state.yes_size * 2}px !important;
        background-color: #28a745 !important; /* أخضر للـ YES */
        color: white !important;
        border-radius: 15px;
        transition: 0.3s;
        margin: 10px auto;
        display: block;
    }}
    
    /* تنسيق زر No - يصغر باستمرار ويصبح باهتاً */
    div.stButton > button:last-child {{
        font-size: {max(2, st.session_state.no_size)}px !important;
        width: {max(10, st.session_state.no_size * 3)}px !important;
        height: {max(5, st.session_state.no_size * 1.5)}px !important;
        background-color: #dc3545 !important; /* أحمر للـ No */
        color: white !important;
        opacity: {max(0.2, st.session_state.no_size / 18)};
        border-radius: 5px;
        margin: 10px auto;
        display: block;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. وضع الأزرار
if st.button("YES"):
    st.balloons()
    st.success("I LOVE YOU TOO! ❤️🥳")

if st.button("no"):
    # زيادة حجم YES بشكل كبير وتصغير No
    st.session_state.yes_size += 40
    if st.session_state.no_size > 4:
        st.session_state.no_size -= 4
    st.rerun() # إعادة تشغيل الصفحة لتطبيق الأحجام الجديدة
