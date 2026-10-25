# Antigravity Acquired Skills Digest

## Platform & Customizations (8 skills)

### `agy-customizations`
Comprehensive guide and reference for the Antigravity Customization System. Use to explain how customizations work, their loading priority, discovery mechanisms, and to guide the creation of skills, rules, plugins, hooks, and MCP servers.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\agy-customizations\SKILL.md`

### `antigravity-guide`
Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands, keybindings, and customizations (skills, rules, MCP, sidecars). Activate this skill when the user asks questions about how to use, configure, or customize Antigravity, AGY, the agy CLI, the Antigravity IDE, or Antigravity 2.0.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\antigravity_guide\SKILL.md`

### `credentials`
Instructions for handling API keys and credentials safely, verifying their presence, and prompting the user to add them if missing using a safe protocol.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\credentials\SKILL.md`

### `generative_ui`
How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show the user diagrams, data visualizations, interactive controls, educational walkthroughs, or any rich visual content beyond plain text and markdown.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\generative_ui\SKILL.md`

### `permissioned-github`
Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environment.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\permissioned-github\SKILL.md`

### `plugin`
How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and disable as a single unit. Use this skill when the user wants to enable, disable, install or uninstall a plugin, when they want to create a new plugin, or when a new customization should be packaged into a plugin rather than left loose. Also triggered by the /plugin slash command. Don't use for the underlying customization system itself — discovery roots, loading priority, or authoring a standalone skill, agent, rule, hook or MCP server outside a plugin; see the customizations guide skill for those.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\plugin\SKILL.md`

### `ui-extension`
Build, package, run, and debug UI extensions for Antigravity: interactive web panels that render in the side pane, served by a Node.js sidecar using the built-in Sidecar SDK.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\ui-extension\SKILL.md`

### `ui-plugin-navigation`
Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side pane. Use when a running UI plugin's panel would help with what the user is doing, or right after the user enables a new UI plugin pane and a shortcut to open it is handy.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\ui-plugin-navigation\SKILL.md`

## Structural Biology & Molecular Modeling (11 skills)

### `alphafold-database-fetch-and-analyze`
Retrieve and analyze AlphaFold predicted structures for a protein. Use when the user provides a specific UniProt Accession ID and wants structural confidence metrics (pLDDT), domain boundary analysis, or disorder assessment. Do not use if the user only has a protein name, gene name, or amino acid sequence — ask for a UniProt ID first.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphafold_database_fetch_and_analyze\SKILL.md`

### `biomolecular-structure-viewer`
Interactive 3D biomolecular structure viewer via Mol*. Renders 3D molecular structures from local workspace files (.cif, .mmcif, .pdb) or conversation artifacts, and manages user 3D annotations and highlighted residues. Use when the user asks to visualise a protein or nucleic acid, display a 3D structure, or asks about 3D biomolecular structure annotations and highlighted residues.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\biomolecular_structure_viewer\SKILL.md`

### `foldseek-structural-search`
Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user provides a physical 3D coordinate file (.cif, .mmcif, or .pdb) and wants to find structurally similar proteins. Do NOT use if the user only provides a protein sequence, gene name, or UniProt ID.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\foldseek_structural_search\SKILL.md`

### `human-protein-atlas-database`
Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\human_protein_atlas_database\SKILL.md`

### `interpro-database`
Identify domains, families, and sites in proteins; find all proteins in a family or sharing a domain; explore species distribution for a domain; annotate genomes with protein families and GO terms. InterPro combines 14 databases (e.g., Pfam, CDD) into one searchable resource. InterPro-N significantly expands annotation and sequence coverage with deep learning. Includes domain architecture (IDA) search.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\interpro_database\SKILL.md`

### `pdb-database`
Use when you want to search for or download experimentally-determined 3D structures for biomolecules (proteins, nucleic acids, bound ligands). Supports searching by sequence similarity, structure similarity, chemical and other attributes. Also use to get metadata about biomolecular structure experiments.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pdb_database\SKILL.md`

### `protein-sequence-msa`
Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity, domain conservation, or key residue conservation. Supports up to 4000 sequences and a maximum file size of 4 MB. Do not use to search for homologous proteins in a database (use MMseqs2, BLAST), align non-protein sequences (DNA, RNA), perform structural alignment (use Foldseek, PyMOL), or if you only have a single sequence.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\protein_sequence_msa\SKILL.md`

### `protein-sequence-similarity-search`
Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback). Trigger this whenever the user provides a protein sequence or FASTA file and asks to find homologues, sequence matches, or wants to infer protein function based on sequence similarity, but not when the user wants to infer protein function based on structural similarity.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\protein_sequence_similarity_search\SKILL.md`

### `pymol`
Visualize, analyze, and render protein and molecular structures using PyMOL. Use when the user wants to create images of protein structures, perform structural alignments or superposition, measure distances or contacts, highlight binding sites or active site residues, color by B-factor/pLDDT, or analyze protein-ligand interactions. Do not use for docking, molecular dynamics, or sequence-only analysis.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pymol\SKILL.md`

### `string-database`
Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific proteins, interaction evidence, confidence scores, protein interaction partners, or pathway enrichments.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\string_database\SKILL.md`

