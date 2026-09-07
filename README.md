# LLM Response Quality Evaluation & Annotation Project

## Overview
A self-directed annotation exercise applying structured labeling guidelines to a sample of 12 prompt/response pairs spanning six domains (factual QA, coding, math, ambiguous prompts, sensitive/health content, creative writing, reasoning, instruction-following). Built to practice the annotation workflow used in AI training-data pipelines: guideline authoring, independent scoring, error flagging, and QA summary reporting.

## Method
1. Authored annotation guidelines (`annotation_guidelines.md`) defining three scoring dimensions (Helpfulness, Accuracy, Clarity, 1-5 scale) and three flag categories (AMBIGUOUS_PROMPT, FACTUAL_ERROR, NEEDS_ESCALATION).
2. Constructed 12 prompt/response pairs, deliberately including correct responses, subtly incorrect responses (wrong arithmetic, inverted logic, wrong fact), an ambiguous prompt, a health-sensitive prompt, and an instruction-following failure - to stress-test the guidelines against edge cases annotators commonly encounter.
3. Scored each pair independently against the guideline and recorded a rationale for any low score.
4. Produced summary statistics and a short QA note on where the guideline needed clarification mid-way through (see below).

## Results
- 12 items annotated; 6 flagged (5 FACTUAL_ERROR, 1 NEEDS_ESCALATION)
- Average scores: Helpfulness 4.25/5, Accuracy 3.50/5, Clarity 4.58/5
- Accuracy was the weakest dimension by design - most inserted errors were factual/arithmetic rather than structural, which matches common LLM failure modes in evaluation datasets

## QA Note (guideline refinement in practice)
While annotating item 10, a response that was initially assumed incorrect was re-verified against the prompt and found to be correct on recheck - this is logged in the code comments as a reminder to always re-derive ground truth rather than annotate from memory or first impression, and matches the guideline's "re-check every ~10 items" step.

## Files
- `annotation_guidelines.md` - scoring rubric and process
- `generate_dataset.py` - builds the annotated dataset
- `annotated_dataset.csv` - the 12 scored prompt/response pairs with flags and rationale
