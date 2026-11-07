# Antigravity Acquired Skills & Projects Ecosystem Digest

Updated: 66 Acquired Skills | 80 Production Projects

## 📦 Part 1: Acquired Agent Skills Catalog

### Platform & Customizations (8 skills)

#### `agy-customizations`
Comprehensive guide and reference for the Antigravity Customization System. Use to explain how customizations work, their loading priority, discovery mechanisms, and to guide the creation of skills, rules, plugins, hooks, and MCP servers.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\agy-customizations\SKILL.md`

#### `antigravity-guide`
Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands, keybindings, and customizations (skills, rules, MCP, sidecars). Activate this skill when the user asks questions about how to use, configure, or customize Antigravity, AGY, the agy CLI, the Antigravity IDE, or Antigravity 2.0.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\antigravity_guide\SKILL.md`

#### `credentials`
Instructions for handling API keys and credentials safely, verifying their presence, and prompting the user to add them if missing using a safe protocol.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\credentials\SKILL.md`

#### `generative_ui`
How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show the user diagrams, data visualizations, interactive controls, educational walkthroughs, or any rich visual content beyond plain text and markdown.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\generative_ui\SKILL.md`

#### `permissioned-github`
Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environment.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\permissioned-github\SKILL.md`

#### `plugin`
How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and disable as a single unit. Use this skill when the user wants to enable, disable, install or uninstall a plugin, when they want to create a new plugin, or when a new customization should be packaged into a plugin rather than left loose. Also triggered by the /plugin slash command. Don't use for the underlying customization system itself — discovery roots, loading priority, or authoring a standalone skill, agent, rule, hook or MCP server outside a plugin; see the customizations guide skill for those.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\plugin\SKILL.md`

#### `ui-extension`
Build, package, run, and debug UI extensions for Antigravity: interactive web panels that render in the side pane, served by a Node.js sidecar using the built-in Sidecar SDK.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\ui-extension\SKILL.md`

#### `ui-plugin-navigation`
Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side pane. Use when a running UI plugin's panel would help with what the user is doing, or right after the user enables a new UI plugin pane and a shortcut to open it is handy.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\ui-plugin-navigation\SKILL.md`

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

### Literature & Knowledge Retrieval (7 skills)

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

#### `predictingthepast`
Ancient text restoration, attribution, dating, contextualization, and embedding via Aeneas (Latin) / Ithaca (Ancient Greek). Use when asked to "restore", "attribute", "date", "contextualize", "find parallels", "where was it written", "when was it written", "embed", or "analyze" an ancient text, inscription, or epigraphic document, or when the user mentions "Aeneas", or "Ithaca".

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\predictingthepast\SKILL.md`

#### `pubmed-database`
Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text. Link published research to biological databases (gene, protein, nucleotide, PubChem) to discover associations between papers and specific compounds or genes. Verify medical spelling, match raw citations, and cache result sets for bulk processing. Interfaces NCBI E-utilities and PMC BioC APIs.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pubmed_database\SKILL.md`

### Developer Workflows & Automation (12 skills)

#### `android-cli`
Provides instructions for installing and using the `android` CLI. The `android` command-line tool is a critical tool for Android development and helps you create new Android projects, run Android apps on devices, manage and interact with Android virtual devices (including screenshots and UI inspection), manage Android SDK components, look up official Android documentation, and discover and install official Android skills.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\SKILL.md`

#### `android-device-hub`
Instructions for working with the Android Device Hub sidecar, which lists, starts, stops, creates and removes Android Virtual Devices (AVDs), lists physical devices connected to adb, and lets the user mirror and control any of them (video, touch, keyboard, mouse wheel) in the Device Hub pane. Also explains how to inspect and interact with the screen the user is mirroring, with `android layout`, `android screen` and `adb`.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\device-hub\SKILL.md`

#### `anti-slop-craftsman`
Audits, prevents, and automatically enhances projects to eliminate AI slop across all codebases in the projects directory. Use when reviewing code for low-effort generative patterns, emoji asset flips, purple prose copy, shovelware ad-traps, missing kinesthetics/game juice, or when executing routine scheduled anti-slop maintenance.

