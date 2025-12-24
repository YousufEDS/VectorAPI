import requests
import os
from dotenv import load_dotenv
import numpy as np
load_dotenv("config.env")

API_KEY = os.getenv("VECTORSHiFT_API_KEY")
if not API_KEY:
    raise RuntimeError("VECTORSHiFT_API_KEY not found")

PIPELINE_ID = "693ff161da24bfd708f3ac96"
RUN_URL = f"https://api.vectorshift.ai/v1/pipeline/{PIPELINE_ID}/run"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "inputs.Typology": "School",
    "inputs.Climate": "Cold"
}

files = {
    "SIM": (  
        "SIM_File.sim",
        open("SIM_File.sim", "rb"),
        "application/octet-stream"
    )
}

response = requests.post(
    RUN_URL,
    headers=headers,
    data=data,
    files=files,
    timeout=300
)

response_json = response.json()

formatted_text = response_json["outputs"]["output_0"]

print("STATUS:", response.status_code)
# print("RESPONSE:")
# output = response.text
# print(output)
print("FORMATTED RESPONSE:\n")
print(formatted_text)

# saving the output to a file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(formatted_text)