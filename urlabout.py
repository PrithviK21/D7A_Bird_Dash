import dash_html_components as html

layout = html.Div(
    [
        html.Header([
            html.Div([
                html.Div([html.A('Bird Name', href='/Welcome')], className='logo'),
                html.Nav([
                    html.A('Map', href='/Map'),
                    html.A('Graphs', href='/Graph'),
                    html.A('Dataset', href='/Data'),
                    html.A('About', href='/About')
                ])
            ], className='wrapper')
        ]),
        html.Div([html.H2("About Us")], className="banner"),
        html.Div([
            html.Div([
                html.H2("What is this app?"),
                html.P("This app is created with a purpose of reaching out to the bird enthusiast in all of us. This "
                       "app will help you access all the data on bird sightings and population distribution in "
                       "Maharashtra for the 7 species we have selected. We have created an interactive scatter map,"
                       "a page to display graphs based on the data, filterable by date and species. Along with this, "
                       "the original dataset is available on the DATASET page. "
                       ),
                html.Hr(),
                html.H2("What did we use?"),
                html.P([
                    "Our primary framework was Dash. Dash is a free web application development framework that "
                    "provides "
                    " pure Python abstraction around HTML, CSS, and JavaScript. We had to learn HTML and CSS in order "
                    "to use Dash. Additional resources include "
                    "the use of Pycharm. To acquire datasets, we have used primarily three sites:", html.Br(), "ebird"
                    ".org "
                    , html.Br(), "inaturalist.org ", html.Br(), "twitter.com"]),
                html.Hr(),
                html.H2("Who are we?"),
                html.P(["We are second year students of Vivekananda Institute of Technology studying Computer Science."
                        "This build is part of our mini-project assigned to us in our year and mentored by Mrs. "
                        "Sharmila Sengupta. We are:",
                        html.Br(),
                        "J N Guru Akaash D7A 26 ",
                        html.Br(),
                        "Prithvi Kumar D7A 38 ",
                        html.Br(),
                        "Ashwin Kurup D7A 39 ",
                        html.Br(),
                        "Anurag Saraswat D7A 58 "]),
            ], className="content2"),
        ], className='wrapper'),

        html.Footer(
            ['© CMPN SE Group 6 2020'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '1300px'}
)
