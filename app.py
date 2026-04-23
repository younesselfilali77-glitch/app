import streamlit as st
import random

st.set_page_config(page_title="Pixel Perfect Trap", page_icon="🖼️")

# 1. الذاكرة
if 'scale' not in st.session_state:
    st.session_state.scale = 100  # مقياس حجم YES
if 'no_scale' not in st.session_state:
    st.session_state.no_scale = 80 # مقياس حجم no
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS السحري: يربط كل شيء بمتغير الـ scale
st.markdown(f"""
    <style>
    /* تنسيق عام للأزرار لجعلها مربعة تماماً */
    .stButton > button {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
        border: none !important;
        transition: all 0.2s ease-in-out !important;
    }}

    /* زر YES: تكبير المربع والنص كأنهما صورة واحدة */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale}px !important;
        height: {st.session_state.scale}px !important;
        font-size: {st.session_state.scale * 0.35}px !important; /* النص دائماً 35% من حجم المربع */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: {st.session_state.scale * 0.1}px !important; /* انحناء الزوايا يتناسب مع الحجم */
    }}
    
    /* زر no: تصغير المربع والنص معاً */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(20, st.session_state.no_scale)}px !important;
        height: {max(20, st.session_state.no_scale)}px !important;
        font-size: {max(8, st.session_state.no_scale * 0.35)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: {max(2, st.session_state.no_scale * 0.1)}px !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. توزيع الأعمدة
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("You caught the BIG YES! ❤️")

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # تكبير YES وتصغير no
        st.session_state.scale += 80
        st.session_state.no_scale -= 15
        
        # تغيير الأماكن عشوائياً
        new_order = [0, 1, 2]
        random
