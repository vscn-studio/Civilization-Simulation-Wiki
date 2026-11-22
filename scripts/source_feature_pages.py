"""Generate configuration meaning and validation rules without source inventories."""
from wiki_content import ROOT
from local_inputs import source_dir
from config_semantics import generate_config_semantics

generate_config_semantics(ROOT, source_dir(
    'SERAPH_SURVIVAL_SOURCE', 'Seraph Living Survival Simulation')/'src')
print('updated seraph-config-semantics.md')
