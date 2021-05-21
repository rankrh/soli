from soli.views.sidebarMultiSection import SidebarMultiSection
from soli.views.sidebarSection import SidebarSection
from soli.views.sidebarSubsection import SidebarSubsection


class Sidebar:
    def __init__(self, page):
        self.sections = [
            SidebarSection("Home", "home", "fa-home", url="home"),
            SidebarSection(
                "Garden Schedule", "garden-schedule", "fa-calendar-alt", url="calendar"
            ),
            SidebarSection("Seed Bank", "seedbank", "fa-seedling", url="seedbank"),
            SidebarSection("Animals", "animals", "fa-horse", url="herd"),
        ]
        self.page = page
        self.get_sidebar_sections()

    def get_sidebar_sections(self):
        self._set_staff_sections()
        self._set_farm_sections()

        return self.sections

    def _set_staff_sections(self):
        if self.page.user.is_staff:
            self.sections.append(
                SidebarSection(
                    "Administration",
                    "admin",
                    "fa-tools",
                    subsections=[
                        SidebarSubsection(
                            "Crops",
                            [
                                SidebarSection(
                                    "All Crops", "listCrops", url="listCrops"
                                ),
                                SidebarSection("Add Crop", "addCrop", url="addCrop"),
                                SidebarSection(
                                    "Add Species", "addSpecies", url="addSpecies"
                                ),
                            ],
                        )
                    ],
                )
            )

    def _set_farm_sections(self):
        farm_section = SidebarMultiSection("My Farms", "farms", [])

        for farm in self.page.farms:
            farm_section.add_section_group(
                SidebarSection(
                    farm.name,
                    farm.slug,
                    "fa-tractor",
                    subsections=[
                        SidebarSubsection(
                            subsections=[
                                SidebarSection(
                                    "Overview",
                                    f"{farm.slug}-overview",
                                    url="farmOverview",
                                    url_params=[farm.slug],
                                ),
                                SidebarSection(
                                    "Plots",
                                    f"{farm.slug}-plots",
                                    url="plotOverview",
                                    url_params=[farm.slug],
                                ),
                            ]
                        )
                    ],
                )
            )

        self.sections.append(farm_section)
