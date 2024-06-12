import os
import subprocess
import glob

# file formats
file_format = 'pdf'

# Directories
input_directory = "chapters/"
output_directory = f"generated/{file_format}"

# Output HTML file
output_file = f"programming-for-all-python.{file_format}"

# Get a list of Markdown files in the input directory
md_files = glob.glob(os.path.join(input_directory, "*.md"))

# List to store generated HTML files
html_files = []

# Command to convert each Markdown file to HTML using Pandoc
for md_file in md_files:
    # Output file name for each Markdown file (replace .md with .html)
    html_file = os.path.join(output_directory, os.path.basename(os.path.splitext(md_file)[0] + f".{file_format}"))
    html_files.append(html_file)  # Add to list of HTML files
    # Command to convert the current Markdown file to HTML using Pandoc
    command = f"pandoc {md_file} -o {html_file}"
    # Execute the command using subprocess
    subprocess.run(command, shell=True)

# # Combine all HTML files into one
# # Open the output file in append mode
# with open(output_file, "a") as outfile:
#     # Loop through each HTML file
#     for html_file in html_files:
#         # Open the current HTML file and read its contents
#         with open(html_file, "r") as infile:
#             # Write the contents of the current HTML file to the output file
#             outfile.write(infile.read())
#             # Add a newline character to separate the contents of each file
#             outfile.write("\n")
