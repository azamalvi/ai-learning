name= "Azam"
skills = ["Python", "AWS", "PHP"]
experience = {
    "company": "Tech Solutions",
    "experience": 3
}
tuple_example = ("Data Scientist", 5, "Remote")

def display_experience(exp):
    print(f"{name} has {exp['experience']} years of experience at {exp['company']}")

# for skill in skills:
#     print(f"{name} has skill in {skill}")

is_active: int = 10.9

def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

avg = calculate_average([10, 20, 30])
print(avg)
