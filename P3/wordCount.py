# pylint: disable=invalid-name
"""Distinct word counter"""
import time


def is_valid_txt_file(filename):
    """Check if the file has a .txt extension."""
    return filename.lower().endswith(".txt")


def read_words_from_file(filename):
    """Read words from a .txt file and count occurrences."""
    words = []
    try:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if word.isalpha():
                    words.append(word.lower())
                else:
                    print(f"Warning: Skipping invalid entry '{word}'")

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    return words


def count_word_occurrences(words):
    """Count occurrences of each distinct word."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def print_and_save_results(word_counts, runtime):
    """Print and save the word count results to a file."""
    output_filename = "WordCountResults.txt"

    with open(output_filename, "w", encoding='utf-8') as file:
        header = f"{'WORD':<20} {'COUNT':<10}\n"
        file.write(header)

        print(header, end="")

        for word, count in sorted(word_counts.items()):
            line = f"{word:<20} {count:<10}\n"
            file.write(line)
            print(line, end="")

        runtime_line = f"\nRuntime: {runtime:.5f} seconds\n"
        file.write(runtime_line)
        print(runtime_line, end="")


def main():
    """File intake and processing"""
    filename = input("Enter the name of a .txt file: ").strip()

    if not is_valid_txt_file(filename):
        print("Error: Only .txt files are allowed.")
        return

    start_time = time.time()

    words = read_words_from_file(filename)
    if words is None:
        return

    word_counts = count_word_occurrences(words)
    runtime = time.time() - start_time

    print_and_save_results(word_counts, runtime)
    print("\nResults saved to 'WordCountResults.txt'.")


if __name__ == "__main__":
    main()
