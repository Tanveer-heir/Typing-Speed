import time

def typing_test():
    test_text = "The quick brown fox jumps over the lazy dog."
    print("=== Typing Speed Test ===")
    print("Type the following text exactly as shown, then press Enter:\n")
    print(test_text)
    input("\nPress Enter to start...")

    start_time = time.time()
    typed_text = input()
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(typed_text.split())
    wpm = words / (time_taken / 60)
    
    errors = sum(1 for a, b in zip(test_text, typed_text) if a != b)
    errors += abs(len(test_text) - len(typed_text))

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Your typing speed: {wpm:.2f} words per minute")
    print(f"Total errors: {errors}")

if __name__ == "__main__":
    typing_test()
