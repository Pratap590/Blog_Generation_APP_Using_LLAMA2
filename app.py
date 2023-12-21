import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def llamaresponce(input_text, no_words, blog_style):
    llm = CTransformers(model = "D:\GenerativeAI_project\Bloge generation llm app\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type ="llama",
                        config ={'max_new_tokens':256,
                              'temperature':0.01})
      
    Template ='''
 Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.

'''
    prompts = PromptTemplate(input_variables=["input_text","no_words","blog_style"],
                         template=Template)

    response=llm(prompts.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title= "Bloge Generation App",
                   page_icon="🤖",
                   layout = "centered",
                   initial_sidebar_state="collapsed")
st.header("Bloge Generation App 🤖")

input_text = st.text_input("Enter Your Blog Topic")

col1, col2 =st.columns([5,5])

with col1:
    no_words = st.text_input("Enter the number of words")
with col2:
    blog_style = st.selectbox("Writing the blog for",
                              ("Data Scientist","ML engineer","Researchers","Common popole"), index=0)
submit =st.button("Generate")


if submit:
    st.write(llamaresponce(input_text, no_words, blog_style))

