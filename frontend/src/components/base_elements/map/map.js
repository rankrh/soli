import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import React, { Component, StrictMode } from 'react'
import '../../../css/maps.css';
import 'mapbox-gl/dist/mapbox-gl.css';
import  'leaflet/dist/leaflet.css';
import 'leaflet/dist/leaflet'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'


mapboxgl.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

export class Map extends Component {
    constructor(props) {
        super(props);

        this.state = {
            lng: props.lng ? props.lng : -100,
            lat: props.lat ? props.lat : 40,
            zoom: props.zoom ? props.zoom : 3,
            size: props.size ? "map-" + props.size : "map-2"
        };

        this.mapContainer = React.createRef();
    }

    componentDidMount() {

        const map = new mapboxgl.Map({
            container: this.mapContainer.current,
            style: 'mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr',
            center: [this.state.lng, this.state.lat],
            zoom: this.state.zoom
        });
        
        map.on('move', () => {
            this.setState({
                lng: map.getCenter().lng.toFixed(4),
                lat: map.getCenter().lat.toFixed(4),
                zoom: map.getZoom().toFixed(2)
            });
        });
    }



    render() {
        return(
            <div ref={ this.mapContainer } className={ this.state.size }/>
        );
    }
}


