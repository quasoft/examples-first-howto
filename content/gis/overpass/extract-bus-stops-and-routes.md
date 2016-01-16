Title: Extract bus stops and routes with http://overpass-turbo.eu and Overpass API.
Date: 2016-01-16 12:53
Category: GIS
Tags: overpass, api, open street map

```xml
<osm-script output="json" timeout="25">
  <query type="relation">
    <has-kv k="name" v="NAME OF BUS SERVICE"/>
    <bbox-query s="43.05823" w="25.59145" n="43.0971" e="25.65926"/>
  </query>
  <recurse type="down"/>
  <print />
</osm-script>
```

1. Replace "NAME OF BUS SERVICE"
2. Replace coordinates in bounding box tag (`<bbox-query>`)