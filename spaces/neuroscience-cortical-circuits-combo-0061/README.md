# COMBO_0061 - Neuroscience Cortical Circuits

## Scientific Question
How do cortical circuit motifs transform and propagate activity?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-l5-pyr-cell-spiking-control-by-oscillatory-inhib-150538-model`: Neuroscience: L5PyrCellSpikingControlByOscillatoryInhib150538Model
- `neuroscience-other-l5b-pc-model-constrained-for-bac-firing-and-peri-139653-model`: Neuroscience: L5bPcModelConstrainedForBacFiringAndPeri139653Model
- `neuroscience-other-l5bpyrcellhayetal2011-l5bpyrcellhayetal2011-model`: Neuroscience: L5bpyrcellhayetal2011L5bpyrcellhayetal2011Model
- `neuroscience-other-lamprey-spinal-cpg-neuron-huss-et-al-2007-93319-model`: Neuroscience: LampreySpinalCpgNeuronHussEtAl200793319Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-other-l5-pyr-cell-spiking-control-by-oscillatory-inhib-150538-model :: modeldb:150538 :: https://modeldb.science/150538
- neuroscience-other-l5b-pc-model-constrained-for-bac-firing-and-peri-139653-model :: modeldb:139653 :: https://modeldb.science/139653
- neuroscience-other-l5bpyrcellhayetal2011-l5bpyrcellhayetal2011-model :: opensourcebrain:L5bPyrCellHayEtAl2011 :: https://github.com/OpenSourceBrain/L5bPyrCellHayEtAl2011
- neuroscience-other-lamprey-spinal-cpg-neuron-huss-et-al-2007-93319-model :: modeldb:93319 :: https://modeldb.science/93319

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
