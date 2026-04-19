import requests

fact = requests.get("https://uselessfacts.jsph.pl/random.json?language=en").json()["text"]

with open("FACT.md", "w") as f:
    f.write(f"## 🧠 Fact of the Day\n\n> {fact}\n")
