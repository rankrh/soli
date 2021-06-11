import { Component } from "react";
import { Card, CardBody, CardHeader } from "../../components/base_elements/card/card";
import { ButtonAppend, InputGroup, InputGroupText } from "../../components/base_elements/forms/FormGroup";
import { Option, Select, Text, TextArea } from "../../components/base_elements/forms/Inputs";
import { Column, Row } from "../../components/base_elements/grid/Grid";


export class CropForm extends Component {

    handleSubmit() {
        alert("Submitted");
    }

    render() {
        return (
            <div className="container">
                <form className="mb5" onSubmit={ this.handleSubmit }>
                    <div className="row justify-content-center">
                        <Card size="lg" accordion={ true } id="crop-information">
                            <CardHeader>
                                <h4>General Information</h4>
                            </CardHeader>
                            <CardBody>
                                <Row>
                                    <Column>
                                        <Text placeholder="Name" maxlength="50" required={ false }/>
                                    </Column>
                                    <Column>
                                        <InputGroup>
                                            <Select placeholder="Crop species" required={ false }>
                                                <Option name="Species"/>
                                            </Select>
                                            <ButtonAppend/>
                                        </InputGroup>
                                    </Column>
                                </Row>
                                <Row>
                                    <Column>
                                        <TextArea placeholder="Description" dimensions={[40, 5]}/>
                                    </Column>
                                </Row>
                            </CardBody>
                        </Card>
                        <Card size="lg" accordion={ true } id="planting-instructions">
                            <CardHeader>
                                <h4>Planting Instructions</h4>
                            </CardHeader>
                            <CardBody>
                                <Row>
                                    <Column>
                                        <InputGroup>
                                            <InputGroupText value="Plant"/>
                                            <Select placeholder="Pattern">
                                            </Select>
                                        </InputGroup>
                                    </Column>
                                </Row>
                            </CardBody>
                        </Card>
                    </div>
                </form>   
            </div> 
        );
    }
}