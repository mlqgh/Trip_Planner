import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

load_dotenv()

class ConfigLoader:
    def __init__(self):
        pass

    def __getitem__(self, key):
       return self.config[key]
class ModelLoader(BaseModel): 
    model_provider:Literal["openai", "groq"]='groq'
    config:Optional[ConfigLoader]=Field(default=None, exclude=True)

    def model_post_init__(self,__context:Any):
        self.config=ConfigLoader()
class config:
    arbitrary_types_allowed = True
    def load_llm(self):
        #load and return llm model based on the model_provider and model_name
        print('llm Loading... ')
        print(f'provider: {self.model_provider}')
        if self.model_provider=='groq':
            groq_api_key= os.getenv('GROQ_API_KEY')
            model_name=self.config['llm']['groq']['model_name']
            llm=ChatGroq(model_name=model_name, api_key=groq_api_key)
        elif self.model_provider=='openai':
            openai_api_key= os.getenv('OPENAI_API_KEY')
            model_name=self.config['llm']['openai']['model_name']
            llm=ChatOpenAI(model_name=model_name, api_key=openai_api_key)
        return llm