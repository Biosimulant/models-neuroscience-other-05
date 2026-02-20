# Space Plan - neuroscience-general-combo-0033

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-ih-levels-roles-in-bursting-and-regular-spiking-82364-model, neuroscience-other-impact-of-dendritic-size-and-topology-on-pyramid-114359-model, neuroscience-other-impact-of-fast-na-channel-inact-on-ap-threshold-153998-model

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
