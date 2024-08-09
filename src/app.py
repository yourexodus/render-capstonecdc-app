import setuptools

from urllib.parse import quote as url_quote
import base64

from flask import Flask
import cv2
from dash import Dash, html, dcc
# app = Flask(__name__)
import dash

from jupyter_dash import JupyterDash

from dash.dependencies import Output, Input, State
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import html, dcc
# 1. pip install Pillow 2. Import Image from Pillow
# 3. pip install pandas
from PIL import Image

from dash_table import DataTable
import plotly.express as px
from prepare import PrepareData

# Initialize user_input_value
user_input_value = 1

##########################################################################################
#################      READ LOCAL DATA :  ALL   ##########################################
##########################################################################################
prepared_data = PrepareData(download_new=False)
df = prepared_data.read_local_data('all', "data/prepared")
##########################################################################################
# Create the app
app = dash.Dash(__name__)
server = app.server in src/app.py

#########################################################################################
########## Header Section Divs: link, Banner, mytable:                              #####
##########                                                                          #####
##########               mytable items:     doctorcat_item and meowmidwest_item     #####
#########################################################################################
#### ********************************  ######
#############      LINK       ################
#### ********************************  ######

link = dbc.NavLink("View Github Repository", href="https://github.com/yourexodus/capstone_CDC")
#### ********************************  ######
#############      BANNER ITEM   ############
#### ********************************  ######
banner_img_path = "assets/banner2.PNG"
banner_img = Image.open(banner_img_path).convert('RGB')

banner_item = dbc.Row(
    [
        dbc.Col(
            [
                dbc.CardImg(src=banner_img, style={'height': '200px', 'width': '100%'}),
                # Add other components for sidebar and navbar here...
            ]
        )
    ]
)

######### ******************************************  ##############
#########              mytable ITEMs:                  ##############
#########      doctorcat_item and meowmidwest_item    ##############
######### ********************************  ########################
doctorcat_img_path = "assets/doctorcat.png"
doctorcat_img = Image.open(doctorcat_img_path)

