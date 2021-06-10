import { LineChart, Line, CartesianGrid, XAxis, YAxis, BarChart, Bar, Legend, Label, Tooltip } from 'recharts';
import { Link } from 'react-router-dom';
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
                    <div class = 'NavBar'>
                        <h1 class='PageTitle'>Soccer Myths: True or False</h1>
                        <div class = 'NavigationElements'>
                            <a href='/'>Home</a>
                            <a href='/articles'>Articles</a>
                            <a href='/about'>About</a>
                        </div>
                    </div>
                    <div class = 'PagePanels'>
                        <div class='ArticleContents'>
                            <div class='FlexContainer'>
                            <h2 class='ArticleTitle'>Is 2-0 really the most dangerous lead?</h2>
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
                                    <LineChart width={550} height={300} data={next_goal.default}>
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
                                <div className='RightGraphContainer'>
                                    <h4>Next Goal Scored by Lead (as Percentage)</h4>
                                    <LineChart width={550} height={300} data={next_goal_normalized.default}>
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
                            <div class='SingleGraph Right'>
                                <div class='GraphContainer'>
                                    <h4>Shots per Minute by Lead</h4>
                                    <LineChart width={600} height={300} data={shot_frequency.default}>
                                            <Line type="monotone" dataKey="Shots per Minute Trailing" stroke="red" />
                                            <Line type="monotone" dataKey="Shots per Minute Leading" stroke="green" />
                                            <CartesianGrid stroke="#ccc" />
                                            <XAxis dataKey="name" />
                                            <Legend/>
                                            <Tooltip/>
                                            <YAxis>
                                                <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Shots per Minute</Label>
                                            </YAxis>
                                        <YAxis />
                                    </LineChart>
                                </div>
                                <div>
                                    <p>
                                        As with the previous analysis, we can generally ignore the results for a lead greater than 5 goals because of the small sample size. For leads smaller than 3 goals,
                                        trailing teams take marginally more shots per minute than leading teams. When extrapolated to a full game, teams trailing by a single goal take 12.5 shots, while 
                                        leading teams average 11.1 shots. For a 2-goal lead, trailing teams would average 12.7 shots, while leading teams take 12.0 shots. For greater leads, the leading team takes
                                        the shot advantage, shooting more on a 3-goal lead and significantly more on any larger lead.   
                                    </p>
                                    <p>
                                        While trailing teams shoot slightly more than leading teams, this difference is marginal. In particular, we see that as the leading team grows their advantage,
                                        they shoot more in comparison with the trailing team, contrary to myth that teams up 2 goals become passive. Trailing teams likely are most aggressive when a single
                                        goal would be enough to tie the game. Alternatively, a larger lead may simply indicate that the leading team is a much better attacking team than the trailing team. When
                                        considering offensive output, it appears that a 2-goal lead is actually less dangerous than a 1-goal lead. 
                                    </p>
                                </div>
                            </div>
                            <p>
                                While all metrics of offensive output seem to indicate that a 2-goal lead is less dangerous than a 1-goal lead, such metrics are inevitably biased towards better offensive teams.
                                Teams that are better at converting offensive possession into shots and goals are most likely to open 2-goal leads, making it difficult to compare the offensive output of teams
                                up or down by any deficit. To analyze the affect of a goal deficit on the playstyle of teams in possession, we can analyze the passing patterns of teams by their lead.  
                            </p>
                            <div class='SingleGraph'>
                                <div>
                                    <p>
                                        We can use the average pass start location as an approximation of field position. One would expect trailing teams to play more aggressively, often holding the ball in their opponent's
                                        half as the leading team is happy to give up possession to protect their lead. The data appears to support this prediction. For a lead of 1 to 3 goals, the trailing team initiates
                                        their passes an average of approximately 2 yards further up the field. As the lead grows to 3 goals, the leading team generally maintains a similar passing profile, with only a slight
                                        decrease in pass start advancement. When interpreted as an approximation of field position, this decrease supports the idea that leading teams tend to play less aggressively than their 
                                        opponents, but does not support the idea that a 2-goal lead is more dangerous than other leads. Because we see a similar difference in pass start location across 1-3 goal leads, there is 
                                        no evidence to suggest that teams become particularly complacent or aggressive in a game with a 2-goal lead.
                                    </p>
                                    <p>
                                        Pass start location does not provide a complete profile of a team's playstyle or aggression. Losing teams might play longer or less accurate passes that start
                                        deeper in their half, negatively biasing their pass start location.
                                    </p>
                                </div>
                                <div class='GraphContainer Left'>
                                    <h4>Mean Pass Start Location by Lead</h4>
                                    <LineChart width={600} height={300} data={pass_location.default}>
                                        <Line type="monotone" dataKey="Mean Pass Start when Trailing" stroke="red" />
                                        <Line type="monotone" dataKey="Mean Pass Start when Leading" stroke="green" />
                                        <CartesianGrid stroke="#ccc" />
                                        <XAxis dataKey="name" />
                                        <Tooltip/>
                                        <Legend/>
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Mean Pass Start Location (yds)</Label>
                                        </YAxis>
                                    </LineChart>
                                </div>
                            </div>
                            <p>To further understand how leads affect attacking patterns, I analyzed the mean pass distance and pass location of teams by lead to get a better understanding
                                of how changing playstyles could bias the starting pass location of teams by lead.
                            </p>
                            <div className='SideBySideGraphs'>
                                <div className='GraphContainer'>
                                    <h4>Mean Attempted Pass Distance by Lead</h4>
                                    <LineChart width={550} height={300} data={pass_distance.default}>
                                        <Line type="monotone" dataKey="Mean Pass Distance when Trailing" stroke="red" />
                                        <Line type="monotone" dataKey="Mean Pass Distance when Leading" stroke="green" />
                                        <CartesianGrid stroke="#ccc" />
                                        <XAxis dataKey="name" />
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Mean Pass Distance (yds)</Label>
                                        </YAxis>
                                        <Legend/>
                                        <Tooltip/>
                                    </LineChart>
                                </div>
                                <div className='RightGraphContainer'>
                                    <h4>Pass Accuracy by Lead</h4>
                                    <LineChart width={550} height={300} data={pass_accuracy.default}>
                                        <Line type="monotone" dataKey="Pass Accuracy when Trailing" stroke="red" />
                                        <Line type="monotone" dataKey="Pass Accuracy when Leading" stroke="green" />
                                        <CartesianGrid stroke="#ccc" />
                                        <XAxis dataKey="name" />
                                        <YAxis>
                                            <Label angle={270} position='left' offset={-10} style={{ textAnchor: 'middle' }}>Pass Accuracy</Label>
                                        </YAxis>
                                        <Legend/>
                                        <Tooltip/>
                                    </LineChart>
                                </div>
                            </div>
                            <p>
                                There is no increase in mean attempted pass distance for trailing teams, suggesting that trailing teams do not significantly increase the number of long
                                to increase the speed of play. The pass accuracy of trailing teams, which remains approximately constant at around 83.5% for almost any lead, supports this conclusion.
                                Trailing teams do not try to play significantly more long or risky passes to increase the speed of play or earn an equalizer, which improves confidence in pass start
                                location as an approximation of field position. For leading teams, larger leads correlate with lower pass distances and higher pass accuracy (with a 2-goal lead), indicating
                                that leading teams are happy to hold possession with shorter, safer passes. When coupled with the pass start location data, this increase in shorter, safer passes supports
                                the prediction that leading teams will sit back and defend, choosing to keep possession instead of advancing the ball when they win possession. Overall, analysis of passing 
                                data indicates that leading teams do play more passively with a 2-goal lead, playing deeper in their own half and holding possession, while trailing teams do not play more aggressively,
                                but continue to play similar passes from more advanced locations.
                            </p>
                            <p>
                                In conclusion, there is no evidence to suggest that 2-0 is the most dangerous lead or supporting the logic that teams up by 2 goals become complacent and mistake-prone. 
                                Teams up 2 goals go on to win more games, shoot more, and score more than teams
                                up by a single goal. While teams up by 2 goals appear to concede marginally more field position to their opponents, they concede less field position than teams up
                                by a single goal. Trailing teams struggle to convert this advanced field position into shots or goals as their playstyle remains generally unchanged, while leading teams 
                                play shorter, safer passes to hold possession after turnovers. 
                            </p>
                            <div class='Buffer'></div>
                            </div>
                        </div>
                        <div class='RightBar'>
                            <div class='MoreArticles'>
                                <h4 class='RightBarTitle'>More Articles</h4>
                            </div>
                            <div class = 'About'>
                                <h4 class='RightBarTitle'>About</h4>
                                <p class='SidebarText'>All code used to conduct this analysis (and display this website!) is hosted publicly on Github. </p>
                                <a href='https://github.com/chirag-singh1/soccer-data-analysis'><button>View Github Repository</button></a>
                                <Link to='/about'> <button class='BottomSidebarButton'>More Development Info</button></Link>
                            </div>
                        </div>
                    </div>    
                </div>
            </div>
        );
    }
}

