#!/bin/bash

# Script Name: coalesce_code.sh
# Description: This script recursively finds all files within a given directory,
#              and copies their contents to an output file in a formatted manner.
#              It ignores any files/folders containing "pycache" in their name.
#              Additionally, if a .gitignore file is present in the script's directory,
#              it applies those rules to filter out ignored files.
#
# Usage: ./coalesce_code.sh <directory> <output_file>
# Example: ./coalesce_code.sh /Users/bob/test /Users/bob/test/output.txt

# Ensure exactly two arguments are provided (directory path and output file)
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <output_file>"
    exit 1
fi

# Assign command-line arguments to variables
DIRECTORY=$1      # Target directory to search for files
OUTPUT_FILE=$2    # Destination file to store collected text

# Clear the output file if it already exists to prevent appending to old content
> "$OUTPUT_FILE"

# Check if a .gitignore file exists in the same directory as the script
GITIGNORE_FILE="$(dirname "$0")/.gitignore"

declare -a GITIGNORE_PATTERNS

if [ -f "$GITIGNORE_FILE" ]; then
    # Read and store .gitignore patterns, ignoring comments and empty lines
    while IFS= read -r line; do
        [[ -z "$line" || "$line" =~ ^#.*$ ]] && continue  # Skip empty lines and comments
        GITIGNORE_PATTERNS+=("$line")
    done < "$GITIGNORE_FILE"
fi

# Function to check if a file should be ignored based on .gitignore patterns
should_ignore() {
    local file_path="$1"

    # Ignore "pycache" files and directories
    #[[ "$file_path" == *pycache* ]] && return 0  

    # Ignore files/folders matching patterns in .gitignore
    for pattern in "${GITIGNORE_PATTERNS[@]}"; do
        if [[ "$file_path" == *"$pattern"* ]]; then
            return 0  # Indicate that the file should be ignored
        fi
    done

    return 1  # Indicate that the file should not be ignored
}

# Function to recursively process files and directories
process_files() {
    local dir="$1"  # Assign the directory path to a local variable

    # Loop through all files and subdirectories inside the given directory
    for file in "$dir"/*; do
        # Skip ignored files and directories
        should_ignore "$file" && continue

        if [ -d "$file" ]; then
            # If it's a directory, recursively process its contents
            process_files "$file"
        elif [ -f "$file" ]; then
            # If it's a file, append its path and content to the output file
            echo "=======================================" >> "$OUTPUT_FILE"
            echo "$file" >> "$OUTPUT_FILE"   # Print the full file path
            echo "---" >> "$OUTPUT_FILE"    # Separator for better readability
            cat "$file" >> "$OUTPUT_FILE"   # Append file contents
            echo -e "\n" >> "$OUTPUT_FILE"  # Add an extra newline for spacing
        fi
    done
}

# Start processing files from the given directory
process_files "$DIRECTORY"

# Display a completion message
echo "✅ Text from all files (excluding 'pycache' and .gitignore patterns) has been successfully copied to '$OUTPUT_FILE'."
