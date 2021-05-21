import string

from soli.views.sidebarSection import SidebarSection


class SidebarMultiSection:
    def __init__(self, header: string, id: string, section_groups):
        self.header = header
        self.id = id
        self.section_groups = section_groups

    def add_section_group(self, section: SidebarSection):
        self.section_groups.append(section)
