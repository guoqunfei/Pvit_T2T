#!/usr/bin/bash

##This script is used to generate the CpG_island_link.gff file

echo start at `date`

genome="/path/to/your/CpG_island.gff"

/path/to/your/python3 CpG_island_link.py ${genome}
echo "$?:/path/to/your/python3 CpG_island_link.py ${genome} "

echo end at `date`

