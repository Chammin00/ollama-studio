# Antigravity Acquired Skills & Projects Ecosystem Digest

Updated: 334 Acquired Skills | 84 Production Projects

## 📦 Part 1: Acquired Agent Skills Catalog

### Platform & Customizations (5 skills)

#### `agy-customizations`
Comprehensive guide and reference for the Antigravity Customization System. Use to explain how customizations work, their loading priority, discovery mechanisms, and to guide the creation of skills, rules, plugins, hooks, and MCP servers.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\agy-customizations\SKILL.md`

#### `antigravity-guide`
Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands, keybindings, and customizations (skills, rules, MCP, sidecars). Activate this skill when the user asks questions about how to use, configure, or customize Antigravity, AGY, the agy CLI, the Antigravity IDE, or Antigravity 2.0.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\antigravity_guide\SKILL.md`

#### `google-antigravity-sdk`
Design, implement, and debug autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK. ACTIVATE this skill when the user wants to create, configure, or orchestrate Google Antigravity agents.

- Source: `C:\Users\chase\.gemini\config\plugins\google-antigravity-sdk\skills\google-antigravity-sdk\SKILL.md`

#### `migrate-workflows`
Automatically migrate legacy workflows to modern skills across global and workspace configurations. Scans for existing workflows, creates target SKILL.md files, and safely archives old workflow files.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\migrate-workflows\SKILL.md`

#### `ui-plugin-navigation`
Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side pane. Use when a running UI plugin's panel would help with what the user is doing, or right after the user enables a new UI plugin pane and a shortcut to open it is handy.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\ui-plugin-navigation\SKILL.md`

### Google Cloud & BigQuery Data Engineering (44 skills)

#### `bigquery-ai-ml`
Leverages BigQuery's built-in machine learning and GenAI capabilities for advanced data analytics. Use when you need to write SQL queries that perform time-series forecasting, predict values, detect outliers or anomalies, find key drivers, perform semantic search or vector search, classify text, calculate similarity, summarize content, translate language, evaluate models, filter by semantic conditions, measure the causal effect of an intervention, compute correlations between columns, generate descriptive statistics and table distribution profiles, detect change points or structural breaks, extract trend or seasonality components, or leverage generative AI capabilities in BigQuery. Do not use for general BigQuery dataset, table, or job management requests.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-ai-ml\SKILL.md`

#### `bigquery-bigframes`
Generates Python code using BigQuery DataFrames (BigFrames). Use by default for any Python data task involving BigQuery, including data processing, analysis, and machine learning. Don't use for SQL-first workflows or the google-cloud-bigquery client library — use bigquery-basics.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-bigframes\SKILL.md`

#### `bigquery-data-transfer-service`
Discovers and inspects BigQuery Data Transfer Service (DTS) configurations. Use this to identify existing ingestion pipelines and extract datasource or transfer config metadata for data pipelines. Use when a user asks for ingestion scenarios while building or managing data pipelines or when a user asks to "ingest" or "add" data that may already be managed by a DTS transfer.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-data-transfer-service\SKILL.md`

#### `bigquery-graph-author`
Provides an end-to-end journey for authoring a BigQuery property graph from your tables or from a model document/diagram (an ER diagram, an ontology, a semantic model): dataset discovery, candidate relationships verified against the data, a readable plan, and `CREATE PROPERTY GRAPH` DDL with schema best practices and semantic measures/dimensions, plus an opt-in verification suite for the landed graph. Use when creating or replacing a property graph, authoring a graph from a dataset or a document, or verifying relationships or suspicious edge counts. Don't use for querying an existing graph, for non-BigQuery graph databases, or for drawing/rendering diagrams.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-graph-author\SKILL.md`

#### `bigquery-graph-query`
Provides guidelines and best practices for querying BigQuery property graphs and semantic graphs: native GQL (Graph Query Language) pattern matching, multi-hop and variable-length paths, aggregation, top-N, path extraction, output formatting (graph visualization with TO_JSON vs tabular), GRAPH_TABLE relational SQL integration, and semantic graph querying via the GRAPH_EXPAND TVF with starting-node view selection and AGG() measures. Also covers hybrid semantic search, combining `VECTOR_SEARCH` candidate generation with graph traversal when a node carries an embedding-backed property. Use when querying graph topology, node/edge connections, paths, or semantic measures over an existing BigQuery graph. Don't use for Cypher or non-BigQuery graph databases, or for creating/modifying a graph schema.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-graph-query\SKILL.md`

#### `bigquery-observability`
Provides data-retrieval best practices, tool selection guidance, and performant SQL query syntax for BigQuery telemetry across INFORMATION_SCHEMA, Cloud Monitoring, and the REST API. Use when the telemetry to fetch is already known, selecting telemetry tools, writing performant INFORMATION_SCHEMA queries, retrieving telemetry for diagnosing single-job performance bottlenecks, investigating slot contention, job concurrency and queue latency, analyzing reservation capacity, utilization and autoscaling saturation, or auditing capacity-based and on-demand compute and storage resource billable usage. Don't use for root-cause diagnosis or symptom troubleshooting when the cause is unknown (use bigquery-troubleshooting first), or for writing or optimizing business logic SQL (use bigquery-optimization).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-observability\SKILL.md`

#### `bigquery-optimization`
Provides workflows to optimize BigQuery environments (capacity planning, editions), storage assets (partitioning, clustering, storage lifecycles, billing models), and SQL queries. Use when optimizing cost, modeling Edition migrations, rightsizing reservations, evaluating logical vs. physical storage, designing table partitioning/clustering, generating table DDL, migrating unpartitioned tables, managing partition expiration, optimizing individual SQL queries, or evaluating acceleration structures (search indexes, materialized views, BI Engine). Do not use for raw usage reporting (use bigquery-observability), query execution plan analysis, error troubleshooting, or diagnosing why a specific job was slow (use bigquery-troubleshooting).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-optimization\SKILL.md`

#### `bigquery-troubleshooting`
Provides diagnostic workflows and step-by-step root-cause analysis procedures for actively broken, failing, or slow BigQuery jobs, execution graph and query plan stage bottlenecks, system performance issues, or unexpectedly expensive workloads. Use when interpreting symptoms, isolating bottlenecks, diagnosing cost spikes (on-demand query spend, capacity slot autoscaling, storage growth), execution graph stages or substep variables, identifying root causes, and determining remediation steps. Don't use for writing or optimizing SQL, proactive capacity planning, or storage layout design (use bigquery-optimization), or when the user already knows which telemetry they want and just needs the query (use bigquery-observability).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-troubleshooting\SKILL.md`

#### `bigtable-basics`
Provisions instances and tables, designs performant schemas, and queries data in Bigtable. Use when designing Bigtable row keys, configuring column families, writing SQL queries or client library code (Java, Go, Python) for Bigtable, or diagnosing performance/hotspotting issues. Also use when provisioning Bigtable clusters using gcloud or cbt CLIs. Don't use for generic Cloud SQL administration.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\bigtable-basics\SKILL.md`

#### `building-data-apps`
Build modern data apps, dashboards, and interactive reports using either React + Vite or Streamlit. Includes optional Gemini Data Analytics chat integration for an AI powered "chat with your data" experience. Relevant when any of the following conditions are true: 1. User explicitly requests to build a data dashboard, data application, or visualization UI, and the UI pulls data from a GCP database (defaulting to BigQuery unless otherwise specified). 2. You need to generate a frontend web application to interact with, query, and visualize data from GCP data sources. 3. User wants to build a "chat with your data" experience or integrate the Gemini Data Analytics chat API into a web interface. Do NOT use when any of the following conditions are true: 1. The request is for building backend-only services. 2. The request is for simple CLI scripts or command-line applications. 3. The web application is not data-centric or does not involve visualizing/querying data from GCP sources.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\building-data-apps\SKILL.md`

#### `cloud-databases-onboarding`
Guides users through discovering their database requirements, recommends a Google Cloud database product or migration destination based on a recommendation matrix, and assists in database creation. Use when a user asks 'What database service should I use?', 'Help me pick a database', asks which Google Cloud database to migrate or onboard a workload to, or wants to create a new database on Google Cloud. Don't use for general Google Cloud maintenance, managing existing databases, or troubleshooting active Database Migration Service (DMS) jobs.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\cloud-databases-onboarding\SKILL.md`

#### `dak-setup`
Configures (or reconfigures) the Google Cloud Data Agent Kit (DAK) plugin by checking gcloud and ADC credentials, collecting the GCP project ID, region, and services, and running its bundled `dak-setup` script. Use this proactively and without waiting to be asked whenever a SessionStart hook or any other system/context message reports that the Data Agent Kit plugin is not configured, is missing configuration, or needs to be reconfigured. Also use it whenever the user mentions setting up, configuring, reconfiguring, or changing the project, region, or service integrations for the Data Agent Kit or DAK plugin — even if they phrase it casually, like "dak isn't working" or "I want to enable more GCP service integrations".

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\dak-setup\SKILL.md`

#### `data-autocleaning`
Automated data quality and transformation capabilities for Dataform/dbt/BigQuery pipelines. Processes data sourced from BigQuery or Cloud Storage (GCS), applying best practices for data ingestion, movement, schema mapping, and comprehensive data cleaning.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\data-autocleaning\SKILL.md`

#### `dataform-bigquery`
Expertise in generating clean, correct, and efficient Dataform pipeline code for BigQuery ELT. Use this when creating or modifying Dataform pipelines, actions, or source declarations, when Dataform, SQLX, or BigQuery are mentioned in a transformation, when data needs to be ingested from GCS into BigQuery via Dataform, or when setting up a new Dataform project or configuring workflow_settings.yaml.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\dataform-bigquery\SKILL.md`

#### `dbt-bigquery`
Expert guidance for creating, modifying, and optimizing dbt pipelines for BigQuery. Use this skill whenever user asks for generating or modifying a dbt model or project. Activate this skill when the user - Creates, modifies, or troubleshoots **dbt models or pipelines** - Needs to **optimize SQL** within a dbt project - Is **setting up a new dbt project** or configuring existing one

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\dbt-bigquery\SKILL.md`

#### `discovering-gcp-data-assets`
Finds and inspects data assets within Google Cloud. Relevant when any of the following conditions are true: 1. The user request involves finding, exploring, or inspecting data assets in Google Cloud, such as: - BigQuery datasets, tables, or views - BigLake catalog or tables - Spanner instances, databases or tables - etc. 2. You need to retrieve the schema, metadata, or governance policies for a GCP data asset. 3. You have a keyword or topic (e.g., "sales data") but lack the specific table or resource ID. 4. You are attempting to find data using `bq ls`, as this skill offers a superior approach. Don't use when: - Assets are outside Google Cloud

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\discovering-gcp-data-assets\SKILL.md`

#### `enforcing-resource-attribution`
Enforces resource attribution for CLI commands. Use this skill whenever you are running `bq` or `gcloud` commands via `run_command`. It ensures mandatory labeling for supported `bq` operations while avoiding invalid flags on read-only commands.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\enforcing-resource-attribution\SKILL.md`

#### `federate-lakehouse-catalog`
Sets up Google Cloud Lakehouse federated catalogs to remote Iceberg REST Catalogs. Currently supported catalogs: Databricks Unity, AWS Glue. Supported clouds hosting those catalogs: GCP, AWS. The primary use case is connecting to remote data to query it from GCP engines (BigQuery, Spark). Examples of when to use this: "federate my lakehouse catalog to databricks", "query data in databricks", "query data in s3", "connect to aws glue". Do NOT use for direct remote database SQL execution (e.g., Databricks SQL) or managing remote clusters and infrastructure (e.g., Databricks clusters, AWS Glue jobs).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\federate-lakehouse-catalog\SKILL.md`

#### `finding-google-skills`
Google platform decision and setup guidance, loaded on demand from Google's skill catalog. Use when a developer is choosing or setting up part of their stack, such as where to run a service, a database, storage, messaging, authentication, analytics, ads, or AI model serving, and a Google product is a reasonable candidate - whether or not a vendor is named - or when a request names a Google product or API. Brings in the matching Google skill so the answer can weigh Google options, their trade-offs, and when they are not the right fit. Skip when the stack is already settled on another provider and no Google product is named, or the task involves no platform choice.

- Source: `C:\Users\chase\.gemini\config\plugins\google-cloud-developer\skills\finding-google-skills\SKILL.md`

#### `gcloud`
Provides safety-critical validation, guardrails, and data reduction for gcloud CLI operations across Google Cloud Platform (GCP) services and infrastructure. Use when planning, generating, constructing, proposing, describing, or executing any gcloud CLI commands - including when answering questions about gcloud syntax, or formatting flags. Don't use when writing Google Cloud client library code or raw REST/gRPC API requests.

- Source: `C:\Users\chase\.gemini\config\plugins\google-cloud-developer\skills\gcloud\SKILL.md`

#### `gcp-composer-troubleshooting`
Provides expert guidance for troubleshooting Cloud Composer (Apache Airflow) and Orchestration pipelines. Use this skill when the user asks to generate Root Cause Analysis (RCA), troubleshoot or fix a failed pipeline, DAG in Composer environment and generate RCA report. '

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-composer-troubleshooting\SKILL.md`

#### `gcp-data-pipelines`
Primary entry point for building, managing, and orchestrating data pipelines on Google Cloud. Guides users to the appropriate skill for dbt, Dataflow (Apache Beam), Dataform, Spark (Dataproc Serverless), BigQuery Data Transfer Service (DTS) or orchestration pipeline using Cloud Composer. Clarify requirements and resolve ambiguity for creating, updating and running data pipelines. '

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-data-pipelines\SKILL.md`

#### `gcp-dataflow`
Guides writing, packaging, executing, and troubleshooting Apache Beam pipelines on Dataflow. Use when creating new pipelines, configuring Flex Templates, or analyzing performance of Dataflow jobs. Capabilities include Java/Python/Go setup, Cloud Build integration, and deep diagnostic analysis of job health and autoscaling. Use when: - Creating an Apache Beam Dataflow pipeline. - Creating a Google Dataflow Flex Template. - Using an existing Google Dataflow Template. - Debugging Dataflow pipeline - Troubleshooting Dataflow pipeline - Analyzing Performance of Dataflow pipeline. Key capabilities: Java/Python/Go project setup, Flex Templates (with Cloud Build), and diagnostics for streaming job health, bottlenecks, and autoscaling. Do NOT use for: - General GCP resource management unrelated to Dataflow. - Issues with other GCP services (e.g., GCE, GCS, BigQuery) unless directly impacting Dataflow pipeline execution. - Pipeline technologies other than Apache Beam on Dataflow.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-dataflow\SKILL.md`

#### `gcp-managed-airflow-dag-authoring`
Guides the authoring and validation of Apache Airflow DAGs for Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers environment context discovery, Airflow 2 vs 3 compatibility, authoring best practices, and local/remote validation processes. Use when creating or extending an Airflow DAG. Don't use when authoring Python code unrelated to Airflow DAGs.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-managed-airflow-dag-authoring\SKILL.md`

#### `gcp-managed-airflow-migrations`
Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers migration to Airflow 2.11.1 (MSAA Gen 2 and 3) and Airflow 3 (MSAA Gen 3), including environment inspection, GCS download/upload and scanning patterns for breaking changes.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-managed-airflow-migrations\SKILL.md`

#### `gcp-managed-airflow-recommendations`
Provides recommendations and best practices for creating, configuring, tuning and optimizing Managed Service for Apache Airflow (MSAA, Cloud Composer) environments. Use when the user asks for guidance, recommendations, or best practices on configuring Cloud Composer, scaling Airflow environments, preventing workload restarts, or analyzing system health.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-managed-airflow-recommendations\SKILL.md`

#### `gcp-managed-spark-upgrades`
Upgrades Spark workloads on Google Cloud Managed Service for Apache Spark (formerly known as Dataproc) clusters and Serverless to a newer image or runtime version. Supports static compatibility analysis, code upgrade, build checks against the target version, and optional verification runs. Use when: - Upgrading Managed Spark versions (major, minor, or sub-minor) or assessing upgrade readiness. Example prompt: "Upgrade Managed Spark job [job_id] in project [project_id], region [region] to target version [target_version]. Code location: [local path or GCS path]. Target GCS path: [gcs_target_path]" Don't use when: - Writing new Spark code. - Migrating non-Spark workloads (e.g., Hive/Flink to Spark). - Troubleshooting a failed Spark job that is not part of an upgrade. Limitation: This skill does not support data/result validation currently.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-managed-spark-upgrades\SKILL.md`

#### `gcp-pipeline-orchestration`
This skill helps the agent generate or update orchestration pipeline definitions for Google Cloud Composer to initialize orchestration pipeline or update the orchestration definition for orchestration of various data pipelines, like dbt pipelines, notebooks, Spark jobs, Dataform, Python scripts, Vertex AI custom jobs, Machine Learning training, or inline BigQuery SQL queries. This skill also helps deploy and trigger orchestration pipelines.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-pipeline-orchestration\SKILL.md`

#### `gcp-pipeline-resource-provisioning`
Automates declarative resource creation and provisioning for data pipelines, supporting BigQuery, Dataform, Dataproc, BigQuery Data Transfer Service (DTS), and other resources. It manages environment-specific configurations (dev, staging, prod) through a deployment.yaml file. Use when: - Modifying or creating deployment.yaml for deployment settings. - Resolving environment-specific variables (e.g., Project IDs, Regions) for deployment. - Provisioning supported infrastructure like BigQuery datasets/tables, Dataform resources, or DTS resources via deployment.yaml. Do not use when: - Resources already exist. - Managing resources not supported by `gcloud beta orchestration-pipelines resource-types list`. - Managing general cloud infrastructure (VMs, networks, Kubernetes, IAM policies), which are better suited for Terraform. - Infrastructure spans multiple cloud providers (AWS, Azure, etc.). - Already uses Terraform for the target resources.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-pipeline-resource-provisioning\SKILL.md`

#### `gcp-spark`
Authors, optimizes, and runs PySpark and Spark code on Google Cloud Managed Spark (Dataproc Serverless, clusters, and Spark Connect). Use when: - Authoring or running Spark/PySpark notebooks in any kernel (Local Kernel with spark-remote templates, Remote Spark / Remote Kernel, ManagedSparkSession, Spark Connect). - Querying, transforming, or writing data with PySpark or Spark SQL, including Apache Iceberg / BigLake Iceberg tables, BigQuery, GCS, Spanner, or Cloud SQL. - Building PySpark ETL pipelines, machine learning workloads, or batch jobs. - Managing Dataproc clusters, serverless batches, or interactive sessions. - Optimizing PySpark or Spark SQL queries for performance, memory, and OOM prevention. Do NOT use when: - Auditing multi-region fleet inventory, DCU/cost consumption, idle/zombie clusters, or workload observability (use @skill:gcp-spark-observability). - Troubleshooting failed Spark jobs or Dataproc batches (use @skill:gcp-spark-troubleshooting).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-spark\SKILL.md`

#### `gcp-spark-observability`
Monitors, inventories, and assesses Google Cloud Managed Service for Apache Spark (Dataproc Serverless and Dataproc on Compute Engine) environments, clusters, batches, jobs, sessions, metrics, logs, costs, and configurations across single and multiple regions. Use when listing active or historical Spark workloads, discovering failed batches or jobs, auditing multi-region fleet inventory, calculating Serverless compute (DCU-Hours) and shuffle storage consumption, detecting idle or zombie clusters, inspecting scheduled pipeline cadence health, investigating failed cluster operations or stockouts, checking quotas and alerting coverage, or querying Cloud Monitoring and Cloud Logging telemetry. Don't use for deep root-cause analysis or performance optimization of a specific job or batch (use gcp-spark-troubleshooting), authoring new PySpark code (use gcp-spark), or upgrading Spark versions (use gcp-managed-spark-upgrades).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-spark-observability\SKILL.md`

#### `gcp-spark-troubleshooting`
Provides expert guidance for troubleshooting Google Cloud Spark and Dataproc workloads (Dataproc Serverless batches and standard Dataproc clusters), and inspecting, streaming, searching, tailing, or summarizing Spark driver outputs and event logs in Cloud Storage. Use when the user asks to debug, troubleshoot, diagnose, or perform Root Cause Analysis (RCA) on failed Spark jobs, PySpark batches, or Spark event logs.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcp-spark-troubleshooting\SKILL.md`

#### `gcs-security-assessment`
Assesses the security posture of Google Cloud Storage (GCS) buckets and projects. Grounds every finding in gathered telemetry, evaluates buckets against Google security best practices (public access, IAM over-granting, CMEK, VPC Service Controls, audit logging), and correlates signals to flag toxic combinations of individually low-risk settings, with actionable remediation. Use whenever a user asks for a security scan, audit, review, vulnerability check, or compliance assessment (including SAIF) — or simply asks whether their buckets, project, or data are secure, exposed, public, or misconfigured, who can access their data, or wants storage hardened or locked down, e.g. before a launch. Don't use for diagnosing a specific access failure or 403, managing or configuring storage, investigating a live outage, or non-GCS resources (Compute Engine, GKE, etc.).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\gcs-security-assessment\SKILL.md`

#### `gemini-api-dev`
Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generation, video generation, speech generation (TTS), voice design, voice replication, streaming responses, background research tasks, function calling, structured output, or migrating from the old generateContent API. Covers SDK usage and best practices for Gemini models and agents in Python and TypeScript.

- Source: `C:\Users\chase\.gemini\config\plugins\gemini-api\skills\gemini-api-dev\SKILL.md`

#### `gemini-live-api-dev`
Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migrating legacy Live models (2.0/2.5/3.1) to Gemini 3.8 Live. Covers WebSocket-based audio/video/text streaming, voice activity detection (VAD), background reasoning (extended thinking), asynchronous function calling, session management, ephemeral tokens, live transcription, and live translation. SDKs covered - google-genai (Python), @google/genai (JavaScript/TypeScript).

- Source: `C:\Users\chase\.gemini\config\plugins\gemini-api\skills\gemini-live-api-dev\SKILL.md`

#### `gemini-omni-flash-api`
Use this skill for generative video editing, text-to-video, image- and video-referenced video generation, first-frame-to-video, first-and-last-frame transitions, and video extensions using Gemini Omni 1.2 Flash (gemini-omni-1.2-flash) via the official google-genai SDK. Includes workflows for pre-processing/optimizing high-resolution or long source videos with ffmpeg, stripping audio for full sound regeneration, and handling turn-by-turn video editing and parallel execution.

- Source: `C:\Users\chase\.gemini\config\plugins\gemini-api\skills\gemini-omni-flash-api\SKILL.md`

#### `google-cloud-recipe-auth`
Provides expert guidance on Identity and Access Management (IAM) and authenticating and authorizing to Google Cloud services and APIs, covering human users, service identities, Application Default Credentials (ADC), and best practices for secure access.

- Source: `C:\Users\chase\.gemini\config\plugins\google-cloud-developer\skills\google-cloud-recipe-auth\SKILL.md`

#### `google-cloud-recipe-onboarding`
Guides a developer's first steps on Google Cloud, covering account creation, billing setup, project management, and deploying a first resource. Use when a new developer wants to initialize their first Google Cloud project, configure billing, and verify deployment. Don't use for enterprise organization setup (use Google Cloud Setup guided flow for that instead). Don't use for complex multi-project architectures.

- Source: `C:\Users\chase\.gemini\config\plugins\google-cloud-developer\skills\google-cloud-recipe-onboarding\SKILL.md`

#### `google-cloud-storage-basics`
Stores, retrieves, and manages data as objects in Cloud Storage on Google Cloud (also known colloquially as GCS) buckets. Use when you need to interact with Cloud Storage — set up a Storage MCP server (remote or local Toolbox), create or configure buckets, upload, download, stream, or transfer data, organize objects with folders, generate signed URLs, control access (IAM, ACLs, public access prevention), set storage classes (Standard, Nearline, Coldline, Archive), manage lifecycle and cost, protect data (versioning, CMEK, retention, Bucket Lock, holds, soft delete), host static websites, trigger Pub/Sub notifications, mount buckets (gcsfuse), or optimize performance. Covers gcloud storage / gsutil, JSON/XML APIs, client libraries, Terraform, and Cloud Storage MCP servers. Don't use for generic MCP setup that doesn't mention Cloud Storage, other MCP servers, block storage (Persistent Disk), BigQuery, or databases (Cloud SQL, Spanner, Bigtable, Firestore).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\google-cloud-storage-basics\SKILL.md`

#### `google-cloud-storage-bucket-architect`
Creates Cloud Storage (Google Cloud Storage, or GCS) buckets. Analyzes the workload (sensitive data, media hosting, ingestion, web hosting, archiving, backup, logging, analytics, AI/ML, or general-purpose), validates project-level security settings, and designs a secure-by-default, cost-effective configuration (location, storage class, uniform bucket-level access, public access prevention, soft delete, lifecycle) before creating it. Use whenever a user wants to create, make, set up, provision, or spin up a bucket, or needs object storage for an app, service, pipeline, or dataset — even a "simple" or "default" bucket, or when bucket creation is one step in a larger workflow. Outputs or executes the creation via gcloud, the JSON/REST API, Terraform, or SDK client libraries (C++, Java, Python, Go). Don't use for anything other than creating new buckets — for uploads, downloads, access changes, or reconfiguring existing buckets, use google-cloud-storage-basics.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\google-cloud-storage-bucket-architect\SKILL.md`

