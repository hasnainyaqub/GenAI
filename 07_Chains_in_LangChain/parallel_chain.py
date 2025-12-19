from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from os import getenv
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

load_dotenv()

# Initialize the Groq model
model1 = ChatGroq(model='llama-3.3-70b-versatile', temperature=0)
# Initialize the OpenRouter
model2 = ChatOpenAI(
                    api_key=getenv("OPENROUTER_API_KEY"),
                    model='deepseek/deepseek-r1', 
                    base_url="https://openrouter.ai/api/v1", 
                    temperature=0
)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text:\n{text}',
    input_variables=['text'],
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text:\n {text}.',
    input_variables=['text'],
)

prompt3 = PromptTemplate(
    template='Merge the following notes and Q&A into a concise summary:\nNotes: {notes}\nQ&A: {qa}',
    input_variables=['notes', 'qa'],
)

parser = StrOutputParser()

chain = RunnableParallel(
    {
        'notes': prompt1 | model1 | parser,
        'qa': prompt2 | model2 | parser,
    }
) | prompt3 | model2 | parser

text = """Artificial intelligence (AI) is a set of technologies that empowers computers to learn, reason, and perform a variety of advanced tasks in ways that used to require human intelligence, such as understanding language, analyzing data, and even providing helpful suggestions. It’s a transformational technology that can bring meaningful and positive change to people and societies and the world.

It encompasses many different disciplines, including computer science, data analytics and statistics, hardware and software engineering, linguistics, neuroscience, and even philosophy and psychology. 

AI is about teaching computers to do the amazing things our own brains can do, from understanding the world around them to learning new things and even coming up with fresh ideas. For instance, AI is used in optical character recognition (OCR) to pull text and data from various images and documents. This process transforms unstructured content into structured, business-ready data, helping uncover valuable insights.

How does AI work?
Artificial intelligence techniques, though diverse, all fundamentally rely on data, algorithms, and computational power. AI systems learn and improve through exposure to vast amounts of data, identifying patterns and relationships that humans might miss. This data serves as the training material, the quality and quantity of which are crucial for the AI's performance.

As mentioned earlier, AI isn't a single technology but a broad field encompassing several key areas:

Machine Learning (ML): This is a type of AI where systems learn from data to identify patterns and make predictions or decisions without direct programming. Imagine teaching a computer to recognize a bird by showing it thousands of bird pictures; it learns what a bird looks like on its own.
Deep Learning (DL): A subfield of ML, deep learning uses artificial neural networks with many layers (hence "deep") to learn from data. These networks are inspired by the structure of the human brain and are particularly good at complex tasks like image and speech recognition.
Natural Language Processing (NLP): NLP enables computers to understand, interpret, and generate human language. This is what powers voice assistants like Siri and Alexa, translation services, and chatbots.
Computer Vision: This area allows computers to "see" and interpret visual information from the world, such as images and videos. It's used in everything from facial recognition to self-driving cars.
Want to learn how to get started with AI? Take the free beginner's introduction to generative AI.

Types of artificial intelligence
Artificial intelligence can be organized in several ways, depending on stages of development or actions being performed. 

AI types of capability
This classification defines AI models based on their intelligence level and problem-solving abilities.

Artificial Narrow Intelligence (ANI): This is the only form of AI that currently exists. ANI models are designed to perform a single, specific task, such as identifying images, engaging in chat, or filtering emails. Examples include voice assistants, facial recognition technology, and generative AI models like Gemini and other large language models (LLMs). Despite its name, ANI does not possess reasoning or self-awareness; instead, it combines data with an algorithm to make predictions within predefined parameters. While ANI offers many benefits, it also carries risks, as poor training data can lead to biased or inaccurate outputs, which can be critical in applications like loan approvals, hiring decisions, and predictive policing. Cybercriminals can also potentially exploit ANI to create sophisticated AI-driven scams. 
Artificial General Intelligence (AGI): This is a proposed future step in AI technology. Theoretically, AGI would be capable of performing a broad range of tasks and would utilize human-like reasoning to learn, adapt, and improve. AGI does not yet exist. Unlike ANI, AGI is expected to be adaptive, autonomous, and capable of learning from its actions. Fictional examples include droids from Star Wars. However, AGI may raise significant safety and ethical concerns, as malicious actors could program AGI with harmful intent, leading to potentially limitless destructive capabilities if unregulated.
Artificial Superintelligence (ASI): This is the most advanced theoretical form of AI. ASI would be a self-aware entity operating beyond human control, significantly surpassing human intelligence in reasoning, creativity, and even emotional intelligence. Like other forms of AI, there are concerns that ASI could pose an existential threat to humanity, with some AI researchers suggesting a non-negligible chance of extremely bad outcomes, including human extinction.
AI types by functionality
This classification categorizes AI based on how it operates and interacts in specific contexts.

Reactive machines: Limited AI that only reacts to different kinds of stimuli based on preprogrammed rules. It lacks memory and therefore cannot learn from new data. A notable example is IBM’s Deep Blue, which defeated chess champion Garry Kasparov in 1997.
Limited memory: Most modern AI is limited memory. It can use memory to improve over time by training on new data, typically through an artificial neural network or other training model. This memory is short-term; once a session ends, the memory often resets. Examples include self-driving cars observing other vehicles and chatbots like Gemini remembering previous messages in a conversation.
Theory of mind: Theory of mind AI doesn't currently exist (yet), but research is ongoing into its possibilities. It describes AI that can emulate the human mind and have decision-making capabilities equal to that of a human, including the ability to recognize and remember emotions and react in social situations as a human would."""

result = chain.invoke({'text': text})
print(result)

chain.get_graph().print_ascii()  