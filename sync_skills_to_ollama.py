import os
import re
import sys
import json
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def extract_frontmatter(content):
    meta = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].strip()
            current_key = None
            multiline_val = []
            
            for line in fm_text.splitlines():
                if line and not line.startswith(" ") and not line.startswith("\t") and ":" in line:
                    if current_key:
                        val_str = " ".join([v.strip() for v in multiline_val if v.strip()]).strip()
                        if val_str:
                            meta[current_key] = val_str
                        multiline_val = []
                    key, val = line.split(":", 1)
                    current_key = key.strip()
                    val = val.strip().strip("'\"")
                    if val in [">", ">-", "|", "|-"]:
                        multiline_val = []
                    else:
                        multiline_val = [val] if val else []
                elif current_key and (line.startswith(" ") or line.startswith("\t")):
                    multiline_val.append(line.strip())
            
            if current_key and multiline_val:
                val_str = " ".join([v.strip() for v in multiline_val if v.strip()]).strip()
                meta[current_key] = val_str
    return meta, body

def find_skills():
    search_dirs = [
        Path(r"C:\Users\chase\.gemini\config\skills"),
        Path(r"C:\Users\chase\.gemini\config\plugins"),
        Path(r"C:\Users\chase\.gemini\config"),
        Path(r"C:\Users\chase\.gemini\skills"),
        Path(r"C:\Users\chase\.gemini\antigravity\skills"),
        Path(r"C:\Users\chase\.gemini\antigravity\builtin\skills"),
        Path(r"C:\Users\chase\.gemini\antigravity\cache\marketplaces"),
        Path(r"C:\Users\chase\.gemini")
    ]
    
    skills = {}
    for base in search_dirs:
        if not base.exists():
            continue
        for p in base.rglob("SKILL.md"):
            # Avoid conversation transcripts and scratch files
            if "brain" in p.parts or "scratch" in p.parts:
                continue
            skill_name = p.parent.name
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
                meta, body = extract_frontmatter(content)
                name = meta.get("name", skill_name)
                desc = meta.get("description", "")
                
                # Deduplicate: first discovered wins based on search_dirs priority
                # (config/skills > config/plugins > builtin > cache > root)
                if name not in skills:
                    skills[name] = {
                        "name": name,
                        "folder": skill_name,
                        "path": str(p),
                        "description": desc,
                        "body_preview": body[:1200]
                    }
            except Exception as e:
                print(f"Error reading {p}: {e}")
    return skills

