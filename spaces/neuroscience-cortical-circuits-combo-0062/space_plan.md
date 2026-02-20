# Space Plan - neuroscience-cortical-circuits-combo-0062

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-large-scale-model-of-neocortical-slice-in-vitro-156072-model, neuroscience-other-larkumetal2009-larkumetal2009-model, neuroscience-other-late-emergence-of-the-whisker-direction-selectiv-154348-model, neuroscience-other-layer-5-pyramidal-neuron-shai-et-al-2015-180373-model

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
