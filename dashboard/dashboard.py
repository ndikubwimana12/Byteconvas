import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import random
from dash import dash_table
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
def create_dashboard(app):
    app.config.suppress_callback_exceptions = True  # Allows dynamic components in callbacks

    # Define the main layout with links to different sections
    app.layout = dbc.Container([
        # Header
        dbc.NavbarSimple(
            children=[
                html.A(html.Img(src="/static/logo.jpg", height="30px"), href="#"),
                
            ],
            brand="  UNEMPLOYMENT IN YOUTH PEOPLE (AGED 0 -25) IN 2023",
            brand_href="#",
            color="purple",
            dark=True,
            className="mb-1",
            style={"background-color": "rgb(2, 34, 107)","height":"70px","width":"101.5%","margin-left":"-1%"}
        ),
        
        dbc.Row([
        # Sidebar with navigation links
        dbc.Col(
            [
                html.Div(
                    [
                        # html.I(className="bi bi-speedometer2 me-2 text-light fs-1"),  # Dashboard icon
                        html.H2("Dashboard", className="text-white"),
                    ],
                    className="d-flex align-items-center",
                ),
                dbc.Nav(
                    [
                        dbc.NavLink(
                            [
                                html.I(className="bi bi-house me-2 text-info"),  # Icon for Home link
                                "Home"
                            ],
                            href="/dashboard/",
                            active="exact",
                            className="text-light d-flex align-items-center",
                            id="home-link"
                        ),
                        dbc.DropdownMenu(
                            label=[
                                html.I(className="bi bi-bar-chart-fill me-2"),  # Icon for Data Representation
                                "Data Representation"
                            ],
                    
                    children=[
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-bar-chart me-2 text-info"), "Youth Unemployment By Age Group"],
                            href="/visualization"
                        ),
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-pie-chart me-2 text-info"), "Youth Unemployment By Education Level"],
                            href="/time-series"
                        ),
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-geo-alt me-2 text-info"), "Youth Unemployment By Districts"],
                            href="/predictive-model"
                        ),
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-person-x me-2 text-info"), "Young Not in Employment nor in Education"],
                            href="/not_education"
                        ),
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-graph-up-arrow me-2 text-info"), "Youth Unemployment Rate (6-Year Comparison)"],
                            href="/6years"
                        ),
                    ],
                    nav=True,
                    in_navbar=True,
                    className="text-light",
                    style={"color": "white", "max-width": "250px"},
                ),
                    
                    dbc.DropdownMenu(
                            label=[
                            html.I(className="bi bi-pie-chart-fill me-2"),  # Icon for Data Representation
                            "Solutions"
                                    ],
                            
                    
                    children=[
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-bar-chart me-2 text-info"), "Attending Techinical Education"],
                            href="/innovation"
                        ),
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-pie-chart me-2 text-info"), "Create Own Oportunity"],
                            href="/tvet"
                        ),
                        
                        dbc.DropdownMenuItem(
                            [html.I(className="bi bi-person-x me-2 text-info"), "Attending Training"],
                            href="/trainning"
                        ),
                        
                    ],
                    nav=True,
                    in_navbar=True,
                    className="text-light",
                    style={"color": "white", "max-width": "250px"},
                ),
                
                        dbc.NavLink(
                    [html.I(className="bi bi-table me-2 text-info"), "Dataset View"],
                    href="/overview",
                    active="exact",
                    className="text-light",
                    id="overview-link"
                ),
                # dbc.NavLink(
                #     [html.I(className="bi bi-card-checklist me-2 text-info"), "Unemployment_Overview"],
                #     href="/data-tables",
                #     active="exact",
                #     className="text-light",
                #     id="data-tables-link"
                # ),
                
                dbc.NavLink(
                    [html.I(className="bi bi-info-circle me-2 text-info"), "User Guide"],
                    href="/user-guide",
                    active="exact",
                    className="text-light"
                ),
                    ],
            vertical=True,
            pills=True,
            className="bg-dark",
        ),
            ],
            width=2,
            style={"padding": "20px", "background-color": "#343a40", "min-height": "100vh"}
        ),

            # Main Content Area
            dbc.Col(
                html.Div(id="page-content"),
                width=10
            )
        ]),
        
        dcc.Location(id="url"),  # URL component to handle page navigation
    ], fluid=True)
    
    # Define callbacks for page navigation
    @app.callback(Output("page-content", "children"),
                    Input("url", "pathname"))
    def display_page(pathname):
        if pathname == "/overview":
            return get_overview_content()
        elif pathname == "/data-tables":
            return get_data_tables_content()
        elif pathname == "/visualization":
            return get_visualization_content()
        elif pathname == "/time-series":
            return get_time_series_content()
        elif pathname == "/predictive-model":
            return get_predictive_model_content()
        elif pathname == "/user-guide":
            return get_user_guide_content()
        elif pathname == "/not_education":
            return get_not_education_content()
        elif pathname == "/6years":
            return get_6years_content()
        elif pathname == "/tvet":
            return get_innovation_content()
        elif pathname == "/innovation":
            return get_tvet_content()
        elif pathname == "/trainning":
            return get_trainning_content()
        else:
            return get_home_content()  # Default page

    # Define callback for overview tabs
    @app.callback(
        Output("overview-content", "children"),
        [Input("overview-tabs", "active_tab")]
    )
    def update_overview_content(active_tab):
        if active_tab == "about":
            return html.Div([
                html.Img(src="/static/map.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}),
                    html.H3("About the Rwanda Youth Unemployment In 2023", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),
                # html.Img(src="/static/map.png",className="text-center", style={"height":"400px", "width":"600px"}),
                html.P("The unemployment rate, defined as the ratio of the number of unemployed persons to the total labour force, is the most commonly used indicator of the labour market. It is sometimes used in a general sense as an indicator of the health of the economy, not just the labour market. According to the results of the 2023 LFS,  the unemployment rate in Rwanda stood at 17.2 percent. It decreased compared to the previous year (20.5  percent). The unemployment rate stood at 15.8 percent in the urban areas and 18.0 percent in the rural areas.  The unemployment rate was higher among female (20.3 percent) than male (14.5 percent) and higher among  the youth (20.8 percent) than in the adults (14.8 percent).", className="px-5"),
                
            ])
        elif active_tab == "dataset":
                    # Load the CSV file from the assets folder
                data = pd.read_csv("assets/population_By_Ages.csv")
                
                # Return a data table to display the CSV content
                return html.Div([
                    html.Img(src="/static/ages.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}),
                    html.H3("Youth Unemployed population by sex, broad age group and urban/rural area, RLFS 2023", className="p-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),                   
                    
                    # Display the table
                    dash_table.DataTable(
                        data=data.to_dict('records'),  # Convert DataFrame to dictionary for Dash DataTable
                        columns=[{"name": i, "id": i} for i in data.columns],  # Create column headers
                        page_size=10,  # Optional: Limits number of rows per page
                        style_table={'overflowX': 'auto'},  # Allows horizontal scrolling
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'textAlign': 'left',
                            'padding': '5px',
                            'minWidth': '100px', 'width': '100px', 'maxWidth': '200px',  # Optional column width adjustments
                        }
                    )
                ])
        elif active_tab == "data_structure":
                # Load the CSV file from the assets folder
                data = pd.read_csv("assets/not_education.csv")
                
                # Return a data table to display the CSV content
                return html.Div([
                    html.Img(src="/static/no-ed.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}),
                    html.H3("Youth Not in Employment, Education, or Training (NEET)", className="p-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),                   
                    
                    # Display the table
                    dash_table.DataTable(
                        data=data.to_dict('records'),  # Convert DataFrame to dictionary for Dash DataTable
                        columns=[{"name": i, "id": i} for i in data.columns],  # Create column headers
                        page_size=10,  # Optional: Limits number of rows per page
                        style_table={'overflowX': 'auto'},  # Allows horizontal scrolling
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'textAlign': 'left',
                            'padding': '5px',
                            'minWidth': '100px', 'width': '100px', 'maxWidth': '200px',  # Optional column width adjustments
                        }
                    )
                ])
        elif active_tab == "summary_statistics":
                # Load the CSV file from the assets folder
                data = pd.read_csv("assets/population_By_District.csv")
                
                # Return a data table to display the CSV content
                return html.Div([
                    html.Img(src="/static/map.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth Unemployed population by District RLFS 2023", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    html.Hr(style={"margin-top":"50px", "color":"white"}),
                    
                    
                    
                    # Display the table
                    dash_table.DataTable(
                        data=data.to_dict('records'),  # Convert DataFrame to dictionary for Dash DataTable
                        columns=[{"name": i, "id": i} for i in data.columns],  # Create column headers
                        page_size=10,  # Optional: Limits number of rows per page
                        style_table={'overflowX': 'auto'},  # Allows horizontal scrolling
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold',
                        },
                        style_cell={
                            'textAlign': 'left',
                            'padding': '5px',
                            'minWidth': '100px', 'width': '100px', 'maxWidth': '200px',  # Optional column width adjustments
                        }
                    )
                ])
        elif active_tab == "education":
                # Load the CSV file from the assets folder
                data = pd.read_csv("assets/population_By_Education_Level.csv")
                
                # Return a data table to display the CSV content
                return html.Div([
                    html.Img(src="/static/education.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth Unemployed population by Education Level RLFS 2023", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    html.Hr(style={"margin-top":"50px", "color":"white"}),
                    
                    # Display the table
                    dash_table.DataTable(
                        data=data.to_dict('records'),  # Convert DataFrame to dictionary for Dash DataTable
                        columns=[{"name": i, "id": i} for i in data.columns],  # Create column headers
                        page_size=10,  # Optional: Limits number of rows per page
                        style_table={'overflowX': 'auto'},  # Allows horizontal scrolling
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'textAlign': 'left',
                            'padding': '5px',
                            'minWidth': '100px', 'width': '100px', 'maxWidth': '200px',  # Optional column width adjustments
                        }
                    )
                ])
        else:
            return html.Div("Select a tab to view content.")

# Define page content for each section
def get_home_content():
    return html.Div([
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H1("Welcome to National Institute of Statistics of Rwanda (NISR)", className="text-center mt-4 text-primary border border-shadow"),
                    ]),
                    className="custom-shadow"
                ),
                width=12
                
            ),
            
        ]),
        

    # First Row of Cards
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Youth Population (0 - 24) years old", className="card-title mt-2 text-center"),
                        html.Img(src="/static/p.png", style={"width": "100px", "height": "100px","margin-left":"30%"}),  # Unemployment rate icon
                        html.H1("  7,664,605  ", className="card-text text-primary text-center"),
                    ]),
                    className="shadow-sm"
                ),
                width=4
            ),
            
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Youth Males Aged 0-24 Years", className="card-title mt-2 text-center"),
                        html.Img(src="/static/male.png", style={"width": "100px", "height": "100px","margin-left":"30%"}),  # Unemployment rate icon
                        html.H1("   3,827,318   ", className="card-text text-primary text-center"),
                    ]),
                    className="shadow-sm"
                ),
                width=4
            ),
            
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Youth Females Aged 0-24 Years", className="card-title mt-2 text-center"),
                        html.Img(src="/static/female.png", style={"width": "100px", "height": "100px","margin-left":"30%"}),  # Unemployment rate icon
                        html.H1("  3,837,287  ", className="card-text text-primary text-center"),
                    ]),
                    className="shadow-sm d-flex"
                ),
                width=4
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Youth In Rural Area Aged 0-24 Years", className="card-title mt-2 text-center"),
                        html.Img(src="/static/rural.png", style={"width": "100px", "height": "100px","margin-left":"30%"}),  # Unemployment rate icon
                        html.H1("  5,473,407  ", className="card-text text-primary text-center"),
                    ]),
                    className="shadow-sm mt-2"
                ),
                width=4
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Youth In Urban Area Aged 0-24 Years", className="card-title mt-2 text-center"),
                        html.Img(src="/static/urban.png", style={"width": "100px", "height": "100px","margin-left":"30%"}),  # Unemployment rate icon
                        html.H1("  2,191,197  ", className="card-text text-primary text-center"),
                    ]),
                    className="shadow-sm mt-2"
                ),
                width=4
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Youth Unemployment Aged 16-30 In Labor Force", className="card-title mt-2 text-center"),
                        html.Img(src="/static/unemployment.png", style={"width": "100px", "height": "100px","margin-left":"30%"}),  # Unemployment rate icon
                        html.H1(" 663,581 ", className="card-text text-primary text-center"),
                    ]),
                    className="shadow-sm mt-2"
                ),
                width=4
            ),
        ], className="mt-2")
    ])
    

