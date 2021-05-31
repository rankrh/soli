import React, { Component } from 'react'
import axios from "axios";
import { Card, CardHeader, CardBody } from "../../components/base_elements/card/card";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { Contact } from '../../components/contact';
import { FarmMap } from '../../components/base_elements/map/farm_map';

export class MemberHome extends Component {

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
    
      renderMyFarms() {
        return this.state.farms.map((farm) => (
            <Card size="full" key={ farm.id }>
                <CardHeader>
                    <a id={ farm.name } href={ "/myfarms/" + farm.slug } className="text-decoration-none d-sm-flex align-items-center justify-content-between mb-4">
                        <div class="col-md-12 col-lg-10 text-center text-lg-left align-self-center">
                            <h2>
                            { farm.name } (est. { farm.year })
                            </h2>
                        </div>
                    </a>
                </CardHeader>
                <CardBody tag="h5">
                    <div className="row">
                        <Card size="lg">
                            <FarmMap farm={ farm }/>
                        </Card>
                        <Contact location={ farm }/>
                    </div>
                </CardBody>
            </Card>
        ));
      };

      renderNewFarm() {
        return (
            <Card size="full">
                <CardHeader>
                    <h4>
                        <a className="btn btn-sm btn-primary btn-circle stretched-link mx-3" href="/myfarms/create">
                            <FontAwesomeIcon icon={faPlus}/>
                        </a>
                        Create a Farm
                    </h4>
                </CardHeader>
                <CardBody>
                    <p>Your farms are the broadest level of organization.  They contain all information about the fields, gardens, and animals.</p>
                </CardBody>
            </Card>
        );
      }

    render() {
        return (
            <div>
                { this.renderMyFarms() }
                { this.renderNewFarm() }
            </div>
        );
    }
}