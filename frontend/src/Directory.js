import { Component } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Calendar } from "./pages/calendar/Calendar";
import { CalendarDirectory } from "./pages/calendar/CalendarDirectory";
import { Home } from "./pages/home/Home";
import { HomeDirectory } from "./pages/home/HomeDirectory";

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
            </Switch>
          </BrowserRouter>
        );
    }
}