import streamlit as st
import random

st.set_page_config(page_title="Final Love Trap", page_icon="❤️", layout="centered")

# 1. تهيئة الأحجام
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120 
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ثيم وردي ناعم
bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
txt = "#d63384"

# 2. CSS متطور لمنع التداخل (Overlapping)
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg} !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    .main .block-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 2;
    }}

    /* حاوية الأزرار لمنع التداخل */
    div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 30px !important; /* مسافة أمان ثابتة بين الأزرار */
        flex-wrap: nowrap !important;
        width: 100% !important;
    }}

    /* تعديل الأعمدة لمنع تداخلها */
    div[data-testid="stHorizontalBlock"] > div {{
        width: auto !important;
        min-width: min-content !important;
        flex-shrink: 0 !important; /* يمنع العمود من الانضغاط أو الاختباء خلف الآخر */
    }}

    .stButton > button {{
        transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1) !important;
        border: none !important;
        white-space: nowrap !important;
    }}

    /* زر YES */
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.25}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
    }}
    
    /* زر NO */
    div[data-testid="stHorizontalBlock"] div:nth-child(2) button {{
        width: {max(35, st.session_state.scale_no)}px !important;
        height: {max(35, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 15px !important;
    }}

    /* القلوب في الخلفية */
    @keyframes fall {{ 
        0% {{ top: -10%; opacity: 1; }} 
        100% {{ top: 110%; opacity: 0; }} 
    }}
    .heart {{ position: fixed; font-size: 30px; animation: fall 3s linear infinite; z-index: 1; pointer-events: none; }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<h1 style='color:{txt}; text-align:center;'>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:{txt}; text-align:center;'>Do you Love ME?</h3>", unsafe_allow_html=True)

if st.session_state.show_hearts:
    hearts = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-delay:{random.uniform(0,2)}s;">❤️</div>' for _ in range(40)])
    st.markdown(hearts, unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰")

# 3. استخدام الأعمدة مع ضمان التباعد
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with col2:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 100 
        st.session_state.scale_no = max(35, st.session_state.scale_no - 15)
        st.rerun()
