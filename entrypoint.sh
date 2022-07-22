#!/bin/sh
uvicorn \
  main:instance \
    --host 0.0.0.0 \
    --port 8080 \
    --reload
