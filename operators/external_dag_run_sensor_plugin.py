from airflow.plugins_manager import AirflowPlugin
from airflow import DAG, settings
from airflow.operators import BashOperator, PythonOperator, BaseSensorOperator
from datetime import timedelta, datetime
from airflow.utils.state import State
from airflow.utils.decorators import apply_defaults
from airflow.models import DagRun
import logging


class ExternalDagRunSensor(BaseSensorOperator):
    @apply_defaults
    def __init__(
            self,
            external_dag_id,
            allowed_states=None,
            execution_delta=None,
            execution_date_fn=None,
            *args, **kwargs):
        super(ExternalDagRunSensor, self).__init__(*args, **kwargs)
        self.allowed_states = allowed_states or [State.RUNNING]
        if execution_delta is not None and execution_date_fn is not None:
            raise ValueError(
                'Only one of `execution_date` or `execution_date_fn` may'
                'be provided to ExternalDagRunSensor; not both.')

        self.execution_delta = execution_delta
        self.execution_date_fn = execution_date_fn
        self.external_dag_id = external_dag_id

    def poke(self, context):
        if self.execution_delta:
            dttm = context['execution_date'] - self.execution_delta
        elif self.execution_date_fn:
            dttm = self.execution_date_fn(context['execution_date'])
        else:
            dttm = context['execution_date']

        logging.info(
            'Poking for '
            '{self.external_dag_id} on '
            '{dttm} ... '.format(**locals()))

        session = settings.Session()
        count = session.query(DagRun).filter(
            DagRun.dag_id == self.external_dag_id,
            DagRun.state.in_(self.allowed_states),
            DagRun.execution_date <= dttm,
        ).count()
        session.commit()
        session.close()
        if count == 0:
            return True
        else:
            return False


class ExternalDagRunSensor_Plugin(AirflowPlugin):
    name = "ExternalDagRunSensor"
    operators = [ExternalDagRunSensor]
