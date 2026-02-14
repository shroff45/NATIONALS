
import pytest
import re
from app.services.judgment_validator import JudgmentValidatorService, get_judgment_validator_service
from app.schemas.judgment import JudgmentValidateRequest, ValidityStatus, IssueCategory, IssueSeverity

@pytest.fixture
def service():
    return get_judgment_validator_service()

@pytest.mark.asyncio
async def test_validate_complete_judgment(service):
    text = """
    IN THE COURT OF SESSIONS JUDGE, CYBER CITY
    Prosecution vs. Accused

    BRIEF FACTS OF THE CASE:
    The prosecution case is that...

    POINTS FOR DETERMINATION:
    1. Whether the accused is guilty?

    ARGUMENTS AND SUBMISSIONS:
    The prosecution argued...

    ANALYSIS AND DISCUSSION:
    Based on (2024) 5 SCC 123...

    ORDER:
    The accused is convicted.
    """
    request = JudgmentValidateRequest(
        case_id="TEST-001",
        judgment_text=text,
        offense_sections=["BNS 303"]
    )
    response = await service.validate(request)

    # Debug info if assertion fails
    if response.status != ValidityStatus.VALID:
        print("\nIssues found:")
        for issue in response.issues:
            print(f"- {issue.title}: {issue.description}")

    assert response.status == ValidityStatus.VALID
    assert response.overall_score >= 80
    assert "✅ Contains Case title with parties" in response.strengths
    assert "✅ Contains Statement of facts" in response.strengths

@pytest.mark.asyncio
async def test_validate_missing_sections(service):
    text = """
    Just some random text without proper sections.
    """
    request = JudgmentValidateRequest(
        case_id="TEST-002",
        judgment_text=text,
        offense_sections=[]
    )
    response = await service.validate(request)

    assert response.status != ValidityStatus.VALID
    # Check for missing section issues
    missing_issues = [i for i in response.issues if i.category == IssueCategory.PROCEDURAL]
    assert len(missing_issues) > 0

@pytest.mark.asyncio
async def test_validate_case_insensitivity(service):
    text = """
    brief facts of the case:
    some facts.

    points for determination:
    some issues.
    """
    # Just checking regex matching on lowercase input
    # The service lowercases the input text internally

    request = JudgmentValidateRequest(
        case_id="TEST-003",
        judgment_text=text,
        offense_sections=[]
    )
    response = await service.validate(request)

    # We expect it to find "facts" and "issues"
    strengths_text = " ".join(response.strengths)
    assert "Statement of facts" in strengths_text
    assert "Issues for determination" in strengths_text
