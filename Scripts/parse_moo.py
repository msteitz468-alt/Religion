import re

with open("raw/commentaries/Galatians (Baker Exegetical Commentary) - Douglas J. Moo.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's look for keywords like "historical-critical", "grammatico-historical", "redaction", "theological", "eschatological", "apocalyptic", "salvation-historical", "hermeneutic"
keywords = ["historical-critical", "grammatico", "redaction", "salvation-historical", "hermeneutic", "apocalyptic", "typological", "allegorical"]

snippets = []
for i, line in enumerate(text.split('\n')):
    if any(k.lower() in line.lower() for k in keywords):
        snippets.append(line.strip())

# print a sample of snippets to see how Moo describes his method
for s in snippets[:20]:
    print(s)
print("...")
for s in snippets[-20:]:
    print(s)

