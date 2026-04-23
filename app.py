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

# اختيار الثيم (Soft Pink كما في آخر صورة ناجحة لك)
bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
txt = "#d63384"

# 2. كود CSS للتمركز وحذف النفاخات وتنسيق الأزرار
st.markdown(f"""
    <style>
    /* التمركز المطلق للمحتوى في وسط الشاشة */
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
        margin-bottom: 2rem !important;
    }}

    /* تنسيق زر YES المربع العملاق */
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
    
    /* تنسيق زر NO المربع الصغير */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(25, st.session_state.scale_no)}px !important;
        height: {max(25, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
    }}

    /* أنيميشن القلوب المتساقطة */
    @keyframes fall {{ 
        0% {{ top: -10%; transform: rotate(0deg); }} 
        100% {{ top: 110%; transform: rotate(360deg); }} 
    }}
    .heart {{ 
        position: fixed; 
        font-size: 35px; 
        animation: fall 3s linear infinite; 
        z-index: 999; 
        user-select: none;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. النصوص
st.markdown("<h1>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>Do you Love ME?</h3>", unsafe_allow_html=True)

# عرض مطر القلوب فقط (تم حذف st.balloons)
if st.session_state.show_hearts:
    hearts_html = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-delay:{random.uniform(0,2)}s;">❤️</div>' for _ in range(40)])
    st.markdown(hearts_html, unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰")

# 4. الأزرار المتمركزة
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.scale_yes += 100
        st.session_state.scale_no = max(20, st.session_state.scale_no - 20)
        
        # خلط عشوائي للأماكن ليهرب الزر
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
