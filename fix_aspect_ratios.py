with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace all vertical aspect ratios to horizontal ones so all cards match in size
content = content.replace('padding-top:177.78%;', 'padding-top:56.25%;')
content = content.replace('aspect="0.5625"', 'aspect="1.7777777777777777"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Aspect ratios fixed")
