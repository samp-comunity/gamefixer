import requests, json

url = "https://api.github.com/repos/samp-comunity/gamefixer/releases"
r = requests.get(url)
releases = r.json()

stats = {
    "name": "gamefixer",
    "total_downloads": 0,
    "created": None,
    "last_update": None,
    "latest_version": None,
    "versions": []
}

for rel in releases:
    tag = rel.get("tag_name")
    downloads = sum(asset["download_count"] for asset in rel.get("assets", []))
    published_at = rel.get("published_at")

    stats["total_downloads"] += downloads
    stats["versions"].append({
        "tag": tag,
        "downloads": downloads,
        "date": published_at
    })

# releases viene ordenado (nuevo primero)
if releases:
    stats["latest_version"] = releases[0].get("tag_name")
    stats["last_update"] = releases[0].get("published_at")
    stats["created"] = releases[-1].get("published_at")  # el más viejo

with open("stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=4)


print("Estadisticas actulizadas")
