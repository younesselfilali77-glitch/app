import streamlit as st
import random

st.set_page_config(page_title="The Love Boss", page_icon="❤️")

# 1. الذاكرة للأحجام (جعلنا البداية أكبر والنمو أسرع)
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 150 # حجم بداية أكبر
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 80
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

st.title("Final Decision... 🙄")
st.subheader("Do you Love ME?")

# 2. كود CSS للسيطرة الكاملة على حجم المربع والنص
st.markdown(f"""
    <style>
    /* تنسيق زر YES: مربع ضخم جداً ونص يملأ الفراغ */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[0] + 1}) button {{
        width: {st.session_state.scale_yes}px !important;
        height: {st.session_state.scale_yes}px !important;
        font-size: {st.session_state.scale_yes * 0.35}px !important; /* نص عملاق متناسب */
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: 900 !important;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0px 0px 30px rgba(40, 167, 69, 0.5) !important;
    }}
    
    /* تنسيق زر no: مربع مجهري يصعب ضغطه */
    div[data-testid="stHorizontalBlock"] div:nth-child({st.session_state.order[1] + 1}) button {{
        width: {max(20, st.session_state.scale_no)}px !important;
        height: {max(20, st.session_state.scale_no)}px !important;
        font-size: {max(6, st.session_state.scale_no * 0.3)}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        border-radius: 5px !important;
    }}

    /* مطر القلوب المتساقطة */
    @keyframes falling {{
        0% {{ transform: translateY(-10vh) rotate(0deg); }}
        100% {{ transform: translateY(110vh) rotate(360deg); }}
    }}
    .heart {{
        position: fixed;
        color: #ff4b4b;
        font-size: 30px;
        user-select: none;
        z-index: 1000;
        animation: falling 3s linear infinite;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. تشغيل القلوب عند الفوز
if st.session_state.show_hearts:
    hearts = "".join([f'<div class="heart" style="left:{random.randint(0,95)}%; animation-duration:{random.uniform(2,4)}s;">❤️</div>' for _ in range(30)])
    st.markdown(hearts, unsafe_allow_html=True)
    st.success("I Love You Too! ❤️🥰🎉")

# 4. توزيع الأزرار
cols = st.columns([1, 1, 1])

with cols[st.session_state.order[0]]:
    if st.button("YES", key="btn_yes"):
        st.session_state.show_hearts = True
        st.rerun()

with cols[st.session_state.order[1]]:
    if st.button("no", key="btn_no"):
        # قفزة عملاقة في الحجم (زيادة 120 بيكسل في كل ضغطة)
        st.session_state.scale_yes += 120 
        st.session_state.scale_no -= 15
        
        # تغيير الأماكن عشوائياً ليهرب الزر
        new_order = [0, 1, 2]
        random.shuffle(new_order)
        st.session_state.order = new_order
        st.session_state.show_hearts = False
        st.rerun()
