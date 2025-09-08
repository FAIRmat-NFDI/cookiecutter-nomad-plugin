from nomad.actions import TaskQueue
from pydantic import Field
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from nomad.config.models.plugins import ActionEntryPoint

class SimpleActionEntryPoint(ActionEntryPoint):
    task_queue: str = Field(
        default=TaskQueue.CPU, description='Determines the task queue for this action'
    )

    def load(self):
        from nomad.actions import Action
        from {{cookiecutter.module_name}}.actions.simple_action.workflows import SimpleWorkflow
        from {{cookiecutter.module_name}}.actions.simple_action.activities import greet

        return Action(
            task_queue=self.task_queue,
            workflow=SimpleWorkflow,
            activities=[greet],
        )


simple_action = SimpleActionEntryPoint(
    name='SimpleAction',
    description='A simple action that returns a greeting.',
)
