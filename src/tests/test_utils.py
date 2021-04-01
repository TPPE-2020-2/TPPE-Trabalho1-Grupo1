import unittest
from utils.utils import Util
from models.activity_diagram_element import ActivityDiagramElement
from parameterized import parameterized


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.util = Util()

    @parameterized.expand([
        [[ActivityDiagramElement(name='A1', element_type=Util().START_NODE), \
          ActivityDiagramElement(name='A2', element_type=Util().TRANSITION_NODE)]],
        [[ActivityDiagramElement(name='B1', element_type=Util().START_NODE), \
          ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
          ActivityDiagramElement(name='B3', element_type=Util().MERGE_NODE)]],
        [[ActivityDiagramElement(name='C1', element_type=Util().START_NODE)]],
    ])
    def test_check_start_node_existence_true(self, nodes):
        response = self.util.check_start_node_existence(nodes)
        self.assertTrue(response)
    
    @parameterized.expand([
        [[ActivityDiagramElement(name='A1', element_type=Util().END_NODE), \
          ActivityDiagramElement(name='A2', element_type=Util().TRANSITION_NODE)]],
        [[ActivityDiagramElement(name='B1', element_type=Util().MERGE_NODE), \
          ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
          ActivityDiagramElement(name='B3', element_type=Util().MERGE_NODE)]],
        [[ActivityDiagramElement(name='C1', element_type=Util().ACTIVITY_NODE)]],
    ])
    def test_check_start_node_existence_false(self, nodes):
        response = self.util.check_start_node_existence(nodes)
        self.assertFalse(response)
    
    @parameterized.expand([
        [[ActivityDiagramElement(name='A1', element_type=Util().START_NODE), \
          ActivityDiagramElement(name='A2', element_type=Util().DECISION_NODE)]],
        [[ActivityDiagramElement(name='B1', element_type=Util().START_NODE), \
          ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
          ActivityDiagramElement(name='B3', element_type=Util().DECISION_NODE)]],
        [[ActivityDiagramElement(name='C1', element_type=Util().DECISION_NODE)]],
    ])
    def test_check_join_possibility(self, nodes):
        response = self.util.check_join_possibility(nodes)
        self.assertTrue(response)
    
    @parameterized.expand([
        [[ActivityDiagramElement(name='A1', element_type=Util().START_NODE), \
          ActivityDiagramElement(name='A2', element_type=Util().MERGE_NODE)]],
        [[ActivityDiagramElement(name='B1', element_type=Util().START_NODE), \
          ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
          ActivityDiagramElement(name='B3', element_type=Util().MERGE_NODE)]],
        [[ActivityDiagramElement(name='C1', element_type=Util().START_NODE)]],
    ])
    def test_check_join_possibility_false(self, nodes):
        response = self.util.check_join_possibility(nodes)
        self.assertFalse(response)