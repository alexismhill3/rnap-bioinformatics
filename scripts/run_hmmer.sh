#!/bin/bash

data_src=("Genbank" "RefSeq" "DDBJ" "EMBL" "PhagesDB" "GPD" "GVD" "MGV" "TemPhD" "CHVD" "IGVD" "IMG_VR" "GOV2" "STV")

# uncomment to test pipeline
#data_src=("RefSeq")

for Pref in "${data_src[@]}"; do
    hmmsearch --noali --cpu 50 -E 0.001 --tblout output/"$Pref"_hmmout.tbl.txt \
    -o output/"$Pref"_hmmout.txt hmm/phage-family-interpro-v4.hmm phagescope/"$Pref".fasta; wait
    echo "finished running hmmer on $Pref"
done