doctorcat_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([

                        html.Img(src=doctorcat_img,
                                 style={'width': '100%', 'height': '500px', 'justify-content': 'center',
                                        'align-items': 'center'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)
doctorcat_item.style = {'gridArea': "doctorcat_item"}


def get_video_frame():
    cap = cv2.VideoCapture('assets/MeowMidwest.mp4')
    ret, frame = cap.read()
    cap.release()  # Release the capture after reading a frame

    if ret:
        # Convert frame to RGB format for encoding
        frame = cv2.resize(frame, (300, 400))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        ret, buffer = cv2.imencode('.jpg', frame)
        # Encode frame as base64 string

        encoded_image = base64.b64encode(buffer).decode('utf-8')
        return f'data:image/jpeg;base64,{encoded_image}'
    else:
        print("Error: Unable to capture video frame")
        return None  # Handle error gracefully (optional)


# Update the video element to use the get_video_frame function
meowmidwest_img = html.Iframe(src=get_video_frame(), style={'width': '800px', 'height': '500px'})

meowmidwest_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([meowmidwest_img]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel"  # ,  

        ),
    ]
)
meowmidwest_item.style = {'gridArea': "meowmidwest_item"}
menu_income = [
    {'label': '1 - Less than $10,000', 'value': 1},
    {'label': '2 - Less than $15,000 ($10,000 to less than $15,000)', 'value': 2},
    {'label': '3 - Less than $20,000 ($15,000 to less than $20,000)', 'value': 3},
    {'label': '4 - Less than $25,000 ($20,000 to less than $25,000)', 'value': 4},
    {'label': '5 - Less than $35,000 ($25,000 to less than $35,000)', 'value': 5},
    {'label': '6 - Less than $50,000 ($35,000 to less than $50,000)', 'value': 6},
    {'label': '7 - Less than $75,000 ($50,000 to less than $75,000)', 'value': 7},
    {'label': '8 - $75,000 or more', 'value': 8}
]

# Define table header and data
header = html.Thead(
    html.Tr([html.Th("Midwest Meow Hospital hours: Sun-up to Sun-down")])  # Single header row with a single column
)

data_row = html.Tr([html.Td(doctorcat_item), html.Td(meowmidwest_item)])

# Create the table
mytable = html.Table([data_row])

#########################################################################################
#########################################################################################
##########                         Dropdown Section                                 #####
##########                          defined in the layout                           #####
##########                          added dropdown list values here                 #####
#########################################################################################
#########################################################################################

menu_income: [
    {'label': '1 - Less than $10,000', 'value': 1},
    {'label': '2 - Less than $15,000 ($10,000 to less than $15,000)', 'value': 2},
    {'label': '3 - Less than $20,000 ($15,000 to less than $20,000)', 'value': 3},
    {'label': '4 - Less than $25,000 ($20,000 to less than $25,000)', 'value': 4},
    {'label': '5 - Less than $35,000 ($25,000 to less than $35,000)', 'value': 5},
    {'label': '6 - Less than $50,000 ($35,000 to less than $50,000)', 'value': 6},
    {'label': '7 - Less than $75,000 ($50,000 to less than $75,000)', 'value': 7},
    {'label': '8 - $75,000 or more', 'value': 8}
]

gen_health = [
    {'label': '1 Excellent', 'value': 1},
    {'label': '2 Very good', 'value': 2},
    {'label': '3 Good', 'value': 3},
    {'label': '4 Fair', 'value': 4},
    {'label': '5 Poor', 'value': 5},
    {'label': '7 Don’t know/Not Sure', 'value': 7},
    {'label': '9 Refused', 'value': 7}

]
# number of days mental health not good
men_health = [
    {'label': '1: 1 - 30 Number of days ', 'value': 1},
    {'label': '2: 88 None ', 'value': 2},
    {'label': '3: 77 Don’t know/Not sure ', 'value': 3},
    {'label': '4: 99 Refused', 'value': 4},
    {'label': '5: BLANK Not asked or Missing', 'value': 5},

]
# numger of days phyical health not good
phy_health = [
    {'label': '1: 1 - 30 Number of days ', 'value': 1},
    {'label': '2: 88 None ', 'value': 2},
    {'label': '3: 77 Don’t know/Not sure ', 'value': 3},
    {'label': '4: 99 Refused', 'value': 4},
    {'label': '5: BLANK Not asked or Missing', 'value': 5},

]

# numger of days you have difficulty walking or climbing stairs
diff = [
    {'label': '1: 1 - 30 Number of days ', 'value': 1},
    {'label': '2: 88 None ', 'value': 2},
    {'label': '3: 77 Don’t know/Not sure ', 'value': 3},
    {'label': '4: 99 Refused', 'value': 4},
    {'label': '5: BLANK Not asked or Missing', 'value': 5},

]


#############################################################################
################## Layout Diff:  will hold the result of the prediction #####

############################################################################
################## Layout: Prediction VALUE message ########################
############################################################################


############################################################################
##################  RAW TABLE      ########################################
###########################################################################
# get the data
def create_raw_table(raw):
    df = raw.head()

    columns = []
    # columns = [{"name": "generalhealth_type",
    #            "id": "gentype", "type": "text"}]
    for name in raw.columns:
        col_info = {
            "name": name,
            "id": name,
            "type": "text",
            "format": {'specifier': ','}
        }
        columns.append(col_info)

    data = df.to_dict("records")
    return DataTable(
        id="raw-table",  # raw-table
        columns=columns,
        data=data,
        active_cell={"row": 0, "column": 0},
        fixed_rows={"headers": True},
        sort_action="native",
        derived_virtual_data=data,
        style_table={
            "minHeight": "30vh",
            "height": "40vh",
            "overflowX": "scroll",
            "borderRadius": "0px 0px 10px 10px",
        },
        style_cell={
            "whiteSpace": "normal",
            "height": "auto",
            "fontFamily": "verdana",
            "width": "50px",

        },
        style_header={
            "textAlign": "center",
            "fontSize": 14,
        },
        style_data={
            "fontSize": 12,
        },
        style_data_conditional=[
            {
                "if": {"column_id": "gentype"},
                "width": "420px",
                "textAlign": "left",
                "textDecoration": "underline",
                "cursor": "pointer",
            },

            {
                "if": {"column_id": "index"},
                "width": "50px",
                "textAlign": "left",
                "textDecoration": "underline",
                "cursor": "pointer",

            },
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#fafbfb"
            }
        ],
    )


