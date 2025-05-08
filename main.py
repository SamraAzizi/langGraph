from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


load_dotenv()

llm = init_chat_model(
    "anthropic:claude-3-5-sonnet-latest"
)

class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires and emotional (therapist) or logical response"
    )




class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None


def classify_message(state: State):
    last_message = state["message"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
        "role": "system",
        "content": ""
    ])


def router(state: State):
    pass

def therapist_agent(state: State):
    pass

def logical_agent(state: State)


graph_builder = StateGraph(State)


graph = graph_builder.compile()

