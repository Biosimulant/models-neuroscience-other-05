# COMBO_0075 - Neuroscience Basal Ganglia Dopamine

## Scientific Question
How do basal ganglia dopamine mechanisms compare across these models?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-investigation-of-different-targets-in-deep-brain-122369-model`: Neuroscience: InvestigationOfDifferentTargetsInDeepBrain122369Model
- `neuroscience-other-linking-stdp-and-dopamine-action-to-solve-the-di-84167-model`: Neuroscience: LinkingStdpAndDopamineActionToSolveTheDi84167Model
- `neuroscience-other-low-dose-of-dopamine-may-stimulate-prolactin-sec-91898-model`: Neuroscience: LowDoseOfDopamineMayStimulateProlactinSec91898Model
- `neuroscience-other-model-of-darpp-32-phosphorylation-in-striatal-me-97743-model`: Neuroscience: ModelOfDarpp32PhosphorylationInStriatalMe97743Model

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
- neuroscience-other-investigation-of-different-targets-in-deep-brain-122369-model :: modeldb:122369 :: https://modeldb.science/122369
- neuroscience-other-linking-stdp-and-dopamine-action-to-solve-the-di-84167-model :: modeldb:84167 :: https://modeldb.science/84167
- neuroscience-other-low-dose-of-dopamine-may-stimulate-prolactin-sec-91898-model :: modeldb:91898 :: https://modeldb.science/91898
- neuroscience-other-model-of-darpp-32-phosphorylation-in-striatal-me-97743-model :: modeldb:97743 :: https://modeldb.science/97743

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
