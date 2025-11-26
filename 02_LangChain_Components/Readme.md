# LangChain Components

LangChain provides modular building blocks that help you create powerful applications using large language models. Each component plays a specific role and can be combined with others to form complete LLM powered workflows.

## 1. Models
Models are the core engine of the system. LangChain supports:
- Chat models  
- Text completion models  
- Embedding models  
- Local and cloud based models  

They can be easily swapped depending on your application needs.

## 2. Prompts
Prompts define how you interact with a model. LangChain provides:
- Prompt templates  
- Chat prompt templates  
- Dynamic and partial prompts  

These tools help you build reusable and well structured prompt designs.

## 3. Memory
Memory stores the conversation or context across user interactions. Types include
- Buffer memory  
- Summary memory  
- Key value memory  
- Combined memory  

Memory allows the application to behave like an intelligent conversational system.

## 4. Indexes and Document Loaders
These convert unstructured text into searchable formats.
- Document loaders for PDFs, websites, text files  
- Vector stores for semantic search  
- Embeddings to represent text mathematically  

This enables retrieval augmented generation for applications that answer from your own data.

## 5. Chains
Chains define a sequence of steps that run in order.
- Simple chains  
- Sequential chains  
- Router chains  
- Custom logic chains  

They ensure predictable and repeatable LLM workflows.

## 6. Tools
Tools expand what a model can do by giving it external capabilities.
Examples:
- Web search  
- APIs  
- Calculators  
- Databases  
- Code execution  

Tools let the model interact with the real world.

## 7. Agents
Agents intelligently decide which tool to use at each step. They combine:
- Reasoning  
- Planning  
- Decision making  
- Tool calling  

Agents allow you to build autonomous LLM applications.

## 8. Callback System
Callbacks give you visibility into what the model is doing.
- Logging  
- Token streaming  
- Monitoring  
- Debugging  

Useful for development and production deployment.

## Summary
LangChain Components work together to create flexible, scalable, and powerful AI applications. You can mix and match models, prompts, memory, tools, chains, and agents to design custom workflows tailored to your use case.
