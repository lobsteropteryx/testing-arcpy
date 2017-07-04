import arcpy

def update_field(feature_class):
    fields = ['MY_STRING_FIELD'] 
    with arcpy.da.UpdateCursor(feature_class, fields) as cursor:
        for row in cursor:
            row[0] = init_cap(row[0])
            cursor.updateRow(row)
            
