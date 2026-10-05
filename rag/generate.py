from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()


def generate(prompt:str):
    if len(prompt)==0:
        raise ValueError("prompt cant be empty")
    client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

    response=client.chat.completions.create(model="openai/gpt-oss-20b",
                                messages=[{
                                    "role":"user",
                                    "content":prompt
                                }])
    return response.choices[0].message.content

if __name__=="__main__":
    print(generate("Hello!"))