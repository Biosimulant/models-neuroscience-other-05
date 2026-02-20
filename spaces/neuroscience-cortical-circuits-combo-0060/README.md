# COMBO_0060 - Neuroscience Cortical Circuits

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
- `neuroscience-other-kv4-3-kv1-4-encoded-k-channel-in-heart-cells-and-62654-model`: Neuroscience: Kv43Kv14EncodedKChannelInHeartCellsAnd62654Model
- `neuroscience-other-kv4-3-kv1-4-encoded-k-channel-in-heart-cells-gre-62287-model`: Neuroscience: Kv43Kv14EncodedKChannelInHeartCellsGre62287Model
- `neuroscience-other-l23pyramidalcelltutorial-l23pyramidalcelltutorial-model`: Neuroscience: L23pyramidalcelltutorialL23pyramidalcelltutorialModel
- `neuroscience-other-l5-pfc-microcircuit-used-to-study-persistent-act-155057-model`: Neuroscience: L5PfcMicrocircuitUsedToStudyPersistentAct155057Model

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
- neuroscience-other-kv4-3-kv1-4-encoded-k-channel-in-heart-cells-and-62654-model :: modeldb:62654 :: https://modeldb.science/62654
- neuroscience-other-kv4-3-kv1-4-encoded-k-channel-in-heart-cells-gre-62287-model :: modeldb:62287 :: https://modeldb.science/62287
- neuroscience-other-l23pyramidalcelltutorial-l23pyramidalcelltutorial-model :: opensourcebrain:L23PyramidalCellTutorial :: https://github.com/OpenSourceBrain/L23PyramidalCellTutorial
- neuroscience-other-l5-pfc-microcircuit-used-to-study-persistent-act-155057-model :: modeldb:155057 :: https://modeldb.science/155057

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
