import { Component } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Calendar } from "./pages/calendar/Calendar";
import { CropForm } from "./pages/crops/CropForm";
import { CropList } from "./pages/crops/CropList";
import { Home } from "./pages/home/Home";

export class Directory extends Component {

    render() {
        return (
          <BrowserRouter>
            <Switch>
              <Route path="/" exact>
                <Home/>
              </Route>
              <Route path="/calendar/" exact>
                <Calendar/>
              </Route>
              <Route path="/crop/list" exact>
                <CropList/>
              </Route>
              <Route path="/crop/add" exact>
                <CropForm/>
              </Route>
            </Switch>
          </BrowserRouter>
        );
    }
}