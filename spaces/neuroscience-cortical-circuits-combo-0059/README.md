# COMBO_0059 - Neuroscience Cortical Circuits

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
- `neuroscience-other-irregular-spiking-in-nmda-driven-prefrontal-cort-82784-model`: Neuroscience: IrregularSpikingInNmdaDrivenPrefrontalCort82784Model
- `neuroscience-other-kinetic-nmda-receptor-model-kampa-et-al-2004-50207-model`: Neuroscience: KineticNmdaReceptorModelKampaEtAl200450207Model
- `neuroscience-other-kinetic-properties-of-voltage-gated-na-channel-n-111967-model`: Neuroscience: KineticPropertiesOfVoltageGatedNaChannelN111967Model
- `neuroscience-other-kv1-channel-governs-cerebellar-output-to-thalamu-150024-model`: Neuroscience: Kv1ChannelGovernsCerebellarOutputToThalamu150024Model

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
- neuroscience-other-irregular-spiking-in-nmda-driven-prefrontal-cort-82784-model :: modeldb:82784 :: https://modeldb.science/82784
- neuroscience-other-kinetic-nmda-receptor-model-kampa-et-al-2004-50207-model :: modeldb:50207 :: https://modeldb.science/50207
- neuroscience-other-kinetic-properties-of-voltage-gated-na-channel-n-111967-model :: modeldb:111967 :: https://modeldb.science/111967
- neuroscience-other-kv1-channel-governs-cerebellar-output-to-thalamu-150024-model :: modeldb:150024 :: https://modeldb.science/150024

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
