# AI Voice Interviewer & Avatar with Python and LangGraph

An AI-powered virtual interviewer designed to automate the first round of candidate screening for HR teams and recruiters. This application conducts real-time, bidirectional voice interviews, dynamically asks structured interview questions, and features a visual AI avatar. It intelligently manages the conversation flow, records candidate responses into a local text file for later review, and uses a local vector database to accurately answer candidate questions about the company.

---

##  Key Features

###  Fully Conversational Voice Interface (No Text Interaction)
- The entire interview is conducted via **voice only**  
- No typing, no chat UI, no text prompts  
- The AI **speaks questions** and **listens to candidate responses**  
- Creates a natural, human-like interview experience  


###  Agentic Conversation Routing
Built with **LangGraph** to control conditional branching. The agent's "brain" evaluates real-time user input to dynamically decide whether to:
- Generate a direct response  
- Execute a tool to record a candidate's answer  
- Execute a tool to retrieve company data  

---

###  Real-Time Voice Pipeline
Powered by **LiveKit**, the system integrates ultra-low latency models to:
- Convert user speech to text  
- Process it through an LLM  
- Generate natural conversational audio responses  

---

### Local RAG (Retrieval-Augmented Generation)
Enables candidates to ask questions about the company:
- Processes PDF documents into chunks  
- Generates embeddings  
- Searches a local vector database  
- Retrieves accurate, context-aware answers  

---

###  Automated Note-Taking
- Listens to candidate responses  
- Automatically stores them in a structured `interview_answers.txt` file  
- Simplifies HR review and evaluation  

---

###  Visual AI Avatar
- Integrates an animated AI face  
- Enhances realism and engagement  
- Creates a more interactive interview experience  

---

##  Tech Stack

###  Frameworks & Orchestration
- Python  
- LangGraph  
- LangChain  
- LiveKit  

###  AI Models & Voice Pipeline
- OpenAI (LLM & Embeddings)  
- Deepgram (Speech-to-Text)  
- Cartesia (Text-to-Speech)  

###  Vector Database & Document Processing
- Chroma (Local Vector Store)  
- PyPDFLoader (PDF parsing & chunking)  

###  Visuals
- LemonSlice (Virtual Avatar Integration)

## Run the agent:
Open the livekit playground and select your current agent at 
https://agents-playground.livekit.io/ <br>

### Refer to official documentation:
https://docs.livekit.io/agents/ <br>
https://lemonslice.com/
