#!/bin/bash

# Run the Python unittest for auth_code.test
python -m unittest auth_code.test

# Check if the tests passed
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above for details."
fi
