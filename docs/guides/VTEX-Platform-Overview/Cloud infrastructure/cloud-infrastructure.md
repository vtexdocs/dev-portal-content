---
title: "Cloud infrastructure"
slug: "cloud-infrastructure"
hidden: false
createdAt: "2024-05-23T13:08:55.338Z"
updatedAt: "2024-05-23T13:08:55.338Z"
excerpt: "Learn how our infrastructure decisions ensure scalability, reliability, and performance for your business."
---

This guide presents an overview of VTEX's infrastructure architecture, exploring its cloud resources and technical aspects. Read the following sections to understand how our multi-tenancy and cloud-based architecture can leverage your business.

## SaaS multi-tenancy

By adopting the Software as a Service (SaaS) model, VTEX eliminates the need to set up and maintain a complex local infrastructure, enabling scalability, stability, and simplified access to advanced digital commerce features such as order management, product offerings in marketplaces, and flexible integrations.

A key element of our platform's architecture is the concept of multi-tenancy. Tenants refer to individual accounts who have access to the same platform infrastructure while keeping their data and configurations isolated and secure. VTEX's multi-tenant architecture enables us to serve multiple customers on a shared infrastructure, ensuring performance, scalability, and cost-effectiveness.

The multi-tenant architecture diagram below illustrates how VTEX supports multiple accounts on a shared infrastructure:

![Multi-tenant](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/cloud-infrastructure/multi-tenant.png)

* **Tenants:** _Tenant 1_ and _Tenant n_ represent different accounts using the VTEX platform. Each tenant sends and receives requests and responses to and from the platform.
* **Application Runtime (Kernel):** Atomic Requests are individual operations processed by the application runtime. Each tenant's requests are handled as atomic requests, ensuring isolation and security.
* **VTEX IO Apps:** These applications provide specific functionalities and can be customized for each tenant. The diagram shows that VTEX IO apps can be standard or customized depending on the tenant's requirements.
* **Database Interaction:** The application runtime processes read and write operations to a shared physical database. This ensures that each tenant's data is handled efficiently.
* **Shared Physical Database:** The database schema is shared among tenants but maintains tenant-specific data and metadata to ensure data isolation and security. Each tenant's data and metadata are stored in isolated sections within the shared schema.

### Logical separation

