# Textbook Quiz Verifier

## The "Anti-Cheat" Philosophy

You're probably curious what this is, and it's quite straightforward. This tool uses basic cryptographic principles (specifically **Polynomial Rolling Hashes**) to create a system where students can self-mark their quizzes.

The goal is to provide immediate feedback without a "back-of-the-book" answer key. This prevents students from accidentally (or intentionally) cheating themselves out of a good "think-and-learn" session.

## How it Works

1. **One-Way Verification:** The script converts a series of answers into a unique numerical "fingerprint" using modulo arithmetic.
2. **Hard to Reverse:** Even if a student looks at the source code, they can't easily work backward from the "Target Number" to find the correct answers.
3. **User-Friendly:** Includes a built-in "Undo" feature (`u`) so students can fix typos without restarting the whole quiz.

## For Cheaters

Obviously you can still cheat, since you can see exactly how the answer key is generated in `KeyGen.py`, but not without first learning a little about cryptography—that's the deal.

To help you get started, learn more about hashing, brute-force via rainbow tables, or try to reverse the modulo arithmetic. If you crack it, you've learned something cool about a topic that has a special place in my heart, and in so doing have earned my forgiveness for this transgression. Happy hacking!