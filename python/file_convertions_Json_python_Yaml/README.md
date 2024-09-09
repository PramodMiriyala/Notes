# File Conversions

* Json & Yaml are data representation languages where Python dictionary is data stucture

## Python --> Json and Yaml

### Python Dict --> Json

```python
with open("resume.json", "w", encoding="utf8") as file:
    json.dump(resume, file, indent = 4)
```

* json.dump(): This function is specifically designed to serialize a Python object and write it directly to a file-like object
* json.dumps(): This function converts a Python object into a JSON string and returns it. It don't write to another file.
  * It is useful when you need the JSON representation as a string for further processing, such as printing or sending over a network.
* Json was inspired from JavaScipt

### Python Dict --> Yaml

* Yaml is not part of python standard library

```bash
pythom -m venv .venv
.\.venv\Scripts\activate
pip install pyyaml
```

```python
with open("resume.yaml", 'w', encoding="utf8") as file:
    yaml.dump(resume, file, default_flow_style=False)
```

#### default_flow_style (Parameter)

* Purpose: The default_flow_style parameter determines whether the YAML output should use the "flow style" or the "block style".

```yaml
#flow style
{name: John Doe, age: 30, city: New York}
#blockstyle
name: John Doe
age: 30
city: New York
```

## Json and Yaml --> Python Dict

### Json --> Python Dict

```python
with open("user.json", "r", encoding="utf8") as json_file:
    data = json.load(json_file)
print(data)
```

* `json.load()` to read the contents of the file and load them into a Python object.

### yaml --> Python Dict

```python
with open("details.yaml", "r", encoding="utf8") as yaml_file:
    details = yaml.load(yaml_file, Loader=yaml.FullLoader)
print(details)
```

* `yaml.load()` to read the contents of the file and load them into a Python object.
* `Loader=yaml.FullLoader` argument is used to safely load the YAML data without potential security risks.
