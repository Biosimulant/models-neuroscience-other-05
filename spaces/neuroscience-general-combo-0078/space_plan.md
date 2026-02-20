# Space Plan - neuroscience-general-combo-0078

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-elementary-mechanisms-producing-facilitation-of-102871-model, neuroscience-other-ell-pyramidal-neuron-simmonds-and-chacron-2014-168590-model, neuroscience-other-encoding-and-discrimination-of-vowel-like-sounds-126371-model, neuroscience-other-endothelin-action-on-pituitary-latotrophs-bertra-91899-model

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
