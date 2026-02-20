# Space Plan - neuroscience-general-combo-0043

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-lobster-stg-pyloric-network-model-with-calcium-s-144387-model, neuroscience-other-long-term-adaptation-with-power-law-dynamics-zil-125855-model, neuroscience-other-loss-of-phase-locking-in-non-weakly-coupled-inhi-118799-model

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
