import dash
import dash_core_components as dcc
import dash_html_components as html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Initials Dash App"),
    html.Label("This is a Dash application with initials."),
    html.Div("Your initials: ", style={'margin': '10px'}),
    dcc.Input(id='input-initials', type='text', placeholder='Enter your initials'),
    html.Div("Select your country: ", style={'margin': '10px'}),
    dcc.Dropdown(
        id='dropdown-country',
        options=[
            {'label': 'United States', 'value': 'US'},
            {'label': 'Canada', 'value': 'CA'},
            {'label': 'United Kingdom', 'value': 'UK'},
            {'label': 'Australia', 'value': 'AU'}
        ],
        value='US'
    ),
    html.Div(id='output-initials', style={'margin': '10px'})
])

# Define callback to update the output
@app.callback(
    dash.dependencies.Output('output-initials', 'children'),
    [dash.dependencies.Input('input-initials', 'value'),
     dash.dependencies.Input('dropdown-country', 'value')]
)
def update_output(initials, country):
    if initials:
        return f"Your initials are: {initials.upper()}, and you selected {country}"
    else:
        return "Please enter your initials"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
