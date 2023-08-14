import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def topTitlesGraph(titles):
    NAME_ORDER = titles['Team Name'].tolist()
    NAME_ORDER.reverse()
    
    fig = go.Figure()

    fig.add_trace(go.Bar(x = titles['Wins'],
                        y = titles['Team Name'],
                        orientation = 'h',
                        text = titles['Wins'],
                        textposition = 'inside',
                        insidetextanchor = 'middle',
                        hovertemplate = '%{y}:%{x} Titles',
                        name = '',
                        marker = dict(color = '#F8D210')))

    fig.update_xaxes(showticklabels=False)

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = '<b>IPL Winners</b>', font_size = 24),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))
    
    return fig

def topWinsTeamGraph(matches):
    winners = matches[['Winner','city']].groupby('Winner').count().reset_index().sort_values('city',ascending=False)
    winners = winners.drop(winners[winners['Winner'] == 'No Result'].index[0])
    winners.rename(columns={'city':'Win'},inplace=True)

    NAME_ORDER = winners['Winner'].tolist()
    NAME_ORDER.reverse()

    fig = go.Figure()

    top = winners.Winner.iloc[0]
    wins = winners[winners['Winner'] == top].Win.values[0]

    annotation = f'<b><span style="color:#057DCD">{top}</span> leads the list with <span style="color:#057DCD">{wins}</span> wins</b>'

    top_df = winners.loc[winners['Winner'] == top]
    non_top_df = winners.loc[winners['Winner'] != top]

    fig.add_trace(go.Bar(x = non_top_df['Win'],
                        y = non_top_df['Winner'],
                        orientation = 'h',
                        text = non_top_df['Win'],
                        insidetextanchor = 'middle',
                        marker = dict(color = '#c5c5c5')))

    fig.add_trace(go.Bar(x = top_df['Win'],
                        y = top_df['Winner'],
                        orientation = 'h',
                        text = top_df['Win'],
                        marker = dict(color = '#057DCD')))

    fig.update_xaxes(showticklabels=False)

    fig.update_traces(name='', hovertemplate='%{y} : %{x} Wins')

    # fig.add_annotation(text=annotation,
    #                 font = dict(color = '#444444',family='Verdana',size=12),
    #                 showarrow = False,
    #                 xref = 'paper',
    #                 yref = 'paper',
    #                 x=0,
    #                 y=1.075)
    
    title = '<b>Distribution of Wins</b>'

    fig.update_layout(plot_bgcolor = 'white',
                    height = 600,
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = annotation),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))
    
    return fig

def topRunsGraph(player_stats, nationality):
    if nationality == 'Indian and Overseas':
        top_runs = player_stats[['Name','TotalRuns']].groupby('Name').sum().reset_index().sort_values('TotalRuns',ascending = False).head(20)
    else:
        top_runs = player_stats[player_stats['Nationality'] == nationality][['Name','TotalRuns']].groupby('Name').sum().reset_index().sort_values('TotalRuns',ascending = False).head(20)

    NAME_ORDER = top_runs.Name.tolist()
    NAME_ORDER.reverse()

    fig = go.Figure()

    top = top_runs.Name.iloc[0]
    runs = top_runs.loc[top_runs['Name'] == top].TotalRuns.values[0]

    top_df = top_runs.loc[top_runs['Name'] == top]
    non_top_df = top_runs.loc[top_runs['Name'] != top]

    annotation = f'<b><span style="color:#ffa500">{top}</span> leads the list with <span style="color:#ffa500">{runs}</span> runs</b>'

    fig.add_trace(go.Bar(x = non_top_df['TotalRuns'],
                        y = non_top_df['Name'],
                        orientation = 'h',
                        text = non_top_df['TotalRuns'],
                        marker = dict(color = '#c5c5c5')))

    fig.add_trace(go.Bar(x = top_df['TotalRuns'],
                        y = top_df['Name'],
                        orientation = 'h',
                        text = top_df['TotalRuns'],
                        marker = dict(color = '#ffa500')))

    fig.update_xaxes(showticklabels=False)

    fig.update_traces(name='' , hovertemplate='%{y}: %{x} Runs', insidetextanchor='middle')

    # fig.add_annotation(text=annotation,
    #                 font = dict(color = '#444444',family='Verdana',size=12),
    #                 showarrow = False,
    #                 xref = 'paper',
    #                 yref = 'paper',
    #                 x=0,
    #                 y=1.05)
    
    title = f'<b>Top 10 Run Scorers of All Time ({nationality})</b>'

    fig.update_layout(plot_bgcolor = 'white',
                    height = 700,
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = annotation),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))
    
    return fig

