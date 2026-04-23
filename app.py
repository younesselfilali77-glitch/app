import streamlit as st
import random

st.set_page_config(page_title="Love Trap v2", page_icon="❤️")

# 1. تهيئة الأحجام لتكون متساوية في أول مرة (120px لكل منهما)
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ---------------------------------------------------------
# اختر الثيم الذي تفضله (Theme 1 أو Theme 2)
# ---------------------------------------------------------
theme = "Theme 1" # غيرها لـ "Theme 2" لتجربة الشكل الآخر

if theme == "Theme 1":
    # ثيم وردي ناعم (Soft Pink)
    bg_gradient = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
    text_color = "#d63384"
else:
    # ثيم ليلي رومانسي (Deep Night Love) كما في صورتك الأخيرة
    bg_gradient = "linear-gradient(135deg, #1a0a10 0%, #4a1020 50%, #1a0a10 100%)"
    text_color = "#ffb3c1"

# 2. كود التنسيق CSS
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg_gradient} !important;
    }}
    h1, h3 {{
        color: {text_color} !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }}
    /* تنسيق زر YES */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.3}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }}
    /* تنسيق زر no */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {st.session_state.scale_no}px !important;
        height: {st.session_state.scale_no}px !important;
        font-size: {st.session_state.scale_no * 0.3}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 20px !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }}
    /* أنيميشن القلوب */
    @keyframes fall {{
        0% {{ transform: translateY(-10vh); }}
        100% {{ transform: translateY(110vh); }}
    }}
    .heart {{
        position: fixed;
        top: -10%;
        font-size: 25px;
        animation: fall 3s linear infinite;
        z-index: 1000;
    }}
    </style>
""", unsafe_allow_html=True)

st.write("# 💖 Final Decision 💖")
st.write("### Do you Love ME?")

# 3. عرض القلوب عند الفوز
if st.session_state.show_hearts:
    hearts_html = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-delay:{random.uniform(0,2)}s;">❤️</div>' for _ in range(30)])
    st.markdown(hearts_html, unsafe_allow_html=True)
    st.success("Victory! ❤️🥰")

# 4. توزيع الأزرار
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # عند ضغط No، يبدأ الانحراف في الأحجام!
        st.session_state.scale_yes += 80
        st.session_state.scale_no = max(20, st.session_state.scale_no - 20)
        
        # تغيير الأماكن عشوائياً
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.session_state.show_hearts = False
        st.rerun()
