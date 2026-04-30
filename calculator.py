import streamlit as st

st.set_page_config(page_title="Blino Calculator", page_icon="🧮",layout="wide", initial_sidebar_state= "auto", menu_items={
    "Get Help": "https://yoursite.com/help",
        "Report a bug": "https://yoursite.com/bugs",
        "About": "# Blino Supermart\n***Built by Blino Solu***."})


st.header("🧮 Blino Calculator")

with st.form("calculator", clear_on_submit=True):
    col_a, col_b, col_c = st.columns([1, 0.5, 1])
    Num1=col_a.number_input('your number', key="quantity_1",)
    Arit=col_b.selectbox('Sign', options=["+", "-", "*", "/", "//", "%", "^"])
    Num2=col_c.number_input('your number', key="quantity_2")
    submitted = st.form_submit_button("Calculate")

if submitted:
    if Arit=='+':
        result = Num1+Num2
    elif Arit=='-':
         result = Num1-Num2
    elif Arit=='/':
         if Num2 !=0:
              result = Num1/Num2
         else:
            result = "CAN'T DIVIDE BY ZERO!" 
    elif Arit=='//':
        if Num2 !=0:
            result = Num1/Num2
        else:
            result = "CAN'T DIVIDE BY ZERO!" 
    elif Arit=='*':
        result = Num1*Num2
    elif Arit=='^':
        result = Num1**Num2
    elif Arit=='%':
         result = (Num1/100)*Num2

    st.success(f"Result: {result}")


    
   
   