def find_antigravity_projects():
    """Scans all Antigravity projects and ingests their active architectures, stack, and latest blueprints."""
    projects_root = Path(r"G:\My Drive\Antigravity\Projects")
    refinement_dir = projects_root / "project refinement"
    catalog_path = refinement_dir / "PROJECT_CATALOG_AND_ACTION_MATRIX.md"
    
    projects = {}
    
    # 1. Ingest from Action Matrix table if present
    if catalog_path.exists():
        try:
            text = catalog_path.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                if line.startswith("| [") and "|" in line:
                    parts = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts) >= 6:
                        name_m = re.search(r"\[(.*?)\]", parts[0])
                        p_name = name_m.group(1) if name_m else parts[0]
                        if (
                            p_name.startswith(".")
                            or p_name.lower().startswith("new folder")
                            or "cache" in p_name.lower()
                        ):
                            continue
                        p_cat = parts[1]
                        p_stack = parts[2]
                        p_status = parts[3]
                        p_frontier = parts[4]
                        p_action = parts[5]
                        projects[p_name] = {
                            "name": p_name,
                            "category": p_cat,
                            "stack": p_stack,
                            "status": p_status,
                            "frontier": p_frontier,
                            "action": p_action
                        }
        except Exception as e:
            print(f"Error reading project catalog: {e}")
            
    # 2. Add or supplement recent new directories (agent 365, ai defense, MCP, etc.)
    new_projects = {
        "agent 365": {
            "name": "agent 365",
            "category": "Enterprise AI / Productivity",
            "stack": "FastAPI, Python 3.12, Vanilla JS, Anti-Slop, High-Gloss Lacquer",
            "status": "Active",
            "frontier": "1-to-1 authentic Microsoft 365 Web Suite replica (Word, Excel with formula engine, PowerPoint with slide show runner, Outlook, Teams, OneDrive, multi-agent Copilot orchestrator), zero-slop UI standards.",
            "action": "Ensure full cross-application agentic task execution and formula bar state preservation."
        },
        "ai defense": {
            "name": "ai defense",
            "category": "AI Security / Zero Trust",
            "stack": "Python, HTTP Server, High-Gloss Lacquer, Vector SVGs",
            "status": "Active",
            "frontier": "Aegis-AI Defense Matrix: 5-layer containment preventing autonomous agent breakouts, indirect prompt injection AST gates, gVisor/Firecracker microVM isolation, DNS egress whitelisting, ephemeral cgroup PIDs limits, zero-trust MCP proxies.",
            "action": "Connect live telemetry simulator to container enforcement hooks and audit test suites."
        },
        "MCP": {
            "name": "MCP",
            "category": "Architecture / Integrations",
            "stack": "Model Context Protocol, JSON-RPC, Node.js, Python",
            "status": "Active",
            "frontier": "Unified global Antigravity MCP Hub coordinating Google Drive filesystem tools, Ollama local inference endpoint, GitHub automation, and Puppeteer browser scraping.",
            "action": "Maintain server heartbeat monitoring and expand tool calling bounds."
        }
    }
    
    for k, v in new_projects.items():
        if k not in projects:
            projects[k] = v
            
    # Also discover any extra folders
    if projects_root.exists():
        for d in projects_root.iterdir():
            if (
                d.is_dir()
                and not d.name.startswith(".")
                and not d.name.lower().startswith("new folder")
                and d.name not in ["project refinement", "Plugins"]
            ):
                if d.name not in projects:
                    projects[d.name] = {
                        "name": d.name,
                        "category": "Antigravity Project",
                        "stack": "Native Workspace",
                        "status": "Active",
                        "frontier": f"Workspace project in {d.name}",
                        "action": "Active development and maintenance"
                    }
                    
    return projects

def clean_desc(desc, max_len=180):
    if not desc:
        return "Advanced domain skill"
    d = " ".join(desc.strip().splitlines())
    if ". " in d:
        first = d.split(". ")[0].strip() + "."
        if len(first) >= 30 and len(first) <= max_len:
            return first
    if len(d) > max_len:
        return d[:max_len-3].rstrip() + "..."
    return d

def ensure_ollama_running():
    import urllib.request
    try:
        with urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=2) as resp:
            if resp.status == 200:
                return True
    except Exception:
        pass
    
    print("Ollama server not detected on port 11434. Starting ollama serve...")
    try:
        ollama_bin = r"C:\Users\chase\AppData\Local\Programs\Ollama\ollama.exe"
        cmd = [ollama_bin, "serve"] if os.path.exists(ollama_bin) else ["ollama", "serve"]
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        import time
        for _ in range(40):
            time.sleep(1)
            try:
                with urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=1) as resp:
                    if resp.status == 200:
                        print("Ollama server started successfully.")
                        return True
            except Exception:
                pass
    except Exception as e:
        print(f"Failed to auto-start ollama serve: {e}")
    return False

