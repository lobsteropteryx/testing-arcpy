from unittest import TestCase
from mock import patch, MagicMock
from my_project.arcpy_wrapper import list_workspaces_for_mxd


@patch('my_project.arcpy_helper.arcpy')
class TestListDataSources(TestCase):
    def test_list_single_data_source(self, mock_arcpy):
        data_source = 'layer1'

        layer = MagicMock()
        layer.supports.return_value = True
        layer.workspacePath = data_source

        mock_arcpy.mapping.ListLayers = MagicMock(return_value=[layer])
        mxd = {}
        expected = [data_source]
        actual = list_workspaces_for_mxd(mxd)

        self.assertEqual(expected, actual)