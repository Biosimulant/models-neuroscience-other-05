# COMBO_0042 - Neuroscience General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-leech-heart-he-motor-neuron-conductances-contrib-153355-model`: Neuroscience: LeechHeartHeMotorNeuronConductancesContrib153355Model
- `neuroscience-other-leech-s-cell-modulation-of-excitability-by-serot-102279-model`: Neuroscience: LeechSCellModulationOfExcitabilityBySerot102279Model
- `neuroscience-other-lillie-transition-onset-of-saltatory-conduction-169208-model`: Neuroscience: LillieTransitionOnsetOfSaltatoryConduction169208Model

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
- neuroscience-other-leech-heart-he-motor-neuron-conductances-contrib-153355-model :: modeldb:153355 :: https://modeldb.science/153355
- neuroscience-other-leech-s-cell-modulation-of-excitability-by-serot-102279-model :: modeldb:102279 :: https://modeldb.science/102279
- neuroscience-other-lillie-transition-onset-of-saltatory-conduction-169208-model :: modeldb:169208 :: https://modeldb.science/169208

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
