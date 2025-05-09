try:
    import docx  # Try importing docx
    print("python-docx is installed.")
except ImportError:
    print("python-docx is NOT installed.")

try:
    import PyPDF2  # Try importing PyPDF2
    print("PyPDF2 is installed.")
except ImportError:
    print("PyPDF2 is NOT installed.")
