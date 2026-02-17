import asyncio
from app.services.judgment_validator import JudgmentValidatorService
from app.schemas.judgment import JudgmentValidateRequest, ValidityStatus, IssueSeverity

async def run_tests():
    service = JudgmentValidatorService()

    # Test Case 1: Valid judgment matching strict regexes
    # "Prosecution" is required by the regex for parties
    text = """
    Prosecution vs. Accused
    Brief Facts of the Case: The accused stole a car.
    Issues for Consideration: Whether the accused is guilty.
    Arguments of Prosecution: He was seen on CCTV.
    Analysis: The evidence is clear.
    Order: The accused is convicted.
    (2024) 5 SCC 123
    """
    request = JudgmentValidateRequest(
        case_id="TEST-1",
        judgment_text=text,
        offense_sections=["BNS 303(2)"]
    )

    response = await service.validate(request)

    # Print issues if validation fails
    if response.status == ValidityStatus.CRITICAL_ISSUES:
        print("Validation FAILED with CRITICAL ISSUES:")
        for issue in response.issues:
            if issue.severity == IssueSeverity.CRITICAL:
                print(f" - {issue.title}: {issue.description}")

    assert response.status != ValidityStatus.CRITICAL_ISSUES, "Validation failed unexpectedly"

    # Check citation was found (it is in strengths)
    citation_found = any("citation" in s.lower() for s in response.strengths)
    assert citation_found, "Citation not found"

    print("Logic test PASSED")

    # Test Case 2: Memory Leak Check
    # This should FAIL if 'reports' exists on service
    if hasattr(service, "reports"):
        print("Memory Leak Check: FAILED ('reports' attribute exists)")
        raise AssertionError("Memory Leak: 'reports' attribute still exists on service")
    else:
        print("Memory Leak Check: PASSED ('reports' attribute does not exist)")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_tests())
    loop.close()