def get_overview_content():
    return html.Div([
        dbc.Tabs(
            [
                dbc.Tab(
                    label="About Youth Unemployment In Rwanda",
                    tab_id="about",
                    tab_style={"backgroundColor": "#f0f0f0", "padding": "5px", "height": "60px", "border": "solid 1px #ccc"},
                    active_tab_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold", "border-radius": "5px"}
                ),
                dbc.Tab(
                    label="Youth Unemployment By Ages",
                    tab_id="dataset",
                    tab_style={"backgroundColor": "#f0f0f0", "padding": "5px", "height": "60px", "border": "solid 1px #ccc"},
                    active_tab_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold", "border-radius": "5px"}
                ),
                dbc.Tab(
                    label="Youth Not in Employment, Education, or Training (NEET)",
                    tab_id="data_structure",
                    tab_style={"backgroundColor": "#f0f0f0", "padding": "5px", "height": "60px", "border": "solid 1px #ccc"},
                    active_tab_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold", "border-radius": "5px"}
                ),
                dbc.Tab(
                    label="Youth Unemployment By Districts",
                    tab_id="summary_statistics",
                    tab_style={"backgroundColor": "#f0f0f0", "padding": "5px", "height": "60px", "border": "solid 1px #ccc"},
                    active_tab_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold", "border-radius": "5px"}
                ),
                dbc.Tab(
                    label="Youth Unemployment By Education Level",
                    tab_id="education",
                    tab_style={"backgroundColor": "#f0f0f0", "padding": "5px", "height": "60px", "border": "solid 1px #ccc"},
                    active_tab_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold", "border-radius": "5px"}
                ),
            ],
            id="overview-tabs",
            active_tab="about",
            className="mb-3",
            style={"box-shadow": "2px 2px 2px 2px"}
        ),
        html.Div(id="overview-content")
    ])



