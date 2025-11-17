"""Test module for Resume Parser"""
import os
import docx2txt
import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
section_title = ['CandidateInformation', 'SummaryText', 'ToolsAndTechnologies', 'WorkExperience', 'Education', 'Extra-curricular', 'AwardsAndRecognition']

def convert_docx2txt(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File not found: {file_name}")
    return docx2txt.process(file_name)

def read_csv():
    csv_path = './section_title.csv'
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    return pd.read_csv(csv_path)

def get_section_data(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"Resume file not found: {file_name}")
    txt = convert_docx2txt(file_name)
    doc = nlp(txt)
    matcher = PhraseMatcher(nlp.vocab)
    section_dict = read_csv()
    section_words = {}
    for section in section_title[1:]:
        section_words[section] = [nlp(text) for text in section_dict[section].dropna(axis=0)]
        matcher.add(section, None, *section_words[section])
    d = []
    matches = matcher(doc)
    if len(matches) > 0:
        d.append((section_title[0], doc[:matches[0][1]-1]))
    for index, section in enumerate(matches):
        match_id, start, end = section
        rule_id = nlp.vocab.strings[match_id]
        if index == len(matches) - 1:
            span = doc[end:]
        else:
            span = doc[end: matches[index + 1][1] - 1]
        if str(span.text) != '':
            d.append((rule_id, span.text))
    return d

def print_details(file_name):
    try:
        data = get_section_data(file_name)
        for n, d in data:
            print(f"{n}: {str(d)[:100]}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    print("Resume Parser Test Module")
