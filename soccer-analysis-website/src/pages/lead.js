import { LineChart, Line, CartesianGrid, XAxis, YAxis, BarChart, Bar } from 'recharts';
import * as shot_frequency from '../assets/shot_frequency.json'
import * as next_goal from '../assets/next_goal.json'
import * as next_goal_normalized from '../assets/next_goal_normalized.json'
import * as pass_distance from '../assets/pass_distance.json'
import * as pass_location from '../assets/pass_location.json'
import * as pass_accuracy from '../assets/pass_accuracy.json'
import * as halftime_lead from '../assets/halftime_lead.json'
import * as halftime_normalized from '../assets/halftime_normalized.json'
import React from 'react';
import './Page.css'

export default class Lead extends React.Component {

    render(){
        return (
            <div class='Page'>
                <div class='PageContents'>
                    <h1>Title</h1>
                    <div class = 'PagePanels'>
                        <div class='ArticleContents'>
                            <h2>Is 2-0 really the most dangerous lead?</h2>
                            <BarChart width={600} height={300} data={halftime_normalized.default}>
                                <XAxis dataKey='name'/>
                                <Bar dataKey='leading'stackId='x' stroke='green' fill='green'/>
                                <Bar dataKey='draw'stackId='x' stroke='orange' fill='orange'/>
                                <Bar dataKey='trailing'stackId='x' stroke='red' fill='red'/>
                                <YAxis/>
                            </BarChart>
                            <BarChart width={600} height={300} data={halftime_lead.default}>
                                <XAxis dataKey='name'/>
                                <Bar dataKey='leading'stackId='x' stroke='green' fill='green'/>
                                <Bar dataKey='draw'stackId='x' stroke='orange' fill='orange'/>
                                <Bar dataKey='trailing'stackId='x' stroke='red' fill='red'/>
                                <YAxis/>
                            </BarChart>
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
                            <LineChart width={600} height={300} data={pass_distance.default}>
                                <Line type="monotone" dataKey="trailing" stroke="red" />
                                <Line type="monotone" dataKey="leading" stroke="green" />
                                <CartesianGrid stroke="#ccc" />
                                <XAxis dataKey="name" />
                                <YAxis />
                            </LineChart>
                            <LineChart width={600} height={300} data={pass_location.default}>
                                <Line type="monotone" dataKey="trailing" stroke="red" />
                                <Line type="monotone" dataKey="leading" stroke="green" />
                                <CartesianGrid stroke="#ccc" />
                                <XAxis dataKey="name" />
                                <YAxis />
                            </LineChart>
                            <LineChart width={600} height={300} data={pass_accuracy.default}>
                                <Line type="monotone" dataKey="trailing" stroke="red" />
                                <Line type="monotone" dataKey="leading" stroke="green" />
                                <CartesianGrid stroke="#ccc" />
                                <XAxis dataKey="name" />
                                <YAxis />
                            </LineChart>
                        </div>
                    </div>
                </div>
                

            

            </div>
        );
    }
}

