import React, { Component } from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Link,
} from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import AddTutorial from "./components/add-tutorial.components";
import Tutorial from "./components/tutorial.components";
import TutorialsList from "./components/tutorials-list.components";
class App extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-expand navbar-dark bg-dark">
          <a href="/tutorials" className="navbar-brand">
            bezKoder
          </a>
          <div className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link to={"/Tutorial"} className="nav-link">
                Tutorials
              </Link>
            </li>
            <li className="nav-item">
              <Link to={"/add"} className="nav-link">
                Add
              </Link>
            </li>
          </div>
        </nav>
        <div className="container mt-3">
        <Router>
          <Switch>
            <Route exact path={["/", "/Tutorial"]} component={TutorialsList} />
            <Route exact path="/add" component={AddTutorial} />
            <Route path="/Tutorial/:id" component={Tutorial} />
          </Switch>
        </Router>
        </div>
      </div>
    );
  }
}
export default App;