import json

templateName = "template.json"

outputFile = open(templateName, "w")

template = {
    "templateName" : "testTemplate",
    "templateType" : "reactFunctional",
    "template" : [{
        "component": "Navbar",
        "arguments": [{
            "className" : "test"
        }],
        "children": [{
            "name" : "Nav"
        }]
    }]
}

outputFile.write(json.dumps(template, indent=4))
outputFile.close()