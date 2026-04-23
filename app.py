import streamlit as st
import random

st.set_page_config(page_title="Perfect Love Trap", page_icon="❤️", layout="centered")

# 1. تهيئة الأحجام
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120 
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ثيم وردي ناعم
bg = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
txt = "#d63384"

# 2. كود CSS السحري لضمان التمركز الأفقي والانتقال الناعم
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg} !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    /* حاوية الأزرار: تضمن بقاءهم بجانب بعضهم مهما حدث */
    [data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important; /* ضمان الترتيب الأفقي */
        flex-wrap: nowrap !important;  /* منع النزول لسطر جديد */
        align-items: center !important;
        justify-content: center !important;
        gap: 20px !important;
    }}

    .stButton > button {{
        transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; /* أنيميشن "سلايد" ناعم جداً */
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    /* تنسيق زر YES */
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.25}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }}
    
    /* تنسيق زر NO */
    div[data-testid="stHorizontalBlock"] div:nth-child(2) button {{
        width: {max(30, st.session_state.scale_no)}px !important;
        height: {max(30, st.session_state.scale_no)}px !important;
        font-size: {max(10, st.session_state.scale_no * 0.25)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 15px !important;
    }}

    /* القلوب في الخلفية */
    @keyframes fall {{ 
        0% {{ top: -10%; opacity: 1; }} 
        100% {{ top: 110%; opacity: 0; }} 
    }}
    .heart {{ position: fixed; font-size: 30px; animation: fall 3s linear infinite; z-index: 1; pointer-events: none; }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<h1 style='color:{txt}; text-align:center;'>💖 Final Decision 💖</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:{txt}; text-align:center;'>Do you Love ME?</h3>", unsafe_allow_html=True)

# 3. عرض القلوب عند الفوز
if st.session_state.show_hearts:
    hearts = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-delay:{random.uniform(0,2)}s;">❤️</div>' for _ in range(40)])
    st.markdown(hearts, unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰")

# 4. حاوية الأزرار (أفقية دائماً)
col1, col2 = st.columns(2)

with col1:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with col2:
    if st.button("no", key="btn_no"):
        # تكبير YES وتقليص NO
        st.session_state.scale_yes += 90 
        st.session_state.scale_no = max(30, st.session_state.scale_no - 15)
        st.rerun()
