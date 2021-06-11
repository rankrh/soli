import React, { Component } from 'react'
import { Column } from '../grid/Grid';


export class CardHeader extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            additionalClasses: " " + props.className,
            id: props.id,
            accordion: props.accordion
        }
    }

    render() {
        let collapseProps = {}

        if (this.state.accordion) {
            collapseProps["data-bs-toggle"] = "collapse";
            collapseProps["data-bs-target"] = "#" + this.id + "-content";
            collapseProps["aria-expanded"] = "false";
            collapseProps["aria-controls"] = this.id + "-content";
        }

        return (
            <div id={this.state.id + "-header"} className={ "card-header py-3" + this.state.additionalClasses } {...collapseProps}>
                { this.props.children }
            </div>
        );
    }
}

export class CardBody extends Component {
    constructor(props) {
        super(props);
        this.state = {
            additionalClasses: " " + this.props.className,
        }

      }

    render() {
        return (
            <div className={ "card-body" + this.state.additionalClasses }>
                { this.props.children }
            </div>
        );
    }
}

export class Card extends Component {

    constructor(props) {
        super(props);
        this.state = {
            size: this.get_size(props.size),
            shadow: false
        }

        const shadowClass = " border-left-primary shadow";
      }

    get_size(size) {
        const sizes = {
            "sm": "col-lg-2",
            "md": "col-lg-4",
            "lg": "col-lg-8",
            "full": "col-lg-12",
        }

        return sizes[size] || "col-lg-4";
    }

    render() {
        return (
            <div className={ this.state.size }>
                <div className="card mb-4">
                    { this.props.children }
                </div>
            </div>
        );
    }
}