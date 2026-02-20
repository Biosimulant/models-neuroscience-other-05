# Space Plan - neuroscience-general-combo-0016

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-generating-coherent-patterns-of-activity-from-ch-127967-model, neuroscience-other-generation-of-granule-cell-dendritic-morphology-167638-model

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
