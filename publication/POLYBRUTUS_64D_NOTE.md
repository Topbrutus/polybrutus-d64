# Polybrutus 64D: Exact 69-point Euclidean metric and a fifty-eightfold ideal graph mode

**Gabriel St-Pierre** - Independent researcher
**21 November 2026**
**Exact mathematical preprint / reproducible synthetic case study**
**AI disclosure:** OpenAI ChatGPT (Astra) materially assisted two independently implemented exact rational verifiers, mathematical manuscript and controlled publication. AI is not the human scientific author.

## Abstract

We construct one exact labelled synthetic Euclidean squared-distance metric on 69 norm-one points through a conservative orthogonal unit-vector extension of the original immutable Polybrutus D63 [1]. All 2278 predecessor labelled squared distances remain unchanged; 68 new squared distances each equal 2R², producing 2346 unordered labelled pairs. The centered exact rational Euclidean Gram is PSD with rank 64, proving minimum affine Euclidean realization dimension 64 for this specified metric. For a separately freely stipulated ideal equal-scalar-mass weighted complete graph with w_ij=1/d_ij², rational Laplacian eigenspace ranks yield eigenvalue 69/2 multiplicity 58 and 34 multiplicity 4. Two independently implemented rational programs verify all 2346 pair labels, all 2278 authentic inherited parent labels, centered Gram rank, ideal graph nullities, and frozen full parent scientific source. No physical discovery or empirical measurement is claimed.

## 1. Immutable immediate parent and exact distance conservation

The sole direct scientific predecessor is St-Pierre, Polybrutus D63 [1], DOI 10.5281/zenodo.24432380, scientific frozen Git tag Topbrutus/polybrutus-d63@v0.1.0 at real peeled commit 221bfb6b49fecc2dd589801df4a7a22d76a2642c. Its **entire original Git scientific source ZIP** is preserved byte-identically at prior/d63/frozen_scientific_tag_v0.1.0.zip, size 4173836 bytes with 32 entries and ZIP CRC PASS, SHA256 536903fa7e706e8ba82247982c24d97926c20d2989134ee588c12769d41b4e36. All earlier original scientific source archives remain nested unchanged. The original D63 deterministic certificate is copied byte-identically at prior/d63/results/certificate_d63.json, SHA256 0dd40ddf147ac0d5ee624d6649d107680a3811af3e83b467fb959a3bd4f2d5b0. Both independent checkers authenticate source ZIP SHA/CRC, certificate bytes and all 2278 old labelled pairs.

Let p_i (i=1,...,68) be parent norm-one vectors and embed them by q_i=(p_i,0) into larger Euclidean coordinates. Append new perpendicular norm-one q_69. Then each old labelled squared distance remains unchanged, ||q_i-q_j||²=||p_i-p_j||². All 68 new squared distances satisfy ||q_69-q_i||²=2R². Thus C(69,2)=2346=2278+68 exact labelled unordered pairs. This is a constructed synthetic metric, not evidence for new physical spacetime dimensions.

## 2. Rational Gram PSD, exact affine rank and labelled histogram

Construct Gram G over rationals as an orthogonal sum of the seven canonical norm-one point Gram (rank 3), a centered regular five-point unit simplex with mutual inner products -1/4 (rank 4), and 57 independent perpendicular norm-one axes (rank 57). Hence G=XXᵀ is PSD with unit diagonal and rank 3+4+57=64. Define D_ii=0, D_ij=2-2G_ij and H=I-11ᵀ/69. The centered Euclidean Gram B=-(HDH)/2=HGH is PSD of exact rank 64. The inherited canonical antipodal pair puts the origin in the affine hull; the minimum affine Euclidean realization dimension for this metric is therefore 64, using 65 coordinate storage.

At R=1, exhaustive normalized histogram k=4d²/R² is 4:6, 7:2, 8:2315, 9:3, 10:10, 12:6, 13:2, 16:2, totaling 2346 unordered labelled pairs. Their exact sum of squared distances is 18815/4. Both programs verify all 2278 parent pair values by their exact original labels; histogram equality alone would not be an adequate conservation proof.

## 3. Separately specified ideal graph and rational spectral eigenspaces

We stipulate unit scalar masses and symmetric positive complete-graph edge weights w_ij=1/d_ij². The new perpendicular norm-one vertex joins all 68 old vertices with edge weight 1/2. The ideal Laplacian block is L64=[[L63+I68/2,-1_68/2],[-1_68ᵀ/2,68/2]]. Its characteristic polynomial satisfies chi69(z)=z(z-69/2)chi68(z-1/2)/(z-1/2). With the inherited seven-point core factor f6(z)=chiP7(z)/z, the chosen-model expression is chi69(z)=z(z-69/2)^58(z-34)^4*f6(z-31).

Independent exact rational rank-nullity for this Laplacian establishes eigenvalue 69/2 multiplicity 58 and 34 multiplicity 4. These are mathematically dimensionless eigenmodes of a freely chosen ideal graph, not measured acoustic or electromagnetic hertz, particles, or physical extra dimensions.

## 4. Two independent implementations and adversarial negative controls

Primary src/verify_d64.py constructs exact Gram G with SymPy, exhausts all 2346 labelled squared distances, independently authenticates parent complete ZIP SHA256/CRC and byte-identical original certificate, compares all 2278 inherited D63 labels, and computes centered Gram and ideal graph eigenspace ranks. Independent tests/independent_d64.py uses separate Python fractions.Fraction distance rules without importing the first program's Gram builder, and independently recomputes every pair label, centered rank and model eigenvalues. Both output the identical deterministic JSON results/certificate_d64.json with matching SHA256.

Four adversarial primary negative controls detect a corrupted new squared distance, duplicate final point, nonperpendicular tilted but norm-one added point, and histogram-preserving pair relabelling. Independent tests separately reject corrupted labels and histogram-preserving relabelled metrics.

The original D47 certificate carries an inaccurate textual D46 grandparent Git commit, disclosed since D48; historical source archives remain unmodified and the actual direct D63 scientific frozen tag is authenticated separately.

## 5. Reproducibility, DOI relationship and scientific boundaries

Python 3.12 and sympy==1.14.0 reproduce the exact calculations. Orthogonal norm-one vector extension and complete graph joins are standard mathematical constructions. This preprint proves properties of this constructed synthetic metric and the separately selected ideal graph, not a novel universal law, independently human-peer-reviewed experimental result, physical particle, measured hertz or extra physical spacetime dimension.

Zenodo metadata must contain nine current D64 keywords including sixty-four and fifty-eightfold, structured isDerivedFrom to immediate direct D63 DOI 10.5281/zenodo.24432380, and separate bibliographic references to D63 [1] and historical D7 [2]. All three public scientific tag ZIP, PDF and certificate JSON originals must match filenames, exact sizes and public MD5 against source SHA256.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 63D: Exact 68-Point Euclidean Metric and Fifty-Sevenfold Ideal Graph Mode. Zenodo DOI 10.5281/zenodo.24432380. https://doi.org/10.5281/zenodo.24432380

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo DOI 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Full original Polybrutus D63 frozen scientific source Git tag v0.1.0, https://github.com/Topbrutus/polybrutus-d63/tree/v0.1.0, peeled commit 221bfb6b49fecc2dd589801df4a7a22d76a2642c, original source ZIP preserved unchanged.
