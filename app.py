import streamlit as st

st.set_page_config(page_title="Final Decision", page_icon="🙄")

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# تهيئة الأحجام
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20 

# كود CSS المطور لجعل الزر يكبر بشكل متناسق
st.markdown(f"""
    <style>
    /* جعل الحاوية تضع الأزرار في المنتصف */
    .stColumn {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    /* تنسيق زر YES ليكبر طولاً وعرضاً بنفس النسبة */
    div.stButton > button:first-child {{
        font-size: {st.session_state.yes_size}px !important;
        width: {st.session_state.yes_size * 3}px !important; /* العرض مربوط بالحجم */
        height: {st.session_state.yes_size * 1.5}px !important; /* الطول مربوط بالحجم */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 15px;
        transition: all 0.3s ease;
        display: block;
        margin: auto;
    }}
    
    /* زر no يبقى صغيراً ومهمشاً */
    div.stButton > button:last-child {{
        font-size: 12px !important;
        background-color: #dc3545 !important;
        color: white !important;
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# استخدام أعمدة لتنظيم المكان
col1, col2 = st.columns([3, 1])

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("I LOVE YOU TOO! ❤️")

with col2:
    if st.button("no"):
        st.session_state.yes_size += 30 # سيكبر الطول والعرض معاً الآن
        st.rerun()
