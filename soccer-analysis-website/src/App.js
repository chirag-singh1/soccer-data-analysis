import './App.css';
import {  BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Lead from './pages/lead.js'
import Home from './Home.js'
import SpainPortugal from './pages/spain-portugal.js'

export default function App() {
  return (
    <Router>
      <Switch>
      <Route path='/articles/lead'>
        <Lead/>
      </Route>
      <Route path='/articles/spain-portugal'>
        <SpainPortugal/>
      </Route>
      <Route path='/'>
        <Home/>
      </Route>
      </Switch>
    </Router>
    
  );
}