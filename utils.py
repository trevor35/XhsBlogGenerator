import os

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from prompt_template import system_template_text, user_template_text
from Xhs_DataModel import Xhs

def get_XhsBlog(theme, api_key):
    prompt = ChatPromptTemplate.from_messages(
        [("system",system_template_text),
         ("human",user_template_text)]
    )

    model = ChatOpenAI(
        model="deepseek-r1-distill-llama-8b",
        openai_api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    parser = PydanticOutputParser(pydantic_object=Xhs)

    chain = prompt | model | parser

    result = chain.invoke({
        "parser_instructions": parser.get_format_instructions(),         # 告诉AI输出格式为JSON
        "theme": theme
    })

    return result

# if __name__ == '__main__':
#     print(get_XhsBlog("拍照", os.getenv("DASHSCOPE_API_KEY")))