#### `google-cloud-storage-fuse`
Mounts Cloud Storage buckets as a POSIX file system with Cloud Storage FUSE (gcsfuse). Use when you need to interact with gcsfuse — decide whether FUSE, native gs:// reads, or Filestore/Managed Lustre fits a workload, deploy tuned mounts on GKE, Compute Engine, or Cloud Run, enable and size the file, stat, and list caches, tune mount flags (--implicit-dirs) or config-file settings, apply workload profiles, keep ML checkpointing safe (rename atomicity, hierarchical namespace, close-time finalization, concurrent writers), or diagnose slow training, low throughput, or GCS bill spikes on existing mounts with gcsfuse metrics. Covers mount semantics, the gcsfuse CLI and config file, the GKE gcsfuse CSI driver (Workload Identity principal:// bindings, profile StorageClasses, sidecar sizing), and Cloud Run volume mounts. Don't use for bucket administration or data management without a mount (google-cloud-storage-basics) or for fully POSIX-compliant shared file systems (Filestore, Managed Lustre; use gke-storage).

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\google-cloud-storage-fuse\SKILL.md`

#### `resolving-mcp-region-configs`
Mandatory Step 0 pre-flight check for regional Google Cloud MCP servers (e.g. Dataproc) before using MCP tools or falling back to gcloud/bq CLI. Use whenever interacting with Dataproc clusters, Spark batches, jobs, sessions, or regional GCP resources. Fixes regional MCP servers whose endpoint URL still has an unreplaced $GCP_REGION / ${REGION} placeholder across Claude Code, Codex, and Antigravity. Trigger: an expected mcp__*_{service}_* tool is missing entirely (not just failing), or a call to one fails/hangs on a malformed host. Check via ToolSearch/deferred-tools listing before falling back to gcloud/bq CLI. Asks the user for a region, patches the live MCP config file(s), and tells the user how to restart without losing session context.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\resolving-mcp-region-configs\SKILL.md`

#### `retrieving-developer-knowledge`
Searches, retrieves, and synthesizes official Google developer documentation across Google Cloud, AI/Gemini, Android, Chrome, Web, Flutter, Go, Firebase, and other Google developer platforms. Integrates with the Developer Knowledge MCP server (search_documents, get_documents, answer_query) or the Developer Knowledge REST API fallback. Use when searching for gcloud CLI commands, API syntax, IAM permissions, official documentation, architectural comparisons, or product choice overviews. Don't use for local filesystem lookups or non-Google documentation.

- Source: `C:\Users\chase\.gemini\config\plugins\google-cloud-developer\skills\retrieving-developer-knowledge\SKILL.md`

#### `schema-mapping`
Guides the process of analyzing, mapping, and documenting transformations between source and target schemas for any database, data warehouse, or data platform. Focuses exclusively on creating a high-fidelity mapping plan (Mapping Manifesto). Used when initiating an ETL, ELT, or data integration task with schema mapping specification for multiple tables (i.e. more than 3 tables) before writing code. Do NOT use this skill for basic SQL generation without mapping requirements, or when the user already has a complete mapping specification.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\schema-mapping\SKILL.md`

### Firebase & Backend Services (12 skills)

#### `extension-to-functions-codebase`
Skill for converting an installed Firebase Extension (or extension source) into a standalone Cloud Functions for Firebase codebase or publishable npm package, including V1 to V2 trigger upgrades, lifecycle hooks, and declarative security

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\extension_to_functions_codebase\SKILL.md`

#### `firebase-ai-logic-basics`
Official skill for integrating Firebase AI Logic (Gemini API) into web applications. Covers setup, multimodal inference, structured output, and security.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_ai_logic_basics\SKILL.md`

#### `firebase-app-hosting-basics`
Deploys and manages full-stack web applications (Next.js, Angular) with Server-Side Rendering (SSR) using Firebase App Hosting. Use when deploying Next.js/Angular apps, configuring apphosting.yaml or firebase.json apphosting blocks, managing secrets, setting up GitHub CI/CD, or configuring Blaze billing requirements. Don't use for classic static web hosting, Auth, Firestore, Crashlytics, or Xcode.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_app_hosting_basics\SKILL.md`

#### `firebase-auth-basics`
Guide for setting up and using Firebase Authentication. Use this skill when the user's app requires user sign-in, user management, or secure data access using auth rules.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_auth_basics\SKILL.md`

#### `firebase-basics`
Provides foundational Firebase CLI setup, CLI installation, version checks (`firebase-tools@latest --version`), CLI login (including --no-localhost), project creation, project selection (`firebase use`), and app config file downloads (`google-services.json`, `GoogleService-Info.plist`). Use ONLY for CLI login, project creation/switching, or downloading app config files. Don't use for Firebase Hosting deploy, Firestore, Auth, App Hosting, Data Connect, Crashlytics, or Remote Config.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_basics\SKILL.md`

#### `firebase-crashlytics`
Comprehensive guide for Firebase Crashlytics, including provisioning and SDK usage. Use this skill when the user needs help setting up Crashlytics, adding crash reporting, or using the Crashlytics SDK in their application.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_crashlytics\SKILL.md`

#### `firebase-data-connect`
Builds and deploys Firebase SQL Connect (aka Firebase Data Connect) backends with PostgreSQL securely. Use when designing schemas with tables and relations, writing authorized queries and mutations, configuring real-time data updates, or generating type-safe SDKs. Use when you need a relational database with Firebase, or when the user mentions SQL Connect or Data Connect.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_data_connect_basics\SKILL.md`

#### `firebase-firestore`
Sets up, manages, queries, and configures Cloud Firestore databases (Standard/Enterprise edition), including data modeling, security rules, indexes, and SDK integrations (Web, Python, iOS, Android, Flutter). Use when creating/listing Firestore databases, defining data models/indexes, writing SDK queries, or integrating Firestore SDKs. For authoring or modifying Firestore Security Rules (firestore.rules), delegate to the firestore-rules-author subagent if subagent delegation is available, or use firestore-rules-creation otherwise. Don't use for Firebase Hosting, Data Connect, Auth, Storage/GCS, Crashlytics, Functions, or BigQuery.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_firestore\SKILL.md`

#### `firebase-hosting-basics`
Deploys and configures classic Firebase Hosting for static websites, single-page apps (SPAs), and microservices. Use when deploying static sites/SPAs, setting up custom domains, configuring firebase.json hosting settings (redirects, rewrites, headers, multi-site), or managing preview channels. Don't use for Firebase App Hosting (Next.js/SSR), Auth, Firestore queries/rules, Data Connect, or Crashlytics.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_hosting_basics\SKILL.md`

#### `firebase-remote-config-basics`
Manages Firebase Remote Config templates, feature flags, loading strategies, and SDKs (Android, iOS). Use when downloading/deploying remoteconfig JSON templates, managing version history/feature flags, setting in-app defaults, fetchAndActivate(), real-time listeners, or SDK setup. Don't use for Firebase Hosting, Auth, Firestore, Data Connect, Crashlytics, or App Hosting.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_remote_config_basics\SKILL.md`

#### `firebase-security-rules-auditor`
Audits Firebase (Firestore, Cloud Storage) security rules for vulnerabilities, privilege escalation, role bypasses, create vs update inconsistencies, resource exhaustion, type safety, size limits, and hasOnly ownership checks. Use when auditing/reviewing rules, running red-team rule assessments, or scoring against auditor checklists. Don't use for Firebase CLI (login, deploy), Auth, Crashlytics, Remote Config, or database queries.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firebase_security_rules_auditor\SKILL.md`

#### `firestore-rules-creation`
Designs, authors, refactors, and hardens production-grade Cloud Firestore Security Rules (firestore.rules). IMPORTANT: If subagent delegation AND the firestore-rules-author subagent are available in your environment, delegate authoring firestore.rules to the firestore-rules-author subagent. If subagent delegation is unavailable (e.g. not enabled in the IDE), firestore-rules-author is not installed, or you are running inside firestore-rules-author, follow this skill directly.

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\firestore_rules_creation\SKILL.md`

### Flutter & Mobile App Development (29 skills)

#### `android-cli`
Provides instructions for installing and using the `android` CLI. The `android` command-line tool is a critical tool for Android development and helps you create new Android projects, run Android apps on devices, manage and interact with Android virtual devices (including screenshots and UI inspection), manage Android SDK components, look up official Android documentation, and discover and install official Android skills.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\SKILL.md`

#### `android-device-hub`
Instructions for working with the Android Device Hub sidecar, which lists, starts, stops, creates and removes Android Virtual Devices (AVDs), lists physical devices connected to adb, and lets the user mirror and control any of them (video, touch, keyboard, mouse wheel) in the Device Hub pane. Also explains how to inspect and interact with the screen the user is mirroring, with `android layout`, `android screen` and `adb`.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\device-hub\SKILL.md`

#### `compose-preview`
Instructions for the Android Compose Preview sidecar, which renders Jetpack Compose @Preview functions with `android preview render` and shows them in the Android Compose Preview pane. Use it when the user wants to see a Compose preview, or to review the result of UI changes — re-render after changing the code so that the pane shows the result.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\compose-preview\SKILL.md`

#### `dart-add-unit-test`
Write and organize unit tests for functions, methods, and classes using `package:test`. Use when creating new logic or fixing bugs to ensure code remains correct and regression-free.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-add-unit-test\SKILL.md`

#### `dart-build-cli-app`
Architectural patterns, entrypoint structure, exit codes, stream routing, and subprocess spawning for Dart command-line interface (CLI) applications. Use when building CLI tools, console utilities, scripts, argument parsing with `package:args` (ArgParser or CommandRunner), handling exit codes, configuring executables in pubspec.yaml, spawning Dart subprocesses, or compiling native CLI binaries. Don't use for Flutter UI widgets, web applications, or standalone HTTP backend servers.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-build-cli-app\SKILL.md`

#### `dart-collect-coverage`
Collect coverage using the coverage packge and create an LCOV report

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-collect-coverage\SKILL.md`

#### `dart-fix-runtime-errors`
Uses get_runtime_errors and lsp to fetch an active stack trace, locate the failing line, apply a fix, and verify resolution via hot_reload.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-fix-runtime-errors\SKILL.md`

#### `dart-generate-test-mocks`
Define and generate mock objects for external dependencies using `package:mockito` and `build_runner`. Use when unit testing classes that depend on complex external services like APIs or databases.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-generate-test-mocks\SKILL.md`

#### `dart-migrate-to-checks-package`
Replace the usage of `expect` and similar functions from `package:matcher` to `package:checks` equivalents.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-migrate-to-checks-package\SKILL.md`

#### `dart-resolve-package-conflicts`
Workflow for fixing package version conflicts. Use this when `pub get` fails due to incompatible package versions.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-resolve-package-conflicts\SKILL.md`

#### `dart-run-static-analysis`
Execute `dart analyze` to identify warnings and errors, and use `dart fix --apply` to automatically resolve mechanical lint issues. Use during development to ensure code quality and before committing changes.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-run-static-analysis\SKILL.md`

#### `dart-setup-ffi-assets`
Guides agents in compiling and packaging C/C++ source code into dynamic or static libraries (Code Assets) using Dart's Native Assets hook system (via hook/build.dart and hook/link.dart utilizing package:hooks and package:native_toolchain_c). Use when a user asks to: 'setup native assets', 'compile C/C++ source code', 'bundle dynamic libraries', 'build native C code', 'link native assets', 'implement build.dart or link.dart hooks', or 'integrate C/C++ interop in Dart/Flutter'. Helps agents avoid manual toolchain orchestration and configures secure hash-validated binary downloads or advanced linker tree-shaking with package:record_use mapping.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-setup-ffi-assets\SKILL.md`

#### `dart-use-doc-examples`
How to inject external code examples into Dartdoc using the {@example} directive, and how to filter those files using #hide, #region, and #endregion tags.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-use-doc-examples\SKILL.md`

#### `dart-use-ffigen`
Guide agents to use `package:ffigen` to automatically generate FFI bindings instead of writing them manually. Use this skill when a task involves writing new FFI bindings, extending C/Objective-C/Swift integrations, or replacing hand-crafted `dart:ffi` setups.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-use-ffigen\SKILL.md`

#### `dart-use-path-package`
Cross-platform file and directory path manipulation, segment splitting, extension extraction, and context conversion using `package:path` and `package:file`. Use when writing, inspecting, joining, splitting, or refactoring file paths, directory names, or extensions, or replacing raw string path operations (`.split('/')`, `'$dir/$file'`, `.endsWith('.ext')`, `.replaceAll('\\', '/')`). Don't use for HTTP network URI routing, database query strings, or non-path string processing.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-use-path-package\SKILL.md`

#### `dart-use-pattern-matching`
Applies Dart 3 pattern matching, switch expressions, and destructuring idiomatically to validate data schemas, handle algebraic data types, and decompose control flow. Use when refactoring complex if-else chains, parsing polymorphic JSON or API responses, destructuring Lists, URI/path segments, String.split() tokens, Records, or Maps, or enforcing exhaustiveness on sealed classes. Don't use for simple boolean conditions, single-variable type promotion (use `is`), or basic collection filtering.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-use-pattern-matching\SKILL.md`

#### `dart-use-primary-constructors`
Help users write syntactically and semantically correct primary constructors in Dart, and migrate/use the new constructor syntax, empty-body semicolon syntax, in-body initializer list syntax, and abbreviated concise constructor syntax.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-use-primary-constructors\SKILL.md`

#### `dart-write-documentation`
Rules and formatting guidelines for writing Dart /// API documentation and doc comments. Use when documenting Dart code, writing doc comments for any Dart declaration (libraries, classes, methods, variables, etc.), or when instructed to follow the Effective Dart documentation guidelines.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\dart-write-documentation\SKILL.md`

#### `flutter-add-integration-test`
Configures Flutter Driver for app interaction and converts MCP actions into permanent integration tests. Use when adding integration testing to a project, exploring UI components via MCP, or automating user flows with the integration_test package.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-add-integration-test\SKILL.md`

#### `flutter-add-widget-preview`
Adds interactive widget previews to the project using the previews.dart system. Use when creating new UI components or updating existing screens to ensure consistent design and interactive testing.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-add-widget-preview\SKILL.md`

#### `flutter-add-widget-test`
Implement a component-level test using `WidgetTester` to verify UI rendering and user interactions (tapping, scrolling, entering text). Use when validating that a specific widget displays correct data and responds to events as expected.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-add-widget-test\SKILL.md`

#### `flutter-apply-architecture-best-practices`
Architects a Flutter application using the recommended layered approach (UI, Logic, Data). Use when structuring a new project or refactoring for scalability.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-apply-architecture-best-practices\SKILL.md`

#### `flutter-build-responsive-layout`
Use `LayoutBuilder`, `MediaQuery`, or `Expanded/Flexible` to create a layout that adapts to different screen sizes. Use when you need the UI to look good on both mobile and tablet/desktop form factors.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-build-responsive-layout\SKILL.md`

#### `flutter-fix-layout-issues`
Fixes Flutter layout errors (overflows, unbounded constraints) using Dart and Flutter MCP tools. Use when addressing "RenderFlex overflowed", "Vertical viewport was given unbounded height", or similar layout issues.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-fix-layout-issues\SKILL.md`

#### `flutter-implement-json-serialization`
Create model classes with `fromJson` and `toJson` methods using `dart:convert`. Use when manually mapping JSON keys to class properties for simple data structures.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-implement-json-serialization\SKILL.md`

#### `flutter-setup-declarative-routing`
Configure `MaterialApp.router` using a package like `go_router` for advanced URL-based navigation. Use when developing web applications or mobile apps that require specific deep linking and browser history support.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-setup-declarative-routing\SKILL.md`

#### `flutter-setup-localization`
Add `flutter_localizations` and `intl` dependencies, enable "generate true" in `pubspec.yaml`, and create an `l10n.yaml` configuration file. Use when initializing localization support for a new Flutter project.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-setup-localization\SKILL.md`

#### `flutter-use-http-package`
Use the `http` package to execute GET, POST, PUT, or DELETE requests. Use when you need to fetch from or send data to a REST API.

- Source: `C:\Users\chase\.gemini\config\plugins\flutter\skills\flutter-use-http-package\SKILL.md`

#### `xcode-project-setup`
Safely modifies Xcode projects (.pbxproj) to add Swift Packages and link files. Use this skill whenever an iOS project needs dependencies installed (e.g. Firebase, Alamofire).

- Source: `C:\Users\chase\.gemini\config\plugins\firebase\skills\xcode_project_setup\SKILL.md`

### Cloud Deployments & Serverless Architecture (60 skills)

#### `access-protected-vercel-deployment`
Access and test Vercel deployments protected by Vercel Authentication, SSO, or Deployment Protection. Use when curl, agent-browser, Playwright, or another automated request reaches a Vercel login or protection page; when a protected preview or production URL returns 401 or 403; when TRUSTED_SOURCES_ENVIRONMENT_MISMATCH appears; or when choosing between `vercel curl` and the `x-vercel-trusted-oidc-idp-token` header.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\access-protected-vercel-deployment\SKILL.md`

#### `ai-gateway`
Vercel AI Gateway guidance for setup, model discovery, authentication, routing, fallbacks, virtual models, evaluation models, BYOK, budgets, spend reporting, observability, compatible APIs, and coding-agent configuration. Use when adding AI Gateway to an app, migrating provider calls, choosing models or providers, centralizing model configuration, evaluating application state, debugging gateway requests, or running `vercel ai-gateway` commands.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\ai-gateway\SKILL.md`

#### `ai-sdk`
Vercel AI SDK expert guidance. Use when building AI-powered features — chat interfaces, text generation, structured output, tool calling, agents, MCP integration, streaming, embeddings, reranking, image generation, or working with any LLM provider.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\ai-sdk\SKILL.md`

#### `auth`
Authentication integration guidance — Clerk (native Vercel Marketplace), Better Auth, Descope, and Auth0 setup for Next.js applications, plus Sign in with Vercel, Vercel Passport, and Vercel KMS. Covers server config, route handlers, proxy.ts auth patterns, sign-in/sign-up flows, and Marketplace provisioning. Use when implementing user authentication, sessions, protected routes, or protecting deployments.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\auth\SKILL.md`

#### `auth0`
Use when adding, fixing, or improving how an app authenticates users or protects an API, or when using or configuring any Auth0 feature — signing users in and out, sessions and tokens, guarding routes and endpoints, MFA, passwordless passkey login (WebAuthn), SSO, Organizations, RBAC, custom domains, Universal Portals for hosted account and organization self-service, or Universal Login branding. Also use to audit a tenant's health, security, and plan fit (CheckMate), to debug why an auth flow fails, to migrate from another auth provider, or to set up the Vercel native integration. Covers any web, mobile, or backend framework and every Auth0 SDK, tool, and API. Use even if the user never mentions Auth0.

- Source: `C:\Users\chase\.gemini\config\plugins\auth0\skills\auth0\SKILL.md`

#### `base44-cli`
The base44 CLI is used for EVERYTHING related to base44 projects: resource configuration (entities, backend functions, realtime actors, ai agents), initialization and actions (resource creation, deployment), and any other operation on an existing app or workspace through the Base44 public API (settings, domains, users, members, source export). This skill is the place for learning about how to configure resources, including actors — the realtime/WebSocket primitive behind multiplayer, collaborative boards, presence and live cursors, in-room chat, and live auctions. When you plan or implement a feature, you must learn this skill

- Source: `C:\Users\chase\.gemini\config\plugins\base44\skills\base44-cli\SKILL.md`

#### `base44-sdk`
The base44 SDK is the library to communicate with base44 services. In projects, you use it to communicate with remote resources (entities, backend functions, realtime actors, ai agents, and the AI gateway for code agents, image, video, and speech generation, and AI decisions) and to write backend functions and actors. This skill is the place for learning about available modules and types, including actors — the realtime/WebSocket primitive for multiplayer, collaborative boards, presence and live cursors, in-room chat, and live auctions. When you plan or implement a feature, you must learn this skill

- Source: `C:\Users\chase\.gemini\config\plugins\base44\skills\base44-sdk\SKILL.md`

#### `base44-troubleshooter`
Troubleshoot production issues using backend function logs and workflow run history. Use when investigating app errors, debugging function calls, diagnosing why a scheduled job or automation failed, or diagnosing production problems in Base44 apps.

- Source: `C:\Users\chase\.gemini\config\plugins\base44\skills\base44-troubleshooter\SKILL.md`

#### `bootstrap`
Project bootstrapping orchestrator for repos that depend on Vercel-linked resources (databases, auth, and managed integrations). Use when setting up or repairing a repository so linking, environment provisioning, env pulls, and first-run db/dev commands happen in the correct safe order.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\bootstrap\SKILL.md`

#### `build-agents`
Default guidance for building AI agents. Use for generic requests to build, create, scaffold, design, architect, or implement an AI agent, agent app, tool-calling agent, durable agent, multi-agent system, or scheduled agent.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\build-agents\SKILL.md`

#### `cdn-caching`
Debug Vercel CDN caching — cache hit rate, stale content, revalidation behavior, ISR + PPR, per-request cache reasons (cacheReason) and PPR state (ppr_state), and costs.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\cdn-caching\SKILL.md`

#### `chat-sdk`
Vercel Chat SDK expert guidance. Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google Chat, GitHub, Linear — with a single codebase. Covers the Chat class, adapters, threads, messages, cards, modals, streaming, state management, and webhook setup.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\chat-sdk\SKILL.md`

#### `create-a-backend`
Backend architecture guidance. Use when planning, building, or migrating an API or backend; choosing between Functions, Services, containers, Daemons, Workflow, Queues, and Marketplace databases; or selecting a supported backend framework or runtime.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\create-a-backend\SKILL.md`

#### `custom-metrics`
Emit and query Vercel Custom Metrics. Use when instrumenting application or business measurements in Vercel Functions, using metric() from @vercel/functions, choosing metric names and attributes, or querying emitted values with vc metrics.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\custom-metrics\SKILL.md`

#### `daemons`
Vercel Daemons guidance — long-running background workers built from a Dockerfile and declared under the `daemons` key in vercel.json. Use when running queue consumers, Celery/Sidekiq/BullMQ workers, workflow workers, or job runners next to an app on Vercel; configuring daemon instances per region, memory, or command; handling SIGTERM; or choosing between Daemons, Functions, Queues, and Workflows.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\daemons\SKILL.md`

#### `debug-optimize-lcp`
Guides debugging and optimizing Largest Contentful Paint (LCP) using Chrome DevTools MCP tools. Use this skill whenever the user asks about LCP performance, slow page loads, Core Web Vitals optimization, or wants to understand why their page's main content takes too long to appear. Also use when the user mentions "largest contentful paint", "page load speed", "CWV", or wants to improve how fast their hero image or main content renders.

- Source: `C:\Users\chase\.gemini\config\plugins\chrome-devtools-plugin\skills\debug-optimize-lcp\SKILL.md`

#### `deployments-cicd`
Vercel deployment and CI/CD expert guidance. Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files for Vercel.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\deployments-cicd\SKILL.md`

#### `domains`
Search, register, connect, transfer, and renew domain names on Vercel using the CLI or Domains Registrar API. Use for domain availability and pricing, custom domains, DNS records, nameservers, ownership verification, and domain orders.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\domains\SKILL.md`

#### `env-vars`
Vercel environment variable expert guidance. Use when working with .env files, vercel env commands, Secret or Config variable types, OIDC tokens, or managing environment-specific configuration.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\env-vars\SKILL.md`

#### `eve`
eve framework guidance for durable AI agents and agent-powered applications. Use when creating, editing, or debugging an eve project, when the user explicitly asks for eve, or when the build-agents skill has selected eve as the default framework. Covers eve's filesystem-first runtime, durable sessions, tools, skills, connections, channels, sandboxes, subagents, schedules, evals, frontend clients, and Agent Runs observability. Do not use for incidental agent mentions, generic agent-building prompts, or established non-eve stacks unless the user asks for comparison or migration.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\eve\SKILL.md`

#### `flags-sdk`
Implement feature flags in Next.js or SvelteKit code with the Flags SDK (`flags` npm package). Use when installing or configuring the SDK, declaring flags with `flag()`, wiring a provider adapter (`@flags-sdk/vercel`, Statsig, LaunchDarkly, PostHog, GrowthBook, Global Config, OpenFeature, and others), using `identify`, `dedupe`, or `evaluate`, keeping pages static with precompute, setting up Flags Explorer, or encrypting flag values. For planning a flag, Vercel Flags rollouts and experiments, the `vercel flags` CLI, or other frameworks, use the `vercel-flags` skill.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\flags-sdk\SKILL.md`

#### `is-agentic`
Score how ready a website, domain, or public MCP endpoint is for AI agents using Is Agentic, and read or act on the resulting report. Use when asked to check a site's agent readiness, get its Is Agentic score, fetch a scored report as JSON, or fix the issues that lower a site's score.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\is-agentic\SKILL.md`

