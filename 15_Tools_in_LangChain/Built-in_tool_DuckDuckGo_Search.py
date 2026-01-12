from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("Best programming language")

print(result)
print('===='*90)
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)