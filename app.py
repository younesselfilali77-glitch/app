import streamlit as st

st.set_page_config(page_title="Square Trap", page_icon="⏹️")

# الذاكرة لحفظ الأحجام
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 60  # حجم البداية لـ YES (كبير قليلاً ليكون مربعاً واضحاً)
if 'no_size' not in st.session_state:
    st.session_state.no_size = 60   # حجم البداية لـ no

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# كود CSS لجعل الأزرار مربعة تماماً
st.markdown(f"""
    <style>
    /* تنسيق زر YES المربع */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size // 3}px !important;
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px; /* زوايا منحنية قليلاً */
        display: flex;
        align-items: center;
        justify-content: center;
        margin: auto;
        transition: 0.3s;
    }}
    
    /* تنسيق زر no المربع */
    div.stButton > button:last-child {{
        font-size: {max(2, st.session_state.no_size // 4)}px !important;
        width: {st.session_state.no_size}px !important;
        height: {st.session_state.no_size}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: auto;
        transition: 0.3s;
    }}
    </style>
""", unsafe_allow_html=True)

# وضع الأزرار
col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("I LOVE YOU TOO! ❤️")

with col2:
    if st.button("no"):
        # تكبير المربع الأخضر وتصغير المربع الأحمر
        st.session_state.yes_size += 50
        if st.session_state.no_size > 10:
            st.session_state.no_size -= 10
        st.rerun()