### `uniprot-database`
Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins, mapping identifiers, or retrieving functional annotations and publications. Don't use for sequence alignment, protein folding, or sequence similarity search (use specialized skills for those tasks).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\uniprot_database\SKILL.md`

## Genomics & Variant Impact (14 skills)

### `alphagenome-atlas-website-links`
Constructs deep-links and URLs for the AlphaGenome Atlas website. Supports generating single-variant exploration links (1-based chr:pos:ref>alt), genomic locus views (1-based closed chr:start-end), candidate summary tables, and AlphaGenome reference vs. alternate predictions. Use whenever visualizing, exploring, charting, or linking genetic variants and genomic loci on the AlphaGenome Atlas, or when asked to inspect, view, or link predictions for a genomic variant.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphagenome_atlas_website_links\SKILL.md`

### `alphagenome-single-variant-analysis`
Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNASE), histone marks (ChIP), and transcription factors using the AlphaGenome API. Use when the user asks about non-coding variant effects, pathogenicity, clinical significance, disease associations, functional effects, gene expression changes, splicing disruption, or regulatory effects in promoters and enhancers. Also use for resolving biological terms to tissue/cell-type ontologies (UBERON/CL) or analyzing variants in chr:pos:ref>alt format.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphagenome_single_variant_analysis\SKILL.md`

### `alphagenome-variant-impact-score`
Score, annotate, and analyze the functional impact of genetic variants using AlphaGenome Variant Impact (AVI) scores. Query variants in chr:pos:ref>alt format, annotate VCF/tabular callsets, perform saturation mutagenesis window scans (1-based closed chr:start-end), and extract GENCODE v46 GTF gene/exon/junction coordinates all via the AlphaGenome Atlas API.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\alphagenome_variant_impact_score\SKILL.md`

### `clinvar-database`
Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales, or finding "hard positive" benchmark controls for human genomic variants.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\clinvar_database\SKILL.md`

### `dbsnp-database`
Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs, genomic coordinates in VCF format, and HGVS strings. For an rsID, returns variant type, gene associations, clinical significance, allele frequencies, and genomic coordinates (GRCh38).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\dbsnp_database\SKILL.md`

### `encode-ccres-database`
Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API, or make custom queries to the ENCODE Portal REST API for experiments and files (ChIP-seq peaks, etc.). Use when you want to query regulatory annotations or raw experimental data across human cell types.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\encode_ccres_database\SKILL.md`

### `ensembl-database`
Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons), and get variant consequence and effect predictions (VEP). Use this skill as a primary ID translator, genomic sequence database and variant effect prediction tool.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\ensembl_database\SKILL.md`

### `gnomad-database`
Query the Genome Aggregation Database (gnomAD). Use when determining the rarity or allele frequency of specific genetic variants, retrieving gene constraint metrics (pLI, LOEUF) to assess loss-of-function intolerance, finding variants in a genomic region or gene, or querying structural variants. Don't use for analyzing individual patient genomes, tracking somatic mutations in cancer (use COSMIC), or requesting raw sequencing reads (use ENA).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\gnomad_database\SKILL.md`

### `gtex-database`
Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project across 54 non-diseased tissue sites.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\gtex_database\SKILL.md`

### `jaspar-database`
Query the JASPAR database for Transcription Factor (TF) binding profiles. Use when retrieving Position Frequency Matrices (PFMs) or Position Weight Matrices (PWMs) for specific TFs, resolving gene symbols to JASPAR Matrix IDs, or getting TF metadata. Supports multiple output formats (MEME, TRANSFAC, PFM, JASPAR, YAML).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\jaspar_database\SKILL.md`

### `ncbi-sequence-fetch`
Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports direct accession lookup, CDS translation, gene+organism search, locus lookup, PubMed-linked sequences, patent protein extraction, and organism+length fallback search. Use when you need to fetch biological sequences by accession, gene name, locus tag, PubMed ID, or patent number.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\ncbi_sequence_fetch\SKILL.md`

### `quickgo-database`
Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need to map genes to biological processes, molecular functions, or cellular components, find genes associated with a specific pathway/GO term, or explore the Gene Ontology hierarchy. Do not use for querying drug targets (use OpenTargets) or mechanistic signaling pathway diagrams (use KEGG).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\quickgo_database\SKILL.md`

### `ucsc-conservation-and-tfbs`
Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser. Use when analyzing whether genomic variants or regions are evolutionarily conserved, functionally important, or bounded by TF regulators across major projects (ENCODE, JASPAR, ReMap).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\ucsc_conservation_and_tfbs\SKILL.md`

### `unibind-database`
Queries the UniBind database for experimentally validated transcription factor (TF) binding sites. Use when retrieving direct TF-DNA interaction datasets, downloading binding site coordinates (BED/FASTA) for local analysis, or listing available datasets by species, cell line, or TF name. Don't use to query specific intervals, locations, genes, motif models or expression data.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\unibind_database\SKILL.md`

## Drug Discovery & Pharmacology (6 skills)

