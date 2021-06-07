import './App.css';
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
import * as shot_frequency from './assets/shot_frequency.json'
import * as next_goal from './assets/next_goal.json'
import * as next_goal_normalized from './assets/next_goal_normalized.json'
const data = [{name: 'Page A', uv: 400, pv: 2800, amt: 2400},{name: 'Page B', uv: 400, pv: 2800, amt: 2800},{name: 'Page C', uv: 300, pv: 2600, amt: 2000}];


function App() {
  return (
    <div className="App">
      <header className="App-header">Title
      </header>
    <LineChart width={600} height={300} data={shot_frequency.default}>
      <Line type="monotone" dataKey="trailing" stroke="green" />
      <Line type="monotone" dataKey="leading" stroke="red" />
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="name" />
      <YAxis />
    </LineChart>
    <LineChart width={600} height={300} data={next_goal.default}>
      <Line type="monotone" dataKey="trailing" stroke="red" />
      <Line type="monotone" dataKey="none" stroke="orange" />
      <Line type="monotone" dataKey="leading" stroke="green" />
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="name" />
      <YAxis />
    </LineChart>
    <LineChart width={600} height={300} data={next_goal_normalized.default}>
      <Line type="monotone" dataKey="trailing" stroke="red" />
      <Line type="monotone" dataKey="none" stroke="orange" />
      <Line type="monotone" dataKey="leading" stroke="green" />
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="name" />
      <YAxis />
    </LineChart>
    </div>
  );
}

export default App;
