import json

with open("data/skills.json", "r", encoding="utf-8") as f:
    data = json.load(f)

skills = []

for skill in data:

    skills.append(
        {
            "skill": skill.get("keyskill")
        }
    )

with open("data/skills.json", "w", encoding="utf-8") as f:

    json.dump(skills, f, indent=4)