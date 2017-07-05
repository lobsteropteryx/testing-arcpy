from unittest import TestCase
from mock import patch, MagicMock
from arcpy_wrapper import list_workspaces_for_mxd

@patch('my_project.arcpy_helper.arcpy')
class TestListDataSources(TestCase):

    def create_mock_layer(self, workspace):
        layer = MagicMock()
        layer.supports = MagicMock(return_value=True)
        layer.workspacePath = workspace
        return layer

    def test_list_single_data_source(self, mock_arcpy):
        data_source = 'layer1'
        layer = self.create_mock_layer(data_source)
        mock_arcpy.mapping.ListLayers = MagicMock(return_value=[layer])
        mxd = {}
        expected = [data_source]
        actual = list_workspaces_for_mxd(mxd)
        self.assertEqual(expected, actual)

    def test_lists_unique_data_sources(self, mock_arcpy):
        data_source1 = 'layer1'
        data_source2 = 'layer2'
        layer1 = self.create_mock_layer(data_source1)
        layer2 = self.create_mock_layer(data_source2)
        mock_arcpy.mapping.ListLayers = MagicMock(return_value=[layer1, layer1, layer2])
        expected = sorted([data_source2, data_source1])
        actual = sorted(list_workspaces_for_mxd({}))
        self.assertEqual(expected, actual)