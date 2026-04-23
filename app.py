import streamlit as st
import random

st.set_page_config(page_title="The Big Trap", page_icon="⏹️")

# 1. الذاكرة لحفظ الأحجام والترتيب
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 100
if 'no_size' not in st.session_state:
    st.session_state.no_size = 60
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS لجعل النص يكبر مع المربع
st.markdown(f"""
    <style>
    /* تنسيق زر YES: النص يكبر بنسبة كبيرة ليملأ المربع */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {st.session_state.yes_size // 4}px !important; /* النص يكبر بنسبة 1/4 المربع */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px;
        font-weight: bold !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: 0.2s;
    }}
    
    /* تنسيق زر no: يصغر ويختفي نصياً */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(15, st.session_state.no_size)}px !important;
        height: {max(15, st.session_state.no_size)}px !important;
        font-size: {max(4, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. عرض الأزرار في 3 أعمدة للقفز العشوائي
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("VICTORY! ❤️🥳")

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # تكبير ضخم جداً لـ YES ونصها
        st.session_state.yes_size += 80 
        # تصغير لـ no
        if st.session_state.no_size > 10:
            st.session_state.no_size -= 10
        
        # تغيير الأماكن عشوائياً
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
