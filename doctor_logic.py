import os
#this might get changed to os.environ.get("GROQ_API_KEY") if you want to use a different method of getting the key
GROQ_KEY= os.getenv("GROQ_API_KEY")
#2. convert image to required format

import base64
image_path="acne.jpg"
image_file=open(image_path,"rb")
encoded_image=base64.b64encode(image_file.read()).decode("utf-8")
#3. setup multimodal llm

from groq import Groq
query="You are a doctor. Please analyze the image and provide a diagnosis based on the symptoms shown in the image. Please provide a detailed explanation of the condition and any recommended treatments."
model="meta-llama/llama-4-scout-17b-16e-instruct"
messages=[
    {
        "role":"user",
        "content": [
            #image model has two queries, one text and one image
            {
                #text query
                
                "type": "text",
                "text": query
            },
            {
                #image query

                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }
            }
        ]
    }
]
client=Groq()
chat_response=client.chat.completions.create(
    messages=messages,
    model=model,
)
print(chat_response.choices[0].message.content)
