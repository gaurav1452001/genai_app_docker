import os
#this might get changed to os.environ.get("GROQ_API_KEY") if you want to use a different method of getting the key
GROQ_KEY= os.getenv("GROQ_API_KEY")
#2. convert image to required format
#3. setup multimodal llm