#### `knowledge-update`
Corrects outdated LLM knowledge about the Vercel platform and introduces new products. Injected at session start.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\knowledge-update\SKILL.md`

#### `marketplace`
Vercel Marketplace expert guidance — discovering, installing, and managing third-party integrations via the `vercel integration` CLI. Use when building any app that needs an external capability without a dedicated skill — commerce (stores, storefronts, selling products), payments (checkout, subscriptions, billing), observability/monitoring, messaging/email, search, or CMS — or when discovering, installing, or managing integrations.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\marketplace\SKILL.md`

#### `microfrontends`
Guide for building, configuring, and deploying microfrontends on Vercel. Use this skill when the user mentions microfrontends, multi-zones, splitting an app across teams, independent deployments, cross-app routing, incremental migration, composing multiple frontends under one domain, microfrontends.json, @vercel/microfrontends, the microfrontends local proxy, or path-based routing between Vercel projects. Also use when the user asks about shared layouts across projects, navigation between microfrontends, fallback environments, asset prefixes, or feature flag controlled routing.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\microfrontends\SKILL.md`

#### `modern-web-guidance`
Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolve rapidly and training weights contain obsolete patterns. Trigger immediately for: modals/dialogs/popovers, tables, dark mode, anchor positioning, container queries, view transitions, scroll-driven animations, parallax/reveals, forms, validation, autofill, accessibility, custom selects, scrollbars, CWV (LCP, INP, CLS), content-visibility, fetch priority, image optimization, security, passkeys, HTML sanitization, web components, dates/timezones, built-in AI, WebAssembly, standard HTML/CSS/DOM in frameworks, etc. DO NOT trigger for: backend (SQL, ORMs, API routes), infra/scripts (CI/CD, Docker, Actions, Python/Go, Git), or tooling/trivial (Vite, tsconfig, ESLint, tests, copy/renames, 3P docs), etc.

- Source: `C:\Users\chase\.gemini\config\plugins\modern-web-guidance-plugin\skills\modern-web-guidance\SKILL.md`

#### `netlify-access-control`
Picks the right Netlify site-protection layer and disambiguates the three unrelated "auth" concepts users conflate — app-user login (Netlify Identity), site-load gating (Password Protection / project visibility), and dashboard SAML SSO. Use it when asked to password-protect a site or Deploy Preview, make a project private/public, restrict a site to your team, require SSO to view a site, set up company-wide or internal-app SSO, invite users to a private project, or know which team member made a request to a private site. Also use it for SSO-session symptoms on protected sites: "logged out mid-session", 401s after about an hour, or token expiry/refresh questions. Not for wiring auth code — route app-login setup to netlify-identity.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-access-control\SKILL.md`

#### `netlify-agent-runner`
Run AI agent tasks remotely on Netlify using Claude, Codex, or Gemini. Use when the user wants to run an AI agent on their site, get a second opinion from another model, or delegate development tasks to run remotely against their repo.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-agent-runner\SKILL.md`

#### `netlify-ai-gateway`
Use Netlify AI Gateway to call OpenAI, Anthropic Claude, Google Gemini, TypeSafe (Jev), or OpenRouter-hosted models (xAI/DeepSeek/Meta/Mistral/Qwen) from Netlify Functions or Edge Functions without managing provider accounts or API keys. Reach for this when adding an AI feature to a Netlify app — a chatbot, text summarizer, image generator, joke/content generator, form-submission routing or analysis, or any LLM call — or when wiring the OpenAI/Anthropic/Gemini/TypeSafe/OpenRouter SDK into a Netlify Function, choosing which env vars to use, streaming long generations, or debugging why gateway calls fail at build time or return 401.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-ai-gateway\SKILL.md`

#### `netlify-blobs`
Store and retrieve unstructured objects, files, and cache-like state on Netlify with the @netlify/blobs module. Use when persisting user file uploads (images/documents), caching computed output from functions or Background Functions, serving downloadable assets, storing JSON blobs keyed by ID, or seeding deploy-specific data. Reach for this for key/value or object storage from Functions, Edge Functions, or Build Plugins — not for per-user, transactional, or relational data (use Netlify DB for that). Triggers include "save an uploaded file", "cache API results", "store generated site map", "key/value store for a function", or "file uploads without a database".

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-blobs\SKILL.md`

#### `netlify-caching`
Cache dynamic and static responses on Netlify's CDN from Functions, Edge Functions, and proxies. Use when you add caching or cache-control headers to a function response, tune cache TTL or stale-while-revalidate, set up the durable cache, vary a cache key by query/header/cookie/country/language, purge or invalidate the cache by site or cache tag, use the programmatic Cache API (caches.open/match/put) or @netlify/cache helpers (fetchWithCache/cacheHeaders/getCacheStatus), speed up an expensive API call, add ISR or on-demand revalidation, or debug why a response is or isn't cached via the Cache-Status header.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-caching\SKILL.md`

#### `netlify-config`
Configure Netlify builds and routing via netlify.toml, _redirects, and _headers. Use when setting a build command or publish directory, adding redirects or rewrites or proxies, adding an SPA fallback rewrite, setting custom response headers or basic auth, managing environment variables and secrets, scoping vars per deploy context, marking a var as secret, disabling secret scanning, configuring functions bundling, ignoring builds, or wiring up a monorepo or JavaScript SPA on Netlify.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-config\SKILL.md`

#### `netlify-database`
Zero-config Postgres for Netlify apps via @netlify/database — querying data from Functions/Edge Functions, writing schema migrations, setting up Drizzle ORM, local dev with netlify dev, database branches for deploy previews, and migrating an existing Postgres project onto Netlify. Use when adding a database, building a contact form or CRUD API, writing SQL migrations, wiring up Drizzle, running netlify database commands, testing with a local Postgres, or switching from Neon/Supabase/RDS to Netlify Database.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-database\SKILL.md`

#### `netlify-deploy`
Create, configure, and manage Netlify deploys from code — reach for this when setting up Git continuous deployment, running netlify deploy or netlify deploy --prod from the CLI, writing netlify.toml deploy contexts, adding a Deploy to Netlify button, wiring build hooks, configuring Deploy Previews or branch deploys, locking or skipping deploys, fixing a failed or secrets-scanning deploy, or when someone asks to "deploy my site", "set up preview deploys", "add per-branch build config", "keep staging out of Google", or "add a deploy button to my README".

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-deploy\SKILL.md`

#### `netlify-edge-functions`
Write, route, cache, and debug Netlify Edge Functions, the Deno-based TypeScript or JavaScript handlers in netlify/edge-functions that run at the network edge in front of static files and serverless functions. Activate this skill whenever someone wants to add auth middleware or a login gate, redirect or rewrite visitors by country or cookie, localize or personalize a page with geolocation, run A/B testing, transform or inject HTML into a response, stream server-side rendering at the edge, or cache an edge response. Also use it when an edge function silently does nothing, runs in the wrong order, ignores its Cache-Control headers, or cannot read an environment variable.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-edge-functions\SKILL.md`

#### `netlify-forms`
Serverless form handling on Netlify-hosted sites — detects HTML forms at deploy time, stores submissions, filters spam, and sends notifications. Use when adding a contact form, lead-capture form, file-upload form, or newsletter signup to a Netlify site; wiring AJAX form submission; setting up a custom thank-you page; adding a honeypot or reCAPTCHA to a form; getting forms working in Next.js, Nuxt, SvelteKit, Astro, or Gatsby; reading form submissions via the Netlify API; setting up submission notifications or ChatGPT automations on form submission events; or debugging missing submissions and forms that silently fail to register.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-forms\SKILL.md`

#### `netlify-frameworks`
Deploy and configure web frameworks on Netlify — build settings and SSR/edge adapters plus local platform emulation and env vars. Use when setting up or fixing a framework deploy (Next.js / Astro / Nuxt / SvelteKit / Remix / React Router / TanStack Start / SolidStart / Gatsby / Angular / Vite / Express / Hydrogen / Hugo / Eleventy / Vue / React), adding SSR or edge functions or middleware wired to Netlify context, fixing SPA redirect and catch-all rules, setting a build command or publish directory, or debugging "why isn't my env var updating" and framework build failures.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-frameworks\SKILL.md`

#### `netlify-functions`
Write, configure, and deploy Netlify serverless functions in TypeScript, JavaScript, or Go. Use this when adding an API endpoint or backend route, adding a contact form handler, wiring auth or Identity signup/login hooks, identifying which Netlify user is calling a private or team-login-protected app, building streaming or AI-proxy responses, scheduling cron jobs, running long background jobs (batch processing/scraping), reacting to deploy or form events, setting up rate limiting or region/memory config, or reading environment variables and secrets inside a function. Covers file locations, the Request/Context/Response handler shape, path routing, config options, and local testing with netlify dev.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-functions\SKILL.md`

#### `netlify-identity`
Add user authentication to a Netlify site with @netlify/identity, covering signup/login/logout, Google/GitHub/GitLab/Bitbucket OAuth, server-side getUser() checks, role-based access control, and Identity event functions. Use it when a task involves adding a login or signup form, gating content to members or roles, "auth middleware" or verifying users in Netlify Functions or Edge Functions, handling OAuth or email-confirmation callbacks, accepting user invites, assigning roles at signup, or customizing Identity emails. For locking a whole site to your company or employees-only access, use netlify-access-control instead.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-identity\SKILL.md`

#### `netlify-image-cdn`
Transforms images on demand via Netlify Image CDN's /.netlify/images endpoint with query parameters for resizing/cropping/format/quality. Use when adding image optimization or responsive images, converting formats (WebP/AVIF/PNG), generating thumbnails or blur placeholders, serving remote/third-party images through the CDN, allowlisting remote domains in netlify.toml, setting up image redirects or cache headers, building user-uploaded image pipelines, or debugging a 404 on /.netlify/images. Also covers framework image handling for Angular/Astro/Gatsby/Next.js/Nuxt.

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-image-cdn\SKILL.md`

#### `netlify-mcp-servers`
Build, deploy, and secure Model Context Protocol (MCP) servers on Netlify. Use whenever the task involves creating an MCP server, exposing an app or API to AI agents as MCP tools, letting Claude / Cursor / Claude Code call a custom remote server, or adding MCP tools to an existing Netlify site. Covers the MCP SDK + Streamable HTTP transport on a Netlify Function, authentication (single shared secret vs per-user API keys with Netlify Identity), read/write safety, file uploads, and connecting clients. Use even when the user just says "MCP", "tool server for an agent", or "let an AI use my API".

- Source: `C:\Users\chase\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-mcp-servers\SKILL.md`

#### `netlify-server`
Build and deploy a long-lived Node.js backend on Netlify Server (Early Access) from netlify/server/index.ts. Use this skill whenever someone wants to run an Express, Fastify, Hono or Koa app on Netlify as it is, add a backend or REST/GraphQL API that keeps database pools and caches warm, build real-time features such as chat, live dashboards or multiplayer with WebSockets or Server-Sent Events, or stream AI responses and run agent loops. It also covers background work after responding with waitUntil, startup and graceful shutdown hooks, load-aware health checks, edge caching of server responses, region/size/scale settings, local testing with netlify dev, reading server logs with netlify logs or log drains, and debugging a server that gets no requests, fails to start, drops database connections after a minute, or returns 429/500/501/502.

- Source: `C:\Users\chase\.gemini\antigravity\cache\marketplaces\antigravity-plugins-partners\plugins\netlify\1.9.0\agent-plugin\skills\netlify-server\SKILL.md`

#### `offload-to-sandbox`
Offload heavy builds, full test suites and parallel experiments from the local machine to Vercel Sandboxes with the `vercel sandbox` CLI. Use when a local machine is overloaded or shared by several agents, when a test suite should be sharded, or when many tasks should run side by side without consuming local CPU, memory or disk.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\offload-to-sandbox\SKILL.md`

#### `queues`
Vercel Queues guidance — durable topics with at-least-once delivery, independent consumer groups, retries, delays, and idempotency keys via @vercel/queue (JS) or vercel-queue (Python). Use when deferring background work, buffering traffic, fanning out events, or choosing between Queues and Workflows.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\queues\SKILL.md`

#### `react-best-practices`
Vercel's React and Next.js performance rules (70 rules in 8 categories ordered by impact - eliminating waterfalls, bundle size, server-side performance, client-side data fetching, re-renders, rendering performance, JavaScript performance, and advanced patterns). Use when writing, reviewing, or refactoring React components, Next.js pages, or data fetching for performance. Not an accessibility or TypeScript style guide.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\react-best-practices\SKILL.md`

#### `routing-middleware`
Vercel Routing Middleware guidance — request interception before cache, rewrites, redirects, personalization. Works with any framework. Supports Edge, Node.js, and Bun runtimes. Use when intercepting requests at the platform level.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\routing-middleware\SKILL.md`

#### `runtime-cache`
Vercel Runtime Cache API guidance — ephemeral per-region key-value cache with tag-based invalidation. Shared across Functions, Routing Middleware, and Builds. Use when implementing caching strategies beyond framework-level caching.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\runtime-cache\SKILL.md`

#### `sandbox`
Creates isolated Linux MicroVMs using Vercel Sandbox SDK. Use when building code execution environments, running untrusted code, spinning up dev servers, testing in isolation, or when the user mentions "sandbox", "microvm", "isolated execution", or "@vercel/sandbox".

- Source: `C:\Users\chase\.gemini\antigravity\cache\marketplaces\antigravity-plugins-partners\plugins\vercel-plugin\0.55.0-agy.4b94cb5a\skills\vercel-sandbox\upstream\SKILL.md`

#### `vercel-agent`
Vercel Agent guidance — dashboard and Slack chat, code review, production investigation, approved actions, and product installation. Use when configuring or working with Vercel's AI assistant.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-agent\SKILL.md`

#### `vercel-cli`
Vercel CLI expert guidance. Use when deploying, managing environment variables, linking projects, viewing logs, querying metrics, debugging a deployed app on Vercel (errors, 5xx responses, timeouts, slow routes, or a single failing request), managing domains, managing feature flags with vercel flags, or interacting with the Vercel platform from the command line. Use the vercel-tracing skill instead for `vercel traces` span search, trace inspection, and sampling rules, or for OpenTelemetry setup.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-cli\SKILL.md`

#### `vercel-connect`
Vercel Connect expert guidance for securely obtaining scoped credentials for third-party services on behalf of apps or users. Use when wiring up provider API access, OAuth, API-key services, MCP servers, triggers, framework adapters, eve agent connections, or provider tokens for Passport-authenticated users.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-connect\SKILL.md`

#### `vercel-firewall`
Vercel Firewall expert guidance — automatic DDoS mitigation, the Vercel WAF (custom rules, IP blocking, managed rulesets, rate limiting), Attack Mode, system bypass, bot management, and the `vercel firewall` CLI. Use when configuring platform-level security, responding to attacks, or staging firewall rules.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-firewall\SKILL.md`

#### `vercel-flags`
Feature flags, A/B tests, and gradual rollouts with Vercel Flags, in any app or framework. Use whenever the user is planning, adding, or changing a feature flag, toggle, kill switch, experiment, percentage rollout, or targeting rule, or wants to gate or hide a feature for some users, even before a library or provider is chosen. Covers choosing an integration (Flags SDK, `@vercel/flags-core`, OpenFeature), the Vercel dashboard, the `vercel flags` CLI (create, inspect, set, split, rollout, rules, segments, evaluations, archive), OIDC vs SDK keys, `FLAGS_SECRET`, and Flags Explorer overrides. For `flag()` declarations, adapters, precompute, and the Flags Explorer endpoint in Next.js or SvelteKit code, load the `flags-sdk` skill.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-flags\SKILL.md`

#### `vercel-functions`
Vercel Functions expert guidance — Node.js/Bun/Python runtimes, Fluid Compute, long-duration (30 min) functions, large functions (5 GB bundles), Docker/OCI container images, plan limits, streaming, WebSockets, and Cron Jobs. Use when configuring, debugging, or optimizing server-side code running on Vercel.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-functions\SKILL.md`

#### `vercel-react-best-practices`
React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\react-best-practices\upstream\SKILL.md`

#### `vercel-sandbox`
Vercel Sandbox guidance — ephemeral Firecracker microVMs for running untrusted code safely. Supports AI agents, code generation, and experimentation. Use when executing user-generated or AI-generated code in isolation.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-sandbox\SKILL.md`

#### `vercel-schedules`
Vercel Schedules guidance — run a private function, route, or Vercel Queues topic on a cron cadence or once at a set time. Covers static schedules in vercel.json, dynamic per-user schedules with @vercel/schedules, handleSchedule, the vercel schedules CLI, environments, jitter, and migrating from Cron Jobs. Use when adding scheduled or recurring work, one-time reminders, or replacing `crons`.

- Source: `C:\Users\chase\.gemini\antigravity\cache\marketplaces\antigravity-plugins-partners\plugins\vercel-plugin\0.55.0-agy.4b94cb5a\skills\vercel-schedules\SKILL.md`

#### `vercel-services`
Configure and troubleshoot Vercel Services for multiple frontends and backends in one project. Use when composing a polyglot or multi-service application on one Vercel deployment; defining the `services` key, service-targeted rewrites, or service bindings in `vercel.json`; or running all services with `vercel dev`.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-services\SKILL.md`

#### `vercel-storage`
Vercel storage expert guidance — Blob, Global Config (formerly Edge Config), and Marketplace storage (Neon Postgres, Upstash Redis). Use when choosing, configuring, or using data storage with Vercel applications.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-storage\SKILL.md`

#### `vercel-tracing`
Set up OpenTelemetry instrumentation for Vercel Tracing and query the resulting spans. Use when adding or fixing `@vercel/otel`, wiring a framework's server startup hook (Next.js, SvelteKit, and others), adding custom spans, turning on spans from libraries such as the AI SDK, Flags SDK, or database clients, propagating trace context between services, configuring always-on tracing sampling, searching or inspecting spans with `vercel traces`, or debugging failed or slow server requests.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\vercel-tracing\SKILL.md`

### Graph Databases & Knowledge Graphs (47 skills)

#### `connecting-looker-to-bigquery`
Looker Developer Onboarding: Step 4. Creates a database connection in Looker to Google BigQuery. Only execute this after Step 3 (CLI Authentication using `authenticating-looker-cli`).'

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\connecting-looker-to-bigquery\SKILL.md`

#### `creating-looker-dashboard`
Looker Developer Onboarding: Step 7 (Final Step). Creates a LookML dashboard in the project, imports it as a user-defined dashboard (UDD) in Looker, and iteratively refines it based on user feedback by syncing changes. Only execute this after Step 6 (Model Setup using `creating-lookml-model`).'

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\creating-looker-dashboard\SKILL.md`

#### `creating-lookml-model`
Looker Developer Onboarding: Step 6. Creates LookML views and models based on the user''s goals, maps model connections, validates LookML, and runs verification queries. Only execute this after Step 5 (Project Setup using `setting-up-looker-project`).'

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\creating-lookml-model\SKILL.md`

#### `exploring-data-for-looker`
Looker Developer Onboarding: Step 1. Guides the agent to explore BigQuery data and define the onboarding goal. This is the first active step, to be executed immediately after reading the parent orchestrator `looker-developer-onboarding`.'

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\exploring-data-for-looker\SKILL.md`

#### `looker-mcp-skill`
Guide for connecting to and using the Looker MCP Server. Explains how to access the Looker MCP server, set up Looker-managed vs local/standalone deployment, configure OAuth authentication, and catalog available MCP tools.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\looker-mcp-skill\SKILL.md`

#### `looker-performance-optimizer`
Master developer skill for auditing, diagnosing, and optimizing query performance in Looker projects. Enforces caching alignment, PDT materialization strategies, and parallel subagent SQL profiling.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\looker-performance-optimizer\SKILL.md`

#### `lookml-access-grants`
Use this skill to create Access Grants for row-level or object-level security.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-access-grants\SKILL.md`

#### `lookml-explore`
Use this skill when you need to create or modify a LookML Explore. This includes defining the Explore, joins, access grants, and basic configuration.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-explore\SKILL.md`

#### `lookml-fields`
Overview of LookML field types (Dimension, Measure, Filter, Parameter) and the role of the `sql` parameter in each. Use this skill to choose the right field type for your data modeling needs.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-fields\SKILL.md`

#### `lookml-liquid`
Use this skill to use Liquid variables in LookML for dynamic SQL, HTML, and Links, including advanced patterns for query optimization.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-liquid\SKILL.md`

#### `lookml-model`
Use this skill when you need to create or modify a LookML Model file (.model.lkml). This includes defining connections, includes, and configuring model-level settings.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-model\SKILL.md`

#### `lookml-modeling-guidelines`
Guidelines for LookML modeling and command execution.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-modeling-guidelines\SKILL.md`

#### `lookml-refinements`
Deep dive into LookML includes, refinements (layering), and project structure best practices. Essential for mastering Looker's object-oriented capabilities.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-refinements\SKILL.md`

#### `lookml-sets`
Guide to using LookML sets for grouping fields, controlling visibility, and managing drill paths.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-sets\SKILL.md`

#### `lookml-tests`
Standards and best practices for writing LookML tests to ensure data integrity, accuracy, and logic validation.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-tests\SKILL.md`

#### `lookml-view`
Use this skill to create or modify LookML Views. Covers basic view definitions, sql_table_name, file organization, and patterns.

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\lookml-view\SKILL.md`

#### `neo4j-agent-memory-skill`
Authoritative reference for the neo4j-agent-memory Python package — a graph-native memory system for AI agents built on Neo4j — and for the hosted service (NAMS) at memory.neo4jlabs.com. Use this skill whenever the user mentions neo4j-agent-memory, agent memory with Neo4j, context graphs, the POLE+O model, MemoryClient/MemorySettings, the memory MCP server, or any of the framework integrations (LangChain, PydanticAI, CrewAI, AWS Strands, Google ADK, Microsoft Agent Framework, OpenAI Agents, LlamaIndex). Also use when the user mentions the hosted service at memory.neo4jlabs.com, NAMS, the Neo4j Agent Memory Service, the `nams_` API key prefix, or the hosted MCP endpoint. Also use when writing documentation, blog posts, tutorials, PRDs, or code samples for the project, when comparing agent memory approaches, or when positioning graph-native memory against vector-only approaches — even if the user doesn't explicitly name the package. Does NOT handle GraphRAG pipelines — use neo4j-graphrag-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-agent-memory-skill\SKILL.md`

#### `neo4j-aura-agent-skill`
Manages Neo4j Aura Agents via the v2beta1 REST API — create, list, get, update, delete, and invoke Aura agents backed by an AuraDB instance. Use when configuring Aura Agent tools (CypherTemplate, SimilaritySearch, Text2Cypher), setting system prompts, deploying agents to REST or MCP endpoints, invoking agents with natural language queries, or generating evaluation datasets (max 50 questions) for the Aura Agent evaluation feature. Covers OAuth2 auth, organization/project scoping, tool parameter schemas, and InvokeAgentResponse format. Does NOT cover AuraDB instance provisioning — use neo4j-aura-provisioning-skill. Does NOT cover vector index creation — use neo4j-vector-index-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-aura-agent-skill\SKILL.md`

#### `neo4j-aura-graph-analytics-skill`
Serverless Aura Graph Analytics (AGA) GDS Sessions — covers GdsSessions, AuraGraphDataScience, AuraAPICredentials, DbmsConnectionInfo, SessionMemory, get_or_create, remote graph projection with gds.graph.project.cypher and gds.graph.project.remote, gds.graph.project.native, gds.graph.construct, graphdatascience client 2.0 session endpoints, async compute and gds.jobs, AuraDB Cypher API memory/sessionId projection, algorithms, write-back, and session lifecycle. Use for AuraDB-connected, self-managed Neo4j, or standalone DataFrame/Spark session workloads. Does NOT cover the embedded GDS plugin on Aura Pro or self-managed Neo4j — use neo4j-gds-skill. Does NOT handle Cypher authoring — use neo4j-cypher-skill. Does NOT cover Snowflake Graph Analytics — use neo4j-snowflake-graph-analytics-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-aura-graph-analytics-skill\SKILL.md`

#### `neo4j-aura-provisioning-skill`
Provisions and manages Neo4j Aura instances via CLI (aura-cli v1.7+) or REST API. Use when creating, pausing, resuming, resizing, or deleting AuraDB Free/Professional/Business Critical/VDC instances; downloading credentials; scripting CI/CD pipelines; polling async status; or using the Terraform neo4j-labs/neo4jaura provider. Covers auth setup (client credentials OAuth2), credential lifecycle (download once — never recoverable), instance type selection, region codes, and Python provisioning scripts. Does NOT handle Cypher queries — use neo4j-cypher-skill. Does NOT cover Graph Data Science algorithms — use neo4j-gds-skill or neo4j-aura-graph-analytics-skill. Does NOT cover neo4j-admin/cypher-shell — use neo4j-cli-tools-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-aura-provisioning-skill\SKILL.md`

#### `neo4j-cli-tools-skill`
Use when working with Neo4j command-line tools — neo4j-cli (modern unified CLI — Cypher via Bolt, schema inspection, Aura management, Docker containers, credential management, agent skill catalog install; install with curl -sSfL https://neo4j.sh/install.sh | bash), neo4j-admin (backup, restore, import, memory sizing), cypher-shell (ad-hoc queries, scripting, CI/CD), or neo4j-mcp (quick MCP server install). Does NOT cover Cypher query authoring — use neo4j-cypher-skill. Does NOT cover driver upgrades — use neo4j-migration-skill. Does NOT cover full MCP editor configuration — use neo4j-mcp-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-cli-tools-skill\SKILL.md`

