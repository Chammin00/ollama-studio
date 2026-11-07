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

def categorize_skills(skills):
    categories = {
        "Platform & Customizations": [],
        "Structural Biology & Molecular Modeling": [],
        "Genomics & Variant Impact": [],
        "Cheminformatics & Computational Chemistry": [],
        "Drug Discovery & Pharmacology": [],
        "Literature & Knowledge Retrieval": [],
        "Developer Workflows & Automation": [],
        "Media & Audience Strategy": []
    }
    
    for name, data in sorted(skills.items()):
        n = name.lower()
        d = data["description"].lower()
        
        # Match by specific skill name identity first for precision
        if any(k in n for k in ["cheminformatics", "rdkit"]):
            categories["Cheminformatics & Computational Chemistry"].append(data)
        elif any(k in n for k in ["youtube", "media", "retention", "audience", "video", "content"]):
            categories["Media & Audience Strategy"].append(data)
        elif any(k in n for k in ["literature", "arxiv", "biorxiv", "europepmc", "openalex", "pubmed", "predictingthepast", "ols"]):
            categories["Literature & Knowledge Retrieval"].append(data)
        elif any(k in n for k in ["alphafold", "pymol", "pdb", "foldseek", "biomolecular", "protein", "msa", "interpro", "string", "uniprot"]):
            categories["Structural Biology & Molecular Modeling"].append(data)
        elif any(k in n for k in ["variant", "genome", "genomic", "clinvar", "dbsnp", "gnomad", "gtex", "encode", "ucsc", "jaspar", "unibind", "ensembl", "ncbi-sequence", "quickgo"]):
            categories["Genomics & Variant Impact"].append(data)
        elif any(k in n for k in ["chembl", "pubchem", "fda", "opentargets", "reactome", "clinical-trial"]):
            categories["Drug Discovery & Pharmacology"].append(data)
        elif any(k in n for k in ["automation", "android", "workflow", "uv", "compose", "script", "practice", "powershell", "bash", "slop", "craftsman", "layout", "fullscreen", "simulation", "primer"]):
            categories["Developer Workflows & Automation"].append(data)
        elif any(k in n for k in ["agy", "antigravity", "customization", "plugin", "generative_ui", "credentials", "permissioned-github", "ui-extension"]):
            categories["Platform & Customizations"].append(data)
        # Fallback keyword matching on description
        elif any(k in d for k in ["cheminformatics", "rdkit", "molecular dynamics", "autodock vina", "smarts"]):
            categories["Cheminformatics & Computational Chemistry"].append(data)
        elif any(k in d for k in ["youtube", "retention", "thumbnail", "audiences", "click-through"]):
            categories["Media & Audience Strategy"].append(data)
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
            desc = item["description"] or "Advanced domain skill"
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
            frontier = p.get("frontier", "")
            action = p.get("action", "")
            lines.append(f"- **{name}** [{stack}]: {frontier} (Immediate target: {action})")
            
    lines.append("\n## OPERATIONAL GUIDELINES & PROBLEM SOLVING METHODOLOGY:")
    lines.append("1. **Deep Scientific, Cheminformatics & Genomic Precision**: When assisting with bioinformatics and cheminformatics (PDB, AlphaFold, Boltz-2, UniProt, ClinVar, gnomAD, ChEMBL, RDKit, AutoDock Vina, OpenMM), reference standard identifier formats, coordinate conventions (1-based vs 0-based), valid SMILES/SMARTS notation, stereochemical integrity, and robust molecular validation protocols.")
    lines.append("2. **System & Automation Mastery**: Provide complete, production-ready code, commands, and scheduled automation patterns. Adhere strictly to enterprise production standards for Bash/RHEL (set -euo pipefail, variable quoting, parameter expansions, trap cleanup) and modern PowerShell (CmdletBinding, pipeline architecture, strongly-typed PSCustomObjects, cross-version compatibility).")
    lines.append("3. **Anti-Slop Craftsmanship & Code Quality**: Eliminate low-effort AI hallmarks across all 8 community anti-patterns: emoji asset flips, hallucinated purple prose, shovelware ad-traps, shallow dilution, zero kinesthetics, sub-48dp touch targets, video/audio SFX brainrot, and sterile CGI plastic renders. Enforce handcrafted organic linework/watercolor textures, cel-shaded WebGL, audio soundboard limits (<=1 subtle cue per 30-45s, -14 to -16 LUFS voiceover), pure gameplay/utility loops, and WCAG AAA ergonomics (minimum 48x48dp touch targets).")
    lines.append("4. **Zero-Trust Security & Containment**: Ingest and enforce the 5-layer Aegis-AI defense matrix (strict AST schema validation, microVM kernel independence, DNS egress filtering, recursion limits, and scoped MCP tokens).")
    lines.append("5. **Content Strategy & Retention Engineering**: Apply elite video packaging mechanics (CTR/AVD optimization, curiosity gaps, loss aversion, pattern interrupts, and session-time retention bridges) when developing technical tutorials, media, or documentation.")
    lines.append("6. **Enterprise UI Architecture & Interactive Simulation Engines**: Architect full-screen (100vw x 100vh) enterprise web layouts with collapsible left navigation rails, top command search palettes (Ctrl+K), zero dead margin space, and dockable right inspector panels using crisp 1px borders and High-Gloss Lacquer physical optics. Build step-by-step interactive traffic and packet journey simulators and self-grading architecture drill engines with fuzzy matching, visual hint hierarchies, and speech feedback.")
    lines.append("7. **Actionable Insights**: Provide direct answers, synthesized reasoning, and actionable code blocks with zero unnecessary fluff.")
    
    return "\n".join(lines)

def sync(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
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
PARAMETER num_ctx 8192

SYSTEM """{system_prompt}"""
'''
    modelfile_path = output_dir / "Modelfile"
    modelfile_path.write_text(modelfile_content, encoding="utf-8")
    print(f"Generated Modelfile at {modelfile_path}")
    
    # Run ollama create
    print("Building Ollama model 'antigravity-skills:latest' with updated skills & projects...")
    try:
        res = subprocess.run(
            ["ollama", "create", "antigravity-skills", "-f", str(modelfile_path)],
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