def get_data_tables_content():
    return html.Div([
        html.H3("Youth Unemployment Over View", className="text-center"),
        html.P("Youth Unemployment overview will be displayed here...", className="text-muted text-center"),
    ])

# Data loading and visualization function
def get_visualization_content():
    try:
        # Load data from CSV
        data = pd.read_csv("assets/population_By_Ages.csv")

        # Normalize column names
        data.columns = data.columns.str.strip().str.lower()


        # Define numeric columns with corrected names
        numeric_columns = ["total", "male", "female", "urban", "rural",
                           "participated in subsistence agriculture",
                           "not participated  in subsistence agriculture"]

        # Convert relevant columns to numeric, handling potential issues with commas
        for col in numeric_columns:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col].str.replace(',', ''), errors='coerce').fillna(0)
            else:
                print(f"Column '{col}' not found in data.")


        # Ensure data lengths are consistent
        if data.shape[0] == 0:
            raise ValueError("The data is empty after processing.")

        # Pie Chart for Total Unemployed Population
        fig_total_unemployed = px.pie(
    data,
    names="unemployed population 16+",
    values="total",
    # title="Distribution of Unemployed Population by Age Group",
    labels={"Youth unemployed population 16+": "Age Group", "total": "Unemployed Population"},
    height=550
)


        # Bar Chart for Male vs Female Unemployed Population
        fig_gender_unemployed = px.bar(
            data,
            x="unemployed population 16+",
            y=["male", "female"],
            labels={"Youth unemployed population 16+": "Age Group", "value": "Population"},
            height=550,
            barmode="group"
        )

        # Line Chart for Urban vs Rural Unemployed Population
        fig_urban_rural = px.line(
            data,
            x="unemployed population 16+",
            y=["urban", "rural"],
            labels={"Youth unemployed population 16+": "Age Group", "value": "Population"},
            height=550
        )

        # Stacked Bar Chart for Participation in Subsistence Agriculture
        fig_subsistence = px.bar(
            data,
            x="unemployed population 16+",
            y=["participated in subsistence agriculture", "not participated  in subsistence agriculture"],
            labels={"Youth unemployed population 16+": "Age Group", "value": "Population"},
            height=550,
            barmode="stack"
        )

        # Layout with navigation links and tabs
        return html.Div([
    html.H3("YOUTH UNEMPLOYMENT BY AGE GROUP", className="text-center"),

    dcc.Tabs(
        id="visualization-tabs",
        children=[
            dcc.Tab(
                label="Total Unemployed Population By Age Group",
                children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"
                    }),
                    html.H3("Total Youth Unemployed Population by Age Group", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),
                    dcc.Graph(id="total-unemployed-bar-chart", figure=fig_total_unemployed)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Male vs Female Unemployed By Age Group",
                children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}),
                    html.H3("Male vs Female Youth Unemployed Population by Age Group", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),
                    dcc.Graph(id="gender-unemployed-bar-chart", figure=fig_gender_unemployed)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Urban vs Rural Unemployed By Age Group",
                children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"
                    }),
                    html.H3("Urban vs Rural Youth Unemployed Population by Age Group", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),
                    dcc.Graph(id="urban-rural-line-chart", figure=fig_urban_rural)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Subsistence Agriculture Participation By Age Group",
                children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={
                        "margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"
                    }),
                    html.H3("Youth Subsistence Agriculture Participation by Education Level", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),
                    dcc.Graph(id="subsistence-bar-chart", figure=fig_subsistence)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            )
        ],
        style={
            "height": "70px",
            "border": "solid 2px #ccc",
            "border-radius": "10px",
            "backgroundColor": "#e6e6e6"
        },
        colors={
            "border": "#ccc",
            "primary": "#00aaff",
            "background": "#f0f0f0"
        },
        vertical=False
    )
])

    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])      
        
