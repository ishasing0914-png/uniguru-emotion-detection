# Emotion-Aware Deterministic Chatbot

## Overview
This project implements a deterministic chatbot with emotion-aware behavior.
The system is rule-based and does not use machine learning or training data.

---

## System Architecture

### 1. Emotion Detection Layer
- Implemented using keyword and structure-based rules
- Deterministic: same input always produces same emotion
- Supported emotions:
  - distressed
  - aggressive
  - frustrated
  - curious
  - neutral

---

### 2. Chatbot Control Layer
- Emotion is detected BEFORE response generation
- Emotion influences:
  - response tone
  - refusal behavior
  - response length
- Emotion does NOT change factual correctness

---

## Emotion Safety Rules
- Distressed: calm, minimal, safe responses
- Aggressive: firm refusal if unsafe
- Frustrated: neutral clarification only
- Curious: educational tone
- Neutral: standard behavior

---

## Testing & Validation
- Emotion rules validated using 10 emotion-specific test cases
- Consistency and stress testing performed with repeated inputs
- Mixed emotional and factual queries tested
- Edge cases verified

---

## Key Properties
- Deterministic behavior
- Emotionally safe
- Refusal-first design
- Stable under stress
