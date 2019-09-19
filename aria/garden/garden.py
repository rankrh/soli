class Garden:
    def __init__(
            self,
            plots,
            spacing,
            boundaries,
            north
    ):

        validateGarden(*boundaries)

        self.plots = plots
        self.spacing = spacing
        self.boundaries = boundaries
        self.north = north