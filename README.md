# Flask on Porter

A minimal Flask app served by gunicorn, ready to deploy on Porter.

## What's inside

| Component | Version | Notes |
| --- | --- | --- |
| Python | 3.13 | `python:3.13-slim` base image |
| Flask | 3.1.3 | Web framework |
| gunicorn | 26.2.0 | Production WSGI server, configured in `gunicorn.conf.py` |

| Endpoint | Method | Response |
| --- | --- | --- |
| `/` | GET | `{"message": "Flask is running on Porter"}` |
| `/healthz` | GET | `{"status": "ok"}`, used by the Porter health check |

## Run locally

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
pytest
gunicorn app:app
```

The app listens on `0.0.0.0:8000`, or on `$PORT` when it is set.

With Docker:

```sh
docker build -t flask-getting-started . && docker run -p 8000:8000 flask-getting-started
```

## Deploy on Porter

### From the dashboard

Fork this repo, then in https://dashboard.porter.run create a new app from your GitHub repo. Porter reads `porter.yaml`, builds the Dockerfile, and opens a PR adding a GitHub Actions workflow. Merge it and every push to `main` redeploys. See https://docs.porter.run/applications/deploy/deploy-from-github-repo for a walkthrough.

### From the CLI

Install the CLI (https://docs.porter.run/cli/installation), then run:

```sh
porter auth login
porter apply -f porter.yaml
```

## Configuration

`porter.yaml` builds the image from the `Dockerfile` and runs one `web` service:

| Field | Value | Purpose |
| --- | --- | --- |
| `run` | `gunicorn app:app` | Start command, same as the Dockerfile `CMD` |
| `port` | `8000` | Port the container listens on |
| `cpuCores` / `ramMegabytes` | `0.25` / `256` | Resources per instance |
| `healthCheck.httpPath` | `/healthz` | Path Porter polls to decide the app is healthy |

| Name | Required | Description |
| --- | --- | --- |
| `PORT` | No | Port gunicorn binds to. Defaults to `8000`, which matches `porter.yaml`. |
| `WEB_CONCURRENCY` | No | Number of gunicorn worker processes. Defaults to `2`. |

Full reference: https://docs.porter.run/applications/configuration-as-code/reference

## Learn more

- https://docs.porter.run/getting-started/quickstart
- https://docs.porter.run/applications/configuration-as-code/overview
- https://docs.porter.run/applications/configure/environment-groups
- https://docs.porter.run/addons/datastores
- https://docs.porter.run/preview-environments/overview
- https://github.com/porter-dev/starters
