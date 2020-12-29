from NodeGraphQt import BaseNode


class And(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'hal.comp'

    # initial default node name.
    NODE_NAME = 'AND Gate'

    def __init__(self):
        super(And, self).__init__()

        # create node inputs.
        self.add_input('in A')
        self.add_input('in B')

        # create node outputs.
        self.add_output('out A')


class Not(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'hal.comp'

    # initial default node name.
    NODE_NAME = 'NOT Gate'

    def __init__(self):
        super(Not, self).__init__()

        # create node inputs.
        self.add_input('in A')

        # create node outputs.
        self.add_output('out A')


class Or2(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'hal.comp'

    # initial default node name.
    NODE_NAME = 'OR Gate'

    def __init__(self):
        super(Or2, self).__init__()

        # create node inputs.
        self.add_input('in A')
        self.add_input('in B')

        # create node outputs.
        self.add_output('out A')


class Edje(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'hal.comp'

    # initial default node name.
    NODE_NAME = 'Edge detector'

    def __init__(self):
        super(Edje, self).__init__()

        # create node inputs.
        self.add_input('in')

        # create node outputs.
        self.add_output('out A')
