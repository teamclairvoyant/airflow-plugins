# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
