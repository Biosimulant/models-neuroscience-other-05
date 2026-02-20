# Space Plan - neuroscience-general-combo-0035

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-inferior-olive-subthreshold-oscillations-torben-144502-model, neuroscience-other-information-transmission-in-cerebellar-granule-c-156733-model, neuroscience-other-input-strength-and-time-varying-oscillation-peak-154770-model

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
