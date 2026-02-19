# --- CHAPTER DATA ---
# Teacher: Generate these using the generator at the bottom
CHAPTER_DATA = {
    "1": {"name": "Chapter 1", "target": 609468792, "count": 10},
    "2": {"name": "Chapter 2", "target": 912004556, "count": 10}
}

def run_quiz():
    print("=== Textbook Self-Marking Tool ===")
    ch = input("Enter Chapter Number: ")
    
    if ch not in CHAPTER_DATA:
        print("Chapter not found!")
        return

    chapter = CHAPTER_DATA[ch]
    answers = []
    
    while len(answers) < chapter["count"]:
        # 1. "Clear" the console (prints 50 newlines to push old text up)
        print("\n" * 50)
        print(f"=== {chapter['name']} ===")
        print("Q : A")
        
        # 2. Display current progress
        for i, val in enumerate(answers):
            print(f"{i + 1} : {val}")
        
        print("-" * 20)
        print("Note: To undo the last answer, enter 'u'")
        
        # 3. Get input
        user_input = input(f"Your answer to question {len(answers) + 1}: ").strip().lower()
        
        # 4. Handle Undo logic
        if user_input == 'u':
            if len(answers) > 0:
                answers.pop()
            continue
            
        # 5. Handle Numeric Input
        if user_input.isdigit():
            answers.append(int(user_input))
        else:
            print("Please enter a number or 'u' to undo.")
            input("Press Enter to continue...")

    # --- FINAL VERIFICATION ---
    prime = 10**9 + 7
    base = 31
    current_hash = 0
    for a in answers:
        current_hash = (current_hash * base + a) % prime
        
    if current_hash == chapter["target"]:
        print("\n✅ SUCCESS: All answers are correct!")
    else:
        print("\nAt least one answer is wrong :(\nHave a think, cover more material, and revisit this quiz again later. Give yourself at least one day.")

if __name__ == "__main__":
    run_quiz()