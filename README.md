# langGraph

langGraph is a conversational chatbot built using LangGraph and LangChain, capable of routing user input between emotional and logical agents. It uses Claude 3.5 Sonnet as the backend language model to classify and respond to user messages appropriately. This project demonstrates how to use a structured state graph and message routing to create an AI assistant that can switch roles dynamically—acting as a therapist or a logical assistant based on message context.


##  Features

-  **Automatic Classification**: Classifies messages as emotional or logical.
-  **Therapist Agent**: Responds empathetically, focusing on emotional support.
-  **Logical Agent**: Delivers fact-based, analytical answers without addressing feelings.
-  **State Graph Architecture**: Built using LangGraph's state graph architecture.


##  Installation

To install and set up the project locally, follow these steps:

1. Clone the repository:

```bash
   git clone https://github.com/SamraAzizi/langGraph.git
   cd langGraph

```
2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```  
3. Install dependencies:
```bash

pip install -r requirements.txt
```

4. Set up environment variables in a .env file:
```bash
# Example .env
ANTHROPIC_API_KEY=your_api_key_here
```

### Usage

Run the chatbot interactively in your terminal:

```bash
python main.py
```


Type messages to interact. To exit the chatbot, type:

```bash
exit
```


### How It Works
- Classification: Uses Claude 3.5 to classify user input as emotional or logical.
- Routing: Based on classification, routes the message to the appropriate agent.

#### Agent Response:

- Therapist: Empathetic, avoids logic unless asked.
- Therapist: Empathetic, avoids logic unless asked.

### Project Structure

```bash
├── main.py              # Main chatbot script
├── .env                 # API keys and environment config
├── requirements.txt     # Python dependencies

```

### To Do
- Improve handling of long conversations
- Add memory/persistence for better context retention
- Deploy as a web app using Streamlit or FastAPI