import json

templateName = "template.json"

outputFile = open(templateName, "w")

template = {
    "templateName" : "testTemplate",
    "templateType" : "reactFunctional",
    "template" : [{
        "component": "TopNav",
        "arguments": [{
            "className" : "test"
        }],
        "children": [{
            "name" : "Nav"
        }]
    },
    {
        "component": "BotNav",
        "arguments": [{
            "className" : "test2"
        }],
        "children": [{
            "name" : "Nav"
        }]
    }]
}

outputFile.write(json.dumps(template, indent=4))
outputFile.close()