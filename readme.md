# 🧬 README — PHYLIP TME (Exercises 2–5)

This document summarizes **all steps and commands** used in exercises 2 to 5 of the PHYLIP TME.  
It covers phylogenetic tree construction (NJ and UPGMA) from aligned protein sequences.

---

## ⚙️ General Setup

- **PHYLIP** programs (`protdist`, `neighbor`, etc.) were executed inside the `phylip/exe` directory.  
- Multiple sequence alignments were performed **online** using the EBI Clustal Omega tool:  
  🔗 https://www.ebi.ac.uk/jdispatcher/msa/clustalo?outfmt=phylip  
- Tree visualization and analysis were done using **iTOL**:  
  🌿 https://itol.embl.de/upload.cgi  
- ⚠️ Each exercise is stored in a **separate folder** (`Ex2`, `Ex3`, `Ex4`, `Ex5`).  
  Therefore, even if some files share the same names (e.g., `outfile`, `outtree`, or `NJ_tree.nwk`),  
  **this causes no conflict** because they are kept in different directories.

---

## 🧩 Exercise 2 — PAH Protein

### Steps
1. **Alignment:** performed online via EBI, exported in **PHYLIP** format (`PAH.aln-phylip`).  
2. **Distance matrix calculation:**
   ```bash
   copy-item PAH.aln-phylip infile
   protdist
   rename-item outfile PAH_protdist.txt
   ```
3. **Neighbor-Joining tree:**
   ```bash
   copy-item PAH_protdist.txt infile
   neighbor
   rename-item outfile PAH_NJ_log.txt
   rename-item outtree PAH_NJ_tree.nwk
   ```
4. **UPGMA tree:**
   ```bash
   copy-item PAH_protdist.txt infile
   neighbor
   # Select UPGMA (press N), then Y to confirm
   rename-item outfile PAH_UPGMA_log.txt
   rename-item outtree PAH_UPGMA_tree.nwk
   ```
5. **Visualization:** `.nwk` trees uploaded to [iTOL](https://itol.embl.de/upload.cgi).

---

## 🧬 Exercise 3 — CFTR Protein (Mammals)

### Steps
1. **Alignment:** done online (EBI), exported as `CFTR.aln-phylip`.  
2. **Distance matrix:**
   ```bash
   cp CFTR.aln-phylip infile
   protdist
   mv outfile CFTR_protdist.txt
   ```
3. **Neighbor-Joining tree:**
   ```bash
   cp CFTR_protdist.txt infile
   neighbor     # Y for NJ
   mv outfile CFTR_NJ_log.txt
   mv outtree CFTR_NJ_tree.nwk
   ```
4. **UPGMA tree:**
   ```bash
   cp CFTR_protdist.txt infile
   neighbor     # N for UPGMA
   mv outfile CFTR_UPGMA_log.txt
   mv outtree CFTR_UPGMA_tree.nwk
   ```
5. **Visualization on iTOL.**

---

## 🧬 Exercise 4 — p53 Protein (Mammals)

### Steps
1. **Alignment:** done online (EBI), exported as `p53.aln-phylip`.  
2. **Distance matrix:**
   ```bash
   cp p53.aln-phylip infile
   protdist
   mv outfile p53_protdist.txt
   ```
3. **Neighbor-Joining tree:**
   ```bash
   cp p53_protdist.txt infile
   neighbor
   mv outfile p53_NJ_log.txt
   mv outtree p53_NJ_tree.nwk
   ```
4. **UPGMA tree:**
   ```bash
   cp p53_protdist.txt infile
   neighbor
   mv outfile p53_UPGMA_log.txt
   mv outtree p53_UPGMA_tree.nwk
   ```
5. **Visualization on iTOL.**

---

## 🦠 Exercise 5 — Spike (S) Protein (Coronaviridae)

### Steps
1. **Alignment:** done online (EBI), exported as `S_protein.aln-phylip`.  
2. **Distance matrix:**
   ```bash
   cp S_protein.aln-phylip infile
   protdist
   mv outfile S_protein_protdist.txt
   cp S_protein_protdist.txt Ex5_distmatrix.txt
   ```
3. **Neighbor-Joining tree:**
   ```bash
   cp S_protein_protdist.txt infile
   neighbor
   mv outfile S_protein_NJ_log.txt
   mv outtree S_protein_NJ_tree.nwk
   ```
4. **UPGMA tree:**
   ```bash
   cp S_protein_protdist.txt infile
   neighbor
   mv outfile S_protein_UPGMA_log.txt
   mv outtree S_protein_UPGMA_tree.nwk
   ```
5. **Visualization:** uploaded and viewed on iTOL.

---

## 🌳 Tree Visualization and Export

All `.nwk` files were uploaded to **iTOL** for visualization and export (as `.png` or `.pdf`).  
Direct link: [https://itol.embl.de/upload.cgi](https://itol.embl.de/upload.cgi)

---

## 💡 Notes and Best Practices

- Each exercise has its **own folder** (`Ex2`, `Ex3`, `Ex4`, `Ex5`), preventing filename conflicts.  
- Rename `outfile` and `outtree` after each PHYLIP run if needed.  
- Use **Neighbor-Joining (NJ)** for main phylogenetic trees and **UPGMA** for comparison.  
- Keep a clean, organized folder structure for reproducibility.

---

📘 **End of README**
