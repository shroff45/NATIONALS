import pytest
import sys
import os
import asyncio

# Ensure backend directory is in path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.judgment_validator import JudgmentValidatorService, get_judgment_validator_service
from app.schemas.judgment import JudgmentValidateRequest, ValidityStatus, IssueCategory, IssueSeverity

@pytest.fixture
def service():
    return get_judgment_validator_service()

@pytest.mark.asyncio
async def test_validate_complete_judgment(service):
    text = """
    IN THE SUPREME COURT OF INDIA
    CRIMINAL APPELLATE JURISDICTION

    Prosecution Versus Accused

    Brief Facts of the Case:
    The respondent was charged under Section 302 of the IPC.

    Issues for Consideration:
    Whether the lower court erred in acquitting the accused.

    Arguments of Prosecution:
    The learned counsel submitted that the evidence was sufficient.

    Analysis:
    The court has considered the submissions.
    We refer to the case of (2020) 5 SCC 123.
    Article 21 guarantees right to life.

    Order:
    The appeal is dismissed. The respondent is acquitted.
    """

    request = JudgmentValidateRequest(
        case_id="TEST-001",
        judgment_text=text,
        judgment_type="judgment",
        offense_sections=["302"]
    )

    response = await service.validate(request)

    assert response.status == ValidityStatus.VALID
    assert response.overall_score >= 80
    assert "✅ Contains Case title with parties" in response.strengths
    assert "✅ Contains Statement of facts" in response.strengths
    assert "✅ Contains Issues for determination" in response.strengths
    assert "✅ Contains Arguments of both sides" in response.strengths
    assert "✅ Contains Court's analysis" in response.strengths
    assert "✅ Contains Final order/disposal" in response.strengths
    assert "✅ References constitutional provisions" in response.strengths

    # Check that no critical issues are present
    critical_issues = [i for i in response.issues if i.severity == IssueSeverity.CRITICAL]
    assert len(critical_issues) == 0

@pytest.mark.asyncio
async def test_validate_missing_sections(service):
    text = """
    This is a text without proper sections.
    """

    request = JudgmentValidateRequest(
        case_id="TEST-002",
        judgment_text=text,
        judgment_type="judgment",
        offense_sections=["302"]
    )

    response = await service.validate(request)

    # Expect warnings/critical issues for missing sections
    missing_issues = [i for i in response.issues if "Missing:" in i.title]
    assert len(missing_issues) > 0

    # Check specifically for Order section missing (Critical)
    order_missing = any(i.title == "Missing: Final order/disposal" and i.severity == IssueSeverity.CRITICAL for i in response.issues)
    assert order_missing

@pytest.mark.asyncio
async def test_validate_constitutional_reference(service):
    text = """
    analysis
    Fundamental rights are important.
    """
    # Just checking logic for constitutional reference, so minimal text

    request = JudgmentValidateRequest(
        case_id="TEST-003",
        judgment_text=text,
        judgment_type="judgment"
    )

    # The service checks mandatory sections, so this will fail validation overall,
    # but we can check if the strength was added.

    response = await service.validate(request)
    assert "✅ References constitutional provisions" in response.strengths

@pytest.mark.asyncio
async def test_validate_no_constitutional_reference(service):
    text = """
    analysis
    No mention of constitution here.
    """

    request = JudgmentValidateRequest(
        case_id="TEST-004",
        judgment_text=text,
        judgment_type="judgment"
    )

    response = await service.validate(request)
    assert "✅ References constitutional provisions" not in response.strengths

@pytest.mark.asyncio
async def test_validate_order_specificity(service):
    # Case 1: Specific order
    text_specific = """
    Order:
    The appeal is dismissed.
    """
    request = JudgmentValidateRequest(case_id="TEST-005", judgment_text=text_specific)
    response = await service.validate(request)

    # Should NOT have "Order lacks specificity" issue
    specific_issue = any(i.title == "Order lacks specificity" for i in response.issues)
    assert not specific_issue

    # Case 2: Non-specific order
    text_vague = """
    Order:
    The matter is disposed of accordingly.
    """
    # "disposed" is in mandatory section check regex, but NOT in order_keywords for specificity check
    # order_keywords = ["acquitted", "convicted", "dismissed", "allowed", "bail granted", "bail rejected", "discharged"]

    request = JudgmentValidateRequest(case_id="TEST-006", judgment_text=text_vague)
    response = await service.validate(request)

    # Should have "Order lacks specificity" issue
    specific_issue = any(i.title == "Order lacks specificity" for i in response.issues)
    assert specific_issue
