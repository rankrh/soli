import React, { Component } from "react";
import { Route } from "react-router-dom";

export class CalendarDirectory extends Component {

    render() {
        console.log("here");
        return (
            <Route path="/calendar/" exact>
            </Route>
        );
    }
}