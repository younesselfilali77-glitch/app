import streamlit as st
import random

st.set_page_config(page_title="The Love Boss", page_icon="❤️", layout="centered")

# 1. تهيئة الذاكرة للأحجام والترتيب
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 160 # حجم بداية ضخم
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# 2. كود CSS للخلفية الرومانسية وتنسيق الأزرار العملاقة
st.markdown(f"""
    <style>
    /* 1. خلفية التطبيق (تدرج لوني رومانسي) */
    .stApp {{
        background: linear-gradient(135deg, #1a0a10 0%, #4a1020 50%, #1a0a10 100%) !important;
        background-attachment: fixed;
    }}

    /* 2. تنسيق العنوان والنصوص */
    h1, h3, p, span {{
        color: #ffb3c1 !important;
        text-shadow: 2px 2px 10px rgba(255, 75, 75, 0.5);
        text-align: center;
    }}

    /* 3. زر YES: المربع والنص العملاق */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.35}px !important;
        background: linear-gradient(145deg, #28a745, #1e7e34) !important;
        color: white !important;
        border: 3px solid #ffb3c1 !important;
        border-radius: 25px !important;
        font-weight: 900 !important;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0px 0px 50px rgba(40, 167, 69, 0.6) !important;
        transition: 0.3s;
    }}
    
    /* 4. زر no: الصغير الهارب */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(20, st.session_state.scale_no)}px !important;
        height: {max(20, st.session_state.scale_no)}px !important;
        font-size: {max(6, st.session_state.scale_no * 0.3)}px !important;
        background-color: #dc3545 !important;
        color: rgba(255,255,255,0.8) !important;
        border-radius: 8px !important;
        border: none !important;
    }}

    /* 5. أنيميشن القلوب المتساقطة (عند الفوز) */
    @keyframes falling {{
        0% {{ transform: translateY(-10vh) rotate(0deg); }}
        100% {{ transform: translateY(110vh) rotate(360deg); }}
    }}
    .heart {{
        position: fixed;
        color: #ff4d6d;
        font-size: 35px;
        user-select: none;
        z-index: 1000;
        animation: falling 3s linear infinite;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. واجهة المستخدم
st.write("# 💖 Final Decision 💖")
st.write("### Do you Love ME?")

# 4. تشغيل مطر القلوب عند الضغط على YES
if st.session_state.show_hearts:
    hearts_html = "".join([f'<div class="heart" style="left:{random.
