import streamlit as st

st.title("👋 사용자 인사 애플리케이션")

name = st.text_input("이름을 입력하세요:")

if st.button("환영 인사 받기"):

    greeting = "안녕하세요! " + name + "님, 첫 번째 Streamlit 애플리케이션에 오신 것을 환영합니다!😎"
    st.success(greeting)


