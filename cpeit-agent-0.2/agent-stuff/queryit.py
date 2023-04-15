import openai
import os

openai.api_key = "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"

def get_cpe(line):
    prompt = f"What is the NIST CPE for {line}?"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    cpe = response.choices[0].text.strip()
    return cpe

with open("input.txt", "r") as f:
    lines = f.readlines()

with open("output.txt", "w") as f:
    for line in lines:
        cpe = get_cpe(line.strip())
        f.write(cpe + "\n")
