from langchain_core.prompts import PromptTemplate

# Prompt Template
prompt_template = PromptTemplate(
    template="""
You explain research papers clearly and accurately.

Write an explanation of the paper "{paper_input}" using the selected options:
• Style: {style_input}
• Length: {length_input}

Guidelines:
- Match the tone and depth to the selected style.
- Keep the explanation within the chosen length.
- If the style is "Code-Oriented", include simple pseudocode where helpful.
- If the style is "Mathematical", describe formulas and intuition clearly.
- If the paper lacks information needed for a section, state: "Insufficient information available."
- Avoid adding details that are not supported by the original paper.

Now provide the explanation.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)



# Save the template to a json file
prompt_template.save("highly_efficient_prompt.json")

# Prompt Template 
# prompt_template = PromptTemplate(
#     template="""
#     You are an expert in explaining research papers.
#     Explain the research paper '{paper_input}' in a {style_input} style with a {length_input} length.
#     """,
#     input_variables=["paper_input", "style_input", "length_input"], 
#     validate_template=True
# )