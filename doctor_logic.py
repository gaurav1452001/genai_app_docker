import os
#this might get changed to os.environ.get("GROQ_API_KEY") if you want to use a different method of getting the key
GROQ_KEY= os.getenv("GROQ_API_KEY")
#2. convert image to required format

import base64
image_path="acne.jpg"
image_file=open(image_path,"rb")
encode_image=base64.b64encode(image_file.read()).decode("utf-8")
#3. setup multimodal llm