def categorize_skills(skills):
    categories = {
        "Platform & Customizations": [],
        "Google Cloud & BigQuery Data Engineering": [],
        "Firebase & Backend Services": [],
        "Flutter & Mobile App Development": [],
        "Cloud Deployments & Serverless Architecture": [],
        "Graph Databases & Knowledge Graphs": [],
        "Design, UI/UX & Creative Engineering": [],
        "Browser Automation & Web DevTools": [],
        "Structural Biology & Molecular Modeling": [],
        "Genomics & Variant Impact": [],
        "Cheminformatics & Computational Chemistry": [],
        "Drug Discovery & Pharmacology": [],
        "Literature & Knowledge Retrieval": [],
        "Developer Workflows & Automation": [],
        "Media & Video Strategy": []
    }
    
    for name, data in sorted(skills.items()):
        n = name.lower()
        d = data["description"].lower()
        p = data.get("path", "").lower()
        
        # Priority matching by domain identity
        if any(k in n for k in ["cheminformatics", "rdkit"]):
            categories["Cheminformatics & Computational Chemistry"].append(data)
        elif any(k in n for k in ["youtube", "retention", "invideo", "higgsfield", "hyperframes", "magnific", "openedit", "remotion", "runway", "video"]):
            categories["Media & Video Strategy"].append(data)
        elif any(k in n for k in ["literature", "arxiv", "biorxiv", "europepmc", "openalex", "pubmed", "predictingthepast", "embl-ebi-ols"]):
            categories["Literature & Knowledge Retrieval"].append(data)
        elif any(k in n for k in ["alphafold", "pymol", "pdb", "foldseek", "biomolecular", "protein", "msa", "interpro", "string", "uniprot"]):
            categories["Structural Biology & Molecular Modeling"].append(data)
        elif any(k in n for k in ["variant", "genome", "genomic", "clinvar", "dbsnp", "gnomad", "gtex", "encode", "ucsc", "jaspar", "unibind", "ensembl", "ncbi-sequence", "quickgo"]):
            categories["Genomics & Variant Impact"].append(data)
        elif any(k in n for k in ["chembl", "pubchem", "openfda", "opentargets", "reactome", "clinical-trial"]):
            categories["Drug Discovery & Pharmacology"].append(data)
        elif any(k in n for k in ["neo4j", "cypher", "graphrag", "lookml", "looker"]):
            categories["Graph Databases & Knowledge Graphs"].append(data)
        elif any(k in n for k in ["bigquery", "bigframes", "bigtable", "dataform", "data-autocleaning", "gcp-", "gcs-", "discovering-gcp", "federate-lakehouse", "enforcing-resource", "gcloud", "google-cloud-storage", "google-cloud-recipe", "cloud-databases-onboarding", "building-data-apps", "finding-google-skills", "schema-mapping", "dak-setup", "resolving-mcp-region-configs", "gemini-api", "gemini-live", "gemini-omni", "retrieving-developer-knowledge", "google-developer-knowledge"]):
            categories["Google Cloud & BigQuery Data Engineering"].append(data)
        elif any(k in n for k in ["firebase", "firestore", "extension-to-functions-codebase"]):
            categories["Firebase & Backend Services"].append(data)
        elif any(k in n for k in ["flutter", "dart-", "android", "compose", "xcode"]):
            categories["Flutter & Mobile App Development"].append(data)
        elif any(k in n for k in ["chrome-devtools", "a11y-debugging", "cookie-debugging", "memory-leak-debugging", "troubleshooting", "puppeteer", "chrome-extensions"]):
            categories["Browser Automation & Web DevTools"].append(data)
        elif (any(k in n for k in ["figma", "canva", "wix", "mobbin", "redesign-screen", "plain-writing", "search", "generative_ui", "motion-craftsmanship"]) or "mobbin" in p) and "ml-best-practices" not in n:
            categories["Design, UI/UX & Creative Engineering"].append(data)
        elif any((k in n if k != "eve" else (n == "eve" or n.startswith("eve-") or n.endswith("-eve"))) for k in ["vercel", "netlify", "base44", "cdn-caching", "runtime-cache", "routing-middleware", "is-agentic", "chat-sdk", "ai-sdk", "flags-sdk", "env-vars", "domains", "bootstrap", "create-a-backend", "custom-metrics", "microfrontends", "modern-web-guidance", "react-best-practices", "debug-optimize-lcp", "auth", "auth0", "offload-to-sandbox", "deployments-cicd", "queues", "daemons", "ai-gateway", "eve", "build-agents", "knowledge-update"]):
            categories["Cloud Deployments & Serverless Architecture"].append(data)
        elif any(k in n for k in ["autofix", "code-review", "script-practice", "anti-slop", "enterprise-fullscreen", "interactive-simulation", "github-primer", "workflow", "uv", "automation", "managing-python-dependencies", "notebook-guidance", "generate-project-plan", "accidental-data-loss-prevention", "verification", "ml-best-practices", "permissioned-github", "google-maps-platform", "gdrive", "gcalendar", "gsheets", "gdocs", "credentials", "context7"]):
            categories["Developer Workflows & Automation"].append(data)
        # Fallback keyword matching on description
        elif any(k in d for k in ["cheminformatics", "rdkit", "molecular dynamics", "autodock vina", "smarts"]):
            categories["Cheminformatics & Computational Chemistry"].append(data)
        elif any(k in d for k in ["youtube", "retention", "thumbnail", "audiences", "click-through"]):
            categories["Media & Video Strategy"].append(data)
        elif any(k in d for k in ["alphafold", "pymol", "pdb", "foldseek", "biomolecular", "protein"]):
            categories["Structural Biology & Molecular Modeling"].append(data)
        elif any(k in d for k in ["variant", "genome", "genomic", "clinvar", "dbsnp", "gnomad", "gtex", "encode", "ucsc", "jaspar", "unibind"]):
            categories["Genomics & Variant Impact"].append(data)
        elif any(k in d for k in ["chembl", "pubchem", "target", "pharmacology", "drug"]):
            categories["Drug Discovery & Pharmacology"].append(data)
        elif any(k in d for k in ["literature", "paper", "preprint"]):
            categories["Literature & Knowledge Retrieval"].append(data)
        elif any(k in d for k in ["automation", "android", "plugin", "workflow", "scripting", "powershell", "bash", "linux", "rhel", "slop", "craftsman", "layout", "fullscreen", "simulation", "simulator"]):
            categories["Developer Workflows & Automation"].append(data)
        else:
            categories["Platform & Customizations"].append(data)
            
    return categories

