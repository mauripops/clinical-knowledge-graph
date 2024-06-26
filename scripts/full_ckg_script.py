import sys
sys.path.append("")

from ckgb.adapter import CKGAdapter
from biocypher import BioCypher

# start biocypher
bc = BioCypher(
    biocypher_config_path="config/biocypher_config_full.yaml",
)

limit=100

# create CKG adapter
adapter = CKGAdapter(
    limit_import_count=limit, # for testing; remove or set to 0 for full import
    biocypher_driver=bc,
    # dirname=output_directory,
) 

# perform import
# TODO find a way to pass nodes and edges to the driver instead of the driver to
# the adapter
adapter.write_nodes()
adapter.write_edges()

# convenience and import stats
bc.write_import_call()

bc.log_duplicates()
bc.log_missing_input_labels()
if limit>1000:
    bc.summary()
#bc.summary()