raw = prepared_data.read_local_data('all', 'data/raw')

#################################################
### call create_table_method defined in prepare.py
###############################################
raw_table = create_raw_table(raw)

############################################################################
################   BORDER ITEM  ###########################################
###########################################################################

border1_img_path = "assets/border1.png"
border1_img = Image.open(border1_img_path)

border1_item = dbc.Row(
    [
        dbc.Col(
            [
                dbc.CardImg(src=border1_img, style={'width': '100%'}),
                # Add other components for sidebar and navbar here...
            ]
        )
    ]
)
border1_item.style = {'gridArea': "border1_item"}
############################################################################
################   Bullet Points  : html.Li(step) for step in steps  #######
###########################################################################


# Bullet Point data

steps = [
    "Import pandas",
    "Reading in Data",
    "Selected Columns",
    "Reset Index",
    "Identified no missing data",
    "Relationships between variables uisng heatmap"
]

tools_used = [
    "Git - source code management",
    "GitBash - terminal application used to push changes up to Github Repository",
    "Jupyter Notebook - web application used to create my documents",
    "Anaconda Prompt - used command line interface to manage my virutal environment and access Jupyter notebook",
    "TCPView - Used to identify and terminate apps running ports on local machine",
    "Pycharm -  Integrated Development Environment (IDE) used to launch my app to render",
    "Render - free web hosting service used to deploy my app to the web"

]

issues = [

    "box plot shows large variances and outliers in Mental Health and Physical Health Data.   outliers can be removed from the dataset prior to modeling. It is good practice to note specifically what outlier values were removed and why",
    "Outliers can be removed from the dataset prior to modeling. It is good practice to note specifically what outlier values were removed and why",
    " Data was note  data should form a bell shaped curve but skewed. How will you transform the skewed data so it is suitable for modeling"

]

treatment = [

    "1- Address Outliers using IQR method",
    "2- Replace codes with label for better interprepation of data",
    "3- Aggregrate data for graph"
]

#########################################################################################
##################    Exploring the Data SECTION ########################################
################                                          ##############################
################     exploredata_item, heatmap_item, boxplot_item       #################
#########################################################################################