def topWicketsGraph(player_stats,nationality):
    if nationality == 'Indian and Overseas':
        top_wickets = player_stats[['Name','Wickets']].groupby('Name').sum().reset_index().sort_values('Wickets',ascending = False).head(20)
    else:
        top_wickets = player_stats[player_stats['Nationality'] == nationality][['Name','Wickets']].groupby('Name').sum().reset_index().sort_values('Wickets',ascending = False).head(20)

    NAME_ORDER = top_wickets.Name.tolist()
    NAME_ORDER.reverse()

    fig = go.Figure()

    top = top_wickets.Name.iloc[0]
    wickets = top_wickets.loc[top_wickets['Name'] == top].Wickets.values[0]

    top_df = top_wickets.loc[top_wickets['Name'] == top]
    non_top_df = top_wickets.loc[top_wickets['Name'] != top]

    annotation = f'<b><span style="color:#A020F0">{top}</span> leads the list with <span style="color:#A020F0">{wickets}</span> wickets</b>'

    fig.add_trace(go.Bar(x = non_top_df['Wickets'],
                        y = non_top_df['Name'],
                        orientation = 'h',
                        text = non_top_df['Wickets'],
                        marker = dict(color = '#c5c5c5')))

    fig.add_trace(go.Bar(x = top_df['Wickets'],
                        y = top_df['Name'],
                        orientation = 'h',
                        text = top_df['Wickets'],
                        marker = dict(color = '#A020F0')))

    fig.update_xaxes(showticklabels=False)

    fig.update_traces(name='' , hovertemplate='%{y}: %{x} Wickets', insidetextanchor = 'middle')

    # fig.add_annotation(text=annotation,
    #                 font = dict(color = '#444444',family='Verdana',size=12),
    #                 showarrow = False,
    #                 xref = 'paper',
    #                 yref = 'paper',
    #                 x=0,
    #                 y=1.05)
    
    title = f'<b>Top 10 Wicket Takers of All Time ({nationality})</b>'

    fig.update_layout(plot_bgcolor = 'white',
                    height = 700,
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = annotation),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))
    
    return fig

