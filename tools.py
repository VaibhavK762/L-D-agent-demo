import pandas as pd
from pypdf import PdfReader

skills_df = pd.read_csv("knowledge/skills.csv")


def get_role_skills(role):
    """
    Return skills for a given role
    """
    result = skills_df[skills_df["Role"].str.lower() == role.lower()]
    if result.empty:
        return None

    return result.iloc[0]["Skills"]


def read_pdf(pdf_path):
    """
    Extract text from PDF
    """
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text