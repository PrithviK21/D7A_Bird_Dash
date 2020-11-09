import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
li = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ac tortor vitae purus faucibus ornare suspendisse. Mi proin sed libero enim sed faucibus turpis in eu. Ac feugiat sed lectus vestibulum mattis. Nec dui nunc mattis enim ut tellus elementum sagittis vitae. Cras ornare arcu dui vivamus arcu felis bibendum. Dui faucibus in ornare quam viverra orci sagittis eu volutpat. Leo vel fringilla est ullamcorper eget nulla. Id faucibus nisl tincidunt eget nullam non nisi est. Fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus. Eget arcu dictum varius duis. Erat nam at lectus urna duis convallis convallis tellus. In est ante in nibh mauris. Sed nisi lacus sed viverra tellus in hac. Velit laoreet id donec ultrices tincidunt arcu non sodales neque. Cras ornare arcu dui vivamus arcu felis. Id diam vel quam elementum pulvinar. Dolor sit amet consectetur adipiscing elit duis. Diam vulputate ut pharetra sit. Et malesuada fames ac turpis egestas integer eget aliquet nibh.Nunc vel risus commodo viverra maecenas accumsan lacus vel facilisis. Interdum consectetur libero id faucibus nisl. In egestas erat imperdiet sed euismod nisi. Donec pretium vulputate sapien nec sagittis aliquam. Orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt. Convallis tellus id interdum velit laoreet id donec ultrices tincidunt. Nisl purus in mollis nunc sed. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque. Arcu non odio euismod lacinia at quis risus. Gravida rutrum quisque non tellus orci ac auctor augue mauris. Neque viverra justo nec ultrices dui sapien. Duis ultricies lacus sed turpis tincidunt id aliquet. Facilisi nullam vehicula ipsum a arcu cursus vitae congue./Elit duis tristique sollicitudin nibh sit amet commodo nulla. Augue eget arcu dictum varius duis at consectetur lorem donec. Enim eu turpis egestas pretium aenean pharetra. Turpis tincidunt id aliquet risus feugiat in ante metus. Malesuada bibendum arcu vitae elementum curabitur vitae. Bibendum neque egestas congue quisque egestas diam. Volutpat odio facilisis mauris sit amet. Urna id volutpat lacus laoreet non curabitur gravida. Quam viverra orci sagittis eu volutpat odio facilisis mauris. Nulla at volutpat diam ut venenatis tellus in metus vulputate. Cras semper auctor neque vitae tempus quam pellentesque nec. Sit amet volutpat consequat mauris nunc congue nisi vitae suscipit. Molestie nunc non blandit massa enim nec dui nunc. Duis convallis convallis tellus id interdum velit laoreet id. Nunc faucibus a pellentesque sit. Sem fringilla ut morbi tincidunt augue. Vitae proin sagittis nisl rhoncus mattis rhoncus urna./Duis ultricies lacus sed turpis tincidunt id. Commodo quis imperdiet massa tincidunt nunc pulvinar sapien. Nunc mi ipsum faucibus vitae. Scelerisque fermentum dui faucibus in ornare. Adipiscing elit pellentesque habitant morbi tristique senectus et netus. Magna fringilla urna porttitor rhoncus dolor purus non. Hendrerit dolor magna eget est lorem ipsum dolor sit. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet. Arcu bibendum at varius vel pharetra. Porttitor eget dolor morbi non arcu risus quis varius. Hac habitasse platea dictumst vestibulum rhoncus. Ipsum dolor sit amet consectetur. Feugiat sed lectus vestibulum mattis. Egestas quis ipsum suspendisse ultrices gravida dictum. Quis commodo odio aenean sed adipiscing diam donec adipiscing tristique.In egestas erat imperdiet sed euismod nisi porta. Senectus et netus et malesuada fames ac. A arcu cursus vitae congue mauris. Pulvinar etiam non quam lacus suspendisse faucibus interdum posuere lorem. Ornare aenean euismod elementum nisi quis eleifend. Etiam dignissim diam quis enim lobortis scelerisque. Purus ut faucibus pulvinar elementum integer enim neque. Nisi vitae suscipit tellus mauris a diam maecenas sed. Dictumst vestibulum rhoncus est pellentesque elit. Viverra mauris in aliquam sem fringilla ut morbi. Ullamcorper sit amet risus nullam eget felis eget.'
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.Header([
            html.Div([
                html.Div([html.A('Bird Name', href='#')], className='logo'),
                html.Nav([
                    html.A('Map', href='#'),
                    html.A('Graphs', href='#'),
                    html.A('Dataset', href='#'),
                    html.A('About', href='#'),
                ])
            ], className='wrapper')
        ]),
        html.Div([html.H2("Welcome to our app!")], className="banner"),
        html.Div([
            html.Div([
                html.H2("Content goes here"),
                html.P(li)], className="content"),
            ], className='wrapper'),

        html.Footer(
            ['Copyright my foot'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '2000px'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
