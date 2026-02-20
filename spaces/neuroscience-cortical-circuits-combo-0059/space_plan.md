# Space Plan - neuroscience-cortical-circuits-combo-0059

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-irregular-spiking-in-nmda-driven-prefrontal-cort-82784-model, neuroscience-other-kinetic-nmda-receptor-model-kampa-et-al-2004-50207-model, neuroscience-other-kinetic-properties-of-voltage-gated-na-channel-n-111967-model, neuroscience-other-kv1-channel-governs-cerebellar-output-to-thalamu-150024-model

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
