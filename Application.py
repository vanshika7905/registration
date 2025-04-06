import streamlit as st
st.header("Student Registration Form") #title of the form
st.subheader("Fill the form below")#sub title of the form
st.markdown("Please fill in the details below to register")#description of the form
name= st.text_input("Enter your name: ")#input box for name
fname= st.text_input("Enter your father's name: ")
adr= st.text_area("Enter your Address: ")#input box which can take multiple lines
classdat=st.selectbox("Select your class:",(1,2,3,4))#select box which helps in selecting classes

button=st.button("Submit")#submit button
if button:
    st.markdown(f"""
                Name:{name}
                Father's name:{fname}
                Address:{adr}
                class:{classdat}
                """)#markdown is used to display the data in a formatted way 
    st.success("Data submitted successfully!")#success message after submission
    st.balloons()#ballons will be shown after submission