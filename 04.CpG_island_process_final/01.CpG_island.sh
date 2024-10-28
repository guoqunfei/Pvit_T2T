#!/usr/bin/bash

##This script is used to generate the CpG_island.gff file

echo start at `date`

genome="/path/to/your/genome.fa"

/path/to/your/python3 CpG_island.py ${genome}
echo "$?:/path/to/your/python3 CpG_island.py ${genome} "

echo end at `date`
