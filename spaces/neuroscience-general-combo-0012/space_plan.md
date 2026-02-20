# Space Plan - neuroscience-general-combo-0012

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-fractional-leaky-integrate-and-fire-model-teka-e-155856-model, neuroscience-other-frog-second-order-vestibular-neuron-models-rosse-139654-model

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
