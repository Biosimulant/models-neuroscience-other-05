# Space Plan - neuroscience-basal-ganglia-dopamine-combo-0071

## Scientific Scope
- Domain: neuroscience
- Theme: basal_ganglia_dopamine
- Base models: neuroscience-other-erg-current-in-repolarizing-plateau-potentials-i-100603-model, neuroscience-other-fs-striatal-interneuron-k-currents-solve-signal-79465-model, neuroscience-other-gap-junction-coupled-network-of-striatal-fast-sp-118389-model, neuroscience-other-globus-pallidus-multi-compartmental-model-neuron-114639-model

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
