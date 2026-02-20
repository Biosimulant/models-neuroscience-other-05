# COMBO_0067 - Neuroscience Hippocampal Circuits

## Scientific Question
How do recurrent hippocampal motifs shape network dynamics over time?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-gamma-and-theta-rythms-in-biophysical-models-of-138421-model`: Neuroscience: GammaAndThetaRythmsInBiophysicalModelsOf138421Model
- `neuroscience-other-grancellrothmanif-grancellrothmanif-model`: Neuroscience: GrancellrothmanifGrancellrothmanifModel
- `neuroscience-other-hemond2008-ca3pyramidalcell-hemond2008ca3pyramidalcell-model`: Neuroscience: Hemond2008Ca3pyramidalcellHemond2008ca3pyramidalcellModel
- `neuroscience-other-high-frequency-oscillations-in-a-hippocampal-com-135902-model`: Neuroscience: HighFrequencyOscillationsInAHippocampalCom135902Model

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
- neuroscience-other-gamma-and-theta-rythms-in-biophysical-models-of-138421-model :: modeldb:138421 :: https://modeldb.science/138421
- neuroscience-other-grancellrothmanif-grancellrothmanif-model :: opensourcebrain:GranCellRothmanIf :: https://github.com/OpenSourceBrain/GranCellRothmanIf
- neuroscience-other-hemond2008-ca3pyramidalcell-hemond2008ca3pyramidalcell-model :: opensourcebrain:Hemond2008-CA3PyramidalCell :: https://github.com/OpenSourceBrain/Hemond2008-CA3PyramidalCell
- neuroscience-other-high-frequency-oscillations-in-a-hippocampal-com-135902-model :: modeldb:135902 :: https://modeldb.science/135902

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
