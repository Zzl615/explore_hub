#!/bin/bash

# Run pytest for the encrypt_case/tortoise_case directory
python -m encrypt_case.tortoise_case.test

# Check if the tests passed
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above for details."
fi
