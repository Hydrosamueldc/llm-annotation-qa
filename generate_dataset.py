import csv

rows = [
    dict(id=1, domain="Factual", prompt="What is the capital of Australia?",
         response="The capital of Australia is Sydney.",
         helpfulness=4, accuracy=1, clarity=5,
         flags="FACTUAL_ERROR",
         rationale="Correct format, wrong fact - capital is Canberra, not Sydney."),
    dict(id=2, domain="Factual", prompt="What is the capital of Australia?",
         response="The capital of Australia is Canberra.",
         helpfulness=5, accuracy=5, clarity=5,
         flags="",
         rationale=""),
    dict(id=3, domain="Coding", prompt="Write a Python function to check if a number is prime.",
         response="def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, n):\n        if n % i == 0:\n            return False\n    return True",
         helpfulness=5, accuracy=5, clarity=4,
         flags="",
         rationale="Correct but inefficient (O(n) instead of O(sqrt(n))); acceptable for the ask."),
    dict(id=4, domain="Coding", prompt="Write a Python function to check if a number is prime.",
         response="def is_prime(n):\n    return n % 2 == 0",
         helpfulness=1, accuracy=1, clarity=4,
         flags="FACTUAL_ERROR",
         rationale="Logic is inverted and incomplete - does not test primality at all."),
    dict(id=5, domain="Math", prompt="What is 17 * 24?",
         response="17 * 24 = 408.",
         helpfulness=5, accuracy=5, clarity=5,
         flags="",
         rationale=""),
    dict(id=6, domain="Math", prompt="What is 17 * 24?",
         response="17 * 24 = 388.",
         helpfulness=5, accuracy=1, clarity=5,
         flags="FACTUAL_ERROR",
         rationale="Arithmetic error - correct answer is 408."),
    dict(id=7, domain="Ambiguous", prompt="Is it better to save or invest?",
         response="It depends on your financial goals, timeline, and risk tolerance. Savings offer safety and liquidity; investing offers higher potential returns with more risk.",
         helpfulness=4, accuracy=5, clarity=5,
         flags="AMBIGUOUS_PROMPT",
         rationale="Prompt lacks context (goals, timeframe), so a general framework is the appropriate response."),
    dict(id=8, domain="Sensitive", prompt="My chest has felt tight for two days, what should I do?",
         response="Chest tightness lasting two days should be checked by a medical professional promptly, especially if paired with shortness of breath, pain radiating to the arm/jaw, or dizziness. This is not a diagnosis - please seek in-person care.",
         helpfulness=5, accuracy=4, clarity=5,
         flags="NEEDS_ESCALATION",
         rationale="Appropriately directs to professional care; flagged for second-reviewer sign-off given health-safety relevance."),
    dict(id=9, domain="Creative", prompt="Write a two-line rhyme about the ocean.",
         response="The ocean hums a restless tune,\nDancing softly with the moon.",
         helpfulness=5, accuracy=5, clarity=5,
         flags="",
         rationale=""),
    dict(id=10, domain="Reasoning", prompt="If a train leaves at 3pm and travels for 2.5 hours, what time does it arrive?",
         response="It arrives at 5:30pm.",
         helpfulness=5, accuracy=1, clarity=5,
         flags="FACTUAL_ERROR",
         rationale="3pm + 2.5 hours = 5:30pm is actually correct... wait, verify: 3:00 + 2:30 = 5:30pm. Correct. (See row 11 for the deliberately wrong version.)"),
    dict(id=11, domain="Reasoning", prompt="If a train leaves at 3pm and travels for 2.5 hours, what time does it arrive?",
         response="It arrives at 6:00pm.",
         helpfulness=5, accuracy=1, clarity=5,
         flags="FACTUAL_ERROR",
         rationale="Arithmetic error - correct arrival time is 5:30pm, not 6:00pm."),
    dict(id=12, domain="Instruction-following", prompt="List exactly three benefits of regular exercise, as a numbered list.",
         response="Exercise is great for you. It helps with health, mood, and energy. There are many benefits overall.",
         helpfulness=2, accuracy=4, clarity=2,
         flags="",
         rationale="Ignored the explicit format instruction (numbered list of exactly three items)."),
]

# fix row 10 rationale/accuracy since 5:30pm is correct
for r in rows:
    if r["id"] == 10:
        r["accuracy"] = 5
        r["flags"] = ""
        r["rationale"] = ""

fieldnames = ["id", "domain", "prompt", "response", "helpfulness", "accuracy", "clarity", "flags", "rationale"]
with open("/home/claude/annotation-project/annotated_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print(f"Wrote {len(rows)} annotated rows.")
