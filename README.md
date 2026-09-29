# genpark-ambient-voice-thought-stream-capture-skill

> Ambient Voice & Thought Stream Capture. 100% Python Standard Library.

Distilled from **Catch**, transforming unstructured stream-of-consciousness voice notes and texting scratchpads into categorized actionable tasks and reflective notes.

## Architecture

```mermaid
flowchart LR
    Input["Raw Voice / Text Stream ('Call accountant before Friday')"] --> Parser["Semantic Intent & Verb Classifier"]
    Parser --> Actionable{"Is Imperative Action Verb?"}
    Actionable -- Yes --> Task["Category: TASK (Queued to Todo Dispatcher)"]
    Actionable -- No --> Note["Category: NOTE (Saved to Knowledge Graph)"]
```

## Features
- **Zero Friction Input**: Accepts any fleeting thought without demanding structured fields.
- **Fast Action Item Extraction**: Automatically tags tasks vs reflective thoughts.
