# Space Plan - neuroscience-cortical-circuits-combo-0073

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-meg-of-somatosensory-neocortex-jones-et-al-2007-113732-model, neuroscience-other-mejiasetal2016-mejiasetal2016-model, neuroscience-other-microcircuits-of-l5-thick-tufted-pyramidal-cells-156780-model, neuroscience-other-microglial-cytokine-network-anderson-et-al-2015-170029-model

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
