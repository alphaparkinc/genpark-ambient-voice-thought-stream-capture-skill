import sys
import json
from client import AmbientThoughtCapture

capture = AmbientThoughtCapture()

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-ambient-voice-thought-stream-capture-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "capture_thought",
                        "description": "Ingest fleeting thought or voice note and categorize into task or note",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "raw_text": {"type": "string"},
                                "source": {"type": "string"}
                            },
                            "required": ["raw_text"]
                        }
                    },
                    {
                        "name": "list_action_items",
                        "description": "List all actionable tasks extracted from captured thoughts",
                        "inputSchema": {"type": "object", "properties": {}}
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "capture_thought":
            res = capture.capture_thought(args["raw_text"], args.get("source", "voice_message"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        elif tool_name == "list_action_items":
            items = capture.list_action_items()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(items, indent=2)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_res = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err_res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
