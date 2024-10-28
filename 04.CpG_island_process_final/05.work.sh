#!/bin/bash

##This script is used to calculate the number of CpG islands and missing zone overlaps and set a certain threshold.

CpGisland="/your/path/to/CpGisland.bed"
Missing="/your/path/to/Missing_zone.bed"

/your/path/to/python3 05.CpGisland_overlap_missing_num.py ${CpGisland} ${Missing}
