from models.activity_diagram_element import ActivityDiagramElement

class MergeNode(ActivityDiagramElement):
    def __init__(self, name='', element_type=''):
        super.__init__(name=name, element_type=element_type)

    def __eq__(self, start_node): # pragma: no cover
        return self.name == start_node.name and \
        self.element_type == start_node.element_type

    def __str__(self): # pragma: no cover
        return 'Name: {}\nElement Type: {}\n'.format(self.name, \
                                                        self.element_type