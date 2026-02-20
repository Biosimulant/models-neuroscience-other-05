# Space Plan - neuroscience-cortical-circuits-combo-0063

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-layer-v-pfc-pyramidal-neuron-used-to-study-persi-144089-model, neuroscience-other-mainenetal-pyramidalcell-mainenetalpyramidalcell-model, neuroscience-other-maki-marttunenetal2020-makimarttunenetal2020-model, neuroscience-other-markov-models-of-scn1a-nav1-1-applied-to-abnorma-87278-model

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
