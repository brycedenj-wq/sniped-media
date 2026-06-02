---
name: signal-noise-forecasting-bayesian
description: |
  Separates signal from noise in data, avoids overfitting, and improves forecast accuracy through Bayesian belief updating and out-of-sample calibration.
  Use when:
  - building prediction or forecasting models
  - a model works on historical data but fails on new data (overfitting)
  - needing to distinguish real patterns from random noise
  - calibrating predictions (events at 70% should happen 70% of the time)
  - updating beliefs incrementally as new evidence arrives
  - someone claims a pattern in data and you need to verify it's signal, not noise
  Keywords: signal vs noise, Bayesian, forecasting, overfitting, calibration, prediction model, out-of-sample, belief updating, Nate Silver, forecast accuracy
---

# Signal vs. Noise Forecasting & Bayesian Calibration

**Skill ID:** 20.1  
**Category:** Signal Detection & Calibration  
**Source Document(s):** Prediction_Forecasting_Systems_FRAMEWORKS.docx, SUPERFORECASTING_FRAMEWORKS.docx

## Purpose

Build forecasting models that separate signal from noise, avoid overfitting, and improve through Bayesian belief updating, complementing the Superforecasting workflow with technical calibration methods.

## When to Use

When you need a calibrated probability estimate for a business-critical question.

## Instructions

Follow this workflow precisely. Each step is grounded in the source document(s) listed above. Do not skip steps. Do not invent frameworks, models, or terminology not present in the source material. Execute each step in order, using the exact logic and decision criteria documented.

## Workflow

1. Classify the prediction domain: Is this an environment where prediction is possible (regular patterns, feedback available) or dominated by irreducible randomness?
2. Establish a prior: What is your best estimate of the probability before seeing new evidence? Use base rates from the outside view.
3. Evaluate new evidence for diagnosticity: Does this evidence actually help distinguish between outcomes, or is it noise? More data does not equal more signal.
4. Update beliefs proportionally: Adjust your prior based on the strength and relevance of the evidence. Small evidence = small update. Diagnostic evidence = larger update.
5. Check for overfitting: Is your model chasing random fluctuations? Test predictions against data the model has never seen (out-of-sample testing). A model that explains everything in hindsight but predicts nothing in advance is overfitted.
6. Aggregate multiple perspectives: Combine diverse information sources. Aggregate forecasts are typically 15-20% more accurate than individual ones.
7. Calibrate over time: Track your predictions with scores (Brier scores or equivalent). Plot calibration curves. Events you say have 70% chance should happen 70% of the time.
8. Run continuous feedback loops: Without clear, prompt, and unambiguous feedback, practice does not produce improvement. Confidence grows faster than accuracy when feedback is absent.

## Output Format

Produce all of the following deliverables:

- A Bayesian reasoning chain (prior > evidence evaluation > posterior)
- An overfitting check (in-sample vs. out-of-sample performance)
- A calibration log tracking predicted probabilities vs. actual outcomes
- Identified signal-to-noise ratio for the prediction domain

## Example Use

User provides context about their specific situation. The skill guides them through each workflow step sequentially, producing all deliverables listed in the Output Format section. Each step builds on the previous one, and no step should be skipped.
