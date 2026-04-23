import streamlit as st
import random

st.set_page_config(page_title="You Can't Catch Me!", page_icon="👻")

# 1. الذاكرة لحفظ الأحجام وأماكن الأزرار
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 60
if 'no_size' not in st.session_state:
    st.session_state.no_size = 60
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2] # ترتيب افتراضي للأعمدة

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS للأحجام والمربعات
st.markdown(f"""
    <style>
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {max(10, st.session_state.yes_size // 4)}px !important;
        background-color: #28a745 !important;
        color: white !important;
    }}
    div[data-testid="stHorizontalBlock"] div:nth-child(2) button {{
        width: {max(10, st.session_state.no_size)}px !important;
        height: {max(10, st.session_state.no_size)}px !important;
        font-size: {max(2, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. إنشاء 3 أعمدة وتغيير ترتيب الأزرار فيها عشوائياً
cols = st.columns([1, 1, 1])

# مصفوفة تحتوي على العمليات
def draw_yes():
    if cols[st.session_state.order[0]].button("YES", key="btn_yes"):
        st.balloons()
        st.success("Victory! ❤️")

def draw_no():
    if cols[st.session_state.order[1]].button("no", key="btn_no"):
        # تغيير الحجم + تغيير الترتيب عشوائياً
        st.session_state.yes_size += 40
        st.session_state.no_size -= 10
        random.shuffle(st.session_state.order) # خلط ترتيب الأعمدة
        st.rerun()

# تنفيذ الرسم بناءً على الترتيب العشوائي في الذاكرة
draw_yes()
draw_no()
