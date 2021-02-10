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
__author__ = 'AravindBoppana'

from airflow.plugins_manager import AirflowPlugin
from airflow.operators.bash_operator import BashOperator
from airflow.utils import apply_defaults
import logging


class BashImpersonateOperator(BashOperator):
    """
     BashImpersonateOperator

     :param bash_command:                   The Bash command that needs to be executed as Impersonated User.
     :type bash_command:                    string

     :param impersonate_as_user:            Run as User.
     :type impersonate_as_user:             string
     """

    @apply_defaults
    def __init__(
            self,
            bash_command,
            impersonate_as_user,
            *args, **kwargs):
        self.impersonated_bash_command = ""
        super(BashImpersonateOperator, self).__init__(bash_command=self.impersonated_bash_command, *args, **kwargs)
        self.bash_command = bash_command
        self.impersonate_as_user = impersonate_as_user

    def execute(self, context):
        logging.info("Executing BashImpersonateOperator.execute(context)")

        self.bash_command = "sudo -u " + str(self.impersonate_as_user) + " -- sh -c '" + str(self.bash_command) + "'"

        logging.info("Finished assembling bash_command in BashImpersonateOperator: " + str(self.bash_command))

        logging.info("Executing bash execute statement")
        super(BashImpersonateOperator, self).execute(context)

        logging.info("Finished executing BashImpersonateOperator.execute(context)")


# Defining the plugin class
class BashImpersonateOperatorPlugin(AirflowPlugin):
    name = "bash_impersonate_operator"
    operators = [BashImpersonateOperator]
