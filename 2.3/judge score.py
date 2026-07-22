score = 0.0
for judge_number in range(1, 6):
    score += float(input("Judge " + str(judge_number) + ": "))
    final_score = score/5
print("final_score: " + str(final_score))
