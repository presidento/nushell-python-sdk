import json
import sys
from typing import Any

sys.stdout.write(chr(4) + "json")
sys.stdout.flush()
first_line = sys.stdin.readline()
sys.stderr.write(first_line + "\n\n")

if first_line == '"Signature"':
    sys.stdout.write(
        json.dumps(
            {
                "Signature": [
                    {
                        "sig": {
                            "name": "into nujson",
                            "usage": "Expose plugin call in JSON",
                            "extra_usage": "",
                            "input_type": "Any",
                            "output_type": "String",
                            "required_positional": [],
                            "optional_positional": [],
                            "vectorizes_over_list": False,
                            "named": [],
                            "input_output_types": [["Any", "String"]],
                            "allow_variants_without_examples": True,
                            "search_terms": [],
                            "is_filter": False,
                            "creates_scope": False,
                            "allows_unknown_args": False,
                            "category": "Experimental",
                        },
                        "examples": [],
                    },
                    {
                        "sig": {
                            "name": "from nujson",
                            "usage": "Load structured data from plugin JSON",
                            "extra_usage": "",
                            "input_type": "String",
                            "output_type": "Any",
                            "required_positional": [],
                            "optional_positional": [],
                            "vectorizes_over_list": False,
                            "named": [],
                            "input_output_types": [["String", "Any"]],
                            "allow_variants_without_examples": True,
                            "search_terms": [],
                            "is_filter": False,
                            "creates_scope": False,
                            "allows_unknown_args": False,
                            "category": "Experimental",
                        },
                        "examples": [],
                    }
                ]
            }
        )
    )
else:
    call_str = ",".join([first_line] + sys.stdin.readlines())
    plugin_call = json.loads(call_str)
    sys.stdout.write(
        json.dumps(
            {
                "Value": {
                    "String": {
                        "span": {"start": 0, "end": 1},
                        "val": json.dumps(plugin_call["CallInfo"]["input"]["Value"]),
                    }
                }
            }
        )
    )
sys.stdout.write("\n")
sys.stdout.flush()