With a multi-tenant architecture, tenants don't have exclusive resources, such as physically separate databases, but we guarantee logical separation. Our clients' information is contained in one account, isolated and protected from other accounts. There is no method of accessing data from different accounts, since all our services require explicit indication of a specific [account](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#vtex-account-types) and [authorized credentials](https://developers.vtex.com/docs/guides/authentication).

Each request belongs to a specific tenant (account) and is processed atomically, which means each request has their own lifecycle, allowing for elastic operation and scalability, and promoting performance.

### Constant evolution and growth

The implementation of new features and updates can take place across the entire platform, ensuring that all tenants can benefit from the latest enhancements.

With a single, shared code base and infrastructure, updates, bug fixes and maintenance tasks are centralized, reducing the time and effort required to keep the platform running smoothly across all tenants.

Given our demand aggregation capability due to SaaS multi-tenancy architecture, VTEX is capable of handling traffic peaks smoothly. Learn more on the [Scalability](#scaling) section.

## Microservices

Our core commerce capabilities consist of over 70 shared microservices. Unlike a monolithic solution of tightly integrated capabilities, microservices are assembled into distinct functional modules, such as Checkout, Promotions, Catalog, or Pricing services, each with their own responsibilities and APIs.

![Microservices](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/cloud-infrastructure/microservices.png)

Each microservice has its lifecycle independent of others, including its environment, [deployment](#deployment-strategy-and-change-management), and codebase, which allows us to use the most appropriate technologies and design patterns for each case. Teams can deploy services independently, enabling continuous improvement and faster updates. Each microservice is independently scalable as demand increases.

Such choices ensure speed and flexibility in the evolution of platform services, and guarantee exclusive resources for each service, eliminating competition between distinct operations and thus ensuring greater availability.

### Virtual Private Network (VPC)

Given our microservices architecture, it is common for an application to need to query others to process a request. To ensure good processing performance while also safeguarding against unwanted external access, the microservices run within the same Virtual Private Network (VPC) – unless in cases where an exclusive VPC is a legal or security prerequisite, as is the case with VTEX's [Payment Gateway](https://help.vtex.com/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk), with [PCI](https://help.vtex.com/tutorial/what-is-the-pci-ssc) certification.

Within the VPC, [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) apps have access control based on [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) that only allow access to necessary resources, thus ensuring greater security.

### Deployment strategy and change management

New features and fixes are introduced daily, in a smooth and seamless way. Over 12,000 upgrades are rolled out annually without causing disruptions to customer operations. For patch and minor updates not impacting backwards-compatibility, there is an automatic update for all clients. In case of major feature changes, we ensure transparent communication by providing notifications, [documentation](https://developers.vtex.com/updates/release-notes) and timelines prior to release.

Our deployment capacity is made possible by a robust architecture of [microservices](#microservices), each having its own independent life cycle but operating within a unified, automated Continuous Delivery framework. Our CI/CD pipeline ensures seamless integration, testing, and deployment of code changes, enabling us to deliver features and updates efficiently and with minimal disruption.

Releases primarily focus on adding new features or addressing bugs. Major releases are typically confined to specific services of the platform. Major versions follow the same development and deployment processes, coexisting with the previous version to allow tenants ample time for adjustment if needed.

General deployments to development and production environments are automated, triggered by reviewed and approved releases from our versioned code repositories. Each [microservice](#microservices) contains a protected main branch that can only be modified after approval of at least two developers, ensuring that peer-reviewing and segregation of duties are part of the process.

After that, a webhook is sent, and a new environment is automatically created without the need for further commands. Finally, the developer defines the autoscaling configuration and the number of instances in the new environment and slowly switches traffic over.

This [blue/green](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html) deployment strategy ensures that any problems are detected with little production traffic (usually 1%) by observing the system's metrics, and rollbacks are immediate since the previous environment still exists.

## REST APIs

Our [REST APIs](https://developers.vtex.com/docs/guides/getting-started-list-of-rest-apis) enable you to leverage and extend VTEX core commerce capabilities to integrate with third-party solutions and deliver best-in-class experiences across a multitude of shopper touchpoints (headless mobile applications, chatbots, IoT integrations) and [back office](https://developers.vtex.com/docs/guides/erp-integration-guide) touchpoints (ERP, PIM, and WMS integrations).

For developers looking to dive deeper into our APIs, we offer comprehensive [API reference](https://developers.vtex.com/docs/api-reference) documentation that includes usage examples to streamline the process of exploration, understanding, and consumption.

Using our REST APIs with our development platform (VTEX IO) and data service (Master Data), you can expand the VTEX platform to address your unique business needs.

## Cloud-native

In our infrastructure, we align with market trends in hosting and computing. VTEX core commerce services are built on top of Amazon Elastic Beanstalk, which monitors and controls the deployment of new servers. VTEX IO is built on [AWS Kubernetes](https://aws.amazon.com/kubernetes/?nc1=h_ls), using Amazon Elastic Compute Cloud (EC2) clusters and containers on those instances. Kubernetes controls the deployment, maintenance, and scaling processes on VTEX IO.

Our cloud-native, multi-tenant SaaS solution allows tenants to run the same version of the platform and benefit from frequent and seamless upgrades on top of high scalability.

Furthermore, our adoption of microservices architecture facilitates seamless modernization and ensures enhanced observability across various computing environments.

>ℹ Verify our credentials by consulting Amazon's assessment of our company at [AWS Partner VTEX](https://partners.amazonaws.com/partners/001E000000pd8JbIAI/VTEX). The [AWS Retail Competency Partners](https://aws.amazon.com/retail/partner-solutions/) undergo rigorous validation by AWS to ensure alignment with AWS best practices for building secure, high-performing, resilient and efficient cloud infrastructure for industry applications – to give customers increased confidence when making decisions.

### Content delivery optimization

In a cloud-native architecture, optimizing content delivery involves leveraging a combination of technologies and strategies to minimize latency, enhance performance, and improve overall user experience. This section explores key components of content delivery logic within our cloud-native framework, including Content Delivery Networks (CDNs), routers, and caching mechanisms.

Check the diagram and the following explanation to learn more about our resilient layered approach to content delivery:

![CDN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/cloud-infrastructure/cdn.png)

1. VTEX maintains [CDN](#cdn) servers across multiple global regions. These servers deliver cached content from the closest location to the user, significantly reducing load times.
2. In scenarios with no [cache](#cache) in the CDN, or during actions like placing an order, requests are directed to the [router](#router). The router's region (AWS zones) being distributed across multiple regions enhances our resilience. Other zones are not fallbacks, they operate concurrently, bolstering our resilience. Even in the event of a failure, it is nearly imperceptible to final customers. Each session loads information independently, not relying on a single server from a specific application. In case of critical scenarios, we are able to maintain performance for active sessions.
3. There is a [caching layer](#cache) after the router as well, relieving the underlying application from reprocessing the same data. When handling numerous requests, only necessary ones reach the application, ensuring availability. These strategies minimize the need to scale applications, ensuring platform resilience and capacity.
4. Applications run on multiple servers, ensuring redundancy. We operate multiple replicas simultaneously, enhancing reliability.

This strategy ensures the platform swiftly recovers and maintains the capacity to process required tasks, embodying resilience.

#### CDN

VTEX's Content Delivery Network (CDN) is a distributed network of servers strategically placed across various geographic locations, whose primary function is to deliver web content to users more efficiently and reliably. At VTEX, CDN redundancy ensures the availability and performance of our services.

Our CDN plays a crucial role in caching delivered content, particularly static content, ensuring superior performance for shoppers during their browsing experience. Additionally, the CDN serves as the primary edge protection against [Denial-of-service (DDoS) attacks](https://aws.amazon.com/en/shield/ddos-attack-protection/).

#### Router

A router is responsible for performing operations on the platform that are common to all services, such as throttling, as well as distributing requests to internal services, acting as the single entry point in the [VPC](#vpc). As the traffic orchestrator, the router ensures control in change management, resulting in lower risks with progressive rollouts and quick rollback in case of failures.

#### Cache

VTEX employs caching across multiple layers, including HTTP, application and database levels, ensuring greater speed and capacity in processing requests and consequently maintaining the platform's high availability.

Our cache layers follow the best practices and are continuously improved to provide better performance, which is critical for improving conversion rates. These cache layers can be easily invalidated to update data as required. For more detailed information, refer to [Cache](https://help.vtex.com/en/tutorial/understanding-how-the-cache-works--tutorials_258) documentation.

### Scalability

Leveraging technologies like [Clusters](https://aws.amazon.com/what-is/kubernetes-cluster/?nc1=h_ls), [Kubernetes](https://kubernetes.io/), and microservices enables us to efficiently manage and scale our resources based on demand, thanks to built-in features like autoscaling.

Our multi-tenant architecture ensures elastic scalability, allowing stores to easily adapt to changing business requirements and handle traffic peaks on events such as Black Friday. As your operation grows, our platform accommodates increased demand without compromising performance.

![Scalability](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/cloud-infrastructure/scalability.jpg)

### Reliability

We deliver high availability, as defined in our [SLA agreement](https://vtex.com/us-en/privacy-and-agreements/agreements/), a document which expresses the service level of the platform's infrastructure and technically clarifies its operational uptime and downtime, as well as all the types of events considered as incidents.

You can monitor the platform's stability in real time and access the full incident and maintenance history at [VTEX Status](https://status.vtex.com/). Learn more about all the information available on this page at our [VTEX Status page](https://help.vtex.com/en/tutorial/vtex-status-page--gPhqDn9IQ3c67wbJEX3JJ) guide.

Additionally, we provision our infrastructure in an automated manner using the [Infrastructure as Code (IaC)](https://aws.amazon.com/what-is/iac/?nc1=h_ls) concept. VTEX is built on top of [AWS Elastic Beanstalk](https://aws.amazon.com/pt/elasticbeanstalk/), so we autoscale our applications and microservices. For each service, we control Latency and CPU usage so that we can identify if a specific module needs more or fewer servers, keeping safe thresholds so changes occur ahead of time. AWS Elastic Beanstalk also helps in load-balancing, deploying and rolling-back versions of our systems, so we can provide scalable and stable up-to-date systems to VTEX customers.

VTEX IO is built on [AWS Kubernetes](https://aws.amazon.com/kubernetes/?nc1=h_ls), using [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/?nc1=h_ls) clusters and containers on those instances. Kubernetes controls the deployment, maintenance, and scaling processes on VTEX IO.

VTEX teams constantly execute load tests to ensure the platform is ready to scale with our customer's demands, gaining visibility and fixing bottlenecks.

#### Maintenance

All scheduled maintenance activities by VTEX are communicated beforehand through [VTEX Status](https://status.vtex.com/). Maintenance typically occurs once every 60 days and has a duration of about 2-3 hours, during the night (BRT) and outside of peak sales hours. During this period, there is no expected downtime for customers.

### Security

VTEX counts with a comprehensive cloud monitoring system, covering both internal environments and the edge, in line with the [AWS Security Maturity Model](https://maturitymodel.security.aws.dev/en/model/). This system offers a range of functionalities, including configuration change alarms and security alarms.

All events within our platform are routed to a Security Information and Event Management (SIEM) infrastructure, where we can correlate events, providing not only traceability but also real-time alerts for our Security team to act on risk mitigation promptly.

>ℹ Read our [Security](https://developers.vtex.com/docs/guides/security) overview for more details.

#### Threat intelligence

In addition to global platform monitoring, we conduct tenant-level monitoring across both the surface web and the dark web. This proactive approach allows us to identify and address issues such as unauthorized exposure of keys or cloned pages quickly, preventing potential incidents from escalating.

#### Active resource monitoring and patch management

Our platform implements active resource monitoring and patch management. This keeps our infrastructure up-to-date with the latest security patches and configurations. By actively monitoring and managing resources, we can efficiently address any security gaps or vulnerabilities.

Find more information about our security practices at [Security - VTEX](https://vtex.com/us-en/security/).
