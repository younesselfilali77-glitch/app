import streamlit as st
import random

st.set_page_config(page_title="Final Boss Level", page_icon="⏹️")

# 1. الذاكرة للأحجام والأماكن
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 120 # نبدأ بحجم كبير وواضح
if 'no_size' not in st.session_state:
    st.session_state.no_size = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS الذي يمنع انهيار الحروف ويجعلها مربعات حقيقية
st.markdown(f"""
    <style>
    /* تنسيق زر YES: مربع ونص ضخم في سطر واحد */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {max(16, st.session_state.yes_size // 4)}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px;
        white-space: nowrap !important; /* يمنع الحروف من النزول لسطر جديد */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: bold !important;
    }}
    
    /* تنسيق زر no: مربع يصغر دون أن تنهار حروفه */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(30, st.session_state.no_size)}px !important;
        height: {max(30, st.session_state.no_size)}px !important;
        font-size: {max(10, st.session_state.no_size // 3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 10px;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. عرض الأزرار في الأعمدة
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("I knew you couldn't resist! ❤️")

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # تكبير YES وتصغير no
        st.session_state.yes_size += 80
        if st.session_state.no_size > 20:
            st.session_state.no_size -= 15
        
        # تغيير الأماكن عشوائياً
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