- Source: `C:\Users\chase\.gemini\config\skills\anti-slop-craftsman\SKILL.md`

#### `automation`
Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an automated or recurring scheduled task (e.g. "summarize my emails every morning", "every Monday send me a to-do list"). Also triggered by the /automation slash command.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\automation\SKILL.md`

#### `compose-preview`
Instructions for the Android Compose Preview sidecar, which renders Jetpack Compose @Preview functions with `android preview render` and shows them in the Android Compose Preview pane. Use it when the user wants to see a Compose preview, or to review the result of UI changes — re-render after changing the code so that the pane shows the result.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\compose-preview\SKILL.md`

#### `enterprise-fullscreen-layout`
Architects full-screen (100vw x 100vh) enterprise web application layouts with collapsible left navigation sidebars, top command search bars (Ctrl+K), zero dead margin space, and dockable right inspector panels. Use when building or upgrading web apps, cloud dashboards, simulators, exam hubs, and internal developer tools.

- Source: `C:\Users\chase\.gemini\config\skills\enterprise-fullscreen-layout\SKILL.md`

#### `github-primer-anti-slop-ui`
Enforces professional GitHub Primer and enterprise cloud console design standards, completely eliminating AI slop hallmarks (raw emoji asset flips, floaty cards, purple prose) using crisp 1px borders, dual-tone inline SVGs, and High-Gloss Lacquer physical material optics.

- Source: `C:\Users\chase\.gemini\config\skills\github-primer-anti-slop-ui\SKILL.md`

#### `interactive-simulation-practice-engine`
Builds interactive, step-by-step traffic and packet journey simulators alongside gamified, self-grading system design drill engines with smart fuzzy matching, architectural hints, audio speech synthesis, and live progress rings. Use when creating educational tools, exam simulators, system architecture trainers, or interactive walkthroughs.

- Source: `C:\Users\chase\.gemini\config\skills\interactive-simulation-practice-engine\SKILL.md`

#### `migrate-workflows`
Automatically migrate legacy workflows to modern skills across global and workspace configurations. Scans for existing workflows, creates target SKILL.md files, and safely archives old workflow files.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\migrate-workflows\SKILL.md`

#### `script-practice`
Interactive scripting practice, challenge generator, code reviewer, and test runner for Red Hat Enterprise Linux (Bash/RHEL 8 & 9) and PowerShell (5.1 & 7+). Use when the user asks for scripting practice, challenges, code reviews, debugging assistance, or test execution for Linux bash or PowerShell.

- Source: `C:\Users\chase\.gemini\config\plugins\script-practice\skills\script-practice\SKILL.md`

#### `uv`
Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH. Use when another skill requires uv as a prerequisite.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\uv\SKILL.md`

