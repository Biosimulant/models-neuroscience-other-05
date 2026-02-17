### Original NEURON scripts for model

These files are the original model scripts for use with the [NEURON simulator](https://www.neuron.yale.edu/neuron/) as [submitted to ModelDB](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=124291).

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/OpenSourceBrain/Ferrante2009-DentateGyrusGranuleCell.git  # clones the git repository
    cd Ferrante2009-DentateGyrusGranuleCell/ModelDB/Granule_Fig_1B_right
    nrnivmodl  # compile .mod files
    nrngui nrngui FIG_1B_right.hoc  # runs a simulation
    specify the amplitude of the input current and press init&run

-------------------------------------------------------------------------------------------------------------------

Authors summary:

In this paper, the model shows that feed-forward inhibition (FFI) can change a steeply sigmoid I/O curve into a double-sigmoid typical of buffer systems. Specifically FIG_1B_left.hoc and FIG_1B_right.hoc respectively produce plots of firing response of the model MOPP cel (left) and granule cell (right) upon somatic current injections.

> Questions on how to use this model should be directed to mferran1@gmu.edu
