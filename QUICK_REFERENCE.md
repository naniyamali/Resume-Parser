# Resume Parser - Quick Reference

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Basic Usage

```python
from ResumeParser import ResumeParser

# Parse resume (DOCX or PDF)
parser = ResumeParser('resume.pdf')
result = parser.parse_information()
```

## File Formats Supported

| Format | Extension | Supported |
|--------|-----------|-----------|
| Word Document | .docx | ✅ Yes |
| PDF | .pdf | ✅ Yes (requires PyPDF2) |
| Plain Text | .txt | ❌ No |
| Google Docs | (export as PDF/DOCX) | ✅ Yes |

## API Quick Reference

```python
# Get all information
result = parser.parse_information()

# Get specific sections
candidate_info = parser.get_candidate_info('CandidateInformation')
summary = parser.get_summary_text('SummaryText')
work_exp = parser.get_work_experience('WorkExperience')
```

## Output Structure

```
{
  'CandidateInformation': {
    'FullName': str,
    'Email': str,
    'Phone': str,
    'Address': str,
    'LinkedInURL': str,
    'GithubURL': str
  },
  'SummaryText': str,
  'WorkExperience': [str, ...]
}
```

## Customization

### Change Section Keywords
Edit `section_title.csv` to add/modify keywords

### Modify Phone Pattern
Edit `PHONE_PATTERN_1` and `PHONE_PATTERN_2` in `MatchEvent` class

### Add Custom Patterns
Add to `CANDIDATE_INFO` list in `ResumeParser` class

## Common Issues

| Issue | Solution |
|-------|----------|
| No text extracted | Check section keywords in CSV match resume format |
| PDF error | Install: `pip install PyPDF2` |
| spaCy model error | Run: `python -m spacy download en_core_web_sm` |
| FileNotFoundError | Verify file path exists and run from project root |

## Environment Setup

### Windows
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python ResumeParser.py
```

### Mac/Linux
```bash
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm
python3 ResumeParser.py
```

## Sample Directory Structure

```
Resume-Parser/
├── ResumeParser.py
├── test.py
├── section_title.csv
├── requirements.txt
├── README.md
├── SETUP_GUIDE.md
├── CODEBASE.md
└── resumes/
    ├── resume1.docx
    ├── resume2.pdf
    └── resume3.docx
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| spacy | >=3.0.0 | NLP processing |
| python-docx | >=0.8.10 | DOCX support |
| pandas | >=1.0.0 | CSV handling |
| docx2txt | >=0.8 | DOCX conversion |
| PyPDF2 | >=3.0.0 | PDF extraction |

## Performance Tips

1. **Batch Processing**: Load NLP model once, reuse for multiple files
2. **Large Files**: May take longer; consider splitting if >50 pages
3. **PDF Files**: Slower than DOCX due to text extraction complexity
4. **First Run**: Initial spaCy model load takes ~5-10 seconds

## Supported Extractable Information

| Category | Fields |
|----------|--------|
| **Contact** | Name, Email, Phone, Address |
| **URLs** | LinkedIn, GitHub |
| **Professional** | Summary, Work Experience |
| **Education** | Degrees, Schools |
| **Technical** | Skills, Languages, Tools |

## Export Results

```python
import json

result = parser.parse_information()

# Save as JSON
with open('output.json', 'w') as f:
    json.dump(result, f, indent=2)

# Save as CSV
import pandas as pd
df = pd.DataFrame([result])
df.to_csv('output.csv', index=False)
```

## Troubleshooting Checklist

- [ ] Python 3.7+ installed?
- [ ] Dependencies installed? (`pip install -r requirements.txt`)
- [ ] spaCy model downloaded? (`python -m spacy download en_core_web_sm`)
- [ ] Resume file exists and readable?
- [ ] Running from project root directory?
- [ ] section_title.csv in same directory as ResumeParser.py?
- [ ] Using supported file format (.docx or .pdf)?

## Documentation Files

- **README.md** - Project overview and quick start
- **CODEBASE.md** - Technical architecture details
- **SETUP_GUIDE.md** - Detailed setup and customization
- **QUICK_REFERENCE.md** - This file

---

For detailed documentation, see **SETUP_GUIDE.md** and **CODEBASE.md**
