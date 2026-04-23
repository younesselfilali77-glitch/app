import streamlit as st

st.set_page_config(page_title="Square Trap", page_icon="⏹️")

# 1. ذاكرة الأحجام
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 80  # حجم البداية للمربع الأخضر
if 'no_size' not in st.session_state:
    st.session_state.no_size = 80   # حجم البداية للمربع الأحمر

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS لجعل الأزرار مربعات مثالية
st.markdown(f"""
    <style>
    /* تنسيق الزر الأخضر YES */
    div.stButton > button:first-child {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {max(10, st.session_state.yes_size // 4)}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto;
        transition: 0.2s;
    }}
    
    /* تنسيق الزر الأحمر no */
    div.stButton > button:last-child {{
        width: {st.session_state.no_size}px !important;
        height: {st.session_state.no_size}px !important;
        font-size: {max(2, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto;
        transition: 0.2s;
        opacity: {max(0.3, st.session_state.no_size / 80)};
    }}
    </style>
""", unsafe_allow_html=True)

# 3. عرض الأزرار
col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("Victory! ❤️🥳")

with col2:
    if st.button("no"):
        # تكبير نعم وتصغير لا
        st.session_state.yes_size += 40
        if st.session_state.no_size > 10:
            st.session_state.no_size -= 10
        st.rerun()