def build_system_prompt(skills, categories, projects):
    lines = [
        "You are Antigravity-Ollama, an elite autonomous AI developer, scientific research intelligence platform, and master architect of the Antigravity Projects ecosystem.",
        "You possess comprehensive specialized knowledge, workflow protocols, and acquired skills across software engineering, bioinformatics, molecular modeling, genomics, cheminformatics, drug discovery, agentic automation, cybersecurity, and full-stack systems engineering.",
        "",
        "## CORE EXPERTISE & ACQUIRED SKILLS DIRECTORY:"
    ]
    
    for cat, items in categories.items():
        if not items:
            continue
        lines.append(f"\n### {cat}")
        for item in items:
            desc = clean_desc(item["description"])
            lines.append(f"- **{item['name']}**: {desc}")
            
    # Append Live Antigravity Projects Knowledge
    lines.append("\n## ANTIGRAVITY PROJECTS & ARCHITECTURE ECOSYSTEM:")
    lines.append(f"You have deep operational awareness and architectural mastery over all {len(projects)} active projects in 'G:\\My Drive\\Antigravity\\Projects':\n")
    
    # Group projects by category
    proj_by_cat = {}
    for p in projects.values():
        cat = p.get("category", "General")
        proj_by_cat.setdefault(cat, []).append(p)
        
    for cat, p_list in sorted(proj_by_cat.items()):
        lines.append(f"### {cat}")
        for p in sorted(p_list, key=lambda x: x["name"]):
            name = p["name"]
            stack = p.get("stack", "Universal")
            frontier = clean_desc(p.get("frontier", ""), max_len=200)
            action = clean_desc(p.get("action", ""), max_len=140)
            lines.append(f"- **{name}** [{stack}]: {frontier} (Immediate target: {action})")
            
    lines.append("\n## OPERATIONAL GUIDELINES & PROBLEM SOLVING METHODOLOGY:")
    lines.append("1. **Deep Scientific, Cheminformatics & Genomic Precision**: When assisting with bioinformatics and cheminformatics (PDB, AlphaFold, Boltz-2, UniProt, ClinVar, gnomAD, ChEMBL, RDKit, AutoDock Vina, OpenMM), reference standard identifier formats, coordinate conventions (1-based vs 0-based), valid SMILES/SMARTS notation, stereochemical integrity, and robust molecular validation protocols.")
    lines.append("2. **Google Cloud, BigQuery & Dataform Engineering**: Architect scalable, idempotent ELT pipelines using BigQuery DataFrames (BigFrames), Dataform, Cloud Storage FUSE, Cloud Composer (Airflow), and Spark. Apply mandatory resource attribution labels to bq operations and optimize slot utilization.")
    lines.append("3. **Firebase & Backend Architecture**: Enforce declarative Firestore security rules, Firebase Auth flows, Cloud Functions v2 triggers, and Firebase Data Connect PostgreSQL backends with strict type safety.")
    lines.append("4. **Flutter & Mobile App Engineering**: Implement clean layered architectures (UI, Logic, Data), declarative routing with go_router, primary constructor syntax, package:checks testing, WCAG accessibility standards, and Android Compose previews.")
    lines.append("5. **Cloud Deployments, Serverless & Edge Systems**: Deploy robust Vercel and Netlify systems utilizing Edge functions, AI SDK, durable workflows, CDN caching/revalidation policies, zero-trust middleware, and automated CI/CD verification.")
    lines.append("6. **Graph Databases & GraphRAG**: Construct high-performance Neo4j Cypher queries, vector indexes, and GraphRAG retrieval patterns. Ingest LookML models with semantic explorations, liquid variables, and access grants.")
    lines.append("7. **Design Systems & Creative Engineering**: Seamlessly bridge design and code using Figma Code Connect, custom shaders, Canva Brand Kits, and Wix headless design systems with pixel-perfect responsive execution.")
    lines.append("8. **Browser Automation & DevTools Diagnostics**: Audit web performance, memory leak profiles, cookie/session configurations, and accessibility trees via Chrome DevTools protocol and Puppeteer automation.")
    lines.append("9. **Enterprise Scripting & Automation Mastery**: Provide complete, production-ready code, commands, and scheduled automation patterns. Adhere strictly to enterprise production standards for Bash/RHEL (set -euo pipefail, variable quoting, parameter expansions, trap cleanup) and modern PowerShell (CmdletBinding, pipeline architecture, strongly-typed PSCustomObjects, cross-version compatibility).")
    lines.append("10. **Anti-Slop Craftsmanship & Code Quality**: Eliminate low-effort AI hallmarks across all 8 community anti-patterns: emoji asset flips, hallucinated purple prose, shovelware ad-traps, shallow dilution, zero kinesthetics, sub-48dp touch targets, video/audio SFX brainrot, and sterile CGI plastic renders. Enforce handcrafted organic linework/watercolor textures, cel-shaded WebGL, audio soundboard limits (<=1 subtle cue per 30-45s, -14 to -16 LUFS voiceover), pure gameplay/utility loops, and WCAG AAA ergonomics (minimum 48x48dp touch targets).")
    lines.append("11. **Zero-Trust Security & Containment**: Ingest and enforce the 5-layer Aegis-AI defense matrix (strict AST schema validation, microVM kernel independence, DNS egress filtering, recursion limits, and scoped MCP tokens).")
    lines.append("12. **Content Strategy & Retention Engineering**: Apply elite video packaging mechanics (CTR/AVD optimization, curiosity gaps, loss aversion, pattern interrupts, and session-time retention bridges) when developing technical tutorials, media, or documentation.")
    lines.append("13. **Enterprise Fullscreen Layouts**: Architect full-screen (100vw x 100vh) enterprise web layouts with collapsible left navigation rails, top command search palettes (Ctrl+K), zero dead margin space, and dockable right inspector panels using crisp 1px borders and High-Gloss Lacquer physical optics.")
    lines.append("14. **Actionable Insights**: Provide direct answers, synthesized reasoning, and actionable code blocks with zero unnecessary fluff.")
    lines.append("15. **Motion Craftsmanship & Anti-Slop Motion**: Enforce tactile, spring-driven 60 FPS motion across all web and mobile interfaces. Eliminate floaty 0.3s ease-in-out transitions, janky max-height animations, and lifeless button clicks. Standardize on critically damped springs (stiffness: 400, damping: 30), Apple-grade quintic beziers (cubic-bezier(0.16, 1, 0.3, 1)), staggered kinetic reveals with blur-up, and zero-jank sliding layoutId indicators synthesized from getlayers.ai, 60fps.design, motion-primitives.com, kinetics.colorion.co, and microkit.co.")
    
    return "\n".join(lines)

