"""Ambient Voice Thought Stream Capture.
100% Python Standard Library.
"""

import time

class AmbientThoughtCapture:
    """Extracts structured tasks and reflective notes from raw voice and text scratchpad inputs."""
    def __init__(self):
        self.thoughts = []
        self.action_items = []

    def capture_thought(self, raw_text, source="voice_message"):
        action_verbs = ["buy", "call", "schedule", "email", "cancel", "review", "order", "fix"]
        words = raw_text.lower().split()
        
        is_actionable = any(words[0] == verb or f" {verb} " in f" {raw_text.lower()} " for verb in action_verbs)
        category = "TASK" if is_actionable else "NOTE"
        
        record = {
            "id": f"THOUGHT-{len(self.thoughts) + 1:04d}",
            "raw_text": raw_text,
            "source": source,
            "category": category,
            "is_actionable": is_actionable,
            "timestamp": time.time()
        }
        self.thoughts.append(record)
        if is_actionable:
            self.action_items.append(record)
        return record

    def list_action_items(self):
        return list(self.action_items)
