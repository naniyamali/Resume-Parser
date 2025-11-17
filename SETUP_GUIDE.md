# Setup & Usage Guide

## Quick Start

### 1. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Download spaCy English model
python -m spacy download en_core_web_sm
```

### 2. Prepare Your Resumes

Create a `resumes/` directory in the project folder and add your resume files:
```
Resume-Parser/
├── resumes/
│   ├── john_doe.docx
│   ├── jane_smith.pdf
│   └── ...
├── ResumeParser.py
├── section_title.csv
└── requirements.txt
```

**Supported Formats:**
- `.docx` (Microsoft Word documents)
- `.pdf` (Portable Document Format)

### 3. Run the Parser

#### Using the CLI directly:

```python
from ResumeParser import ResumeParser

# Parse a DOCX file
parser = ResumeParser('./resumes/resume.docx')
result = parser.parse_information()
print(result)

# Parse a PDF file
parser = ResumeParser('./resumes/resume.pdf')
result = parser.parse_information()
print(result)
```

#### Using the demo script:

```bash
python ResumeParser.py
```

This will parse all sample resumes and display results.

#### Using the test module:

```bash
python test.py
```

### 4. Expected Output

The parser returns a dictionary with extracted information:

```python
{
    'CandidateInformation': {
        'FullName': 'John Doe',
        'Email': 'john@example.com',
        'Phone': '123-456-7890',
        'Address': '123 Main St New York NY',
        'LinkedInURL': 'https://linkedin.com/in/johndoe',
        'GithubURL': 'https://github.com/johndoe'
    },
    'SummaryText': 'Professional summary or objective...',
    'WorkExperience': [
        'Job description 1...',
        'Job description 2...'
    ]
}
```

## API Reference

### ResumeParser Class

```python
from ResumeParser import ResumeParser

parser = ResumeParser(file_path)
```

**Parameters:**
- `file_path` (str): Path to DOCX or PDF resume file

**Methods:**

| Method | Returns | Description |
|--------|---------|-------------|
| `parse_information()` | dict | Extract all resume sections and info |
| `get_candidate_info(title)` | dict | Extract contact info (name, email, phone, address, URLs) |
| `get_summary_text(title)` | dict | Extract summary/objective section |
| `get_work_experience(title)` | dict | Extract work experience entries |
| `convert_docx2txt(file_name)` | str | Convert file to text (supports DOCX and PDF) |
| `load_data(doc)` | dict | Parse document sections |

### Example: Extract Specific Sections

```python
from ResumeParser import ResumeParser

parser = ResumeParser('./resumes/resume.pdf')

# Get contact information only
candidate_info = parser.get_candidate_info('CandidateInformation')
print(candidate_info)

# Get work experience
work_exp = parser.get_work_experience('WorkExperience')
print(work_exp)

# Get summary/objective
summary = parser.get_summary_text('SummaryText')
print(summary)
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'spacy'"

**Solution:**
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Issue: "No module named 'docx2txt'"

**Solution:**
```bash
pip install docx2txt
```

### Issue: "PDF support requires PyPDF2"

**Solution:**
```bash
pip install PyPDF2
```

### Issue: "FileNotFoundError: section_title.csv not found"

**Solution:**
- Ensure `section_title.csv` is in the same directory as `ResumeParser.py`
- Run the script from the project root directory

### Issue: No data extracted from resume

**Possible causes:**
1. Resume doesn't have clear section headers (check `section_title.csv` for keywords)
2. File format is corrupted
3. spaCy model not properly loaded

**Solutions:**
- Verify resume structure matches expected format
- Try with a different resume file
- Reinstall spaCy model: `python -m spacy download en_core_web_sm`

### Issue: Limited text extraction from PDF

**Note:** PDF extraction depends on PDF structure and encoding. Some PDFs may:
- Have limited text (scanned images)
- Use special encoding
- Require additional tools

**Solutions:**
- Try OCR tools if PDF is scanned (e.g., Tesseract)
- Convert PDF to DOCX first using online tools
- Check PDF accessibility settings

## Performance Notes

- **First Run:** Takes longer as spaCy model is loaded
- **Large Files:** Processing time increases with resume size
- **PDFs:** May be slower than DOCX due to text extraction complexity
- **Batch Processing:** For multiple resumes, initialize parser once per file

## Customization

### Add Custom Section Keywords

Edit `section_title.csv` to add more keywords for better section detection:

```csv
SummaryText,Education,ToolsAndTechnologies,...
My Objective,University,Languages,...
Career Goal,College,Programming,...
```

### Modify Patterns

Edit the `MatchEvent` class patterns in `ResumeParser.py` to match different:
- Phone number formats (not just US)
- Address patterns (other countries)
- URL patterns (different social networks)

### Add New Sections

Extend `SECTION_TITLE` list:
```python
SECTION_TITLE = ['CandidateInformation', 'SummaryText', 'YourCustomSection', ...]
```

## License

GNU General Public License v3 (GPL-3.0)

## Contributing

To improve the parser:
1. Add support for more file formats
2. Improve pattern matching accuracy
3. Add multilingual support
4. Enhance error handling
5. Add unit tests

See CODEBASE.md for architecture details.
