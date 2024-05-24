# command for extracting genbank hits 
# alternative to esl-sfetch, which breaks on the Genbank DB
cat output/Genbank_hmmout.csv | awk -F "," 'NR > 1 {print $1}' | xargs -I% find phagescope/Genbank/ -name "%".fasta -exec cat {} \; > output/Genbank_hits.fasta