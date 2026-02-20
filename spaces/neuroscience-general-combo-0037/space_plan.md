# Space Plan - neuroscience-general-combo-0037

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-ion-channel-modeling-with-whole-cell-and-a-genet-97756-model, neuroscience-other-ion-concentration-dynamics-as-a-mechanism-for-ne-142630-model, neuroscience-other-ionic-basis-of-alternans-and-timothy-syndrome-fo-104623-model

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
