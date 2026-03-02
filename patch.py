import re

with open('backend/app/services/judgment_validator.py', 'r') as f:
    content = f.read()

# Replace MANDATORY_SECTIONS initialization
old_sections = """    MANDATORY_SECTIONS = [
        ("parties", r"(petitioner|appellant|complainant|prosecution)\s*(v\.?s?\.?|versus)\s*(respondent|accused|defendant)", "Case title with parties"),
        ("facts", r"(brief facts|facts of the case|factual matrix)", "Statement of facts"),
        ("issues", r"(issues? (for|to be) (consideration|decided)|points? for determination)", "Issues for determination"),
        ("arguments", r"(arguments?|submissions?|contentions?)\s*(of|by)\s*(prosecution|defence|petitioner|respondent)", "Arguments of both sides"),
        ("analysis", r"(analysis|discussion|reasoning|consideration)", "Court's analysis"),
        ("order", r"(order|judgment|decree|verdict|disposed)", "Final order/disposal"),
    ]"""

new_sections = """    MANDATORY_SECTIONS = [
        ("parties", re.compile(r"(petitioner|appellant|complainant|prosecution)\s*(v\.?s?\.?|versus)\s*(respondent|accused|defendant)", re.IGNORECASE), "Case title with parties"),
        ("facts", re.compile(r"(brief facts|facts of the case|factual matrix)", re.IGNORECASE), "Statement of facts"),
        ("issues", re.compile(r"(issues? (for|to be) (consideration|decided)|points? for determination)", re.IGNORECASE), "Issues for determination"),
        ("arguments", re.compile(r"(arguments?|submissions?|contentions?)\s*(of|by)\s*(prosecution|defence|petitioner|respondent)", re.IGNORECASE), "Arguments of both sides"),
        ("analysis", re.compile(r"(analysis|discussion|reasoning|consideration)", re.IGNORECASE), "Court's analysis"),
        ("order", re.compile(r"(order|judgment|decree|verdict|disposed)", re.IGNORECASE), "Final order/disposal"),
    ]"""

content = content.replace(old_sections, new_sections)

# Replace re.search call
old_search = """        # --- Check 1: Mandatory Sections ---
        for section_key, pattern, label in self.MANDATORY_SECTIONS:
            if not re.search(pattern, text, re.IGNORECASE):"""

new_search = """        # --- Check 1: Mandatory Sections ---
        for section_key, pattern, label in self.MANDATORY_SECTIONS:
            if not pattern.search(text):"""

content = content.replace(old_search, new_search)

# Remove memory leak (self.reports initialization)
old_init = """    def __init__(self):
        self.reports: Dict[str, JudgmentValidateResponse] = {}

    async def validate(self, request: JudgmentValidateRequest) -> JudgmentValidateResponse:"""

new_init = """    async def validate(self, request: JudgmentValidateRequest) -> JudgmentValidateResponse:"""

content = content.replace(old_init, new_init)

# Remove memory leak (self.reports assignment)
old_assign = """        self.reports[result_id] = response
        return response"""

new_assign = """        return response"""

content = content.replace(old_assign, new_assign)

with open('backend/app/services/judgment_validator.py', 'w') as f:
    f.write(content)
