# Resume Parser - Codebase Documentation

## Overview

Resume Parser is a Python-based NLP tool for extracting structured information from resume documents. It uses **spaCy** (Natural Language Processing library) to identify and extract key information such as:
- Full Name
- Email Address
- Phone Number
- Address
- LinkedIn URL
- GitHub URL
- Work Experience
- Education
- Skills & Technologies
- And more

## Project Structure

```
Resume-Parser/
├── ResumeParser.py          # Main parser class implementation
├── test.py                  # Test utilities and helper functions
├── section_title.csv        # CSV file with section keywords/aliases
├── README.md                # Project overview
├── CODEBASE.md             # This file
└── LICENSE                 # GNU General Public License v3
```

## Dependencies

### Required Python Packages

- **spacy** (>=3.0.0) - Natural Language Processing
- **python-docx** (>=0.8.10) - Parse .docx files
- **pandas** (>=1.0.0) - Data manipulation and CSV reading
- **docx2txt** (>=0.8) - Convert DOCX to text

### Installation

```bash
# Install required packages
pip install spacy python-docx pandas docx2txt

# Download the spaCy English model
python -m spacy download en_core_web_sm
```

## Core Components

### 1. **MatchEvent Class** (`ResumeParser.py`)

Defines regex-like patterns for matching resume information using spaCy's matcher:

- **PERSON_PATTERN**: Matches full names (sequence of PROPN tokens)
- **EMAIL_ID_PATTERN**: Matches email addresses using `LIKE_EMAIL` attribute
- **PHONE_PATTERN_1**: Matches phone format like `123-456-7890`
- **PHONE_PATTERN_2**: Matches phone format like `(123) 456-7890`
- **ADDRESS_PATTERN**: Matches full addresses with US state codes
- **LINKEDIN_URL_PATTERN**: Matches LinkedIn URLs
- **GIT_URL_PATTERN**: Matches GitHub URLs

**Callback Methods:**
- `full_name_event()`: Custom callback for processing full name matches
- `summary_text_event()`: Placeholder for summary text processing

### 2. **ResumeParser Class** (`ResumeParser.py`)

Main class for parsing resume documents.

**Key Attributes:**
- `nlp`: Shared spaCy language model (loaded once)
- `CANDIDATE_INFO`: List of info patterns to extract
- `SECTION_TITLE`: List of resume section types
- `PROFILE_INFORMATION`: Storage for extracted data

**Key Methods:**

| Method | Purpose |
|--------|---------|
| `__init__(file_name)` | Initialize parser with DOCX file |
| `convert_docx2txt(file_name)` | Convert DOCX to plain text |
| `load_data(data)` | Segment resume into sections using keywords |
| `get_candidate_info(title)` | Extract structured info (name, email, phone, etc.) |
| `get_summary_text(title)` | Extract summary/objective section |
| `get_work_experience(title)` | Extract work experience entries |
| `parse_information()` | Main parsing orchestrator |

### 3. **Test Module** (`test.py`)

Contains helper functions for testing and development:

- `convert_docx2txt()`: Convert DOCX to text
- `read_csv()`: Load section keywords from CSV
- `get_section_data()`: Extract resume sections
- `print_details()`: Display extracted section data
- `print_entity()`: Placeholder for entity analysis

### 4. **Section Keywords** (`section_title.csv`)

CSV file mapping resume section names to various aliases/keywords. Includes columns for:
- SummaryText
- Education
- ToolsAndTechnologies
- WorkExperience
- Extra-curricular
- AwardsAndRecognition

This allows flexible section detection (e.g., "Summary", "Professional Summary", "Career Summary" all map to SummaryText).

## Usage

### Basic Example

```python
from ResumeParser import ResumeParser

# Create parser instance with resume file
parser = ResumeParser('path/to/resume.docx')

# Extract all information
resume_data = parser.parse_information()

# Access specific information
print(resume_data)
```

### Expected Output Format

```python
{
    'CandidateInformation': {
        'FullName': 'John Doe',
        'Email': 'john.doe@example.com',
        'Phone': '123-456-7890',
        'Address': '123 Main St New York NY',
        'LinkedInURL': 'https://linkedin.com/in/johndoe',
        'GithubURL': 'https://github.com/johndoe'
    },
    'SummaryText': 'Professional summary here...',
    'WorkExperience': [
        'Job 1 description...',
        'Job 2 description...'
    ]
}
```

## Known Limitations & Future Improvements

1. **File Format**: Currently only supports `.docx` files (not PDF or plain text)
2. **Language**: Only works with English resumes
3. **Phone Patterns**: Limited to US phone number formats
4. **Address Detection**: Only recognizes US state abbreviations
5. **Incomplete Features**: 
   - `summary_text_event()` callback not fully implemented
   - Some pattern matching callbacks not utilized
6. **Error Handling**: Minimal error handling for malformed documents

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'spacy'`
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

**Issue**: `FileNotFoundError: section_title.csv not found`
- Ensure `section_title.csv` is in the same directory as the script
- Use absolute paths or ensure working directory is set correctly

**Issue**: No data extracted from resume
- Verify resume format matches expected structure (has clear section headers)
- Check that section headers match keywords in `section_title.csv`
- Ensure spaCy model is properly trained on your resume format

## Development Notes

### Code Quality Issues (Fixed)

1. Hard-coded file paths removed
2. Unused test data removed
3. Better error handling for missing files
4. Cleaner code structure

### Architecture

The parser uses a two-stage extraction approach:

1. **Section Segmentation**: Uses PhraseMatcher to find section headers
2. **Information Extraction**: Uses Matcher patterns to extract specific entities from each section

## License

GNU General Public License v3 (GPL-3.0)

See LICENSE file for full terms.

## Contributing

To contribute improvements:

1. Fix any remaining edge cases in pattern matching
2. Add support for additional file formats (PDF, TXT)
3. Implement multilingual support
4. Improve error handling and logging
5. Add comprehensive unit tests

## Related Resources

- [spaCy Documentation](https://spacy.io/)
- [Pattern Matching in spaCy](https://spacy.io/usage/rule-based-matching)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
