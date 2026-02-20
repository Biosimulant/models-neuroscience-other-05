# Space Plan - neuroscience-cortical-circuits-combo-0053

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-extraction-and-classification-of-three-cortical-143148-model, neuroscience-other-farinellaetal-nmdaspikes-farinellaetalnmdaspikes-model, neuroscience-other-fast-population-coding-huys-et-al-2007-93394-model

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
