import streamlit as st
import random

st.set_page_config(page_title="Love Trap Final", page_icon="❤️", layout="centered")

# 1. تهيئة الأحجام (بداية متساوية كما في صورتك الأخيرة)
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120 
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ---------------------------------------------------------
# اختيار الثيم (Soft Pink أو Deep Night)
# ---------------------------------------------------------
theme_choice = "Soft Pink" # غيرها لـ "Deep Night" للثيم الغامق

if theme_choice == "Soft Pink":
    bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
    txt = "#d63384"
else:
    bg = "linear-gradient(135deg, #1a0a10 0%, #4a1020 50%, #1a0a10 100%)"
    txt = "#ffb3c1"

# 2. كود السحر للتمركز في المنتصف تماماً
st.markdown(f"""
    <style>
    /* جعل التطبيق بالكامل يتمركز عمودياً وأفقياً */
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
        padding-top: 0rem;
    }}

    h1, h3 {{
        color: {txt} !important;
        text-align: center;
        margin-bottom: 2rem !important;
    }}

    /* تنسيق زر YES المربع */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.25}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
    }}
    
    /* تنسيق زر NO المربع */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(25, st.session_state.scale_no)}px !important;
        height: {max(25, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 20px !important;
    }}

    /* أنيميشن القلوب */
    @keyframes fall {{ 0% {{ top: -10%; }} 100% {{ top: 110%; }} }}
    .heart {{ position: fixed; font-size: 30px; animation: fall 3s linear infinite; z-index: 999; }}
    </style>
""", unsafe_allow_html=True)

# 3. المحتوى
st.markdown("<h1>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>Do you Love ME?</h3>", unsafe_allow_html=True)

# عرض القلوب عند الفوز
if st.session_state.show_hearts:
    hearts = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-delay:{random.uniform(0,2)}s;">❤️</div>' for _ in range(30)])
    st.markdown(hearts, unsafe_allow_html=True)
    st.balloons()
    st.success("I Love You Too! ❤️🥰")

# 4. الأزرار في منتصف الأعمدة
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 100
        st.session_state.scale_no = max(20, st.session_state.scale_no - 20)
        # خلط عشوائي للأماكن
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
