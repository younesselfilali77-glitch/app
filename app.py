import streamlit as st
import random

st.set_page_config(page_title="The Final Victory", page_icon="⏹️")

# 1. الذاكرة
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 120
if 'no_size' not in st.session_state:
    st.session_state.no_size = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS لإجبار المربعات والنص العملاق
st.markdown(f"""
    <style>
    /* منع التفاف النص نهائياً وتوسيطه */
    .stButton > button {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
        margin: auto !important;
    }}

    /* زر YES: مربع ونصوص ضخمة */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {st.session_state.yes_size // 3}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: bold !important;
    }}
    
    /* زر no: مربع صغير يتقلص */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(30, st.session_state.no_size)}px !important;
        height: {max(30, st.session_state.no_size)}px !important;
        font-size: {max(10, st.session_state.no_size // 3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. توزيع الأزرار في أعمدة واسعة
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("Victory! ❤️🥳")

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # قفزة ضخمة في الحجم لفرض السيطرة
        st.session_state.yes_size += 100
        if st.session_state.no_size > 20:
            st.session_state.no_size -= 15
        
        # خلط الأماكن
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
