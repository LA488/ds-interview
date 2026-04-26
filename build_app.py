# -*- coding: utf-8 -*-
import json
import os
import sys

# Force UTF-8 for stdout and everything else
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, "questions.json")
TEMPLATE_FILE = os.path.join(BASE_DIR, "template.html")
OUTPUT_FILE = os.path.join(BASE_DIR, "ds-interview-standalone.html")

def main():
    print(f"Loading questions from {QUESTIONS_FILE}")
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    SQL_TASKS_FILE = os.path.join(BASE_DIR, "sql_tasks.json")
    print(f"Loading SQL tasks from {SQL_TASKS_FILE}")
    with open(SQL_TASKS_FILE, "r", encoding="utf-8") as f:
        sql_tasks = json.load(f)
        
    print(f"Loading template from {TEMPLATE_FILE}")
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()
        
    print(f"Injecting {len(questions)} questions and {len(sql_tasks)} SQL tasks into HTML...")
    json_data = json.dumps(questions, ensure_ascii=False, indent=4)
    sql_json_data = json.dumps(sql_tasks, ensure_ascii=False, indent=4)
    
    final_html = template.replace("{{QUESTIONS_JSON}}", json_data)
    final_html = final_html.replace("{{SQL_TASKS_JSON}}", sql_json_data)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Success! Build complete: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
