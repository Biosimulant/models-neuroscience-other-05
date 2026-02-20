# Space Plan - neuroscience-cortical-circuits-combo-0056

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-grancelllayer-grancelllayer-model, neuroscience-other-granularlayersolinasnieusdangelo2010-granularlayersolinasnieusdangelo2010-model, neuroscience-other-high-dimensional-dynamics-and-low-dimensional-re-82394-model, neuroscience-other-hmm-of-nav1-7-wt-and-f1449v-gurkiewicz-et-al-201-138082-model

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
