#!/bin/bash
rm ../record/master_record.csv
python3 ../server/server.py 0.0.0.0 10000
