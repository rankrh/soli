import React, { Component } from "react";
import { Card, CardHeader, CardBody } from "reactstrap";
import { Sidebar } from "./components/sidebar/sidebar"
import axios from "axios";
import {library} from '@fortawesome/fontawesome-svg-core';
import * as Icons from '@fortawesome/free-solid-svg-icons';

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
      <Card className="col-lg-12 mb-4" key={ farm.id }>
        <CardHeader className="py-3">{ farm.name } (est. { farm.year })</CardHeader>
        <CardBody tag="h5">{ farm.owner }</CardBody>
      </Card>
    ));
  };


  render() {
    return (
      <div id="wrapper">
        <Sidebar farms={ this.state.farms } />
        <div id="content-wrapper" className="d-flex flex-column">
          <div id="content">
            <div className="container-fluid">
              <div
                id="my-farms"
                className="row">
                  <Card className="col-lg">
                    { this.renderMyFarms() }
                  </Card>
                </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;