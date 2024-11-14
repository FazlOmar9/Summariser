from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(api_key=os.getenv("HF_API_KEY"))

def summarize(pages: list, batch_limit: int = 10):
    content_length = len(pages)
    if (content_length == 0):
        print("Warning: No content to summarize")
        return 1
    iters = content_length // batch_limit + (content_length % batch_limit > 0)

    responses = []

    for i in range(iters):
        print(f"=================== Processing batch {i+1} of {iters} ===================")
        start = i * batch_limit
        end = min((i + 1) * batch_limit, content_length)

        content = ' '.join(pages[start:end])
            
        messages = [
        {
            "role": "system",
            "content": """You are an assistant and are an expert at summarizing 
            financial documents. For each part of content the user provides
            you should return a summarized one line each as points. No small talk
            , no other details. Just the points.
            """
        },
            {
                "role": "user",
                "content": f"Please give the summary for the following content: {content}"
            }
        ]

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct", 
            messages=messages,
        max_tokens=1024,
            stream=False
        )
        responses.append(response.choices[0].message.content)
        print(response.choices[0].message.content)

    return responses