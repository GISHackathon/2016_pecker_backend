import copy

class GeojsonBuilder(object):
    geojson_skeleton = {
              "type": "FeatureCollection",
              "features": []
        }

    feature_skeleton = {
            "geometry": {
                "type": "Point",
                "coordinates": []
            },
            "type": "Feature",
            "properties": {}
        }

    @classmethod
    def build_geojson(cls, features):
        tmp_geojson = copy.deepcopy(cls.geojson_skeleton)
        for f in features:
            if not ('x_coord' in f.keys()) or not ('y_coord' in f.keys()):
                continue
            tmp_feature = copy.deepcopy(cls.feature_skeleton)
            tmp_feature['geometry']['coordinates'] = [f['x_coord'], f['y_coord']]
            del f['x_coord']
            del f['y_coord']
            for key, val in f.iteritems():
                if '_' != key[0]:
                    tmp_feature['properties'][key] = str(val)
            tmp_geojson['features'].append(tmp_feature)
        return tmp_geojson