def get_time_series_content():
    try:
        # Load data from CSV
        data = pd.read_csv("assets/population_By_Education_Level.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Convert relevant columns to numeric, handling potential issues with commas
        numeric_columns = ["Total", "Male", "Female", "Urban", "Rural", 
                           "Participated in subsistence agriculture", 
                           "Not Participated in subsistence agriculture"]
        for col in numeric_columns:
            data[col] = pd.to_numeric(data[col].str.replace(',', ''), errors='coerce').fillna(0)

        # Sort the data by "Total" unemployed population
        data_sorted = data.sort_values(by="Total", ascending=True)

        # Bar Chart for Total Unemployed Population by Education Level
        fig_total_unemployed = px.bar(
            data_sorted,
            x="Unemployed population By Age Group",
            y="Total",
            # title="Total Unemployed Population by Education Level",
            labels={"Youth Unemployed population By Age Group": "Education Level", "Total": "Unemployed Population"},
            height=550
        )

        # Pie Chart for Male vs Female Unemployed Population
        # Summing up the total male and female unemployed population
        total_male = data_sorted["Male"].sum()
        total_female = data_sorted["Female"].sum()

        # Creating a pie chart with male vs female distribution
        fig_gender_unemployed = px.pie(
            names=["Male", "Female"],
            values=[total_male, total_female],
            # title="Male vs Female Unemployed Population",
            labels={"names": "Gender", "values": "Population"},
            height=550
        )


        # Line Chart for Urban vs Rural Unemployed Population
        fig_urban_rural = px.line(
            data_sorted,
            x="Unemployed population By Age Group",
            y=["Urban", "Rural"],
            # title="Urban vs Rural Unemployed Population by Education Level",
            labels={"Youth Unemployed population By Age Group": "Education Level", "value": "Population"},
            height=550
        )

        # Stacked Bar Chart for Participation in Subsistence Agriculture
        fig_subsistence = px.bar(
            data_sorted,
            x="Unemployed population By Age Group",
            y=["Participated in subsistence agriculture", "Not Participated in subsistence agriculture"],
            # title="Participation in Subsistence Agriculture by Education Level",
            labels={"Unemployed population By Age Group": "Education Level", "value": "Population"},
            height=550,
            barmode="stack"
        )

        # Layout with navigation links and tabs
        return html.Div([
            html.H3("YOUTH UNEMPLOYMENT BY EDUCATION LEVEL", className="text-center"),
            
            dcc.Tabs(id="visualization-tabs", children=[
                dcc.Tab(label="Total Youth Unemployed Population By Education Level", children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Total Youth Unemployed Population by Education Level", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="total-unemployed-bar-chart", figure=fig_total_unemployed)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "0px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                dcc.Tab(label="Male vs Female Youth Unemployed By Education Level", children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"0px", "border-radius":"50px"}),
                    html.H3("Male vs Female Youth Unemployed Population by Education Level", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),                    
                    dcc.Graph(id="gender-unemployed-bar-chart", figure=fig_gender_unemployed)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "0px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                dcc.Tab(label="Urban vs Rural Youth Unemployed By Education Level", children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"0px", "border-radius":"50px"}),
                    html.H3("Urban vs Rural Youth Unemployed Population by Education Level", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),                    
                    dcc.Graph(id="urban-rural-line-chart", figure=fig_urban_rural)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "0px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                dcc.Tab(label="Youth Subsistence Agriculture Participation By Education Level", children=[
                    html.Img(src="/static/map.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"0px", "border-radius":"50px"}),
                    html.H3("Youth Participation in Subsistence Agriculture by Education Level", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="subsistence-bar-chart", figure=fig_subsistence)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "0px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            )
            ],
            style={
            "height": "70px",
            "border": "solid 2px #ccc",
            "border-radius": "10px",
            "backgroundColor": "#e6e6e6"
        },
        colors={
            "border": "#ccc",
            "primary": "#00aaff",
            "background": "#f0f0f0"
        },
        vertical=False
    )
])
    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])


