import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Dash App with Dropdown Menu"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'},
            {'label': 'Option 3', 'value': 'option3'}
        ],
        value='option1'
    ),
    html.Div(id='output-display', className='output-container')
])

@app.callback(
    Output('output-display', 'children'),
    [Input('dropdown', 'value')]
)
def update_output(selected_option):
    return f'You have selected {selected_option}'

if __name__ == '__main__':
    app.run_server(debug=True)
