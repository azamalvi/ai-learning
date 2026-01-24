def clean_score(scores: list[int]) -> list[int]:
    return [s for s in scores if s > 50]

print(clean_score([20,50,55,32]))