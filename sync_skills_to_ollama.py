import os
import re
import json
import subprocess
from pathlib import Path

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
        Path(r"C:\Users\chase\.gemini\antigravity\builtin\skills"),
        Path(r"C:\Users\chase\.gemini\config\plugins"),
        Path(r"C:\Users\chase\.gemini\antigravity\cache\marketplaces"),
        Path(r"C:\Users\chase\.gemini\skills"),
        Path(r"C:\Users\chase\.gemini\antigravity\skills")
    ]
    
    skills = {}
    for base in search_dirs:
        if not base.exists():
            continue
        for p in base.rglob("SKILL.md"):
            skill_name = p.parent.name
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
                meta, body = extract_frontmatter(content)
                name = meta.get("name", skill_name)
                desc = meta.get("description", "")
                
                # Deduplicate: prefer config/builtin over cache
                if name not in skills or "cache" not in str(p):
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

def categorize_skills(skills):
    categories = {
        "Platform & Customizations": [],
        "Structural Biology & Molecular Modeling": [],
        "Genomics & Variant Impact": [],
        "Drug Discovery & Pharmacology": [],
        "Literature & Knowledge Retrieval": [],
        "Developer Workflows & Automation": []
    }
    
    for name, data in sorted(skills.items()):
        n = name.lower()
        d = data["description"].lower()
        
        # Match by specific skill name identity first for precision
        if any(k in n for k in ["literature", "arxiv", "biorxiv", "europepmc", "openalex", "pubmed", "predictingthepast", "ols"]):
            categories["Literature & Knowledge Retrieval"].append(data)
        elif any(k in n for k in ["alphafold", "pymol", "pdb", "foldseek", "biomolecular", "protein", "msa", "interpro", "string", "uniprot"]):
            categories["Structural Biology & Molecular Modeling"].append(data)
        elif any(k in n for k in ["variant", "genome", "genomic", "clinvar", "dbsnp", "gnomad", "gtex", "encode", "ucsc", "jaspar", "unibind", "ensembl", "ncbi-sequence", "quickgo"]):
            categories["Genomics & Variant Impact"].append(data)
        elif any(k in n for k in ["chembl", "pubchem", "fda", "opentargets", "reactome", "clinical-trial"]):
            categories["Drug Discovery & Pharmacology"].append(data)
        elif any(k in n for k in ["automation", "android", "workflow", "uv", "compose"]):
            categories["Developer Workflows & Automation"].append(data)
        elif any(k in n for k in ["agy", "antigravity", "customization", "plugin", "generative_ui", "credentials", "permissioned-github", "ui-extension"]):
            categories["Platform & Customizations"].append(data)
        # Fallback keyword matching on description
        elif any(k in d for k in ["alphafold", "pymol", "pdb", "foldseek", "biomolecular", "protein"]):
            categories["Structural Biology & Molecular Modeling"].append(data)
        elif any(k in d for k in ["variant", "genome", "genomic", "clinvar", "dbsnp", "gnomad", "gtex", "encode", "ucsc", "jaspar", "unibind"]):
            categories["Genomics & Variant Impact"].append(data)
        elif any(k in d for k in ["chembl", "pubchem", "target", "pharmacology", "drug"]):
            categories["Drug Discovery & Pharmacology"].append(data)
        elif any(k in d for k in ["literature", "paper", "preprint"]):
            categories["Literature & Knowledge Retrieval"].append(data)
        elif any(k in d for k in ["automation", "android", "plugin", "workflow"]):
            categories["Developer Workflows & Automation"].append(data)
        else:
            categories["Platform & Customizations"].append(data)
            
    return categories

def build_system_prompt(skills, categories):
    lines = [
        "You are Antigravity-Ollama, an elite autonomous AI developer and scientific research intelligence platform.",
        "You possess comprehensive specialized knowledge, workflow protocols, and acquired skills across software engineering, bioinformatics, molecular modeling, genomics, drug discovery, and agentic automation.",
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
            
    lines.append("\n## OPERATIONAL GUIDELINES & PROBLEM SOLVING METHODOLOGY:")
    lines.append("1. **Deep Scientific & Technical Precision**: When assisting with bioinformatics (PDB, AlphaFold, UniProt, ClinVar, gnomAD, ChEMBL), reference standard identifier formats, coordinate conventions (1-based vs 0-based), and validation protocols.")
    lines.append("2. **System & Automation Mastery**: Provide complete, production-ready code, commands, and scheduled automation patterns.")
    lines.append("3. **Actionable Insights**: Provide direct answers, synthesized reasoning, and actionable code blocks with zero unnecessary fluff.")
    
    return "\n".join(lines)

def sync(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    print("Discovering skills...")
    skills = find_skills()
    print(f"Found {len(skills)} unique skills.")
    
    categories = categorize_skills(skills)
    
    # Save JSON database
    kb_json = output_dir / "skills_knowledge_base.json"
    with open(kb_json, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2)
    print(f"Saved skills database to {kb_json}")
    
    # Save Markdown digest
    kb_md = output_dir / "skills_directory.md"
    with open(kb_md, "w", encoding="utf-8") as f:
        f.write("# Antigravity Acquired Skills Digest\n\n")
        for cat, items in categories.items():
            f.write(f"## {cat} ({len(items)} skills)\n\n")
            for item in items:
                f.write(f"### `{item['name']}`\n")
                f.write(f"{item['description']}\n\n")
                f.write(f"- Source: `{item['path']}`\n\n")
    print(f"Saved skills directory to {kb_md}")
    
    # Generate Modelfile
    system_prompt = build_system_prompt(skills, categories)
    # Choose base model: prefer llama3:latest if present, else deepseek-r1:7b
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
    print("Building Ollama model 'antigravity-skills:latest'...")
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
        print("Successfully fed all skills to Ollama as model 'antigravity-skills'!")
    except Exception as e:
        print("Failed to run ollama create:", e)
        if hasattr(e, 'stderr'):
            print("Stderr:", e.stderr)

if __name__ == "__main__":
    work_dir = Path(r"G:\My Drive\Antigravity\Projects\ollama")
    sync(work_dir)
