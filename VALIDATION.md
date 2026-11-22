# Polybrutus D64 — proof-first validation and controlled publication

1. Direct scientific parent D63 frozen v0.1.0 peeled Git commit 221bfb6b49fecc2dd589801df4a7a22d76a2642c, DOI 10.5281/zenodo.24432380, entire original source ZIP SHA256 536903fa7e706e8ba82247982c24d97926c20d2989134ee588c12769d41b4e36, certificate SHA256 0dd40ddf147ac0d5ee624d6649d107680a3811af3e83b467fb959a3bd4f2d5b0. Both exact programs validate original ZIP SHA/CRC, original certificate bytes and inherited labels.
2. Exhaust all 69 norm-one points and 2346 labelled exact squared distances; 2278 unchanged old D63 pairs and 68 new squared distances 2R²; Euclidean Gram and centered Gram PSD rank 64.
3. Two independent implementations (SymPy exact Gram vs fractions.Fraction separate pair rules), four adversarial negative controls, exact deterministic certificate. Chosen dimensionless ideal graph eigenvalue 69/2 mult 58 and 34 mult 4.
4. Scientific GitHub initial main CI must pass, then freeze source tag v0.1.0 and require tag CI green; after public Zenodo DOI document on main and require third green CI.
5. Public Zenodo originals: full frozen Git scientific source ZIP, two-page mathematical PDF and exact deterministic certificate JSON; all 3 filenames, sizes and MD5 from public API match SHA256-verified originals. Nine current D64 sixty-four/fifty-eightfold keywords, structured isDerivedFrom direct D63 DOI, separate D63/D7 textual bibliography.
6. Preserve entire historic original source ZIP nesting unchanged, disclose D47/D46 historical parent text SHA mistake, never claim physical spacetime, measured hertz or new universal theorem.

    python -m pip install sympy==1.14.0
    python src/verify_d64.py
    python tests/independent_d64.py
    python src/check_zenodo_metadata.py
