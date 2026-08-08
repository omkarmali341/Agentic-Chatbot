import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import UIConfigFile

class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfigFile()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=" 🤖 " +self.config.get_page_title(),layout="wide")
        st.header("🤖 "+self.config.get_page_title())

        with st.sidebar:
            #Get Options from config file
            llm_options=self.config.get_llm_options()
            usercase_options= self.config.get_usecase_options()

            # LLM Selection
            self.user_controls['llm_selection'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['llm_selection'] == "Groq":
                # Model Selection
                model_options = self.config.get_model_options()
                self.user_controls['model_selection'] = st.selectbox("Select Model", model_options)
                self.user_controls['Groq_api_key']=st.session_state['Groq_api_key'] = st.text_input("API Key", type="password")

                # Validate API Key
                if not self.user_controls['Groq_api_key']:
                    st.warning("Please enter your Groq API key to proceed.")

            #select usecase
            self.user_controls['usecase_selection'] = st.selectbox("Select Use Case", usercase_options)

        return self.user_controls

