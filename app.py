import streamlit as st
import random

st.set_page_config(page_title="The Final Trap", page_icon="🖼️")

# 1. تهيئة الأحجام في الذاكرة
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 100  # حجم البداية لـ YES
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 80    # حجم البداية لـ no
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. CSS يربط المربع والنص بنفس المقياس
st.markdown(f"""
    <style>
    /* تنسيق زر YES: المربع والنص يكبران معاً */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.3}px !important; /* النص دائماً 30% من حجم المربع */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
    }}
    
    /* تنسيق زر no: المربع والنص يصغران معاً */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(20, st.session_state.scale_no)}px !important;
        height: {max(20, st.session_state.scale_no)}px !important;
        font-size: {max(8, st.session_state.scale_no * 0.3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. وضع الأزرار في الأعمدة
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("I Love You Too! ❤️🥳")

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # تكبير YES عملاق وتصغير no
        st.session_state.scale_yes += 100
        st.session_state.scale_no -= 15
        
        # خلط الأماكن عشوائياً
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
