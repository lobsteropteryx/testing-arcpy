import arcpy


def add_sum_field(feature_class):
    arcpy.AddField_management(
        in_table=feature_class,
        field_name='SUM',
        field_type='DOUBLE'
    )