#### `workflow-skill-creator`
Distills a completed user workflow or interaction into a reusable agent skill. Use when the user asks to turn their workflow, interaction, or multi-step process into a skill, or when they say "make this a skill", "create a skill from what we just did", "package this workflow" or similar. Do not use for creating skills from scratch without an existing workflow (use a generic skill-creator for that).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\workflow_skill_creator\SKILL.md`

### Media & Audience Strategy (1 skills)

#### `youtube-master-strategist`
Top 0.1% YouTube packaging strategist, retention engineer, and algorithm optimizer. Use when writing, auditing, or generating YouTube titles, thumbnails, hooks, scripts, pacing audits, and session-time retention bridges. Enforces strict CTR and AVD mechanics.

- Source: `C:\Users\chase\.gemini\config\skills\youtube-master-strategist\SKILL.md`


## 🚀 Part 2: Active Antigravity Projects Catalog

### `.pytest_cache` (Maintenance)
- **Stack**: `Cache Artifacts`
- **Status**: `Internal`
- **Frontier Architecture**: Automated test execution cache
- **Target Action**: Maintain `.gitignore` rules to keep repository trees clean of test cache files

### `1st grade learning` (Education)
- **Stack**: `HTML, JS, Audio`
- **Status**: `Active`
- **Frontier Architecture**: Gamified phonics engine, Web Audio sound effects, typing arcade, celebratory canvas particles
- **Target Action**: Expand spelling word dictionary and add positive reinforcement celebratory canvas particles

### `3d images` (3D / Graphics)
- **Stack**: `Node.js, WebGL, Shaders`
- **Status**: `Active`
- **Frontier Architecture**: WebGL2 stereoscopic shaders, glTF Draco mesh compression, Three.js TSL materials
- **Target Action**: Integrate Draco mesh compression to load high-resolution 3D models with minimal latency

### `Choogle` (Search / Portals)
- **Stack**: `Static Web, JS, CSS, PWA`
- **Status**: `Active`
- **Frontier Architecture**: Automated `Sync-ChoogleProjects.ps1` catalog sync, offline Service Worker, local inverted index
- **Target Action**: Sync search database with expanded project inventory and add offline search caching

### `Github Portfolio` (Web / Career Showcase)
- **Stack**: `HTML5, CSS3, JS, Markdown, PDF Resumes`
- **Status**: `Active`
- **Frontier Architecture**: Chase Hamilton Master Developer & Infrastructure Showcase, dynamic GitHub REST/GraphQL API integration, interactive terminal CLI modal (`whoami`, `cat resume`, `ls projects`, `skills`), Bento grid glassmorphism, live operational health badges synced from `deploy/health_status.json`
- **Target Action**: Integrate terminal emulator component in `app.js` and connect project cards to live `deploy/PROJECT_CATALOG.json` health badges

### `How to train your AI` (AI / Agents)
- **Stack**: `Ollama, Python, Modelfiles`
- **Status**: `Active`
- **Frontier Architecture**: TensorRT-LLM 1.x (PyTorch-native), vLLM 0.7+, Blackwell NVFP4 16-element micro-block scaling with FP8 E4M3 local scaling & FP32 global scaling via ModelOpt (`mtq.quantize` with `NVFP4_DEFAULT_CFG` or `NVFP4_MLP_ONLY_CFG`), dual export pathways (`export_tensorrt_llm_checkpoint` & `export_hf_checkpoint` via `hf_quant_config.json`), vLLM/SGLang native `--quantization modelopt_fp4 --linear-backend cutlass` with Marlin W4A16 fallback, ModelOpt Quantization-Aware Distillation (QAD), `KvCacheConfig(dtype='nvfp4')`, RoPE precision control (`skip_rope_quantization=True` / `2FP4`), Speculative Decoding (EAGLE-2 / DFlash)
- **Target Action**: Deploy `serve_vllm.ps1` with dynamic prefix caching; integrate AST parser and local ChromaDB knowledge base

### `Images` (Asset Store)
- **Stack**: `Image Formats (.heic, .jpg)`
- **Status**: `Active`
- **Frontier Architecture**: Shared high-res image repository, automated format converter (Pillow WebP batch compression)
- **Target Action**: Add Python image conversion script batch-converting mobile `.heic` photos to `.webp`

### `MCP` (Systems / AI Tools)
- **Stack**: `Node.js, JSON-RPC, Python`
- **Status**: `Active`
- **Frontier Architecture**: Centralized Model Context Protocol hub, custom MCP servers (`game-studio-mcp`, `game-capture-mcp`), mcp-baseline.js HUD, global `mcp_config.json` integration
- **Target Action**: Sync live tool availability to `My Planetarium` and `My Custom Gui`; enforce loopback HMAC token auth

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
- **Frontier Architecture**: 3D Interactive Deep Space Planetary Observatory & Sector Atlas, 64 charted planetary bodies, astronomical rigor, Antigravity bidirectional prompt dispatching (`window.sidecar.agent.sendMessage`), auto-fit panoramic projection (`[F]`), MCP matrix
- **Target Action**: Keep `projects-data.js` synchronized with expanded project inventory; package as Antigravity UI extension plugin

### `New folder (3)` (Maintenance / Staging)
- **Stack**: `Empty Workspace Dirs`
- **Status**: `Clean`
- **Frontier Architecture**: Temporary workspace cleanup rules, staging area isolation for ephemeral tests
- **Target Action**: Maintain clean staging isolation; archive or repurpose scratch directories into dedicated testbeds

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
- **Stack**: `Markdown, Shell, RHEL 9.5/10`
- **Status**: `Active`
- **Frontier Architecture**: Podman 5 Quadlets (`.container`, `.image`, `.volume`, `.network`, `.kube`, `.pod`), Netavark + `pasta` rootless networking (replacing slirp4netns), systemd v256+ `run0` (`--machine=` container execution), `systemd-creds` encrypted secret injection, `loginctl enable-linger $USER`, journald streaming, cgroups v2 direct PID 1 monitoring, SELinux context (`:Z`)
- **Target Action**: Build `grade_rhcsa_lab.sh` validating Quadlets, pasta/Netavark networks, persistent LVM UUIDs, and SGID permissions

### `Record my Gameplay` (XR / Media / Game Capture)
- **Stack**: `Python 3.12, OBS Studio 30/31, obsws-python, OpenCV`
- **Status**: `Active`
- **Frontier Architecture**: obs-websocket v5.x protocol, NVIDIA NVENC AV1 hardware encoding (`jim_av1_nvenc` and OBS 31 `obs_nvenc_av1_tex`), OpenCV template matching (`cv2.TM_CCOEFF_NORMED`) with multi-scale downscaled pyramids for sub-45ms boss health bar & victory screen detection, automated failed attempt disk purging (`Path.unlink`), direct integration into `youtube shorts edit for gaming`
- **Target Action**: Implement downscaled template matching loop in `vision_monitor.py` for hands-free detection; configure OBS encoder to NVENC AV1 for RTX 4080

### `Scary Water Slides` (XR / 3D Simulation / Media)
- **Stack**: `Three.js, WebGL, Web Audio, VFX`
- **Status**: `Active`
- **Frontier Architecture**: Playable 3D waterslide simulation (Space Exosphere, Avalanche, Volcanic Core), real-world terrain 4K VFX integration (Blender camera tracking, PBR glass BSDF, Runway Gen-3/Kling 1.5 AI motion), top 0.1% YouTube packaging drawer
- **Target Action**: Record 4K simulation runs; generate episode 1 thumbnail assets and test audio synthesis

### `Scripting` (Linux / PowerShell Automation)
- **Stack**: `Bash, RHEL 9.5/10, PowerShell 5.1/7+, Pester 5.5+`
- **Status**: `Active`
- **Frontier Architecture**: Production RHEL 10 & systemd v256+ `run0` privilege management (`--machine=` container debug shells), defensive Bash standards (`set -euo pipefail`, `IFS`), LVM storage monitoring, firewalld rich rules, Modern PowerShell cmdlet architecture (`[CmdletBinding(SupportsShouldProcess)]`, `[PSCustomObject]` streaming), Pester 5.5+ unit testing, `script-coach` AI mentor
- **Target Action**: Execute `Test-Runner.ps1` and `test.sh` to validate all 14 labs; link interactive portal (`webpage/index.html`) into `My Custom Gui` quick launcher

### `Track Home Value` (Finance / Real Estate)
- **Stack**: `Python, Chart.js, CSV, JSON`
- **Status**: `Active`
- **Frontier Architecture**: Collin CAD scraper, Zestimate/Redfin consensus, Collin County ARB Tax protest CMA generator
- **Target Action**: Build automated property tax protest packet generator using Collin CAD comps

### `VR creation apps` (XR / VR)
- **Stack**: `WebXR, Three.js, Quest 3`
- **Status**: `Active`
- **Frontier Architecture**: Three.js `WebGPURenderer` (`await renderer.init()`), TSL (Three Shading Language), node-based `RenderPipeline` (Three.js r183) with MRT, Quest 3 bare-hand tracking (`XRHandModelFactory`), HRTF Web Audio
- **Target Action**: Upgrade `word-defender-xr.html` to WebGPU/TSL with `RenderPipeline` and add `XRHandModelFactory` pinch firing

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
- **Stack**: `Batch, VBS, Markdown, Python`
- **Status**: `Active`
- **Frontier Architecture**: Kokoro-82M speech synthesis, multi-source telemetry ingestion, Stock Watch coiling alerts, automated YouTube Shorts packaging
- **Target Action**: Synthesize daily morning briefing into `morning_brief.wav` for audio playback

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
- **Frontier Architecture**: Google Chrome Manifest V3 2026 standard, persistent `chrome.sidePanel` with Chrome 140+ `sidePanel.getLayout()` dynamic left/right docking orientation awareness, programmatic `chrome.tabGroups` auto-categorization and color palettes, proactive memory reclamation via `chrome.tabs.discard`, `chrome.system.memory` & `chrome.system.cpu` live HUD telemetry, custom breadcrumb status bar, `chrome.storage.session` state persistence
- **Target Action**: Scaffold Manifest V3 manifest, background service worker, and sidepanel UI; integrate search, domain auto-grouping, and sleep controls

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
- **Frontier Architecture**: Automated health audits (`Test-ProjectHealth.ps1`), full portfolio catalog sync (71 tracked projects + 10 extension sub-projects), nightly health scan (17/17 Deploy Suite 100% Healthy)
- **Target Action**: Maintain continuous health verification and sync all active projects into `PROJECT_CATALOG.json`

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
- **Stack**: `C++ UE5, Unity 6, MSVC, ROMs`
- **Status**: `Active`
- **Frontier Architecture**: Unreal Engine 5 C++ (`ShadowBlade_Tekken_Naraka_UE5` Battle Royale), BPS/UPS delta-patching, Capstone disassembly, Anti-Slop combat feedback standards
- **Target Action**: Expand ShadowBlade C++ character combat system (Naraka clash, Tekken heat, Ninja Gaiden Izuna drop); verify hit-stop kinesthetics

### `google drive organizer` (Automation)
- **Stack**: `PowerShell, Google Drive API`
- **Status**: `Active`
- **Frontier Architecture**: PEP 723 inline script metadata, SHA-256 deduplication, automatic OAuth2 token refresh
- **Target Action**: Implement hash-based pre-upload check to eliminate redundant cloud uploads

### `improve gaming pc performance` (Gaming / Tuning)
- **Stack**: `PowerShell, Registry`
- **Status**: `Active`
- **Frontier Architecture**: GPU MSI mode verification, Dynamic Ultimate Performance power plan, timer resolution tuning
- **Target Action**: Create PowerShell tuning script enabling MSI mode on RTX GPU and optimizing timer resolution

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
- **Stack**: `React Native 0.88, Expo, TypeScript`
- **Status**: `Active`
- **Frontier Architecture**: Aether Ascent dual-mode card battle engine (Gwent 3-row tactical warfare + Slay the Spire roguelike ascension), React Native New Architecture (Fabric), Margelo Nitro Modules (`margelo/nitro`, package `react-native-nitro-modules`, ~7.27ms vs 115ms per 100k calls, Nitrogen code generator, Swift 5.9+ direct C++ interop, Android `fbjni`), SHA-256 deterministic combat state hashing, Anti-Slop kinesthetics (haptics, spring tweening, hit-stops, min 48dp touch targets)
- **Target Action**: Add deterministic battle state hashing to `gwentEngine.ts` and migrate critical card state bindings to Nitro Modules Hybrid Objects; enforce 48dp touch targets

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
- **Stack**: `Python, Ollama, HTML/JS`
- **Status**: `Active`
- **Frontier Architecture**: Automated Antigravity skill ingestion, dynamic Modelfile generation, local HTTP web studio, Windows scheduled daily sync
- **Target Action**: Expand `sync_skills_to_ollama.py` to auto-ingest newly added project refinement blueprints into the local system prompt

### `onestop` (Portals / Hubs)
- **Stack**: `PowerShell, HTML, CSS`
- **Status**: `Active`
- **Frontier Architecture**: Lightweight local PowerShell HTTP server, health status badge, quick-launch grid
- **Target Action**: Add live health badge polling from `deploy/health_status.json`

### `openshift` (Linux / Platform Engineering)
- **Stack**: `OpenShift 4.17/4.18/4.19, Kubernetes 1.30-1.32, oc, Podman 5, Helm, Argo CD`
- **Status**: `Active`
- **Frontier Architecture**: Red Hat OpenShift Administration II (DO280) & EX280 certification curriculum, DO180 container architecture, DO380 advanced automation, OpenShift 4.17 (K8s 1.30, OVN-Kubernetes only), 4.18 (K8s 1.31 EUS, User Defined Networks UDNs GA, Secrets Store CSI Operator GA, `cert-manager` v1.15), 4.19 (K8s 1.32, unified console, BGP Route Advertisements for ClusterUserDefinedNetworks CUDNs with FRR via `k8s.ovn.org/v1` `RouteAdvertisements` CR, Network Observability Operator native UDN flow tracing, strict cgroups v2, Service Mesh 3.1, Argo CD/Rollouts), Security Context Constraints (SCC `restricted-v2`), Ingress Routes TLS profiles (Edge, Passthrough, Re-encrypt), dynamic CSI StorageClasses, `oc adm must-gather` & `ovn-trace`
- **Target Action**: Execute `setup-workstation.ps1` and `check-binary.ps1`; run `diagnose-route.ps1` and `deploy-hello-world.ps1` to validate ingress routes and RBAC; configure CUDN BGP route advertisements; integrate EX280 timed mock exam engine

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

### `using ai agents for profit` (AI / Finance)
- **Stack**: `Python, SQLite, Pydantic v2`
- **Status**: `Active`
- **Frontier Architecture**: LangGraph StateGraph, Double-entry invariants, IBM Docling & Surya OCR receipts, SHA-256 cryptographic digests
- **Target Action**: Build cyclic self-correcting invoice parser with SHA-256 cryptographic checksums and anomaly isolation

### `vulnerability management` (Cybersecurity)
- **Stack**: `C#, .NET 10 MVC, SQLite`
- **Status**: `Active`
- **Frontier Architecture**: Cisco PSIRT openVuln API, `CiscoPSIRT/openvuln-mcp` (Streamable HTTP at `apix.cisco.com/api/mcp/openvuln`), CSAF 2.0/3.0 JSON feeds, DefectDojo v2/v3, October/November 2026 advisories (**CVE-2026-76418** ASA/FTD SSL VPN tunnel DoS actively exploited in wild, fixed in ASA 9.16.4.104+ / FTD 7.0.11+; `cisco-sa-asaftd-vpn-dos-dzv4mQFF`, `cisco-sa-sec-client-priv-esc-muF8eZdm`, **CVE-2026-76482** Smart License On-Prem CVSS 10.0, **CVE-2026-76519** Email Gateway RCE in AMP - CISA KEV, Secure Firewall & ISE hardening releases, **CVE-2026-76465** NX-OS MPLS OAM, **CVE-2026-76485/76486/76501** NGOAM, **CVE-2026-76471** NX-API, **CVE-2026-76498..500** APIC, **CVE-2026-76466** Expressway, **CVE-2026-76506** UCS Central RCE - CVSS 7.6, **CVE-2026-20236/20043** Snort 3 RCE - CVSS 9.0, **Nov 4, 2026 ISE/UCS Central/CUCM disclosures & Cisco EOY release freeze until Jan 20, 2027**)
- **Target Action**: Ingest actively exploited CVE-2026-76418, CVE-2026-76519, CVE-2026-76482, and CVE-2026-76506 into automated scanner; compile scanner with .NET 10 Native AOT

### `windows event viewer` (Cybersecurity)
- **Stack**: `PowerShell, Sysmon 15+, Batch`
- **Status**: `Active`
- **Frontier Architecture**: Sysmon Event IDs (1, 3, 7, 10, 22, 25), MITRE ATT&CK, automated McAfee scanner orchestration (`Invoke-McAfeeScanner.ps1`)
- **Target Action**: Connect `Invoke-McAfeeScanner.ps1` to automated alert triggers for LSASS dump attempts; parse hourly scan logs

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

