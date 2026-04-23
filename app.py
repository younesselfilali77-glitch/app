import streamlit as st
import random

st.set_page_config(page_title="Love Trap Final", page_icon="❤️", layout="centered")

# 1. تهيئة الأحجام
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

# 2. كود CSS المطور (نقل القلوب للخلفية)
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
        z-index: 2; /* جعل المحتوى فوق القلوب */
    }}

    h1, h3 {{
        color: {txt} !important;
        text-align: center;
        margin-bottom: 2rem !important;
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
        border: none !important;
    }}
    
    /* زر NO */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(25, st.session_state.scale_no)}px !important;
        height: {max(25, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 20px !important;
    }}

    /* أنيميشن القلوب في الخلفية */
    @keyframes fall {{ 
        0% {{ top: -10%; transform: rotate(0deg); opacity: 1; }} 
        100% {{ top: 110%; transform: rotate(360deg); opacity: 0; }} 
    }}
    .heart {{ 
        position: fixed; 
        font-size: 30px; 
        animation: fall 4s linear infinite; 
        z-index: 1 !important; /* وضع القلوب خلف المحتوى */
        pointer-events: none; /* لكي لا تعيق الضغط على الأزرار */
    }}
    </style>
""", unsafe_allow_html=True)

# 3. النصوص
st.markdown("<h1>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>Do you Love ME?</h3>", unsafe_allow_html=True)

# 4. توليد القلوب عند الفوز
if st.session_state.show_hearts:
    hearts_list = []
    for _ in range(40):
        l_pos = random.randint(0, 95)
        delay = random.uniform(0, 4)
        hearts_list.append(f'<div class="heart" style="left:{l_pos}%; animation-delay:{delay}s;">❤️</div>')
    st.markdown("".join(hearts_list), unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰")

# 5. توزيع الأزرار
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 100
        st.session_state.scale_no = max(20, st.session_state.scale_no - 20)
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
