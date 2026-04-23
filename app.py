import streamlit as st

# إضافة عنوان جميل مع رمز تعبيري
st.title("🚀 Youness Elite Web App")

# إضافة خط فاصل
st.divider()

name = st.text_input("Who is visiting today?")

if name:
    # تحويل الاسم لحروف صغيرة لضمان عمل الكود حتى لو كتب المستخدم Anas أو anas
    user_name = name.strip().lower()

    if user_name == "youness":
        st.balloons() # إضافة بالونات احتفالية!
        st.success("Welcome Boss! You are in love with Ikram! ❤️")
        
    elif user_name == "anas":
        st.snow() # إضافة تأثير الثلج!
        st.warning("You are in love with (7choma nktb smitha) 🤫")
        
    else:
        st.info(f"Hello {name}! Hope you're having a great day.")
