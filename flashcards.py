flashcards = {
    "What command shows your cd?": "pwd",
    "What is Git commit?": "A saved snapshot of changes in a repository.",
    "What is Git branch?": "A separate line of development in a repository."
}

print("Git Version Control Flashcards")
print("------------------------------")

for question, answer in flashcards.items():
    print("\n" + question)
    input("Press Enter to see the answer...")
    print("Answer:", answer)