### `chembl-database`
Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures. Use when the user asks about compounds, targets, IC50/Ki values, drug mechanisms, or structure searches.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\chembl_database\SKILL.md`

### `clinical-trials-database`
Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, drug, location, status, or phase; retrieve trial details by NCT ID; check eligibility/inclusion criteria; count trials across conditions or time periods; identify a sponsor's trial portfolio; find recruiting trials for patient matching.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\clinical_trials_database\SKILL.md`

### `openfda-database`
Query, search, and download data from the openFDA API for drugs, devices, foods, tobacco, cosmetics, animal and veterinary products, substances, and transparency data. Use for FDA adverse events, recalls, labeling, approvals, shortages, 510(k) clearances, NDC lookups, and any FDA safety or regulatory data query across all 28 API endpoints.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\openfda_database\SKILL.md`

### `opentargets-database`
Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeutic target identification.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\opentargets_database\SKILL.md`

### `pubchem-database`
Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics. Use when a user asks about a specific chemical, drug, or molecule.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pubchem_database\SKILL.md`

### `reactome-database`
Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment, retrieving results by token, finding unmapped or not-found identifiers, mapping identifiers, reaction participants (inputs, outputs), pathway hierarchy (including top-level pathways), diagram export, cross-reference mapping, or searching the knowledgebase.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\reactome_database\SKILL.md`

## Literature & Knowledge Retrieval (7 skills)

### `embl-ebi-ols`
Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions, and hierarchies across 250+ ontologies (e.g., GO, DOID, HP). Use when the user asks to search for terms, retrieve details, navigate hierarchies (parents, children, ancestors), look up properties and individuals, get autocomplete suggestions, or access ontology metadata and statistics.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\embl_ebi_ols\SKILL.md`

### `literature-search-arxiv`
Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstracts, and download full-text PDFs or HTML versions of papers. Use when the user asks to find research papers, literature, or specific arXiv IDs.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_arxiv\SKILL.md`

### `literature-search-biorxiv`
Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and medRxiv. Supports fetching paper metadata by DOI, and browsing by date range with category and keyword filters. Keyword filtering is local, so date ranges MUST be narrow (1-4 weeks) with a category to prevent timeouts.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_biorxiv\SKILL.md`

### `literature-search-europepmc`
Search Europe PMC for scientific literature and download open-access full texts and PDFs. Retrieve full-text XML/plain text by PMCID, get citation lists and bibliography.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_europepmc\SKILL.md`

### `literature-search-openalex`
Query the OpenAlex scholarly database for research papers, authors, institutions, topics, sources, publishers, funders, geo-locations, and keywords. Use when searching academic papers, resolving DOIs, downloading open-access PDFs, finding an author's publications, aggregating bibliometric data (citation counts, h-index, impact factor), exploring the research taxonomies, or performing DOI lookups.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\literature_search_openalex\SKILL.md`

### `predictingthepast`
Ancient text restoration, attribution, dating, contextualization, and embedding via Aeneas (Latin) / Ithaca (Ancient Greek). Use when asked to "restore", "attribute", "date", "contextualize", "find parallels", "where was it written", "when was it written", "embed", or "analyze" an ancient text, inscription, or epigraphic document, or when the user mentions "Aeneas", or "Ithaca".

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\predictingthepast\SKILL.md`

### `pubmed-database`
Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text. Link published research to biological databases (gene, protein, nucleotide, PubChem) to discover associations between papers and specific compounds or genes. Verify medical spelling, match raw citations, and cache result sets for bulk processing. Interfaces NCBI E-utilities and PMC BioC APIs.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\pubmed_database\SKILL.md`

## Developer Workflows & Automation (5 skills)

### `android-cli`
Provides instructions for installing and using the `android` CLI. The `android` command-line tool is a critical tool for Android development and helps you create new Android projects, run Android apps on devices, manage and interact with Android virtual devices (including screenshots and UI inspection), manage Android SDK components, look up official Android documentation, and discover and install official Android skills.

- Source: `C:\Users\chase\.gemini\config\plugins\android-cli-plugin\skills\SKILL.md`

### `automation`
Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an automated or recurring scheduled task (e.g. "summarize my emails every morning", "every Monday send me a to-do list"). Also triggered by the /automation slash command.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\automation\SKILL.md`

### `migrate-workflows`
Automatically migrate legacy workflows to modern skills across global and workspace configurations. Scans for existing workflows, creates target SKILL.md files, and safely archives old workflow files.

- Source: `C:\Users\chase\.gemini\antigravity\builtin\skills\migrate-workflows\SKILL.md`

### `uv`
Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH. Use when another skill requires uv as a prerequisite.

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\uv\SKILL.md`

### `workflow-skill-creator`
Distills a completed user workflow or interaction into a reusable agent skill. Use when the user asks to turn their workflow, interaction, or multi-step process into a skill, or when they say "make this a skill", "create a skill from what we just did", "package this workflow" or similar. Do not use for creating skills from scratch without an existing workflow (use a generic skill-creator for that).

- Source: `C:\Users\chase\.gemini\config\plugins\science\skills\workflow_skill_creator\SKILL.md`

