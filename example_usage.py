from client import AmbientThoughtCapture

capture = AmbientThoughtCapture()

# User texts or sends voice note while commuting
t1 = capture.capture_thought("Buy replacement filters for air purifier", source="whatsapp_voice")
t2 = capture.capture_thought("Interesting thought: local model latency dropped 4x this year", source="imessage")

print(f"Captured Thought 1: [{t1['category']}] {t1['raw_text']}")
print(f"Captured Thought 2: [{t2['category']}] {t2['raw_text']}")

print("Extracted Action Items:", len(capture.list_action_items()))
