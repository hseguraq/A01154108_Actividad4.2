# pylint: disable=invalid-name
"""Number conversion to BIN and HEX"""
import time


def is_valid_txt_file(filename):
    """Check if the file has a .txt extension."""
    return filename.lower().endswith(".txt")


def read_numbers_from_file(filename):
    """Read a single column of numbers from a .txt file."""
    numbers = []
    try:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line.isdigit() or (line.startswith("-") and line[1:].isdigit()): # noqa
                    numbers.append(int(line))
                else:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    return numbers


def convert_numbers(numbers):
    """Convert numbers to binary and hexadecimal formats."""
    results = []
    for index, num in enumerate(numbers, start=1):
        binary = bin(num)[2:] if num >= 0 else "1" + bin(num & 0xFFFFFFFF)[3:]
        hexadecimal = hex(num)[2:].upper() if num >= 0 else hex(num & 0xFFFFFFFF).upper() # noqa
        results.append((index, num, binary, hexadecimal))
    return results


def print_and_save_results(results, runtime):
    """Print and save the results to a file."""
    output_filename = "ConvertionResults.txt"

    with open(output_filename, "w", encoding='utf-8') as file:
        header = f"{'ITEM':<5} {'NUMBER':<10} {'BIN':<20} {'HEX':<10}\n"
        file.write(header)

        print(header, end="")

        for item, num, binary, hexadecimal in results:
            line = f"{item:<5} {num:<10} {binary:<20} {hexadecimal:<10}\n"
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

    numbers = read_numbers_from_file(filename)
    if numbers is None:
        return

    results = convert_numbers(numbers)
    runtime = time.time() - start_time

    print_and_save_results(results, runtime)
    print("\nResults saved to 'ConversionResults.txt'.")


if __name__ == "__main__":
    main()
