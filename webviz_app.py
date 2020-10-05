#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AUTOMATICALLY MADE FILE. DO NOT EDIT.
# This file was generated by ingeknudsen on 2020-09-07.

import logging
import threading
import datetime
import os.path as path
from pathlib import Path, PosixPath, WindowsPath

import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_talisman import Talisman
import webviz_config
import webviz_config.certificate
from webviz_config.themes import installed_themes
from webviz_config.common_cache import CACHE
from webviz_config.webviz_store import WebvizStorage, WEBVIZ_STORAGE
from blob_storage.webviz_blob_store import WEBVIZ_BLOB_STORAGE
from webviz_config.webviz_assets import WEBVIZ_ASSETS

import webviz_config.plugins as standard_plugins


# We do not want to show INFO regarding werkzeug routing as that is too verbose,
# however we want other log handlers (typically coming from webviz plugin dependencies)
# to be set to user specified log level.
logging.getLogger("werkzeug").setLevel(logging.WARNING)
logging.getLogger().setLevel(logging.WARNING)

theme = webviz_config.WebvizConfigTheme("equinor")
theme.from_json((Path(__file__).resolve().parent / "theme_settings.json").read_text())

app = dash.Dash(__name__, external_stylesheets=theme.external_stylesheets)
app.logger.setLevel(logging.WARNING)
server = app.server

app.title = "Reek Webviz Example"
app.config.suppress_callback_exceptions = True

app.webviz_settings = {
    "shared_settings": webviz_config.SHARED_SETTINGS_SUBSCRIPTIONS.transformed_settings(
        {'scratch_ensembles': {'sens_run': '../reek_fullmatrix/realization-*/iter-0', 'iter-0': '../reek_history_match/realization-*/iter-0', 'iter-1': '../reek_history_match/realization-*/iter-1', 'iter-2': '../reek_history_match/realization-*/iter-2', 'iter-3': '../reek_history_match/realization-*/iter-3'}}, PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/webviz_examples'), True
    ),
    "portable": True,
    "theme": theme,
}

CACHE.init_app(server)

Talisman(server, content_security_policy=theme.csp, feature_policy=theme.feature_policy)

WEBVIZ_STORAGE.get_stored_data = WEBVIZ_BLOB_STORAGE.get_stored_data
WEBVIZ_STORAGE.get_stored_data = WEBVIZ_BLOB_STORAGE.get_stored_data
WEBVIZ_STORAGE.use_storage = True
WEBVIZ_STORAGE.storage_folder = path.join(
    path.dirname(path.realpath(__file__)), "webviz_storage"
)

WEBVIZ_ASSETS.portable = True

if False and not webviz_config.is_reload_process():
    # When Dash/Flask is started on localhost with hot module reload activated,
    # we do not want the main process to call expensive component functions in
    # the layout tree, as the layout tree used on initialization will anyway be called
    # from the child/restart/reload process.
    app.layout = html.Div()
