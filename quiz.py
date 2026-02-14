import pandas as pd

print("Welcome to Smart Quiz System")

data = pd.read_excel("quiz_questions.xlsx", header=4)

score = 0
total_questions = len(data)

for i in range(len(data)):
    print("\nQuestion:", data["QUESTIONS"][i])
    print("A)", data["A"][i])
    print("B)", data["B"][i])
    print("C)", data["C"][i])

    ans = input("Enter option (A/B/C): ")

    if ans.upper() == data["CORRECT"][i].upper():
        print("Correct")
        score += 1
    else:
        print(f"Wrong! Correct answer:{data['CORRECT'][i]}")

print(f"Your final score is:{score}/{total_questions}")

    