#### `neo4j-cypher-skill`
Generates, optimizes, and validates Cypher 25 queries for Neo4j 2025.x and 2026.x. Use when writing new Cypher queries, optimizing slow queries, graph pattern matching, vector or fulltext search, subqueries, or batch writes. Covers MATCH, MERGE, CREATE, WITH, RETURN, CALL, UNWIND, FOREACH, LOAD CSV, SEARCH, expressions, functions, indexes, and subqueries. Does NOT handle driver migration or API changes — use neo4j-migration-skill. Does NOT cover DB administration or server ops — use neo4j-cli-tools-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-cypher-skill\SKILL.md`

#### `neo4j-document-import-skill`
Ingests unstructured and semi-structured documents into Neo4j as a knowledge graph. Use when chunking PDFs, HTML, plain text, or Markdown; extracting entities and relationships from text with an LLM (SimpleKGPipeline, neo4j-graphrag); loading JSON via apoc.load.json; building Document→Chunk→Entity graph structures; or connecting LangChain/LlamaIndex document loaders to Neo4j. Covers neo4j-graphrag SimpleKGPipeline, LLM Graph Builder web UI, entity resolution, chunking strategies, and graph schema design for RAG pipelines. Does NOT handle structured CSV/relational import — use neo4j-import-skill. Does NOT handle GraphRAG retrieval after ingestion — use neo4j-graphrag-skill. Does NOT handle vector index creation — use neo4j-vector-search-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-document-import-skill\SKILL.md`

#### `neo4j-driver-dotnet-skill`
Neo4j .NET Driver v6 — IDriver lifecycle, DI registration (singleton), ExecutableQuery fluent API, ExecuteReadAsync/ExecuteWriteAsync managed transactions, IResultCursor (FetchAsync/ ToListAsync), record value access (.Get<T>/As<T>), null safety, UNWIND batching, temporal types, await using, EagerResult, object mapping, CancellationToken, error handling, and common traps. Use when writing C# or .NET code connecting to Neo4j. Also triggers on Neo4j.Driver, IDriver, ExecutableQuery, ExecuteReadAsync, ExecuteWriteAsync, IResultCursor, IAsyncSession, or any Bolt/Aura work in .NET/C#. Does NOT handle Cypher authoring — use neo4j-cypher-skill. Does NOT cover driver version upgrades — use neo4j-migration-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-driver-dotnet-skill\SKILL.md`

#### `neo4j-driver-go-skill`
Covers the Neo4j Go Driver v6 — driver lifecycle, ExecuteQuery, managed and explicit transactions, session config, error handling, data type mapping, and connection tuning. Use when writing Go code that connects to Neo4j, setting up NewDriver or ExecuteQuery, debugging sessions/transactions/result handling, or working with neo4j-go-driver v5→v6 migration. Triggers on NewDriver, ExecuteQuery, SessionConfig, ManagedTransaction, neo4j-go-driver. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT cover driver version migration steps — use neo4j-migration-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-driver-go-skill\SKILL.md`

#### `neo4j-driver-java-skill`
Neo4j Java Driver v6 — driver lifecycle, Maven/Gradle setup, executableQuery, executeRead/Write managed transactions, explicit transactions, async/reactive patterns, error handling, data type mapping, connection pool tuning, causal consistency/bookmarks. Use when writing Java or Kotlin code that connects to Neo4j via GraphDatabase.driver, executableQuery, SessionConfig, executeRead, executeWrite, or TransactionCallback. Does NOT handle Cypher authoring — use neo4j-cypher-skill. Does NOT cover driver version upgrades — use neo4j-migration-skill. Does NOT cover Spring Data Neo4j (@Node, Neo4jRepository) — use neo4j-spring-data-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-driver-java-skill\SKILL.md`

#### `neo4j-driver-javascript-skill`
Neo4j JavaScript/TypeScript Driver v6 — driver lifecycle, executeQuery, managed transactions (executeRead/executeWrite), session.run, Integer handling, JSON serialization, record access, async/await patterns, TypeScript types, error handling, and connection setup for Node.js and browser. Use when writing JS/TS code that connects to Neo4j — neo4j.driver(), executeQuery, executeRead, executeWrite, session.run, neo4j.int, record.get, Integer, BookmarkManager, bolt://, neo4j+s://. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT cover driver version migration — use neo4j-migration-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-driver-javascript-skill\SKILL.md`

#### `neo4j-driver-python-skill`
Neo4j Python Driver v6 — driver lifecycle, execute_query, managed and explicit transactions, async (AsyncGraphDatabase), result handling, data type mapping, error handling, UNWIND batching, connection pool tuning, and causal consistency. Use when writing Python code that connects to Neo4j via GraphDatabase.driver, execute_query, execute_read, execute_write, AsyncGraphDatabase, neo4j.Result, or RoutingControl. Package name is `neo4j` (not neo4j-driver) since v6. Python >=3.10 required. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT cover driver upgrades or breaking changes — use neo4j-migration-skill. Does NOT cover GraphRAG pipelines (neo4j-graphrag package) — use neo4j-graphrag-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-driver-python-skill\SKILL.md`

#### `neo4j-gds-skill`
Neo4j Graph Data Science (GDS) embedded plugin via Python client or Cypher — covers graphdatascience client 2.x, GraphDataScience, gds.graph.project.native, gds.graph.project.cypher, snake_case endpoints, graph catalog operations, stream/stats/mutate/write modes, memory estimation, PageRank, Louvain, WCC, FastRP, KNN, Node Similarity, ML pipelines, and cleanup. Use for Aura Pro, self-managed, local, or offline Neo4j DBMS with the GDS plugin installed. Does NOT cover Aura Graph Analytics GDS Sessions, AuraGraphDataScience, GdsSessions, gds.graph.project.remote, or AuraDB Cypher API projection/session management — use neo4j-aura-graph-analytics-skill. Does NOT handle Cypher authoring — use neo4j-cypher-skill. Does NOT cover driver setup — use neo4j-driver-python-skill or other driver skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-gds-skill\SKILL.md`

#### `neo4j-genai-plugin-skill`
Use Neo4j GenAI Plugin ai.text.* functions and procedures for in-Cypher embedding generation, text completion, structured output, chat, tokenization, and batch ingestion. Covers ai.text.embed(), ai.text.embedBatch(), ai.text.completion(), ai.text.structuredCompletion(), ai.text.aggregateCompletion(), ai.text.chat(), ai.text.tokenCount(), ai.text.chunkByTokenLimit(), and provider configuration for OpenAI, Azure OpenAI, VertexAI, and Amazon Bedrock. Requires CYPHER 25. Replaces deprecated genai.vector.encode(). Use when writing pure-Cypher GraphRAG, embedding nodes in-graph, generating structured maps from prompts, or calling LLMs inside Cypher queries. Does NOT handle neo4j-graphrag Python library pipelines — use neo4j-graphrag-skill. Does NOT handle vector index creation/search — use neo4j-vector-index-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-genai-plugin-skill\SKILL.md`

#### `neo4j-getting-started-skill`
Orchestrates zero-to-running-app in 8 stages — prerequisites → context → provision → model → load → explore → query → build. Each stage reads its own reference file. Supports HITL and fully autonomous operation. Use when starting a new Neo4j project from scratch, provisioning Aura, generating synthetic data, building a notebook or app, or running the full onboarding pipeline. Time budget ≤15 min autonomous, ≤90 min HITL. Does NOT cover Cypher query authoring — use neo4j-cypher-skill. Does NOT cover driver upgrades or Cypher migration — use neo4j-migration-skill. Does NOT cover CLI/admin tasks on an existing DB — use neo4j-cli-tools-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-getting-started-skill\SKILL.md`

#### `neo4j-graphql-skill`
Build and configure a GraphQL API backed by Neo4j using @neo4j/graphql v7 (current) or v5 (LTS). Covers Neo4jGraphQL constructor, getSchema(), assertIndexesAndConstraints(), type definitions with @node, @relationship (IN/OUT/UNDIRECTED), @cypher for custom resolvers, @authorization/@authentication for JWT/JWKS security, auto-generated queries/mutations, OGM programmatic access, subscriptions via CDC, and Apollo Federation. Use when writing typeDefs, securing fields, or wiring Neo4j to Apollo Server. Does NOT handle raw Cypher outside resolvers — use neo4j-cypher-skill. Does NOT cover Spring Data Neo4j entity mapping — use neo4j-spring-data-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-graphql-skill\SKILL.md`

#### `neo4j-graphrag-skill`
Build GraphRAG retrieval pipelines on Neo4j using the neo4j-graphrag Python package (v1.22.0+). Covers retriever selection (VectorRetriever, HybridRetriever, VectorCypherRetriever, HybridCypherRetriever, Text2CypherRetriever, ToolsRetriever), external vector DB retrievers (Weaviate, Pinecone, Qdrant), retrieval_query Cypher fragments, query_params, filters, GraphRAG pipeline wiring (GraphRAG + LLM + prompt), all LLM providers (OpenAI, Anthropic, Gemini/VertexAI, Bedrock, Cohere, Mistral, Ollama), embedder setup, index creation, token usage tracking, Cypher 25 SEARCH clause, and LangChain/LlamaIndex integration. Does NOT handle KG construction — use neo4j-document-import-skill. Does NOT handle plain vector search — use neo4j-vector-index-skill. Does NOT handle GDS analytics — use neo4j-gds-skill. Does NOT handle agent memory — use neo4j-agent-memory-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-graphrag-skill\SKILL.md`

#### `neo4j-import-skill`
Import structured data into Neo4j — LOAD CSV, CALL IN TRANSACTIONS, neo4j-admin database import full (offline bulk), apoc.load.csv/json, apoc.periodic.iterate, driver batch writes. Covers method selection, header file format, type coercion, null handling, ON ERROR modes, CONCURRENT TRANSACTIONS, pre-import constraint setup, and post-import validation. Use when importing CSV/JSON/Parquet files, migrating relational data to graph, or bulk-loading large datasets. Does NOT handle unstructured document/PDF/vector chunking pipelines — use neo4j-document-import-skill. Does NOT handle live app write patterns (MERGE/CREATE) — use neo4j-cypher-skill. Does NOT handle neo4j-admin backup/restore/config — use neo4j-cli-tools-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-import-skill\SKILL.md`

#### `neo4j-kafka-skill`
Configure and operate the Neo4j Connector for Kafka (sink + source) and the native Neo4j CDC API. Covers Cypher/Pattern/CUD sink strategies, CDC-based and query-based source, exactly-once semantics, DLQ error handling, Confluent Cloud managed connector, schema registry (Avro/JSON), and native db.cdc.query cursor-loop patterns (Neo4j 5.13+ Enterprise/Aura BC/VDC). Use when streaming Kafka events into Neo4j, streaming Neo4j changes to Kafka, or querying Neo4j change events without Kafka. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT handle bulk CSV/file import — use neo4j-import-skill. Does NOT handle GDS algorithms — use neo4j-gds-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-kafka-skill\SKILL.md`

#### `neo4j-mcp-skill`
Use when installing, configuring, or troubleshooting the official Neo4j MCP server (neo4j/mcp) — connecting Claude Code, Claude Desktop, Cursor, Windsurf, VS Code, Kiro, or other MCP-compatible editors to a Neo4j database via stdio or HTTP transport. Covers the four MCP tools (get-schema, read-cypher, write-cypher, list-gds-procedures), read-only mode, and multi-database configuration. Does NOT cover writing Cypher queries via those tools — use neo4j-cypher-skill. Does NOT cover agent memory — use neo4j-agent-memory-skill. Does NOT cover Aura instance provisioning — use neo4j-aura-provisioning-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-mcp-skill\SKILL.md`

#### `neo4j-migration-skill`
Migrates Neo4j driver code and Cypher queries from older versions (4.x, 5.x) to current (2025.x/2026.x, Cypher 25). Covers Python, JavaScript/Node.js, Java, .NET, and Go drivers — package renames, removed APIs, version requirements, diff-ready fixes. Also handles Cypher syntax migration — QPE paths, CALL subqueries, id() → elementId(), PERIODIC COMMIT → CALL IN TRANSACTIONS, and all Cypher 25 removals. Does NOT write new Cypher queries — use neo4j-cypher-skill. Does NOT cover DB administration or server ops — use neo4j-cli-tools-skill. Does NOT provision new Neo4j instances — use neo4j-getting-started-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-migration-skill\SKILL.md`

#### `neo4j-modeling-skill`
Design, review, and refactor Neo4j graph data models. Use when choosing node labels vs relationship types vs properties, migrating relational/document schemas to graph, detecting anti-patterns (generic labels, supernodes, missing constraints), designing intermediate nodes for n-ary relationships, enforcing schema with constraints and indexes, or assessing an existing model against graph modeling best practices. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT handle Spring Data Neo4j entity mapping — use neo4j-spring-data-skill. Does NOT handle GraphQL type definitions — use neo4j-graphql-skill. Does NOT handle data import — use neo4j-import-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-modeling-skill\SKILL.md`

#### `neo4j-nvl-skill`
Neo4j Visualization Library (NVL) — framework-agnostic graph rendering for the browser. Covers @neo4j-nvl/base (NVL class, nodes/relationships, Canvas vs WebGL renderer), @neo4j-nvl/interaction-handlers (ZoomInteraction, PanInteraction, DragNodeInteraction, ClickInteraction, HoverInteraction, BoxSelectInteraction, LassoInteraction, KeyboardInteraction), and @neo4j-nvl/react (InteractiveNvlWrapper, BasicNvlWrapper, StaticPictureWrapper). Use when rendering a Neo4j graph in a browser, feeding driver results through nvlResultTransformer, choosing Canvas vs WebGL, wiring node/relationship click/hover/drag handlers, or embedding NVL in React, Vite, or vanilla JS apps. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT handle driver lifecycle, sessions, or executeQuery setup — use neo4j-driver-javascript-skill. Does NOT handle GraphVisualization/Needle default embed — use @neo4j-ndl/react.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-nvl-skill\SKILL.md`

#### `neo4j-ontology-skill`
Author and validate Neo4j Ontology Graph Specification (ontology graph spec) documents. Use when writing or editing an ontology, defining nodes and relationships with properties, Neo4jType data types, constraints (key/unique/must_exist), labels, and endpoint cardinality, in YAML or JSON, or validating an ontology document against the live-resolved spec schema. Does NOT handle Cypher or loading an ontology into a database — use neo4j-cypher-skill. Does NOT cover generic graph data modeling advice — use neo4j-modeling-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-ontology-skill\SKILL.md`

#### `neo4j-query-tuning-skill`
Diagnoses and fixes slow Neo4j Cypher queries by reading execution plans, identifying bad operators (AllNodesScan, CartesianProduct, Eager, NodeByLabelScan), and prescribing fixes (indexes, hints, query rewrites, runtime selection). Use when a query is slow, when EXPLAIN or PROFILE output needs interpretation, when dbHits or pageCacheHitRatio are poor, when cardinality estimation diverges from actuals, or when deciding between slotted/pipelined/parallel runtimes. Covers USING INDEX / USING SCAN / USING JOIN hints, db.stats.retrieve, SHOW QUERIES, SHOW TRANSACTIONS, TERMINATE TRANSACTION. Does NOT write new Cypher from scratch — use neo4j-cypher-skill. Does NOT cover GDS algorithm tuning — use neo4j-gds-skill. Does NOT cover index/constraint creation syntax details — use neo4j-cypher-skill references/indexes.md.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-query-tuning-skill\SKILL.md`

#### `neo4j-security-skill`
Programmatic security management in Neo4j — RBAC/ABAC, user lifecycle (CREATE/ALTER/DROP USER), role lifecycle (CREATE/GRANT ROLE/DROP ROLE), privilege grants and denies (GRANT/DENY/REVOKE on graph, database, DBMS), property-level access control, sub-graph access control, SHOW PRIVILEGES inspection, and auth provider config reference (LDAP, OIDC/SSO). Use when an agent needs to manage users, roles, or privileges programmatically via Cypher on the system database. Does NOT handle Cypher query writing — use neo4j-cypher-skill. Does NOT handle cluster ops or backups — use neo4j-cli-tools-skill. Property-level security and ABAC require Enterprise Edition.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-security-skill\SKILL.md`

#### `neo4j-snowflake-graph-analytics-skill`
Run Neo4j Graph Analytics algorithms (PageRank, Louvain, WCC, Dijkstra, KNN, Node2Vec, FastRP, GraphSAGE) directly inside Snowflake without moving data. Use when running graph algorithms against Snowflake tables via the Neo4j Snowflake Native App ("GDS Snowflake", "graph algorithms in Snowflake", "Neo4j Graph Analytics"). Covers the explore → prepare projection views → project-compute-write flow, the strict view/column type rules the graph engine requires, exact SQL CALL syntax, and privilege setup in both modes — app-identity grants and execute-as-user / per-user PAT auth (programmatic access token, set_enable_custom_credentials, register_user_role, caller grants). Does NOT cover Cypher or Neo4j DBMS queries — use neo4j-cypher-skill. Does NOT cover Aura Graph Analytics — use neo4j-aura-graph-analytics-skill. Does NOT cover self-managed GDS — use neo4j-gds-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-snowflake-graph-analytics-skill\SKILL.md`

#### `neo4j-spark-skill`
Use when reading from or writing to Neo4j with Apache Spark or Databricks using the Neo4j Connector for Apache Spark 6.0 (org.neo4j.connectors:spark) or 5.x (org.neo4j:neo4j-connector-apache-spark). Covers SparkSession setup, DataFrame reads via labels/Cypher/relationship scan, DataFrame writes with SaveMode, node.keys for MERGE, relationship write mapping, partition and batch tuning, PySpark and Scala examples, Databricks cluster config, Databricks secrets for credentials, Delta Lake to Neo4j pipelines. Does NOT handle Cypher authoring — use neo4j-cypher-skill. Does NOT handle the Python bolt driver — use neo4j-driver-python-skill. Does NOT handle GDS algorithms — use neo4j-gds-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-spark-skill\SKILL.md`

#### `neo4j-spring-data-skill`
Use when building Spring Boot applications with Neo4j using Spring Data Neo4j (SDN 7.x/8.x) — @Node entity mapping, @Relationship, @RelationshipProperties, Neo4jRepository, ReactiveNeo4jRepository, @Query annotations, application.yml configuration, projections, Neo4jClient, Neo4jTemplate, transactions, auditing, or Spring AI Neo4jVectorStore vector search. Does NOT handle raw Java driver code without Spring — use neo4j-driver-java-skill. Does NOT handle Cypher query authoring — use neo4j-cypher-skill. Does NOT handle driver version upgrades — use neo4j-migration-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-spring-data-skill\SKILL.md`

#### `neo4j-vector-index-skill`
Create and manage Neo4j vector indexes, run vector similarity search (ANN/kNN), store embeddings on nodes or relationships, use SEARCH clause (Neo4j 2026.01+, preferred) or db.index.vector.queryNodes() procedure (deprecated 2026.04, still works on 2025.x), configure HNSW and quantization options, pick similarity function and embedding provider dimensions, and batch-update embeddings. Use when tasks involve CREATE VECTOR INDEX, vector.dimensions, cosine/euclidean search, embedding ingestion pipelines, semantic or structural nearest-neighbor lookup, or hybrid search (vector + fulltext, multiple vector sources, or graph-derived scores). Does NOT handle GraphRAG retrieval_query graph traversal — use neo4j-graphrag-skill. Does NOT handle fulltext-only/keyword-only search — use neo4j-cypher-skill. Does NOT compute GDS graph embeddings (FastRP, Node2Vec) — use neo4j-gds-skill.

- Source: `C:\Users\chase\.gemini\config\plugins\neo4j\neo4j-vector-index-skill\SKILL.md`

#### `setting-up-looker-project`
Looker Developer Onboarding: Step 5. Creates a new Looker project and configures Git. Only execute this after Step 4 (BigQuery Connection using `connecting-looker-to-bigquery`).'

- Source: `C:\Users\chase\.gemini\config\plugins\looker\skills\setting-up-looker-project\SKILL.md`

### Design, UI/UX & Creative Engineering (40 skills)

#### `best-practices`
Tells your agent what Mobbin can and can't do and how the Mobbin skills work together, so it picks the right one or says when Mobbin isn't the right tool. Read it first, before any other Mobbin skill or tools, when the user asks about Mobbin or its connection, or starts a design task Mobbin could help with, including one that's too big or outside what Mobbin does.

- Source: `C:\Users\chase\.gemini\config\plugins\mobbin\skills\best-practices\SKILL.md`

#### `canva-brand-check`
Check a Canva design against a brand kit and report where it diverges — off-palette colors, non-brand fonts, logo misuse, and off-tone copy. Read-only; makes no changes. Use when the user asks "is this on brand", "check this against our brand kit", "do a brand review", "does this match our brand guidelines", or "brand-check my design".

- Source: `C:\Users\chase\.gemini\config\plugins\canva\skills\brand-check\SKILL.md`