def popup_html(row,ground_data,matches):
        avg_innings_score = matches[['GroundName','Runs1']][matches['Runs1'] > 0].groupby('GroundName').agg('mean').apply(lambda x: round(x,0)).astype(int).reset_index().rename(columns={'GroundName':'Ground Name','Runs1':'Average First Innings Score'})
    
        bat_first = matches
        bat_first['WinnerBattingFirst'] = np.where((matches['FirstBattingTeamName'] == matches['Winner']),
                                            'First',
                                            np.where((matches['SecondBattingTeamName'] == matches['Winner']),
                                                    'Second',
                                                    'No Result')
                                            )
        bat_first = bat_first[['GroundName','WinnerBattingFirst','Winner']].groupby(['GroundName','WinnerBattingFirst']).count().reset_index()
        
        i = row
        ground_name = ground_data['GroundName'].iloc[i]
        ground_city = ground_data['City'].iloc[i]
        matches_held = matches[matches['GroundName'] == ground_name]['MatchRow'].count()
        
        wins_df = matches[matches['GroundName'] == ground_name]['Winner'].value_counts().reset_index().rename(columns={'index':'Team','Winner':'Wins'})
        lst = wins_df['Team'][wins_df['Wins'] == max(wins_df['Wins'])].tolist()
        
        if len(lst)>1:
            most_wins_team = ', '.join(lst)
        else:
            most_wins_team = lst[0]
            
        wins = max(wins_df['Wins'])
        
        avg_first_inns = avg_innings_score[avg_innings_score['Ground Name'] == ground_name].iloc[0,1]


        if not bat_first[(bat_first['GroundName'] == ground_name) & (bat_first['WinnerBattingFirst'] == 'First')].empty:
            wins_batting_first = bat_first[(bat_first['GroundName'] == ground_name) & (bat_first['WinnerBattingFirst'] == 'First')]['Winner'].values[0]
        else:
            wins_batting_first = 0

        if not bat_first[(bat_first['GroundName'] == ground_name) & (bat_first['WinnerBattingFirst'] == 'Second')].empty:
            wins_batting_second = bat_first[(bat_first['GroundName'] == ground_name) & (bat_first['WinnerBattingFirst'] == 'Second')]['Winner'].values[0]
        else:
            wins_batting_second = 0

        if not bat_first[(bat_first['GroundName'] == ground_name) & (bat_first['WinnerBattingFirst'] == 'No Result')].empty:
            no_result = bat_first[(bat_first['GroundName'] == ground_name) & (bat_first['WinnerBattingFirst'] == 'No Result')]['Winner'].values[0]
        else:
            no_result = 0

        left_col_color = "#EAFBFF"
        right_col_color = "#EAFBFF"

        html = f"""
                    <!DOCTYPE html>
                    
                    <html>
                    <center><h4 style="margin-bottom:5; font-family:Verdana; font-weight:900; width=200px;">{ground_name}</h4></center>
                    <center>
                        <table style="height:120px; width:300px;">
                            <tbody style="font-family:Verdana; font-weight:400;">
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">City </span></td>
                                    <td style="width: 150px;background-color:{right_col_color};">{ground_city}</td>
                                </tr>
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">Matches Held </span></td>
                                    <td style="width: 150px;background-color:{right_col_color};">{matches_held}</td>
                                </tr>
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">Team with Most Wins </span></td>
                                    <td style="width: 150px;background-color:{right_col_color};">{most_wins_team} ({wins})</td>
                                </tr>
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">Average First Innings Score </span></td>
                                    <td style="width: 150px;background-color:{right_col_color};">{avg_first_inns}</td>
                                </tr>
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">Wins Batting First</span></td>
                                    <td style="width: 150px;background-color:{right_col_color};">{wins_batting_first}</td>
                                </tr>
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">Wins Batting Second</span></td>
                                    <td style="width: 150px;background-color:{right_col_color};">{wins_batting_second}</td>
                                </tr>
                                <tr>
                                    <td style="background-color:{left_col_color};"><span style="color: #000000;">No Result</span></td>
                                    <td style="width: 150px; background-color:{right_col_color};">{no_result}</td>
                                </tr>
                            </tbody>
                        </table>
                    </center>
                    </html>
                """

        return html

def pointsTableGraph(table,year):
    teams = []
    for team in table.Team.tolist():
        team = f'<b>{team}</b>'
        teams.append('<br>'.join(team.split()))

    fig = make_subplots(cols=1, rows=3, shared_xaxes=False, row_heights = [0.1,0.4,0.35], vertical_spacing = 0.1)

    fig.add_trace(go.Scatter(x = teams,
                            y = table['Points'],
                            name = 'Points',
                            hovertemplate = '%{x} : %{y} Points',
                            marker = dict(size=8, color='#FFA500'),
                            line = dict(width = 1)),
                row = 1,
                col = 1)

    fig.update_yaxes(showticklabels=True, row = 1, col = 1)

    for column,color in [('Loss','#EF3340'), ('No Result','#00150C'), ('Tie','#C0E7F6'), ('Win','#02894B')]:
        fig.add_trace(go.Bar(x = teams,
                            y = table[column].tolist(),
                            name = column,
                            hovertemplate = '(%{x}: %{y})',
                            text = table[column].tolist(),
                            textposition = 'inside',
                            insidetextanchor = 'middle',
                            width = 0.3,
                            marker = dict(color = color,
                                        line_width = 0)),
                    row = 2,
                    col = 1)
        
    fig.update_yaxes(showticklabels=False, row = 2, col = 1)


    fig.add_trace(go.Bar(x = teams,
                            y = table['Net Run Rate'].tolist(),
                            name = 'Net Run Rate',
                            hovertemplate = '(%{x}: %{y})',
                            text = table['Net Run Rate'].tolist(),
                            textposition = 'outside',
                            width = 0.4,
                            marker = dict(color = '#2F435A',
                                        line_width = 0)),
                row = 3,
                col = 1)

    fig.update_yaxes(showticklabels=False, row = 3, col = 1)

    fig.update_xaxes(showgrid=False, tickangle=0, tickfont_size=10)
    fig.update_yaxes(showgrid=False)

    fig.add_vrect(x0=-0.5, x1=3.5, fillcolor='#02894B', opacity=0.1, annotation_text='')

    fig.update_layout(plot_bgcolor='white',
                    barmode = 'stack',
                    title = dict(text =f'<b>Points Table Visualized</b>'),
                    font = dict(family='Verdana',size = 11,color='#444444'),
                    height = 1200,
                    width = 900)
    
    return fig

