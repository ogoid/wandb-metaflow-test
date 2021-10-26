
`python test.py run` fails with:

```
Warning: `pandas` not installed >> @wandb_log(datasets=True) may not auto log your dataset!
Warning: `pytorch` not installed >> @wandb_log(models=True) may not auto log your model!
Warning: `sklearn` not installed >> @wandb_log(models=True) may not auto log your model!
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    from wandb.integration.metaflow import wandb_log
  File "/home/user/miniconda3/envs/wandb-test/lib/python3.8/site-packages/wandb/integration/metaflow/__init__.py", line 1, in <module>
    from .metaflow import wandb_log, wandb_track, wandb_use
  File "/home/user/miniconda3/envs/wandb-test/lib/python3.8/site-packages/wandb/integration/metaflow/metaflow.py", line 109, in <module>
    data: pd.DataFrame,
NameError: name 'pd' is not defined
```