#### `canva-branded-presentation`
Create on-brand Canva presentations from an outline or brief. Use when the user asks to create a branded presentation, make an on-brand deck, turn an outline into slides, or generate a presentation from a brief. Input can be text directly in the message, a Canva design ID, a reference to a Canva doc by name, or a Canva design link (e.g., https://www.canva.com/design/...).

- Source: `C:\Users\chase\.gemini\config\plugins\canva\inactive-skills\branded-presentation\SKILL.md`

#### `canva-bulk-create`
Bulk-create Canva designs from tabular data using a brand template with autofill fields, producing one design per row. Use when users say "bulk create designs from this CSV", "generate one design per row", "create a design for each product", "batch generate from a template", or "autofill a template from a spreadsheet". Accepts any tabular data source — uploaded files, pasted tables, JSON, or URLs.

- Source: `C:\Users\chase\.gemini\config\plugins\canva\skills\bulk-create\SKILL.md`

#### `canva-classroom-helper`
Turn a lesson plan into a teaching slide deck in Canva. Use when the user asks to build classroom slides from a lesson plan, convert a lesson plan into a presentation, make a teaching deck, create school slides from an outline, or generate a lesson deck for students. Input can be a lesson plan pasted in the message, a Canva design ID, a Canva doc or design by name, or a Canva design link (e.g., https://www.canva.com/design/...).

- Source: `C:\Users\chase\.gemini\config\plugins\canva\inactive-skills\classroom-helper\SKILL.md`

#### `canva-cli`
Use the Canva CLI to use Canva's REST APIs.

- Source: `C:\Users\chase\.gemini\config\plugins\canva\inactive-skills\canva-cli\SKILL.md`

#### `canva-design-feedback`
Read a Canva design and return structured, actionable design feedback — visual hierarchy, copy/messaging, layout & spacing, consistency, readability, and accessibility. Read-only; makes no changes to the design. Use when the user asks to "review my design", "give me feedback on this", "critique my deck/poster/flyer", "how can I improve this design", or "what's wrong with this slide".

- Source: `C:\Users\chase\.gemini\config\plugins\canva\skills\get-design-feedback\SKILL.md`

#### `canva-edit-design`
Make edits to an existing Canva design — change or fix text, replace/insert/delete images and videos, reformat text (size, weight, style, color, alignment, lists, line height), reposition or resize elements, and update the title. Use when the user wants to change, edit, update, fix, translate, replace, or reformat content in a specific Canva design. This is the safe edit engine that other Canva skills (e.g. implement-feedback) build on.

- Source: `C:\Users\chase\.gemini\config\plugins\canva\skills\edit-design\SKILL.md`

#### `canva-implement-feedback`
Implement reviewer feedback on a Canva design. Reads all comment threads, synthesises what reviewers want, makes the clear-cut changes directly, and flags anything that needs a human decision. Use when the user asks to "implement feedback on my deck", "address comments on a design", "apply review feedback", "fix the comments on my presentation", or "implement the feedback".

- Source: `C:\Users\chase\.gemini\config\plugins\canva\skills\implement-feedback\SKILL.md`

#### `canva-presentation-time-fitting`
Fit a Canva presentation to a target speaking duration by generating or rewriting presenter notes only (visible slide text is not edited). Use when users say "make this a 10-minute presentation", "split time evenly across slides", "generate speaker notes for a 15-minute talk", "fit my deck to [duration]", or "how long per slide for a 20-minute slot".

- Source: `C:\Users\chase\.gemini\config\plugins\canva\inactive-skills\presentation-time-fitting\SKILL.md`

#### `canva-resize-for-social-media`
Resize a Canva design into multiple social media formats (Facebook post, Facebook story, Instagram post, Instagram story, LinkedIn post). Use this skill when users want to resize Canva designs specifically for multiple social media platforms in one operation, rather than resizing to a single format manually.

- Source: `C:\Users\chase\.gemini\config\plugins\canva\skills\resize-for-social-media\SKILL.md`

#### `canva-translate-design`
Translate all text in a Canva design to another language, creating a translated copy. Faster than manually copying and editing each text box in Canva's editor. Use when users say "translate my design to [language]", "make a Spanish/French/etc version", or "localize my Canva design".

- Source: `C:\Users\chase\.gemini\config\plugins\canva\inactive-skills\design-translation\SKILL.md`

#### `figma-code-connect`
Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Connect, Figma component mapping, design-to-code translation, or asks to create/update .figma.ts or .figma.js files.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-code-connect\SKILL.md`

#### `figma-code-workflows`
Import or upload local HTML or project files into Figma, choose editable Design frames, runnable Code Layers or standalone Code (also known as Make), and repair imported previews. Use only when the user explicitly names editable Design layers, a runnable Code Layer, or a standalone Code/Make file, or supplies a Figma file key/link as the import destination. Generic code or code-component requests need output clarification before using this workflow.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-code-workflows\SKILL.md`

#### `figma-create-new-file`
Always use this skill when the user wants to create a new Figma Design, FigJam, or Slides file. You MUST invoke this skill BEFORE every `create_new_file` tool call.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-create-new-file\SKILL.md`

#### `figma-design-to-code`
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool. You MUST trigger this skill whenever the user wants to implement, build, port, or code up a Figma design as code. Example prompts (not exhaustive) are 'implement this Figma design', 'build this screen from Figma', 'turn this Figma into code', 'design to code'. This skill provides critical instructions and steps to the agent on how to correctly implement Figma designs in code and must NOT be skipped.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-design-to-code\SKILL.md`

#### `figma-generate-design`
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code', 'convert this modal/dialog/drawer/panel to Figma'. This is the preferred workflow skill whenever the user wants to build or update a full page, modal, dialog, drawer, sidebar, panel, form, dashboard, list, table, card, header, message preview, or other composed product UI in Figma from code or a description—even when the user calls that composed UI a component. Discovers design system components, variables, and styles from Code Connect files, existing screens, and library search, then imports them and assembles views incrementally section-by-section using design system tokens instead of hardcoded values.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-generate-design\SKILL.md`

#### `figma-generate-diagram`
MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-generate-diagram\SKILL.md`

#### `figma-generate-library`
Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, create individual components with proper variant sets and variable bindings, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. Also use when the user asks to create or generate any component in Figma — even a single one — since components require proper variable foundations, variant states, and design token bindings to be production-quality. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-generate-library\SKILL.md`

#### `figma-generative-plugins`
**MANDATORY prerequisite** — load this skill before calling `create_generative_plugin` or `update_generative_plugin`. Use when the user asks to create, author, change, fix, or extend a reusable generative Figma plugin.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-generative-plugins\SKILL.md`

#### `figma-implement-motion`
Translates Figma motion and animations into production-ready application code. Use when implementing animation/motion from a Figma design — user mentions "implement this motion", "add animation from Figma", "animate this component", provides a Figma URL whose node is animated, or when `get_design_context` returns motion data or instructs you to call `get_motion_context`.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-implement-motion\SKILL.md`

#### `figma-shaders`
**MANDATORY prerequisite** — load this skill before calling `create_shader` or `update_shader`. Use when the user asks to create, author, change, fix, or iterate on a shader effect, shader fill, custom effect, custom fill, or procedural shader in Figma.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-shaders\SKILL.md`

#### `figma-spec`
This skill is required to create, read, edit, review, or comment on Figma specs. You must read it when working on a PRD, brief, RFC or any kind of document in either a standalone Figma spec or a Figma spec embedded in a Figma Design or Figjam file.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-spec\SKILL.md`

#### `figma-swiftui`
SwiftUI ↔ Figma translation. Use whenever the user mentions Swift, SwiftUI, iOS, iPhone, or iPad — in EITHER direction — translating a Figma design into SwiftUI (design → code), or pushing SwiftUI views / screens / tokens back into a Figma file (code → design). Triggers on phrases like 'implement this Figma design in SwiftUI', 'build this screen in Swift', 'push this SwiftUI view to Figma', 'mirror my Swift code in a Figma file', or whenever a Figma URL appears alongside `.swift` files / an `.xcodeproj`. Routes to a direction-specific reference doc; loads alongside `figma-use` for the code → design path.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-swiftui\SKILL.md`

#### `figma-use`
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-use\SKILL.md`

#### `figma-use-figjam`
This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-use-figjam\SKILL.md`

#### `figma-use-motion`
Motion / animation context for the `use_figma` MCP tool — animating Figma nodes via manual keyframes, animation styles, easing, and timeline duration. Load alongside figma-use whenever a task involves adding, editing, or inspecting animation on a node. Also covers working with custom animation styles.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-use-motion\SKILL.md`

#### `figma-use-slides`
This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational context for using the use_figma tool.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\skills\figma-use-slides\SKILL.md`

#### `generative_ui`
How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show the user diagrams, data visualizations, interactive controls, educational walkthroughs, or any rich visual content beyond plain text and markdown.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\generative_ui\SKILL.md`

#### `motion-craftsmanship`
Eliminates floaty AI motion slop by enforcing tactile physics, spring dynamics, kinetic typography, and drop-in micro-interactions. Synthesizes getlayers.ai, 60fps.design, motion-primitives.com, kinetics.colorion.co, and microkit.co into production-ready prompts and code.

- Source: `C:\Users\chase\.gemini\config\skills\motion-craftsmanship\SKILL.md`

#### `plain-writing`
Makes every report a Mobbin skill writes read like a person wrote it, in plain interface terms. Use only when a Mobbin skill writes prose for the user or asks for this skill by name; not for writing outside Mobbin skills. Removes the tells of AI-generated writing (em dashes, puffery, design buzzwords, rule-of-three, sign-offs) without changing a fact or adding one.

- Source: `C:\Users\chase\.gemini\config\plugins\mobbin\skills\plain-writing\SKILL.md`

#### `redesign-screen`
Redesign any screen from patterns real apps ship. Share a screenshot, your code or a design file, and the skill finds how apps on Mobbin handle the same screen. Explore a few directions or fix specific problems, and see the evidence behind each change. You get a before and after image and a short report. The redesign stays in your own design system, and anything that already works is kept. Use whenever the user points at a screen, section, or component they have, or at a reference, a Mobbin result, one or more Mobbin collections or the screens they saved, and asks to redesign, improve, restyle, or rebuild it, or to see a few directions for it.

- Source: `C:\Users\chase\.gemini\config\plugins\mobbin\skills\redesign-screen\SKILL.md`

#### `search`
Gets better results from every Mobbin search, so the references match what you're working on. Use before every call to search_screens, search_flows or search_sections. Covers the tool, writing an effective query, the mode, pulling more results, and what to do when a search falls short.

- Source: `C:\Users\chase\.gemini\config\plugins\mobbin\skills\search\SKILL.md`

#### `wix-app`
Build and review Wix CLI app extensions — dashboard pages, modals, plugins, menu plugins, custom element widgets, Editor React components, site plugins, embedded scripts, context providers, function libraries, lightbox (popup) behavior, page onLoad contexts, backend APIs, backend events, service plugins, data collections, and App Market readiness. Use when building ANY feature or extension for a Wix CLI app or preparing a Wix app for App Market review. Triggers on: add, build, create, implement, help me, dashboard, widget, plugin, backend, API, event, collection, embedded script, service plugin, Editor React component, context provider, function library, onLoad, on page load, checkout, shipping, tax, discount, SPI, CMS, schema, tracking, popup, lightbox, admin panel, menu item, modal, validate, test, verify, register extension, App Market, app review, submission readiness.

- Source: `C:\Users\chase\.gemini\config\plugins\wix\skills\wix-app\SKILL.md`

#### `wix-design-system`
Wix Design System component reference. Use when building UI with @wix/design-system, choosing components, checking props and examples, or writing tests with component testkits. Triggers on "what component", "how do I make", "WDS", "show me props", "testkit", "driver", or component names like Button, Card, Modal, Box, Text.

- Source: `C:\Users\chase\.gemini\config\plugins\wix\skills\wix-design-system\SKILL.md`

#### `wix-docs`
Look up the Wix API/SDK documentation to confirm an exact endpoint, HTTP method, request/response shape, field, enum, or error before writing Wix code — never guess a Wix API from memory. A lookup is a short flow: find the right page, then read it. Two ways: (1) plain `curl` (zero dependencies) — find a page by **semantic search** (`POST /mcp-docs-search/v1/docs/search`, natural-language `{ search_term, document_type(s) }`, incl. the SKILLS recipe corpus for multi-step workflows) **or by browsing** a docs portal as a menu — a structured, typed, counted browse of the REST, SDK, CLI, Build Apps, and Headless portals (`POST /mcp-docs-search/v1/docs/menu/browse`), or the `.md` menu tree from the `llms.txt` root for any surface — then read the page by appending `.md` to its URL; (2) the Wix MCP doc tools when present. Triggers: look up a Wix API, find the Wix endpoint/method, confirm a Wix request body or field, verify a Wix API shape, explore Wix docs, which Wix API do I call, read a Wix method schema.

- Source: `C:\Users\chase\.gemini\config\plugins\wix\skills\wix-docs\SKILL.md`

#### `wix-headless-kit`
Build a Wix Headless site fast by wiring SHIPPED, verified @wix/sdk code instead of authoring the integration from recipes. Each Wix business vertical ships a typed, framework-agnostic React core (data layer returning plain DTOs, hooks, headless components) plus an Astro overlay (SSR pages with owner-editable SEO pre-wired) and a build-time REST seed script — the agent scaffolds via the Wix CLI, deploys the shipped code, seeds the backend, designs the presentation layer itself on the shipped hooks (product card/grid, PDP, home, theme), and releases to Wix hosting. Works on Wix-managed Astro (ambient auth, the default) and on any React-based project (Vite, non-Astro) over the public OAuth client id. Verticals: stores/storefront (products, categories, variants, cart, hosted checkout), bookings (services, appointment/class time slots, staff, booking form, checkout-or-place), rentals (rooms, vehicles, gear by the hour or the day: resources, customer-picked length, priced quote, checkout), blog (posts, categories/tags, rich content), cms (structured content collections), forms (schema-driven visitor forms: render, validate, submit), events (listing, RSVP, ticket sales), members (login, gated pages, account), portfolio (project collections, media galleries), pricing-plans (plan grid, hosted purchase), restaurants (menus, online ordering, table reservations), faq (categorized questions and answers, search, a link per question), donations (campaign pages, goal progress, one-time and recurring donations via hosted checkout). Triggers: build me a store/blog/booking/rental/event/restaurant/portfolio/FAQ/donation site fast, take appointments fast, rent out rooms/cars/equipment headless, sell tickets or membership plans headless, collect donations headless, wix headless kit, connect a Wix business app with ready-made SDK code.

- Source: `C:\Users\chase\.gemini\config\plugins\wix\skills\wix-headless-kit\SKILL.md`

#### `wix-manage`
REST recipes to configure and manage a Wix site's business solutions — stores, bookings, donations, payments, CMS, and more. Open the matching recipe for the exact endpoint, method, and payload before calling — never guess a Wix API, never write Wix dashboard URL from memory. Routes to: automations, stores, bookings, donations, get-paid, CMS, contacts, forms, media, app-installation, custom-apps, pricing-plans, restaurants, ricos rich-content, sites, collaborators, blog, calendar, domains, events, site-properties, ecommerce, marketing, online-programs, google-ads, google-business-profile, analytics, accessibility, seo, dashboard-navigation.

- Source: `C:\Users\chase\.gemini\config\plugins\wix\skills\wix-manage\SKILL.md`

#### `wix-readme`
What the Wix plugin holds and how to work with Wix through it: the flow the Wix MCP README returns, an index of the plugin's skills with what each does, and the Wix MCP tools with what each does. Use when the plugin was just installed or when the user asks what the Wix plugin can do or which skill or tool fits a task.

- Source: `C:\Users\chase\.gemini\config\plugins\wix\skills\wix-readme\SKILL.md`

#### `wix-studio-two`
Build or edit a Wix website by chat, with no local setup - start a new site, or change an existing Wix Studio Two site's pages, sections, text, images, colors or layout, or bring another site's or project's pages into one. The site's code is exported to a remote machine, edited and previewed there, and saved to Wix when the user asks. Not for sites built in the Wix Editor or Studio 1, not for headless sites, which belong to wix-headless-kit, and not for products, bookings, blog posts or other business data, which belong to wix-manage, and not for publishing HTML files or a static build the user already has, which belongs to wix-headless-kit. Never publishes.

- Source: `C:\Users\chase\.gemini\antigravity\cache\marketplaces\antigravity-plugins-partners\plugins\wix\1.41.3\skills\wix-studio-two\SKILL.md`

### Browser Automation & Web DevTools (9 skills)

#### `a11y-debugging`
Uses Chrome DevTools MCP for accessibility (a11y) debugging and auditing based on web.dev guidelines. Use when testing semantic HTML, ARIA labels, focus states, keyboard navigation, tap targets, and color contrast.

- Source: `C:\Users\chase\.gemini\config\plugins\chrome-devtools-plugin\skills\a11y-debugging\SKILL.md`

#### `browse`
Use the browse CLI for Browserbase browser automation, Browserbase cloud APIs, Browserbase Functions, templates, web fetch/search, diagnostics, and Browse.sh skill discovery/installation. Use when the user asks to navigate pages, inspect browser state, run local or remote browser sessions, manage Browserbase resources, call Browserbase Functions, browse or scaffold Browserbase templates, fetch or search web content, diagnose browse setup, find or install a skill for a website task, discover site-specific Browse.sh skills, or install/refresh this browse skill.

- Source: `C:\Users\chase\.gemini\config\plugins\browse\skills\browse\SKILL.md`

#### `chrome-devtools`
Uses Chrome DevTools via MCP for efficient debugging, troubleshooting and browser automation. Use when debugging web pages, automating browser interactions, analyzing performance, or inspecting network requests. This skill does not apply to `--slim` mode (MCP configuration).

- Source: `C:\Users\chase\.gemini\config\plugins\chrome-devtools-plugin\skills\chrome-devtools\SKILL.md`

#### `chrome-extensions`
Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser extensions, add-ons, or anything involving the Chrome Extensions API. Trigger on mentions of: 'Chrome extension', 'browser extension', 'manifest.json', 'content script', 'service worker' (in browser context), 'popup' (in browser extension context), 'side panel', 'chrome.* API', 'declarativeNetRequest', 'omnibox', 'context menu' (in extension context), 'userScripts', 'user script', 'script manager', or any request to build functionality that integrates with the Chrome browser UI. Also trigger for publishing to the Chrome Web Store: 'publish extension', preparing an extension for publishing, responding to a review rejection, writing permission justifications, or drafting a privacy policy.

- Source: `C:\Users\chase\.gemini\config\plugins\modern-web-guidance-plugin\skills\chrome-extensions\SKILL.md`

#### `cookie-debugging`
Uses Chrome DevTools MCP for inspecting, debugging, and testing cookies, session state, authentication issues, and cookie consent compliance. Use when diagnosing 401/403 errors, authentication redirects, session expiration, Cookie/Set-Cookie header issues, cookie banner consent conformance, or third-party cookie/SameSite/Partitioned cookie warnings.

- Source: `C:\Users\chase\.gemini\config\plugins\chrome-devtools-plugin\skills\cookie-debugging\SKILL.md`

#### `firecrawl-scraper`
Extracts clean, LLM-ready markdown, crawls multi-page websites, and maps sitemaps using Firecrawl MCP. Use when scraping web pages, ingesting technical documentation without HTML clutter, extracting structured data, or crawling entire documentation sites.

- Source: `C:\Users\chase\.gemini\config\skills\firecrawl-scraper\SKILL.md`

#### `memory-leak-debugging`
Diagnoses and resolves memory leaks in JavaScript/Node.js applications. Use when a user reports high memory usage, OOM errors, or wants to capture, compare, or inspect heap snapshots with Chrome DevTools MCP memory tools.

- Source: `C:\Users\chase\.gemini\config\plugins\chrome-devtools-plugin\skills\memory-leak-debugging\SKILL.md`

#### `playwright-automation`
Automates Chromium, Firefox, and WebKit browsers using Playwright MCP for end-to-end testing, UI verification, visual regression, form filling, and DOM interaction. Use when validating web apps, clicking interactive controls, capturing full-page screenshots, or executing automated browser QA directly from the workspace.

- Source: `C:\Users\chase\.gemini\config\skills\playwright-automation\SKILL.md`

#### `troubleshooting`
Uses Chrome DevTools MCP and documentation to troubleshoot connection and target issues. Trigger this skill when list_pages, new_page, or navigate_page fail, or when the server initialization fails.

- Source: `C:\Users\chase\.gemini\config\plugins\chrome-devtools-plugin\skills\troubleshooting\SKILL.md`

### Structural Biology & Molecular Modeling (11 skills)

#### `alphafold-database-fetch-and-analyze`
Retrieve and analyze AlphaFold predicted structures for a protein. Use when the user provides a specific UniProt Accession ID and wants structural confidence metrics (pLDDT), domain boundary analysis, or disorder assessment. Do not use if the user only has a protein name, gene name, or amino acid sequence — ask for a UniProt ID first.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphafold_database_fetch_and_analyze\SKILL.md`

#### `biomolecular-structure-viewer`
Interactive 3D biomolecular structure viewer via Mol*. Renders 3D molecular structures from local workspace files (.cif, .mmcif, .pdb) or conversation artifacts, and manages user 3D annotations and highlighted residues. Use when the user asks to visualise a protein or nucleic acid, display a 3D structure, or asks about 3D biomolecular structure annotations and highlighted residues.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\biomolecular_structure_viewer\SKILL.md`

#### `foldseek-structural-search`
Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user provides a physical 3D coordinate file (.cif, .mmcif, or .pdb) and wants to find structurally similar proteins. Do NOT use if the user only provides a protein sequence, gene name, or UniProt ID.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\foldseek_structural_search\SKILL.md`

#### `human-protein-atlas-database`
Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\human_protein_atlas_database\SKILL.md`

#### `interpro-database`
Identify domains, families, and sites in proteins; find all proteins in a family or sharing a domain; explore species distribution for a domain; annotate genomes with protein families and GO terms. InterPro combines 14 databases (e.g., Pfam, CDD) into one searchable resource. InterPro-N significantly expands annotation and sequence coverage with deep learning. Includes domain architecture (IDA) search.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\interpro_database\SKILL.md`

#### `pdb-database`
Use when you want to search for or download experimentally-determined 3D structures for biomolecules (proteins, nucleic acids, bound ligands). Supports searching by sequence similarity, structure similarity, chemical and other attributes. Also use to get metadata about biomolecular structure experiments.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pdb_database\SKILL.md`

#### `protein-sequence-msa`
Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity, domain conservation, or key residue conservation. Supports up to 4000 sequences and a maximum file size of 4 MB. Do not use to search for homologous proteins in a database (use MMseqs2, BLAST), align non-protein sequences (DNA, RNA), perform structural alignment (use Foldseek, PyMOL), or if you only have a single sequence.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\protein_sequence_msa\SKILL.md`

#### `protein-sequence-similarity-search`
Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback). Trigger this whenever the user provides a protein sequence or FASTA file and asks to find homologues, sequence matches, or wants to infer protein function based on sequence similarity, but not when the user wants to infer protein function based on structural similarity.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\protein_sequence_similarity_search\SKILL.md`

#### `pymol`
Visualize, analyze, and render protein and molecular structures using PyMOL. Use when the user wants to create images of protein structures, perform structural alignments or superposition, measure distances or contacts, highlight binding sites or active site residues, color by B-factor/pLDDT, or analyze protein-ligand interactions. Do not use for docking, molecular dynamics, or sequence-only analysis.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pymol\SKILL.md`

#### `string-database`
Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific proteins, interaction evidence, confidence scores, protein interaction partners, or pathway enrichments.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\string_database\SKILL.md`

#### `uniprot-database`
Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins, mapping identifiers, or retrieving functional annotations and publications. Don't use for sequence alignment, protein folding, or sequence similarity search (use specialized skills for those tasks).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\uniprot_database\SKILL.md`

### Genomics & Variant Impact (14 skills)

#### `alphagenome-atlas-website-links`
Constructs deep-links and URLs for the AlphaGenome Atlas website. Supports generating single-variant exploration links (1-based VCF-style coordinates), genomic locus views (1-based closed chr:start-end), candidate summary tables, and AlphaGenome reference vs. alternate predictions. Use when visualizing, exploring, charting, or linking genetic variants and genomic loci on the AlphaGenome Atlas, or when asked to inspect, view, or link predictions for a genomic variant. Don't use for computing raw AlphaGenome variant predictions directly without Atlas URLs (use alphagenome-single-variant-analysis or alphagenome-variant-impact-score).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphagenome_atlas_website_links\SKILL.md`

#### `alphagenome-single-variant-analysis`
Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNASE), histone marks (ChIP), and transcription factors using the AlphaGenome API. Use when the user asks about non-coding variant effects, pathogenicity, clinical significance, disease associations, functional effects, gene expression changes, splicing disruption, or regulatory effects in promoters and enhancers. Also use for resolving biological terms to tissue/cell-type ontologies (UBERON/CL) or analyzing variants in chr:pos:ref>alt format.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphagenome_single_variant_analysis\SKILL.md`

#### `alphagenome-variant-impact-score`
Score, annotate, and analyze the functional impact of genetic variants using AlphaGenome Variant Impact (AVI) scores. Query variants in chr:pos:ref>alt format, annotate VCF/tabular callsets, perform saturation mutagenesis window scans (1-based closed chr:start-end), and extract GENCODE v46 GTF gene/exon/junction coordinates all via the AlphaGenome Atlas API.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphagenome_variant_impact_score\SKILL.md`

#### `clinvar-database`
Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales, or finding "hard positive" benchmark controls for human genomic variants.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\clinvar_database\SKILL.md`

#### `dbsnp-database`
Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs, genomic coordinates in VCF format, and HGVS strings. For an rsID, returns variant type, gene associations, clinical significance, allele frequencies, and genomic coordinates (GRCh38).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\dbsnp_database\SKILL.md`

#### `encode-ccres-database`
Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API, or make custom queries to the ENCODE Portal REST API for experiments and files (ChIP-seq peaks, etc.). Use when you want to query regulatory annotations or raw experimental data across human cell types.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\encode_ccres_database\SKILL.md`

#### `ensembl-database`
Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons), and get variant consequence and effect predictions (VEP). Use this skill as a primary ID translator, genomic sequence database and variant effect prediction tool.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\ensembl_database\SKILL.md`

#### `gnomad-database`
Query the Genome Aggregation Database (gnomAD). Use when determining the rarity or allele frequency of specific genetic variants, retrieving gene constraint metrics (pLI, LOEUF) to assess loss-of-function intolerance, finding variants in a genomic region or gene, or querying structural variants. Don't use for analyzing individual patient genomes, tracking somatic mutations in cancer (use COSMIC), or requesting raw sequencing reads (use ENA).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\gnomad_database\SKILL.md`

#### `gtex-database`
Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project across 54 non-diseased tissue sites.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\gtex_database\SKILL.md`

#### `jaspar-database`
Query the JASPAR database for Transcription Factor (TF) binding profiles. Use when retrieving Position Frequency Matrices (PFMs) or Position Weight Matrices (PWMs) for specific TFs, resolving gene symbols to JASPAR Matrix IDs, or getting TF metadata. Supports multiple output formats (MEME, TRANSFAC, PFM, JASPAR, YAML).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\jaspar_database\SKILL.md`

#### `ncbi-sequence-fetch`
Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports direct accession lookup, CDS translation, gene+organism search, locus lookup, PubMed-linked sequences, patent protein extraction, and organism+length fallback search. Use when you need to fetch biological sequences by accession, gene name, locus tag, PubMed ID, or patent number.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\ncbi_sequence_fetch\SKILL.md`

#### `quickgo-database`
Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need to map genes to biological processes, molecular functions, or cellular components, find genes associated with a specific pathway/GO term, or explore the Gene Ontology hierarchy. Do not use for querying drug targets (use OpenTargets) or mechanistic signaling pathway diagrams (use KEGG).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\quickgo_database\SKILL.md`

#### `ucsc-conservation-and-tfbs`
Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser. Use when analyzing whether genomic variants or regions are evolutionarily conserved, functionally important, or bounded by TF regulators across major projects (ENCODE, JASPAR, ReMap).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\ucsc_conservation_and_tfbs\SKILL.md`

#### `unibind-database`
Queries the UniBind database for experimentally validated transcription factor (TF) binding sites. Use when retrieving direct TF-DNA interaction datasets, downloading binding site coordinates (BED/FASTA) for local analysis, or listing available datasets by species, cell line, or TF name. Don't use to query specific intervals, locations, genes, motif models or expression data.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\unibind_database\SKILL.md`

### Cheminformatics & Computational Chemistry (7 skills)

#### `cheminformatics-cofolding`
Co-folds protein-ligand, protein-DNA/RNA, and covalent inhibitor complexes: prepares AlphaFold 3 JSON, Boltz-2 YAML, and Boltz API (boltz-2.1) inputs, extracts bound ligand poses from mmCIF/PDB, and computes 3D protein-ligand interaction fingerprints (PLIF) and pharmacophore overlaps.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\cheminformatics_cofolding\SKILL.md`

#### `cheminformatics-core`
Computes RDKit physicochemical descriptors (MW, cLogP, TPSA, CNS MPO, SA score), PAINS/Brenk structural alerts, pH 7.4 ionization, congeneric series curation, activity cliffs, combinatorial library enumeration, vendor pricing, and organometallic %V_bur sterics.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\cheminformatics_core\SKILL.md`

#### `cheminformatics-doc2mol`
Extracts and curates validated chemical structures from patents, literature, synthesis procedures, and Markush core/R-group tables: resolves IUPAC names via OPSIN and PubChem, retrieves Google Patents full text and assay tables, and exports curated SDF/CSV.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\cheminformatics_doc2mol\SKILL.md`

#### `cheminformatics-ml`
Trains, benchmarks, and evaluates predictive SAR and QSAR/ADMET models for chemical series: small-N regularized regressors, nested cross-validation, Tukey HSD model tiering, scaffold/temporal splitting, matched molecular pairs (MMPA), similarity attribution maps, model persistence, and candidate scoring.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\cheminformatics_ml\SKILL.md`

#### `cheminformatics-physics`
Simulates 3D molecular physics, conformer ensembles, and CADD workflows: pH-dependent ligand and receptor protonation, ETKDGv3 3D conformer generation, dihedral/relaxed PES torsion scans, AutoDock Vina/smina docking, conformational ligand strain energy, PROTAC/macrocycle 3D geometry, and OpenMM molecular dynamics.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\cheminformatics_physics\SKILL.md`

#### `cheminformatics-reactions`
Proposes and models organic reactions, retrosynthesis, multi-step synthesis routes, intramolecular cyclizations, and reaction SMARTS: checks experimental precedents first, validates atom conservation, prochirality (pro-R/pro-S, Re/Si), topicity, 1H/13C NMR equivalence, and stereogenesis, and renders 2D curved-arrow mechanisms.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\cheminformatics_reactions\SKILL.md`

#### `rdkit-general`
Generates 2D chemical structure depictions (PNG/SVG), interactive HTML compound grids, standalone chemical applications/visualizers, and ChemDraw (.cdxml/.cdx) documents using ACS 1996 publication styling; validates IUPAC/stereochemical nomenclature and provides shared RDKit version compatibility helpers.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\rdkit_general\SKILL.md`

### Drug Discovery & Pharmacology (6 skills)

#### `chembl-database`
Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures. Use when the user asks about compounds, targets, IC50/Ki values, drug mechanisms, or structure searches.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\chembl_database\SKILL.md`

#### `clinical-trials-database`
Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, drug, location, status, or phase; retrieve trial details by NCT ID; check eligibility/inclusion criteria; count trials across conditions or time periods; identify a sponsor's trial portfolio; find recruiting trials for patient matching.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\clinical_trials_database\SKILL.md`

#### `openfda-database`
Query, search, and download data from the openFDA API for drugs, devices, foods, tobacco, cosmetics, animal and veterinary products, substances, and transparency data. Use for FDA adverse events, recalls, labeling, approvals, shortages, 510(k) clearances, NDC lookups, and any FDA safety or regulatory data query across all 28 API endpoints.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\openfda_database\SKILL.md`

#### `opentargets-database`
Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeutic target identification.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\opentargets_database\SKILL.md`

#### `pubchem-database`
Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics. Use when a user asks about a specific chemical, drug, or molecule.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pubchem_database\SKILL.md`

#### `reactome-database`
Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment, retrieving results by token, finding unmapped or not-found identifiers, mapping identifiers, reaction participants (inputs, outputs), pathway hierarchy (including top-level pathways), diagram export, cross-reference mapping, or searching the knowledgebase.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\reactome_database\SKILL.md`

### Literature & Knowledge Retrieval (8 skills)

#### `embl-ebi-ols`
Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions, and hierarchies across 250+ ontologies (e.g., GO, DOID, HP). Use when the user asks to search for terms, retrieve details, navigate hierarchies (parents, children, ancestors), look up properties and individuals, get autocomplete suggestions, or access ontology metadata and statistics.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\embl_ebi_ols\SKILL.md`

#### `literature-search-arxiv`
Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstracts, and download full-text PDFs or HTML versions of papers. Use when the user asks to find research papers, literature, or specific arXiv IDs.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_arxiv\SKILL.md`

#### `literature-search-biorxiv`
Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and medRxiv. Supports fetching paper metadata by DOI, and browsing by date range with category and keyword filters. Keyword filtering is local, so date ranges MUST be narrow (1-4 weeks) with a category to prevent timeouts.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_biorxiv\SKILL.md`

#### `literature-search-europepmc`
Search Europe PMC for scientific literature and download open-access full texts and PDFs. Retrieve full-text XML/plain text by PMCID, get citation lists and bibliography.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_europepmc\SKILL.md`

#### `literature-search-openalex`
Query the OpenAlex scholarly database for research papers, authors, institutions, topics, sources, publishers, funders, geo-locations, and keywords. Use when searching academic papers, resolving DOIs, downloading open-access PDFs, finding an author's publications, aggregating bibliometric data (citation counts, h-index, impact factor), exploring the research taxonomies, or performing DOI lookups.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_openalex\SKILL.md`

#### `perplexity-search`
Executes live real-time web search, deep technical research, and citation synthesis using Perplexity AI. Use when answering questions requiring fresh online documentation, latest library releases, live web data, or verified external technical citations without leaving the terminal.

- Source: `C:\Users\chase\.gemini\config\skills\perplexity-search\SKILL.md`

#### `predictingthepast`
Ancient text restoration, attribution, dating, contextualization, and embedding via Aeneas (Latin) / Ithaca (Ancient Greek). Use when asked to "restore", "attribute", "date", "contextualize", "find parallels", "where was it written", "when was it written", "embed", or "analyze" an ancient text, inscription, or epigraphic document, or when the user mentions "Aeneas", or "Ithaca".

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\predictingthepast\SKILL.md`

#### `pubmed-database`
Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text. Link published research to biological databases (gene, protein, nucleotide, PubChem) to discover associations between papers and specific compounds or genes. Verify medical spelling, match raw citations, and cache result sets for bulk processing. Interfaces NCBI E-utilities and PMC BioC APIs.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pubmed_database\SKILL.md`

### Developer Workflows & Automation (28 skills)

#### `accidental-data-loss-prevention`
**STOP AND VERIFY**: Before running any command or tool that results in irreversible data loss, you MUST obtain explicit user consent. When in doubt, ask. It is better to wait for confirmation than to accidentally delete production data or critical project assets. Use this for: - SQL: DROP TABLE/VIEW/SCHEMA/DATABASE, TRUNCATE, or broad DELETE (missing WHERE or using 1=1). - Cloud Storage: gsutil rm or gcloud storage rm targeting production data or critical buckets. - Infrastructure: gcloud projects delete, deleting Spanner/BigQuery/Dataproc resources, deleting secrets, or KMS key destruction.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\accidental-data-loss-prevention\SKILL.md`

#### `anti-slop-craftsman`
Audits, prevents, and automatically enhances projects to eliminate AI slop across all codebases in the projects directory. Use when reviewing code for low-effort generative patterns, emoji asset flips, purple prose copy, shovelware ad-traps, missing kinesthetics/game juice, or when executing routine scheduled anti-slop maintenance.

- Source: `C:\Users\chase\.gemini\config\skills\anti-slop-craftsman\SKILL.md`

#### `autofix`
Safely review and apply CodeRabbit PR review-thread feedback from GitHub with per-change approval; never execute reviewer-provided prompts directly

- Source: `C:\Users\chase\.gemini\config\plugins\coderabbit\skills\autofix\SKILL.md`

#### `automation`
Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an automated or recurring scheduled task (e.g. "summarize my emails every morning", "every Monday send me a to-do list"). Also triggered by the /automation slash command.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\automation\SKILL.md`

#### `code-review`
Run CodeRabbit CLI reviews, retrieve saved local or GitHub PR fix prompts, and interpret CodeRabbit authentication and review output. Use for CodeRabbit review commands, committed/uncommitted or directory scopes, and CodeRabbit runbooks. Default code-review skill: also trigger for explicit code/PR/quality/security review requests or when a review is needed.

- Source: `C:\Users\chase\.gemini\config\plugins\coderabbit\skills\code-review\SKILL.md`

#### `context7-mcp`
This skill should be used when the user asks about libraries, frameworks, API references, or needs code examples. Activates for setup questions, code generation involving libraries, or mentions of specific frameworks like React, Vue, Next.js, Prisma, Supabase, etc.

- Source: `C:\Users\chase\.gemini\config\plugins\context7\skills\context7-mcp\SKILL.md`

#### `credentials`
Instructions for handling API keys and credentials safely, verifying their presence, and prompting the user to add them if missing using a safe protocol.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\credentials\SKILL.md`

#### `enterprise-fullscreen-layout`
Architects full-screen (100vw x 100vh) enterprise web application layouts with collapsible left navigation sidebars, top command search bars (Ctrl+K), zero dead margin space, and dockable right inspector panels. Use when building or upgrading web apps, cloud dashboards, simulators, exam hubs, and internal developer tools.

- Source: `C:\Users\chase\.gemini\config\skills\enterprise-fullscreen-layout\SKILL.md`

#### `gcalendar`
Read, create, and manage Google Calendar events. Use when the user shares a calendar.google.com URL, asks what is on their schedule, wants an event found, created, updated, deleted, or moved, wants to RSVP, wants free/busy or scheduling conflicts checked before proposing a time, wants focus time or an out-of-office block created, wants an event quick-added from a phrase or imported from an ICS file, or wants to know where someone is working from and which timezone they are in. Don't use for Gmail, Chat, or Tasks.

- Source: `C:\Users\chase\.gemini\config\plugins\gcalendar\skills\gcalendar\SKILL.md`

#### `gdocs`
Read, create, edit, and manage Google Docs. Use when the user shares a docs.google.com URL, asks to summarize or extract content from a doc, wants a doc drafted, edited, formatted, or commented on, wants tables, images, or smart chips inserted, wants markdown imported or synchronized with a doc, or wants a doc exported. Requires a known document ID — to find documents, use the gdrive skill from the Google Drive plugin; if it isn't installed, ask the user for the doc link. Don't use for Google Sheets, Slides, or Drive file management.

- Source: `C:\Users\chase\.gemini\config\plugins\gdocs\skills\gdocs\SKILL.md`

#### `gdrive`
Browse, search, and manage Google Drive files and folders. Use when the user shares a drive.google.com URL, asks what is in a folder, wants a file found, downloaded, uploaded, updated in place, moved, copied, or renamed, wants a Google file exported to PDF, Markdown, or CSV, wants comments read or added, wants sharing and permissions checked or changed, or wants Drive activity watched. Don't use for editing the contents of a Doc, Sheet, or Slides deck.

- Source: `C:\Users\chase\.gemini\config\plugins\gdrive\skills\gdrive\SKILL.md`

#### `generate-project-plan`
Generate a FigJam project plan board from a PRD plus codebase context. Interactive flow: research → propose sections → per-section deep research → per-section content + block-shape proposal → create FigJam → skeleton → fill → diagrams → wrap. Each content block (section, nested section, intro callout, table, multi-column text, sticky column, diagram section, metadata strip) has its own subskill reference file. Use when the user asks for 'project plan in FigJam', 'interactive project plan', '/generate-project-plan', or provides a PRD and wants per-section confirmation on content + rendering.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\workflow-skills\generate-project-plan\SKILL.md`

#### `github-primer-anti-slop-ui`
Enforces professional GitHub Primer and enterprise cloud console design standards, completely eliminating AI slop hallmarks (raw emoji asset flips, floaty cards, purple prose) using crisp 1px borders, dual-tone inline SVGs, and High-Gloss Lacquer physical material optics.

- Source: `C:\Users\chase\.gemini\config\skills\github-primer-anti-slop-ui\SKILL.md`

#### `google-maps-platform`
A collection of skills for architecting and implementing production-ready code using Google Maps Platform APIs and SDKs for any map, place, address, geocoding, routing/ETA (including eco-friendly routing), nearby search, 3D / Street View / static map, marker clustering, custom styling, drawing, geofencing, heatmap, or environmental (air-quality / pollen / solar / weather) feature — across Web, Android, iOS, and Web Services APIs. For prototyping, use the public Maps Demo Key — no billing setup and no Cloud project required, covering a growing set of the most popular Google Maps Platform APIs. For production, the skill prompts you to create and restrict your own key. All non-trivial code is grounded in freshly retrieved docs via the Google Maps Platform Code Assist service (no reliance on training-data memory).

- Source: `C:\Users\chase\.gemini\config\plugins\google_maps_platform\skills\SKILL.md`

#### `gsheets`
Read, write, format, and manage Google Sheets. Use when the user shares a sheets.google.com or docs.google.com/spreadsheets URL, asks to read or summarize spreadsheet data, wants cells written, formatted, sorted, merged, or validated, wants rows/columns inserted or deleted, wants charts, pivot tables, or tables added, wants CSV imported, or wants a spreadsheet created, copied, shared, or exported. Don't use for Google Docs, Slides, or Drive file management.

- Source: `C:\Users\chase\.gemini\config\plugins\gsheets\skills\gsheets\SKILL.md`

#### `gslides`
Read, create, and edit Google Slides presentations. Use when creating presentations, when the user shares a slides.google.com URL, asks to summarize or extract content from a deck, wants slides drafted or updated, or wants a presentation exported. Don't use for Google Docs, Sheets, or Drive file management.

- Source: `C:\Users\chase\.gemini\config\plugins\gslides\skills\gslides\SKILL.md`

#### `interactive-simulation-practice-engine`
Builds interactive, step-by-step traffic and packet journey simulators alongside gamified, self-grading system design drill engines with smart fuzzy matching, architectural hints, audio speech synthesis, and live progress rings. Use when creating educational tools, exam simulators, system architecture trainers, or interactive walkthroughs.

- Source: `C:\Users\chase\.gemini\config\skills\interactive-simulation-practice-engine\SKILL.md`

#### `managing-python-dependencies`
Ensures proper Python dependency management, avoiding global `pip install` and adhering to project-specific tooling. Use this skill if any of the following are true: 1. Attempting to run `pip install {package_name}`. 2. Python packages or dependencies need to be added or modified. 3. Initiating a new Python project. 4. Installing missing packages inside a notebook or Python project. 5. Generating Python code that includes `import` statements for third-party libraries. 6. Before executing Python scripts via the terminal to ensure the correct virtual environment is active.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\managing-python-dependencies\SKILL.md`

#### `ml-best-practices`
CRITICAL RULE: You MUST use this skill whenever the task involves any machine learning tasks or data analysis. Use this skill if the user's prompt or requirements mention any of the following: * Clustering * Classification * Regression * Time series forecasting * Statistical testing * Model comparison * ML * Data analysis SQL/BigQuery ML HANDOFF: If the user requires a SQL solution, use this skill to dictate the ANALYSIS STEPS (e.g., markdown analysis cells, visualization logic), but defer to `bigquery` for all SQL syntax.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\ml-best-practices\SKILL.md`

#### `notebook-guidance`
This skill guides the use of Jupyter notebooks for data analysis, exploration, and visualization, particularly with BigQuery. It outlines best practices for notebook execution and validation (supporting both cell-by-cell execution and full notebook generation depending on tool availability), library installation, and structuring notebooks for clarity. It also covers specific rules for data cleaning, plotting, and integrating with BigQuery SQL and machine learning workflows. Relevant when any of the following conditions are true: 1. The user request involves a data analysis, data exploration, data visualization, or data insights task that requires multiple steps, queries, or visualizations to answer. 2. The user explicitly requests a notebook (.ipynb). 3. You are creating, editing, or executing cells in a Jupyter notebook. 4. You need to query BigQuery from within a notebook. DO NOT use the Python BigQuery client library; instead, you MUST use the `%%bqsql` magics explained in this skill.

- Source: `C:\Users\chase\.gemini\config\plugins\data-agent-kit-plugin\skills\notebook-guidance\SKILL.md`

#### `permissioned-github`
Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environment.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\permissioned-github\SKILL.md`

#### `plugin`
How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and disable as a single unit. Use this skill when the user wants to enable, disable, install or uninstall a plugin, when they want to create a new plugin, or when a new customization should be packaged into a plugin rather than left loose. Also triggered by the /plugin slash command. Don't use for the underlying customization system itself — discovery roots, loading priority, or authoring a standalone skill, agent, rule, hook or MCP server outside a plugin; see the customizations guide skill for those.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\plugin\SKILL.md`

#### `run-workflow`
How to write and run a dynamic workflow script with the `run_workflow` tool: a Python script that orchestrates many agents with `agent`, `parallel`, `pipeline`, and `phase`. Use when a task splits into many independent or staged pieces of agent work (fan out over files, modules, bugs, or review angles, then aggregate), or when the user asks for a workflow. Don't use for a single delegated task (use a subagent) or for legacy workflow files (see migrate-workflows).

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\run-workflow\SKILL.md`

#### `script-practice`
Interactive scripting practice, challenge generator, code reviewer, and test runner for Red Hat Enterprise Linux (Bash/RHEL 8 & 9) and PowerShell (5.1 & 7+). Use when the user asks for scripting practice, challenges, code reviews, debugging assistance, or test execution for Linux bash or PowerShell.

- Source: `C:\Users\chase\.gemini\config\plugins\script-practice\skills\script-practice\SKILL.md`

#### `uv`
Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH. Use when another skill requires uv as a prerequisite.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\uv\SKILL.md`

#### `verification`
Full-story verification — infers what the user is building, then verifies the complete flow end-to-end: browser → API → data → response. Triggers on dev server start and 'why isn't this working' signals.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\verification\SKILL.md`

#### `workflow`
Vercel Workflow SDK expert guidance. Use when building durable workflows, long-running tasks, API routes or agents that need pause/resume, retries, step-based execution, or crash-safe orchestration with Vercel Workflow.

- Source: `C:\Users\chase\.gemini\config\plugins\vercel-plugin\skills\workflow\SKILL.md`

#### `workflow-skill-creator`
Distills a completed user workflow or interaction into a reusable agent skill. Use when the user asks to turn their workflow, interaction, or multi-step process into a skill, or when they say "make this a skill", "create a skill from what we just did", "package this workflow" or similar. Do not use for creating skills from scratch without an existing workflow (use a generic skill-creator for that).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\workflow_skill_creator\SKILL.md`

### Media & Video Strategy (14 skills)

#### `higgsfield-generation`
Generates cinematic AI images, character motion, and high-fidelity video sequences using Higgsfield AI MCP. Use when creating visual concept art, character animation, game cutscenes, video ad assets, or YouTube Short backgrounds across 30+ visual models.

- Source: `C:\Users\chase\.gemini\config\skills\higgsfield-generation\SKILL.md`

#### `higgsfield-to-invideo`
Use when the person has clips from Higgsfield and wants a finished video: put the clips in order, add captions and music, export.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\higgsfield-to-invideo\SKILL.md`

#### `hyperframes-to-invideo`
Use when the person has a HyperFrames composition and wants it finished in invideo: render it to MP4, upload it, then cut it, caption it, add music and export.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\hyperframes-to-invideo\SKILL.md`

#### `invideo`
Use for any video job: make, edit, trim, stitch, caption or grade clips; ads, launches, product and personal videos, invitations, intros, explainers, films, shorts. Unlike an ffmpeg script, each edit lands on a timeline the person can see and change. Read first: connecting, the work loop, cost.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\invideo\SKILL.md`

#### `invideo-generate`
Generate images, video, voice-over, music, sound effects and 3D for an invideo video: picking and prompting a model, pricing, narration first, retries.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\invideo-generate\SKILL.md`

#### `invideo-media`
Get and check media for an invideo video: the person's uploads, stock video, images and music, rights, and the craft of voice-over, music, sound effects, cleanup and dubbing.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\invideo-media\SKILL.md`

#### `invideo-pipeline`
Use for scale and automation: a CSV to many videos, `--json`, idempotency keys, CI with device sign-in, outreach at scale, course batches, bulk orders, and several agents sharing one project.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\invideo-pipeline\SKILL.md`

#### `invideo-timeline`
Use for operations depth on an invideo timeline: frame math, tracks and layering, keyframes and motion, speed ramps, grades, LUTs, effects and custom shaders, audio buses, ducking and loudness.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\invideo-timeline\SKILL.md`

#### `magnific-to-invideo`
Use when the person has clips from Magnific and wants a finished video: put the clips in order, add captions and music, export.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\magnific-to-invideo\SKILL.md`

#### `openedit-to-invideo`
Use when the person has an OpenEdit plan and wants it finished in invideo: render it to MP4, upload it, then cut it, caption it, add music and export.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\openedit-to-invideo\SKILL.md`

#### `remotion-to-invideo`
Use when the person has a Remotion composition and wants it finished in invideo: render it to MP4, upload it, then cut it, caption it, add music and export.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\remotion-to-invideo\SKILL.md`

#### `runway-to-invideo`
Use when the person has clips from Runway and wants a finished video: put the clips in order, add captions and music, export.

- Source: `C:\Users\chase\.gemini\config\plugins\invideo\skills\runway-to-invideo\SKILL.md`

#### `video-interaction-mapper`
This skill should be used when the user asks to analyze a UI screen recording and map interaction states into Figma. Trigger for requests such as "put video frames in Figma", "extract states from my recording", "map interactions from video to Figma", "analyze this screen recording", "create a storyboard from my video", "deconstruct this interaction in Figma", "annotate the UI states in my recording", or "pull the key moments from this video into Figma". Also trigger when the user references a video file (.mp4, .mov, .webm, .avi) together with Figma, design review, interaction analysis, prototypes, or UI states. The skill extracts key visual moments from a video, infers interaction triggers, and builds an annotated Figma Design storyboard using native Figma annotations and uploaded screenshot assets.

- Source: `C:\Users\chase\.gemini\config\plugins\figma\workflow-skills\video-interaction-mapper\SKILL.md`

#### `youtube-master-strategist`
Top 0.1% YouTube packaging strategist, retention engineer, and algorithm optimizer. Use when writing, auditing, or generating YouTube titles, thumbnails, hooks, scripts, pacing audits, and session-time retention bridges. Enforces strict CTR and AVD mechanics.

- Source: `C:\Users\chase\.gemini\config\skills\youtube-master-strategist\SKILL.md`


## 🚀 Part 2: Active Antigravity Projects Catalog

### `1st grade learning` (Education)
- **Stack**: `HTML, JS, Audio`
- **Status**: `Active`
- **Frontier Architecture**: Gamified phonics engine, Web Audio sound effects, typing arcade, celebratory canvas particles
- **Target Action**: Expand spelling word dictionary and add positive reinforcement celebratory canvas particles

### `3d images` (3D / Graphics)
- **Stack**: `Node.js, WebGL, Shaders`
- **Status**: `Active`
- **Frontier Architecture**: WebGL2 stereoscopic shaders, glTF Draco mesh compression, Three.js r184/r185 TSL materials with automatic WGSL/GLSL cross-compilation, FSR 1 and TAAU upscaling nodes
- **Target Action**: Integrate Draco mesh compression and Three.js r184 FSR 1 / TAAU upscaling nodes to load high-resolution 3D models with minimal latency

### `AAC` (Assistive Tech / Accessibility)
- **Stack**: `TypeScript, Vite, Web Speech API, PWA, CSS`
- **Status**: `Active`
- **Frontier Architecture**: Amina Universal AAC & Systematic Phonics Studio, WCAG 2.1 AAA compliance, Open Board Format (`.obf`) & Open Board Zip (`.obz`) JSON schemas for Cboard/Open-AAC interoperability, Modified Fitzgerald Key clinical color coding, Afro-European female voice scoring engine ("Amina") with male voice exclusion, decodable micro-phonics ("The help lives on the word" single-letter dots, digraph bars, magic-e arcs), PWA offline caching, system screen reader synchronization (`aria-live="assertive"`, `v.default`)
- **Target Action**: Implement .obf/.obz board export/import; calibrate switch-scanning dwell intervals; verify WCAG AAA contrast

### `Choogle` (Search / Portals)
- **Stack**: `Static Web, JS, CSS, PWA`
- **Status**: `Active`
- **Frontier Architecture**: Automated `Sync-ChoogleProjects.ps1` catalog sync (verified executed 2026-11-11 00:07:48 with active search mappings and app catalog ingestion), offline Service Worker, local inverted index
- **Target Action**: Maintain scheduled sync; expand search mappings for newly staged micro-apps and tools

### `Game Library` (Portals / Gaming UI)
- **Stack**: `React, TailwindCSS, Python, Model Context Protocol`
- **Status**: `Active`
- **Frontier Architecture**: Clean-Room Xbox PC App & Game Library Visual Reconstruction, 100vw x 100vh fullscreen layout, collapsible rail (280px <-> 64px), sticky 52px command bar (Ctrl+K), multi-dock inspector, live MCP telemetry bridge (`mcp_xbox_sync.py`) streaming data from `game-capture` (Xbox Game Bar DVR, RTX 4080 thermals) and `game-studio` (UE5, Unity 6 PIE), MCP Baseline 2.0 (`Ctrl+M`, `Ctrl+E`)
- **Target Action**: Execute `python mcp_xbox_sync.py` to refresh live MCP telemetry; verify in-app element inspection and hot-patching editor console; run `Invoke-AntiSlopAudit.ps1` to verify zero-slop visual fidelity

### `Github Portfolio` (Web / Career Showcase)
- **Stack**: `HTML5, CSS3, JS, Markdown, PDF Resumes`
- **Status**: `Active`
- **Frontier Architecture**: Chase Hamilton Master Developer & Infrastructure Showcase, dynamic GitHub REST/GraphQL API integration, interactive terminal CLI modal (`whoami`, `cat resume`, `ls projects`, `skills`), Bento grid glassmorphism, live operational health badges synced from `deploy/health_status.json`
- **Target Action**: Integrate terminal emulator component in `app.js` and connect project cards to live `deploy/PROJECT_CATALOG.json` health badges

### `How to train your AI` (AI / Agents)
- **Stack**: `Ollama, Python, Modelfiles`
- **Status**: `Active`
- **Frontier Architecture**: TensorRT-LLM 1.4+ (PyTorch-native, DFlash 2 support, KV-Cache Manager V2 default for Llama, explicit `sampler_type` in `SamplingConfig`), vLLM v0.33.0 (LibTorch Stable ABI migration, PyTorch 2.14, concurrent worker startup for TP > 1, native watchdog, removal of Medusa and old MLP speculators, `uv pip install vllm --torch-backend=auto`), Blackwell NVFP4 16-element micro-block scaling with FP8 E4M3 local scaling & FP32 global scaling via ModelOpt (`mtq.quantize` with `NVFP4_DEFAULT_CFG` or `NVFP4_MLP_ONLY_CFG`), dual export pathways (`export_tensorrt_llm_checkpoint` & `export_hf_checkpoint` via `hf_quant_config.json`), vLLM/SGLang native `--quantization modelopt_fp4 --linear-backend cutlass` with Marlin W4A16 fallback, ModelOpt Quantization-Aware Distillation (QAD), `KvCacheConfig(dtype='nvfp4')`, RoPE precision control (`skip_rope_quantization=True` / `2FP4`), Speculative Decoding (EAGLE-2 / DFlash 2)
- **Target Action**: Deploy `serve_vllm.ps1` with vLLM v0.33.0 LibTorch ABI; enable DFlash 2 and KV-Cache Manager V2; integrate AST parser and local ChromaDB knowledge base

### `Images` (Asset Store)
- **Stack**: `Image Formats (.heic, .jpg)`
- **Status**: `Active`
- **Frontier Architecture**: Shared high-res image repository, automated format converter (Pillow WebP batch compression)
- **Target Action**: Add Python image conversion script batch-converting mobile `.heic` photos to `.webp`

### `MCP` (Systems / AI Tools)
- **Stack**: `Node.js, JSON-RPC, Python, JavaScript, FastMCP v4`
- **Status**: `Active`
- **Frontier Architecture**: Centralized Model Context Protocol hub, MCP `2026-07-28` specification standard (Linux Foundation, stateless protocol core, header routing `Mcp-Method`/`Mcp-Name`, multi round-trip `input_required`, `ttlMs` cache hints, formal `io.modelcontextprotocol/tasks` extensions), FastMCP v4 (`CurrentContext` dependency injection), newly deployed dedicated `ollama-mcp` server (`MCP/ollama-mcp`) exposing 6 specialized tools, MCP Baseline 2.0 (`MCP_WEB_APPS_BASELINE.md`), `mcp-baseline.js` v2.0, `mcp-registry.json`, `Ctrl+M` telemetry HUD, `Ctrl+E` in-app element inspection & hot-patching editor console, custom MCP servers (`game-studio-mcp`, `game-capture-mcp`, `ollama-mcp`), global `mcp_config.json`, Texas Property Tax Form 50-132 protest generator (`Tax_Summary_and_2027_Protest_Plan.md`)
- **Target Action**: Sync live tool availability across all project hubs (`My Planetarium`, `My Custom Gui`, `index folder`); enforce loopback HMAC token auth; test FastMCP v4 `CurrentContext` dependency injection in `ollama-mcp`

### `MY Security` (Cybersecurity)
- **Stack**: `C#, .NET 10, PowerShell`
- **Status**: `Active`
- **Frontier Architecture**: NetBird Zero-Trust posture checks, WireGuard kernel overlay, BitLocker/Defender compliance hooks, Cisco KEV telemetry, actively exploited CVE-2026-76418, CVE-2026-76519 & Secure Client posture check validation
- **Target Action**: Add endpoint posture validator (BitLocker, Defender, OS build) before peer access; alert on unpatched ASA SSL VPN, AMP, Expressway, and NX-OS endpoints

### `My Custom Gui` (Portals / Command Center)
- **Stack**: `HTML5, TailwindCSS, Glassmorphism`
- **Status**: `Active`
- **Frontier Architecture**: Nexus Hub Pro Command Center, real-time telemetry polling (`deploy/health_status.json`), quick-launcher grid, local app hooks (`vscode://`, `file:///`)
- **Target Action**: Integrate live WebSocket/REST health polling to `deploy/health_status.json`; add quick-launch tiles for new Plugins, Synthetix Studio, and OpenShift Lab

### `My Planetarium` (XR / Graphics / Navigation)
- **Stack**: `Three.js, WebGL, High-Gloss Lacquer`
- **Status**: `Active`
- **Frontier Architecture**: 3D Interactive Deep Space Planetary Observatory & Sector Atlas, 64 charted planetary bodies, astronomical rigor, Three.js r184/r185 WebGPURenderer and TSL materials, Antigravity bidirectional prompt dispatching (`window.sidecar.agent.sendMessage`), auto-fit panoramic projection (`[F]`), slide-out MCP telemetry drawer
- **Target Action**: Keep `projects-data.js` synchronized with expanded 76-project inventory; package as Antigravity UI extension plugin; verify Three.js r184/r185 TSL shader rendering

### `Plugins/chrome-pulse-task-manager` (Browser Extension)
- **Stack**: `Manifest V3, JS, Chrome APIs`
- **Status**: `Active`
- **Frontier Architecture**: Chrome Pulse Toolbar Task Manager & Memory Saver, live toolbar badge stats (`chrome.system.memory`, `chrome.system.cpu`), safe tab discard memory reclamation (`chrome.tabs.discard`), tab search & sleep controls
- **Target Action**: Add configurable memory pressure alert threshold; implement `chrome.sidePanel` persistent inspector

### `Plugins/raindrop-sports-nba` (Browser Extension)
- **Stack**: `Manifest V3, ESPN API, JS`
- **Status**: `Active`
- **Frontier Architecture**: Specialized NBA scoreboard, live box scores, team timeout counts, quarter-by-quarter scoring flow, individual stat leaders
- **Target Action**: Test live game clock sync; connect favorite team push alerts

### `Plugins/raindrop-sports-ncaab` (Browser Extension)
- **Stack**: `Manifest V3, ESPN API, JS`
- **Status**: `Active`
- **Frontier Architecture**: Specialized NCAA Men's Basketball live tracker, AP Top 25 rankings, conference filters, live March Madness tournament brackets
- **Target Action**: Implement conference tournament bracket view; track live upset alerts

### `Plugins/raindrop-sports-ncaaf` (Browser Extension)
- **Stack**: `Manifest V3, ESPN API, JS`
- **Status**: `Active`
- **Frontier Architecture**: Specialized NCAA College Football tracker, CFP top-25 rankings, conference standings, scoring drive summaries, bowl game tracker
- **Target Action**: Connect CFP playoff bracket predictor; verify ranking update hooks

### `Plugins/raindrop-sports-nfl` (Browser Extension)
- **Stack**: `Manifest V3, ESPN API, JS`
- **Status**: `Active`
- **Frontier Architecture**: Specialized NFL scoreboard, real-time drive charts, red zone possession indicators, down-and-distance, field position tracker
- **Target Action**: Add red zone score alerts; verify Thursday/Sunday/Monday night game schedules

### `Plugins/raindrop-sports-scoreboard` (Browser Extension)
- **Stack**: `Manifest V3, ESPN API, JS`
- **Status**: `Active`
- **Frontier Architecture**: Raindrop Sports Scoreboard Master, real-time live scores for NBA, NFL, NCAAB, and NCAAF via ESPN REST API, quarter clocks, broadcast badges, floating on-screen overlay (`Ctrl+Shift+S`)
- **Target Action**: Calibrate polling intervals via `chrome.alarms`; verify floating overlay drag ergonomics

### `Plugins/webpage-reverse-engineer` (Browser Extension)
- **Stack**: `Manifest V3, Gemini API, Ollama`
- **Status**: `Active`
- **Frontier Architecture**: ReverseCraft AI webpage reverse engineer & recompiler, full-page DOM/CSS extraction, automated transpilation into standalone web apps, Playwright scripts, React components, and Ollama modelfiles
- **Target Action**: Connect local Ollama bridge (`localhost:11434`) and Gemini API; test Studio dashboard (`Ctrl+Shift+U`)

### `Plugins/website-bookmark-manager` (Browser Extension)
- **Stack**: `Manifest V3, JS, CSS`
- **Status**: `Active`
- **Frontier Architecture**: Full bookmark suite, auto-tagging, search & filter, import/export JSON, broken link verification, `manager/manager.html` full dashboard, `chrome.sidePanel.getLayout()` (Chrome 140+) dynamic left/right panel docking orientation detection
- **Target Action**: Integrate `chrome.sidePanel` for persistent split-screen bookmark triage; implement `getLayout()` responsive sidebar layout

### `Plugins/website-screenshot` (Browser Extension)
- **Stack**: `Manifest V3, Canvas, Offscreen`
- **Status**: `Active`
- **Frontier Architecture**: Multi-mode screenshot capture (full-page scrolling stitch, visible viewport, custom selection), built-in Canvas annotation editor (shapes, text, arrow, blur redaction, crop), PNG/PDF export, single offscreen document guard via `chrome.runtime.getContexts()`
- **Target Action**: Implement `chrome.offscreen` with `getContexts()` collision guards for headless canvas stitch operations; add one-click copy to clipboard via Offscreen document

### `Plugins/youtube-audio-converter` (Browser Extension)
- **Stack**: `Manifest V3, WebAssembly LAME, JS`
- **Status**: `Active`
- **Frontier Architecture**: SoundFlow YouTube & video-to-audio converter, in-page WASM audio extraction (MP3/WAV/WebM), lossless tab audio capture via `tabCapture` + `offscreen`, A/B waveform trimming, ID3 tagger
- **Target Action**: Test offscreen tab capture audio pipeline; verify keyboard shortcuts (`Ctrl+Shift+U`, `Ctrl+Shift+R`)

### `REA` (Cybersecurity / Reversing)
- **Stack**: `Python, Ghidra 11.3, PowerShell`
- **Status**: `Active`
- **Frontier Architecture**: Dedicated Reverse Engineering Applications Hub, Ninja Gaiden 2 Xenon/x64 DAT unpacker, Tekken 8 UE5 hooks, Naraka asset boundaries, PyGhidra CPython 3 integration, `JitPcodeEmulator` accelerated decoding
- **Target Action**: Automate 1-click Ghidra 11.3 + JDK 21 installer in `tools/setup_ghidra.ps1` and connect `binary_inspector.py` with `JitPcodeEmulator` to `game mods`

### `RHCSA Exam200` (Linux / SysAdmin)
- **Stack**: `Markdown, Shell, RHEL 9.5/9.6/10`
- **Status**: `Active`
- **Frontier Architecture**: RHEL 9.6 modernization: Landlock LSM unprivileged application sandboxing, Unified Kernel Images (UKIs) signed with UEFI stubs for secure boot root-of-trust, NFS RPC over TLS encryption, NetworkManager 1.52, Podman 5.4+ with rootless Netavark/`pasta` networking, Podman Quadlets (`.container`, `.image`, `.volume`, `.network`, `.kube`, `.pod`), systemd v256+ `run0` (`--machine=` container execution), `systemd-creds` encrypted secret injection, `loginctl enable-linger $USER`, journald streaming, cgroups v2 direct PID 1 monitoring, SELinux context (`:Z`)
- **Target Action**: Build `grade_rhcsa_lab.sh` validating Quadlets, pasta/Netavark networks, Landlock rules, persistent LVM UUIDs, and SGID permissions

### `Record my Gameplay` (XR / Media / Game Capture)
- **Stack**: `Python 3.12, OBS Studio 30/31, obsws-python, OpenCV`
- **Status**: `Active`
- **Frontier Architecture**: obs-websocket v5.x protocol, NVIDIA NVENC AV1 hardware encoding (`jim_av1_nvenc` and OBS 31 `obs_nvenc_av1_tex`), OpenCV template matching (`cv2.TM_CCOEFF_NORMED`) with multi-scale downscaled pyramids for sub-45ms boss health bar & victory screen detection, automated failed attempt disk purging (`Path.unlink`), direct integration into `youtube shorts edit for gaming`
- **Target Action**: Implement downscaled template matching loop in `vision_monitor.py` for hands-free detection; configure OBS encoder to NVENC AV1 for RTX 4080

### `Scary Water Slides` (XR / 3D Simulation / Media)
- **Stack**: `Three.js, WebGL, Web Audio, VFX`
- **Status**: `Active`
- **Frontier Architecture**: Playable 3D waterslide simulation (Space Exosphere, Avalanche, Volcanic Core), Three.js r184/r185 TSL continuous gravity tube splines with Catmull-Rom interpolation, real-world terrain 4K VFX integration (Blender camera tracking, PBR glass BSDF, Runway Gen-3/Kling 1.5 AI motion), top 0.1% YouTube packaging drawer
- **Target Action**: Record 4K simulation runs; generate episode 1 thumbnail assets and test audio synthesis; test Three.js r184 TSL water shader nodes

### `Scripting` (Linux / PowerShell Automation)
- **Stack**: `Bash, RHEL 9.5/10, PowerShell 5.1/7+, Pester 5.5+`
- **Status**: `Active`
- **Frontier Architecture**: Production RHEL 10 & systemd v256+ `run0` privilege management (`--machine=` container debug shells), defensive Bash standards (`set -euo pipefail`, `IFS`), LVM storage monitoring, firewalld rich rules, Modern PowerShell cmdlet architecture (`[CmdletBinding(SupportsShouldProcess)]`, `[PSCustomObject]` streaming), Pester 5.5+ unit testing, `script-coach` AI mentor
- **Target Action**: Execute `Test-Runner.ps1` and `test.sh` to validate all 14 labs; link interactive portal (`webpage/index.html`) into `My Custom Gui` quick launcher

### `Social Media` (Media / Staging)
- **Stack**: `Asset Staging, Markdown`
- **Status**: `Staging`
- **Frontier Architecture**: Social media distribution staging ground, scheduled content queue, multi-platform publishing templates (YouTube Shorts, TikTok, Instagram Reels, X/Twitter)
- **Target Action**: Build automated distribution dispatcher linking rendered video outputs from `youtube channels` and `youtube shorts edit for gaming`

### `Track Home Value` (Finance / Real Estate)
- **Stack**: `Python, Chart.js, CSV, JSON`
- **Status**: `Active`
- **Frontier Architecture**: Collin CAD scraper, Zestimate/Redfin consensus, Collin County ARB Tax protest CMA generator, official Texas Property Tax Form 50-132 evidence packet (Collin CAD account # 2883011 for 1766 Crestridge Cir Princeton TX generated via `MCP`)
- **Target Action**: Integrate automated sales comps calculation ($/sqft variance modeling) directly into annual protest PDF pipeline; sync valuation metrics to `My Custom Gui`

### `VR creation apps` (XR / VR)
- **Stack**: `WebXR, Three.js, Quest 3`
- **Status**: `Active`
- **Frontier Architecture**: Three.js `WebGPURenderer` (`await renderer.init()`), Three.js r184 non-blocking `compileAsync()` and WebGL compatibility layers for TSL node materials on `WebGLRenderer`, Three.js r185 full WebGPU feature parity & native immersive VR support directly into `WebGPURenderer`, TSL (Three Shading Language) transpiling dynamically to WGSL and GLSL, node-based `RenderPipeline` with MRT, Quest 3 bare-hand tracking (`XRHandModelFactory`), HRTF Web Audio
- **Target Action**: Upgrade `word-defender-xr.html` to Three.js r184/r185 WebGPURenderer with `compileAsync()` and TSL `RenderPipeline`; integrate `XRHandModelFactory` pinch firing

### `agent 365` (AI / Enterprise Productivity)
- **Stack**: `Python 3.12, FastAPI, Pydantic v2, MSAL`
- **Status**: `Active`
- **Frontier Architecture**: Authentic 1-to-1 Microsoft 365 replica, multi-agent Copilot orchestrator (Chief of Staff DAG task breakdown across Mail, Calendar, OneDrive, Teams, and Office specialists), MSAL Graph API client + in-memory mock tenant, high-gloss lacquer UI
- **Target Action**: Expand multi-agent DAG task decomposition; wire in real-time execution telemetry to `automate my day` and `deploy` suite

### `ai defense` (Cybersecurity / AI Safety)
- **Stack**: `Python 3.12, HTML5, High-Gloss Lacquer`
- **Status**: `Active`
- **Frontier Architecture**: Aegis-AI Defense Matrix: 5-layer zero-trust agent containment, gVisor microVMs (`runsc`), AST parameter validation, eBPF Tetragon in-kernel telemetry, default-deny DNS egress proxy, emergency hardware killswitch
- **Target Action**: Deploy live simulation testbed on port 5050; bind anomaly alerts to Sysmon and `MY Security`

### `ai models tools from threads` (AI / Directory & Studio)
- **Stack**: `HTML5, TailwindCSS, JSON, JS`
- **Status**: `Active`
- **Frontier Architecture**: Curated AI tools directory (reasoning, video, audio, design, web builders), Synthetix Studio workspace, multi-modal pipeline templates
- **Target Action**: Sync `tools_catalog.json` with latest 2026 frontier releases; connect quick-launch buttons to `My Custom Gui`

### `ai slop` (Automation / Code Craftsmanship)
- **Stack**: `PowerShell 7+, Regex, AST, Git Hooks, Windows Scheduler`
- **Status**: `Active`
- **Frontier Architecture**: Anti-Slop Craftsman automated audit engine (`Invoke-AntiSlopAudit.ps1`), 6 community anti-patterns (Emoji Asset Flips, LLM Purple Prose, Shovelware Ad-Traps, Shallow Dilution, Zero Kinesthetics & Lifeless Touch, Sub-48dp touch targets), `Clear-AiSlop.ps1` automated remediation, `Register-AntiSlopSchedule.ps1` recurring audit
- **Target Action**: Execute `Invoke-AntiSlopAudit.ps1` across all workspace projects; register daily scheduled audit; integrate anti-slop quality score into `deploy/health_status.json` and morning briefings

### `anime` (Media)
- **Stack**: `Python, PowerShell, REST`
- **Status**: `Active`
- **Frontier Architecture**: AniList GraphQL API, Plex/Kodi naming format compliance, structured `.nfo` generator
- **Target Action**: Build AniList scraper script matching video files and generating structured `.nfo` metadata

### `architect` (Architecture)
- **Stack**: `Markdown, Mermaid, HTML`
- **Status**: `Active`
- **Frontier Architecture**: Mermaid.js global diagrams, control plane sequence diagrams, living architecture map
- **Target Action**: Maintain living system architecture map reflecting new OpenShift, Anti-Slop, financial, and trading nodes

### `automate my day` (Productivity)
- **Stack**: `Python 3.12, UV, Batch, VBS, Kokoro-82M, FFmpeg`
- **Status**: `Active`
- **Frontier Architecture**: Passive income sentinel daemon (`sentinel_daemon.py`, `storage_cleaner.py`), automated clip cutter & YouTube shorts converter (`convert_to_shorts.py`, `smart_cutter.py`, `sfx_manager.py`) processing TEKKEN 8, Beast of Reincarnation, and Sonic Racing clips, Kokoro-82M ONNX speech synthesis (`morning_brief.wav`), multi-source telemetry ingestion, Stock Watch coiling alerts
- **Target Action**: Verify sentinel daemon automated clip processing; ensure morning audio briefing synthesizes daily telemetry via Kokoro-82M ONNX

### `aws` (Cloud / DevOps)
- **Stack**: `Markdown, Terraform, CDK`
- **Status**: `Active`
- **Frontier Architecture**: AWS CDK v2 (Python), Terraform, IAM Identity Center (SSO), EventBridge GuardDuty auto-quarantine
- **Target Action**: Supplement Cloud Practitioner domains with reproducible Terraform modules and SCP guardrails

### `backgrounds for gaming,apps` (Graphics / Dev)
- **Stack**: `HTML5, CSS3, JS, Python`
- **Status**: `Active`
- **Frontier Architecture**: 5-layer parallax engine, horizontal seamless feathering, automated contrast squint test
- **Target Action**: Deploy Python background processor for seamless loop generation and squint contrast checks

### `baselines` (Automation / Standards)
- **Stack**: `Python, PowerShell, High-Gloss Lacquer`
- **Status**: `Active`
- **Frontier Architecture**: Automated workspace habit tracking & pattern synthesis across 1,042+ conversation prompts, automated rule synthesis to `Projects/AGENTS.md`, `Sync-StillCosmicAndLacquer.ps1` distribution across 16 project hubs
- **Target Action**: Execute daily midnight cron via `Register-BaselineSchedule.ps1`; stream synthesized rules into Ollama knowledge base

### `bot finder` (Cybersecurity)
- **Stack**: `Python, UV, FastAPI`
- **Status**: `Active`
- **Frontier Architecture**: TLS fingerprinting (JA4), Heuristic IP reputation, Token buckets, rate-limiting middleware
- **Target Action**: Add JA4 fingerprint inspection and rate-limiting middleware to FastAPI server

### `chancenvaders` (Games / Retro Arcade)
- **Stack**: `HTML5 Canvas, Procedural Web Audio API, JS`
- **Status**: `Active`
- **Frontier Architecture**: Museum-grade 1978 Space Invaders Arcade Replica, 100% Intel 8080 spec fidelity (`invaders.asm`), bitmask sprite matrices, destructible arched bunkers with dynamic pixel blast carving, procedural Web Audio API synthesizer (discrete oscillators, 4-tone accelerating march 55.0Hz down to 33ms, zero audio files), continuous vertical swept-bounding-box raycast intervals (`[min(y, prevY), max(y, prevY)]` with `±3px` horizontal tolerances eliminating bullet tunneling), point-and-click finger/touch aim and rapid-fire streaming, 5 collectible power-up pods (Cyan Spread Laser, Neon Green Piercing Beam, Amber Shield, Orange Overdrive Rapid, Crimson Nuke), 6-tier Orbital Tower Ascension elevator, 1978 Pepper's Ghost Mirror Illusion (lunar diorama backdrop behind semi-transparent two-way mirror, 45-degree cabinet shelf reflection, cellophane color overlays)
- **Target Action**: Add localStorage high scores persistence; integrate Gamepad API haptic rumble vibration; scaffold WebGL 3D curved CRT bezel simulation

### `chess` (Games)
- **Stack**: `JS, CSS, WebAssembly`
- **Status**: `Active`
- **Frontier Architecture**: Stockfish 16+ WebAssembly in Web Workers, client evaluation bar, blunder coaching, high-contrast SVG pieces
- **Target Action**: Integrate Stockfish 16 WASM worker for real-time engine evaluation and blunder coaching

### `chrome tab and bar` (Browser Extension)
- **Stack**: `Manifest V3, JS, CSS, Chrome APIs`
- **Status**: `Active`
- **Frontier Architecture**: Google Chrome Manifest V3 2026 standard, persistent `chrome.sidePanel` with Chrome 140+ `sidePanel.getLayout()` dynamic left/right docking orientation awareness (and Chrome 148+ `browser.sidePanel.getLayout()` cross-browser namespace), programmatic `chrome.tabGroups` auto-categorization and color palettes, proactive memory reclamation via `chrome.tabs.discard`, `chrome.system.memory` & `chrome.system.cpu` live HUD telemetry, custom breadcrumb status bar, `chrome.storage.session` state persistence
- **Target Action**: Implement `sidePanel.getLayout()` in `sidepanel.js` to dynamically mirror UI layout based on left/right docking; integrate search, domain auto-grouping, and sleep controls

### `comptia exam simulator` (Education)
- **Stack**: `HTML, JS, CSS`
- **Status**: `Active`
- **Frontier Architecture**: SY0-701 domain weighting, Performance-Based Questions (PBQ), interactive network topologies, `diagnose.html` diagnostic engine
- **Target Action**: `diagnose.html` diagnostic PBQ engine implemented and verified (health restored to 100% Healthy 17/17); expand domain-specific PBQ network simulation questions

### `deal Finder` (E-Commerce)
- **Stack**: `Python, Playwright, SQLite`
- **Status**: `Active`
- **Frontier Architecture**: Multi-store deal scrapers (Amazon, Best Buy), 90-day ATL tracker, discount code harvester
- **Target Action**: Build initial Playwright price drop crawler storing daily hardware pricing in SQLite

### `deploy` (DevOps / Control)
- **Stack**: `PowerShell, SQLite, JSON`
- **Status**: `Active`
- **Frontier Architecture**: Automated health audits (`Test-ProjectHealth.ps1`), full portfolio catalog sync (`PROJECT_CATALOG.json` tracking all 76 projects, 32 deployable, 6 in progress), nightly health scan (verified 2026-11-11 23:46:51: 17/17 Deploy Suite 100% Healthy, 0 degraded, 0 critical in 7,021ms)
- **Target Action**: Maintain continuous health verification and sync all 76 active projects into `PROJECT_CATALOG.json`; link new 'index folder' into automated deployment manager

### `desktopscreensaver` (Graphics)
- **Stack**: `HTML5 Canvas, JS`
- **Status**: `Active`
- **Frontier Architecture**: Hardware-accelerated canvas particles, dynamic frame pacing, idle power conservation
- **Target Action**: Add automatic frame throttling when window is unfocused to conserve GPU cycles

### `docker` (DevOps / Containers)
- **Stack**: `PowerShell, Docker Desktop 4.98+, WSL2, Linux`
- **Status**: `Active`
- **Frontier Architecture**: Enterprise Container Virtualization on Windows 11 with WSL2, Intel Core i9-13900HX VT-x/VT-d firmware enablement, `.wslconfig` Mirrored Mode networking (`networkingMode=mirrored`), `dnsTunneling=true`, `autoProxy=true`, `virtiofs=true` high-performance shared-memory filesystem acceleration (slashing bind mount latency over legacy 9P), `autoMemoryReclaim=gradual` and `pageReporting=true` (dynamic RAM reclamation eliminating bloated `vmmemWSL`), `sparseVhd=true`, Docker Compose v2, rootless Podman 5 vs Docker CLI context bridging (`DOCKER_HOST`)
- **Target Action**: Verify VT-x firmware status post-reboot; execute `Test-DockerEnvironment.ps1 -RunContainerTest`; test multi-service stack with `docker compose up -d`; apply Mirrored networking in `.wslconfig`

### `email organizer` (Automation)
- **Stack**: `Python, UV, Gmail API`
- **Status**: `Active`
- **Frontier Architecture**: OAuth2 token refresh lifecycle, LangGraph triage agent, IBM Docling attachment parsing
- **Target Action**: Route invoice/receipt attachments directly to Google Drive structured folders; stream spam senders to `spam block`

### `game mods` (Game Dev)
- **Stack**: `Batch, Asset Injectors, HTML`
- **Status**: `Active`
- **Frontier Architecture**: Mod conflict resolver, automated asset validator, IoStore (`.utoc`/`.ucas`) extraction with FModel, Xbox PC GUI dashboard (`xbox_pc_gui.html`)
- **Target Action**: Build checksum validation script verifying patched game assets against known good hashes; polish `xbox_pc_gui.html`

### `game review` (Media / Script)
- **Stack**: `Markdown`
- **Status**: `Active`
- **Frontier Architecture**: Video metadata optimization, B-roll cue synchronization, narration script templates, Anti-Slop narrative depth
- **Target Action**: Align *A Plague Tale: Resonance* script timestamps with captured gameplay footage

### `game studio` (Game Dev)
- **Stack**: `C++ UE5, Godot 4.3/4.4, Unity 6, MSVC, ROMs`
- **Status**: `Active`
- **Frontier Architecture**: Unreal Engine 5 C++ (`ShadowBlade_Tekken_Naraka_UE5` Battle Royale: Naraka clash, Tekken heat, Ninja Gaiden Izuna drop), Godot 4 3D arena (`ShatteredPagoda_Godot` with 3D models, scenes, tests, `Launch_Kagura_Godot3D.bat`, `Play_Kagura_Godot3D.vbs`), `ChessClash_Godot`, `aether_ascent_spire` build, 3D Art Studio (`index.html`, `game-studio-scene.js`, `game-studio-engine.js`), automated studio quality gate verification (`Test-StudioQualityGate.ps1`), BPS/UPS delta-patching, Capstone disassembly, Anti-Slop hit-stop kinesthetics
- **Target Action**: Execute `Test-StudioQualityGate.ps1`; run `Launch_Kagura_Godot3D.bat` to verify 3D pagoda arena rendering; benchmark Forward+ clustered lighting and hit-stop frame freezing

### `google drive organizer` (Automation)
- **Stack**: `PowerShell, Google Drive API`
- **Status**: `Active`
- **Frontier Architecture**: PEP 723 inline script metadata, SHA-256 deduplication, automatic OAuth2 token refresh
- **Target Action**: Implement hash-based pre-upload check to eliminate redundant cloud uploads

### `improve gaming pc performance` (Gaming / Tuning)
- **Stack**: `PowerShell 7+, Registry, WMI, UE5 Ini`
- **Status**: `Active`
- **Frontier Architecture**: Dynamic Ultimate Performance power plan (`$UltimatePlanGuid = "ce71df13-30de-418e-9c7c-7afb0a84dc89"`), discrete RTX 4080 GPU registry assignment (`HKCU:\Software\Microsoft\DirectX\UserGpuPreferences`, `GpuPreference=2;`), Phantom Blade Zero (PBZ) & Steam continuous performance watcher (`Start-SteamGamingPerformanceWatcher.ps1` polling every 5s), automated optimization suite (`Invoke-PBZOptimization.ps1`), process priority elevation (`High`), UE5 `Engine.ini` streaming & async compute tuning (`r.Streaming.PoolSize=6144`, `r.CreateShadersOnLoad=1`, `r.AsyncCompute=1`, `FX.Niagara.AllowAsyncBudgeting=1`), GPU MSI-X mode verification, Windows 11 24H2 DirectStorage 1.2 GPU decompression
- **Target Action**: Execute `Invoke-PBZOptimization.ps1` prior to gaming sessions; register `Start-SteamGamingPerformanceWatcher.ps1` as a startup background daemon; verify `Engine.ini` 6GB texture pool & shader preload across steamapps directories

### `index folder` (Portals / Workspace Navigation & 3D Museum)
- **Stack**: `HTML5, Three.js WebGL, JS, CSS, High-Gloss Lacquer`
- **Status**: `Active`
- **Frontier Architecture**: Antigravity Central Directory & Index Hub, 3D Art Gallery Studio & Index Museum (`3d-gallery-studio.html`, `3d-gallery-studio.js`, `Launch_3D_Art_Gallery_Studio.url`) with first-person WASD controls, automated VIP cinematic tour, minimap radar, and iframe previews, 5 domain category trees (`01_Cybersecurity_and_IT`, `02_Games_and_Simulation`, `03_AI_and_Agent_Systems`, `04_Web_Apps_and_Media`, `05_Productivity_and_Finance`), and multi-root workspace config (`Antigravity_Projects.code-workspace`)
- **Target Action**: Maintain directory shortcuts and 3D Art Gallery Studio; sync new project additions into `projects-catalog.js` and `PROJECTS_DIRECTORY.md`; link to `deploy` and `My Custom Gui`

### `inspect my pc for improvements` (SysAdmin / Tuning)
- **Stack**: `PowerShell, WMI`
- **Status**: `Active`
- **Frontier Architecture**: Windows Performance Toolkit (`xperf`), SSD SMART diagnostics, DPC/ISR latency sweeps
- **Target Action**: Implement DPC and ISR latency check to flag driver-level audio/gaming microstutter

### `is this AI` (AI / Detection)
- **Stack**: `Python, Transformers, FFT`
- **Status**: `Active`
- **Frontier Architecture**: 2D Fourier FFT spectral radial power density analysis, Kirchenbauer watermarking, acoustic phase flattening
- **Target Action**: Implement 2D FFT radial power density check to catch synthetic diffusion grid artifacts

### `mobile game` (Mobile / Game Dev)
- **Stack**: `React Native 0.88, Expo, TypeScript, Nitro Modules`
- **Status**: `Active`
- **Frontier Architecture**: React Native 0.88, Expo SDK 53/54, TypeScript, Margelo Nitro Modules (`react-native-nitro-modules`, `nitrogen` code generator, Swift 5.9+ direct C++ interop, Android `fbjni`, compile-time JSI bindings delivering ~7.27ms vs 115ms per 100k calls), Aether Ascent dual-mode card battle engine: Gwent 3-row tactical warfare (`gwentEngine.ts`, `gwentCards.ts`, Hayabusa faction kodachi/kusarigama/odachi, `GwentScreen.tsx`), Slay the Spire roguelike ascension (`spire.ts`, `spireCards.ts`, `spireEnemies.ts`, `SpireCombatScreen.tsx`), Afro-Asian warrior animated motion stage (`AfroAsianMotionStage.tsx`), Chess campaign play mode (`chessAudioService.ts`, `ChessPlayScreen.tsx`, `CampaignShopModal.tsx`), clean-room monetization service (`monetization.ts`, `monetizationService.ts`), React Native New Architecture (Fabric), SHA-256 deterministic combat state hashing, Anti-Slop kinesthetics (haptics, spring tweening, min 48dp touch targets)
- **Target Action**: Benchmark Nitro Modules JSI hybrid objects against standard state recalculations; test Expo web export bundle in `mobile game/public`; test Gwent 3-row combat flows

### `monopoly` (Games)
- **Stack**: `HTML5 Canvas, JS, Python`
- **Status**: `Active`
- **Frontier Architecture**: Monte Carlo Tree Search (MCTS), Markov chain probabilities, adaptive AI trading, tactile piece movement
- **Target Action**: Implement MCTS bot decision engine for dynamic property trading valuation

### `note taker` (Productivity)
- **Stack**: `Markdown, Notes`
- **Status**: `Active`
- **Frontier Architecture**: SuperMemo SM-2 algorithm, Anki CSV export, Hierarchical notes
- **Target Action**: Add automated flashcard exporter converting Security+ notes into Anki flashcards

### `ollama` (AI / Knowledge Hub)
- **Stack**: `Python, Ollama, HTML/JS, FastMCP`
- **Status**: `Active`
- **Frontier Architecture**: Automated Antigravity skill ingestion, dynamic Modelfile generation, local HTTP web studio (`index.html`), Windows scheduled daily sync, dedicated Ollama Model Context Protocol server (`MCP/ollama-mcp`) exposing 6 specialized tools (`ollama_list_models`, `ollama_show_model`, `ollama_generate`, `ollama_chat`, `ollama_get_telemetry`, `ollama_studio_consult`) with FastMCP v4 / Python SDK v2 architecture
- **Target Action**: Verify `MCP/ollama-mcp` server tools integration; expand `sync_skills_to_ollama.py` to auto-ingest newly added project refinement blueprints into local system prompt; validate `index.html` Web Studio

### `onestop` (Portals / Hubs)
- **Stack**: `PowerShell, HTML, CSS`
- **Status**: `Active`
- **Frontier Architecture**: Lightweight local PowerShell HTTP server, health status badge, quick-launch grid
- **Target Action**: Add live health badge polling from `deploy/health_status.json`

### `openshift` (Linux / Platform Engineering)
- **Stack**: `OpenShift 4.17/4.18/4.19, Kubernetes 1.30-1.32, oc, Podman 5, Helm, Argo CD`
- **Status**: `Active`
- **Frontier Architecture**: Red Hat OpenShift Administration II (DO280) & EX280 certification curriculum, DO180 container architecture, DO380 advanced automation, OpenShift 4.17 (K8s 1.30, OVN-Kubernetes mandatory), 4.18 (K8s 1.31 EUS, User Defined Networks UDNs GA, Secrets Store CSI Driver Operator GA for external vault/GCP secret injection without etcd storage, `cert-manager` v1.15), 4.19 (Built on K8s 1.32 & CRI-O 1.32 on RHEL 9.6 RHCOS; complete removal of cgroups v1 with strict cgroups v2 requirement; Kubernetes Gateway API Generally Available via Service Mesh 3 with Istio 1.26 + Envoy for L4/L7 routing and traffic splitting; BGP Route Advertisements for ClusterUserDefinedNetworks CUDNs with FRR via `k8s.ovn.org/v1` `RouteAdvertisements` CR; Network Observability Operator native UDN flow tracing; unified console merging Admin and Developer views; `cert-manager` Router direct secret loading; oc-mirror v2 with Cosign SigStore tag signatures for air-gapped supply chain verification), Security Context Constraints (SCC `restricted-v2`), Ingress Routes TLS profiles (Edge, Passthrough, Re-encrypt), dynamic CSI StorageClasses, `oc adm must-gather` & `ovn-trace`
- **Target Action**: Validate OpenShift 4.19 strict cgroups v2 compatibility; configure Gateway API HTTPRoute manifests and CUDN BGP route advertisements; execute `diagnose-route.ps1` and `deploy-hello-world.ps1`; test oc-mirror v2 Cosign SigStore signatures; integrate EX280 timed mock exam engine

### `opensource` (DevOps / Governance & Supply Chain)
- **Stack**: `Markdown, Git, GitHub CLI, CycloneDX, SPDX, Python`
- **Status**: `Active`
- **Frontier Architecture**: Open-Source Program Office (OSPO) architecture, OpenChain (ISO/IEC 5230) license compliance, automated CycloneDX 1.6 / SPDX 3.0 profile-based SBOM generation (ECMA-424 & ISO/IEC standards), OpenSSF Scorecard automated security auditing (0-10 security rating across 18 checks), SLSA Level 3 build provenance with Cosign/Sigstore keyless OIDC attestations, automated Git submodule/subtree upstream sync (`Sync-UpstreamForks.ps1`), SemVer 2.0.0 release automation with `git-cliff`
- **Target Action**: Scaffold `ospo_governance.py` and `Generate-ProjectSbom.ps1`; enforce SPDX license headers across all 76 portfolio repositories; deploy automated upstream fork synchronizer

### `personal assistant` (AI / Desktop)
- **Stack**: `Python, Audio, JSON`
- **Status**: `Active`
- **Frontier Architecture**: Faster-Whisper Turbo (CTranslate2), Kokoro-82M v1.0 ONNX (`kokoro-onnx` + G2P `misaki`), multi-voice linear interpolation blending (`0.6 * voice_sarah + 0.4 * voice_adam`), Structured JSON Tool Calling, sub-150ms speech loops
- **Target Action**: Implement sub-150ms speech loop; bind `inspect_pc`, `windows event viewer`, and `automate my day` as callable tools

### `personal training` (Health / Fitness)
- **Stack**: `Markdown`
- **Status**: `Active`
- **Frontier Architecture**: Progressive overload tracking, 1RM Brzycki formula metrics, volume fatigue autoregulation
- **Target Action**: Add automated weekly volume calculator and deload week recommendation script

### `portfolio` (Web / Showcase)
- **Stack**: `HTML5, CSS3, JS`
- **Status**: `Active`
- **Frontier Architecture**: Dynamic JSON project catalog sync, dark-mode animations, interactive category filtering
- **Target Action**: Connect project showcase cards directly to live `deploy/PROJECT_CATALOG.json`

### `project refinement` (Strategy / Docs)
- **Stack**: `Markdown, Schemas`
- **Status**: `Active`
- **Frontier Architecture**: 5 Frontier Blueprints, Action Matrix, Daily automated refresh, 2026 intelligence pipeline
- **Target Action**: Keep master blueprints continuously aligned with 2026 tech breakthroughs across all active projects in the portfolio

### `reverse engineer applications` (Cybersecurity)
- **Stack**: `Ghidra 11.3, x64dbg, PE-bear`
- **Status**: `Active`
- **Frontier Architecture**: Headless Ghidra 11.3 decompilation, PyGhidra CPython 3 (JPype, `./support/pyghidra`), `JitPcodeEmulator` (JIT P-code translation to JVM bytecode for 3x-5x accelerated unpacking and string decryption), VS Code module project scaffolding, IAT inspection
- **Target Action**: Build automated headless Ghidra Python script using PyGhidra and `JitPcodeEmulator` to unpack binaries and extract decrypted strings

### `sandbox` (DevOps / Test)
- **Stack**: `Python, PowerShell, Web`
- **Status**: `Active`
- **Frontier Architecture**: Mock HTTP endpoints, rapid prototyping sandbox, isolated script validation
- **Target Action**: Maintain isolated staging ground for testing experimental scripts before project deployment

### `scheduled task` (DevOps / Ops)
- **Stack**: `Windows Task Scheduler, PS1`
- **Status**: `Scaffolding`
- **Frontier Architecture**: Event-driven triggers, PowerShell task health logger, automated task failure alerts
- **Target Action**: Add automated daily health check auditing all registered Antigravity scheduled tasks

### `screen reader` (Accessibility)
- **Stack**: `Python, Surya OCR, Piper TTS`
- **Status**: `Active`
- **Frontier Architecture**: IBM Docling / Surya OCR layout parsing, Piper TTS, Tkinter UI snapshot caching, bookmarks persistence
- **Target Action**: Replace legacy OCR with Surya/Docling to read multi-column technical PDFs without text interleaving

### `spam block` (Privacy / Security)
- **Stack**: `Python, Flask, Playwright, XML`
- **Status**: `Active`
- **Frontier Architecture**: Headless Playwright opt-out runner (`kevinl95/privotron` pattern), Texas TDPSA & HB 2802 compliance, California DELETE Act (DROP), Gmail filter XML rules
- **Target Action**: Deploy automated Playwright opt-out runner for 15+ data brokers; sync suppression status and spam filters to `email organizer`

### `stock Bot traders` (Quantitative Finance / Algotrading)
- **Stack**: `Python 3.12, alpaca-py, CCXT, Flask`
- **Status**: `Active`
- **Frontier Architecture**: Multi-broker execution architecture (Alpaca equities & CCXT crypto), `alpaca-py` parent `LimitOrderRequest` (zero entry slippage) & stop-limit `StopLossRequest`, rug pull detector & liquidity cliff sentinel (`core/rug_pull_detector.py`), regulatory compliance engine (PDT & wash-sale check), vectorized alpha factors & screeners, real-time Web GUI dashboard (localhost:5000), automated daily upskilling knowledge logger
- **Target Action**: Ingest coiling volatility squeeze signals from `stock watch` into vector screener; enforce zero entry slippage via bracket limit orders

### `stock watch` (Quantitative Finance)
- **Stack**: `Python 3.12, UV, alpaca-py, cuDF`
- **Status**: `Active`
- **Frontier Architecture**: NVIDIA RAPIDS cuDF GPU acceleration (`cudf.pandas.install()`), Volume-Filtered Carter Squeeze (VWAP & 21/50 EMA), Wyckoff Spring smart-money absorption ($>2.0\times$ volume), Half-Kelly capital sizing, Alpaca paper-to-live execution slippage & spread delta logging
- **Target Action**: Implement slippage and spread-crossing delta logger in `alpaca_broker.py`; connect evening screener alerts to `automate my day` briefing

### `synergize and pay` (Strategy / Business)
- **Stack**: `Markdown, HTML`
- **Status**: `Active`
- **Frontier Architecture**: Digital product packaging, cross-project monetization matrix, turnkey distribution
- **Target Action**: Create turnkey commercial distribution packaging for PC Optimizer and Study Simulator

### `track most wanted` (E-Commerce)
- **Stack**: `Python, Chart.js, eBay API`
- **Status**: `Active`
- **Frontier Architecture**: eBay Browse API, `curl_cffi` TLS Chrome fingerprint impersonation (StockX), Webhook alerts
- **Target Action**: Set up automated alert webhook notifying when ANTA KAI "Ocean Eye" drops $\le \$120$

### `using ai agents for profit` (AI / Operations Engine)
- **Stack**: `Python 3.12, FastAPI, SQLite, Three.js WebGL`
- **Status**: `Active`
- **Frontier Architecture**: Antigravity Operations Engine: B2B document ingestion & reconciliation, 3D NPR pipeline topology simulator (cel/toon shaders, cross-hatching, inverted hull outlines), step-by-step packet simulator across 4 operational scenarios, Client Acquisition ROI & SOW Studio (`POST /api/roi/calculate`, `POST /api/proposal/generate`), forensic reconciliation drill engine, 6 deterministic business invariants, batch approvals (`POST /api/documents/batch-approve`), QuickBooks CSV export, and async outbound webhook dispatch
- **Target Action**: Maintain 6 core invariants; execute `pytest tests/test_pipeline.py`; link live demo to `My Custom Gui`

### `vulnerability management` (Cybersecurity)
- **Stack**: `C#, .NET 10 MVC, SQLite`
- **Status**: `Active`
- **Frontier Architecture**: Cisco PSIRT openVuln API, `CiscoPSIRT/openvuln-mcp` (Streamable HTTP at `apix.cisco.com/api/mcp/openvuln`), CSAF 2.0/3.0 JSON feeds, DefectDojo v2/v3, November 4, 2026 Disclosures: Cisco UCS Central Software RCE **CVE-2026-76506** (CWE-22 Path Traversal, CVSS 7.6, Bug ID `CSCwv60193`), Cisco Unified CM XSS **CVE-2026-76419** (CVSS 6.1), Cisco Identity Services Engine Authorization Bypass **CVE-2026-20241** (CVSS 5.3, `CWE-285` in cert services); Cisco official EOY vulnerability freeze until January 20, 2027; Actively Exploited Disclosures: **CVE-2026-76418** (ASA/FTD SSL VPN tunnel DoS with secondary auth, Bug ID `CSCwx26625`, actively exploited in wild, fixed in ASA 9.16.4.104+ / FTD 7.0.11+; emergency workaround: `no secondary-authentication`), **CVE-2026-20349** (ASA/FTD Remote Access SSL VPN HTTP processing flaw DoS actively exploited in wild - CVSS 8.6), **CVE-2026-76482** (Smart License On-Prem CVSS 10.0), **CVE-2026-76519** (Secure Email Gateway RCE in AMP - CISA KEV cataloged), **CVE-2026-20271** (IOS XE memory leak DoS), **CVE-2026-76465** (NX-OS MPLS OAM), **CVE-2026-76485/76486/76501** (NGOAM), **CVE-2026-76471** (NX-API), **CVE-2026-76498..500** (APIC), **CVE-2026-76466** (Expressway), **CVE-2026-111497** (Node.js Brotli RCE), **CVE-2026-20043/20236/20291/20356** (Snort 3 RCE - CVSS 9.0), **CVE-2026-76524** (Snort socket command exec - CVSS 7.8)
- **Target Action**: Ingest November 4, 2026 disclosures (CVE-2026-76506, CVE-2026-76419, CVE-2026-20241) and actively exploited CVE-2026-76418/76519 into automated scanner; lock scanner baseline for Cisco EOY freeze period until Jan 20, 2027; compile scanner with .NET 10 Native AOT

### `windows event viewer` (Cybersecurity)
- **Stack**: `PowerShell, Sysmon 15+, Batch`
- **Status**: `Active`
- **Frontier Architecture**: Sysmon Event IDs (1, 3, 7, 10, 22, 25), MITRE ATT&CK, automated McAfee scanner orchestration (`Invoke-McAfeeScanner.ps1`)
- **Target Action**: Connect `Invoke-McAfeeScanner.ps1` to automated alert triggers for LSASS dump attempts; parse hourly scan logs

### `youtube channels` (Media / YouTube Automation)
- **Stack**: `PowerShell, Python, YouTube Data API v3, FFmpeg, Pillow`
- **Status**: `Active`
- **Frontier Architecture**: Your Favorite Character's White Noise & Sleep Ambience Automation Engine, high-AVD 3–8 hour sleep loops, 2-Upload Funnel (12–18s discovery Short with Related Video pill funnelling into 3–8h sleep loop), 4-slot rotating character format (Eustace Bagge, Rolf, Courage Computer, Nostalgia Wildcard), dynamic anti-repetition visual loops (CRT static grain, farmhouse shadows, audio waveforms), 12 complete episodes generated with matching audio, thumbnails, and short/long videos (`ep01-eustace` through `ep12-sa1-mystic-ruins`), automated publishing queue (`Invoke-AutoUploadQueue.ps1`, `youtube_api_upload.py`, `Start-ChannelAndUploadWizard.ps1`, `New-WhiteNoisePair.ps1`), character rotation catalog updated 2026-11-10 10:51 PM
- **Target Action**: Execute `Invoke-AutoUploadQueue.ps1` across the 12 generated episodes; verify YouTube Data API v3 OAuth2 token refresh and scheduled publish cadence

### `youtube shorts edit for gaming` (Media / AI)
- **Stack**: `Python, FFmpeg 7, OpenCV`
- **Status**: `Active`
- **Frontier Architecture**: NVIDIA NVENC AV1 (`av1_nvenc`), Faster-Whisper karaoke subtitles (`.ass`), optical flow crosshair tracker, video craftsmanship pacing
- **Target Action**: Build FFmpeg script reframing 16:9 gameplay to 9:16 vertical video with animated `.ass` subs

### `zfold6 features` (Mobile / Android)
- **Stack**: `Markdown, Termux`
- **Status**: `Active`
- **Frontier Architecture**: Termux Linux environment, Tasker automation, DeX multi-window, bi-directional Syncthing sync
- **Target Action**: Document Termux Python execution recipes and bi-directional Syncthing sync scripts

