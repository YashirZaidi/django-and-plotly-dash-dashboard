from django.shortcuts import render
import pandas as pd
import plotly.express as px
from plotly.io import to_html

# Updated dataset
data_extended = {
    "project_name": ["areoone", "aliwee", "notie app", "project4", "project5", "project6", "project7", "project8", "project9", "project10"],
    "project_type": ["ecomerce app", "flutter web", "shopping app", "mobile app", "web app", "ecomerce app", "flutter web", "shopping app", "mobile app", "web app"],
    "manager_name": ["ali", "sarah", "ali", "john", "david", "ali", "sarah", "ali", "john", "david"],
    "project_milestones": [10, 5, 15, 8, 12, 10, 5, 15, 8, 12],
    "milstone_done_by_team": [6, 2, 10, 4, 7, 6, 2, 10, 8, 12],
    "completed": [False, False, False, False, False, False, True, True, True, True],
    "uiux": ["alice", "bob", "charlie", "david", "eve", "alice", "bob", "charlie", "david", "eve"],
    "graphic_designer": ["faythe", "grace", "heidi", "ivan", "judy", "faythe", "grace", "heidi", "ivan", "judy"],
    "front_end_developer": ["mallory", "nikki", "oscar", "peggy", "quinn", "mallory", "nikki", "oscar", "peggy", "quinn"],
    "back_end_developer": ["trent", "ursula", "victor", "wendy", "xavier", "trent", "ursula", "victor", "wendy", "xavier"]
}

df = pd.DataFrame(data_extended)

def get_project_type_dist(filtered_df):
    fig = px.bar(
        filtered_df,
        x="project_type",
        title="Project Distribution by Type",
        color_discrete_sequence=px.colors.sequential.Purples_r
    )
    fig.update_layout(
        plot_bgcolor='#2c2c54',
        paper_bgcolor='#2c2c54',
        font=dict(color='#fff')
    )
    return to_html(fig, full_html=False, include_plotlyjs="cdn")

def get_projects_by_manager(df):
    fig = px.bar(
        df,
        x="manager_name",
        title="Projects by Manager",
        color="manager_name",
        color_discrete_sequence=px.colors.sequential.Purples_r
    )
    fig.update_layout(
        plot_bgcolor='#2c2c54',
        paper_bgcolor='#2c2c54',
        font=dict(color='#fff')
    )
    return to_html(fig, full_html=False, include_plotlyjs="cdn")

def get_completion_status(filtered_df):
    fig = px.pie(
        filtered_df,
        names='completed',
        title='Project Completion Status',
        color_discrete_sequence=px.colors.sequential.Purples_r
    )
    fig.update_layout(
        plot_bgcolor='#2c2c54',
        paper_bgcolor='#2c2c54',
        font=dict(color='#fff')
    )
    return to_html(fig, full_html=False, include_plotlyjs="cdn")

def dashboard(request):
    selected_manager = request.GET.get('manager', 'ali')
    filtered_df = df[df["manager_name"] == selected_manager]

    total_projects = len(filtered_df)
    avg_milestones = round(filtered_df["project_milestones"].mean(), 2)
    completed_projects = filtered_df["completed"].sum()

    context = {
        'managers': df["manager_name"].unique().tolist(),
        'selected_manager': selected_manager,
        'total_projects': total_projects,
        'avg_milestones': avg_milestones,
        'completed_projects': completed_projects,
        'project_type_dist': get_project_type_dist(filtered_df),
        'projects_by_manager': get_projects_by_manager(df),
        'completion_status': get_completion_status(filtered_df),
    }
    return render(request, 'dashboard/dashboard.html', context)