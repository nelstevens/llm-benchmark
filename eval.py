import os
import re
import sys
# Set the directory containing your .txt files
input_dir = sys.argv[1]
output_file = input_dir + "/output.md"  # Optional: Write all markdown tables to this file

# Regular expression pattern to parse key-value pairs
pattern = re.compile(r'^(.*?):\s+(.*)$')

# Expected keys in order
headers = [
    "total duration", "load duration", "prompt eval count", "prompt eval duration",
    "prompt eval rate", "eval count", "eval duration", "eval rate"
]

# Store markdown output
markdown_output = []

# Loop through all txt files in the directory
for filename in sorted(os.listdir(input_dir)):
    if filename.endswith(".log"):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        # Extract model name from the first line
        model_name_line = lines.pop(0)
        model_name = model_name_line.split('=')[1].strip()

        rows = []
        row = []

        for line in lines:
            match = pattern.match(line)
            if match:
                key, value = match.groups()
                if key in headers:
                    row.append(value)
                    if len(row) == len(headers):
                        rows.append(row)
                        row = []

        # Add table for current file/model
        markdown_output.append(f"### Model: {model_name} (File: {filename})\n")
        markdown_output.append("| " + " | ".join(headers) + " |")
        markdown_output.append("|" + "|".join(["---"] * len(headers)) + "|")
        for row in rows:
            markdown_output.append("| " + " | ".join(row) + " |")
        markdown_output.append("\n")  # Add space between tables

# Output to console or write to file
# Print to console:
print("\n".join(markdown_output))

# Optional: write to file
with open(output_file, 'w') as out:
    out.write("\n".join(markdown_output))

print(f"\nMarkdown tables saved to: {output_file}")