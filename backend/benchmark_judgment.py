
import sys
import os
import time
import asyncio
# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from app.services.judgment_validator import get_judgment_validator_service
from app.schemas.judgment import JudgmentValidateRequest

async def run_benchmark():
    service = get_judgment_validator_service()

    # Reset reports just in case
    if hasattr(service, 'reports'):
        service.reports = {}

    request = JudgmentValidateRequest(
        case_id="BENCHMARK-001",
        judgment_text="""
        IN THE COURT OF SESSIONS JUDGE, CYBER CITY
        State vs. Accused
        FIR No. 42/2025

        BRIEF FACTS: The case involves...
        ISSUES FOR DETERMINATION: Guilt of accused.
        ARGUMENTS: Prosecution says X. Defence says Y.
        ANALYSIS: Evidence suggests guilt. (2024) 5 SCC 123.
        ORDER: The accused is convicted.
        """ * 10, # Make it longer
        offense_sections=["BNS 303(2)"]
    )

    start_time = time.time()
    iterations = 1000

    print(f"Running validation {iterations} times...")
    for _ in range(iterations):
        await service.validate(request)

    end_time = time.time()
    duration = end_time - start_time

    print(f"Total time: {duration:.4f} seconds")
    print(f"Average time per call: {duration/iterations*1000:.4f} ms")

    if hasattr(service, 'reports'):
        print(f"Service reports count: {len(service.reports)}")
        if len(service.reports) == iterations:
            print("⚠️ MEMORY LEAK DETECTED: self.reports is growing!")
    else:
        print("✅ No reports attribute found (Memory leak fixed or not present)")

if __name__ == "__main__":
    asyncio.run(run_benchmark())
