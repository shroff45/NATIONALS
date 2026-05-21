import pytest
import sys
import uuid
from datetime import datetime, timedelta
import networkx as nx
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.financial_service import FinancialAnalyzer
from app.schemas.financial import Transaction, Account, TransactionType

def test_cycles():
    analyzer = FinancialAnalyzer()
    analyzer.graph = nx.DiGraph()
    # create dense graph
    for i in range(50):
        for j in range(5):
            target_idx = (i + j + 1) % 50
            analyzer.graph.add_edge(f"ACC_{i}", f"ACC_{target_idx}", weight=15000.0)

    start_time = time.time()
    try:
        import itertools
        # Lazily evaluate cycles!
        cycles_gen = nx.simple_cycles(analyzer.graph)
        cycles = list(itertools.islice(cycles_gen, 100))
        print(f"Time: {time.time() - start_time:.4f} seconds, Cycles: {len(cycles)}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    test_cycles()
