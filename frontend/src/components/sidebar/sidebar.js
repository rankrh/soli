import React, { Component } from 'react'
import { SidebarSection } from "./sidebar_section"
import axios from "axios";
import { faCarrot, faChevronLeft, faChevronRight } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'



export class Sidebar extends Component {
    constructor(props) {
        super(props);
        this.state = {
          sections: [],
          expanded: true
        };
      }

    componentDidMount() {
        this.refreshSections();
      }
      
    refreshSections = () => {
        axios
          .get("/layout/sidebar/")
          .then((res) => {
            this.setState({ sections: res.data.sections });
          })
          .catch((err) => console.log(err));
    };

    renderSections = () => {
        return this.state.sections.map((section) => (
            <SidebarSection section={ section } key={ section.id } expanded={ this.state.expanded }></SidebarSection> 
        ));
    };

    toggleSidebar = () => {
      this.setState( { expanded: !this.state.expanded });
    }
    
    render() {
        return (
            <div className={ "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion " + (!this.state.expanded && "toggled")} id="accordionSidebar">
                <div className="sidebar-brand d-flex align-items-center justify-content-center">
                    <div className="sidebar-brand-icon rotate-n-15">
                        <FontAwesomeIcon icon={ faCarrot } />
                    </div>
                    <div className="sidebar-brand-text mx-3">SOLI</div>
                </div>
                <hr className="sidebar-divider my-0"></hr>
               { this.renderSections() }
               <hr class="sidebar-divider d-none d-md-block"/>
               <div class="text-center d-none d-md-inline">
                    <button class="rounded-circle border-0" id="sidebarToggle" onClick={ this.toggleSidebar }>
                      <FontAwesomeIcon prefix="fal" icon={ this.state.expanded ? faChevronLeft : faChevronRight } />
                    </button>
                </div>
            </div>
        )
    }
}