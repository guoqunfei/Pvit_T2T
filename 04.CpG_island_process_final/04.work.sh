#!/bin/bash

##This script is used to find the CpG island closest to the TSS site and a randomly selected genome_win with the same number of Cpg islands, and calculate their distance.

CpGisland="/your/path/to/your/CpGisland_link.gff"
Annotation="/your/path/to/your/Annotation.gff"

less ${CpGisland} | awk '{print $1 "\t" $4 "\t"  $5}' > CpG_island.list
awk 'BEGIN {FS="\t"} $3 == "mRNA" && $7 == "+" {print $1 "\t" $4} $3 == "mRNA" && $7 == "-" {print $1 "\t" $5}' ${Annotation} > TSS.list

/your/path/to/python3 04.Distance.py CpG_island.list TSS.list > CpGisland_TSS_min_distance.txt

###Randomly select  windows with the same number of CpG islands in the 200bp window of the genome, and use the same method to find the window closest to each TSS and calculate the distance.
