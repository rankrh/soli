import React, { Component } from "react";
import { Sidebar } from "./components/sidebar/sidebar"
import axios from "axios";
import {library} from '@fortawesome/fontawesome-svg-core';
import * as Icons from '@fortawesome/free-solid-svg-icons';
import bootstrap from 'bootstrap'
import { Card, CardHeader, CardBody } from "./components/base_elements/card/card";
import { Topbar } from "./components/topbar/topbar";
import { Footer } from "./components/footer/footer";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Home } from "./pages/home/home";

const iconList = Object.keys(Icons)
  .filter((key) => key !== 'fas' && key !== 'prefix')
  .map((icon) => Icons[icon]);

library.add(...iconList);

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      farms: []
    };
  }

  componentDidMount() {
    this.refreshFarms();
  }

  refreshFarms = () => {
    axios
      .get("/myfarms/")
      .then((res) => {
        this.setState({ farms: res.data });
      })
      .catch((err) => console.log(err));
  };

  renderMyFarms = () => {
    return this.state.farms.map((farm) => (
      <Card size="lg" key={ farm.id }>
        <CardHeader className="py-3">{ farm.name } (est. { farm.year })</CardHeader>
        <CardBody tag="h5">{ farm.owner }</CardBody>
      </Card>
    ));
  };

  renderContent() {
    return (
      <div className="container-fluid">
        <BrowserRouter>
          <Switch>
            <Route path="/">
              <Home/>
            </Route>
          </Switch>
        </BrowserRouter>
      </div>
    );
  }


  render() {
    return (
      <div id="wrapper">
        <Sidebar farms={ this.state.farms } />
        <div id="content-wrapper" className="d-flex flex-column">
          <div id="content">
            <Topbar/>
            { this.renderContent() }
          </div>
          <Footer/>
        </div>
      </div>
    );
  }
}

export default App;