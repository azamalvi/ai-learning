name= "Azam"
skills = ["Python", "AWS", "PHP"]
experience = {
    "company": "Tech Solutions",
    "experience": 3
}

def display_experience(exp):
    print(f"{name} has {exp['experience']} years of experience at {exp['company']}")

# for skill in skills:
#     print(f"{name} has skill in {skill}")

class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Added skill: {skill}")

# create a Developer instance
#dev = Developer(name, skills)
#dev.add_skill('JavaScript')
#print(skills)

# please provide code that multiply an array with 3 then calculate mean and then normalize the array
import numpy as np
data = np.array([1, 2, 3, 4, 5])
# Multiply array with 3
multiplied_data = data * 3
# Calculate mean
mean_value = np.mean(multiplied_data)
# Normalize the array
normalized_data = (multiplied_data - np.min(multiplied_data)) / (np.max(multiplied_data) - np.min(multiplied_data))
print("Multiplied Data:", multiplied_data)
print("Mean Value:", mean_value)
print("Normalized Data:", normalized_data)

# Create a 2D NumPy array representing: height, weight, gender
people = np.array([[170, 70, 'M'],
                   [160, 60, 'F'],
                   [180, 80, 'M'],
                   [165, 55, 'F']])
print("People Array:\n", people)


