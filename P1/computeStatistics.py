# pylint: disable=invalid-name
"""Basic stats calculator"""
import os
import time

output_file = 'StatisticsResults.txt'


def compute_statistics(data):
    """Direct calculations for metrics"""
    count = len(data)
    mean = sum(data) / count if count > 0 else 'N/A'

    # Median calculation
    sorted_data = sorted(data)
    if count > 0:
        mid = count // 2
        median = (
            sorted_data[mid] if count % 2 != 0
            else (sorted_data[mid - 1] + sorted_data[mid]) / 2
        )
    else:
        median = 'N/A'

    # Mode calculation
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    mode = max(frequency, key=frequency.get) if frequency else 'N/A'

    # Variance and Standard Deviation
    if count > 1:
        variance = sum((x - mean) ** 2 for x in data) / (count - 1)
        std_dev = variance ** 0.5
    else:
        variance, std_dev = 'N/A', 'N/A'

    return {"COUNT": count, "MEAN": mean, "MEDIAN": median,
            "MODE": mode, "VARIANCE": variance, "SD": std_dev}


def process_file(input_file_path):
    """File intake and processing"""
    start_time = time.time()
    warnings_messages = []

    try:
        with open(input_file_path, "r", encoding='utf-8') as f:
            data = []
            for line in f:
                line = line.strip()
                try:
                    data.append(float(line))
                except ValueError:
                    warning_msg = (
                     f"Warning: Skipping invalid data '{line}' in {input_file_path}" # noqa
                    )
                    print(warning_msg)
                    warnings_messages.append(warning_msg)

        if not data:
            return {"Error": "No valid numeric data found."}, 0, warnings_messages # noqa

        results = compute_statistics(data)
        process_runtime = time.time() - start_time
        return results, process_runtime, warnings_messages
    except (OSError, ValueError) as error:
        return {"Error": str(error)}, 0, warnings_messages


file_name = input("Enter the name of the TXT file (including .txt): ").strip()
file_path = os.path.join(os.getcwd(), file_name)

if not file_name.endswith(".txt") or not os.path.isfile(file_path):
    print(
     "Error: Only .txt files are allowed."
    )
else:
    result, runtime, warnings = process_file(file_path)

    with open(output_file, "w", encoding='utf-8') as out:
        for metric, value in result.items():
            print(f"{metric}: {value}")
            out.write(f"{metric}: {value}\n")

        print(f"Processed {file_name} in {runtime:.4f} seconds")
        out.write(f"Processed {file_name} in {runtime:.4f} seconds\n")

    print(f"Results saved in {output_file}")
