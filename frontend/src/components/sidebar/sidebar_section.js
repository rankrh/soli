import React, { Component } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'


export class SidebarSection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            section: props.section,
            expanded: props.expanded
        }
      }

    renderHeader() {
        return (
            <React.Fragment>
                { this.state.section.subsections.length > 0 && <hr className="sidebar-divider"/> }
                { this.state.section.heading ? (
                    <div class="sidebar-heading">
                        { this.state.section.heading }
                    </div>
                ) : "" }
            </React.Fragment>

        )
    };

    renderSectionDropdown(section) {
        return (
            <div id={ "collapse-" + section.id} className="collapse" data-bs-parent="#accordionSidebar" aria-labelledby={ section.id }>
                <div className="bg-white py-2 collapse-inner rounded">
                    { section.subsection_name && <h6 className="collapse-header">{ section.subsection_name }</h6>}
                    { section.subsections.map((subsection) =>
                        <a className="collapse-item" href={ subsection.url }>{ subsection.name }</a>
                    )}
                </div>
            </div>
        );
    }

    renderSectionHeader(section) {
        let url = section.subsections.length > 0 ? "#" :  section.url;
        //alert(url);
        let collapseProps = {}

        if (section.subsections.length) {
            collapseProps["data-bs-toggle"] = "collapse";
            collapseProps["data-bs-target"] = "#collapse-" + section.id
            collapseProps["aria-expanded"] = "false"
            collapseProps["aria-controls"] ="collapse-" + section.id
        }

        return (
            <a className="nav-link" href={ url } {...collapseProps}>
                { section.icon && <FontAwesomeIcon className="fa-fw mr-1" icon={ section.icon }/> }
                <span>{ section.name }</span>
            </a>
        );
    }


    renderSectionBody(section) {
        return (
            <React.Fragment key={ section.id }>
                { this.renderSectionHeader(section) }
                { this.state.section.subsections.length > 0 && this.renderSectionDropdown(section) }
            </React.Fragment>
        );
    }

    renderBody() {

        let body;

        if (this.state.section.section_groups) {
            body = this.state.section.section_groups.map((subsection) =>
                this.renderSectionBody(subsection)
            );
        } else {
            body = this.renderSectionBody(this.state.section);
        }

        return (
            <li className={"nav-item" + (this.state.section.subsections && " active")} id={ this.state.section.id }>
                { body }
            </li>
        );
    }

    render() {

        return (
            <React.Fragment>
                { this.renderHeader() }
                { this.renderBody() }
             </React.Fragment>
        )
    };
}