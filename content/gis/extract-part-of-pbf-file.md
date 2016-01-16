Title: Extract part of PBF file (Open Street Map binary data)
Date: 2016-01-16 13:25
Category: GIS
Tags: osmosis, pbf, extract

Extract part of PBF file, including information for highways and railways.

```bash
apt-get install osmosis
osmosis \
    --read-pbf file=/home/user/Downloads/bulgaria-latest.osm.pbf \
    --bounding-box \
      top=43.1671 \
      left=25.5254 \
      right=25.7760 \
      bottom=42.9886 \
      completeWays=yes \
    --tag-filter accept-ways "highway=*" \
    --tag-filter accept-ways "railway=*" \
    --tag-filter reject-relations \
    --used-node \
    --write-pbf veliko-tarnovo.osm.pbf
```