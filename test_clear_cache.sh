#!/bin/bash
#
ATTEMPTS=100
FAILURES=0

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
ATTEMPT=1
while [ ${ATTEMPT} -lt ${ATTEMPTS} ]; do
    python ${THIS_DIR}/test_clear_cache.py
    if [ $? == 0 ]; then
        echo "Attempt ${ATTEMPT}: success"
    else
        echo "Attempt ${ATTEMPT}: FAILURE"
        FAILURES=$((${FAILURES}+1))
    fi
    ATTEMPT=$((${ATTEMPT}+1))
done

echo "Total attempts: ${ATTEMPTS}"
echo "Failed: ${FAILURES}"
