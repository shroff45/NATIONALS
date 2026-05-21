import pytest
import sys
import uuid
from datetime import datetime, timedelta
import networkx as nx
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.financial_service import FinancialAnalyzer
from app.schemas.financial import Transaction, Account, TransactionType, FinancialAnalysisRequest

def test_financial_analyzer_performance():
    analyzer = FinancialAnalyzer()

    # Generate a somewhat dense graph to test nx.all_simple_paths and nx.simple_cycles
    transactions = []
    accounts = []
    for i in range(50):
        accounts.append(Account(
            account_number=f"ACC_{i}",
            bank_name="TestBank",
            account_holder=f"Holder_{i}",
            account_type="savings"
        ))

    # Create circular flows and layering
    for i in range(40):
        for j in range(10):
            target_idx = (i + j + 1) % 50
            transactions.append(Transaction(
                id=str(uuid.uuid4()),
                from_account=f"ACC_{i}",
                to_account=f"ACC_{target_idx}",
                amount=15000.0,
                date=datetime.now() - timedelta(days=j),
                description=f"Transfer {i} to {target_idx}",
                type=TransactionType.TRANSFER,
                channel="NEFT"
            ))

    print(f"Generated {len(transactions)} transactions")

    request = FinancialAnalysisRequest(
        case_id="case_123",
        transactions=transactions,
        accounts=accounts,
        focus_accounts=["ACC_0"]
    )

    start_time = time.time()
    result = analyzer.analyze(request)
    end_time = time.time()

    print(f"Analysis took {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    test_financial_analyzer_performance()
