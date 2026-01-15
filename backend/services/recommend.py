def analyze_and_inject_context(user_message: str) -> str:
    """
    Analyze what the student is asking about and
    add resource hints to guide the LLM.
    """

    msg = user_message.lower()
    suggestions = []

 
    if any(word in msg for word in ["internship", "career", "resume", "jobs", "job"]):
        suggestions.append(
            "The student might benefit from the university's Career Center, resume review services, Handshake platform, and internship search support."
        )

 
    if any(word in msg for word in ["stress", "stressed", "anxiety", "burnout", "homesick", "mental"]):
        suggestions.append(
            "You can mention mental health resources such as campus counseling center, wellness programs, and student support groups."
        )

  
    if any(word in msg for word in ["class", "classes", "professor", "study", "assignment", "exam", "tutor"]):
        suggestions.append(
            "You can suggest academic advising, tutoring center, writing center, library study rooms, and professor office hours."
        )

    

    if any(word in msg for word in ["scholarship", "scholarships", "fees", "financial", "aid", "money"]):
        suggestions.append(
            "You can recommend contacting the Financial Aid Office, scholarship portal, emergency fund, or student employment office."
        )

   
    if any(word in msg for word in ["friends", "alone", "events", "clubs", "community"]):
        suggestions.append(
            "You can suggest student organizations, campus events, cultural groups, and involvement opportunities."
        )

  
    if not suggestions:
        suggestions.append(
            "Offer general guidance and ask a follow-up question to understand their situation better."
        )

   
    context = "\n".join(suggestions)

    final_prompt = f"""
User message: "{user_message}"

Context suggestions for the assistant:
{context}

Now respond in a helpful, friendly, student-support tone.
"""

    return final_prompt.strip()
