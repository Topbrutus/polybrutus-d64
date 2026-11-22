#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d64.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==64
assert c['vertices']==m['norm_one_vertices']==69
assert c['pairs']==m['exact_labelled_squared_pairs']==2346
assert c['affine_rank']==c['centered_gram_rank']==64
assert c['eigenvalue_69_over_2_multiplicity']==m['model_eigenvalue_69_over_2_multiplicity']==58
assert c['eigenvalue_34_multiplicity']==m['model_eigenvalue_34_multiplicity']==4
assert c['parent_tag_commit']=='221bfb6b49fecc2dd589801df4a7a22d76a2642c'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24432380'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24432380','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty-four' in m['keywords']
assert 'fifty-eightfold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24432380' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not set(m['keywords']).intersection({'affine Euclidean dimension sixty-three','fifty-sevenfold ideal eigenvalue','affine Euclidean dimension sixty-five','fifty-ninefold ideal eigenvalue'})
note=(R/'publication/POLYBRUTUS_64D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24432380','10.5281/zenodo.24407952'))
print('D64_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D63_PARENT_AND_SEPARATE_D63_D7_REFERENCES_PASS')
