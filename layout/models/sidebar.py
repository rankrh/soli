from farm.models.farm import Farm
from layout.models.sidebarSection import SidebarSection


class Sidebar:
    def __init__(self, user):
        self.user = user
        self.sections = [
            SidebarSection("Home", "home", "home", url="/"),
            SidebarSection(
                "Garden Schedule", "garden-schedule", "calendar-alt", url="calendar"
            ),
            SidebarSection("Seed Bank", "seedbank", "seedling", url="seedbank"),
            SidebarSection("Animals", "animals", "horse", url="herd"),
        ]

        self._set_sidebar_sections()

    def _set_sidebar_sections(self):
        self._set_staff_sections()
        self._set_farm_sections()

    def _set_staff_sections(self):
        if self.user.is_staff:
            self.sections.append(
                SidebarSection(
                    "Administration",
                    "admin",
                    "tools",
                    subsection_name="Crops",
                    subsections=[
                        SidebarSection("All Crops", "listCrops", url="listCrops"),
                        SidebarSection("Add Crop", "addCrop", url="addCrop"),
                        SidebarSection("Add Species", "addSpecies", url="addSpecies"),
                    ],
                )
            )

    def _set_farm_sections(self):

        for farm in Farm.objects.filter(farmer=self.user):
            self.sections.append(
                SidebarSection(
                    farm.name,
                    farm.slug,
                    "tractor",
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
                    ],
                )
            )
