#!/bin/bash
# Mock out the 'requests' import in the test files so pytest discovery works.
for file in ../backend/test_auth.py ../backend/test_auth_comprehensive.py ../backend/test_endpoints.py ../backend/test_evidence.py; do
    # Add a mock at the top of the file before imports
    sed -i '1i import sys, mock\nsys.modules["requests"] = mock.Mock()\n' "$file"
done
