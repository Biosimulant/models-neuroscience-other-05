from pyneuroml.neuron import export_to_neuroml2
# from pyneuroml.neuron.nrn_export_utils import clear_neuron

export_to_neuroml2("../NEURON/test_granulecell.hoc", 
                   "granule.cell.nml", 
                   includeBiophysicalProperties=True,
                   known_rev_potentials={'ichan2':0})

