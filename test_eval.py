from evaluator import evaluate_response

query = "What happens during the first 90 days?"

context = """
Complete role-specific technical training.
Mid-probation check-in with manager.
Provide onboarding feedback.
Set development goals.
"""

response = """
During the first 90 days, employees complete role-specific training,
attend a manager check-in, provide onboarding feedback,
and establish development goals.
"""

result = evaluate_response(
    query,
    context,
    response
)

print(result)