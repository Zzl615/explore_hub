#!/bin/bash

# Run the Python unittest for encrypt_info.test
python -m unittest encrypt_info.test

# Check if the tests passed
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above for details."
fi
