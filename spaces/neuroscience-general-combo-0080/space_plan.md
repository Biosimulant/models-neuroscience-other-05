# Space Plan - neuroscience-general-combo-0080

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-encoding-and-discrimination-of-vowel-like-sounds-126371-model, neuroscience-other-endothelin-action-on-pituitary-latotrophs-bertra-91899-model, neuroscience-other-evaluation-of-stochastic-diff-eq-approximation-o-118195-model, neuroscience-other-event-related-simulation-of-neural-processing-in-140964-model

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