def sync(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    ensure_ollama_running()
    print("Discovering skills...")
    skills = find_skills()
    print(f"Found {len(skills)} unique skills.")
    
    print("Ingesting Antigravity projects catalog & blueprints...")
    projects = find_antigravity_projects()
    print(f"Loaded {len(projects)} active Antigravity projects.")
    
    categories = categorize_skills(skills)
    
    # Save Skills JSON database
    kb_json = output_dir / "skills_knowledge_base.json"
    with open(kb_json, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2)
    print(f"Saved skills database to {kb_json}")
    
    # Save Projects JSON database
    proj_json = output_dir / "projects_knowledge_base.json"
    with open(proj_json, "w", encoding="utf-8") as f:
        json.dump(projects, f, indent=2)
    print(f"Saved projects database to {proj_json}")
    
    # Save Unified Knowledge Markdown digest
    kb_md = output_dir / "skills_directory.md"
    with open(kb_md, "w", encoding="utf-8") as f:
        f.write("# Antigravity Acquired Skills & Projects Ecosystem Digest\n\n")
        f.write(f"Updated: {len(skills)} Acquired Skills | {len(projects)} Production Projects\n\n")
        
        f.write("## 📦 Part 1: Acquired Agent Skills Catalog\n\n")
        for cat, items in categories.items():
            f.write(f"### {cat} ({len(items)} skills)\n\n")
            for item in items:
                f.write(f"#### `{item['name']}`\n")
                f.write(f"{item['description']}\n\n")
                f.write(f"- Source: `{item['path']}`\n\n")
                
        f.write("\n## 🚀 Part 2: Active Antigravity Projects Catalog\n\n")
        for name, p in sorted(projects.items()):
            f.write(f"### `{p['name']}` ({p.get('category', 'General')})\n")
            f.write(f"- **Stack**: `{p.get('stack', 'Native')}`\n")
            f.write(f"- **Status**: `{p.get('status', 'Active')}`\n")
            f.write(f"- **Frontier Architecture**: {p.get('frontier', 'N/A')}\n")
            f.write(f"- **Target Action**: {p.get('action', 'N/A')}\n\n")
            
    print(f"Saved comprehensive directory to {kb_md}")
    
    # Generate Modelfile
    system_prompt = build_system_prompt(skills, categories, projects)
    base_model = "llama3:latest"
    
    modelfile_content = f'''FROM {base_model}

PARAMETER temperature 0.5
PARAMETER top_p 0.9
PARAMETER num_ctx 32768

SYSTEM """{system_prompt}"""
'''
    modelfile_path = output_dir / "Modelfile"
    modelfile_path.write_text(modelfile_content, encoding="utf-8")
    print(f"Generated Modelfile at {modelfile_path}")
    
    # Run ollama create
    print("Building Ollama model 'antigravity-skills:latest' with updated skills & projects...")
    try:
        ollama_cmd = r"C:\Users\chase\AppData\Local\Programs\Ollama\ollama.exe" if os.path.exists(r"C:\Users\chase\AppData\Local\Programs\Ollama\ollama.exe") else "ollama"
        res = subprocess.run(
            [ollama_cmd, "create", "antigravity-skills", "-f", str(modelfile_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True
        )
        print("Ollama create output:", res.stdout)
        print("Successfully fed all skills AND recent project changes to Ollama model 'antigravity-skills'!")
    except Exception as e:
        print("Failed to run ollama create:", e)
        if hasattr(e, 'stderr'):
            print("Stderr:", e.stderr)

if __name__ == "__main__":
    work_dir = Path(r"G:\My Drive\Antigravity\Projects\ollama")
    sync(work_dir)
