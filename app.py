import streamlit as st

st.set_page_config(page_title="Final Decision", page_icon="😈")

# الذاكرة لحفظ الأحجام
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20
if 'no_size' not in st.session_state:
    st.session_state.no_size = 16

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# كود CSS محسن لمنع التكدس العمودي للحروف
st.markdown(f"""
    <style>
    /* تنسيق زر YES */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        padding: 10px 20px !important;
        width: auto !important;
        min-width: {st.session_state.yes_size * 2}px !important; /* ضمان مساحة عرضية للكلمة */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px;
        display: inline-block;
        white-space: nowrap !important; /* منع الحروف من النزول لسطر جديد */
    }}
    
    /* تنسيق زر no */
    div.stButton > button:last-child {{
        font-size: {max(2, st.session_state.no_size)}px !important;
        padding: 5px 10px !important;
        width: auto !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        display: inline-block;
        white-space: nowrap !important;
    }}
    </style>
""", unsafe_allow_html=True)

# وضع الأزرار بجانب بعضها
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("I LOVE YOU TOO! ❤️")

with col2:
    if st.button("no"):
        st.session_state.yes_size += 30
        if st.session_state.no_size > 5:
            st.session_state.no_size -= 3
        st.rerun()
