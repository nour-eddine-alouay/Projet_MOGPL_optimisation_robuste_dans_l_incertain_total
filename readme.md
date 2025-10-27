# 🧬 README — Commands Summary for PHYLIP TME (Exercises 2–5)

This README contains all commands and execution steps used across the PHYLIP exercises.  
It includes the sequence alignment, distance computation, tree reconstruction (NJ & UPGMA),  
and visualization steps for each exercise.

---

## ⚙️ General setup

Make sure **Clustal Omega** and **PHYLIP** are installed and accessible from your terminal or PowerShell.  
All PHYLIP programs (`protdist`, `neighbor`, etc.) must be run from inside the `phylip/exe` folder.

---

## 🧩 Exercise 2 — Building NJ & UPGMA trees (PAH protein)

### 1️⃣ Prepare and align sequences
```bash
clustalo -i PAH.fasta -o PAH.aln-phylip --outfmt=phylip
```

### 2️⃣ Compute distance matrix
```bash
copy-item PAH.aln-phylip infile
protdist
rename-item outfile PAH_protdist.txt
```

### 3️⃣ Build NJ tree
```bash
copy-item PAH_protdist.txt infile
neighbor
# When prompted about "outfile" existing → type R
# Confirm settings → Y
rename-item outfile PAH_NJ_log.txt
rename-item outtree PAH_NJ_tree.nwk
```

### 4️⃣ Build UPGMA tree
```bash
copy-item PAH_protdist.txt infile
neighbor
# Choose UPGMA (press N to toggle), then Y to confirm
rename-item outfile PAH_UPGMA_log.txt
rename-item outtree PAH_UPGMA_tree.nwk
```

### 5️⃣ Files produced
```
PAH_protdist.txt
PAH_NJ_tree.nwk
PAH_UPGMA_tree.nwk
PAH_NJ_log.txt
PAH_UPGMA_log.txt
```

---

## 🧬 Exercise 3 — CFTR protein in mammals

### 1️⃣ Alignment
```bash
clustalo -i CFTR_in_mammals.fasta -o CFTR.aln-phylip --outfmt=phylip
```

### 2️⃣ Distance matrix
```bash
cp CFTR.aln-phylip infile
protdist
mv outfile protdist_out.txt
```

### 3️⃣ Neighbor-Joining tree
```bash
cp protdist_out.txt infile
neighbor     # Y for NJ
mv outfile neighbor_NJ.txt
mv outtree NJ_tree.newick
```

### 4️⃣ UPGMA tree
```bash
cp protdist_out.txt infile
neighbor     # N for UPGMA
mv outfile neighbor_UPGMA.txt
mv outtree UPGMA_tree.newick
```

### 5️⃣ Output files
```
CFTR.aln-phylip
protdist_out.txt
NJ_tree.newick
UPGMA_tree.newick
neighbor_NJ.txt
neighbor_UPGMA.txt
```

---

## 🧬 Exercise 4 — p53 protein in mammals

### 1️⃣ Alignment
```bash
clustalo -i p53.fasta -o p53.aln-phylip --outfmt=phylip
```

### 2️⃣ Distance matrix
```bash
cp p53.aln-phylip infile
protdist
mv outfile protdist_out.txt
```

### 3️⃣ NJ tree
```bash
cp protdist_out.txt infile
neighbor     # Y for NJ
mv outfile neighbor_NJ.txt
mv outtree NJ_tree.newick
```

### 4️⃣ UPGMA tree
```bash
cp protdist_out.txt infile
neighbor     # N for UPGMA
mv outfile neighbor_UPGMA.txt
mv outtree UPGMA_tree.newick
```

### 5️⃣ Output files
```
p53.aln-phylip
protdist_out.txt
NJ_tree.newick
UPGMA_tree.newick
neighbor_NJ.txt
neighbor_UPGMA.txt
```

---

## 🦠 Exercise 5 — Spike (S) protein (Coronaviridae)

### 1️⃣ Alignment
```bash
clustalo -i S_protein.afa -o S_protein.aln-phylip --outfmt=phylip
```

### 2️⃣ Distance matrix
```bash
cp S_protein.aln-phylip infile
protdist
mv outfile protdist_out.txt
cp protdist_out.txt Ex5_distmatrix.txt
```

### 3️⃣ NJ tree
```bash
cp protdist_out.txt infile
neighbor     # Y for NJ
mv outfile neighbor_NJ.txt
mv outtree NJ_tree.newick
```

### 4️⃣ UPGMA tree
```bash
cp protdist_out.txt infile
neighbor     # N for UPGMA
mv outfile neighbor_UPGMA.txt
mv outtree UPGMA_tree.newick
```

### 5️⃣ Output files
```
S_protein.afa
S_protein.aln-phylip
protdist_out.txt
Ex5_distmatrix.txt
NJ_tree.newick
UPGMA_tree.newick
neighbor_NJ.txt
neighbor_UPGMA.txt
```

---

## 🌳 Tree visualization

You can visualize `.newick` files with:

* **iTOL:** [https://itol.embl.de/upload.cgi](https://itol.embl.de/upload.cgi)
* **FigTree:** `figtree NJ_tree.newick`

Export your tree as `.png` or `.pdf` and include it in your report.

---

## 🪴 Notes and good practices

* Always rename `outfile` and `outtree` after each run to avoid overwriting.
* When PHYLIP asks about existing `outfile`, **type `R`** (Replace).
* Use **Neighbor-Joining (NJ)** for realistic phylogenies, and **UPGMA** for comparison.
* Keep a clear directory structure for each exercise.

---

📘 **End of README**
