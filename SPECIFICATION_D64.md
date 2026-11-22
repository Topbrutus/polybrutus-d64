# Polybrutus D64 — exact 69-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d63@v0.1.0, actual peeled scientific Git commit \`221bfb6b49fecc2dd589801df4a7a22d76a2642c\`, DOI 10.5281/zenodo.24432380, original full source ZIP SHA256 \`536903fa7e706e8ba82247982c24d97926c20d2989134ee588c12769d41b4e36\`, original D63 certificate SHA256 \`0dd40ddf147ac0d5ee624d6649d107680a3811af3e83b467fb959a3bd4f2d5b0\`.

## Conservative perpendicular norm-one extension

Embed all 68 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_69. Every one of C(68,2)=2278 old labelled squared distances remains unchanged; all 68 new squared distances equal 2R². Total C(69,2)=2346 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **57** independent mutually orthogonal norm-one axes (rank 57). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+57=64**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/69, B=-(HDH)/2=HGH is PSD of rank **64**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 64 (65 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2315, 9:3, 10:10, 12:6, 13:2, 16:2; total 2346. Exact sum of squared pair distances R=1: **18815/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 68 old points with weight 1/2. The chosen ideal Laplacian is L64=[[L63+I68/2,-1_68/2],[-1_68ᵀ/2,68/2]]. Its characteristic recurrence is chi69(z)=z(z-69/2)chi68(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi69(z)=z(z-69/2)^58(z-34)^4*f6(z-31).
Exact rational nullities yield Laplacian eigenvalue **69/2 multiplicity 58**, and **34 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D63 DOI 10.5281/zenodo.24432380; historical D7 DOI 10.5281/zenodo.24407952.
