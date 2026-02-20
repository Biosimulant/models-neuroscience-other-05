# Space Plan - neuroscience-hippocampal-circuits-combo-0067

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-gamma-and-theta-rythms-in-biophysical-models-of-138421-model, neuroscience-other-grancellrothmanif-grancellrothmanif-model, neuroscience-other-hemond2008-ca3pyramidalcell-hemond2008ca3pyramidalcell-model, neuroscience-other-high-frequency-oscillations-in-a-hippocampal-com-135902-model

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
