import { LineChart, Line, CartesianGrid, XAxis, YAxis, BarChart, Bar, Legend, Label, Tooltip } from 'recharts';
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
                            <p>Almost every soccer player has heard the myth that a 2-0 lead is the most dangerous lead. Conventional wisdom holds that
                                a team with a 2-goal lead will become complacent and sloppy, potentially letting a trailing, but motivated, team back
                                into the game. But does this logic hold up to real match data?
                            </p>
                            <p>To find out, I analyzed the results of over 1500 games from a public dataset of games compiled by a team of researches from 
                                the University of Pisa in 2019. This dataset includes games from the 2017-8 domestic seasons of the top 5 European leagues, the
                                2018 World Cup, and Euro 2016 international tournament. By tracking each goal and comparing the halftime lead to the final result
                                of the game, we can test the age-old cliche that 2-0 is the most dangerous lead. 
                            </p>
                            <div className='SideBySideGraphs'>
                                <div className='GraphContainer'>
                                    <h4>Final Match Result by Halftime Lead</h4>
                                    <BarChart width={600} height={300} data={halftime_lead.default}>
                                        <XAxis dataKey='name'/>
                                        <Bar dataKey='Leading Team Wins'stackId='x' stroke='green' fill='green'/>
                                        <Bar dataKey='Draw'stackId='x' stroke='orange' fill='orange'/>
                                        <Bar dataKey='Trailing Team Wins'stackId='x' stroke='red' fill='red'/>
                                        <Tooltip/>
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Wins</Label>
                                        </YAxis>
                                        <Legend/>
                                    </BarChart>
                                    
                                </div>
                                <div className='GraphContainer'>
                                    <h4>Final Match Result by Halftime Lead (Normalized)</h4>
                                    <BarChart width={600} height={300} data={halftime_normalized.default}>
                                        <XAxis dataKey='name'/>
                                        <Bar dataKey='Leading Team Wins'stackId='x' stroke='green' fill='green'/>
                                        <Bar dataKey='Draw'stackId='x' stroke='orange' fill='orange'/>
                                        <Bar dataKey='Trailing Team Wins'stackId='x' stroke='red' fill='red'/>
                                        <Tooltip/>
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Wins (as Percentage)</Label>
                                        </YAxis>
                                        <Legend/>
                                    </BarChart>
                                </div>
                            </div>
                            <p>Clearly, 2-0 is not the most dangerous lead. A team with a 2-goal lead would go on to win the game 91.7% of the time, drawing only 7.5% of games.
                                When compared with a 1-goal lead, which holds in only 71.4% of games, it becomes clear that a 2-goal lead is significantly more valuable than a 
                                1-goal lead. In fact, as might be expected, larger halftime leads almost always correspond to a higher chance of winning each game and decrease 
                                the chances of a draw or a loss. With the exception of the small sample of the 4-goal halftime lead (which is further distored by Schalke's miracle 
                                4-goal comeback against Dortmund), a team up 3 or more goals is almost certain to win the game. 
                            </p>
                            <p>However, this analysis does not completely address the myth that 2-0 is the most dangerous lead. The assumption that a team up 2 goals will become
                                more complacent as the trailing team becomes more aggressive does not necessarily affect the outcome of the game. To test the logic behind the myth,
                                I analyzed the scoring, shooting, and passing patterns of teams when ahead and behind. First, I attempted to approximate the aggression or complacency
                                of each team by measuring the frequency at which the next goal was scored by the leading team at various leads.
                            </p>
                            <div className='SideBySideGraphs'>
                                <div className='GraphContainer'>
                                    <h4>Next Goal Scored by Lead</h4>
                                    <LineChart width={600} height={300} data={next_goal.default}>
                                        <Line type="monotone" dataKey="Trailing Team Scores Next" stroke="red" />
                                        <Line type="monotone" dataKey="No More Goals" stroke="orange" />
                                        <Line type="monotone" dataKey="Leading Team Scores Next" stroke="green" />
                                        <CartesianGrid stroke="#ccc" />
                                        <XAxis dataKey="name" />
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Next Goal Scored</Label>
                                        </YAxis>
                                        <Legend/>
                                        <Tooltip/>
                                    </LineChart>
                                </div>
                                <div className='GraphContainer'>
                                    <h4>Next Goal Scored by Lead (as Percentage)</h4>
                                    <LineChart width={600} height={300} data={next_goal_normalized.default}>
                                        <Line type="monotone" dataKey="Trailing Team Scores Next" stroke="red" />
                                        <Line type="monotone" dataKey="No More Goals" stroke="orange" />
                                        <Line type="monotone" dataKey="Leading Team Scores Next" stroke="green" />
                                        <CartesianGrid stroke="#ccc" />
                                        <XAxis dataKey="name" />
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Next Goal Scored (as Percentage)</Label>
                                        </YAxis>
                                        <Legend/>
                                        <Tooltip/>
                                    </LineChart>
                                </div>
                            </div>
                            <p>
                                A lead of 5 goals or more does not appear frequently enough to be rigorously analyzed, so any attempt to identify trends in the scoring patterns
                                of teams leading or trailing must be limited to smaller deficits. As expected, the frequency at which no further goals are scored increases
                                with higher deficits (likely because higher deficits become more likely as the game progresses). However, we see that the absolute number of games
                                that end tied is significantly lower than the number of games ending with a 1-goal deficit. This is likely because both teams will attack more 
                                aggressively in pursuit of a win, while a team with a one-goal lead will attempt to defend their lead, often playing more conservatively than a trailing
                                team. This number decreases significantly for 2-goal leads, but this decrease does not support the myth that a 2-goal deficit causes teams to play complacently.
                                When adjusted for the total number of goals scored at each lead, we see that the number of games in which no more goals is scored actually increases as a percentage
                                of times in which a 2-goal lead occurs. More interestingly, we observe that the odds of a trailing team scoring next actually decreases with a larger deficit, while
                                the odds of the leading team scoring next remains approximately the same for up to a 4-goal lead. This suggests that teams opening up larger leads do not become complacent,
                                instead leveraging whichever advantages first opened their lead to increase it. Clearly, the next goal scored does not support the myth that a 2-goal deficit is a dangerous
                                lead, as the leading team goes on to score next 40.0% of the time, compared with only 24.7% for the trailing team.
                            </p>
                            <p>
                                Though analyzing goals scored generally gives a picture of the course of a game, soccer is a generally low-scoring game, making it more difficult to analyze the attacking
                                and defensive tendencies of teams, especially for uncommon leads. We can use shots per minute as an improved metric for the aggression of leading and trailing teams, grouping
                                teams by lead to determine how lead magnitude affects the willingnes of teams to attack.
                            </p>
                            <LineChart width={600} height={300} data={shot_frequency.default}>
                                    <Line type="monotone" dataKey="trailing" stroke="green" />
                                    <Line type="monotone" dataKey="leading" stroke="red" />
                                    <CartesianGrid stroke="#ccc" />
                                    <XAxis dataKey="name" />
                                    <Legend/>
                                    <Tooltip/>
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

