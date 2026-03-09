import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

KEYS = [
    ("KEY_1", os.getenv("GOOGLE_API_KEY_1")),
    ("KEY_2", os.getenv("GOOGLE_API_KEY_2")),
]

for key_name, key in KEYS:
    if not key:
        print(f"{key_name}: No key found")
        continue
    print(f"\n=== Testing {key_name}: {key[:10]}... ===")
    genai.configure(api_key=key)
    try:
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                print(f"  Available: {m.name}")
    except Exception as e:
        print(f"  Error: {e}")
