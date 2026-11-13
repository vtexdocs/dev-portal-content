---
title: "VTEX IO Observability plugin for Grafana"
slug: "vtex-io-observability-plugin"
hidden: false
createdAt: "2026-10-29T00:00:00.000Z"
updatedAt: "2026-10-29T00:00:00.000Z"
excerpt: "Learn how to install the VTEX IO Observability plugin for Grafana manually or with Docker, connect it to your VTEX account, and query app logs and metrics."
---

>⚠️ The VTEX IO Observability plugin for Grafana is in beta. It isn't published in the [Grafana plugin catalog](https://grafana.com/grafana/plugins) to use with [Grafana Cloud](https://grafana.com/docs/grafana-cloud), so you must install it manually from the [plugin GitHub releases page](https://github.com/vtex/vtexio-grafana-plugin/releases).

The **VTEX IO Observability plugin for Grafana** is a data source plugin that lets you visualize logs and metrics from your VTEX IO apps in [Grafana](https://grafana.com/) dashboards. The plugin doesn't store logs or metrics in Grafana. It retrieves data from the [VTEX IO Observability API](https://developers.vtex.com/docs/guides/vtex-io-observability-api-guide) using an API key and token from your VTEX account.

This guide explains how to install the plugin, either manually on a Grafana server or with Docker, connect it to your VTEX account, and query logs and metrics.

## Before you begin

Make sure you have the following:

- **VTEX account name:** The [account name](https://help.vtex.com/en/docs/tutorials/what-is-an-account-name) of the store whose app data you want to visualize.
- **VTEX API key and token:** An [API key and token](https://help.vtex.com/en/docs/tutorials/generated-keys) pair associated with a [role](https://help.vtex.com/en/docs/tutorials/roles) that includes the `colossus-read-logs` [resource](https://help.vtex.com/docs/tutorials/license-manager-resources). You can generate them by following the steps in [Generate an API key and token](#1-generate-an-api-key-and-token).
- **VTEX IO apps that meet the plugin requirements:** The plugin only displays logs and metrics from apps that meet all of the following requirements:
  - Your account is the app vendor. Apps installed in your account but developed by other vendors aren't displayed.
  - The app uses version `7.x` of the [`node` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder). You can check the builder version in the `builders` field of the app's [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file.
  - The app generates logs using the standard `logger` from the `@vtex/api` package, which is available in the `ctx.vtex` object. No additional logging code is required. For more information, see [Managing application logs](https://developers.vtex.com/docs/guides/vtex-io-documentation-managing-application-logs#implementing-the-vtex-io-logging-service).
  - The app is [deployed](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version) and installed in a production [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace).

## Installing Grafana

If you don't have a Grafana instance yet, follow these steps to download, install, and access Grafana:

1. Go to the [Grafana download page](https://grafana.com/grafana/download).
2. Select the edition, the version, and your platform. Grafana is available for the following platforms:

    - Linux
    - Linux on ARM64
    - Windows
    - macOS
    - Docker

3. Follow the installation instructions displayed for your platform. For more details, see [Install Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation).
4. Start the Grafana server and open `http://localhost:3000` in your browser. `3000` is the default Grafana port.
5. Sign in with the default username `admin` and password `admin`.

>⚠️ We recommend changing the default password when you first sign in, especially if your Grafana instance is accessible from other machines. Grafana asks you to set a new password on the first sign-in, but this step can be skipped.

>ℹ️ If you use Docker, you don't need to install Grafana separately. The steps in [Installing the plugin with Docker](#installing-the-plugin-with-docker) start Grafana in a container with the plugin installed.

## Installing the plugin manually

Follow these steps to install the plugin on a Grafana server running on Linux, macOS, or Windows. If you run Grafana in a container, see [Installing the plugin with Docker](#installing-the-plugin-with-docker).

### 1. Download and extract the plugin

1. Download the `vtexio-grafana-datasource-{version}.zip` file from the latest release on the [GitHub releases page](https://github.com/vtex/vtexio-grafana-plugin/releases).
2. Extract the zip file into the plugins directory. For example, on Linux:

    ```bash
    sudo unzip vtexio-grafana-datasource-{version}.zip -d /var/lib/grafana/plugins
    ```

    The default Grafana plugins directory depends on your operating system:

    | Operating system | Plugins directory |
    | :---- | :---- |
    | Linux | `/var/lib/grafana/plugins` |
    | macOS (Homebrew on Intel) | `/usr/local/var/lib/grafana/plugins` |
    | macOS (Homebrew on Apple silicon) | `/opt/homebrew/var/lib/grafana/plugins` |
    | Windows | `C:\Program Files\GrafanaLabs\grafana\data\plugins` |

3. Check that the extracted folder is named `vtexio-grafana-datasource` and that the `plugin.json` file is at the root of this folder, as in `plugins/vtexio-grafana-datasource/plugin.json`.

>ℹ️ Some earlier releases extract to a folder with the version in its name, such as `vtexio-grafana-datasource-0.2.2-beta.0`. In this case, rename the folder to `vtexio-grafana-datasource` so the folder name matches the plugin ID.

### 2. Allow Grafana to load the plugin

>ℹ️ If your Grafana root URL is `http://localhost:3000/`, the plugin signature is valid, and you can skip this step.

Grafana blocks unsigned plugins by default. To allow Grafana to load the plugin, add its ID to the [`allow_loading_unsigned_plugins`](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#allow_loading_unsigned_plugins) setting in the Grafana configuration file. The default configuration file location depends on your operating system:

| Operating system | Configuration file |
| :---- | :---- |
| Linux | `/etc/grafana/grafana.ini` |
| macOS (Homebrew on Intel) | `/usr/local/etc/grafana/grafana.ini` |
| macOS (Homebrew on Apple silicon) | `/opt/homebrew/etc/grafana/grafana.ini` |
| Windows | `C:\Program Files\GrafanaLabs\grafana\conf\custom.ini` |

1. Open the configuration file. On Windows, if the `custom.ini` file doesn't exist, create it in the `conf` folder.
2. Find the `[plugins]` section.
3. Add the plugin ID to the `allow_loading_unsigned_plugins` setting:

    ```ini
    [plugins]
    allow_loading_unsigned_plugins = vtexio-grafana-datasource
    ```

    If the line starts with `;`, remove the `;` to uncomment it. If the setting already lists other plugins, add `vtexio-grafana-datasource` to the list, separating the IDs with commas.

4. Save the file.

### 3. Restart Grafana

Grafana detects the plugin and configuration changes only after a restart. Restart the Grafana service according to your operating system:

| Operating system | How to restart Grafana |
| :---- | :---- |
| Linux | Run `sudo systemctl restart grafana-server`. |
| macOS (Homebrew) | Run `brew services restart grafana`. |
| Windows | Open **Services** (`services.msc`), right-click **Grafana**, and click `Restart`. |

### 4. Verify the installation

1. Sign in to Grafana and go to **Administration** > **Plugins and data** > **Plugins**.
2. Search for **VTEX IO** and check that the plugin appears in the list.

After verifying the installation, [connect the plugin to your VTEX account](#connecting-the-plugin-to-your-vtex-account).

## Installing the plugin with Docker

When you run Grafana in a Docker container, you install the plugin by mounting the plugin folder as a volume. To allow Grafana to load the plugin, you set the `GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS` environment variable, which is equivalent to the `allow_loading_unsigned_plugins` setting.

### 1. Extract the plugin on your host machine

1. Download the `vtexio-grafana-datasource-{version}.zip` file from the latest release on the [GitHub releases page](https://github.com/vtex/vtexio-grafana-plugin/releases).
2. In the folder where you'll run Docker, extract the zip file:

    ```bash
    unzip vtexio-grafana-datasource-{version}.zip
    ```

3. Check that the folder structure is the following:

    ```text
    📂 vtexio-grafana-datasource
    └─ 📄 plugin.json
    ```

>ℹ️ Some earlier releases extract to a folder with the version in its name, such as `vtexio-grafana-datasource-0.2.2-beta.0`. In this case, rename the folder to `vtexio-grafana-datasource`.

### 2. Start the Grafana container

Start Grafana with `docker run` or with Docker Compose. Both options mount the local `vtexio-grafana-datasource` folder into the container plugins directory, `/var/lib/grafana/plugins`, and allow Grafana to load the plugin.

**Using `docker run`**

Run the following command in the folder where you extracted the plugin:

```bash
docker run -d \
  --name grafana \
  -p 3000:3000 \
  -v $(pwd)/vtexio-grafana-datasource:/var/lib/grafana/plugins/vtexio-grafana-datasource \
  -e GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS=vtexio-grafana-datasource \
  grafana/grafana:latest
```

>ℹ️ This command uses Bash syntax. In PowerShell, replace `$(pwd)` with `${PWD}` and the line continuation character `\` with a backtick (`` ` ``).

**Using Docker Compose**

1. In the folder where you extracted the plugin, create a `docker-compose.yml` file with the following content:

    ```yaml
    services:
      grafana:
        image: grafana/grafana:latest
        container_name: grafana
        ports:
          - "3000:3000"
        volumes:
          - ./vtexio-grafana-datasource:/var/lib/grafana/plugins/vtexio-grafana-datasource
        environment:
          - GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS=vtexio-grafana-datasource
    ```

2. Start Grafana:

    ```bash
    docker compose up -d
    ```

    If you use the standalone Docker Compose v1, run `docker-compose up -d` instead.

>ℹ️ These examples don't persist Grafana data, so data sources and dashboards are lost when you remove the container. To keep them, also mount a volume to `/var/lib/grafana`.

### 3. Verify the installation

1. Open `http://localhost:3000` in your browser and sign in to Grafana with the default credentials described in [Installing Grafana](#installing-grafana).
2. Go to **Administration** > **Plugins and data** > **Plugins**.
3. Search for **VTEX IO** and check that the plugin appears in the list.

After verifying the installation, [connect the plugin to your VTEX account](#connecting-the-plugin-to-your-vtex-account).

## Connecting the plugin to your VTEX account

After installing the plugin, either manually or with Docker, connect it to your VTEX account by generating an API key and adding a **VTEX IO** data source in Grafana.

### 1. Generate an API key and token

1. In the top bar of the VTEX Admin, click your profile avatar and then click **Account Settings** > **API Keys**.
2. In the **Generated** tab, click `+ Generate Key`.
3. In the **Key identification** field, enter a name that identifies the integration, such as `grafana-observability`.
4. Select a role that includes the `colossus-read-logs` resource. To create a role, see [Creating roles](https://help.vtex.com/en/docs/tutorials/creating-roles).
5. Click `Generate`.
6. Copy the single-access link to the new token, open it, and copy the API token. Also copy the API key, which follows the format `vtexappkey-{accountName}-{suffix}`.
7. Store the API key and token in a secure location, such as a password manager.

>⚠️ The API token is displayed only once. Never share it in public channels, emails, or version control repositories. If a token is exposed, [deactivate the API key](https://help.vtex.com/en/docs/tutorials/generated-keys#deactivating-or-activating-generated-keys) immediately.

For more details about this process, see [Generating keys](https://help.vtex.com/en/docs/tutorials/generated-keys#generating-keys).

### 2. Add the VTEX IO data source

1. In Grafana, go to **Connections** > **Data sources**.
2. Click `Add data source`, search for **VTEX IO**, and select it.
3. Fill in the following fields:

    | Field | Description |
    | :---- | :---- |
    | **Name** | Name that identifies the data source in Grafana. The default name is `vtex-grafana-datasource`. You can change it to a name of your choice. |
    | **App Key** | Your VTEX API key, such as `vtexappkey-mystore-ABCD1234`. Required. |
    | **Account** | The VTEX account name to query. The plugin fills in this field automatically based on the API key. It accepts only lowercase letters and numbers and automatically converts uppercase letters. |
    | **App Token** | Your VTEX API token. Required. |

4. Click `Save & test`.

If the connection works, Grafana displays the message "Successfully connected to VTEX Observability Platform." If an error occurs, see [Troubleshooting](#troubleshooting).

## Querying logs and metrics

You can use the **VTEX IO** data source in [dashboard panels](https://grafana.com/docs/grafana/latest/visualizations/dashboards/), and in [**Explore**](https://grafana.com/docs/grafana/latest/visualizations/explore/get-started-with-explore/). Use dashboards to save and share visualizations of your app data, and use **Explore** to investigate logs and metrics without creating a dashboard.

Like other Grafana data sources, the plugin provides its own [query editor](https://grafana.com/docs/grafana/latest/visualizations/explore/query-editor/) with the following fields:

| Field | Description |
| :---- | :---- |
| **Query Type** | Type of data to query: `Logs` or `Metrics`. |
| **App name** | VTEX IO app to query, in the format `{vendor}.{app-name}@{version}`. |
| **Metric Type** | Predefined metric to visualize. Only available for `Metrics` queries, after you select an app. |
| **Page Size** | Number of records to retrieve. The default value is `100` and the maximum value is `1000`. |

The **App name** list only shows apps that meet the requirements described in [Before you begin](#before-you-begin) and that sent logs or metrics within the selected time range, with the most recent versions first. If an app is missing from the list, expand the [dashboard time range](https://grafana.com/docs/grafana/latest/visualizations/dashboards/use-dashboards/#set-dashboard-time-range).

>ℹ️ Logs and metrics are retained for three days. Queries for time ranges older than three days don't return data.

To run queries, [create a dashboard](https://grafana.com/docs/grafana/latest/visualizations/dashboards/build-dashboards/create-dashboard/) and add a [visualization](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/), or [open **Explore**](https://grafana.com/docs/grafana/latest/visualizations/explore/get-started-with-explore/#access-explore) from the main menu. Then, follow the steps below for the type of data you want to query.

### Querying logs

1. Select the data source with the name you defined in the **Name** field when [adding the data source](#2-add-the-vtex-io-data-source), such as `vtex-grafana-datasource`.
2. In **Query Type**, select `Logs`.
3. In **App name**, select the app whose logs you want to view. The query runs automatically.
4. Optionally, change the **Page Size** value to adjust the number of log entries to retrieve.

To filter logs, expand a log entry to open its details and click the **Filter for value** or **Filter out value** icon next to the `account`, `workspace`, or `level` field. The active filters appear as tags in the **Filters** row of the query editor. To remove a filter, click its tag.

### Querying metrics

1. Select the data source with the name you defined in the **Name** field when [adding the data source](#2-add-the-vtex-io-data-source), such as `vtex-grafana-datasource`.
2. In **Query Type**, select `Metrics`.
3. In **App name**, select the app you want to monitor.
4. In **Metric Type**, select one of the predefined metrics described in the table below. The query runs when both the app and the metric type are selected.

| Metric type | Description |
| :---- | :---- |
| **Request Rate per Account** | Total number of requests over time. |
| **Error Rate per Handler** | Error rate over time. |
| **Latency Stats per Account and Handler** | Latency percentiles (p50, p95, and p99, in milliseconds), displayed as a table. |
| **Latency Stats per Account** | Latency percentiles (p50, p95, and p99). |
| **2xx Latency P50 per Handler** | Median latency of successful (2xx) requests. |
| **2xx Latency P90 per Handler** | 90th percentile latency of successful (2xx) requests. |
| **2xx Latency P99 per Handler** | 99th percentile latency of successful (2xx) requests. |

Request and error rate metrics are based on the `runtime_http_requests_total` metric, and latency metrics are based on the `runtime_http_requests_duration_milliseconds` histogram. To build custom queries with these metrics, use the [VTEX IO Observability API](https://developers.vtex.com/docs/guides/vtex-io-observability-api-guide).

>ℹ️ Results for **Latency Stats per Account and Handler** are intended for the **Table** visualization, with the `account`, `handler`, `p50`, `p95`, and `p99` columns. If the panel doesn't switch to this visualization automatically, select **Table** in the visualization picker.

## Updating the plugin

To update the plugin, download the latest release from the [GitHub releases page](https://github.com/vtex/vtexio-grafana-plugin/releases), replace the contents of the `vtexio-grafana-datasource` folder with the new version, and restart Grafana. For Docker installations, replace the folder on your host machine and run `docker restart grafana`.

>⚠️ Version `0.3.2-beta.0` was released with the plugin ID `vtex-grafana-datasource`. If you installed this version, after installing a newer release, remove the `vtex-grafana-datasource` folder from the plugins directory, use `vtexio-grafana-datasource` in the `allow_loading_unsigned_plugins` setting or in the `GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS` variable, and add the data source again. Grafana doesn't migrate existing data sources between plugin IDs.

## Troubleshooting

| Issue | Possible cause | Solution |
| :---- | :---- | :---- |
| The plugin doesn't appear in the plugins list. | The plugin folder structure is incorrect. | Make sure the `plugin.json` file is exactly one level below the plugins directory, as in `plugins/vtexio-grafana-datasource/plugin.json`, and that the plugin folder isn't nested inside another folder. |
| Grafana reports a signature verification error or blocks the plugin as unsigned. | Grafana isn't allowed to load the plugin. | Check that the `allow_loading_unsigned_plugins` setting or the `GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS` variable contains exactly `vtexio-grafana-datasource`, and restart Grafana. |
| Grafana reports a permission error when loading the plugin on Linux. | The `grafana` user can't read the plugin folder. | Run `sudo chown -R grafana:grafana /var/lib/grafana/plugins/vtexio-grafana-datasource`, adjusting the path to your plugins directory. |
| Configuration changes have no effect. | Grafana wasn't restarted. | Restart Grafana and check the logs to confirm that the configuration was reloaded. Use `sudo journalctl -u grafana-server` on Linux or `docker logs grafana` for Docker installations. |
| `Save & test` returns the message "App Key and App Token are required." | The data source credentials are missing. | Fill in the **App Key** and **App Token** fields and click `Save & test` again. |
| `Save & test` returns the message "Failed to connect to VTEX Observability Platform." | The credentials are invalid or inactive, or the API key doesn't have the required permissions. | Check that the API key is active, that the API token is correct, and that the role associated with the key includes the `colossus-read-logs` resource. |
| The **App name** list is empty or doesn't show a specific app. | The app either doesn't meet the plugin requirements or didn't send logs or metrics within the selected time range. | Check that the app meets all the requirements described in [Before you begin](#before-you-begin): your account is the app vendor, the app uses the `node` builder 7.x and the standard `logger` from `@vtex/api`, and the app is deployed and installed in a production workspace. Then, expand the [dashboard time range](https://grafana.com/docs/grafana/latest/visualizations/dashboards/use-dashboards/#set-dashboard-time-range), keeping it within the last three days. |
| A panel or table doesn't refresh automatically. | Auto refresh is turned off (the Grafana default), the queries aren't running, or the selected time range doesn't include periods when the app received traffic. | To turn on [auto refresh](https://grafana.com/docs/grafana/latest/visualizations/dashboards/use-dashboards/#refresh-dashboard), click the arrow next to the **Refresh dashboard** icon and select a refresh interval. To confirm that the queries are running, open the [query inspector](https://grafana.com/docs/grafana/latest/visualizations/explore/get-started-with-explore/#query-inspector) and check the request and response details. Make sure the dashboard time range covers a period in which the app received traffic. |

## Next steps

- Learn how to query logs and metrics programmatically in the [VTEX IO Observability API guide](https://developers.vtex.com/docs/guides/vtex-io-observability-api-guide).
- Explore other Grafana configuration options in the [Grafana documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/).
- To report a bug or request a feature for the plugin, open a ticket with [VTEX Support](https://help.vtex.com/en/support).
