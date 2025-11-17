from ResumeParser import ResumeParser
import sys

pdf_path = r"C:\Users\Y NANI\Downloads\images\naniyamali__resume.pdf"
print('Running test with interpreter:', sys.executable)
try:
    rp = ResumeParser(pdf_path)
    print('TXT length:', len(rp.txt))
    print('Sections:', list(rp.section_data.keys()))
except Exception as e:
    import traceback
    traceback.print_exc()
    print('Error:', e)
