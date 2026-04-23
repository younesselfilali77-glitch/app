import streamlit as st
import random

st.set_page_config(page_title="The Love Boss", page_icon="❤️", layout="centered")

# 1. تهيئة الذاكرة
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 160
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# 2. كود التنسيق (CSS)
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #1a0a10 0%, #4a1020 50%, #1a0a10 100%) !important;
    }}
    h1, h3 {{
        color: #ffb3c1 !important;
        text-align: center;
    }}
    /* زر YES */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.3}px !important;
        background: linear-gradient(145deg, #28a745, #1e7e34) !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: 900 !important;
        box-shadow: 0px 0px 30px rgba(40, 167, 69, 0.6) !important;
    }}
    /* زر no */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(30, st.session_state.scale_no)}px !important;
        height: {max(30, st.session_state.scale_no)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
    }}
    @keyframes falling {{
        0% {{ transform: translateY(-10vh); }}
        100% {{ transform: translateY(110vh); }}
    }}
    .heart {{
        position: fixed;
        color: #ff4d6d;
        font-size: 30px;
        animation: falling 3s linear infinite;
        z-index: 1000;
    }}
    </style>
""", unsafe_allow_html=True)

st.write("# 💖 Final Decision 💖")
st.write("### Do you Love ME?")

# 3. الجزء الذي كان فيه الخطأ (تم إصلاحه)
if st.session_state.show_hearts:
    hearts_list = []
    for _ in range(30):
        left_pos = random.randint(0, 95)
        duration = random.uniform(2, 5)
        # كتابة الـ HTML بدون f-string متداخل لتجنب الخطأ
        heart_tag = f'<div class="heart" style="left:{left_pos}%; animation-duration:{duration}s;">❤️</div>'
        hearts_list.append(heart_tag)
    
    st.markdown("".join(hearts_list), unsafe_allow_html=True)
    st.balloons()
    st.success("I Love You Too! ❤️🥰")

# 4. الأزرار
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 100
        st.session_state.scale_no -= 15
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
