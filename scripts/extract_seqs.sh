#!/bin/bash

#data_src=("Genbank" "RefSeq" "DDBJ" "EMBL" "PhagesDB" "GPD" "GVD" "MGV" "TemPhD" "CHVD" "IGVD" "IMG_VR" "GOV2" "STV")

data_src=("RefSeq" "DDBJ" "EMBL" "PhagesDB" "GPD" "GVD" "MGV" "TemPhD" "CHVD" "IGVD" "IMG_VR" "GOV2" "STV")


# uncomment to test pipeline
#data_src=("RefSeq")

# create index file for esl-sfetch program
cd phagescope
for Pref in "${data_src[@]}"; do
    echo "skipping $Pref index creation"
    #esl-sfetch --index "$Pref".fasta
done
cd ..

# convert hmmsearch tabular output to csv
for Pref in "${data_src[@]}"; do
    python3 scripts/parse_hmmsearch.py output/"$Pref"_hmmout.tbl.txt output/"$Pref"_hmmout.csv
done

# run esl-sfetch to extract sequences for all hits
for Pref in "${data_src[@]}"; do
    cat output/"$Pref"_hmmout.csv | awk -F "," 'NR > 1 {print $1}' | esl-sfetch -f phagescope/"$Pref".fasta - > output/"$Pref"_hits.fasta
done

# convert fasta sequences to csv (seqID, sequence)
for Pref in "${data_src[@]}"; do
    python3 scripts/sequences_to_csv.py output/"$Pref"_hits.fasta output/"$Pref"_hits.csv
done