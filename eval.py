import os
import re

def extract_model_name_and_rates(filepath):
    eval_rates = []
    model_name = None

    with open(filepath, 'r') as file:
        for line in file:
            if model_name is None and line.startswith("model_name"):
                match = re.search(r'model_name\s*=\s*(.+)', line)
                if match:
                    model_name = match.group(1).strip()

            if line.strip().startswith("eval rate:"):
                match = re.search(r'eval rate:\s+([\d.]+)\s+tokens/s', line)
                if match:
                    eval_rates.append(float(match.group(1)))

    return model_name or os.path.basename(filepath), eval_rates

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    directory = './aws-t2-xlarge'  # Change if needed
    output_file = './aws-t2-xlarge/averages.md'
    files = [f for f in os.listdir(directory) if f.endswith('.log')]
    results = []

    for filename in sorted(files):
        filepath = os.path.join(directory, filename)
        model_name, rates = extract_model_name_and_rates(filepath)
        avg = average(rates)
        results.append((model_name, len(rates), avg))

    # Build the Markdown table
    table_lines = [
        "| Model Name | # of Eval Rates | Average Eval Rate (tokens/s) |",
        "|------------|------------------|-------------------------------|"
    ]
    for model_name, count, avg in results:
        table_lines.append(f"| {model_name} | {count} | {avg:.2f} |")

    # Write to Markdown file
    with open(output_file, 'w') as f:
        f.write("\n".join(table_lines))

    print(f"Markdown table written to: {output_file}")

if __name__ == '__main__':
    main()
