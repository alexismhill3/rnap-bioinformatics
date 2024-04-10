import torch
import numpy as np
import csv
import esm
import sys

BP_FASTA_PATH = sys.argv[1]
BP_EMB_PATH = sys.arv[2]
EMB_LAYER = sys.arv[3]

with open('embeddings.csv', 'a') as fl:
    wr = csv.writer(fl)
    for header, _seq in esm.data.read_fasta(BP_FASTA_PATH):
        fn = f'{BP_EMB_PATH}/{header}.pt'
        embs = torch.load(fn)
        mean_repr = embs['mean_representations'][EMB_LAYER].numpy().tolist()
        ID, desc = (header.split("|")[0], header.split("|")[1])
        row = [ID, desc] + mean_repr
        wr.writerow(row)
