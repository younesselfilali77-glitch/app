import streamlit as st
import random

st.set_page_config(page_title="Love Trap v2", page_icon="❤️")

# 1. تهيئة الأحجام لتكون متساوية في أول مرة (120px لكل منهما)
if 'scale_yes' not in st.session_state:
    st.session_state.scale_yes = 120
if 'scale_no' not in st.session_state:
    st.session_state.scale_no = 120
if 'order' not in st.session_state:
    st.session_state.order = [0, 1, 2]
if 'show_hearts' not in st.session_state:
    st.session_state.show_hearts = False

# ---------------------------------------------------------
# اختر الثيم الذي تفضله (Theme 1 أو Theme 2)
# ---------------------------------------------------------
theme = "Theme 1" # غيرها لـ "Theme 2" لتجربة الشكل الآخر

if theme == "Theme 1":
    # ثيم وردي ناعم (Soft Pink)
    bg_gradient = "linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%)"
    text_color = "#d63384"
else:
    # ثيم ليلي رومانسي (Deep Night Love
