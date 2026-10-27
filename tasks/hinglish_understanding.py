# %%
"""
Hinglish & Regional Language Understanding Benchmark Task
=======================================================
Tests how well LLMs understand Hinglish (Hindi-English mix)
and common Indian code-switching patterns.
"""

import kaggle_benchmarks as kbench
from typing import Dict, Any

# %%
@kbench.task(
    name="hinglish_understanding",
    description="Evaluates LLM understanding of Hinglish and Indian code-switching across comprehension, intent, sentiment, reasoning and instruction following."
)
def hinglish_understanding(llm) -> Dict[str, float]:
    """
    Main evaluation task.
    Returns a dictionary of category-wise scores (0.0 to 1.0)
    so the leaderboard can show detailed breakdown.
    """

    results = {}

    # -------------------------------------------------
    # 1. Simple Understanding
    # -------------------------------------------------
    prompt1 = """Yeh sentence samjhao simple language mein:

\"Bhai kal office nahi aa paya kyunki subah se pet kharab tha, doctor ne rest karne ko bola.\"

Sirf meaning batao, extra bakwas mat karna."""

    response1 = llm.prompt(prompt1)

    # Expected key ideas: couldn't come to office, stomach problem, doctor advised rest
    score1 = 0.0
    lower = response1.lower()
    if any(w in lower for w in ["office", "kaam", "work"]):
        score1 += 0.3
    if any(w in lower for w in ["pet", "stomach", "stomach ache", "upset stomach", "diarrhea", "loose motion"]):
        score1 += 0.4
    if any(w in lower for w in ["doctor", "rest", "aaram"]):
        score1 += 0.3
    results["simple_understanding"] = min(score1, 1.0)

    kbench.assertions.assert_that(
        score1 >= 0.6,
        expectation="Model should correctly understand basic Hinglish sentence about missing office due to stomach issue."
    )

    # -------------------------------------------------
    # 2. Intent Detection
    # -------------------------------------------------
    prompt2 = """User ne yeh message bheja hai:

\"Yaar thoda help kar de na, kal tak assignment submit karna hai lekin abhi tak half bhi nahi hua. Koi idea hai kaise jaldi complete karun?\"

User ka main intent kya hai? Short mein batao."""

    response2 = llm.prompt(prompt2)
    lower2 = response2.lower()

    score2 = 0.0
    if any(w in lower2 for w in ["help", "madad", "assistance"]):
        score2 += 0.4
    if any(w in lower2 for w in ["assignment", "submit", "deadline", "complete"]):
        score2 += 0.4
    if any(w in lower2 for w in ["idea", "suggestion", "kaise", "how"]):
        score2 += 0.2
    results["intent_detection"] = min(score2, 1.0)

    kbench.assertions.assert_that(
        score2 >= 0.6,
        expectation="Model should detect that user is asking for help to complete assignment quickly."
    )

    # -------------------------------------------------
    # 3. Sentiment Analysis
    # -------------------------------------------------
    prompt3 = """Is Hinglish message ka sentiment batao (Positive / Negative / Neutral / Mixed):

\"Aaj to full maza aa gaya yaar! Movie ekdum mast thi, lekin last mein ending thodi bekaar ho gayi. Overall worth it tha.\"

Sirf ek word mein answer do + short reason."""

    response3 = llm.prompt(prompt3)
    lower3 = response3.lower()

    # Correct is Mixed (positive overall but ending negative)
    score3 = 0.0
    if "mixed" in lower3 or "mix" in lower3:
        score3 = 1.0
    elif "positive" in lower3 and "negative" in lower3:
        score3 = 0.8
    elif "positive" in lower3:
        score3 = 0.4
    results["sentiment"] = score3

    kbench.assertions.assert_that(
        score3 >= 0.6,
        expectation="Model should identify Mixed sentiment (enjoyed movie but ending was bad)."
    )

    # -------------------------------------------------
    # 4. Code-switch Reasoning
    # -------------------------------------------------
    prompt4 = """Hinglish mein soch ke jawab do:

Ravi ke paas 3 apples hain. Usne 2 apne dost ko de diye. Phir uski mummy ne usko 5 aur apples diye.
Ab Ravi ke paas total kitne apples hain?

Step by step batao."""

    response4 = llm.prompt(prompt4)
    lower4 = response4.lower()

    score4 = 0.0
    # Final answer should be 6
    if "6" in response4 or "six" in lower4 or "छह" in response4:
        score4 += 0.6
    if any(w in lower4 for w in ["3", "teen", "three"]):
        score4 += 0.1
    if any(w in lower4 for w in ["2", "do", "two"]):
        score4 += 0.1
    if any(w in lower4 for w in ["5", "paanch", "five"]):
        score4 += 0.2
    results["reasoning"] = min(score4, 1.0)

    kbench.assertions.assert_that(
        score4 >= 0.6,
        expectation="Model should correctly calculate 3 - 2 + 5 = 6 in Hinglish context."
    )

    # -------------------------------------------------
    # 5. Instruction Following
    # -------------------------------------------------
    prompt5 = """Mere instructions carefully follow karo:

1. Pehle \"Namaste\" likho
2. Phir ek line mein batao ki tum kaun se model ho (agar pata ho)
3. Last mein \"Dhanyavaad\" likho

Kuch extra mat likhna."""

    response5 = llm.prompt(prompt5)
    lower5 = response5.lower()

    score5 = 0.0
    if "namaste" in lower5:
        score5 += 0.4
    if "dhanyavaad" in lower5 or "dhanyavad" in lower5 or "thanks" in lower5:
        score5 += 0.4
    # Check if it tried to say model name (bonus)
    if any(w in lower5 for w in ["gemini", "claude", "gpt", "qwen", "deepseek", "llama", "model"]):
        score5 += 0.2
    results["instruction_following"] = min(score5, 1.0)

    kbench.assertions.assert_that(
        score5 >= 0.6,
        expectation="Model should follow the exact 3-step Hinglish instruction (Namaste + model + Dhanyavaad)."
    )

    # -------------------------------------------------
    # Final Aggregate Score
    # -------------------------------------------------
    overall = sum(results.values()) / len(results)
    results["overall"] = round(overall, 3)

    return results


# %%
# Local test run (when running this file directly)
if __name__ == "__main__":
    print("Running Hinglish Understanding task locally...")
    result = hinglish_understanding.run(llm=kbench.llm)
    print("\nResults:")
    print(result)
