import streamlit as st
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Final Love Trap", page_icon="❤️", layout="centered")

# 2. تهيئة الذاكرة (Session State)
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'answered_yes' not in st.session_state:
    st.session_state.answered_yes = False

# ألوان الثيم
bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
txt = "#d63384"

# 3. كود الـ CSS لتنسيق الأزرار والخلفية
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg} !important;
    }}
    [data-testid="stHorizontalBlock"] {{
        align-items: center !important;
        justify-content: center !important;
        gap: 20px !important;
    }}
    .stButton > button {{
        transition: all 0.4s ease !important;
        border: none !important;
    }}
    /* تنسيق زر YES الديناميكي */
    div[data-testid="column"]:nth-child(1) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.2}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 50% !important;
    }}
    /* تنسيق زر NO الذي يصغر */
    div[data-testid="column"]:nth-child(2) button {{
        width: {max(40, st.session_state.scale_no)}px !important;
        height: {max(40, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.2)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
    }}
    @keyframes heartbeat {{
        0% {{ transform: scale(1); }}
        25% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); }}
    }}
    .big-heart {{
        font-size: 80px;
        text-align: center;
        animation: heartbeat 1.2s infinite;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. الجزء الأول: فخ الحب (The Trap)
if not st.session_state.answered_yes:
    st.markdown(f"<h1 style='color:{txt}; text-align:center;'>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:{txt}; text-align:center;'>Do you Love ME?</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("YES", key="btn_yes"):
            st.session_state.answered_yes = True
            st.balloons()
            st.rerun()

    with col2:
        if st.button("no", key="btn_no"):
            st.session_state.scale_yes += 50  # زر نعم يكبر
            st.session_state.scale_no -= 15   # زر لا يصغر
            st.rerun()

# 5. الجزء الثاني: يظهر فقط بعد الضغط على YES
else:
    st.markdown("<div class='big-heart'>❤️</div>", unsafe_allow_html=True)
    st.success("I knew it! ❤️🥰")
    
    st.divider()
    st.title("🚀 Youness Elite Web App")
    
    name = st.text_input("Who is visiting the app today?")
    
    if name:
        user_name = name.strip().lower()
        
        if user_name == "youness":
            st.balloons()
            st.success("Welcome Boss! You are in love with Ikram! ❤️")
            
        elif user_name == "anas":
            st.snow()
            st.warning("You are in love with (7choma nktb smitha) 🤫")
            
        elif user_name == "ikram":
            st.balloons()
            st.markdown("<div class='big-heart'>❤️</div>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center; color: #d63384;'>I love you more than you know 💗🫶🏻</h2>", unsafe_allow_html=True)
            
        else:
            st.info(f"Hiii {name}! Nice to meet you.")
