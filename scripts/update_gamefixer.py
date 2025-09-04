import json

# Rutas relativas desde gamefixer/
stats_path = "data/stats.json"                      # stats.json está dentro de gamefixer
scripts_path = "../plujin-manager/assets/scripts.json"  # scripts.json está en el otro repo

# Cargar stats.json
with open(stats_path, "r", encoding="utf-8") as f:
    stats = json.load(f)

# Cargar scripts.json
with open(scripts_path, "r", encoding="utf-8") as f:
    scripts = json.load(f)

# Buscar entrada de GameFixer.lua
gamefixer = None
for mod in scripts.get("mods", []):
    if mod.get("name") == "GameFixer.lua":
        gamefixer = mod
        break

if gamefixer:
    # Actualizar campos
    gamefixer["total_downloads"] = stats.get("total_downloads")
    gamefixer["created"] = stats.get("created")
    gamefixer["last_update"] = stats.get("last_update")
    gamefixer["latest_version"] = stats.get("latest_version")
else:
    # Si no existe, agregarlo como nuevo
    scripts["mods"].append({
        "name": "GameFixer.lua",
        "description": "",
        "author": "vxnzz",
        "downloads": 0,
        "url": "https://github.com/samp-comunity/gamefixer/releases/latest/download/GameFixer.lua",
        "icon": "https://raw.githubusercontent.com/samp-comunity/plujin-manager/refs/heads/master/assets/icons/gamefixer.png",
        "tags": ["Legal", "Utilidad"],
        "total_downloads": stats.get("total_downloads"),
        "created": stats.get("created"),
        "last_update": stats.get("last_update"),
        "latest_version": stats.get("latest_version"),
    })

# Guardar de nuevo en plujin-manager
with open(scripts_path, "w", encoding="utf-8") as f:
    json.dump(scripts, f, indent=2, ensure_ascii=False)

print("✅ scripts.json actualizado con datos de GameFixer")
