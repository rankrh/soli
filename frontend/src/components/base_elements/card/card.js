import React, { Component } from 'react'


export class CardHeader extends Component {
    constructor(props) {
        super(props);
        this.id = props.id;
        this.accordion = props.accordion;
    }

    render() {
        let collapseProps = {}

        if (this.accordion) {
            collapseProps["data-bs-toggle"] = "collapse";
            collapseProps["data-bs-target"] = "#" + this.id + "-content";
            collapseProps["aria-expanded"] = "false";
            collapseProps["aria-controls"] = this.id + "-content";
        }

        return (
            <div id={this.id + "-header"} className="card-header py-3" {...collapseProps}>
                { this.props.children }
            </div>
        );
    }
}

export class CardBody extends Component {
    
    render() {
        return <p></p>
    }
}

export class Card extends Component {
    constructor(props) {
        super(props);
        this.size = this.get_size(props.size);
        this.shadow = " border-left-primary shadow";
        console.log(props);

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
            <div className={this.size}>
                <div className="card mb-4">
                    { this.props.children }
                </div>
            </div>
        );
    }
}