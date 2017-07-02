import arcpy


def add_sum_field(feature_class):
    arcpy.AddField_management(
        in_table=feature_class,
        field_name='SUM',
        field_type='DOUBLE'
    )

    fields = ['FIRST_VALUE', 'SECOND_VALUE', 'SUM'] 
    with arcpy.da.UpdateCursor(feature_class, fields) as cursor:
        for row in cursor:
            row[2] = row[0] + row[1]
            cursor.updateRow(row)