def get_predictive_model_content():
    try:
        # Load data from CSV
        data = pd.read_csv("assets/population_By_District.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Rename the column if it has extra spaces
        if "Unemployed" not in data.columns and "  Unemployed" in data.columns:
            data.rename(columns={"  Unemployed": "Unemployed"}, inplace=True)

        # Convert the "Unemployed" column to numeric
        # data["Unemployed"] = pd.to_numeric(data["Unemployed"], errors='coerce').fillna(0)

        # Sort the DataFrame by "Unemployed" in ascending order
        data_sorted = data.sort_values(by="Unemployed", ascending=True)

        # Get the sorted list of districts
        sorted_districts = data_sorted["Province/ District"].tolist()

        # Bar Chart for Unemployed Population (sorted by "Unemployed")
        fig_unemployed = px.bar(
            data_sorted,
            x="Province/ District",
            y="Unemployment rate",
            labels={"Province/ District": "District", "Unemployment rate": "Unemployed Rate (%)"},
            height=550,
            category_orders={"Province/ District": sorted_districts}
        )
        
        fig_unemploy = px.bar(
            data_sorted,
            x="Province/ District",
            y="Combined rate of unemployment and potential labour force",
            # title="Unemployment Rate by District (Sorted by Unemployed Population)",
            labels={"Province/ District": "District", "Unemployment rate": "Unemployed Population Rate (%)"},
            height=550,
            category_orders={"Province/ District": sorted_districts}
        )

        # Line Chart for Unemployment Rate (sorted by "Unemployed" to match)
        fig_unemployment_rate = px.line(
            data_sorted,
            x="Province/ District",
            y="Combined rate of unemployment and time-related underemployment",
            labels={"Province/ District": "District", "Unemployment rate": "Rate (%)"},
            category_orders={"Province/ District": sorted_districts}
        )

        # Layout with navigation links and tabs
        return html.Div([
            html.H3("YOUTH UNEMPLOYMENT BY DISTRICTS", className="text-center"),
            
            dcc.Tabs(id="visualization-tabs", children=[
                dcc.Tab(label="Youth Unemployment Rate By Districts", children=[
                    html.Img(src="/static/job.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth Unemployed population by District RLFS 2023", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="unemployed-bar-chart", figure=fig_unemployed),
                    ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                dcc.Tab(label="Combined rate of Youth unemployment and time-related underemployment By Districts", children=[
                    html.Img(src="/static/job.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Combined rate of Youth unemployment and time-related underemployment", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="unemployment-rate-line-chart", figure=fig_unemployment_rate)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                dcc.Tab(label="Combined rate of Youth unemployment and potential labour force By Districts", children=[
                    html.Img(src="/static/job.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Combined rate of Youth unemployment and potential labour force", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="unemployment-rate-line-chart", figure=fig_unemploy)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "10px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            )
            ],
            style={
            "height": "70px",
            "border": "solid 2px #ccc",
            "border-radius": "10px",
            "backgroundColor": "#e6e6e6"
        },
        colors={
            "border": "#ccc",
            "primary": "#00aaff",
            "background": "#f0f0f0"
        },
        vertical=False
    )
        ])
    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])


def get_not_education_content():
    try:
        # Load data from CSV file (assuming comma-separated values)
        data = pd.read_csv("assets/not_education.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Define expected numeric columns and check if they exist
        expected_columns = ["Total", "Male_Total", "Female_Total", "Urban_Male","Urban_Female", "Rural_Male","Rural_Female"]
        missing_columns = [col for col in expected_columns if col not in data.columns]
        
        # Raise an error if essential columns are missing
        if missing_columns:
            raise ValueError(f"Missing columns in CSV: {', '.join(missing_columns)}")

        # Convert numeric columns (handle commas in the CSV file)
        for col in expected_columns:
            # Replace commas and convert to numeric, filling NaN values with 0
            data[col] = pd.to_numeric(data[col].astype(str).str.replace(',', ''), errors='coerce').fillna(0)

        # Separate the data into age group analysis and education level analysis
        age_data = data.iloc[1:4].copy()  # Adjust these indices based on your data
        education_data = data.iloc[5:].copy()  # Adjust these indices based on your data

        # Create bar chart for 'Youth Category' by age group
        fig_age_group = px.bar(
            age_data,
            x="Youth Category",
            y=["Total", "Male_Total", "Female_Total"],
            labels={"value": "Population", "Youth Category": "Age Group"},
            barmode="group",
            height=400
        )

        # Create line chart for Urban vs Rural distribution by age group
        fig_urban_rural_age = px.line(
            age_data,
            x="Youth Category",
            y=["Total", "Male_Total", "Female_Total"],
            labels={"value": "Population", "Youth Category": "Age Group"},
            height=400
        )

        # Create bar chart for 'Unemployment by Education Level'
        fig_education_level = px.bar(
            education_data,
            x="Youth Category",
            y=["Total", "Male_Total", "Female_Total"],
            labels={"value": "Population", "Youth Category": "Education Level"},
            barmode="group",
            height=400
        )

        # Create a pie chart for Total, Male, and Female distribution
        pie_labels = ["Total", "Male_Total", "Female_Total"]
        pie_values = [
            age_data["Total"].sum(),
            age_data["Male_Total"].sum(),
            age_data["Female_Total"].sum()
        ]

        fig_pie_chart = px.pie(
            names=pie_labels,
            values=pie_values,
            title="Distribution of Youth Not in Employment or Education (Total vs Male vs Female)",
            labels={"names": "Category", "values": "Population"}
        )
        fig_pie_chart.update_layout(margin=dict(t=50, b=50, l=50, r=50))

        # Layout with navigation links and tabs
        return html.Div([
            html.H3("Youth Not in Employment, Education, or Training (NEET)", className="text-center"),
            
            dcc.Tabs(id="neet-visualization-tabs", children=[
                dcc.Tab(label="Youth not in employment nor in education In Total", children=[
                    html.Img(src="/static/no-ed.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth not in employment nor in education In Total", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="age-group-bar-chart", figure=fig_age_group)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                
                dcc.Tab(label="Youth not in employment nor in education By Urban vs Rural by Education Level", children=[
                    html.Img(src="/static/no-ed.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth not in employment nor in education By Urban vs Rural by Education Level", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="distribution-pie-chart", figure=fig_pie_chart)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                
                
                
                dcc.Tab(label="Youth not in employment nor in education By Education Level Analysis", children=[
                    html.Img(src="/static/no-ed.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth not in employment nor in education By Education Level Analysis", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="education-level-bar-chart", figure=fig_education_level)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            ),
                dcc.Tab(label="Youth neither in employment nor in education By Urban vs Rural by Age Group", children=[
                    html.Img(src="/static/no-ed.png", height="100px", width="100px", style={"margin-top":"20px", "border":"solid 4px blue", "padding":"5px", "border-radius":"50px"}),
                    html.H3("Youth neither in employment nor in education By Urban vs Rural by Age Group", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width":"50%","margin-top":"-17px"}),
                    dcc.Graph(id="urban-rural-age-line-chart", figure=fig_urban_rural_age)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
            )
            ],
            style={
            "height": "70px",
            "border": "solid 2px #ccc",
            "border-radius": "10px",
            "backgroundColor": "#e6e6e6"
        },
        colors={
            "border": "#ccc",
            "primary": "#00aaff",
            "background": "#f0f0f0"
        },
        vertical=False
    )
        ])
        
    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])

def get_6years_content():
    try:
        # Load data from CSV file (assuming comma-separated values)
        data = pd.read_csv("assets/6years.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Extract the unemployment data for the pie chart
        years = ["2018", "2019", "2020", "2021", "2022", "2023"]
        unemployment_rates = data.iloc[0, 1:].astype(float).values  # Extract the rates from the first row

        # Create the pie chart for youth unemployment rates across 6 years
        fig_pie_chart = px.pie(
            names=years,
            values=unemployment_rates,
            # title="Youth Unemployment Rates (2018-2023)",
            labels={"names": "Year", "values": "Unemployment Rate (%)"}
        )

        # Layout with a pie chart tab
        return html.Div([
            html.H3("Youth Unemployment Analysis (2018-2023)", className="text-center"),

            dcc.Tabs(id="unemployment-visualization-tabs", children=[
                dcc.Tab(label="Youth Unemployment Rate (Pie Chart)", children=[
                    html.Img(src="/static/no-ed.png", height="100px", width="100px",
                            style={"margin-top": "20px", "border": "solid 4px blue", "padding": "5px",
                                    "border-radius": "50px"}),
                    html.H3("Youth Unemployment Rates (2018-2023)", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),
                    dcc.Graph(id="unemployment-pie-chart", figure=fig_pie_chart)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
                )
            ],
            style={
                "height": "70px",
                "border": "solid 2px #ccc",
                "border-radius": "10px",
                "backgroundColor": "#e6e6e6"
            },
            colors={
                "border": "#ccc",
                "primary": "#00aaff",
                "background": "#f0f0f0"
            },
            vertical=False
            )
        ])

    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])


def get_tvet_content():
    try:
        # Load data from CSV file (assuming comma-separated values)
        data = pd.read_csv("assets/sol1.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Extract categories and their corresponding values
        categories = data.iloc[:, 0].values  # First column: categories
        values = data.iloc[:, 1].astype(float).values  # Second column: values (percentages)

        # Create a pie chart for TVET employment data
        fig_pie_chart = px.pie(
            names=categories,
            values=values,
            title="Employment Status of TVET Graduates",
            labels={"names": "Employment Status", "values": "Percentage (%)"},
            color_discrete_sequence=px.colors.sequential.RdBu
        )

        # Layout with a pie chart tab
        return html.Div([
            dcc.Tabs(id="tvet-visualization-tabs", children=[
                dcc.Tab(label="Solution To Youth Unemployment By Attending TVET Schools And Gaining Jobs (Pie Chart)", children=[
                    html.Img(
                        src="/static/job..png",
                        height="100px",
                        width="100px",
                        style={"margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}
                    ),
                    html.H3("YOUTH EMPLOYMENT BASED ON ACQUIRED TVET SKILLS", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),

                    # Button to toggle the collapsible content
                    html.A(
                        "Explore Details Data Text Information | Solution 1",
                        className="btn btn-primary p-2 border border-rounded d-flex justify-content-center",
                        **{"data-bs-toggle": "collapse", "data-bs-target": "#demo"}
                    ),

                    # Collapsible content
                    html.Div(
                        id="demo",
                        className="collapse mt-3",
                        children=[
                            html.P(
                                "Researcher wanted to know the level of employability for graduands from TVET schools. "
                                "The findings are: The majority (65.1%) of all respondents strongly agreed that TVET graduates "
                                "find public jobs based on their acquired TVET skills. 30.2% agreed, 0.4% were neutral, "
                                "3.0% strongly disagreed, 1.3% disagreed, and 0.4% refused to comment on employment based on "
                                "skills from TVET schools.",
                                style={"margin-left": "0%", "margin-top": "-16px"},
                                className="border border-primary border-rounded p-3 bg-info"
                            ),
                            html.Ul([html.Li(f"{cat}: {val}%") for cat, val in zip(categories, values)])
                        ]
                    ),

                    dcc.Graph(id="tvet-pie-chart", figure=fig_pie_chart)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
                )
            ],
            style={
                "height": "70px",
                "border": "solid 2px #ccc",
                "border-radius": "10px",
                "backgroundColor": "#e6e6e6"
            },
            colors={
                "border": "#ccc",
                "primary": "#00aaff",
                "background": "#f0f0f0"
            },
            vertical=False
            )
        ])

    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])


def get_innovation_content():
    try:
        # Load data from CSV file
        data = pd.read_csv("assets/sol2.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Extract categories and their corresponding values
        categories = data.iloc[:, 0].values  # First column: Findings
        values = data.iloc[:, 1].astype(float).values  # Second column: Collected Data

        # Create a bar chart for the findings data
        fig_bar_chart = px.bar(
            x=categories,
            y=values,
            title="Innovation by TVET Graduates",
            labels={"x": "Findings", "y": "Percentage (%)"},
            color_discrete_sequence=["#1f77b4"]
        )

        # Customize the layout of the bar chart
        fig_bar_chart.update_layout(
            xaxis_title="Findings",
            yaxis_title="Collected Data (%)",
            xaxis_tickangle=-45,
            plot_bgcolor="#f0f0f0",
            bargap=0.2,
            bargroupgap=0.1
        )
        fig_bar_chart.update_traces(marker=dict(line=dict(color="#000000", width=1.5)))

        # Layout with a bar chart tab
        return html.Div([
            dcc.Tabs(id="tvet-visualization-tabs", children=[
                dcc.Tab(label="Solution To Youth Unemployment By Innovation (Bar Chart)", children=[
                    html.Img(
                        src="/static/innovation.png",
                        height="100px",
                        width="100px",
                        style={"margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}
                    ),
                    html.H3("INNOVATION BASED ON TVET SKILLS, CREATE JOB AND REDUCE UNEMPLOYMENT", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),

                    # Button to toggle the collapsible content
                    html.A(
                        "Explore Detailed Text Information | Solution 2 ",
                        className="btn btn-primary p-2 border border-rounded d-flex justify-content-center",
                        **{"data-bs-toggle": "collapse", "data-bs-target": "#demo"}
                    ),

                    # Collapsible content
                    html.Div(
                        id="demo",
                        className="collapse mt-3",
                        children=[
                            html.P(
                                "This analysis shows that 79.8% of TVET graduate, create their own opportunities based on their trade. this innovations increate employment among youth, and reduce unemployment in youth."
                                "The analysis shows respondents' views on the innovation and job creation abilities of TVET graduates. "
                                "A significant percentage (79.8%) appreciated these abilities, while others had different views, "
                                "including disagreement or lack of information.",
                                style={"margin-left": "0%", "margin-top": "-16px"},
                                className="border border-primary border-rounded p-3 bg-info"
                            ),
                            html.Ul([html.Li(f"{cat}: {val}%") for cat, val in zip(categories, values)])
                        ]
                    ),

                    dcc.Graph(id="tvet-bar-chart", figure=fig_bar_chart)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
                )
            ],
            style={
                "height": "70px",
                "border": "solid 2px #ccc",
                "border-radius": "10px",
                "backgroundColor": "#e6e6e6"
            },
            colors={
                "border": "#ccc",
                "primary": "#00aaff",
                "background": "#f0f0f0"
            },
            vertical=False
            )
        ])

    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])


def get_trainning_content():
    try:
        # Load data from CSV file
        data = pd.read_csv("assets/trainnings.csv")

        # Strip spaces from column names
        data.columns = data.columns.str.strip()

        # Extract categories and their corresponding percentage values
        categories = data["Type of technical skills learned"].values
        percentage_values = data["Percentage %"].astype(float).values

        # Create a bar chart for the training data
        fig_bar_chart = px.bar(
            x=categories,
            y=percentage_values,
            title="Employment Percentage by Technical Skills Learned",
            labels={"x": "Technical Skills", "y": "Percentage (%)"},
            color_discrete_sequence=["#1f77b4"]
        )

        # Customize the layout of the bar chart
        fig_bar_chart.update_layout(
            xaxis_title="Technical Skills",
            yaxis_title="Percentage (%)",
            xaxis_tickangle=-45,
            plot_bgcolor="#f0f0f0",
            bargap=0.2,
            bargroupgap=0.1
        )
        fig_bar_chart.update_traces(marker=dict(line=dict(color="#000000", width=1.5)))

        # Layout with a bar chart tab
        return html.Div([
            dcc.Tabs(id="tvet-visualization-tabs", children=[
                dcc.Tab(label="Solution To Youth Unemployment, By Attending Different Trainning", children=[
                    html.Img(
                        src="/static/trainning.png",
                        height="100px",
                        width="100px",
                        style={"margin-top": "20px", "border": "solid 4px blue", "padding": "5px", "border-radius": "50px"}
                    ),
                    html.H3("ATTENDING DIFFERENT TRAINNING WILL REDUCE UNEMPLOYMENT IN YOUTH", className="py-5 d-inline align-middle"),
                    html.Hr(style={"border": "solid 3px green", "margin-left": "6.5%", "width": "50%", "margin-top": "-17px"}),

                    # Button to toggle the collapsible content
                    html.A(
                        "Explore Detailed Data Text Information | Solution 3",
                        className="btn btn-primary p-2 border border-rounded d-flex justify-content-center",
                        **{"data-bs-toggle": "collapse", "data-bs-target": "#demo"}
                    ),

                    # Collapsible content
                    html.Div(
                        id="demo",
                        className="collapse mt-3",
                        children=[
                            html.P(
                                "the distribution of training courses completed and the status of employment of the"
                                "participants. There is in total 13 training courses or subjects that covered more than 1 percent each of the"
                                "total number of graduates. Among them, the most popular training course was tailoring with a participation"
                                "rate of 32.3 percent, followed by masonry with participation rates of 17.9 percent and hairdressing with 6.2 percent. ",
                                style={"margin-left": "0%", "margin-top": "-16px"},
                                className="border border-primary border-rounded p-3 bg-info"
                            ),
                            html.Ul([html.Li(f"{cat}: {val}%") for cat, val in zip(categories, percentage_values)])
                        ]
                    ),

                    dcc.Graph(id="tvet-bar-chart", figure=fig_bar_chart)
                ],
                style={"backgroundColor": "#f0f0f0", "padding": "2px", "height": "60px", "border": "solid 1px #ccc"},
                selected_style={"backgroundColor": "#00aaff", "color": "white", "fontWeight": "bold"}
                )
            ],
            style={
                "height": "70px",
                "border": "solid 2px #ccc",
                "border-radius": "10px",
                "backgroundColor": "#e6e6e6"
            },
            colors={
                "border": "#ccc",
                "primary": "#00aaff",
                "background": "#f0f0f0"
            },
            vertical=False
            )
        ])

    except Exception as e:
        return html.Div([
            html.H3("Error Loading Data", className="text-center text-danger"),
            html.P(f"An error occurred: {str(e)}", className="text-center text-muted")
        ])


def get_user_guide_content():
    return html.Div([
        
        html.H3("How to Use the Dashboard:", className="mt-4 text-center py-5"),
        dbc.Row([
            dbc.Col([
                html.H1("Step 1", className="text-center"),
                html.P("Open Project Folder in editor, then open terminal and type this: "),
                html.P("python app.py", style={"color":"yellow"}, className="text-bold"),
                html.Pre("PS D:\\unemployment_dashboard1> python app.py")
            ],
                width=3,
                className="bg-primary text-bold text-light",
                style={"border":"solid 1px", "border-radius":"10px", "height":"205px"}
                
                ),
            
            dbc.Col([
                html.H1("Step 2", className="text-center"),
                html.P("Then Follow this link to run Dashboard:  "),
                html.P("http://127.0.0.1:8050/dashboard/", style={"color":"yellow"}, className="text-bold")
            ],
                width=4,
                className="bg-primary text-bold text-light",
                style={"border":"solid 1px", "border-radius":"10px", "height":"205px"}
                
                ),
            
            dbc.Col([
                html.H1("Step 3", className="text-center"),
                html.P("Exprole Home link on left sidebar, to get the overview of Youth Peope aged 0-25"),
                html.Img(src="static/hom.png", style={"color":"yellow"}, height="50px", width="290px")
            ],
                width=3,
                className="bg-primary text-bold text-light",
                style={"border":"solid 1px", "border-radius":"10px", "height":"205px"}
                
                ),
            
            dbc.Col([
                html.H1("Step 4", className="text-center"),
                html.P("Click Data Presentation Link to get interactive charts"),
                html.Img(src="static/presentation.png", style={"color":"yellow"}, height="30px", width="200px")
            ],
                width=3,
                className="bg-primary text-bold text-light",
                style={"border":"solid 1px", "border-radius":"10px", "height":"205px"}
                
                ),
            dbc.Col([
                html.H1("Step 5", className="text-center"),
                html.P("After Visit Data Visualization, Navigate all Tabs to get all information you need to know. "),
                html.Img(src="static/tabs.png", style={"color":"yellow"}, height="50px", width="380px")
            ],
                width=4,
                className="bg-primary text-bold text-light",
                style={"border":"solid 1px", "border-radius":"10px", "height":"205px"}
                
                ),
            
            dbc.Col([
                html.H1("Step 6", className="text-center"),
                html.P("Select Solution on sidebar to see how Unemployment Problem can be fixed. "),
                html.Img(src="static/solution.png", style={"color":"yellow"}, height="30px", width="200px")
            ],
                width=3,
                className="bg-primary text-bold text-light",
                style={"border":"solid 1px", "border-radius":"10px", "height":"205px"}
                
                ),
            
        ],
                className="gap-5")
    ], className="container")
    