def topRunsYearGraph(top_runs,year):
    NAME_ORDER = top_runs['Name'].tolist()
    NAME_ORDER.reverse()

    fig = make_subplots(cols=3, rows=1, subplot_titles=['<b>Total Runs</b>','<b>Strike Rate</b>','<b>Average</b>'], shared_yaxes=True, column_widths = [0.4,0.3,0.3])

    top_scorer = top_runs.Name.iloc[0]

    top_runs['Color'] = '#C5C5C5'
    top_runs.loc[top_runs['Name'] == top_scorer,'Color'] = '#ffa500'

    top_scorer_df = top_runs.loc[top_runs['Name'] == top_scorer]
    non_top_scorer_df = top_runs.loc[top_runs['Name'] != top_scorer]

    fig.add_trace(go.Bar(x = non_top_scorer_df['TotalRuns'],
                        y = non_top_scorer_df['Name'],
                        orientation = 'h',
                        text = non_top_scorer_df['TotalRuns'],
                        marker = dict(color = non_top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.add_trace(go.Bar(x = top_scorer_df['TotalRuns'],
                        y = top_scorer_df['Name'],
                        orientation = 'h',
                        text = top_scorer_df['TotalRuns'],
                        marker = dict(color = top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.add_trace(go.Scatter(x = top_runs['StrikeRate'],
                            y = top_runs['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_scorer_df['StrikeRate'],
                            y = top_scorer_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_runs['BattingAverage'],
                            y = top_runs['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 3)

    fig.add_trace(go.Scatter(x = top_scorer_df['BattingAverage'],
                            y = top_scorer_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 3)
    
    fig.update_xaxes(showticklabels=False, row=1, col=1,showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    fig.update_traces(textposition='inside', insidetextanchor='middle', hovertemplate='(%{y}: %{x} Runs)', row=1, col=1)
    fig.update_traces(hovertemplate='(%{y}: %{x})', row=1, col=2)
    fig.update_traces(hovertemplate='(%{y}: %{x})', row=1, col=3)

    title_text = f'<b><span style="color:{top_scorer_df.Color.iloc[0]}">{top_scorer}</span></b> leads the list of top run scorers in IPL {year} with <b><span style="color:{top_scorer_df.Color.iloc[0]}">{top_runs.TotalRuns.iloc[0]}</span></b> runs, at a strike rate of <b><span style="color:{top_scorer_df.Color.iloc[0]}">{top_runs.StrikeRate.iloc[0]}</span></b>'

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = title_text, font_size = 14),
                    showlegend = False,
                    height = 500,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))

    fig.update_traces(name='')

    return fig

def topWicketsYearGraph(top_wickets,year):
    NAME_ORDER = top_wickets['Name'].tolist()
    NAME_ORDER.reverse()

    fig = make_subplots(cols=3, rows=1, subplot_titles=['<b>Total Wickets</b>','<b>Strike Rate</b>','<b>Average</b>'], shared_yaxes=True, column_widths = [0.4,0.3,0.3])

    top_wicket_taker = top_wickets.Name.iloc[0]

    top_wickets['Color'] = '#C5C5C5'
    top_wickets.loc[top_wickets['Name'] == top_wicket_taker,'Color'] = '#A020F0'

    top_wicket_taker_df = top_wickets.loc[top_wickets['Name'] == top_wicket_taker]
    non_top_wicket_taker_df = top_wickets.loc[top_wickets['Name'] != top_wicket_taker]

    fig.add_trace(go.Bar(x = non_top_wicket_taker_df['Wickets'],
                        y = non_top_wicket_taker_df['Name'],
                        orientation = 'h',
                        text = non_top_wicket_taker_df['Wickets'],
                        marker = dict(color = non_top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.add_trace(go.Bar(x = top_wicket_taker_df['Wickets'],
                        y = top_wicket_taker_df['Name'],
                        orientation = 'h',
                        text = top_wicket_taker_df['Wickets'],
                        marker = dict(color = top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.add_trace(go.Scatter(x = top_wickets['BowlingStrikeRate'],
                            y = top_wickets['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_wicket_taker_df['BowlingStrikeRate'],
                            y = top_wicket_taker_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_wickets['BowlingAverage'],
                            y = top_wickets['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 3)

    fig.add_trace(go.Scatter(x = top_wicket_taker_df['BowlingAverage'],
                            y = top_wicket_taker_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 3)
    
    fig.update_traces(textposition='inside', insidetextanchor='middle', hovertemplate='(%{y}: %{x} Wickets)', row=1, col=1)
    fig.update_traces(hovertemplate='(%{y}: %{x})', row=1, col=2)
    fig.update_traces(hovertemplate='(%{y}: %{x})', row=1, col=3)

    fig.update_xaxes(showticklabels=False, row=1, col=1, showgrid=False)
    fig.update_yaxes(showgrid=False)

    title_text = f'<b><span style="color:{top_wicket_taker_df.Color.iloc[0]}">{top_wicket_taker}</span></b> leads the list of top wicket takers in IPL {year} with <b><span style="color:{top_wicket_taker_df.Color.iloc[0]}">{top_wickets.Wickets.iloc[0]}</span></b> wickets, at a strike rate of <b><span style="color:{top_wicket_taker_df.Color.iloc[0]}">{top_wickets.BowlingStrikeRate.iloc[0]}</span></b>'

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=12),
                    height = 500,
                    title = dict(text = title_text, font_size = 14),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))

    fig.update_traces(name='')

    return fig

def topStrikerBat(strikers):
    NAME_ORDER = strikers.Name.tolist()
    NAME_ORDER.reverse()

    fig = make_subplots(cols=2, rows=1,subplot_titles=['<b>Strike Rate</b>','<b>Runs</b>'], shared_yaxes=True, column_widths = [0.6,0.4])

    top_striker = strikers.Name.iloc[0]
    strike_rate = strikers.loc[strikers['Name'] == top_striker,'StrikeRate'].values[0]

    top_striker_df = strikers.loc[strikers['Name'] == top_striker]
    non_top_striker_df = strikers.loc[strikers['Name'] != top_striker]

    fig.add_trace(go.Bar(x = non_top_striker_df['StrikeRate'],
                        y = non_top_striker_df['Name'],
                        orientation = 'h',
                        text = non_top_striker_df['StrikeRate'],
                        marker = dict(color = '#c5c5c5')),
                row = 1,
                col = 1)

    fig.add_trace(go.Bar(x = top_striker_df['StrikeRate'],
                        y = top_striker_df['Name'],
                        orientation = 'h',
                        text = top_striker_df['StrikeRate'],
                        marker = dict(color = '#ffa500')),
                row = 1,
                col = 1)

    fig.update_traces(textposition='inside', insidetextanchor='middle', row=1, col=1)
    fig.update_xaxes(showticklabels=False, row=1, col=1, showgrid = False)
    fig.update_yaxes(showgrid = False)

    fig.add_trace(go.Scatter(x = strikers['TotalRuns'],
                            y = strikers['Name'],
                            mode = 'lines+markers',
                            marker = dict(size = 8),
                            line = dict(width=1,color = '#c5c5c5')),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_striker_df['TotalRuns'],
                            y = top_striker_df['Name'],
                            mode = 'markers',
                            marker = dict(size = 8),
                            line = dict(width=1,color = '#ffa500')),
                row = 1,
                col = 2)

    annotation = f'<b><span style="color:#ffa500">{top_striker}</span> leads the list with a strike rate of <span style="color:#ffa500">{strike_rate}</span></b>'

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=12),
                    height = 500,
                    title = dict(text = annotation, font_size = 14),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))

    fig.update_traces(name='', hovertemplate='(%{y}: %{x})')

    return fig

def topStrikerBowl(strikers):
    NAME_ORDER = strikers.Name.tolist()
    NAME_ORDER.reverse()

    fig = make_subplots(cols=2, rows=1, subplot_titles=['<b>Strike Rate</b>','<b>Wickets</b>'], shared_yaxes=True, column_widths = [0.6,0.4])

    top_striker = strikers.Name.iloc[0]
    strike_rate = strikers.loc[strikers['Name'] == top_striker,'BowlingStrikeRate'].values[0]

    top_striker_df = strikers.loc[strikers['Name'] == top_striker]
    non_top_striker_df = strikers.loc[strikers['Name'] != top_striker]

    fig.add_trace(go.Bar(x = non_top_striker_df['BowlingStrikeRate'],
                        y = non_top_striker_df['Name'],
                        orientation = 'h',
                        marker = dict(color='#c5c5c5'),
                        text = non_top_striker_df['BowlingStrikeRate']),
                row = 1,
                col = 1)

    fig.add_trace(go.Bar(x = top_striker_df['BowlingStrikeRate'],
                        y = top_striker_df['Name'],
                        orientation = 'h',
                        text = top_striker_df['BowlingStrikeRate'],
                        marker = dict(color = '#A020F0')),
                row = 1,
                col = 1)

    fig.update_traces(textposition='inside', insidetextanchor='middle', row=1, col=1)
    fig.update_xaxes(showticklabels=False, row=1, col=1, showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.add_trace(go.Scatter(x = strikers['Wickets'],
                            y = strikers['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1, color='#c5c5c5')),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_striker_df['Wickets'],
                            y = top_striker_df['Name'],
                            mode = 'markers',
                            marker = dict(size = 8),
                            line = dict(width=1,color = '#A020F0')),
                row = 1,
                col = 2)

    annotation = f'<b><span style="color:#A020F0">{top_striker}</span> leads the list with a strike rate of <span style="color:#A020F0">{strike_rate}</span></b>'

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=11),
                    height = 500,
                    title = dict(text = annotation),
                    showlegend = False,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))

    fig.update_traces(name='', hovertemplate='(%{y}:%{x})')

    return fig

def franchiseRunsGraph(player_stats,year,franchise):

    franchise_runs = player_stats[(player_stats['Year'] == year) & (player_stats['TeamName'] == franchise)][['Name','Matches','TotalRuns','StrikeRate','BattingAverage']].head(5)
    franchise_runs.Matches = franchise_runs.Matches.astype(int)
    franchise_runs.rename(columns={'TotalRuns':'Runs','StrikeRate':'Strike Rate','BattingAverage':'Average'},inplace=True)
    franchise_runs.Average = franchise_runs.Average.apply(lambda x:round(x,1))
    franchise_runs['Color'] = '#C5C5C5'
    franchise_runs.iloc[0,-1] = '#ffa500'

    NAME_ORDER = franchise_runs.Name.tolist()
    NAME_ORDER.reverse()

    fig = make_subplots(cols=3, rows=1, subplot_titles=['<b>Total Runs</b>','<b>Strike Rate</b>','<b>Average</b>'], shared_yaxes=True, column_widths = [0.4,0.3,0.3])

    top_scorer = franchise_runs.Name.iloc[0]

    top_scorer_df = franchise_runs.loc[franchise_runs['Name'] == top_scorer]
    non_top_scorer_df = franchise_runs.loc[franchise_runs['Name'] != top_scorer]

    fig.add_trace(go.Bar(x = non_top_scorer_df['Runs'],
                        y = non_top_scorer_df['Name'],
                        orientation = 'h',
                        text = non_top_scorer_df['Runs'],
                        marker = dict(color = non_top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.add_trace(go.Bar(x = top_scorer_df['Runs'],
                        y = top_scorer_df['Name'],
                        orientation = 'h',
                        text = top_scorer_df['Runs'],
                        marker = dict(color = top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.update_traces(textposition='inside', insidetextanchor='middle', hovertemplate='(%{y}:%{x})', row=1, col=1)
    fig.update_traces(hovertemplate='(%{y}:%{x})', row=1, col=2)
    fig.update_traces(hovertemplate='(%{y}:%{x})', row=1, col=3)

    fig.update_xaxes(showticklabels=False, row=1, col=1, showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.add_trace(go.Scatter(x = franchise_runs['Strike Rate'],
                            y = franchise_runs['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_scorer_df['Strike Rate'],
                            y = top_scorer_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = franchise_runs['Average'],
                            y = franchise_runs['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 3)

    fig.add_trace(go.Scatter(x = top_scorer_df['Average'],
                            y = top_scorer_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_scorer_df.Color.iloc[0])),
                row = 1,
                col = 3)

    title_text = f'<b><span style="color:{top_scorer_df.Color.iloc[0]}">{top_scorer}</span> leads the list with <span style="color:{top_scorer_df.Color.iloc[0]}">{top_scorer_df.Runs.iloc[0]}</span> runs, at a strike rate of <span style="color:{top_scorer_df.Color.iloc[0]}">{top_scorer_df["Strike Rate"].iloc[0]}</span></b>'

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = title_text),
                    showlegend = False,
                    height = 400,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))

    fig.update_traces(name='')

    return fig

def franchiseWicketsGraph(player_stats,year,franchise):
    franchise_wickets = player_stats[(player_stats['Year'] == year) & (player_stats['TeamName'] == franchise)][['Name','Matches','Wickets','BowlingStrikeRate','BowlingAverage']].sort_values('Wickets',ascending=False).head(5)
    franchise_wickets.Matches = franchise_wickets.Matches.astype(int)
    franchise_wickets.rename(columns={'BowlingStrikeRate':'Strike Rate','BowlingAverage':'Average'},inplace=True)
    franchise_wickets.Average = franchise_wickets.Average.apply(lambda x:round(x,1))

    franchise_wickets['Color'] = '#C5C5C5'
    franchise_wickets.iloc[0,-1] = '#A020F0'

    NAME_ORDER = franchise_wickets.Name.tolist()
    NAME_ORDER.reverse()

    fig = make_subplots(cols=3, rows=1, subplot_titles=['Wickets','Strike Rate','Average'], shared_yaxes=True, column_widths = [0.4,0.3,0.3])

    top_wicket_taker = franchise_wickets.Name.iloc[0]

    top_wicket_taker_df = franchise_wickets.loc[franchise_wickets['Name'] == top_wicket_taker]
    non_top_wicket_taker_df = franchise_wickets.loc[franchise_wickets['Name'] != top_wicket_taker]

    fig.add_trace(go.Bar(x = non_top_wicket_taker_df['Wickets'],
                        y = non_top_wicket_taker_df['Name'],
                        orientation = 'h',
                        text = non_top_wicket_taker_df['Wickets'],
                        marker = dict(color = non_top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.add_trace(go.Bar(x = top_wicket_taker_df['Wickets'],
                        y = top_wicket_taker_df['Name'],
                        orientation = 'h',
                        text = top_wicket_taker_df['Wickets'],
                        marker = dict(color = top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 1)

    fig.update_traces(textposition='inside', insidetextanchor='middle', hovertemplate='%{y}: %{x} Wickets', row=1, col=1)
    fig.update_traces(hovertemplate='(%{y}: %{x})', row=1, col=2)
    fig.update_traces(hovertemplate='(%{y}: %{x})', row=1, col=3)
    fig.update_xaxes(showticklabels=False, row=1, col=1, showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.add_trace(go.Scatter(x = franchise_wickets['Strike Rate'],
                            y = franchise_wickets['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = top_wicket_taker_df['Strike Rate'],
                            y = top_wicket_taker_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 2)

    fig.add_trace(go.Scatter(x = franchise_wickets['Average'],
                            y = franchise_wickets['Name'],
                            mode = 'lines+markers',
                            line = dict(width=1,color=non_top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 3)

    fig.add_trace(go.Scatter(x = top_wicket_taker_df['Average'],
                            y = top_wicket_taker_df['Name'],
                            mode = 'markers',
                            marker = dict(size=10,color=top_wicket_taker_df.Color.iloc[0])),
                row = 1,
                col = 3)

    title_text = f'<b><span style="color:{top_wicket_taker_df.Color.iloc[0]}">{top_wicket_taker}</span> leads the list with <span style="color:{top_wicket_taker_df.Color.iloc[0]}">{top_wicket_taker_df.Wickets.iloc[0]}</span> wickets, at a strike rate of <span style="color:{top_wicket_taker_df.Color.iloc[0]}">{top_wicket_taker_df["Strike Rate"].iloc[0]}</span></b>'

    fig.update_layout(plot_bgcolor = 'white',
                    font = dict(color = '#444444',family='Verdana',size=12),
                    title = dict(text = title_text),
                    showlegend = False,
                    height = 400,
                    yaxis = dict(linecolor = 'white',categoryorder = 'array',categoryarray = NAME_ORDER))

    fig.update_traces(name='')

    return fig
