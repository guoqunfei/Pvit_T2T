#!/bin/bash

##This script is used to generate a gff file of GC_Content and CpG_OE values for a random 200bp window in the genome, and then calculate the number of CpG islands and random window overlaps in the genome at intervals of 200bp within the TSS site and its upstream and downstream 8kb.

Genome="/your/path/to/your/Genome.fa"

#Generate a gff file of GC_Content and CpG_OE values for a random 200bp window in the genome

/your/path/to/python3 03.Genome_win.py ${Genome} 

#Calculate the number of CpG islands and random window overlaps in the genome within 8 kb upstream and downstream of the TSS site at intervals of 200 bp.

CpGisland="/your/path/to/CpGisland.gff"
Genomewin="/your/path/to/Genomewin.gff"
Annotation="/your/path/to/Annotation.gff"

/your/path/to/python3 03.Overlap_TSS_CpGisland_num.py ${CpGisland} ${Annotation} > Overlap_TSS_CpGisland_num.txt 
/your/path/to/python3 03.Overlap_TSS_Genomewin_num.py ${Genomewin} ${Annotation} > Overlap_TSS_Genomewin_num.txt
