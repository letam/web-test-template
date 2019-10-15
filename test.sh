#!/bin/sh

source venv/bin/activate

echo EXECUTING: pytest "$@"
pytest "$@"
