import React, { Component } from "react";
import { Route } from "react-router-dom";
import { Home } from "./Home";

export class HomeDirectory extends Component {

    render() {
        return (
            <Route path="/" exact>
                <Home/>
            </Route>
        );
    }
}