class Garden:
    def __init__(
            self,
            plots=None,
            spacing=None,
            boundaries=None,
            north=None
    ):

        #validateGarden(*boundaries)

        self.plots = plots
        self.spacing = spacing
        self.boundaries = boundaries
        self.north = north