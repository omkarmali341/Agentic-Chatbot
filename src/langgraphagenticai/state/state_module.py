from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    A TypedDict representing the state of the application.

    Attributes:
        messages (List[Annotated[dict, "message"]]): A list of messages in the application state.
    """
    messages: Annotated[List, add_messages]
    