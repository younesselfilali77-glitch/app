import streamlit as st
import random

st.set_page_config(page_title="The Love Boss", page_icon="❤️", layout="centered")

# 1. تهيئة الذاكرة
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120 
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ثيم وردي ناعم
bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
txt = "#d63384"

# 2. كود التنسيق CSS (حل مشكلة التداخل + القلوب)
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg} !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    /* منع تداخل الأزرار وجعلها جنباً إلى جنب دائماً */
    div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 20px !important;
        flex-wrap: nowrap !important;
    }}

    .stButton > button {{
        transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1) !important;
        border: none !important;
        white-space: nowrap !important;
    }}

    /* زر YES: جعله دائماً في المقدمة لمنع NO من الظهور فوقه */
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.25}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        z-index: 99 !important; /* طبقة عليا */
        position: relative !important;
    }}
    
    /* زر NO: وضعه في طبقة خلفية */
    div[data-testid="stHorizontalBlock"] div:nth-child(2) button {{
        width: {max(35, st.session_state.scale_no)}px !important;
        height: {max(35, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 15px !important;
        z-index: 1 !important; /* طبقة خلفية */
        position: relative !important;
    }}

    /* أنيميشن القلوب: تبدأ من الأعلى وتختفي بالأسفل */
    @keyframes fall {{ 
        0% {{ top: -15%; opacity: 1; }} 
        100% {{ top: 110%; opacity: 0.2; }} 
    }}
    .heart {{ 
        position: fixed; 
        font-size: 35px; 
        top: -15%; 
        animation: fall 3s linear infinite; 
        z-index: 0 !important; 
        pointer-events: none;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<h1 style='color:{txt}; text-align:center;'>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:{txt}; text-align:center;'>Do you Love ME?</h3>", unsafe_allow_html=True)

# 3. عرض القلوب عند الفوز
if st.session_state.show_hearts:
    hearts_list = []
    for _ in range(40):
        l_pos = random.randint(0, 95)
        delay = random.uniform(0, 3)
        hearts_list.append(f'<div class="heart" style="left:{l_pos}%; animation-delay:{delay}s;">❤️</div>')
    st.markdown("".join(hearts_list), unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰")

# 4. حاوية الأزرار (أفقية دائماً بدون تداخل)
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
