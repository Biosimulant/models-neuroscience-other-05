# Space Plan - neuroscience-hippocampal-circuits-combo-0065

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-encoding-and-retrieval-in-a-model-of-the-hippoca-123815-model, neuroscience-other-epilepsy-may-be-caused-by-very-small-functional-124392-model, neuroscience-other-excitability-of-the-soma-in-central-nervous-syst-62266-model, neuroscience-other-fast-sodium-channel-gating-in-mossy-fiber-axons-128079-model

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
