import os
import unittest
import arcpy


class MyModuleTest(unittest.TestCase):

    TEST_GDB = 'in_memory'

    def setup_data(self, table_name='MyTable'):
        input_file = os.path.abspath('tests/fixtures/test_data.gdb/{}'.format(table_name))
        output_file = '{}/{}'.format(self.TEST_GDB, table_name)
        arcpy.CreateFeatureclass_management(
            out_path=self.TEST_GDB,
            out_name=table_name,
            template=input_file
        )
        arcpy.Append_management(
            inputs=input_file,
            target=output_file,
            schema_type='NO_TEST'
        )
        return output_file

    def tearDown(self):
        arcpy.Delete_management(self.TEST_GDB)

    def test_adds_sum_field(self):
        feature_class = self.setup_data('SumData')
        field_name = 'SUM'
        field_names = [field.name for field in arcpy.ListFields(feature_class)]
        self.assertTrue(field_name in field_names)
