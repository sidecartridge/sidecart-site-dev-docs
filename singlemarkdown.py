import os
import sys

def get_unique_output_filename(base_name):
    if not os.path.exists(base_name):
        return base_name
    base, ext = os.path.splitext(base_name)
    counter = 1
    while True:
        candidate = f"{base}_{counter}{ext}"
        if not os.path.exists(candidate):
            return candidate
        counter += 1

def is_merged_output_file(filename):
    if not filename.endswith('.md'):
        return False
    base = os.path.splitext(filename)[0]
    return base == "merged_docs" or base.startswith("merged_docs_")

def merge_markdown_files(root_folder):
    output_file = get_unique_output_filename("merged_docs.md")
    output_abs_path = os.path.abspath(output_file)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for dirpath, _, filenames in os.walk(root_folder):
            for filename in sorted(filenames):
                if filename.endswith('.md') and not is_merged_output_file(filename):
                    filepath = os.path.join(dirpath, filename)
                    if os.path.abspath(filepath) == output_abs_path:
                        continue  # Absolute path match — skip!
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        rel_path = os.path.relpath(filepath, root_folder)
                        outfile.write(f"\n\n# {rel_path}\n\n")
                        outfile.write(infile.read())
                        outfile.write('\n\n---\n\n')

    print(f"✅ Merged Markdown written to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_markdown.py <root_folder>")
        sys.exit(1)

    root_folder = sys.argv[1]
    if not os.path.isdir(root_folder):
        print(f"❌ Error: '{root_folder}' is not a valid directory.")
        sys.exit(1)

    merge_markdown_files(root_folder)