#############################################################
################     exploredata_item        #################
###############################################################
exploredata_img_path = "assets/exploredata.png"
exploredata_img = Image.open(exploredata_img_path)
exploredata_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        # html.Img(src=banner_img, style={'width': '100%', 'height': '50%'})
                        html.Img(src=exploredata_img,
                                 style={'width': '800px', 'height': '600px', 'justify-content': 'center',
                                        'align-items': 'center'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)

exploredata_item.style = {'gridArea': "exploredata_item"}

############################################################
################     heatmap_item       ######################
###############################################################

heatmap_img_path = "assets/heatmap.PNG"
heatmap_img = Image.open(heatmap_img_path)
heatmap_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        # html.Img(src=banner_img, style={'width': '100%', 'height': '50%'})
                        html.Img(src=heatmap_img,
                                 style={'width': '800px', 'height': '600px', 'justify-content': 'center',
                                        'align-items': 'center'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)

heatmap_item.style = {'gridArea': "heatmap_item"}

############################################################
################     boxplot_item       ######################
###############################################################
boxplot_img_path = "assets/boxplot.PNG"
boxplot_img = Image.open(boxplot_img_path)
boxplot_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        html.Img(src=boxplot_img,
                                 style={'width': '800px', 'height': '600px', 'justify-content': 'center',
                                        'align-items': 'center'})
                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)

boxplot_item.style = {'gridArea': "boxplot_item"}

#########################################################################################
##################    Feature Engineered & Aggregated data SECTION        ###############
##################                 outliers_item , updatecolumns , updated_table ########
#########################################################################################

############################################################
################     outliers_item       ######################
###############################################################
outliers_img_path = "assets/outliers.png"
outliers_img = Image.open(outliers_img_path)
outliers_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        # html.Img(src=banner_img, style={'width': '100%', 'height': '50%'})
                        html.Img(src=outliers_img,
                                 style={'width': '800px', 'height': '600px', 'justify-content': 'center',
                                        'align-items': 'center'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)

outliers_item.style = {'gridArea': "outliers_item"}

############################################################
################     updatecolumns_item       ################
###############################################################
updateColumns_img_path = "assets/updateColumns.png"
updateColumns_img = Image.open(updateColumns_img_path)

updatecolumns_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        # html.Img(src=banner_img, style={'width': '100%', 'height': '50%'})
                        html.Img(src=updateColumns_img,
                                 style={'width': '800px', 'height': '600px', 'justify-content': 'center',
                                        'align-items': 'center'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)

updatecolumns_item.style = {'gridArea': "updatecolumns_item"}


##############################################################
################     updated table       ######################
###############################################################
def create_updated_table(df):
    df = df.head()

    columns = []

    for name in df.columns:
        col_info = {
            "name": name,
            "id": name,
            "type": "text",
            "format": {'specifier': ','}
        }
        columns.append(col_info)

    data = df.to_dict("records")
    return DataTable(
        id="updated-table",  # updated-table
        columns=columns,
        data=data,
        active_cell={"row": 0, "column": 0},
        fixed_rows={"headers": True},
        sort_action="native",
        derived_virtual_data=data,
        style_table={
            "minHeight": "30vh",
            "height": "40vh",
            "overflowX": "scroll",
            "borderRadius": "0px 0px 10px 10px",
        },
        style_cell={
            "whiteSpace": "normal",
            "height": "auto",
            "fontFamily": "verdana",
            "width": "50px",

        },
        style_header={
            "textAlign": "center",
            "fontSize": 14,
        },
        style_data={
            "fontSize": 12,
        },
        style_data_conditional=[
            {
                "if": {"column_id": "gentype"},
                "width": "420px",
                "textAlign": "left",
                "textDecoration": "underline",
                "cursor": "pointer",
            },

            {
                "if": {"column_id": "index"},
                "width": "50px",
                "textAlign": "left",
                "textDecoration": "underline",
                "cursor": "pointer",

            },
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#fafbfb"
            }
        ],
    )


df_prep = prepared_data.read_local_data('all', "data/prepared")
updated_table = create_updated_table(df_prep)

#########################################################################################
##################    Aggregate and view Bar chart percentage   #########################
####                                                                                ####
####          graph_01, summary_table,(id='graph-output,analysis_graph_figure       ####
####                                                                                ###
#########################################################################################

############################################################
################     graph_01               ################
##############################################################
df = prepared_data.read_local_data('all', 'data/prepared')
summary = prepared_data.create_dataframe_from_counts_part2(df, 'GeneralHealth', 'Type')
summary = summary.reset_index()

circle_fig = px.pie(summary, values='count', names='percentage', title='Distribution of Health by Type')  # No filtering

graph_01 = dcc.Graph(figure=circle_fig, style={'gridArea': "graph_01"})


##############################################################
################     summary_table           ################
#############################################################
def create_sum_table(summary):
    used_columns = ["index", "combined", "count", "percentage", "GeneralHealth", "Type"]
    df = summary[used_columns]
    df = df.rename(columns={"combined": "generalhealth_type", "count": "total"})
    columns = []
    # columns = [{"name": "generalhealth_type",
    #            "id": "gentype", "type": "text"}]
    for name in df.columns:
        col_info = {
            "name": name,
            "id": name,
            "type": "text",
            "format": {'specifier': ','}
        }
        columns.append(col_info)



    data = df.sort_values("total", ascending=False).to_dict("records")
    return DataTable(
        id="sum-table",  # sum-table
        columns=columns,
        data=data,
        active_cell={"row": 0, "column": 0},
        fixed_rows={"headers": True},
        sort_action="native",
        derived_virtual_data=data,
        style_table={
            "minHeight": "80vh",
            "height": "40vh",
            "overflowY": "scroll",
            "borderRadius": "0px 0px 10px 10px",
        },
        style_cell={
            "whiteSpace": "normal",
            "height": "auto",
            "fontFamily": "verdana",
        },
        style_header={
            "textAlign": "center",
            "fontSize": 14,
        },
        style_data={
            "fontSize": 12,
        },
        style_data_conditional=[
            {
                "if": {"column_id": "gentype"},
                "width": "420px",
                "textAlign": "left",
                "textDecoration": "underline",
                "cursor": "pointer",
            },

            {
                "if": {"column_id": "index"},
                "width": "70px",
                "textAlign": "left",
                "textDecoration": "underline",
                "cursor": "pointer",
            },
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#fafbfb"
            }
        ],
    )


summary_table = create_sum_table(summary)

############################################################
################     graph-output      -- OUTPUT     ################
###############################################################


##############################################################
################     analysis_graph_figure      ##############
###############################################################

analysis_graph = prepared_data.create_dataframe_counts_specificGenH_fig(df, 'Very good', 'diabetic')

analysis_graph_figure = dcc.Graph(figure=analysis_graph, id="analysis_graph_figure",
                                  style={'gridArea': "analysis_graph_figure"})

#########################################################################################
##################    PREDICTION MODELING SECTION #######################################
#########################################################################################

Model_img_path = "assets/Model.png"
Model_img = Image.open(Model_img_path)

Model_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        html.Img(src=Model_img, style={'width': '800px', 'height': '600px', 'justify-content': 'center',
                                                       'align-items': 'center'})

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)

