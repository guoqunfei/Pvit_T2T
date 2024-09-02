#!/bin/bash

JUICER_TOOLS_JAR="/path/to/your/juicer_tools_1.22.01.jar"

mkdir trans_contact
cd trans_contact

cat ../yahs.out_scaffolds_final.agp |awk '{print $1}' | while read p;do cat ../yahs.out_scaffolds_final.agp |awk '{print $1}' | while read s;do java -Xmx800G -jar ${JUICER_TOOLS_JAR} dump observed NONE ../out_JBAT.hic ${p} ${s} BP 100000 ${p}-${s}.cis-contact.txt;done;done

cat ../yahs.out_scaffolds_final.agp |awk '{print $1"\t"$3}' | while read a b;do ls ${a}-* | grep -v "${a}-${a}\." | while read p;do cat ${p};done | awk '{sum += $3};END{print sum}' | while read s;do echo -ne "${a}\t${b}\t${s}\n";done;done > Trans-contacts.summary.txt
