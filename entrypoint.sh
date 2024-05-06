#!/bin/sh

for i in /duckdb/sql/*.py; do eval "python $i"; done

