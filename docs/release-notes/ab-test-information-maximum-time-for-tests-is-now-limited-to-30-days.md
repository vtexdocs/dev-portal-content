---
title: "A/B test information: maximum time for tests is now limited to 30 days"
slug: "ab-test-information-maximum-time-for-tests-is-now-limited-to-30-days"
type: "info"
excerpt: "Now, every A/B test started until the publishing of this announcement may end automatically in 30 days. From now on, every new A/B test may end automatically 30 days after starting."
createdAt: "2023-12-13T16:00:00.000Z"
tags:
    - Store Framework
    - VTEX IO
---

A/B tests compare the sales performance between a production workspace and the master workspace.

Previously, A/B tests could run indefinitely. Once started, they would only end after manually using the [`workspace abtest finish` command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#workspace-abtest-finish) from the VTEX IO CLI.

Now, every A/B test started until the publishing of this announcement may end automatically in 30 days. **From now on, every new A/B test may end automatically 30 days after starting**. It is not possible to retrieve data from tests after they are finished, so we recommend acquiring any relevant test data using the [`workspace abtest status` command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#workspace-abtest-status) before its ending.

Learn more at [Running A/B tests](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing).
