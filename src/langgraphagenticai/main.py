import streamlit as st

##from src.langgraphagenticai import graph
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLm
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResult

def Load_langgraph_agentic_ai_ui():
    """
    This function loads the LangGraph Agentic AI UI using Streamlit.
    It initializes the UI configuration, sets up the page layout, and provides user controls for selecting LLMs, models, 
    and use cases. The function returns a dictionary containing the user's selections.  

    """
    ui_loader = LoadStreamlitUI()
    user_imput = ui_loader.load_streamlit_ui()


    if not user_imput:
        st.error("Error : Failed to load user input")
        return

    user_message = st.chat_input("Enter your message here...")

    if user_message:
        try:
            ## Configure the LLM
            obj_llm_config=GroqLLm(user_controls_input=user_imput)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error : Failed to initialize the LLM model")
                return

            ## Initialize the model and build the graph
            usecase=user_imput.get('usecase_selection')

            if not usecase:
                st.error("Error : Use case selection is missing")
                return

            ## Graph Building
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResult(usecase,graph,user_message).display_result_on_ui()
               

            except Exception as e:
                st.error(f"Error : Failed to build the graph: {e}")
                return
        except Exception as e:
            st.error(f"Unexpected error occurred: {e}")
            return
