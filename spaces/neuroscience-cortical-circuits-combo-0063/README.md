# COMBO_0063 - Neuroscience Cortical Circuits

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
- `neuroscience-other-layer-v-pfc-pyramidal-neuron-used-to-study-persi-144089-model`: Neuroscience: LayerVPfcPyramidalNeuronUsedToStudyPersi144089Model
- `neuroscience-other-mainenetal-pyramidalcell-mainenetalpyramidalcell-model`: Neuroscience: MainenetalPyramidalcellMainenetalpyramidalcellModel
- `neuroscience-other-maki-marttunenetal2020-makimarttunenetal2020-model`: Neuroscience: MakiMarttunenetal2020Makimarttunenetal2020Model
- `neuroscience-other-markov-models-of-scn1a-nav1-1-applied-to-abnorma-87278-model`: Neuroscience: MarkovModelsOfScn1aNav11AppliedToAbnorma87278Model

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
- neuroscience-other-layer-v-pfc-pyramidal-neuron-used-to-study-persi-144089-model :: modeldb:144089 :: https://modeldb.science/144089
- neuroscience-other-mainenetal-pyramidalcell-mainenetalpyramidalcell-model :: opensourcebrain:MainenEtAl_PyramidalCell :: https://github.com/OpenSourceBrain/MainenEtAl_PyramidalCell
- neuroscience-other-maki-marttunenetal2020-makimarttunenetal2020-model :: opensourcebrain:Maki-MarttunenEtAl2020 :: https://github.com/OpenSourceBrain/Maki-MarttunenEtAl2020
- neuroscience-other-markov-models-of-scn1a-nav1-1-applied-to-abnorma-87278-model :: modeldb:87278 :: https://modeldb.science/87278

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
