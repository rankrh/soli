import React, { Component } from 'react'
import { List } from 'reactstrap'
import { SidebarSection } from "./sidebar_section"
import axios from "axios";
import { faCarrot } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'



export class Sidebar extends Component {
    constructor(props) {
        super(props);
        this.state = {
          sections: []
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
            <SidebarSection section={ section } key={ section.id }></SidebarSection> 
        ));
    };
    
    
    render() {
        return (
            <List className="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion">
                <div className="sidebar-brand d-flex align-items-center justify-content-center">
                    <div className="sidebar-brand-icon rotate-n-15">
                        <FontAwesomeIcon icon={ faCarrot } />
                    </div>
                    <div className="sidebar-brand-text mx-3">SOLI</div>
                </div>
                <hr className="sidebar-divider my-0"></hr>
               { this.renderSections() }
            </List>
        )
    }
}