import json
import sys

sys.stdout.write(chr(4) + "json")
sys.stdout.flush()
first_line = sys.stdin.readline()

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
                            "usage": "Load structured data from plugin JSON format",
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
                    },
                ]
            }
        )
    )
else:
    call_str = ",".join([first_line] + sys.stdin.readlines())
    plugin_call = json.loads(call_str)
    command_name = plugin_call["CallInfo"]["name"]
    # sys.stderr.write(f"***{command_name}***\n{call_str}\n\n")
    if command_name == "into nujson":
        sys.stdout.write(
            json.dumps(
                {
                    "Value": {
                        "String": {
                            "span": {"start": 0, "end": 1},
                            "val": json.dumps(
                                plugin_call["CallInfo"]["input"]["Value"]
                            ),
                        }
                    }
                }
            )
        )
    elif command_name == "from nujson":
        sys.stdout.write(
            json.dumps(
                {
                    "Value": json.loads(
                        plugin_call["CallInfo"]["input"]["Value"]["String"]["val"]
                    )
                }
            )
        )
sys.stdout.write("\n")
sys.stdout.flush()
