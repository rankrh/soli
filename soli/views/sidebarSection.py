class SidebarSection:
    def __init__(self, name, id, icon=None, subsections=[], url=None, url_params=None):
        self.name = name
        self.id = id
        self.icon = icon
        self.url = url
        self.url_params = url_params
        self.subsections = subsections

        self.validate()

    def validate(self):
        if self.url is not None and self.subsections:
            raise ValueError("Sidebar sections cannot have both a url and children")
