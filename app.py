import streamlit as st
import random

st.set_page_config(page_title="Real Square Trap", page_icon="⏹️")

# الذاكرة لحفظ الأحجام والترتيب
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 100
if 'no_size' not in st.session_state:
    st.session_state.no_size = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# كود CSS لإجبار الشكل المربع وتكبير النص
st.markdown(f"""
    <style>
    /* تنسيق زر YES: مربع مثالي ونص عملاق */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important; /* نفس العرض لضمان المربع */
        font-size: {st.session_state.yes_size // 3}px !important; /* النص يكبر مع المربع */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 15px;
        font-weight: bold !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        line-height: 1 !important;
    }}
    
    /* تنسيق زر no: مربع يصغر */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(25, st.session_state.no_size)}px !important;
        height: {max(25, st.session_state.no_size)}px !important;
        font-size: {max(8, st.session_state.no_size // 3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    </style>
""", unsafe_allow_html=True)

cols = st.columns([1, 1, 1])

# زر YES
with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("Victory! ❤️")

# زر no
with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        st.session_state.yes_size += 70 # تكبير سريع
        if st.session_state.no_size > 20:
            st.session_state.no_size -= 10
        
        # تغيير الأماكن عشوائياً
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.rerun()
