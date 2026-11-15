"""String exercises."""


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]


def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""


def are_anagrams(first, second):
    # Ignore spaces and letter case.
    a = sorted(ch.lower() for ch in first if not ch.isspace())
    b = sorted(ch.lower() for ch in second if not ch.isspace())
    return a == b


def remove_duplicate_characters(text):
    seen = set()
    result = []
    for ch in text:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)


def compress_string(text):
    """Run-length encoding: 'aaabbc' -> 'a3b2c1'. Empty input -> ''."""
    if not text:
        return ""
    parts = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            parts.append(f"{text[i - 1]}{count}")
            count = 1
    parts.append(f"{text[-1]}{count}")
    return "".join(parts)


if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Palindrome:", is_palindrome(s))
    print("Longest word:", longest_word(input("Enter a sentence: ")))
    first = input("First string for anagram check: ")
    second = input("Second string: ")
    print("Anagrams:", are_anagrams(first, second))
    text = input("String to remove duplicate characters from: ")
    print("Without duplicate characters:", remove_duplicate_characters(text))
    print("Compressed string:", compress_string(input("String to compress: ")))
