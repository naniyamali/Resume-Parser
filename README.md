# Resume Parser

A Python-based NLP tool for extracting structured information from resumes using **spaCy**.

## Features

✨ **Extract Key Information:**
- Full Name
- Email Address  
- Phone Number
- Address
- LinkedIn URL
- GitHub URL
- Work Experience
- Education
- Technical Skills
- And more...

📄 **Supported Formats:**
- DOCX (Microsoft Word)
- PDF (Portable Document Format)

🔍 **Smart Parsing:**
- Uses spaCy NLP for accurate entity recognition
- Section-based extraction for organized data
- Flexible pattern matching for various formats

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/naniyamali/Resume-Parser.git
cd Resume-Parser

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### Usage

```python
from ResumeParser import ResumeParser

# Parse a resume (DOCX or PDF)
parser = ResumeParser('./resumes/resume.pdf')
result = parser.parse_information()
print(result)
```

### Example Output

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
    'SummaryText': 'Experienced professional with 5+ years...',
    'WorkExperience': ['Job 1 details...', 'Job 2 details...']
}
```

## Documentation

- **[CODEBASE.md](./CODEBASE.md)** - Detailed architecture and components
- **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - Installation and usage guide
- **[section_title.csv](./section_title.csv)** - Customizable section keywords

## Project Structure

```
Resume-Parser/
├── ResumeParser.py       # Main parser class
├── test.py               # Test utilities
├── section_title.csv     # Resume section keywords
├── requirements.txt      # Dependencies
├── README.md            # This file
├── CODEBASE.md          # Technical documentation
├── SETUP_GUIDE.md       # Setup and usage guide
└── LICENSE              # GNU GPL v3
```

## Requirements

- Python 3.7+
- spacy >= 3.0.0
- python-docx >= 0.8.10
- pandas >= 1.0.0
- docx2txt >= 0.8
- PyPDF2 >= 3.0.0 (for PDF support)

See `requirements.txt` for complete list.

## How It Works

1. **File Conversion** - Converts DOCX/PDF to plain text
2. **Tokenization** - Uses spaCy to tokenize and process text
3. **Section Detection** - Identifies resume sections using keyword matching
4. **Entity Extraction** - Extracts specific information using pattern matching
5. **Data Organization** - Returns structured data as dictionary

## Supported Information

| Category | Extracted Data |
|----------|-----------------|
| Contact | Name, Email, Phone, Address, URLs |
| Professional | Summary, Work Experience, Skills |
| Education | Degree, University, Courses |
| Technical | Programming Languages, Tools, Technologies |
| Additional | Certifications, Awards, Affiliations |

## Customization

### Add Section Keywords

Edit `section_title.csv` to customize resume section detection:

```csv
SummaryText,Education,...
My Objective,University,...
Career Goal,College,...
```

### Modify Patterns

Edit regex patterns in `ResumeParser.py` `MatchEvent` class to match different:
- Phone number formats
- Address formats  
- URL patterns
- Custom fields

## Limitations

- ⚠️ **Language**: English only
- ⚠️ **Phone**: US format only
- ⚠️ **PDF**: Text extraction depends on PDF structure
- ⚠️ **Pattern Matching**: Limited to configured patterns

## Future Improvements

- [ ] Multilingual support
- [ ] International phone number formats
- [ ] OCR for scanned PDFs
- [ ] Machine learning-based extraction
- [ ] Web UI for easy access
- [ ] Batch processing support
- [ ] Database export functionality

## Troubleshooting

**Issue**: No text extracted from resume
- **Solution**: Verify resume has clear section headers matching `section_title.csv`

**Issue**: PDF support error
- **Solution**: Install PyPDF2: `pip install PyPDF2`

**Issue**: spaCy model not found
- **Solution**: Download model: `python -m spacy download en_core_web_sm`

See [SETUP_GUIDE.md](./SETUP_GUIDE.md) for more troubleshooting.

## License

This project is licensed under the **GNU General Public License v3** - see [LICENSE](./LICENSE) file for details.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Contact & Support

- **GitHub**: [naniyamali/Resume-Parser](https://github.com/naniyamali/Resume-Parser)
- **Issue Tracker**: Report bugs via GitHub Issues

---

**Note**: This tool is designed for resume parsing and may require adjustments for specific resume formats or languages.

