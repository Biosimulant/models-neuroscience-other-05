# Space Plan - neuroscience-cortical-circuits-combo-0061

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-l5-pyr-cell-spiking-control-by-oscillatory-inhib-150538-model, neuroscience-other-l5b-pc-model-constrained-for-bac-firing-and-peri-139653-model, neuroscience-other-l5bpyrcellhayetal2011-l5bpyrcellhayetal2011-model, neuroscience-other-lamprey-spinal-cpg-neuron-huss-et-al-2007-93319-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
