from agent import client
from tools import get_role_skills, read_pdf


def run_agent(query):

    query_lower = query.lower()

    if "data analyst" in query_lower:

        skills = get_role_skills("Data Analyst")

        prompt = f"""
        User wants information about becoming a Data Analyst.
        Skills:{skills}
        Explain these skills and suggest a learning path.
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user","content": prompt}]
        )

        return response.choices[0].message.content

    elif "software engineer" in query_lower:

        skills = get_role_skills("Software Engineer")

        prompt = f"""User wants information about becoming a Software Engineer.
        Skills:{skills}
        Explain these skills and suggest a learning path.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user","content": prompt}]
            )

        return response.choices[0].message.content

    elif "ai engineer" in query_lower:

        skills = get_role_skills("AI Engineer")
        
        prompt = f"""
        User wants information about becoming an AI Engineer.
        Skills:{skills}
        Explain these skills and suggest a learning path.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user","content": prompt}]
        )

        return response.choices[0].message.content

    elif "summarize" in query_lower:

        pdf_text = read_pdf(
            "knowledge/onboarding_doc.pdf"
        )

        prompt = f"""Summarize the following document:{pdf_text}"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user","content": prompt}]
        )
        return response.choices[0].message.content

    elif any(word in query_lower for word in [
        "onboarding",
        "salary",
        "leave",
        "benefits",
        "safety",
        "probation",
        "90 days",
        "30 days",
        "first week",
        "day 1",
        "contact",
        "training"
    ]):

        pdf_text = read_pdf("knowledge/onboarding_doc.pdf")
        prompt = f"""
        Use ONLY the information below to answer.
        Document:{pdf_text}
        Question:{query}"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user","content": prompt}]
        )
        return response.choices[0].message.content

    else:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user","content": query}]
            )
        return response.choices[0].message.content