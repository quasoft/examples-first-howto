Title: Add values to object map
Date: 2016-02-28 12:27
Category: JavaScript
Tags: javascript, object, map, config

Example:
-------

```javascript
var config = {
  'name1': 'value1',
  'name2': 'value2'
};

function use(configOverride) {
  for (var key in configOverride) { config[key] = configOverride[key]; }

  // Use `config` containing original values, merged with configOverride values ...
  console.log(config);
};
```

Explanation:
------------
The `init` function above allows the caller to override default config values, by providing an object map to be merged with defaults.

#### Usage:

```javascript
// Usage
var customConfig = {
  'name2': 'newvalue2',
  'newname3': 'value3'
};

use(customConfig);
```

#### Result:
```json
Object {name1: "value1", name2: "newvalue2", newname3: "value3"}
```
