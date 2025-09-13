from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from openai import RateLimitError

load_dotenv()

def generate_pet_name(animal_type, pet_color, api_key=None):
    try:
        # 檢查是否有 API key
        if not api_key and not os.getenv("OPENAI_API_KEY"):
            return "錯誤：請提供 OpenAI API Key"
        
        # 使用提供的 API key 或環境變量中的 API key
        openai_api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        model_name = "gpt-3.5-turbo-instruct"
        llm = OpenAI(model=model_name, temperature=0.7, openai_api_key=openai_api_key)

        prompt_template_name = PromptTemplate(
            input_variables=["animal_type", "pet_color"],
            template=f"I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
        )

        name_chain = prompt_template_name | llm
        response = name_chain.invoke({"animal_type": animal_type, "pet_color": pet_color})

        return response
    
    except RateLimitError:
        return "錯誤：OpenAI API 配額不足，請檢查你的帳戶餘額和計費詳情"
    except Exception as e:
        return f"發生錯誤：{str(e)}"

if __name__ == "__main__":
    print(generate_pet_name("cow", "black"))