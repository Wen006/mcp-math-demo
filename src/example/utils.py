import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
# from langchain.chat_models import init_chat_model
# from langchain_core.language_models import BaseChatModel

load_dotenv()

def init_model(): 
    # 公网-Deepseek模型
    llm = ChatDeepSeek(
        model= os.getenv("DEEPSEEK_MODEL"),  # 尝试不同的模型名称
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    ## 不行坑比较多，可能是版本功能问题，初始化后的llm 总是报各种错误
    # llm = load_chat_model(f"{model_provider}/{model_name}",{
    #     "api_key": api_key,
    #     "base_url": base_url,
    #     # enable_auto_tool_choice: True,
    #     # tool_call_parser:True
    # })
    return llm;