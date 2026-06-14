# ============================================================
#   DecodeLabs | Batch 2026 | Project 1
#   Rule-Based AI Chatbot — The Logic Skeleton
# ============================================================

# ── KNOWLEDGE BASE (Dictionary / Hash Map) ──────────────────
# Using a dict instead of if-elif ladder → O(1) lookup time
responses = {
    # Greetings
    "hello":        "Hey there! 👋 I'm DecoBot. How can I help you today?",
    "hi":           "Hi! Great to see you. What's on your mind?",
    "hey":          "Hey! What can I do for you?",

    # Farewells
    "bye":          "Goodbye! Keep building! 🚀",
    "goodbye":      "See you later! Good luck with your projects. 👋",

    # Identity
    "who are you":  "I'm DecoBot 🤖 — a rule-based AI chatbot built at DecodeLabs.",
    "what are you": "I'm a rule-based chatbot. I match your input to predefined rules and reply instantly!",
    "your name":    "My name is DecoBot. Nice to meet you!",

    # Capabilities
    "what can you do": "I can answer questions, greet you, tell you about AI, and chat — all using pure logic!",
    "help":            "Sure! Try asking: 'hello', 'what is ai', 'tell me a fact', or 'what can you do'.",

    # AI topics
    "what is ai":       "AI (Artificial Intelligence) is the simulation of human intelligence by machines. 🧠",
    "what is ml":       "Machine Learning is a subset of AI where systems learn from data instead of explicit rules.",
    "what is deep learning": "Deep Learning uses neural networks with many layers to learn complex patterns from data.",
    "what is nlp":      "NLP (Natural Language Processing) helps computers understand and generate human language.",

    # DecodeLabs
    "what is decodelabs": "DecodeLabs is an AI training platform that gives interns real-world project experience! 💡",
    "about decodelabs":   "DecodeLabs helps you build an AI portfolio through hands-on projects. This is Project 1!",

    # Fun / misc
    "tell me a fact": "Fun fact: The term 'Artificial Intelligence' was coined by John McCarthy in 1956! 🎓",
    "joke":           "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
    "how are you":    "I'm running at 100% efficiency! All systems operational. 🟢",
    "thanks":         "You're welcome! Happy to help. 😊",
    "thank you":      "Anytime! That's what I'm here for. 🤝",
}

# ── PHASE 1: INPUT SANITIZATION ──────────────────────────────
def sanitize(raw: str) -> str:
    """Lowercase + strip whitespace → normalized input."""
    return raw.lower().strip()

# ── PHASE 2: INTENT MATCHING ─────────────────────────────────
def get_response(clean_input: str) -> str:
    """O(1) dictionary lookup with fallback for unknowns."""
    return responses.get(clean_input, "🤔 I don't understand that yet. Try typing 'help' to see what I can do!")

# ── PHASE 3: OUTPUT / MAIN LOOP ──────────────────────────────
def main():
    print("=" * 55)
    print("  DecoBot 🤖 | DecodeLabs Rule-Based Chatbot")
    print("  Type 'exit' or 'quit' to end the session.")
    print("=" * 55)

    # THE HEARTBEAT — infinite loop until kill command
    while True:
        raw_input_text = input("\nYou: ")          # raw feed
        clean_input    = sanitize(raw_input_text)  # sanitize

        # EXIT STRATEGY — clean break command
        if clean_input in ("exit", "quit"):
            print("\nDecoBot: Shutting down. Great work today! 🚀")
            print("=" * 55)
            break

        # Skip empty input
        if not clean_input:
            print("DecoBot: Please type something!")
            continue

        # Lookup + fallback in one atomic operation
        reply = get_response(clean_input)
        print(f"DecoBot: {reply}")

# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
