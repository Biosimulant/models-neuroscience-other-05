# Space Plan - neuroscience-general-combo-0023

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-grid-cell-spatial-firing-models-zilli-2012-144006-model, neuroscience-other-grid-cells-from-place-cells-castro-and-aguiar-20-150846-model

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
