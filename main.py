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
        {
        "role": "system",
        "content": """Classif the user message as either:
        - 'emotional' : if it asks for the emotional support, therapy, deals with feelings, or personal problems
        - 'logical': if it asks for fact, information, logical analysis, or practical solutions """
        },
        {"role": "user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}


def router(state: State):
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}
    
    return {"next": "logical"}

def therapist_agent(state: State):
    last_message = state["message"][-1]

    messsages = [
        {"role": "system",
         "content": """You are a compationate therapist.Focus on the emotional aspects of the user's message.
         Show empathy, evaluate thier feelings, and help them process their emotions.
         Ask thoughful questions to help them explore their feelings more deeply.
         Avoid giving logical solutions unless explicitly asked."""}
    ]

def logical_agent(state: State)


graph_builder = StateGraph(State)


graph = graph_builder.compile()