Model_item.style = {'gridArea': "Model_item"}

#########################################################################################
#######     Create Test program to accept user input and display prediction SECTION  ####
######                        programlink, mytable2  : prediction code.PNG and code.mp4 #
#########################################################################################

programlink = html.A('Python Program Making Prediction',
                     href="https://github.com/yourexodus/capstone_CDC/blob/4b4f4f3c0933f6968cb9b2651c8c35f3f5372d1f/Prediction_Menu.py")

##############################################
predictionCode_img_path = "assets/predictionCode.png"
predictionCode_img = Image.open(predictionCode_img_path)
predictionCode_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([

                        html.Img(src=predictionCode_img,
                                 style={'width': '100%', 'height': '500px', 'justify-content': 'center',
                                        'align-items': 'center'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)
predictionCode_item.style = {'gridArea': "predictionCode_item"}
##############################################################

code_img = html.Iframe(src=get_video_frame(), style={'width': '400px', 'height': '500px'})

code_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([code_img]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel", #  

        ),
    ]
)
code_item.style = {'gridArea': "code_item"}

##############################################################
################     mytable2                   ##############
###############################################################

# Define table header and data
header = html.Thead(
    html.Tr([html.Th("Test")])  # Single header row with a single column
)

data_row2 = html.Tr([html.Td(predictionCode_item), html.Td(code_item)])  # Single data row with two cells

# Create the table
mytable2 = html.Table([data_row2])

########################################################################################
##############         TESTING PROGRAM                    ##############################
#########################################################################################

flowchart_img_path = "assets/flowchart.png"
flowchart_img = Image.open(flowchart_img_path)

flowchart_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div([
                        # html.Img(src=banner_img, style={'width': '100%', 'height': '50%'})
                        html.Img(src=flowchart_img, style={'width': '500px', 'height': '300px'})
                        # html.Img(src=banner_img, 'width': '50%', 'height': '200px'),               # using the pillow image variable

                    ]),
                    html.Div(className="sidebar-wrapper"),
                ]
            ),
            className="sidebar",
        ),
        html.Div(
            html.Div(
                html.Div(className="container-fluid"),
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ",
            ),
            className="main-panel",
        ),
    ]
)
flowchart_item.style = {'gridArea': "flowchart_item"}
#########################################################################################

