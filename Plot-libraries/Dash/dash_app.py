import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Dash App with Dropdown Menus"),
    
    # Dropdown menu for selecting statistics
    dcc.Dropdown(
        id='stat-dropdown',
        options=[
            {'label': 'GDP Growth Rate', 'value': 'gdp'},
            {'label': 'Inflation Rate', 'value': 'inflation'},
            {'label': 'Unemployment Rate', 'value': 'unemployment'}
        ],
        value='gdp'  # Default value
    ),
    
    # Input container for selected statistics
    html.Div(id='input-container', className='input-container'),
    
    # Output container
    html.Div(id='output-display', className='output-container')
])

# Callback to update both input and output containers
@app.callback(
    [Output('input-container', 'children'),
     Output('output-display', 'children')],
    [Input('stat-dropdown', 'value')]
)
def update_containers(selected_stat):
    # Update input container based on selected statistics
    input_content = f'Selected statistics: {selected_stat}'
    
    # Perform some dummy operation based on selected statistics
    output_content = f'Dummy operation result for {selected_stat}'
    
    return input_content, output_content

if __name__ == '__main__':
    app.run_server(debug=True)
