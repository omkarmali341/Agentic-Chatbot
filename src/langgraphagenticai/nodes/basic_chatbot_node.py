from src.langgraphagenticai.state import State



class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a LangGraph Agentic AI system.
    This contains basic chatbot logic implementation]"""

    def __init__(self, model):
        self.llm = model

    def process(self, state=State)->dict:

        """
        Processes the input and generate the chatbot response

       """
        return{"messages":self.llm.invoke(state['messages'])}