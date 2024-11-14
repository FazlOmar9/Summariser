import requests
from dotenv import load_dotenv
import os

load_dotenv()


def segmenter(text: list) -> list:
    url = 'https://segment.jina.ai/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("JINA_API_KEY")}'
    }
    chunks = []
    for i in text:
        data = {
            "content": i,
            "return_chunks": True,
            "max_chunk_length": 1000
        }

        response = requests.post(url, headers=headers, json=data)
        for j in list(response.json()['chunks']):
            chunks.append(j)
    return chunks
