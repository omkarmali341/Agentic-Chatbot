import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLm:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            Groq_api_key=self.user_controls_input.get('Groq_api_key')
            model_selection=self.user_controls_input.get('model_selection')
            if  Groq_api_key =='' or os.environ.get('Groq_api_key')=='':
                st.warning("Please enter your Groq API key to proceed.")

            llm=ChatGroq(
                api_key=Groq_api_key,model=model_selection
            )

        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")
        return llm

        