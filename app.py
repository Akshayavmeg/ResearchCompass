from tools.llm import ask_llm

print("=" * 60)
print("🧭 Welcome to ResearchCompass")
print("=" * 60)

while True:
    query = input("\nYou: ")

    if query.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    response = ask_llm(query)

    print(f"\nResearchCompass: {response}")