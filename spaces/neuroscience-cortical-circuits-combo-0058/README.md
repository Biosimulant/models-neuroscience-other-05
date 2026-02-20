# COMBO_0058 - Neuroscience Cortical Circuits

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
- `neuroscience-other-inhibitory-control-by-an-integral-feedback-signa-62268-model`: Neuroscience: InhibitoryControlByAnIntegralFeedbackSigna62268Model
- `neuroscience-other-inhibitory-plasticity-balances-excitation-and-in-143751-model`: Neuroscience: InhibitoryPlasticityBalancesExcitationAndIn143751Model
- `neuroscience-other-input-fluctuations-effects-on-f-i-curves-arsiero-83590-model`: Neuroscience: InputFluctuationsEffectsOnFICurvesArsiero83590Model
- `neuroscience-other-intracortical-synaptic-potential-modulation-by-p-135787-model`: Neuroscience: IntracorticalSynapticPotentialModulationByP135787Model

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
- neuroscience-other-inhibitory-control-by-an-integral-feedback-signa-62268-model :: modeldb:62268 :: https://modeldb.science/62268
- neuroscience-other-inhibitory-plasticity-balances-excitation-and-in-143751-model :: modeldb:143751 :: https://modeldb.science/143751
- neuroscience-other-input-fluctuations-effects-on-f-i-curves-arsiero-83590-model :: modeldb:83590 :: https://modeldb.science/83590
- neuroscience-other-intracortical-synaptic-potential-modulation-by-p-135787-model :: modeldb:135787 :: https://modeldb.science/135787

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
