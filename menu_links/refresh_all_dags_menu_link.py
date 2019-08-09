__author__ = 'robertsanders'

from airflow.plugins_manager import AirflowPlugin
from flask_admin.base import MenuLink

"""
Provides a Menu Link under the Admin tab in the Web Server to allow you to Refresh All DAGs at Once
"""

refresh_all_dags_menu_link = MenuLink(
    category='Admin',
    name='Refresh All DAGs',
    url='/admin/airflow/refresh_all')


# Defining the plugin class
class RefreshAllDagsLinkPlugin(AirflowPlugin):
    name = "refresh_all_dags_link"
    menu_links = [refresh_all_dags_menu_link]
