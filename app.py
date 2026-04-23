import streamlit as st
import random

st.set_page_config(page_title="Square Trap", page_icon="⏹️")

# 1. الذاكرة
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 80
if 'no_size' not in st.session_state:
    st.session_state.no_size = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. CSS يربط حجم الخط بحجم المربع
st.markdown(f"""
    <style>
    /* زر YES: النص يكبر بنسبة 30% من حجم المربع */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {st.session_state.yes_size // 3}px !important; /* النص يكبر تلقائياً */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 15px;
        font-weight: bold !important;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    
    /* زر no: النص يصغر مع المربع */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(20, st.session_state.no_size)}px !important;
        height: {max(20, st.session_state.no_size)}px !important;
        font-size: {max(6, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    </style>
""", unsafe_allow_html=True)

cols = st.columns([1, 1, 1])

# زر YES
with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("I knew it! ❤️🥳")

# زر no
with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.yes_size += 60 # زيادة الحجم
        st.session_state.no_size -= 10  # تصغير الحجم
        
        # تغيير الأماكن عشوائياً
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
