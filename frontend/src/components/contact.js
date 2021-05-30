import { faFacebook, faFacebookF, faInstagram, faTwitter } from "@fortawesome/free-brands-svg-icons";
import { faEnvelope } from "@fortawesome/free-regular-svg-icons";
import { faMapMarkerAlt, faPhone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Component } from "react";
import { Card, CardBody, CardHeader } from "./base_elements/card/card";

export class Contact extends Component {
    constructor(props) {
        super(props);
        this.state = {
          location: props.location
        };
        console.log(this.state.location);
    }

    renderAddress() {

        if (this.state.location.address) {
            return (
                <li>
                    <p>
                        <FontAwesomeIcon className="pr-1" icon={faMapMarkerAlt}/>
                        { this.state.location.address }
                        { this.state.location.address2 && <p>{ this.state.location.address2 }</p>}
                        { this.state.location.city && this.state.location.state && <p>{ this.state.location.city }, { this.state.location.state }</p>}
                   </p>
                 </li>
            )
        }
    }


    formatPhone(number) {

        var match = String(number).match(/^(\d{3})(\d{3})(\d{4})$/);
        if (match) {
            return "(" + match[1] + ") " + match[2] + "-" + match[3];
        }
    }

    renderPhone() {

        let number = this.formatPhone(this.state.location.phone);
        if (number) {
            return (
                <li>
                    <p>
                        <FontAwesomeIcon className="pr-1" icon={ faPhone }/>
                        { number }
                    </p>
                </li>
            );
        }
    }

    renderEmail() {
        if (this.state.location.email) {
            return (
                <li>
                    <p>
                       <FontAwesomeIcon icon={ faEnvelope } className="pr-1"/>
                        { this.state.location.email }
                    </p>
                </li>  
            );
        }
    }

    renderSocialMedia() {

        return (
            <ul class="list-inline text-center list-unstyled">
                <li class="list-inline-item">
                    <a class="p-2 fa-lg tw-ic">
                        <FontAwesomeIcon icon={ faTwitter }/> 
                    </a>
                 </li>
                <li class="list-inline-item">
                    <a class="p-2 fa-lg fa-ic">
                        <FontAwesomeIcon icon={ faFacebookF }/>
                    </a>
                </li>
                <li class="list-inline-item">
                    <a class="p-2 fa-lg ins-ic">
                        <FontAwesomeIcon icon={ faInstagram }/>
                    </a>
                </li>
            </ul>
        );
    }

    render() {
        return (
            <Card>
                <CardHeader className="contact text-center">
                    Get In Touch
                </CardHeader>
                <CardBody className="contact text-center">
                    <ul className="list-unstyled">
                        { this.renderAddress() }
                        { this.renderPhone() }
                        { this.renderEmail() }
                        <hr class="hr-light my-4"/>
                        { this.renderSocialMedia() }
                    </ul>
                </CardBody>
            </Card>
        );
    }
}