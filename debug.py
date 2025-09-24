# debug_docx.py
import docx
import json
import os

# --- CONFIGURATION ---
# Please rename your file to this name exactly and place it in the same folder
DOCX_FILE_TO_ANALYZE = "tech02.docx"
JSON_OUTPUT_FILE = "debug_output_2.json"

def analyze_docx_structure(docx_path):
    """
    Reads a DOCX file and extracts detailed information about each paragraph,
    including its text, style, and the formatting of each text segment (run).
    This helps diagnose issues with automatic numbering and bolding.
    """
    if not os.path.exists(docx_path):
        print("--- ERROR ---")
        print(f"The file '{docx_path}' was not found.")
        print("Please rename your 'technical test piston engine answers.docx' file to 'piston_engine_quiz.docx' and place it in the same folder as this script.")
        return

    print(f"Analyzing '{docx_path}'...")
    try:
        doc = docx.Document(docx_path)
        
        # This list will store the data we extract from each paragraph
        structure_data = []

        for i, para in enumerate(doc.paragraphs):
            # We will extract as much info as possible to understand the structure
            para_info = {
                "paragraph_index": i,
                "text": para.text.strip(),
                "style_name": para.style.name,
                "runs_details": [] # 'Runs' are segments of text with the same formatting
            }
            
            # Get detailed info about each run within the paragraph
            for run in para.runs:
                para_info["runs_details"].append({
                    "text": run.text,
                    "is_bold": run.bold or False, # Ensure it's always a boolean
                    "is_italic": run.italic or False,
                })
            
            structure_data.append(para_info)
            
        # Save the extracted structure to a JSON file for easy viewing
        with open(JSON_OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(structure_data, f, indent=2, ensure_ascii=False)
            
        print(f"\n--- SUCCESS ---")
        print(f"Analysis complete. A new file named '{JSON_OUTPUT_FILE}' has been created.")
        print("Please open that file, copy its ENTIRE contents, and paste them back in our chat.")
        print("This will give me the exact blueprint needed to build the correct parser.")

    except Exception as e:
        print(f"\n--- ERROR ---")
        print(f"An unexpected error occurred: {e}")
        print("The file might be corrupted or in an unsupported format.")


if __name__ == "__main__":
    analyze_docx_structure(DOCX_FILE_TO_ANALYZE)