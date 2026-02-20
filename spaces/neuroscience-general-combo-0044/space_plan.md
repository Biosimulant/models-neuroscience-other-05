# Space Plan - neuroscience-general-combo-0044

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-m1networkmodel-m1networkmodel-model, neuroscience-other-mammalian-ventricular-cell-beeler-and-reuter-197-97863-model, neuroscience-other-mapping-function-onto-neuronal-morphology-stiefe-93398-model

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
