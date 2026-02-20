# COMBO_0073 - Neuroscience Cortical Circuits

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
- `neuroscience-other-meg-of-somatosensory-neocortex-jones-et-al-2007-113732-model`: Neuroscience: MegOfSomatosensoryNeocortexJonesEtAl2007113732Model
- `neuroscience-other-mejiasetal2016-mejiasetal2016-model`: Neuroscience: Mejiasetal2016Mejiasetal2016Model
- `neuroscience-other-microcircuits-of-l5-thick-tufted-pyramidal-cells-156780-model`: Neuroscience: MicrocircuitsOfL5ThickTuftedPyramidalCells156780Model
- `neuroscience-other-microglial-cytokine-network-anderson-et-al-2015-170029-model`: Neuroscience: MicroglialCytokineNetworkAndersonEtAl2015170029Model

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
- neuroscience-other-meg-of-somatosensory-neocortex-jones-et-al-2007-113732-model :: modeldb:113732 :: https://modeldb.science/113732
- neuroscience-other-mejiasetal2016-mejiasetal2016-model :: opensourcebrain:MejiasEtAl2016 :: https://github.com/OpenSourceBrain/MejiasEtAl2016
- neuroscience-other-microcircuits-of-l5-thick-tufted-pyramidal-cells-156780-model :: modeldb:156780 :: https://modeldb.science/156780
- neuroscience-other-microglial-cytokine-network-anderson-et-al-2015-170029-model :: modeldb:170029 :: https://modeldb.science/170029

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
