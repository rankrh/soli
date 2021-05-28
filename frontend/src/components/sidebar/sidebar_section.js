import React, { Component } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'


export class SidebarSection extends Component {
    constructor(props) {
        super(props);
        this.section = props.section
      }
      
    render() {

        return (
            <li className="nav-item" id={ this.section.id }>
                { this.section.subsections.length ? <hr className="sidebar-divider"/> : ""}
                <a className="nav-link" href={ this.section.url }>
                    <FontAwesomeIcon
                        className="fa-fw mr-1"
                        icon={ this.section.icon } />
                    <span>{ this.section.name }</span>
                </a>
            </li>
        )
    };
}