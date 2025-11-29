#!/usr/bin/env python3
"""
Jupyter Notebook'u HTML formatına çeviren script
"""

import subprocess
import sys

def convert_notebook_to_html(notebook_path):
    """Notebook'u HTML'e çevirir"""
    try:
        print(f"Converting {notebook_path} to HTML...")
        
        # nbconvert komutunu çalıştır
        result = subprocess.run([
            'jupyter', 'nbconvert', 
            '--to', 'html',
            notebook_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Conversion successful!")
            print(f"HTML file created: {notebook_path.replace('.ipynb', '.html')}")
        else:
            print("✗ Conversion failed!")
            print("Error:", result.stderr)
            
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    notebook_file = "veri_madenciligi_projesi.ipynb"
    convert_notebook_to_html(notebook_file)
