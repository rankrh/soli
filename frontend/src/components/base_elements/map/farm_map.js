import { Map } from "./map";
import React, { Component } from 'react'

export class FarmMap extends Component {

    constructor(props) {
        super(props);

        this.state = {
            farm: props.farm,
        }
    }

    render() {
        return (
            <Map lat={ this.state.farm.location.lat } lng={ this.state.farm.location.long } zoom="16"/>
        );
    }
}
