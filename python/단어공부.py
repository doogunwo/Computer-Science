def most_common_letter_without_counter(s):
    s = s.upper()
    letter_counts = {}

    for letter in s:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
        print(letter_counts[letter])

    max_count = max(letter_counts.values())
    print(letter_counts.values())
    most_common = [letter for letter, count in letter_counts.items() if count == max_count]

    if len(most_common) > 1:
        return '?'
    else:
        return most_common[0]

# 예제 입력
s = input()
print(most_common_letter_without_counter(s))
