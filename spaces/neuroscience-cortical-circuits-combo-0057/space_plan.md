# Space Plan - neuroscience-cortical-circuits-combo-0057

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-human-sleep-wake-cycle-rempe-et-al-2010-147748-model, neuroscience-other-huntington-s-disease-model-gambazzi-et-al-2010-125748-model, neuroscience-other-information-processing-in-lamina-specific-cortic-82385-model, neuroscience-other-inhibitory-cells-enable-sparse-coding-in-v1-mode-182373-model

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
