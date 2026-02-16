
import pytest
import sys
import os
import asyncio

# Ensure backend directory is in path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from app.services.judgment_validator import get_judgment_validator_service
from app.schemas.judgment import JudgmentValidateRequest, ValidityStatus, IssueCategory

@pytest.mark.asyncio
async def test_judgment_validation_complete():
    """Test with a complete judgment that should be valid"""
    service = get_judgment_validator_service()

    # Reset reports if it exists (before fix)
    if hasattr(service, 'reports'):
        service.reports = {}

    request = JudgmentValidateRequest(
        case_id="TEST-CASE-001",
        judgment_text="""
        IN THE COURT OF SESSIONS JUDGE, CYBER CITY
        State Prosecution vs Accused Suresh Kumar
        FIR No. 42/2025 under BNS Section 303(2)

        BRIEF FACTS OF THE CASE:
        The prosecution case is that on 15.01.2025, the accused Suresh Kumar
        committed theft at Shop No. 12, Sector 4 Market.

        POINTS FOR DETERMINATION:
        1. Whether the prosecution has proved the guilt of the accused beyond
        reasonable doubt?

        ARGUMENTS OF PROSECUTION:
        The prosecution argued that CCTV footage (Exhibit P-1) and witness
        testimony clearly establish the presence of accused. The defence
        submitted that the identification is unreliable.

        ANALYSIS AND DISCUSSION:
        Having considered the evidence on record, this Court notes that the
        CCTV footage corroborates the eyewitness account of PW-1.
        As held in Tomaso Bruno v State of UP (2015) 7 SCC 178, circumstantial
        evidence must form a complete chain. Also refer AIR 2024 SC 456.
        Constitutional provisions under Article 21 were considered.

        ORDER:
        The accused is convicted under BNS Section 303(2).
        """,
        offense_sections=["BNS 303(2)"]
    )

    response = await service.validate(request)

    # If assertions fail, print issues for debugging
    if response.status != ValidityStatus.VALID:
        print("\nValidation Failed. Issues found:")
        for issue in response.issues:
            print(f"- [{issue.severity}] {issue.title}: {issue.description}")

    assert response.case_id == "TEST-CASE-001"
    assert response.status == ValidityStatus.VALID
    assert response.overall_score >= 80

    # Check strengths
    assert any("Contains Case title with parties" in s for s in response.strengths)
    assert any("Contains Statement of facts" in s for s in response.strengths)
    assert any("Contains Issues for determination" in s for s in response.strengths)
    assert any("Contains Arguments of both sides" in s for s in response.strengths)
    assert any("Contains Court's analysis" in s for s in response.strengths)
    assert any("Contains Final order/disposal" in s for s in response.strengths)
    assert any("Contains 2 case citation(s)" in s for s in response.strengths)
    assert any("References constitutional provisions" in s for s in response.strengths)

    # Check issues (should be empty or minor)
    critical_issues = [i for i in response.issues if i.severity == "critical"]
    assert len(critical_issues) == 0

@pytest.mark.asyncio
async def test_judgment_validation_missing_sections():
    """Test with missing mandatory sections"""
    service = get_judgment_validator_service()

    request = JudgmentValidateRequest(
        case_id="TEST-CASE-002",
        judgment_text="""
        State vs. Accused
        Brief facts: Something happened.
        Order: Dismissed.
        """,
        offense_sections=[]
    )

    response = await service.validate(request)

    # Should be missing issues, arguments, analysis
    issues_titles = [i.title for i in response.issues]
    assert "Missing: Issues for determination" in issues_titles
    assert "Missing: Arguments of both sides" in issues_titles
    assert "Missing: Court's analysis" in issues_titles

    # Order is present but maybe not specific enough? "Dismissed" is specific.
    # Check if "Order: Dismissed" passes the order specificity check.
    # The code checks for keywords in the whole text. "dismissed" is in text.
    assert not any("Order lacks specificity" in t for t in issues_titles)

@pytest.mark.asyncio
async def test_judgment_validation_case_insensitivity():
    """Test that validation works regardless of casing in headers"""
    service = get_judgment_validator_service()

    request = JudgmentValidateRequest(
        case_id="TEST-CASE-003",
        judgment_text="""
        PETITIONER VS RESPONDENT

        FACTUAL MATRIX:
        Some facts.

        POINTS FOR DETERMINATION:
        Is he guilty?

        SUBMISSIONS OF PROSECUTION:
        He did it.

        REASONING:
        Because of evidence.

        VERDICT:
        The accused is ACQUITTED.
        """,
        offense_sections=[]
    )

    response = await service.validate(request)

    issues_titles = [i.title for i in response.issues]

    # Should verify that capitalized headers are detected
    assert not any("Missing: Case title with parties" in t for t in issues_titles)
    assert not any("Missing: Statement of facts" in t for t in issues_titles)
    assert not any("Missing: Issues for determination" in t for t in issues_titles)
    assert not any("Missing: Arguments of both sides" in t for t in issues_titles)
    assert not any("Missing: Court's analysis" in t for t in issues_titles)
    assert not any("Missing: Final order/disposal" in t for t in issues_titles)

    # Check order specificity
    assert not any("Order lacks specificity" in t for t in issues_titles)

if __name__ == "__main__":
    # Allow running directly
    pytest.main([__file__])
