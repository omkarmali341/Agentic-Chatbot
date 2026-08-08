from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state_module import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder():
    def __init__(self,model):
        self.model = model
        self.state_graph=StateGraph(State)
    def basic_chatbot_build_graph(self):
        """
        Biuilds a basic chatbot graph using langgraph.
        This method initializes the state graph and adds nodes and edges to create a simple chatbot flow. 
        The graph consists of a start node, a user input node, a model response node, and an end node. 
        The edges define the flow of the conversation from the start to the end.
        
      """
        self.basic_chatbot_node=BasicChatbotNode(self.model)


        self.state_graph.add_node("chatbot",self.basic_chatbot_node.process)
        self.state_graph.add_edge(START,"chatbot")
        self.state_graph.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """"Setup graph for selected usecase"""
        if usecase=="Basic Chatbot":

            self.basic_chatbot_build_graph()


        return self.state_graph.compile()
    