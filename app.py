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
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS للأزرار والتأثيرات
st.markdown(f"""
    <style>
    .stButton > button {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
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
        width: {max(25, st.session_state.scale_no)}px !important;
        height: {max(25, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
    }}
    
    /* أنيميشن القلوب المتساقطة */
    @keyframes hearts-fall {{
        0% {{ top: -10%; }}
        100% {{ top: 100%; }}
    }}
    .heart {{
        position: fixed;
        top: -10%;
        font-size: 24px;
        animation: hearts-fall 3s linear infinite;
        z-index: 9999;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. دالة توليد القلوب (HTML)
if st.session_state.show_hearts:
    heart_html = ""
    for i in range(20):
        left = random.randint(0, 100)
        delay = random.uniform(0, 3)
        heart_html += f'<div class="heart" style="left: {left}%; animation-delay: {delay}s;">❤️</div>'
    st.markdown(heart_html, unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥳")

# 4. عرض الأزرار
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 80
        st.session_state.scale_no -= 15
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.session_state.show_hearts = False # إيقاف القلوب إذا حاول الهرب مجدداً
        st.rerun()