else:
    app.layout = dcc.Tabs(
        parent_className="layoutWrapper",
        content_className="pageWrapper",
        vertical=True,
        children=[
          
            dcc.Tab(id="logo",
                className="styledLogo",children=[
                  standard_plugins.BannerImage(**{'image': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/webviz_examples/content/reek_image.jpg'), 'title': 'Reek FMU Webviz example'}).plugin_layout(contact_person=None),
                  standard_plugins.Markdown(**{'markdown_file': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/webviz_examples/content/front_page.md')}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="how_was_this_made",label="How was this made?",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.Markdown(**{'markdown_file': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/webviz_examples/content/how_was_this_made.md')}).plugin_layout(contact_person=None),
                  standard_plugins.SyntaxHighlighter(**{'filename': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/webviz_examples/webviz-full-demo.yml'), 'dark_theme': True}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="sensitivity_study_inplace",label="Sensitivity study (inplace)",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.InplaceVolumesOneByOne(app=app, **{'ensembles': ['sens_run'], 'volfiles': {'geogrid': 'geogrid--oil.csv', 'simgrid': 'simgrid--oil.csv'}}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="sensitivity_study_time_series",label="Sensitivity study (time series)",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.ReservoirSimulationTimeSeriesOneByOne(app=app, **{'ensembles': ['sens_run'], 'initial_vector': 'FOPT'}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="inplace_volumes",label="Inplace volumes",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.InplaceVolumes(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'volfiles': {'geogrid': 'geogrid--oil.csv', 'simgrid': 'simgrid--oil.csv'}}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="simulation_time_series",label="Simulation time series",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.ReservoirSimulationTimeSeries(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'obsfile': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/share/observations/observations.yml'), 'options': {'vector1': 'WOPR:OP_1', 'visualization': 'statistics'}}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="regional_simulation_time_series",label="Regional simulation time series",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.ReservoirSimulationTimeSeriesRegional(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'fipfile': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/share/regions/fip.yaml')}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="reservoir_simulation_map",label="Reservoir simulation map",
                selected_className="selectedButton",
                className="styledButton",children=[
                  dcc.Markdown(r"""In this example, the horizontal permeability is shown together with oil fluid flow for a given date during simulation."""),
                  standard_plugins.SubsurfaceMap(app=app, **{'ensemble': 'iter-0', 'map_value': 'PERMX', 'flow_value': 'FLROIL', 'time_step': 2}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="parameter_distribution",label="Parameter distribution",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.ParameterDistribution(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3']}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="correlation_between_input_parameters_and_responses",label="Correlation between input parameters and responses",
                selected_className="selectedButton",
                className="styledButton",children=[
                  dcc.Markdown(r"""# Correlation between input parameters and inplace volumes"""),
                  standard_plugins.ParameterResponseCorrelation(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'response_file': 'share/results/volumes/geogrid--oil.csv', 'response_filters': {'ZONE': 'multi', 'REGION': 'multi'}}).plugin_layout(contact_person=None),
                  dcc.Markdown(r"""# Correlation between input parameters and time series"""),
                  standard_plugins.ParameterResponseCorrelation(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'response_file': 'share/results/tables/unsmry--monthly.csv', 'response_filters': {'DATE': 'single'}}).plugin_layout(contact_person=None),
                  dcc.Markdown(r"""# Pairwise correlation between all input parameters"""),
                  standard_plugins.ParameterCorrelation(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3']}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="history_match_iknu_test",label="History match (IKNU Test)",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.HistoryMatch(app=app, **{'observation_file': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/share/observations/observations.yml'), 'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3']}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="relative_permeability",label="Relative permeability",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.RelativePermeability(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'relpermfile': 'share/results/tables/relperm.csv', 'scalfile': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/share/scal/scalreek.csv')}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="parameter_parallel_coordinates",label="Parameter parallel coordinates",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.ParameterParallelCoordinates(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3']}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="seg-y_viewer",label="SEG-Y viewer",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.SegyViewer(app=app, **{'segyfiles': [PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/observed_data/seismic/syntseis_20000101_seismic_depth_stack.segy'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/observed_data/seismic/syntseis_20030101_seismic_depth_stack.segy')]}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="surface_with_seismic_cross-section",label="Surface with seismic cross-section",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.SurfaceWithSeismicCrossSection(app=app, **{'segyfiles': [PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/observed_data/seismic/syntseis_20000101_seismic_depth_stack.segy'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/observed_data/seismic/syntseis_20030101_seismic_depth_stack.segy')], 'surfacefiles': [PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_fullmatrix/realization-0/iter-0/share/results/maps/topupperreek--ds_extracted_horizons.gri'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_fullmatrix/realization-0/iter-0/share/results/maps/topmidreek--ds_extracted_horizons.gri'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_fullmatrix/realization-0/iter-0/share/results/maps/toplowerreek--ds_extracted_horizons.gri'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_fullmatrix/realization-0/iter-0/share/results/maps/baselowerreek--ds_extracted_horizons.gri')], 'surfacenames': ['Top Upper Reek', 'Top Middle Reek', 'Top Lower Reek', 'Base Lower Reek']}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="surface_with_grid_cross-section",label="Surface with grid cross-section",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.SurfaceWithGridCrossSection(app=app, **{'gridfile': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/grids/geogrid.roff'), 'gridparameterfiles': [PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/grids/geogrid--poro.roff'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/grids/geogrid--perm.roff'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/grids/geogrid--facies.roff')], 'surfacefiles': [PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/maps/topupperreek--ds_extracted_horizons.gri'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/maps/topmidreek--ds_extracted_horizons.gri'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/maps/toplowerreek--ds_extracted_horizons.gri'), PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/realization-0/iter-0/share/results/maps/baselowerreek--ds_extracted_horizons.gri')], 'surfacenames': ['Top Upper Reek', 'Top Middle Reek', 'Top Lower Reek', 'Base Lower Reek']}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="surface_viewer_fmu",label="Surface viewer (FMU)",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.SurfaceViewerFMU(app=app, **{'ensembles': ['iter-0', 'iter-3'], 'wellfolder': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/observed_data/wells'), 'attribute_settings': {'stoiip': {'min': 0, 'max': 2, 'color': 'inferno'}}}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="well_cross-section_fmu",label="Well cross-section (FMU)",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.WellCrossSectionFMU(app=app, **{'ensembles': ['iter-0', 'iter-3'], 'wellfolder': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/observed_data/wells'), 'surfacefiles': ['topupperreek--ds_extracted_horizons.gri', 'topmidreek--ds_extracted_horizons.gri', 'toplowerreek--ds_extracted_horizons.gri', 'baselowerreek--ds_extracted_horizons.gri'], 'surfacenames': ['Top Upper Reek', 'Top Middle Reek', 'Top Lower Reek', 'Base Lower Reek'], 'zonelog': 'Zonelog', 'zmin': 1500.0, 'zmax': 1700.0, 'marginal_logs': ['Poro', 'Perm'], 'nextend': 20}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="rft_plotter",label="RFT plotter",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.RftPlotter(app=app, **{'ensembles': ['iter-0', 'iter-1', 'iter-2', 'iter-3'], 'formations': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/share/results/tables/formations.csv'), 'faultlines': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/reek_history_match/share/results/polygons/faultpolygons.csv')}).plugin_layout(contact_person=None)
                  ],
            ),
            dcc.Tab(id="last_page",label="Horizon Uncertainty Viewer",
                selected_className="selectedButton",
                className="styledButton",children=[
                  standard_plugins.HorizonUncertaintyViewer(app=app, **{'basedir': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/horizon_uncertainty_data/simple_model'), 'planned_wells_dir': PosixPath('/Users/ingeknudsen/Documents/equinor/repos/webviz-subsurface-testdata/horizon_uncertainty_data/additional_wells')}).plugin_layout(contact_person=None)
                  ],
            )],
    )



if __name__ == "__main__":
    # This part is ignored when the webviz app is started
    # using Docker container and uwsgi (e.g. when hosted on Azure).
    #
    # It is used only when directly running this script with Python,
    # which will then initialize a localhost server.

    port = webviz_config.utils.get_available_port(preferred_port=5000)

    token = webviz_config.LocalhostToken(app.server, port).one_time_token
    webviz_config.utils.LocalhostOpenBrowser(port, token)

    webviz_config.utils.silence_flask_startup()

    app.run_server(
        host="localhost",
        port=port,
        ssl_context=webviz_config.certificate.LocalhostCertificate().ssl_context,
        debug=False,
        use_reloader=False,
        dev_tools_prune_errors=False,
      
    )
