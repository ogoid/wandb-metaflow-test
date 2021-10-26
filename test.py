from wandb.integration.metaflow import wandb_log
from metaflow import FlowSpec, step

@wandb_log
class TestFlow(FlowSpec):

  @step
  def start(self):
    self.next(self.end)

  @step
  def end(self):
    pass


if __name__ == '__main__':
    TestFlow()
