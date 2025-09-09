import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("column1")
    st.write("bfdbvbvbfdvjhbjhdfvjhbdhbvjh")

with col2:
    st.header("column2")
    st.write("bfdbvbvbfdvjhbjhdfvjhbdhbvjh")

with col3:
    st.header("column3")
    st.write("bfdbvbvbfdvjhbjhdfvjhbdhbvjh")

with col4:
    st.header("column4")
    st.write("bfdbvbvbfdvjhbjhdfvjhbdhbvjh")

with col5:
    st.header("column5")
    st.write("bfdbvbvbfdvjhbjhdfvjhbdhbvjh")

with st.container():
    st.header("container")
    st.write("dhsjkhdkhfusdhihfsjjkfhjksbhfjkh")

st.write("bdgsjdgjsdjgsj")