echo start at `date`

## minimap2 software can be installed from https://github.com/lh3/minimap2 

read1=Cyclone.fa
read2=Cyclone.fa

path/to/minimap2 -t 8 -x ava-ont -X -g 500 ${read1} ${read2} > overlap.paf

less overlap.paf | awk '($4-$3+1)/$2>0.3' > overlap.filter.paf

rm -f overlap.paf

echo end at `date`