#########################################################################################
##################    LAYOUT SECTION ####################################################
#########################################################################################

# layout is saved to a variable so I dont have to keep running it
app.layout = html.Div([
    link,
    banner_item,
    mytable,  # add doctor cat
    ########################################################
    ############# Prediction output ######################

    html.Div(
        children=[
            html.H3(
                "Note: drop downs are in a persistence state.  click new values in all the fields to populate a prediction.  The last field will calls the prediction.  It can take a copule minutes  to display")
        ])
    ,
    ########################################################################################################
    ################## Define input and out for income drop down ###########################################
    #######################################################################################################

    html.Div(
        children=[
            'Please choose your income range.:', dcc.Dropdown(
                id='menu_income_id',
                options=menu_income,
                placeholder="Please choose your income range.",
                value=user_input_value,
                persistence=True,  # store user dropdown
            )
        ],
        style={
            "display": "block"
        }
    ),
    ######################################################################
    ##################  OUTPUT VALUE for income #######################

    html.Div(id='income-output'),

    #################################################################################################
    ###########  gen_health  ########################################################################
    ################################################################################################
    html.Div(  # Assuming user_input1 is a Div
        children=[
            "Please enter your general health code:", dcc.Dropdown(
                id='gen_health_id',
                options=gen_health,
                placeholder="Please enter your general health code.",
                value=user_input_value,
                persistence=True,  # store user dropdown
            )
        ],
        style={
            "display": "block",  # Set display to block
        }
    ),
    ######################################################################
    ##################  OUTPUT VALUE for general health #######################

    html.Div(id='gen-health-output'),

    ################################################################################################
    html.Div(
        children=[
            "Please choose your physical health code:", dcc.Dropdown(
                id='phy_health_id',
                options=phy_health,
                placeholder="Please choose your physical health code.",
                value=user_input_value,
                persistence=True,  # store user dropdown
            )
        ],
        style={
            "display": "block"
        }
    ),
    ######################################################################
    ##################  OUTPUT VALUE for physical health days #######################

    html.Div(id='phy-health-output'),

    ################################################################################################
    html.Div(
        children=[
            "Please choose your physical health range:", dcc.Dropdown(
                id='men_health_id',
                options=men_health,
                placeholder="Please choose your physical health range.",
                value=user_input_value,
                persistence=True,  # store user dropdown
            )
        ],
        style={
            "display": "block"
        }
    ),
    ######################################################################
    ##################  OUTPUT VALUE for mental health #######################

    html.Div(id='men-health-output'),

    #################################
    html.Div(
        children=[
            "Please choose number of days you had diffculty walking:", dcc.Dropdown(
                id='diff_id',
                options=phy_health,
                placeholder="Please choose number of days you had diffculty walking.",
                value=user_input_value,
                persistence=True,  # store user dropdown
            )
        ],
        style={
            "display": "block"
        }
    ),
    ######################################################################
    ##################  OUTPUT VALUE for income #######################
    html.Div(
        children=[
            html.H2(id='diff-output')
        ])

    # html.Div(id='diff-output')

    ,
    html.Div(id='prediction-output')
    ,

    html.Br(),
    html.Br(),
    ################################
    border1_item,
    ###############################################
    #########  About the Data ######################
    ##############################################

    html.Div(
        children=[
            html.H1("Capstone: CDC Diabetes Project")
        ])
    ,
    html.Div(
        children=[
            html.P(
                "This is the result of a Logcial Regression Capstone Project used to determine the probability of diabetes based select features.  My desire is to use this capstone to demonstrate skills in the areas of data science, machine learning, and python to predict and outcome using data analysis.")
        ])
    ,
    html.Div(
        children=[
            html.H2("About the Data"),
            html.P(
                '"The Diabetes Health Indicators Dataset contains healthcare statistics and lifestyle survey information about people in general along with their diagnosis of diabetes. -- source: Machine learning repository"'),
            html.A('Available Data', "https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators"),
            html.A('CDC data Codes', "https://www.cdc.gov/brfss/annual_data/2014/pdf/CODEBOOK14_LLCP.pdf"),

        ])
    ,
    html.Div(
        children=[
            html.H3("Raw data")
        ])
    ,
    html.Div([raw_table])
    ,
    border1_item
    ,
    html.Div(
        children=[
            html.H2("Step 1: Explored the Data")
        ])
    ,

    html.Div([
        html.Ul([
            html.Li(step) for step in steps
        ])
    ])

    ,
    html.Div(
        children=[
            html.H3("Identified issues with the data")
        ])

    ,

    html.Div([exploredata_item, heatmap_item])
    ,
    html.Div([
        html.Ul([
            html.Li(step) for step in issues
        ])
    ])
    ,

    html.Div([boxplot_item])

    ,
    html.Div(
        children=[
            html.A(
                "box plot shows large variances and outliers in Mental Health and Physical Health Data. This can affect my model performance.  Also, since the data is categorical data, I will use a categorical response to determine the probability of diabetes based the most prominent features identified in my heatmap. According to the stats, there is a 30point difference from min and max for Mental and Physical Health data")
        ])

    ,
    border1_item
    ,
    html.Div(
        children=[
            html.H2("Step 2: Feature Engineered & Aggregated data")
        ])
    ,

    html.Div(
        children=[
            html.H3("Purpose of this Section:")
        ])
    ,
    html.Div([
        html.Ul([
            html.Li(step) for step in treatment
        ])
    ])

    ,

    html.Div(
        children=[
            html.H3("Address Outliers using IQR method")
        ])

    ,

    html.Div([outliers_item])

    ,

    html.Div(
        children=[
            html.A(
                "I identied 14% percent of the records are outliers using IQP the lower & upper bounds in the MentHlth data.  I identied 19% percent of the records are outliers using IQP the lower & upper bounds in the PhysHlth data")
        ])

    ,
    html.Div(
        children=[
            html.H3("Replace codes with label for better interprepation of data")
        ])

    ,
    html.Div([updatecolumns_item])

    ,
    html.Div(
        children=[
            html.H3("Top 4 header rows of updated data table")
        ])
    ,
    html.Div([updated_table])
    ,
    html.Div(
        children=[
            html.H3("Aggregate and view Bar chart percentage")
        ])
    ,

    html.Div([graph_01])
    ,
    html.Div(
        children=[
            html.H3(
                "The 3 Interactive Graphs will update to match your row selection on the summary table to provide additional insights on the data for each row")
        ])

    ,
    html.Div([summary_table])
    ,
    html.Div(id='graph-output')
    ,
    html.Div([analysis_graph_figure])
    ,
    border1_item

    ,

    html.Div(
        children=[
            html.H2("Step 3: Create Predictive models")
        ])
    ,

    html.Div(
        children=[
            html.H3("Nominal Classification Problem: Predict diabetis for a customer.")
        ])
    ,
    html.Div(
        children=[
            html.A(
                "Tested out several feature combination using Test Train Split method. Select the best accuracy score"),

        ])

    ,
    html.Div(
        children=[
            html.A("Feature columns are cols =['Income','GenHlth','MentHlth','PhysHlth','DiffWalk']"),

        ])

    ,
    html.Div(
        children=[
            html.H4("Target column is y  = df['Diabetes_binary']")
        ])
    ,

    html.Div([Model_item])
    ,
    border1_item
    ,

    html.Div(
        children=[
            html.H2("Step 5: Create Test program to accept user input and display prediction")
        ])
    ,
    programlink
    ,
    mytable2  # html.Div(programvideo_div)
    ,
    border1_item
    ,

    html.Div(
        children=[
            html.H2("Step 5: Build the app")
        ])
    ,
    html.Div([flowchart_item])
    ,

    border1_item
    ,
    html.Div(
        children=[
            html.H2("Summary Tools Used")
        ])
    ,

    html.Div([
        html.Ul([
            html.Li(step) for step in tools_used
        ])
    ])

    ,
], style={'padding': 10})


