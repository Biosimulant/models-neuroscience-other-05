# Space Plan - neuroscience-cortical-circuits-combo-0054

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-fast-spiking-cortical-interneuron-golomb-et-al-2-97747-model, neuroscience-other-ffv1mt-a-v1-mt-feedforward-architecture-for-opti-181035-model, neuroscience-other-firing-neocortical-layer-v-pyramidal-neuron-reet-168148-model

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
