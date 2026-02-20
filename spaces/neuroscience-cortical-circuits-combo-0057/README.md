# COMBO_0057 - Neuroscience Cortical Circuits

## Scientific Question
How do cortical circuit motifs transform and propagate activity?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-human-sleep-wake-cycle-rempe-et-al-2010-147748-model`: Neuroscience: HumanSleepWakeCycleRempeEtAl2010147748Model
- `neuroscience-other-huntington-s-disease-model-gambazzi-et-al-2010-125748-model`: Neuroscience: HuntingtonSDiseaseModelGambazziEtAl2010125748Model
- `neuroscience-other-information-processing-in-lamina-specific-cortic-82385-model`: Neuroscience: InformationProcessingInLaminaSpecificCortic82385Model
- `neuroscience-other-inhibitory-cells-enable-sparse-coding-in-v1-mode-182373-model`: Neuroscience: InhibitoryCellsEnableSparseCodingInV1Mode182373Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-other-human-sleep-wake-cycle-rempe-et-al-2010-147748-model :: modeldb:147748 :: https://modeldb.science/147748
- neuroscience-other-huntington-s-disease-model-gambazzi-et-al-2010-125748-model :: modeldb:125748 :: https://modeldb.science/125748
- neuroscience-other-information-processing-in-lamina-specific-cortic-82385-model :: modeldb:82385 :: https://modeldb.science/82385
- neuroscience-other-inhibitory-cells-enable-sparse-coding-in-v1-mode-182373-model :: modeldb:182373 :: https://modeldb.science/182373

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
