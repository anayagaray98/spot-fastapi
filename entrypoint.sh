#!/bin/sh

set -e

uvicorn app.main:app --reload --host 0.0.0.0 --timeout-keep-alive 2400