#########################################
############ call back for income drop down
###############################

@app.callback(
    Output('income-output', 'children'),
    [Input('menu_income_id', 'value')]

)
def callback_a(income_value):
    # Access and use the global variable here
    # For example:

    return f"You've selected: {income_value}"


#################################################3
########### call back for gen health ###########
#########################
@app.callback(
    Output('gen-health-output', 'children'),
    [Input('gen_health_id', 'value')]
)
def callback_b(gen_health_value):
    gl_gen_health = gen_health_value
    return 'Youve selected "{}"'.format(gen_health_value)


#################################################
###### call back for phy health
############################################
@app.callback(
    Output('phy-health-output', 'children'),
    [Input('phy_health_id', 'value')]
)
def callback_c(phy_health_value):
    gl_phy_health = phy_health_value
    return 'Youve selected "{}"'.format(phy_health_value)


#################################################
###### call back for phy health
############################################
@app.callback(
    Output('men-health-output', 'children'),
    [Input('men_health_id', 'value')]
)
def callback_d(men_health_value):
    gl_men_health = men_health_value
    return 'Youve selected "{}"'.format(men_health_value)


#################################################
###### call back for phy health
############################################

@app.callback(
    Output('diff-output', 'children'),
    [Input('diff_id', 'value')],
    [State('menu_income_id', 'value')],  # Add menu_income_id as a State
    [State('gen_health_id', 'value')],  # Add gen_health_id as a State
    [State('phy_health_id', 'value')],  # Add phy_health_id as a State
    [State('men_health_id', 'value')]  # Add men_health_id as a State
)
def callback_e(diff_value, menu_income_id, gen_health_id, phy_health_id, men_health_id):
    # Access and use the variables here
    if not all([menu_income_id, gen_health_id, phy_health_id, men_health_id, diff_value]):
        return 'Youve selected "{}"'.format(diff_value)
    all_input_data = [menu_income_id, gen_health_id, phy_health_id, men_health_id, diff_value]
    # label = prepared_data.get_label_by_value(menu_income, value_to_find)
    result = prepared_data.make_prediction(all_input_data)

    return result + ".  Refresh your browser to start again"


###########################################################################
####### Call back for graphs
########################################################################
@app.callback(
    Output("analysis_graph_figure", "figure"),
    Input('sum-table', 'active_cell'),
    State('sum-table', 'derived_virtual_data')
)
def change_area_graphs(sum_cell, sum_data):
    ##    """
    ##  Change the all three graphs in the upper right hand corner of the app
    #   Parameters
    #    ----------
    ##    avg_cell : dict with keys `row` and `cell` mapped to integers of cell location
    #   avg_data : list of dicts of one country per row.
    #                    Has keys Country, Deaths, Cases, Deaths per Million, Cases per Million
    #   Returns
    #    -------
    #    List of three plotly figures, one for each of the `Output`
    #    """
    row_number = sum_cell["row"]
    row_data = sum_data[row_number]

    fig = prepared_data.create_dataframe_counts_specificGenH_fig(df, row_data["GeneralHealth"], row_data["Type"])
    return fig




#############################################
if __name__ == '__main__':
    app.run(debug=True, port=8054)
