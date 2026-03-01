import pytest
from app.services.judgment_validator import JudgmentValidatorService
from app.schemas.judgment import JudgmentValidateRequest

@pytest.mark.asyncio
async def test_stateless_judgment_validator():
    service = JudgmentValidatorService()
    request = JudgmentValidateRequest(
        case_id="123",
        judgment_text="The petitioner versus respondent. Facts of the case. Issues for consideration. Arguments by prosecution. Court analysis. Final order disposed.",
        offense_sections=["BNS 101"]
    )
    # Ensure there is no self.reports dictionary
    assert not hasattr(service, "reports")

    response = await service.validate(request)
    assert response.case_id == "123"
    assert not hasattr(service, "reports")
