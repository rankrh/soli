import React, { Component } from 'react'
import { MemberHome } from './MemberHome';
import { Landing } from './Landing';

export class Home extends Component {

    constructor(props) {
        super(props);
        this.user = props.user;
    }

    render() {
        // this is not right, just temporary.  Need to figure out how to redirect/render differently if logged in
        // vs if just on landing page.
        return !this.user ? <MemberHome/> : <Landing/>
    }
}