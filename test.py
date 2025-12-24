name= "Azam"
skills = ["Python", "AWS", "PHP"]
experience = {
    "company": "Tech Solutions",
    "experience": 3
}

def display_experience(exp):
    print(f"{name} has {exp['experience']} years of experience at {exp['company']}")

for skill in skills:
    print(f"{name} has skill in {skill}")

class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Added skill: {skill}")

    add_skill('aa', 'xxx')