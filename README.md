# gs_cron_jobs

Small cron-friendly scripts for periodic license checks and internal sync polling.

## Scripts

- cron_scripts/commercial_license_check.py: calls the license check endpoint and returns status + timing.
- cron_scripts/commercial_sync_script.py: calls the sync endpoint and returns status + timing.

## Configuration

Environment variables (set in your shell or via `.env` on the target host):

- AUTHORIZED_SERVER_TOKEN: shared auth token for server-to-server calls.
- LICENSE_CHECK_URL: full URL for license checks.
- SYNC_URL: full URL for sync queue polling.
- REQUEST_TIMEOUT_SECONDS: HTTP timeout in seconds (default 120).

## Local run

```bash
python3 -m cron_scripts.commercial_license_check
python3 -m cron_scripts.commercial_sync_script
```


## Deployment + system setup

```bash
# Set the script user and target host first!
./scripts/move.sh

# In target computer
REPO_PATH=/mnt/storage/gs_cron_jobs
CRON_USER=aaeon
sudo mkdir -p "$REPO_PATH" /var/log/gs_cron_jobs
sudo chown "$CRON_USER":"$CRON_USER" /var/log/gs_cron_jobs
cd "$REPO_PATH"
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
sed "s|REPO_PATH|$REPO_PATH|g; s|CRON_USER|$CRON_USER|g" cronjobs/gs_cron_jobs.cron \
	| sudo tee /etc/cron.d/gs_cron_jobs >/dev/null

# Then
sudo chmod 644 /etc/cron.d/gs_cron_jobs
sudo systemctl restart cron
```

## Add a new cronjob

1. Add a new script under cron_scripts/ (follow the existing pattern and read config from env).
2. Add a new line to cronjobs/gs_cron_jobs.cron by copying an existing entry.
3. Pick a log file name under /var/log/gs_cron_jobs/.
4. Re-install cronjobs using the deployment steps above.

You can listen logs with 
```bash
tail -f /var/log/gs_cron_jobs/license_check.log
tail -f /var/log/gs_cron_jobs/sync_script.log
```

