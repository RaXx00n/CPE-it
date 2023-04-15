import openai
import json

openai.api_key = "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"

def get_cpe(name, publisher, version):
    prompt = f"What is the NIST CPE for {publisher} {name} {version}?"
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

with open("test3.json", "r") as f:
    software = json.load(f)

with open("output.txt", "w") as f:
    for s in software:
        name = s["Name"]
        publisher = s["Publisher"]
        version = s["Version"]
        cpe = get_cpe(name, publisher, version)
        f.write(cpe + "\n")
