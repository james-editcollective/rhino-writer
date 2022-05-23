try:
    from typing import List
except:
    pass

import Rhino
import Rhino.Geometry as geo
import os

class RhinoWirter:
    def __init__(self, path, file_name):
        # type: (str, str) -> None

        self._file = Rhino.FileIO.File3dm()
        self._full_path = path + os.sep + file_name + ".3dm"

    def write_3dm(self, geo_objects, attribute_key, attribute_value):
        # type: (List[geo.GeometryBase] | geo.GeometryBase, str, str) -> None

        self._set_att_to_file(geo_objects, attribute_key, attribute_value)
        
        result = self._file.Write(self._full_path, 7)
        if result:
            print("Write 3dm sucess : ", self._full_path)

    def _set_att_to_file(self, geo_objects, attribute_key, attribute_value):
        # type: (List[geo.GeometryBase] | geo.GeometryBase, str, str) -> None

        if not isinstance(geo_objects, list):
            geo_objects = [geo_objects]
        
        for geo_object in geo_objects:
            att = Rhino.DocObjects.ObjectAttributes()
            att.SetUserString(attribute_key, attribute_value)
            if isinstance(geo_object, geo.Curve):
                self._file.Objects.AddCurve(geo_object, att)
            elif isinstance(geo_object, geo.Mesh):
                self._file.Objects.AddMesh(geo_object, att)
            elif isinstance(geo_object, geo.Brep):
                self._file.Objects.AddBrep(geo_object, att)
            else:
                raise Exception("Check geo_object type")