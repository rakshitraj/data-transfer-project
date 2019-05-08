#!/bin/bash
rm RECORD/master_record.csv
python3 SERVER/server.py 0.0.0.0 10000
