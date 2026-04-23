import streamlit as st

st.set_page_config(page_title="The Trap", page_icon="⏹️")

# الذاكرة
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 60  
if 'no_size' not in st.session_state:
    st.session_state.no_size = 60   

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# استخدام CSS دقيق جداً باستخدام الـ Key (مفتاح الزر)
st.markdown(f"""
    <style>
    /* زر نعم - أخضر ويكبر */
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {{
        width: {st.session_state.yes_size}px !important;
        height: {st.session_state.yes_size}px !important;
        font-size: {max(10, st.session_state.yes_size // 4)}px !important;
        background-color: #28a745 !important;
        color: white !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    
    /* زر لا - أحمر ويصغر */
    div[data-testid="stHorizontalBlock"] div:nth-child(2) button {{
        width: {max(5, st.session_state.no_size)}px !important;
        height: {max(5, st.session_state.no_size)}px !important;
        font-size: {max(2, st.session_state.no_size // 4)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("YES", key="btn_yes"):
        st.balloons()
        st.success("Victory! ❤️")

with col2:
    if st.button("no", key="btn_no"):
        # التعديل هنا: نرفع واحد وننزل الآخر
        st.session_state.yes_size += 50
        st.session_state.no_size -= 10
        st.rerun()
