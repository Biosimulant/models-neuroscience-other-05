# COMBO_0062 - Neuroscience Cortical Circuits

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
- `neuroscience-other-large-scale-model-of-neocortical-slice-in-vitro-156072-model`: Neuroscience: LargeScaleModelOfNeocorticalSliceInVitro156072Model
- `neuroscience-other-larkumetal2009-larkumetal2009-model`: Neuroscience: Larkumetal2009Larkumetal2009Model
- `neuroscience-other-late-emergence-of-the-whisker-direction-selectiv-154348-model`: Neuroscience: LateEmergenceOfTheWhiskerDirectionSelectiv154348Model
- `neuroscience-other-layer-5-pyramidal-neuron-shai-et-al-2015-180373-model`: Neuroscience: Layer5PyramidalNeuronShaiEtAl2015180373Model

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
- neuroscience-other-large-scale-model-of-neocortical-slice-in-vitro-156072-model :: modeldb:156072 :: https://modeldb.science/156072
- neuroscience-other-larkumetal2009-larkumetal2009-model :: opensourcebrain:LarkumEtAl2009 :: https://github.com/OpenSourceBrain/LarkumEtAl2009
- neuroscience-other-late-emergence-of-the-whisker-direction-selectiv-154348-model :: modeldb:154348 :: https://modeldb.science/154348
- neuroscience-other-layer-5-pyramidal-neuron-shai-et-al-2015-180373-model :: modeldb:180373 :: https://modeldb.science/180373

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
