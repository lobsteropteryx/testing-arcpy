import arcpy
from my_project.updater import init_cap


def update_field(feature_class):
    fields = ['MY_STRING_FIELD'] 
    with arcpy.da.UpdateCursor(feature_class, fields) as cursor:
        for row in cursor:
            row[0] = init_cap(row[0])
            cursor.updateRow(row)


def list_workspaces_for_mxd(mxd):
    workspaces = set() 
    layers = arcpy.mapping.ListLayers(mxd)
    for layer in layers:
        if layer.supports("WORKSPACEPATH"):
            workspaces.add(layer.workspacePath)
    return list(workspaces)
