This archive contains Q-Chem output files for frequency calculations 
at optimized reactant, product, and transition state structures for 
most schemes in the main text and supporting information.

Folders are numbered according to the Supporting Figure number.

with a few exceptions:
- A transition state connecting reactant and product could not be
  found for Supporting Figure 8 (first path of Scheme 2c).
- Supporting Figure 20 contains more detailed calculations including an
  optimization of a minimum energy crossing point (see 20/About.txt).
- Supporting Figures 26-30 only have gradient calculations at the
  optimized reactant and product structures, because free energy
  corrections to the reaction energy and activation energy were not
  calculated.

The folders also contain .xyz files extracted from the Q-Chem output files.

The script getFreeEnergyDiff.py will parse two Q-Chem frequency output files
to calculate energy differences and Gibbs free energy differences.

The script DE_aE_DG_aG.sh will call getFreeEnergyDiff.py and print out
energetic data consistent with tables in the manuscript.
