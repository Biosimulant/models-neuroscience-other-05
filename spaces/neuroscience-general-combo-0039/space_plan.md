# Space Plan - neuroscience-general-combo-0039

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-jitcon-just-in-time-connectivity-for-large-spiki-106891-model, neuroscience-other-joglekaretal18-joglekaretal18-model, neuroscience-other-kinetics-of-the-p2x7-receptor-as-expressed-in-xe-95990-model

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
