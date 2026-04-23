import streamlit as st
import random

st.set_page_config(page_title="Smooth Love Trap", page_icon="❤️", layout="centered")

# 1. تهيئة الأحجام والترتيب (بداية متساوية كما طلبت)
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120 
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ثيم وردي ناعم
bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
txt = "#d63384"

# 2. CSS السحري: تمركز + انتقال انسيابي للحجم والموقع
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
    }}

    h1, h3 {{
        color: {txt} !important;
        text-align: center;
    }}

    /* الانتقال الانسيابي لكل شيء (الحجم والموقع) */
    .stButton > button {{
        transition: width 0.6s ease, height 0.6s ease, font-size 0.6s ease, transform 0.6s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border: none !important;
    }}

    /* زر YES */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.25}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
    }}
    
    /* زر NO */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(30, st.session_state.scale_no)}px !important;
        height: {max(30, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 20px !important;
    }}

    /* أنيميشن القلوب في الخلفية */
    @keyframes fall {{ 
        0% {{ top: -10%; opacity: 1; }} 
        100% {{ top: 110%; opacity: 0; }} 
    }}
    .heart {{ 
        position: fixed; 
        font-size: 35px; 
        animation: fall 3s linear infinite; 
        z-index: 1; 
        pointer-events: none;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. النصوص
st.markdown("<h1>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>Do you Love ME?</h3>", unsafe_allow_html=True)

if st.session_state.show_hearts:
    hearts = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-delay:{random.uniform(0,2)}s;">❤️</div>' for _ in range(40)])
    st.markdown(hearts, unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰")

# 4. الأزرار (توزيع في أعمدة)
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # تغيير الأحجام
        st.session_state.scale_yes += 100
        st.session_state.scale_no = max(30, st.session_state.scale_no - 20)
        
        # تغيير الترتيب (الهروب لمكان جديد)
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        
        st.rerun()
