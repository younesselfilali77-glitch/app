import streamlit as st
import random

st.set_page_config(page_title="Heart Trap ❤️", page_icon="❤️")

# 1. الذاكرة
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 100
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. CSS للمربعات والتكبير المتوازي
st.markdown(f"""
    <style>
    .stButton > button {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
        transition: all 0.2s ease;
    }}

    /* زر YES */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.3}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
    }}
    
    /* زر no */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(20, st.session_state.scale_no)}px !important;
        height: {max(20, st.session_state.scale_no)}px !important;
        font-size: {max(8, st.session_state.scale_no * 0.3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
    }}
    </style>
""", unsafe_allow_html=True)

cols = st.columns([1, 1, 1])

# زر YES
with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        # بدلاً من النفاخات.. قلوب!
        st.toast("❤️❤️❤️❤️❤️❤️❤️❤️")
        st.snow() # هذا سيسقط ندف ثلج، لكننا سنضيف رسالة قلوب
        st.success("I Love You Too! ❤️")

# زر no
with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 100
        st.session_state.scale_no -= 15
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
